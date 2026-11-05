# Where Sparewatt keeps its data

Everything is local. Deleting these resets the matching feature; Sparewatt recreates them.

## Settings

macOS's preferences store, domain `app.sparewatt.Sparewatt`:

```bash
defaults read app.sparewatt.Sparewatt
```

(ResourceWarden used `local.shiraz.ResourceWarden`; Sparewatt copies it once on first launch and leaves the old domain
in place.)

## `~/Library/Application Support/Sparewatt/`

| File | Holds | Kept |
|---|---|---|
| `history.json` | one reading a minute (charge, Mac's draw, on battery or not, processor load, temperature, health) and every stretch on battery | 30 days |
| `insights.json` | battery health and recharges, one reading a day; battery watt-hours per app per day | a year; 14 days |
| `idle-apps.json` | the floor calibration (Mac's draw and total energy impact, one pair a minute on battery) and when each open app was last in front | last 3,000 minutes; while the app runs |
| `process-baseline.json` | each background process's usual level, for "far more than usual" | grows; never trimmed |
| `folder-sizes.json` | the last count of each home folder's size | until the folder changes |
| `switches.json` | your Switches (commands, checks, options) | until you change them |
| `switches.json.bak` | `switches.json` as it was, kept when it could not be read in full | until you delete it |

Also in the settings: Watchlist rules, cache size limits, the Shelf's file **paths** (not copies — so the Shelf survives
a restart), pinned clipboard entries (plain text), profiles, the idle-app never-suggest list and the old-settings
migration marker.

## `~/Library/Logs/Sparewatt/`

Each switch's output when it runs, one file per switch, appended to (never trimmed).

## Not stored

The clipboard history (memory only).
