# Getting started

## Install

1. Download **Sparewatt.dmg** from the app's latest release.
2. Open it and drag **Sparewatt** onto **Applications**.
3. Open Sparewatt. It lives in the menu bar only — no Dock icon, no window — until you open the dashboard.

A `.zip` of the app is in each release too, if you prefer.

**Needs** macOS 14 (Sonoma) or later, on Apple silicon or Intel.

## "macOS cannot verify the developer"

Sparewatt is not signed with an Apple Developer ID, so the first launch shows this warning. Either:

- right-click the app → **Open** → **Open**, or
- remove the download flag in Terminal:

```bash
xattr -dr com.apple.quarantine /Applications/Sparewatt.app
```

You only do this once.

## First look

- The menu bar shows **one compact item** with live readings (processor, graphics, memory, storage, temperature, battery, power).
- **Hover** over any part of it to open that part's panel. Click to keep it open.
- **⌥⌘R** opens the dashboard window from anywhere: every monitor on the left under *Monitor*, every setting under *Control*.
- Right-click the menu bar item for the dashboard, settings, Extreme Saver and Quit.

## VoiceOver

Every panel, chart, diagram, meter and icon button reads as words, with units spelt out. The menu bar item reads as one
sentence ("cpu 12%, ram 54%…"); the power flow says "the 65-watt charger gives 44 watts to the Mac and 17 watts to the
battery"; a graph says its latest reading, average and peak; list rows read like "Xcode, App, 4.2%, button", with
Notify and Quit as actions.

## Start at login

Dashboard → **Menu Bar** → **Start Sparewatt when you log in**. macOS may ask once whether Sparewatt may control
*System Events*; that is how the login item is added.

## Updating from Sparewatt 1.4

Later versions use the bundle ID `local.ahmad.Sparewatt` (1.4 used `app.sparewatt.Sparewatt`). The first launch
copies your 1.4 settings once; history, switches and logs stay where they are, in folders named Sparewatt. macOS
asks again, once each, for Downloads access and for control of *System Events* (the login item).

## Updates

The update check is **off** by default. Turn it on in Dashboard → Menu Bar → General → *Check GitHub once a day for a
newer version*.
