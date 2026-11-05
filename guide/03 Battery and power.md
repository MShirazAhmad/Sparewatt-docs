# Battery and power

## Power per app

The Power panel's pie splits the Mac's **measured** draw between apps by their *energy impact* (the score Activity
Monitor shows).

- **On the charger** it shows watts per app.
- **On battery** it shows each app's share of the drain and, beside it, **how much battery time that app takes** — the
  time you would get back by quitting it.

Click a slice or a name to see that app's processes (energy, processor, memory, owner) and **Quit** or **Force Quit**
the ones you own. Force Quit asks first, because unsaved work is lost.

These are estimates; macOS does not measure power per app. [How the estimates work](07%20How%20the%20estimates%20work.md)
explains the method.

## Idle apps on battery

Apps you left open hours ago can keep costing battery. On battery, Sparewatt suggests quitting an app when **both** are
true:

1. you have not brought it to the front for a while — **10 minutes** by default, and
2. quitting it would add at least a set amount of battery time — **30 minutes** by default.

The suggestion appears as a card, *Not in use, still costing battery*, in the Battery and Power panels:

- **Quit** — a normal quit, so the app can still ask to save.
- **Not now** — not again until you plug in.
- **Never suggest** this app.

You also get **one notification per app each time you unplug**, only while you are at the Mac and outside quiet hours.
Clicking the notification does not open Sparewatt; the Quit button is in the panel.

Never suggested: apps playing sound or video, Finder, and Sparewatt itself.

**Settings:** Dashboard → **On Battery** → *Apps you aren't using* — the switch, both limits, the notification, and the
never-suggest list. The slider icon on the card opens the same page.

If you rarely see a suggestion, that is usually right: at a high draw (say 25 W), an idle app has to use several watts
before quitting it adds 30 minutes.

## Charge plan

"At your usual 14 W you reach 20% around 10:44 PM." *Usual* is your last 30 minutes on battery, or your recent
stretches on battery when you have just unplugged. On the charger it reads *If you unplug now*.

## Battery wear

One reading a day, kept a year: health (how much the battery holds now compared with new), recharges per month, health
lost per month, and when it would reach 80% at that rate. Above 80% health is good.

## Charger check

Plugged in, but the battery still draining? The Power panel says the charger is too small for what the Mac is using
(or the cable is poor), and warns when a small charger is close to its limit.

## While asleep

What woke the Mac in the last 24 hours (lid, you, scheduled timers, Power Nap, network, USB), and how much charge the
longest sleep cost — flagged when it lost more than a sleeping Mac should.

## Battery used per app, last 7 days

The measured draw split by energy impact, added up a minute at a time while on battery, shown in watt-hours and as a
share of a full charge.

## Busy with no window on screen

Apps that are hidden or have no window on screen but keep the processor busy (10% by default) are listed, with a
notification after 10 minutes.
