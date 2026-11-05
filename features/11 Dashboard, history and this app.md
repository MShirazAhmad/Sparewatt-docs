# Dashboard, history and this app

---

## Dashboard window

**Purpose.** Everything in one window — larger than the menu bar panels, with history and every setting.

**What it does.** **⌥⌘R** from any app (or the button in any panel header, or the right-click menu). A sidebar:

- **Monitor:** Overview, Processor, Graphics, Memory, Storage, Temperature, Network, Battery, Power flow, History — each
  with its current value beside it.
- **Control:** Switches, On Battery, Extreme Saver, Watchlist, Menu Bar, Startup Items, This App.

At the bottom: the Extreme Saver switch and, when there is one, *Version X is available*. While the window is open,
Sparewatt appears in the Dock and ⌘-Tab.

Monitor pages show the same cards as the panels plus dashboard-only ones: 24-hour trends, battery wear, the wake log, the
background-processes table, battery use per app this week.

---

## Overview and Mac health

**Purpose.** One look to know whether anything needs your attention.

**What it does.** The Overview starts with a health card — *All good*, or *1 needs action · 2 worth a look* — then eight
tiles (Processor, Graphics, Memory, Storage, Battery, Power flow, Temperature, Network), each with *Open*.

| Finding | Level |
|---|---|
| Battery state doesn't add up | needs action |
| A background process far above its normal | needs action |
| Storage under 10% free | needs action |
| Storage under 20% free | worth a look |
| Memory pressure critical / raised | needs action / worth a look |
| More than 4 GB spilled to disk (swap) | worth a look |
| Processor above 95 °C / above 85 °C | needs action / worth a look |
| Battery health under 80% | worth a look |
| On battery with under an hour left at this rate | needs action |

Click a finding to open its page.

**Use cases.** A morning check; or "the Mac feels off — is it anything?"

**Benefits.** Only lists what is actually unusual; *All good* means you can stop looking.

---

## History

**Purpose.** See how the Mac behaved over hours and days.

**What it does.** One reading a minute, kept 30 days. Charts of **battery charge**, **Mac power use**, **processor** and
**processor temperature** over 1 hour, 24 hours, 7 days or 30 days (lines break across sleep), battery health over the
period, and **Times on battery**: each stretch with start, length, from–to %, average watts and the apps that used the
most power.

**Export CSV…** saves everything stored (not just the chosen range): the minute readings, then the stretches on battery
with their top apps.

**Use cases.**
- "Why did the battery last only 3 hours yesterday?" — find the stretch and its top apps.
- Compare power use before and after a macOS update or a new app.
- Keep data for a battery-life comparison, or a support request.

**Where.** Dashboard → **History**; shorter trends on the Battery and Power flow pages.

---

## Startup Items

**Purpose.** See everything that starts on its own, and what it usually costs.

**What it does.** Lists launch agents and daemons — yours, for all users, and system-wide — with whether each is loaded
now, tags (*at login*, *restarts itself*, *disabled*), its usual processor use (learned by Sparewatt) and a Finder button.
Read-only; *Open Login Items settings* takes you to where macOS lets you turn them off.

**Use cases.** A new Mac feels slower after installing a few tools: find the background helpers they added.

---

## This App

**Purpose.** A monitor should not itself cost much. This page shows exactly what Sparewatt uses.

**What it does.** *Right now* (% of one core, memory), *average since launch*, macOS's energy impact for Sparewatt, the
update-speed setting, and a breakdown **by feature** (processor & memory readings, graphics, temperature sensors, fans,
network & disk speed, battery & power, top-apps lists, folder sizes, Latest File, background watch, drawing the menu
bar).

**Use cases.** Choose a slower update speed or turn off live diagrams if Sparewatt's own cost matters on battery.

---

## Updates

*Check GitHub once a day for a newer version* (Dashboard → Menu Bar → *General*) — **off** by default. When a newer
release exists, the dashboard sidebar and the right-click menu say so; nothing is downloaded or installed automatically.

---

## Moving from ResourceWarden

Sparewatt was called ResourceWarden until November 2026. The first launch copies its settings and moves its data and
logs; switch *Start Sparewatt when you log in* on again. See [Getting started](../guide/01%20Getting%20started.md#coming-from-resourcewarden).
