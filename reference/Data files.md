# Where Sparewatt keeps its data

Everything is local. Deleting these resets the matching feature; Sparewatt recreates them. To remove all of them at
once, use Dashboard → This App → *Uninstall Sparewatt…*
([more](../features/11%20Dashboard%2C%20history%20and%20this%20app.md#uninstall-sparewatt)).

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
| `power-sensors.json` | which power sensor belongs to which part, found by *Calibrate* in the experimental Power by part card, and when | until you calibrate again |
| `history.json` | one reading a minute (charge, Mac's draw, on battery or not, processor load, temperature, health) and every stretch on battery | 30 days |
| `insights.json` | battery health and recharges, one reading a day; battery watt-hours per app per day | a year; 14 days |
| `idle-apps.json` | the floor calibration (Mac's draw and total energy impact, one pair a minute on battery) and when each open app was last in front | last 3,000 minutes; while the app runs |
| `process-baseline.json` | each background process's usual level, for "far more than usual" | grows; never trimmed |
| `folder-sizes.json` | the last count of each home folder's size | until the folder changes |
| `switches.json` | your Switches (commands, checks, options) | until you change them |
| `chargers.json` | every charger plugged in: rating, kind, Power Delivery version, levels, last port, best watts delivered, times connected, first and last seen, your nickname (name, maker and serial when the charger reports them) | until you delete it |
| `data-usage.json` | internet data per app per day, download and upload in bytes (no addresses or sites), and when counting began | 14 days |
| `devices.json` | each accessory's battery level (keyboard, mouse, headphones, game controller) with the time and whether it was charging, noted when it changes and every 30 minutes while it doesn't, for the [time left](../features/05%20Battery.md#device-batteries); written at most every 10 minutes and when Sparewatt quits | 30 days |
| `settings-backup-<date>.json` | your settings, switches and profiles as they were just before an import replaced them (the same format as *Export settings…*) | until you delete it |
| `<name>.bak` | one of the files above (not a settings backup) as it was, kept when it could not be read in full (see below) | until you delete it |

Also in the settings: Watchlist rules, cache size limits, the Shelf's file **paths** (not copies — so the Shelf survives
a restart), pinned clipboard entries (plain text), profiles, the idle-app never-suggest list, the AI Assistant's on/off, port and
*Allow changes* (`mcpEnabled`, `mcpPort`, `mcpAllowChanges`) and the old-settings migration marker.

**When a file can't be read.** Reading a file never changes it. If one of the files above (other than a settings
backup) can't be read in full (not JSON, or with entries Sparewatt had to leave out), it is first copied to
`<name>.bak` beside it, such as `history.json.bak`, or to `<name> <date>.json.bak` when a different `.bak` is already
there. Only then can a later save write over the file; if no copy can be made, the file is never written over. Every
save writes a whole new file, so a crash mid-save leaves the old one whole. `switches.json`, `chargers.json`,
`data-usage.json` and `devices.json` are indented, so they are easy to read or edit by hand.

**The "version" key.** `history.json`, `insights.json`, `idle-apps.json` and `devices.json` carry `"version": 1` beside
their data. An older Sparewatt ignores it, and a file without it reads as before. The list-shaped files (`switches.json`,
`chargers.json`, `folder-sizes.json`, `process-baseline.json`) carry none and keep exactly the shape they had before.

## `~/Library/Logs/Sparewatt/`

Each switch's output when it runs, one file per switch, appended to (never trimmed).

`crash-<date>.log`: if Sparewatt crashes, the app and macOS version, what went wrong and the call stack. Kept until you
delete it, and sent nowhere unless you [report it](../features/11%20Dashboard%2C%20history%20and%20this%20app.md#crash-log-and-report-a-problem)
yourself.

## Settings files you export

*Export settings…* (Dashboard → This App) writes one JSON file wherever you choose, named "Sparewatt settings" with the
date: the settings you changed from their defaults, your switches and your profiles. It leaves out open at login and
Sparewatt's own state on this Mac (the Shelf's files, pinned clipboard text, window positions). See
[Your settings](../features/11%20Dashboard%2C%20history%20and%20this%20app.md#your-settings-export-import-welcome-again).

## Not stored

The clipboard history and the AI Assistant's activity list (memory only). The drive's health check and Time Machine's
last backup are read again each time and never saved. (Device battery levels are kept since 1.10, in `devices.json`,
for the time left.)
