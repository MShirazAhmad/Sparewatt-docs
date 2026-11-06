# Controls

All controls are pages under **Control** in the dashboard (⌥⌘R).

## Energy modes

**Automatic**, **Low Power** or **High Power**, set separately for battery and charger, from the Battery panel's
*Energy mode* card. Changing one uses macOS's own `pmset`, so macOS asks for your administrator password each time.

## On Battery

What the Mac may do when unplugged: Low Power mode, when the screen turns off, when the Mac sleeps, disk sleep, dimming,
Power Nap, staying online while asleep, waking for network access, deep sleep (standby). Change the values, then
**Apply** (asks for your password). Your charger settings are not touched. If the Mac would sleep before the screen
turns off, the page warns you.

The same page holds the idle-app suggestion settings (*Apps you aren't using*); those save at once and need no
password. See [Battery and power](03%20Battery%20and%20power.md#idle-apps-on-battery).

## Extreme Saver

One switch for the times battery matters most:

- applies the battery settings you tick (each row says what it will set),
- **pauses chosen apps** — they stay open but use no power until Extreme Saver is off; optionally also any background
  app above an energy score you choose (the app you are using is never paused),
- can **turn on by itself** at a battery level, and **off when you plug in**,
- can make Sparewatt itself check only every 30 seconds.

Don't pause apps you are working in: they freeze until the switch is off. Quitting Sparewatt wakes them too, so
nothing stays frozen once it is gone. ⌥⌘E toggles Extreme Saver from anywhere.

## Profiles

**Lecture**, **Lab** and **Travel**: energy modes for battery and charger plus Extreme Saver, applied in one click from
the top of the Battery panel. Each change asks for your password; a profile is marked as the current one only when every
change went through. Edit their names, icons and choices on Dashboard → **Shelf, Profiles & Alerts** (click a
profile's icon to pick another).

## Watchlist

Click the bell next to an app in a list to be told when it uses more than a limit of processor, graphics, memory or
energy — by default only on battery.

## Shelf, Profiles & Alerts

One page for the profiles' names, icons and choices, the Shelf's options, quiet hours, the low-storage and "busy with no
window" alerts, and the list of keyboard shortcuts.

## Switches

Any local service as an on/off switch: Django, Apache, nginx, Ollama, LM Studio, llama.cpp, MCP servers, Docker,
PostgreSQL, Redis, launchd jobs, or your own start/stop commands. Sparewatt checks whether each one is running by port,
URL, process or command. A switch can stop on battery and start with the app. Toggle them from the SWITCH part of the
menu bar, its right-click menu, or the Switches page (with an editor and each switch's log).

## Alerts and quiet hours

- When processor, memory or temperature stays above its limit for a number of minutes (5 by default).
- When a background process uses far more than it usually does (on battery, or always).
- When free storage drops below a limit (20 GB by default).
- Once, if macOS or the notch hides the menu bar item.

**Quiet hours** (off by default, 22:00–07:00) silence every notification.

The first and second alerts are set on Dashboard → Menu Bar → *Warnings*. The storage limit, quiet hours and the
"busy with no window" alert are on Dashboard → **Shelf, Profiles & Alerts**.

## Startup items

Everything that starts on its own when you log in or the Mac starts, and what each usually costs. Turn items off in
System Settings → General → Login Items & Extensions.
