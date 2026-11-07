# How the estimates work

macOS measures how much power the **whole Mac** draws, but not how much each app draws. Sparewatt combines two readings
to estimate it:

1. **The Mac's draw in watts**, from the battery's own current and voltage (on the charger: charger power minus what
   goes into the battery).
2. **Energy impact** per process, the score Activity Monitor shows. On current macOS it equals the process's processor
   use as a percentage of one core (Sparewatt checked it process by process against Activity Monitor's own figures),
   so Sparewatt reads every process's processor time with one quick `ps` and compares it with the previous reading —
   usually seconds earlier. It tracks power, but it is not in watts.

## Watts per app

Some of the draw stays whatever you quit: the screen, the chip at rest, macOS itself. Sparewatt calls this the
**floor** and splits only the draw **above** it, by each app's share of the energy impact of **every** process:

> app watts = (Mac's draw − floor) × app's energy impact ÷ all processes' energy impact

An app's helpers (for example a browser's renderer processes) count towards that app when they live inside its bundle.

**Finding the floor.** Once a minute on battery, Sparewatt notes the Mac's draw and the total energy impact. A straight
line through those minutes (watts against energy impact) crosses zero energy impact at the floor. Until there are about
30 minutes of such readings, it uses the quietest 5% of your minutes on battery instead — a high guess, so early savings
lean low rather than high. The idle-app card says which method is in use.

## Battery time gained

With *E* watt-hours left in the battery, a draw of *W* watts and an app using *a* watts:

> time now = E ÷ W  time after quitting = E ÷ (W − a)  gained = the difference

Example: 41 Wh left. At 29 W, quitting an app that uses 1.2 W adds about 4 minutes. At 10 W, the same app adds about
34 minutes. Idle apps matter most when the Mac is otherwise quiet.

## The idle-app rule

On battery, once a minute, for every app with a Dock icon (not Finder, not Sparewatt):

1. **Not used**: the app has not been the front app for at least your idle limit (10 minutes by default). Apps that were
   already open when Sparewatt started count from Sparewatt's start.
2. **Average, not a spike**: its watts are averaged over the minutes it has been idle (up to 15), and only once there are
   enough readings (as many minutes as the idle limit, but at least 2 and at most 5).
3. **Worth it**: the battery time gained from that average is at least your limit (30 minutes by default; never below 5).
4. **Not busy for you**: apps playing sound or video — those keeping the display awake, or with audio running on their
   behalf — are left out.

"Not now" lasts until you plug in. Plugging in also clears the readings, so every battery stretch starts fresh.

## Limits of the method

- Safari's web pages run in a macOS process outside Safari's bundle, so their cost is counted under macOS, and Safari
  reads lower than it is.
- Energy impact over a short stretch is noisy; the idle-app rule averages it, the power-per-app chart shows the stretch
  since the previous reading (a few seconds while a panel is open).
- "Used" means "was the front app". An app you read on a second screen without clicking it counts as unused — add it to
  the never-suggest list.
- The weekly per-app battery card splits the whole draw by energy impact without the floor, so its numbers are larger.
