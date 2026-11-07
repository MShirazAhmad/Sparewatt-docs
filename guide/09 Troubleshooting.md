# Troubleshooting

## I can't see the menu bar item

macOS can hide menu bar items: in System Settings → Menu Bar (newer macOS asks per app), or under the camera notch when
the bar is full. Sparewatt notices once and tells you. Fixes: allow Sparewatt in System Settings → Menu Bar, keep
**Group all items into one** on, choose **Compact** text or small icons, or hide parts you don't need (Dashboard → Menu
Bar → *Show in the menu bar*). ⌥⌘R still opens the dashboard.

## A reading says n/a

This Mac has no such sensor or reading (for example fans on a fanless Mac). Sparewatt shows n/a instead of a made-up
zero.

## macOS asks for my password every time I change a power setting

Expected: energy modes, On Battery settings and Extreme Saver change system settings through `pmset`, which needs an
administrator each time.

## Notifications don't pop up as banners

Sparewatt's notifications start out *delivered quietly*: they go to Notification Center (click the date and time in the
menu bar) with no banner or sound, until you choose otherwise. To get banners, choose to keep them prominent in one of
its notifications, or turn banners on in System Settings → Notifications → Sparewatt. If they don't arrive at all,
check that Sparewatt is allowed there, macOS's Focus settings, and Sparewatt's own quiet hours (Dashboard → **Shelf,
Profiles & Alerts**). Clicking a notification opens the panel it is about; see
[Alerts and notifications](../features/08%20Alerts%20and%20notifications.md#notifications-with-buttons).

## I never get idle-app suggestions

- They appear on battery only.
- The app must be unused for your idle limit **and** be worth your gain limit. At a high draw, idle apps rarely reach
  30 minutes — try a lower gain limit on Dashboard → On Battery.
- Apps playing sound or video, apps on your never-suggest list and apps you chose *Not now* for (until you plug in) are
  left out.
- Right after unplugging, Sparewatt needs a few minutes of readings first.

## "Battery state doesn't add up"

The charge state macOS reports and the current actually flowing disagreed for a minute (for example "charging" while
the battery drains). Often a weak charger or cable; see the Power panel's charger check.

## Sparewatt itself uses too much

Dashboard → **This App** shows what each feature costs. Slower update speed, fewer live diagrams, and closing panels you
don't need all help.

## An app is still frozen after Extreme Saver

Apps Extreme Saver paused wake up when you turn it off, when Sparewatt quits (also when it is stopped with `kill`), and
at the next launch if Sparewatt crashed while they were paused. If Extreme Saver is still on at that launch, the apps
stay paused until you turn it off.

## My switches are gone, or one is missing

If `switches.json` can't be read in full, the Switches page says so at the top, and the file as it was is kept beside
it as `switches.json.bak` before anything is saved over it. A field left out of an entry is not a problem: it takes its
usual default. Fix the file (or copy the `.bak` back), then *Reload from file*.

## Downloads tidy-up says it can't see Downloads

macOS was told not to let Sparewatt read your Downloads folder. Allow it in System Settings → Privacy & Security →
Files and Folders → Sparewatt → *Downloads Folder* (the card's *Open Privacy & Security* button goes there), then click
*Look* again. Sparewatt isn't signed with a developer certificate, so a newly built copy may be asked again.

## Latest File doesn't show a file I just saved on the Desktop or in Documents

macOS leaves Desktop and Documents out of Spotlight results for Sparewatt, and Sparewatt doesn't ask for those folders,
so Latest File can't see them; the card says so. For Downloads, click *Look* in Downloads tidy-up once (in each newly
built copy); from then on Latest File reads Downloads too.

## My chargers are gone, or one is missing

If `chargers.json` can't be read in full, the *Chargers* card (Dashboard → **Power flow**) says so, and the file as it
was is kept beside it as `chargers.json.bak` before anything is saved over it. Two identical chargers that don't report
a serial number show as one.

## Sparewatt crashed, or something is wrong

After a crash, Dashboard → **This App** shows *Sparewatt crashed on …*. **Report…** opens a new GitHub issue in your
browser with the start of the crash log, your name and file paths removed; read it, add what you were doing, and send
it if you want to. **Show log** shows the full log in Finder (`~/Library/Logs/Sparewatt/`). For anything else, **Report
a problem…** on the same page opens an issue with the app and macOS versions filled in. Nothing is sent by itself.

## Known issues

- Safari's cost is counted partly under macOS (see [How the estimates work](07%20How%20the%20estimates%20work.md#limits-of-the-method)).
