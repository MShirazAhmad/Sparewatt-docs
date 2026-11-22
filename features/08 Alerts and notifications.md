# Alerts and notifications

Sparewatt tells you about a problem **once per episode** — it can tell you again only after the value has gone back to
normal. Every notification it sends is listed here.

| Notification | When | How often | Battery only? | Turn off / change |
|---|---|---|---|---|
| **Quit *app*? About +N of battery** | an app unused for 10 min would give back ≥ 30 min | once per app per unplug, only while you're at the Mac | yes | Dashboard → On Battery → *Apps you aren't using* |
| ***App* kept your Mac awake while you were away** — "…On battery your Mac sleeps after 10m, but Xcode kept it awake (running tests)." | on battery, the Mac would have gone to sleep or turned its screen off while you were away, but an app kept it awake (sound and video, and parts of macOS, left out) | once per app per unplug, as you come back | yes | Dashboard → On Battery → *What keeps your Mac awake* (on) |
| **Charged to 80%** — "Unplug now to keep the battery at about 80%." (**Fully charged** at 100%) | plugged in, the battery charges up to the level you set | once per charge; again after unplugging | no | Dashboard → On Battery → *Battery level alerts* (off) |
| **Battery at 20%** — "About 1h 10m left at this rate. Plug in soon." | on battery, the battery runs down to the level you set | once per unplug; again after plugging in | yes | Dashboard → On Battery → *Battery level alerts* (off) |
| **"*Backup*" wasn't ejected** — "Preview has files open on it. Quit or close it, then eject again." | you ejected a disk from the right-click menu or a link and macOS refused (a link naming no connected disk gets **No disk named "*name*"**) | each time | no | always on; the Storage panel shows the same reason |
| **Still high** — "Processor has been above 85% for 5 min (now 92%)." (or "Graphics has been above 85%…") | processor, graphics, memory or temperature above its red limit for N minutes (graphics as a 10-second average) | once per episode | no | Dashboard → Menu Bar → *Alerts* (on, 5 min) |
| **Unusual background activity** — "*name* (*kind*) is using 34% of the processor — usually 0.8%." | a background process far above its learned normal | once per episode | yes, by default | Dashboard → Menu Bar → *Alerts* (*…also when plugged in*) |
| **Busy in the background** — "*app* has used about 18% of the processor for 10 minutes with no window on screen." | a hidden or windowless app busy for 10 minutes | once per episode | no | Dashboard → Shelf, Profiles & Alerts (on, 10%) |
| **Keep awake is off** — "The battery is down to 9%, so your Mac can sleep again as usual." | [Keep awake](07%20Power%20controls.md#keep-awake) was on and the charge fell below 10% on battery | once each time it happens | yes | always on while Keep awake is on |
| **The internet is down** — "No answer from 1.1.1.1 since 10:41, though the Mac is connected (Wi-Fi)…" | the [internet check](03%20Temperature%2C%20network%20and%20storage%20space.md#connection-and-internet-check) went unanswered three times in a row while a network was connected | once per outage | no | Dashboard → Shelf, Profiles & Alerts → *Internet check* (**off**; notifications on once it is on) |
| **The internet is back** — "It was down for about 12m." | the first answer after an outage | once per outage | no | as above |
| **Battery state doesn't add up** | charge state and measured current disagree for a minute | once per episode | no | always on |
| **Storage almost full** — "Only 18 GB free (your limit is 20 GB)…" | free space below the limit | once, re-armed when space recovers | no | Dashboard → Shelf, Profiles & Alerts (20 GB) |
| **On battery: *app*** — "*app* is using 45% processor (limit 30%)" | a Watchlist rule is exceeded | not repeated within the quiet period (10 min) | per rule | Dashboard → **Watchlist** |
| **Caches cleared** — "Emptied over its limit: …" | an app cache passed its size limit and was emptied | each hourly check that emptied something | no | remove the limit in the Storage panel |
| **Mac is slowing down to cool** — "macOS is slowing the processor to keep the Mac from overheating (70% speed)…" | macOS starts slowing the processor to cool the Mac | once per episode, until it is back to normal | no | always on |
| ***Device* is at *N*%** — "Magic Mouse is at 12%" | a connected keyboard, mouse, trackpad, pair of headphones or game controller at 15% or less, not charging | once per discharge; again after it charged above 30% | no | Dashboard → On Battery → *Alert when a device's battery is low* (on) |
| **Memory keeps growing** — "Safari's memory grew 3.10 GB in the last hour…" | an app's memory grew by more than 2 GB in an hour while it kept running | once per episode | no | Dashboard → Shelf, Profiles & Alerts → *More alerts* (**off**) |
| **Data limit passed** — "3.2 GB of internet data used today, over your 3 GB a day. Most of it: …" | today's internet data passes your daily limit | once a day | no | Dashboard → Shelf, Profiles & Alerts → *More alerts* (**off**; 1–50 GB a day) |
| **Your Mac last week** — "Last week: 18h on battery · top drain Xcode · 4.2 GB used" | Monday, the first time the Mac is awake after 9:00 | once a week | no | Dashboard → Shelf, Profiles & Alerts → *More alerts* (**off**) |

## Warnings without a notification

| Warning | Where |
|---|---|
| An item **glows red** (processor, memory, storage, temperature, battery, a failed Switch) | menu bar ([Menu bar](01%20Menu%20bar.md#red-warnings)) |
| *Sparewatt is running, but hidden* | an alert, once per run ([Menu bar](01%20Menu%20bar.md#hidden-item-check)) |
| Charger too small / near its limit | Power panel |
| Memory forecast (swap growing fast) | Memory panel |
| *Needs action* / *Worth a look* | dashboard Overview ([Mac health](11%20Dashboard%2C%20history%20and%20this%20app.md#overview-and-mac-health)) |
| Drive health failing, last Time Machine backup over 7 days old | Storage panel ([Storage space](03%20Temperature%2C%20network%20and%20storage%20space.md#storage-space)) and the Overview |
| *Restarting would help* | dashboard Overview |

## Quiet hours

All notifications can be silenced between two hours of the day (off by default, 22:00–07:00). The switch and the hours
are on Dashboard → **Shelf, Profiles & Alerts**.

## Notifications with buttons

**Purpose.** Act on a notification where it appears, instead of hunting for the panel.

**What it does.** Notifications come from macOS's own notification center, under Sparewatt's name and icon.

| Notification | Buttons | Clicking it opens |
|---|---|---|
| **Quit *app*? About +N of battery** (one app) | **Quit *app*** · **Not now** (not again until you plug in) | Battery panel |
| **Busy in the background** | **Quit *app*** · **Not now** | Processor panel |
| **On battery: *app*** (Watchlist) | **Show** | the panel for that resource |
| **Memory keeps growing** | **Quit *app*** · **Not now** | Memory panel |
| **Your Mac last week** | none | the dashboard's share sheet, on the "My Mac this week" card |
| every other notification | none | the panel it is about |

**Quit *app*** is the app's normal quit: it can ask to save first. It is never a force quit. When a menu bar part is
hidden, a click opens the matching dashboard page instead of its panel.

**Banners.** Sparewatt doesn't ask for permission at launch: its notifications start out *delivered quietly*, to
Notification Center only, with no banner or sound. To see banners, choose to keep them prominent in a notification's
menu, or turn banners on in System Settings → Notifications → Sparewatt. Turning Sparewatt off there silences them all.

**Limits.** When macOS won't let Sparewatt use the notification center (for example a copy run outside the app), it
falls back to a plain banner from macOS's scripting tool: no buttons, and a click doesn't open Sparewatt.
