"""Build a starter draw.io world map for MaLAPA from Natural Earth land polygons.

usage: python -I build_map.py <ne_50m_land.geojson> <out_dir>
Writes: world-land.svg (land only), malapa_map.drawio, preview.svg
"""
import base64, html, json, math, sys
from pathlib import Path

src, out = Path(sys.argv[1]), Path(sys.argv[2])

W = 1447
LAND = "#3A8ACF"
OCEAN = "#3A8ACF"          # drawn at 18% opacity
INK = "#163B5A"            # pin outline + numbers (--malapa-blue-900)
LAT_N, LAT_S = 84.0, -57.0  # north Greenland .. just south of Cape Horn
LON_W, LON_E = -180.0, 180.0


def miller(lat):
    r = math.radians(max(min(lat, 89.9), -89.9))
    return 1.25 * math.log(math.tan(math.pi / 4 + 0.4 * r))


Y_N, Y_S = miller(LAT_N), miller(LAT_S)
SCALE = W / math.radians(LON_E - LON_W)
H = round((Y_N - Y_S) * SCALE)


def proj(lon, lat):
    x = (math.radians(lon - LON_W)) * SCALE
    y = (Y_N - miller(lat)) * SCALE
    return x, y


def dp(pts, eps):
    """Douglas-Peucker line simplification."""
    if len(pts) < 3:
        return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1
    norm = math.hypot(dx, dy)
    i_max, d_max = 0, 0.0
    for i in range(1, len(pts) - 1):
        x0, y0 = pts[i]
        if norm == 0:                 # closed ring: endpoints coincide
            d = math.hypot(x0 - x1, y0 - y1)
        else:
            d = abs(dy * x0 - dx * y0 + x2 * y1 - y2 * x1) / norm
        if d > d_max:
            i_max, d_max = i, d
    if d_max > eps:
        return dp(pts[: i_max + 1], eps)[:-1] + dp(pts[i_max:], eps)
    return [pts[0], pts[-1]]


def area(pts):
    return abs(sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]))) / 2


rings = []
for feat in json.loads(src.read_text())["features"]:
    g = feat["geometry"]
    polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
    for poly in polys:
        for ring in poly:
            if max(lat for _, lat in ring) < LAT_S:      # Antarctica etc.
                continue
            pts = dp([proj(lon, lat) for lon, lat in ring], 0.4)
            if len(pts) >= 4 and area(pts) >= 4:          # drop specks < 4 px²
                rings.append(pts)

d = " ".join("M" + " ".join(f"{x:.1f},{y:.1f}" for x, y in r) + "Z" for r in rings)
land_svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<path fill="{LAND}" fill-rule="evenodd" d="{d}"/></svg>')
(out / "world-land.svg").write_text(land_svg)

# Workshop pins: label, lat, lon, which way the label sits relative to the point
PINS = [
    ("1,7", 37.65, -122.2, "up"),     # SLAC Menlo Park (1) + LBNL Berkeley (7)
    ("2,5", 46.9, 7.2, "up"),         # PSI Villigen (2) + CERN Geneva (5)
    ("3", 41.88, -87.63, "up"),       # Chicago (BNL-hosted 2022)
    ("4", 35.86, 129.22, "left"),     # PAL, Gyeongju
    ("6", 34.95, 134.43, "right"),    # SPring-8, Himeji
]
PIN_H, PTR = 64, 20                   # label box height, pointer length


def pin_geometry(label, x, y, side):
    w = 64 if len(label) == 1 else 104
    h = PIN_H + PTR
    if side == "up":
        return x - w / 2, y - h, w, h, 0.5 - 10 / w, 0.5
    if side == "left":                # box to the left, tip at its bottom-right
        return x - w + 8, y - h, w, h, 1 - 36 / w, 1 - 8 / w
    return x - 8, y - h, w, h, 16 / w, 8 / w   # right: tip at bottom-left


cells, preview = [], []
cells.append(f'<mxCell id="ocean" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor={OCEAN};'
             f'fillOpacity=18;strokeColor=none;movable=0;resizable=0;" vertex="1" parent="1">'
             f'<mxGeometry width="{W}" height="{H}" as="geometry"/></mxCell>')
b64 = base64.b64encode(land_svg.encode()).decode()
cells.append(f'<mxCell id="land" value="" style="shape=image;verticalLabelPosition=bottom;verticalAlign=top;'
             f'imageAspect=0;aspect=fixed;image=data:image/svg+xml,{b64};movable=0;resizable=0;" '
             f'vertex="1" parent="1"><mxGeometry width="{W}" height="{H}" as="geometry"/></mxCell>')

for i, (label, lat, lon, side) in enumerate(PINS):
    x, y = proj(lon, lat)
    gx, gy, w, h, pos, pos2 = pin_geometry(label, x, y, side)
    style = (f"shape=callout;whiteSpace=wrap;html=1;perimeter=calloutPerimeter;rounded=1;arcSize=50;"
             f"size={PTR};base=20;position={pos:.3f};position2={pos2:.3f};"
             f"fillColor=#FFFFFF;strokeColor={INK};strokeWidth=4;"
             f"fontFamily=Helvetica;fontSize=34;fontStyle=1;fontColor={INK};spacingBottom={PTR};")
    cells.append(f'<mxCell id="pin{i}" value="{html.escape(label)}" style="{style}" vertex="1" parent="1">'
                 f'<mxGeometry x="{gx:.1f}" y="{gy:.1f}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    # preview: rounded box + pointer triangle
    bx, by = gx, gy
    tipx = gx + pos2 * w
    b0 = gx + pos * w
    preview.append(
        f'<path d="M{b0:.1f},{by + PIN_H:.1f} L{tipx:.1f},{y:.1f} L{b0 + 14:.1f},{by + PIN_H:.1f}" '
        f'fill="#fff" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
        f'<rect x="{bx:.1f}" y="{by:.1f}" width="{w}" height="{PIN_H}" rx="23" fill="#fff" stroke="{INK}" stroke-width="3"/>'
        f'<rect x="{b0 + 1.5:.1f}" y="{by + PIN_H - 3:.1f}" width="11" height="5" fill="#fff"/>'
        f'<text x="{bx + w / 2:.1f}" y="{by + PIN_H / 2 + 8:.1f}" text-anchor="middle" '
        f'font-family="Helvetica" font-weight="bold" font-size="24" fill="{INK}">{html.escape(label)}</text>')

drawio = (f'<mxfile host="Electron" compressed="false"><diagram id="map" name="MaLAPA map">'
          f'<mxGraphModel dx="0" dy="0" grid="0" gridSize="10" guides="1" tooltips="1" connect="0" arrows="0" '
          f'fold="1" page="1" pageScale="1" pageWidth="{W}" pageHeight="{H}" background="none" math="0" shadow="0">'
          f'<root><mxCell id="0"/><mxCell id="1" parent="0"/>{"".join(cells)}</root>'
          f'</mxGraphModel></diagram></mxfile>\n')
(out / "malapa_map.drawio").write_text(drawio)

(out / "preview.svg").write_text(
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
    f'<rect width="{W}" height="{H}" fill="{OCEAN}" fill-opacity="0.18"/>'
    f'<path fill="{LAND}" fill-rule="evenodd" d="{d}"/>{"".join(preview)}</svg>')
print(f"size {W}x{H}, rings {len(rings)}, land svg {len(land_svg)//1024} KB, drawio {len(drawio)//1024} KB")
