# Alerts and notifications

Sparewatt tells you about a problem **once per episode** — it can tell you again only after the value has gone back to
normal. Every notification it sends is listed here.

| Notification | When | How often | Battery only? | Turn off / change |
|---|---|---|---|---|
| **Quit *app*? About +N of battery** | an app unused for 10 min would give back ≥ 30 min | once per app per unplug, only while you're at the Mac | yes | Dashboard → On Battery → *Apps you aren't using* |
| **Still high** — "Processor has been above 85% for 5 min (now 92%)." | processor, memory or temperature above its red limit for N minutes | once per episode | no | Dashboard → Menu Bar → *Warnings* (on, 5 min) |
| **Unusual background activity** — "*name* (*kind*) is using 34% of the processor — usually 0.8%." | a background process far above its learned normal | once per episode | yes, by default | Dashboard → Menu Bar → *Warnings* (*…also when plugged in*) |
| **Busy in the background** — "*app* has used about 18% of the processor for 10 minutes with no window on screen." | a hidden or windowless app busy for 10 minutes | once per episode | no | Dashboard → Shelf, Profiles & Alerts (on, 10%) |
| **Battery state doesn't add up** | charge state and measured current disagree for a minute | once per episode | no | always on |
| **Storage almost full** — "Only 18 GB free (your limit is 20 GB)…" | free space below the limit | once, re-armed when space recovers | no | Dashboard → Shelf, Profiles & Alerts (20 GB) |
| **On battery: *app*** — "*app* is using 45% processor (limit 30%)" | a Watchlist rule is exceeded | not repeated within the quiet period (10 min) | per rule | Dashboard → **Watchlist** |
| **Caches cleared** — "Emptied over its limit: …" | an app cache passed its size limit and was emptied | each hourly check that emptied something | no | remove the limit in the Storage panel |

## Warnings without a notification

| Warning | Where |
|---|---|
| An item **glows red** (processor, memory, storage, temperature, battery, a failed Switch) | menu bar ([Menu bar](01%20Menu%20bar.md#red-warnings)) |
| *Sparewatt is running, but hidden* | an alert, once per run ([Menu bar](01%20Menu%20bar.md#hidden-item-check)) |
| Charger too small / near its limit | Power panel |
| Memory forecast (swap growing fast) | Memory panel |
| *Needs action* / *Worth a look* | dashboard Overview ([Mac health](11%20Dashboard%2C%20history%20and%20this%20app.md#overview-and-mac-health)) |

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
| every other notification | none | the panel it is about |

**Quit *app*** is the app's normal quit: it can ask to save first. It is never a force quit. When a menu bar part is
hidden, a click opens the matching dashboard page instead of its panel.

**Banners.** Sparewatt doesn't ask for permission at launch: its notifications start out *delivered quietly*, to
Notification Center only, with no banner or sound. To see banners, choose to keep them prominent in a notification's
menu, or turn banners on in System Settings → Notifications → Sparewatt. Turning Sparewatt off there silences them all.

**Limits.** When macOS won't let Sparewatt use the notification center (for example a copy run outside the app), it
falls back to a plain banner from macOS's scripting tool: no buttons, and a click doesn't open Sparewatt.
