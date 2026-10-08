# Here lies the code to render the [MALAPA-Collab.github.io](https://malapa.org) website.

## Making changes

Pages are Markdown files in `docs/`; the menu and site settings live in `mkdocs.yml`.
Dependencies are pinned in `pyproject.toml` / `uv.lock` and managed with [uv](https://docs.astral.sh/uv/).

1. Preview locally from the repo root: `uv run mkdocs serve`, then open <http://127.0.0.1:8000> (reloads on save).
2. Check for broken links and missing pages: `uv run mkdocs build --strict`.
3. Commit on a branch, push it, and open a pull request. When it's merged into `main`, GitHub Actions builds and publishes the site automatically.

## Common updates

**After each workshop / when the next one is announced**

1. `docs/workshops.md`: move the current workshop from the *Upcoming* box into the top row of the *Past workshops* table, then fill the box with the next one.
2. `docs/index.md`: update the *Next workshop* button text.
3. `dev/malapa_map.drawio`: add the new pin in draw.io, then run `./dev/export-map.sh`. It writes `docs/img/malapa_map.webp` (the image the Workshops page uses); commit both files. See `dev/README.md`.

**Committee changes** (`docs/committee.md`)

Add a headshot to `docs/img/` (`lastname.webp`, square, ~360 px), then add or move a list item:

```markdown
-   ![Full Name](img/lastname.webp)
    **Full Name**
    Institution
```

**Software / Sister Collaborations listings** arrive as GitHub issues from the forms in `.github/ISSUE_TEMPLATE/`. Add a row to the table in `docs/resources/software.md` or `docs/resources/sister-collaborations.md`, just above the *Request a listing* row (which stays last).

**Styling** lives in `docs/assets/css/styles.css`. Colours are variables at the top of that file; pages opt into a style with a wrapper such as `<div class="people" markdown>`.

## Caveats

- **`main` is protected.** Everyone (admins included) must go through a pull request; you can merge your own. Merging publishes immediately and there is no staging site, so preview first.
- **The edit pencil** on each page opens the file on GitHub. Visitors without write access are offered a fork and a pull request; nothing goes live until it's merged.
- **New pages must be added to `nav:` in `mkdocs.yml`**, or they won't appear in the menu.
- **Everything in `docs/` is published.** Keep source/working files (e.g. the Keynote map source) in `dev/`.
- **Keep `docs/CNAME`.** Deleting it drops the `malapa.org` custom domain on the next deploy.
- **Stay on MkDocs 1.x.** MkDocs 2.0 is incompatible with this site and the Material theme, so the dependencies are capped at `mkdocs<2`. Update versions with `uv lock --upgrade`.
