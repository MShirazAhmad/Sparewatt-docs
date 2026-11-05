# Battery

---

## Real battery readings and charge state

**Purpose.** Know exactly how much charge is in the battery and what it is really doing — not a rounded percentage and
an icon that can be wrong.

**What it does.** Reads the battery controller directly (every 2 seconds by default, and at once when you plug in or
unplug):
- the **real fill** to 0.1% (charge now ÷ what the battery holds when full);
- watt-hours left, voltage, the current in and out;
- the Mac's **total draw** — from the battery on battery, from charger power minus what goes into the battery when
  plugged in;
- one shared **charge state**, decided from the current actually flowing:

| State | When |
|---|---|
| On battery | unplugged |
| Charging / Topping up | plugged in and at least 0.5 W going into the battery (Topping up when already at 100%) |
| On hold · Optimized Charging | plugged in, not charging, macOS holding the charge to protect the battery |
| At charge limit | plugged in, held at the limit you set in System Settings |
| Full · battery idle / Not charging | plugged in, nothing flowing |

**In the menu bar** the battery part shows `4:58 LEFT` on battery, or ⚡︎ CHARGING, ⚡︎ TOPPING UP, ⏸︎ ON HOLD, ⇥ AT LIMIT,
✓ FULL, over the fill.

**Use cases.**
- Before leaving for a meeting: is it really 81%, and is it actually charging or just "on hold"?
- macOS shows 100% but the battery isn't full: see the real fill (macOS rounds up near full).

**Benefits.** One consistent wording everywhere (menu bar, panels, dashboard), based on measured current — the true
state, not a guess.

**Where.** Battery part of the menu bar; Battery panel; Dashboard → **Battery**.

---

## Battery card

**What it shows.** A battery picture (green while charging, teal while resting on the charger, red at 20% and below),
the fill, macOS's time estimate, **health** (what it holds now vs when new — green from 80%), *Charge now*, *Holds at
most*, *Held when new* (mAh), *Full recharges*, *Battery temp*, and *Health means* Good or Worn.

**Use cases.** Check whether a battery is worn enough to replace (Apple counts below 80% as worn); compare recharges
with the age of the Mac.

---

## "Battery state doesn't add up"

**Purpose.** Catch the moments when the reported state and the actual current disagree — a charge limiter that isn't
holding, a weak charger, a bad cable.

**What it does.** Raises a warning when one of these lasts a full minute:
- macOS says *not charging*, yet more than 1 W flows into the battery (a charge limiter may not be holding);
- plugged in, but the battery drains by more than 1 W (charger too weak for this load, or cable/port not delivering);
- charging should be *on hold*, yet the battery gained at least 1% in 5 minutes or more.

**Where.** An orange card at the top of the Battery panel; a *Needs action* item on the dashboard's Overview; the
battery part glows red; and one notification per episode: *Battery state doesn't add up*.

**Benefits.** Problems that otherwise go unnoticed for weeks (a battery kept at 100% against your limit, a laptop
draining on a too-small charger) are caught in a minute.

---

## Charge plan

**Purpose.** Plan the day: when will the battery reach 20%, and when will it run out?

**What it does.** "At your usual 14 W you reach 20% around **4:40 PM** (2h 10m), empty around 6:05 PM."
*Usual* is the average of your last 30 minutes on battery, or of your last few battery stretches when you have just
unplugged. Below 20%: "about 35 min left at your usual use". On the charger, the card reads **If you unplug now**.

**Use cases.**
- A long lab day: know whether you need the charger before the afternoon session.
- Before unplugging for a lecture: will it last?

**Benefits.** Based on **your** use, so it doesn't swing with every momentary spike the way macOS's time estimate does.

**Where.** Battery panel.

---

## Charge limit shortcut

A button opens macOS's own **Charge Limit** (System Settings → Battery), which protects the battery without extra
software. Sparewatt itself never sets a limit.

---

## Battery wear

**Purpose.** See how fast the battery is aging and when it will count as worn.

**What it does.** Records health and recharge count once a day, keeps a year, and shows the line, **health now**,
**points lost per month**, **recharges per month**, and "At this rate it reaches 80% in about N months."

**Use cases.** Decide whether charging habits (always at 100%, hot desk) are wearing the battery; plan a battery service.

**Where.** Dashboard → **Battery**.

**Limits.** The trend appears after a few days of readings.

---

## While asleep (last 24 hours)

**Purpose.** Find out why the battery dropped overnight.

**What it does.** Reads macOS's power log and counts what woke the Mac in the last day, in plain words: *Lid opened*,
*You (keyboard, mouse)*, *Scheduled timer*, *Maintenance (Power Nap)*, *Sleep service (network, mail, iCloud)*,
*Wi-Fi / network*, *USB device*, *Charger / power events*… Background wakes (screen stays off) are marked. It also shows
the **longest sleep** and how much charge it cost, flagged when it lost more than 3 points.

**Use cases.** The MacBook loses 15% in a night with the lid closed: see whether Power Nap or network wakes are the
cause, then switch them off on the **On Battery** page.

**Where.** Dashboard → **Battery**.

---

## Battery history and stretches on battery

**Purpose.** Look back at how the battery was used.

**What it does.** One reading a minute (charge, the Mac's draw, processor, temperature, health), kept 30 days, and a
log of **every stretch on battery**: when, how long, from what % to what %, average watts, and the apps that used the
most power. See [Dashboard, history and this app](11%20Dashboard%2C%20history%20and%20this%20app.md) for the charts and
CSV export.

**Use cases.** "Yesterday's 4-hour session cost 60% — which apps?"
