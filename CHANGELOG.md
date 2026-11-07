# Changelog

What changed in Sparewatt, newest first, in plain words. Dates are when the change landed in the app's repository.

## 2026-11-06 — Sparewatt 1.7

Released as [Sparewatt 1.7](https://github.com/MShirazAhmad/Sparewatt-docs/releases/tag/v1.7-2026-11-06).

- **Shorter, clearer menu bar panels.** Each panel answers its question at a glance. Nothing was removed: details moved
  behind disclosures that remember whether you opened them, into tooltips, or onto the dashboard. No number shows twice
  in a panel, and the grey explanation paragraphs became tooltips. Heights in points, before → after, with the lists
  loaded: Power 963 → 549, Processor 851 → 595, Storage 911 → 663, Memory 619 → 518, Network 603 → 562, Switches
  593 → 220, Battery 578 → 413, Files 485 → 365, Temperature 586 → 359, Graphics 501 → 272.
- **Power:** the live flow diagram comes first. Under it, one row: *Full in*, *If unplugged* and *In battery* on the
  charger; *Left* and *In battery* on battery. The charger card shows its kind and port, and the volts × amps agreed and
  coming in; the other voltage levels and the maker's details sit behind a chevron. A charger too small for the load is
  a line inside the charger card. Power per app is a stacked bar with a row per app (the donut stays on the dashboard).
  On battery it opens with a line like "Quit Xcode and Claude → +1h 05m of battery": the top two apps that can actually
  be quit, worked out together. Idle-app suggestions have a plain **Quit** button.
- **Battery:** the header says "Charging · full in 4h 09m" or "On battery · 4h 58m left", and the charge plan is one
  line. A Health card shows health % with a bar marking 80%, recharges, temperature and capacity; the charge now and the
  capacity when new are behind *Details*, with a small *Set a charge limit ↗* link. Energy modes are two compact pickers
  (battery and charger), Extreme Saver is one line, and the profiles row sits inside the Energy mode card.
- **Processor and Graphics:** the chip's name is in the header's subtitle, and the core count is a stat ("8P + 2E").
  Core tiles show the load sized to fit, with E or P underneath, so the labels no longer run into each other. Background
  activity folds to one line with its status ("Nothing unusual" or "2 unusual"). *Who is using … by kind* is on the
  dashboard.
- **Memory:** a two-column legend with short names (the full names are in tooltips); swap shows as an *On disk* row.
- **Temperature:** a thin *Last 2 min* strip with its range sits in the fans card; the header says "Processor · Normal";
  *All sensors* folds to one line that shows the hottest sensor.
- **Network:** the live diagram is the main picture; the speed graph is a thin strip with the peak.
- **Storage:** the header reads "146 GB free of 926 GB · 33 °C". One usage bar is split into biggest home folders
  and macOS, apps & System Data, with "781 GB used" beside it; purgeable space shows lightly next to free, since the
  free figure already counts it (before, it was counted as used too, so System Data read too small by that much). The read/write diagram is shorter. App caches
  and Downloads tidy-up share one card, as two rows.
- **Files:** Latest File and "N more recent files" share one card with "3 folders not searched" (a tooltip says which
  and why). An empty Shelf is a one-line drop zone. The Shelf count shows once.
- **Switches:** one card with a row per group and its count ("Servers 0/7"). A click opens a group, and it stays open.
  Switches that are on, starting or failing always show.
- **"Using the most" lists:** the share is a small meter under the value (the thin line under names read as an
  underline). A folder's growth leads its subtitle, in colour ("▲3.82 GB · ~/Projects"), instead of being
  cut off. Subtitles are short: ~ for the home folder, "WebContent" not "com.apple.WebKit.WebContent".
- **The memory list counts each process's own footprint**, as Activity Monitor does. Adding up resident sizes counted
  shared memory once per process, so the iOS Simulator showed 41.8 GB instead of about 4 GB. iOS Simulator processes
  show as one "iOS Simulator" row with the Simulator's icon. Sizes from 1000 MB show in GB (0.99 GB, not 1010 MB).
- Menu bar: a part keeps its widest width only for small digit changes, so a burst value (say during a big copy) no
  longer leaves a wide gap.

## 2026-11-06 — Sparewatt 1.6

Released as [Sparewatt 1.6](https://github.com/MShirazAhmad/Sparewatt-docs/releases/tag/v1.6-2026-11-06).

- **Uses much less power itself.** The power-per-app list no longer runs a one-second `top` over every process (about a
  second of processor time each time); one quick `ps` reading does it, measured from the previous reading. Closed panels
  and a closed dashboard stop redrawing in the background. Live diagrams draw at 15 frames a second and only while you
  can see them. Switch checks run every 10 seconds while a panel or the dashboard is open, otherwise once a minute, and
  "a process is running" checks look through the process list once for all switches. Menu bar labels already drawn
  are reused instead of drawn again. Temperatures are read in the background (the menu bar and panels no longer wait
  for them) and, with nothing open, only the sensors the menu bar uses, every third update. Free space is read every
  30 seconds.
  - What woke the Mac comes from macOS's power log (`pmset -g log`), now read only while the *While asleep* card is
    shown (Dashboard → Battery) and at most once an hour, at background priority on the efficiency cores. Before, it
    was read at every launch and every 30 minutes, and one read costs about 10 seconds of processor time because macOS
    prints its whole power log. The AI Assistant's insights also ask for a read; it is ready on the next call.
- **New Files panel and FILES part in the menu bar** (shows how many files are on the Shelf): Latest File, the Shelf and
  the clipboard moved out of the Storage panel, which now shows storage only. ⌥⌘V and files dropped on the menu bar
  open the Files panel. Hide the FILES part (Menu Bar settings) to have the three back in the Storage panel.
- **One time left.** On battery, the menu bar, the Battery and Power panels, the charge plan, Mac health and the AI
  Assistant all show the same figure: macOS's estimate from the battery's averaged draw. On the charger, *if you unplug
  now* uses your usual draw on battery in both panels.
- **Charger details** in the Power panel while plugged in: the most it can give (65 W max), its kind and port (USB
  Power Delivery 3.x · on the USB-C port 1; also plain USB-C, USB charging ports, MagSafe 3, wireless), the voltage and
  current agreed with the Mac (20 V × 3.25 A), what comes in now (63.5 W at 20.1 V · 3.16 A), every voltage level it
  offers with the one in use highlighted, and — for Apple chargers — name, maker, serial and firmware. Also in the AI
  Assistant's `get_battery`. The rating, kind, voltage levels, name and serial, the port and the Power Delivery version
  are read once, in the background, when macOS says a charger was plugged in, pulled out or swapped, or agreed a new
  voltage (and once more 5 seconds later, in case they were still agreeing); the battery's drain average then starts
  afresh. The regular update every 2 seconds reads only what comes in (watts, volts, amps). The version shows as 3.x
  because macOS doesn't tell 3.0, 3.1 and 3.2 apart.
- **Charger too small for the load** (say a 30 W charger while the Mac uses 57 W): the Mac's draw now counts the
  watts the battery adds, so the Power panel, the flow diagram and power per app show 57 W, not the charger's 29 W.
  The menu bar reads **CHARGER LOW 42.1% · 4:27 LEFT ↓8W** with a red glow instead of "ON BATT", the Power panel shows
  how long the battery lasts at that drain ("left, draining"), and the charge plan says "— even plugged in". That time left comes from the battery's average drain over the last minute, counted only since the
  charger went in, not from macOS's own estimate, which lagged behind: it showed 3 h left at an 8 W drain from 37 Wh,
  where 37 Wh ÷ 8 W is about 4 h 37 min.
- **Time to full while charging**: the Battery and Power panels say "full in 1h 10m" — macOS's own estimate when it has
  one (it knows charging slows near the top), otherwise the energy still needed ÷ the last minute's charging power.
- **The battery and power parts of the menu bar read as one pair**, nothing said twice: the battery part gives the state
  and the fill, the power part the time and which way the power flows — **⚡︎ CHARGING 43.0% · 5:02 TO FULL ↑13W**,
  **ON BATTERY 42.1% · 3:01 LEFT ↓8W**, **⏸︎ ON HOLD 80.0% · MAC USES 37W**. With one of them hidden, the other carries
  everything as before.
- Power per app: in a menu bar panel the list sits under the chart, so names read in full ("Draws everything on screen",
  not "Draws eve…").
- Sizes show the decimals that matter: 164 GB, 12.4 GB, 1.25 GB.
- Mac health: "Storage is getting full" only under 15% free **and** under 50 GB free (164 GB free on a 1 TB disk is fine).
- Dashboard overview: each tile's *Open* link has its own row instead of covering the tile's last line.

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
