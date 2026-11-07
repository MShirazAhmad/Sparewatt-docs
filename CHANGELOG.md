# Changelog

What changed in Sparewatt, newest first, in plain words. Dates are when the change landed in the app's repository.

## 2026-11-06 — Sparewatt 1.5.1

Released as [Sparewatt 1.5.1](https://github.com/MShirazAhmad/Sparewatt-docs/releases/tag/v1.5.1-2026-11-06).

- The battery and power text on the drain glow (green, lime, yellow…) is white on a dark menu bar, like the other
  readings, instead of turning black on bright colours; a faint shadow keeps it readable. On a light menu bar it is
  black, like the others.

## 2026-11-06 — Sparewatt 1.5

Released as [Sparewatt 1.5](https://github.com/MShirazAhmad/Sparewatt-docs/releases/tag/v1.5-2026-11-06), with
everything from 5 November below.

- **Icon picker**: a switch's icon, and each profile's, is picked from a searchable grid of symbols instead of typing an
  SF Symbol name. Search by name or by a word like "database" or "AI"; any other SF Symbol name can still be typed in.
- **Fixes:**
  - A switch that comes up after Sparewatt stopped waiting no longer shows ON next to "Didn't come up — see its log":
    the message goes away as soon as the switch is on (and "Still running" as soon as it is off). A start command that
    is still running, such as a slow server loading, gets 60 seconds instead of 30 before that message.
  - A switch's log keeps every start and stop instead of being emptied at each start, and stops without a stop command
    are logged too. A log over 5 MB is set aside as `<name>.old.log`.
  - Just after unplugging, the menu bar shows *ON BATTERY* with the battery's draw instead of *NOT CHARGING* /
    *POWER 0W* while the battery gauge catches up.

## 2026-11-05

- **AI Assistant** (dashboard → Control): an MCP server, off by default, lets Claude Code, Codex, Cursor, LM Studio or
  any MCP app read Sparewatt's readings, top apps, battery history, insights and Switches. *Show Instructions* gives a
  sentence to paste into your assistant. With *Allow changes* on, it can also turn Switches on or off, quit an app and
  set Extreme Saver or energy modes (with your password). This Mac only (127.0.0.1); web pages are refused.
  [AI Assistant](features/12%20AI%20Assistant.md)
- New bundle ID **`local.ahmad.Sparewatt`** (1.4 used `app.sparewatt.Sparewatt`): the first launch copies your 1.4
  settings once; history, switches and logs stay where they are.
- The update check (off by default) reads the public releases here, and reads a dated tag like `v1.4-2026-11-05` as 1.4.
- Each panel's window button opens the dashboard on that panel's own page.
- The grouped menu bar item has a thin outline and a soft shade behind it (*Outline and shade behind the grouped item*,
  on by default).
- **Power going out to USB devices**: the power-flow diagram shows a device charging from the Mac's ports, with the
  measured watts ("iPhone 5.6 W"), and the Power card adds *iPhone gets 5.6 W*.
- Idle-app notifications held back by quiet hours are sent once quiet hours end, instead of being skipped.
- A warning in the menu bar (processor, memory, storage or temperature over its limit, low battery, a failed switch)
  shows as a soft red glow behind the item, with the text in the menu bar's own colour, instead of red text.
  The drain colours on battery glow the same way (red, orange, yellow, lime or green behind the battery and power
  parts), with white or black text, whichever reads better on that colour.
- **Fixes:**
  - A charger that gives less than 1 W while the battery drains (switched off at the wall, an unpowered hub) shows as
    *On battery* with the battery's real draw, instead of *On adapter, uses 0 W*.
  - The *Shelf, Profiles & Alerts* page is on the dashboard (Control), so quiet hours, the low-storage and "busy with no
    window" alerts, profile editing and the Shelf options can be changed.
  - `switches.json` can no longer be wiped: missing fields take their defaults, and a file that can't be read in full is
    kept as `switches.json.bak` before anything is saved over it; the Switches page says so.
  - Apps paused by Extreme Saver wake up when Sparewatt quits, and at the next launch after a crash (unless Extreme
    Saver is still on).
  - Trash in the Shelf card needs a second click, like the floating Shelf.
  - Downloads tidy-up: *Select all* ticks only the 30 listed findings, and moving to the Trash asks first.
  - Downloads tidy-up finds downloads again. It searched through Spotlight, which macOS doesn't let see Downloads for an
    app without access, so it always came back empty. *Look* now reads the folder itself; the first time, macOS asks.
  - Latest File shows new downloads (once *Look* in Downloads tidy-up has read Downloads) and says which chosen folders
    it can't see: macOS keeps Desktop and Documents out of its search, and Sparewatt doesn't ask for them.
  - Latest File looks again each time the Storage panel opens, and looks back a day, then a week, when the last hour has
    nothing. Before, it searched only once per launch.
  - A cache that takes over 15 seconds to count shows what was counted instead of dropping off the list.
  - Watchlist: energy alerts read "energy score of 25" (not "25 energy energy"); the Network limit steps by 0.5 MB/s.
  - The floating Shelf's *Quick Look* opens the system preview, not the file's app.
  - Processor page: with live diagrams off, the "Each core" bars show once.
  - The busy-app tooltip also works on the separate CPU and GPU items.
  - This App lists Switches and insights in the by-feature breakdown.
  - A profile is marked current only when every change went through (not when a password prompt was cancelled).

## 2026-11-04

- **Named Sparewatt**: the app, its data folder `~/Library/Application Support/Sparewatt` and its logs
  `~/Library/Logs/Sparewatt`.
- **Idle apps on battery**: suggests quitting apps you haven't used for a while (10 min) when quitting would add enough
  battery time (30 min). Card with Quit / Not now / Never, one notification per app per unplug, limits on the On Battery
  page.
- Battery time per app now counts only the draw above what the screen and macOS use anyway, and measures each app's
  share against every process, so the numbers are smaller and closer to what quitting really gives back.
- **Switches**: any local service (Django, nginx, Ollama, Docker, PostgreSQL, launchd jobs, your own commands) as an
  on/off switch, with a SWITCH part in the menu bar, an editor, logs, stop on battery and start with the app.
- **Shelf**: drop files on the menu bar, drag them out later; Move to, AirDrop, Zip, Copy path, Open with, Trash; folder
  chips; a drop zone that follows the pointer while you drag; shake for a floating Shelf.
- Charge plan, battery wear log, charger check, what woke the Mac, battery used per app this week, busy apps with no
  window, memory forecast, Downloads tidy-up, low-storage alert, clipboard pins, profiles, quiet hours, ⌥⌘V and ⌥⌘E.
- Clipboard card: recent copies in memory only (passwords skipped), click or drag to reuse as plain text.
- Consistency passes: °C everywhere, one duration style, one wording for charge states, clearer list headings.

## 2026-11-03

- The menu bar became **one grouped item** with a hover panel per part; true charging states and the battery's real
  fill to 0.1%.
- A warning when the charge state and the measured current disagree.
- **Live diagrams**: power flow, network, storage read/write, processor cores, memory map, chip heat map.
- **This App** page: what Sparewatt itself costs, per feature. Colour limits per item.
- **Who is using it**: macOS, Apple Intelligence & Siri, indexing/sync/backup, your apps, other tools; background
  processes grouped, with their usual and peak levels.
- Process drill-downs: click a power slice or a "Using … most" row to see its processes and quit them.
- **Mac health** summary and the **Startup Items** page.
- Latest File searches through Spotlight, so protected folders are never opened.
- Research into similar Mac apps and their users' complaints (see [research](research/README.md)).

## 2026-11-01

- First version: menu bar readings for processor, graphics, memory, storage, battery and power; energy modes;
  Extreme Saver; the app icon.
- **Watchlist**: be told when an app overuses a resource on battery.
- **Dashboard** window with every monitor and control; every list row says where it comes from.
- Power pie chart with watts per app; battery time left at the current draw.
- Temperatures and fans, network speed, per-core load, memory pressure, disk speed, folder drill-down.
- Universal build (Apple silicon and Intel), DMG installer, a link to macOS's own Charge Limit.
