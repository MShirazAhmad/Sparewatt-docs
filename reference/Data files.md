# Where Sparewatt keeps its data

Everything is local. Deleting these resets the matching feature; Sparewatt recreates them.

## Settings

macOS's preferences store, domain `local.ahmad.Sparewatt`:

```bash
defaults read local.ahmad.Sparewatt
```

(Sparewatt 1.4 used `app.sparewatt.Sparewatt`; a later version copies those settings once on its first launch and leaves
the old domain in place.)

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
| `chargers.json` | every charger plugged in: rating, kind, Power Delivery version, levels, last port, best watts delivered, times connected, first and last seen, your nickname (name, maker and serial when the charger reports them) | until you delete it |
| `chargers.json.bak` | `chargers.json` as it was, kept when it could not be read in full | until you delete it |

Also in the settings: Watchlist rules, cache size limits, the Shelf's file **paths** (not copies — so the Shelf survives
a restart), pinned clipboard entries (plain text), profiles, the idle-app never-suggest list, the AI Assistant's on/off, port and
*Allow changes* (`mcpEnabled`, `mcpPort`, `mcpAllowChanges`) and the old-settings migration marker.

## `~/Library/Logs/Sparewatt/`

Each switch's output when it runs, one file per switch, appended to (never trimmed).

`crash-<date>.log`: if Sparewatt crashes, the app and macOS version, what went wrong and the call stack. Kept until you
delete it, and sent nowhere unless you [report it](../features/11%20Dashboard%2C%20history%20and%20this%20app.md#crash-log-and-report-a-problem)
yourself.

## Not stored

The clipboard history and the AI Assistant's activity list (memory only).
