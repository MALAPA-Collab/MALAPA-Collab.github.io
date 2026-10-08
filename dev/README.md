# dev/

Source files for site images. Nothing in this folder is published.

## Workshop map

| File | What it is |
|---|---|
| `malapa_map.drawio` | The map. Edit this in [draw.io](https://www.drawio.com) (desktop app or app.diagrams.net). |
| `export-map.sh` | Exports the map to `docs/img/malapa_map.webp`. |
| `build_map_starter.py` | Script that generated the starter `.drawio` from map data. Only needed to rebuild from scratch (input: [`ne_50m_land.geojson`](https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_50m_land.geojson)); it overwrites manual edits. |

**Adding a workshop pin:** open `malapa_map.drawio`, copy an existing pin, change its number, and drag its tip onto the city. The ocean and land layers are locked so they can't be moved by accident. To flip a pin, use Arrange → Flip (not rotate) so the number stays upright.

**Exporting:** after saving `malapa_map.drawio`, run this (it works from any directory):

```bash
./dev/export-map.sh
```

It exports the map with a transparent background, converts it to WebP, and writes it to `docs/img/malapa_map.webp`, which is the file the Workshops page shows. Commit the updated `.webp` together with the `.drawio` change. Needs [draw.io Desktop](https://www.drawio.com) and uv; on a headless Linux machine set `DRAWIO="xvfb-run -a drawio --no-sandbox"`.

**Colours** (match `docs/assets/css/styles.css`):

- Land `#3A8ACF`
- Ocean `#3A8ACF` at 18% opacity on a transparent background, so it shows as `#DCEAF6` in light mode and dark navy in dark mode
- Pins: white fill, `#163B5A` outline and numbers

**Map data:** coastlines from [Natural Earth](https://www.naturalearthdata.com) 1:50m land (public domain), Miller projection, cropped to 57°S to 84°N.
