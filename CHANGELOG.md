# Changelog

What changed in Sparewatt, newest first, in plain words. Dates are when the change was made.

## 2026-11-08 — Sparewatt 1.13

Released as [Sparewatt 1.13](https://github.com/MShirazAhmad/Sparewatt-docs/releases/tag/v1.13-2026-11-08).

**Last until.** A new card at the top of the Battery panel: pick the time you need the battery to reach, and Sparewatt
keeps watch until then.

- **A set point on a battery bar.** The fill is how far the battery reaches at this rate, the marker is your time, and
  what it won't reach is hatched. Drag the marker or type a time.
- **In the menu bar too:** the battery item shows the time and how much is to spare (`→3:00`, `+38m`), green, orange or
  red, with the level line showing how much of the wait the battery covers.
- **Apps coloured by what they cost against that time,** each with its watts and the minutes it's worth. Mark an app to
  keep it running or to pause it; *Pause these* does what's suggested. Pausing closes nothing, and what you're using is
  the last thing suggested.
- **It says when pausing can't get there,** and how far short it would still be.
- **By itself** pauses what it has to when the time starts slipping; never what you're using or what you said to keep.
  A notification says so once if it starts to fall short.
- Everything paused for it wakes when the time comes, when you end it, or when the charger goes in.
- Also from a link: `sparewatt://last-until/15:00`, `sparewatt://last-until/off`.

**Live diagrams cost a fraction of what they did.** Their motion now runs in macOS's own animation system, so between
readings the app does nothing. Measured on one Mac, a panel with a diagram open: Network 26.5% of one core before, 2.5%
after. They are also smoother, at up to 30 frames a second instead of 15.

**Keys inside a panel.** With a panel opened by a click or a shortcut: ← → move to the neighbouring panel, Esc closes
it, D opens its dashboard page, ⌘, opens Settings, and Tab reaches the rows you can click, with Return or Space to press
them.

**macOS's display settings.** *Increase contrast* gives the cards edges and the diagrams stronger lines. *Differentiate
without colour* adds a shape wherever colour was doing the talking: status dots, the memory map's key, a mark after a
figure in the menu bar, side-by-side bars for download and upload. *Reduce transparency* makes the floating shelf and
the menu bar's glow solid.

**Fixes.** A process number of 0 or 1 can no longer be offered for quitting, and Sparewatt never offers to quit itself.
A rate just under 1 MB/s no longer reads "1024 KB/s".

## 2026-11-08 — Sparewatt 1.12

Released as [Sparewatt 1.12](https://github.com/MShirazAhmad/Sparewatt-docs/releases/tag/v1.12-2026-11-08).

The menu bar's intensity colours, for *Battery and power: a glow and a line* (Dashboard → Menu Bar → *Colours*, which
had the name *On battery, glow by drain rate*):

- **The glow follows the drain.** It is strongest for heavy drain and fades as the drain gets lighter; from 5 hours of
  battery there is no glow, so a colour means something. Even heavy drain stays quieter than a red warning.
- **A thin level line** along the bottom of Battery and Power, as long as the watts, so you can read it without the colour.
- **Steadier.** It is judged on the last minute's drain, so one spike doesn't change it, and a figure sitting on a limit
  keeps its colour until it is clearly past it. Colours by value hold still the same way.
- **One glow and one line** across Battery and Power when the items are grouped, instead of the same fact twice.
- **On the charger too:** the line shows how fast it charges, in green with no glow. A charger too small for the Mac
  counts as draining and is at least orange.
- **Fixes to colours by value.** Graphics went by a different reading from the number beside it; now they agree.
  Memory went by how full it was, so it could turn red while macOS was fine; now it follows macOS's memory pressure.

## 2026-11-08 — Sparewatt 1.11.1

Released as [Sparewatt 1.11.1](https://github.com/MShirazAhmad/Sparewatt-docs/releases/tag/v1.11.1-2026-11-08).

- **Power per app lines up with the rest of the dashboard.** The flow takes the left half of the card, each band lands
  on its app's row, the rows start at the page's middle column and their figures end at the card's edge, like the cards
  around it. Click a band or a row to see the app's processes.
- **Replay my day** spans the full width of its card, like the Power flow.

## 2026-11-08 — Sparewatt 1.11

Released as [Sparewatt 1.11](https://github.com/MShirazAhmad/Sparewatt-docs/releases/tag/v1.11-2026-11-08).

Live simulations across the app, in the spirit of the Power flow. Every motion follows a real reading; where macOS gives
no number, nothing moves.

- **The battery, to scale** (Battery panel). The whole cell is what it held when new, the hatched part is lost to wear
  ("9% lost to wear"), and dots run toward the edge of the charge while it charges and away while it drains, faster the
  more watts flow. Resting, they stop. A line marks where macOS is holding the charge.
- **A memory map** (Memory panel): 100 blocks, one per 1% of memory, in place of the bar. Blocks fly between *Apps* and
  *Squeezed* while macOS squeezes and unsqueezes memory, and to or from the drive while it swaps, from macOS's own
  counters.
- **Fans that spin in proportion to their rpm** (Temperature panel), and stand still when the fan stops. Before, the
  speed was set once and never followed the fan.
- **Replay my day** (Dashboard → History): a day played back in 30 seconds from the saved minute readings, with a strip
  to drag to any moment and any of the last days to pick. Gaps say the Mac was asleep or Sparewatt wasn't running.
- **Power per app as a flow** (Power panel and dashboard): from the battery or charger to each app, each band as thick
  as its share, still marked as an estimate. A click opens the app's processes, as before.
- **Graphics as a flow** (Graphics panel): each app's part of the chip's work flowing into it, the same figures as the
  list under it.
- **A pulse on each Switch** each time its health check runs and finds it on. A switch with no check to run has none.
- **Extreme Saver's moment:** when it turns on, the apps it pauses dim one by one while the battery time that gives back
  counts up ("Paused 3 apps · about +48m", an estimate). The row stays while it is on.
- **Reduce Motion.** With macOS's Reduce Motion on, every diagram is a still picture, and Replay my day keeps its strip
  to drag through instead of **Play**.
- **What it costs.** Each new diagram takes about a third of the drawing time of the Power flow, only while it is on
  screen, and none at all while nothing in it is moving. With no panel open nothing is drawn.
- **Smoother dots.** A new reading changes how fast the dots carry on, instead of making them jump.
- **Fix:** opening a panel from a link or a shortcut while another panel was open could leave nothing open.

## 2026-11-07 — Sparewatt 1.10

Released as [Sparewatt 1.10](https://github.com/MShirazAhmad/Sparewatt-docs/releases/tag/v1.10-2026-11-07).

- **Desktop Macs.** Macs with no battery are now supported: Mac mini, Mac Studio, iMac and Mac Pro. In the menu bar the
  battery part steps aside and the power part reads `MAC USES 22W`, the Mac's draw as its system management controller
  reports it (on a Mac that reports none, that part steps aside too, and the Power panel shows "—", not a made-up 0 W).
  The Battery panel says *This Mac has no battery* and keeps what still applies: the energy mode, as one *Wall* row,
  and the batteries in your keyboard, mouse and headphones. The Power panel has a *From the wall* card, with the draw
  and its last 2 minutes, in place of the flow, battery time and charger cards. Extreme Saver is left out (sidebar,
  right-click menu, ⌥⌘E and the AI Assistant), the On Battery page keeps only the device low-battery alert, and History
  has no charge chart or stretches on battery. The "My Mac today" and "My Mac this week" cards lead with time awake,
  the average draw and the processor, and the Monday summary counts hours awake.
- **macOS 14 and Intel.** The app now declares macOS 14 (Sonoma) as its minimum, so an older macOS won't open it, and
  every icon it uses is checked to exist on macOS 14. On Intel Macs: the battery percentage is worked out from the
  charge in mAh where the battery reports it that way (it could read "4321%"); the system management controller's draw
  stands in when the battery gives no power reading; an unexpected sensor value can no longer crash Sparewatt; and
  processors whose cores are all one kind no longer get P/E letters.
- **More in the *Devices* card** (Battery panel):
  - **AirPods Max, Beats and other headphones with one battery** show one figure with the right picture. The row's
    tooltip has the firmware (and the case's, for earbuds) and the signal: "Firmware 9A348 · case 9A348 · signal strong
    (−54 dBm)".
  - **Game controllers** (Xbox, PlayStation and others): the level, and *Charging* under the name while one charges.
    Read when a controller connects or disconnects, every minute and when the panel opens.
  - **Devices charging from the Mac's own ports**, such as an iPhone: a row with the watts the port measures, and
    *Charging from the Mac · 5 V × 1.6 A* under the name (*Powered by the Mac* for a drive). The device doesn't share
    its own battery level with the Mac, so none is shown.
  - **Time left per device:** "about 9h left" on a small second line, from how fast the device has drained since its
    last charge. It shows once a device has dropped at least 5 points over at least an hour, never while it charges,
    and not beyond two weeks. For this, each device's level is kept 30 days in `devices.json`, on this Mac only.
    VoiceOver reads "AirPods Max, 72 percent, about 9 hours left".
- **Uninstall Sparewatt…** on Dashboard → This App, under *Trust*. A sheet lists what Sparewatt keeps on this Mac,
  with sizes, all ticked: *Saved data* (each file in `~/Library/Application Support/Sparewatt`, by name), *Logs*,
  *Settings*, *Notifications*, *Open at login* (when it is on) and *Move Sparewatt.app to the Trash*. Untick what you
  want to keep. Files go to the Trash, so you can put them back until you empty it; settings are cleared from macOS's
  settings store. Apps Extreme Saver paused are resumed first; Switches that are on keep running, and the sheet names
  them. *Uninstall and Quit* then quits Sparewatt.
- **A Privacy page** in the dashboard (Dashboard → **Privacy**, or This App → *What Sparewatt runs and reads*): the 12
  macOS programs Sparewatt starts, when and why; every place it reads or writes; the permissions it may ask for; and
  its network use ("Nothing is sent anywhere."). The guide page
  [What Sparewatt runs and reads](guide/10%20What%20Sparewatt%20runs%20and%20reads.md) is made from the same table, and
  the app's tests fail if the code starts a program the list doesn't name.
- **Find a setting.** A search field at the top of the dashboard sidebar. Type a few words ("login", "clipboard") and
  each matching setting is listed with where it is, such as *Menu Bar › General*; click one to open its page.
- **Menu Bar settings in six sections** instead of eight: *General* · *Items* (which items show, and what each shows) ·
  *Look* · *Colours* · *Alerts* · *Panels*. *Warnings* is now *Alerts*, *Colours by value* is *Colours*, and the old
  *Details* is shared out among *Items*, *Colours* and *Panels*. No setting was removed, and yours stay as they were.
- **A calmer, lighter menu bar.** A new reading redraws the menu bar at most every 4 seconds when only its figures
  changed. A change of state redraws it at once: the charger going in or out, charging, a warning, Extreme Saver; so
  do changes to settings, the Shelf and Switches. With no panel open, Sparewatt now uses about 0.77% of one core (1.8:
  about 0.84%), measured with Instruments over 30 seconds.
- **Saved data is safer.** Every file Sparewatt keeps now gets the care Switches, chargers and data usage already had:
  if a file can't be read in full, it is copied to a `.bak` beside it before anything is saved over it. History,
  insights, idle-app timings, folder sizes and usual levels used to be overwritten within a minute.

## 2026-11-07 — Sparewatt 1.9

Released as [Sparewatt 1.9](https://github.com/MShirazAhmad/Sparewatt-docs/releases/tag/v1.9-2026-11-07).

- **Device batteries.** A *Devices* card in the Battery panel shows each connected accessory that reports a battery.
  Magic Keyboard, Magic Mouse and Magic Trackpad come from macOS's device registry, read every minute, with a bolt
  while one charges over its cable. AirPods, Beats and other Bluetooth headphones show left, right and case
  ("L 64% · R 61% · Case 90%"); macOS keeps those only in `system_profiler`, which starts a process, so they are read
  every 5 minutes and when the panel opens. A level is orange at 20% or less and red at 10% or less. The card is hidden
  when nothing reports a battery. One notification per discharge at 15% or less ("Magic Mouse is at 12%"), and again
  only after the device has charged above 30%; *Alert when a device's battery is low* is on the **On Battery** page,
  on by default. Nothing is saved.
- **Mac health, beyond the live readings:**
  - **Slowing down to cool.** While macOS slows the processor to keep the Mac from overheating, the Temperature panel
    says so in one line, with macOS's speed limit when it records one: "macOS is slowing the processor to cool it —
    70% speed". It is a *Needs action* finding on the Overview, and one notification per episode, *Mac is slowing down
    to cool*. Warm for 10 minutes, before any slow-down, is *worth a look*.
  - **Time since the last restart.** The Mac health card's header says "Up 18 days". *Restarting would help* is a
    finding when the Mac has been up more than 14 days and either more than 4 GB of memory has moved to disk (swap) or
    memory pressure was raised for 10 minutes of the last hour.
  - **Drive health and Time Machine** in the Storage panel. *Drive health* is the drive's own check (SMART), read every
    6 hours: *Verified*, or *Failing — back up now*, which needs action. *Last backup* reads "yesterday 22:10", or
    *Backing up… 40%*, checked every 30 minutes and when the panel opens; over 7 days old is *worth a look*. With no
    backup disk set up it says *not set up*. macOS shows the backup dates only to apps with Full Disk Access, or through
    `tmutil` while the backup disk is connected; with neither, it says *needs Full Disk Access*, with a button to that
    setting.
  - **Memory that keeps growing.** An app whose memory grew by more than 2 GB in the last hour, while it kept running,
    is *worth a look*: "Safari's memory grew 3.10 GB in the last hour — quitting and reopening it would free that."
    A notification with **Quit ‹app›** is off by default (Dashboard → Shelf, Profiles & Alerts → *More alerts*).
- **A welcome window for new installs.** Anyone who already used Sparewatt doesn't see it. It has three lines on what
  Sparewatt does; the menu bar presets *Minimal* (processor, memory, battery), *Battery* (battery, power, temperature)
  and *Everything*, with a live preview of the menu bar, applied at once; *Open Sparewatt when you log in*; a note that
  notifications arrive quietly, with a button to their settings; and "Nothing leaves your Mac". *Show welcome again* is
  on Dashboard → This App.
- **Open at login** is a switch at the top of Dashboard → Menu Bar. It uses macOS's own login-item service, so
  Sparewatt is listed in System Settings → General → Login Items, where macOS may first ask for your OK; the *System
  Events* prompt is gone. A login item from an older Sparewatt, or one you added yourself, stays as it is and the switch
  doesn't see it; remove it in Login Items if you no longer want it. The same page has *Apply preset: Minimal ·
  Battery · Everything*, which sets the item switches and ticks the preset they match.
- **Export and import settings** on Dashboard → This App: one JSON file with your settings (the ones you changed from
  their defaults), your switches and your profiles, to keep a copy or move them to another Mac. Not included: open at
  login (a macOS registration, not a setting) and Sparewatt's own state on this Mac, such as the files on the Shelf,
  pinned clipboard text, whether Extreme Saver is on, and window positions. Import first asks "12 settings, 13 switches,
  3 profiles — replace your current ones?", with a warning when the file holds switches (they run their own commands).
  It then saves your current settings as `settings-backup-<date>.json` and replaces them; a setting not in the file goes
  back to its default. A file from a newer Sparewatt is refused.
- **Data used per app, today and this week.** A *Data used today* card in the Network panel: download and upload so
  far today, and the five apps that used the most. The dashboard's Network page adds today, the last 7 days and the
  daily average, each app's figure for today and the 7 days, and a chart of each day's total for 14 days. Counted once
  a minute from one `nettop` that runs as long as Sparewatt does, so a download that starts and ends between two
  readings still counts. Only internet traffic (Wi-Fi, Ethernet, hotspot) counts, not apps talking to each other inside
  the Mac. An optional daily limit (1 to 50 GB a day, off by default) sends one notification the first time today's
  data passes it. Kept 14 days on this Mac only, in `data-usage.json` (bytes per app per day; no addresses or sites).
- **"My Mac this week" card.** The share sheet has a *Day / Week* switch. The week card shows the last 7 days: time on
  battery and the daily average, a bar for each day, the three apps that used the most battery, battery health and
  recharges, and the internet data used. Same rules as the day card: no file paths, names or serial numbers. An
  optional **Monday summary** ("Last week: 18h on battery · top drain Xcode · 4.20 GB used") comes the first time the
  Mac is awake after 9:00 on Monday; clicking it opens the share sheet on the week card. It is off by default
  (Dashboard → Shelf, Profiles & Alerts → *More alerts*). New link: `sparewatt://share`, `/day` or `/week`.
- **Fix:** the "using the network most" list's helper, `nettop`, spun on its empty input: 1.4 s of processor time per
  run instead of 0.04 s, while the Network panel was open. It now gets an input that stays open and silent.
- Builds with older Swift versions too (the automatic tests on GitHub use Swift 6.2).

## 2026-11-07 — Sparewatt 1.8.1

Released as [Sparewatt 1.8.1](https://github.com/MShirazAhmad/Sparewatt-docs/releases/tag/v1.8.1-2026-11-07).

- Finishing touches: the app builds with no warnings (twelve thread-safety checks that a future Swift would refuse are
  fixed, in the background watch, app caches, power settings, charger lookup and screen-sleep code), and the
  Temperature and Network strips read "Last 2 min" again (1.8 wrote "Last 2m").

## 2026-11-07 — Sparewatt 1.8

Released as [Sparewatt 1.8](https://github.com/MShirazAhmad/Sparewatt-docs/releases/tag/v1.8-2026-11-07).

- **Lighter still.** With no panel open, Sparewatt now uses about 0.84% of one core (1.7: about 2.1%), measured with
  Instruments' Time Profiler over 30 seconds. The menu bar is redrawn only for real changes: CPU, GPU and memory move
  their shown figure on a 2-point change, temperature on 2°, watts on 2 W and network speed on 30%, or after 10
  seconds. Red warnings still look at the exact readings. The grouped item is drawn once per change, from the parts
  already drawn. While the screen is asleep or locked, readings drop to every 30 seconds and the menu bar isn't drawn;
  waking or unlocking refreshes it at once. Free space is read every minute.
- **FILES and SWITCH step aside while they'd show only 0:** an empty Shelf; no switch on, changing or failed. Menu Bar
  settings has *Files: show even when the Shelf is empty* and *Switches: show even when none is on*. Dropping files on
  the menu bar, or ⌥⌘V, still opens the Files panel.
- **"My Mac today" share card.** A 1200 × 630 picture of your Mac's day, dark or light: time on battery and how much of
  a charge it used, a curve of today's charge, the app that used most battery, battery health and recharges, and the
  charger. No file paths, names or serial numbers. *Share my day* is on the dashboard's Overview, and an icon next to
  *Export CSV…* on History; the preview has *Share…*, *Copy image* and *Save…*.
- **Charger history.** Every charger you plug in is remembered: its rating, kind and Power Delivery version, the port,
  the voltage levels it offers, the most it has actually delivered, how many times it was connected, when it was first
  and last seen, and a nickname you give it. The Power panel's charger card says, for example, "Seen 4 times · best
  63.5 W delivered". Dashboard → Power flow lists every charger. One is tagged *slow* when it couldn't keep up (the
  battery drained for a minute while it was plugged in), or when the most it has delivered is under 60% of what it
  should manage: its rating, capped at the most this Mac has drawn from any charger, so a 96 W charger on a Mac that
  never takes more than 40 W isn't slow. Kept only on this Mac.
- **An honest battery wear trend.** No projection until there are at least 14 daily readings spread over three weeks;
  until then the card says "Needs about N more days of readings for a wear trend". The trend is the straight line that
  best fits every reading, so one odd day can't swing it. After that it reads, for example, "−0.6%/month · At this
  rate, 80% around mid-2028", or *steady* when the change is within the day-to-day wobble. No more "about 0 months".
- **Notifications with buttons.** Notifications come from macOS's own notification center, under Sparewatt's name and
  icon, instead of a script. A suggestion to quit an idle app, and "Busy in the background", offer **Quit ‹app›** (a
  normal quit, never a force quit) and **Not now**; Watchlist alerts offer **Show**. Clicking any notification opens its
  panel. Quiet hours still silence everything. They start out delivered quietly, to Notification Center only, until you
  choose banners in System Settings → Notifications → Sparewatt.
- **`sparewatt://` links for Shortcuts and scripts:** `extreme-saver/on`, `/off` or `/toggle`;
  `energy-mode/battery/…` and `energy-mode/charger/…` with `low`, `automatic` or `high`; `panel/<name>`; `dashboard`
  or `dashboard/<page>`; `switch/<name>/on`, `/off` or `/toggle`. Use Shortcuts' *Open URLs* action, or
  `open "sparewatt://extreme-saver/toggle"` in Terminal. Every link is in
  [Links for Shortcuts and scripts](reference/Links%20for%20Shortcuts%20and%20scripts.md).
- **Crash log and Report a problem.** If Sparewatt ever crashes, it keeps a log on this Mac, and the next launch shows a
  card on Dashboard → This App with *Report…* (opens a GitHub issue you read before sending, with paths and names
  removed), *Show log* and *Dismiss*. A *Report a problem…* button is always there. Nothing is sent by itself.
- **VoiceOver.** Every panel, chart, diagram, meter and icon button reads as words. The power flow says "the 65-watt
  charger gives 44 watts to the Mac and 17 watts to the battery"; list rows read like "Xcode, App, 4.2%, button", with
  Notify and Quit as actions.
- **One time style everywhere:** "46m", "1h 05m". The idle-apps card and the notifications used "52 min" and
  "1 h 30 min".
- **New screenshots** in these docs, from a made-up demo dataset (no real names or folders).

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
