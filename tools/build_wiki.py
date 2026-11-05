#!/usr/bin/env python3
"""Build the GitHub wiki (https://github.com/MShirazAhmad/Sparewatt-docs/wiki) from this repository's Markdown.

    python3 tools/build_wiki.py <wiki-checkout>      # e.g. ../Sparewatt-docs.wiki (a clone of Sparewatt-docs.wiki.git)

The repository is the source; the wiki is generated — edit the repository, then run this and push the wiki checkout.
Each page gets a wiki name (PAGES), links between pages and their #anchors are rewritten to wiki links, images are
copied under images/, the page's own first "# Title" is dropped (the wiki shows the page name as its title), and
_Sidebar.md / _Footer.md are written. Pages the wiki has that are not generated here are left alone.
"""
import re, shutil, sys, urllib.parse
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent

# repository file → wiki page name (file name without .md; hyphens show as spaces)
PAGES = {
    "README.md": "Home",
    "guide/01 Getting started.md": "Getting-started",
    "guide/02 Menu bar and panels.md": "Using-the-menu-bar",
    "guide/03 Battery and power.md": "Using-battery-and-power",
    "guide/04 Controls.md": "Using-the-controls",
    "guide/05 Files and storage.md": "Using-files-and-storage",
    "guide/06 Dashboard and history.md": "Using-the-dashboard-and-history",
    "guide/07 How the estimates work.md": "How-the-estimates-work",
    "guide/08 Privacy and permissions.md": "Privacy-and-permissions",
    "guide/09 Troubleshooting.md": "Troubleshooting",
    "features/README.md": "Features",
    "features/01 Menu bar.md": "Menu-bar",
    "features/02 Processor, graphics and memory.md": "Processor-graphics-and-memory",
    "features/03 Temperature, network and storage space.md": "Temperature-network-and-storage-space",
    "features/04 Who is using it.md": "Who-is-using-it",
    "features/05 Battery.md": "Battery",
    "features/06 Power.md": "Power",
    "features/07 Power controls.md": "Power-controls",
    "features/08 Alerts and notifications.md": "Alerts-and-notifications",
    "features/09 Files and storage.md": "Files-and-storage",
    "features/10 Switches.md": "Switches",
    "features/11 Dashboard, history and this app.md": "Dashboard-history-and-this-app",
    "reference/Keyboard shortcuts.md": "Keyboard-shortcuts",
    "reference/Data files.md": "Data-files",
    "CHANGELOG.md": "Changelog",
    "research/README.md": "Research",
    "research/Mac menu bar monitor pain points.md": "Research-Mac-menu-bar-monitor-pain-points",
    "research/drop-zone-apps.md": "Research-Drop-zone-apps",
    "research/notes/system_monitors.md": "Research-notes-system-monitors",
    "research/notes/battery_thermal.md": "Research-notes-battery-and-thermal",
    "research/notes/disk_space.md": "Research-notes-disk-space",
    "research/notes/menubar_dragshelf.md": "Research-notes-menu-bar-and-drag-shelves",
}
# folder links (e.g. "../guide") → a page
FOLDERS = {"guide": "Home#guide", "features": "Features", "reference": "Home#reference", "research": "Research"}

SIDEBAR = [
    ("Guide", [p for k, p in PAGES.items() if k.startswith("guide/")]),
    ("Features", [p for k, p in PAGES.items() if k.startswith("features/")]),
    ("Reference", ["Keyboard-shortcuts", "Data-files", "Changelog", "Research"]),
]

LINK = re.compile(r'(\]\()([^)\s]+)(\))|(src=")([^"]+)(")')


def target(src: str, t: str) -> str:
    """A link as written in the repository file `src` → the same link in the wiki."""
    if re.match(r"^[a-z]+:", t) or t.startswith("#"):
        return t                                            # web links and same-page anchors stay
    path, _, frag = t.partition("#")
    rel = PurePosixPath(src).parent / urllib.parse.unquote(path)
    parts = []
    for p in rel.parts:                                     # resolve "..", keep it inside the repository
        if p == "..":
            parts = parts[:-1]
        elif p != ".":
            parts.append(p)
    key = "/".join(parts)
    if key in PAGES:
        return PAGES[key] + ("#" + frag if frag else "")
    if key in FOLDERS:
        return FOLDERS[key]
    if (ROOT / key).is_file():                              # images and other files are copied as they are
        return key
    raise SystemExit(f"{src}: link to {t!r} goes nowhere")


def page(src: str) -> str:
    text = (ROOT / src).read_text()
    if src != "README.md":
        text = re.sub(r"\A# .*\n+", "", text)               # the wiki shows the page name as the title
    return LINK.sub(lambda m: (m.group(1) + target(src, m.group(2)) + m.group(3)) if m.group(1)
                    else (m.group(4) + target(src, m.group(5)) + m.group(6)), text)


def main(out: Path):
    if not out.is_dir():
        raise SystemExit(f"{out} is not a folder (clone the wiki first)")
    for src, name in PAGES.items():
        (out / f"{name}.md").write_text(page(src))
    if (out / "images").exists():
        shutil.rmtree(out / "images")
    shutil.copytree(ROOT / "images", out / "images")
    # sidebar labels: each page's own "# Title" (keeps commas the page names drop), else the page name
    titles = {}
    for src, name in PAGES.items():
        m = re.match(r"# (.+)", (ROOT / src).read_text())
        titles[name] = m.group(1).strip() if m and src != "README.md" else name.replace("-", " ")
    side = ["**[Home](Home)**", ""]
    for title, names in SIDEBAR:
        side += [f"**{title}**", ""] + [f"- [{titles[n]}]({n})" for n in names] + [""]
    (out / "_Sidebar.md").write_text("\n".join(side))
    (out / "_Footer.md").write_text("Generated from the [Sparewatt-docs](https://github.com/MShirazAhmad/Sparewatt-docs) "
                                    "repository by `tools/build_wiki.py` — edit the repository, not the wiki.\n")
    print(f"{len(PAGES)} pages, sidebar, footer and images written to {out}")


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / "Sparewatt-docs.wiki")
