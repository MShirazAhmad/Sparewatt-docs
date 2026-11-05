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

## Start at login

Dashboard → **Menu Bar** → **Start Sparewatt when you log in**. macOS may ask once whether Sparewatt may control
*System Events*; that is how the login item is added.

## Coming from ResourceWarden

Sparewatt is the same app under a new name. On its first launch it:

- copies your ResourceWarden settings,
- moves your history, battery calibration and other data from `~/Library/Application Support/ResourceWarden`
  to `~/Library/Application Support/Sparewatt`, and the switch logs from `~/Library/Logs/ResourceWarden` to
  `~/Library/Logs/Sparewatt`.

It does **not** move the login item. If ResourceWarden started at login, switch **Start Sparewatt when you log in** on
again, and delete the old ResourceWarden app.

## Updates

The update check is **off** by default. Turn it on in Dashboard → Menu Bar → General → *Check GitHub once a day for a
newer version*.
