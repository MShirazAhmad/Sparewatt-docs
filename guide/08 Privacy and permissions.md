# Privacy and permissions

## What stays on your Mac

Everything. Sparewatt collects nothing and sends nothing about you. It makes only two kinds of network request, both
your choice:

- the once-a-day update check against GitHub, **off** by default;
- a [Switch](../features/10%20Switches.md) whose running check is *a web address answers* asks that address (usually a
  server on your own Mac) every 10 seconds while a panel or the dashboard is open, otherwise once a minute.

If you turn on the [AI Assistant](../features/12%20AI%20Assistant.md)'s MCP server (off by default), Sparewatt also
**answers** requests, from programs on this Mac only (127.0.0.1; web pages are refused). While it is on, any program
running as you can read the readings, lists and history it offers. The clipboard, the Shelf and Latest File are never
offered. What an AI assistant does with what it reads is up to that assistant.

**Report…** and **Report a problem…** (Dashboard → This App) don't send anything themselves: they open a new GitHub
issue in your browser, filled in, with your name, the Mac's name and file paths removed from a crash log. You read it
and send it, or close it. The crash logs stay in `~/Library/Logs/Sparewatt/`.

The **"My Mac today"** and **"My Mac this week"** pictures are made only when you ask for them and hold only figures,
app names and the charger type: no file paths, user or folder names, or serial numbers. They go where you share or save
them.

Dashboard → **Privacy** lists every program Sparewatt starts, every place it reads or writes and every permission it
may ask for; [What Sparewatt runs and reads](10%20What%20Sparewatt%20runs%20and%20reads.md) is the same list.

The [charger history](../features/06%20Power.md#charger-history) is kept only on this Mac. So are your
[devices' battery levels](../features/05%20Battery.md#device-batteries) (30 days, for their time left), and
[data used per app](../features/03%20Temperature%2C%20network%20and%20storage%20space.md#data-used-per-app): macOS's own
`nettop` counts bytes per app on this Mac, and Sparewatt keeps only each app's bytes per day, for 14 days, with no
addresses or sites. An exported settings file goes only where you save it.

The clipboard history is kept in memory only and skips passwords. Entries you **pin** are saved, as plain text, in
Sparewatt's settings so they survive a restart — don't pin secrets.

## Prompts you may see

| Prompt | When | Why |
|---|---|---|
| "macOS cannot verify the developer" | first launch | the app is not signed with an Apple Developer ID ([Getting started](01%20Getting%20started.md)) |
| Administrator password | changing an energy mode, On Battery settings, Extreme Saver | these use macOS's own `pmset`, which needs an administrator each time |
| Login Items asks for your OK | sometimes, after turning on *Open Sparewatt when you log in* | macOS's own login-item service may want you to switch Sparewatt on in System Settings → General → Login Items |
| none for Full Disk Access (optional) | the Storage panel's *Last backup* says *needs Full Disk Access* | macOS shows Time Machine's backup dates only to apps with Full Disk Access (or while the backup disk is connected). The panel's *Open Privacy & Security* button opens the setting; without it, Sparewatt just doesn't show the date |
| "Sparewatt would like to access files in your Downloads folder" | the first *Look* in Downloads tidy-up | it reads the folder to find old installers and duplicate downloads |
| none for notifications | | they start out *delivered quietly* to Notification Center; choose banners, or turn them off, in System Settings → Notifications → Sparewatt |

Reading the numbers needs no permission.

## Folders

The storage list skips folders macOS protects (Desktop, Documents, Downloads, Library, Pictures, Movies, Music).
Latest File finds files through Spotlight, so it never opens Desktop or Documents itself; macOS also leaves those
folders out of Sparewatt's Spotlight results, so Latest File doesn't see new files there. Downloads is the exception:
Downloads tidy-up reads the folder when you click *Look*, after macOS has asked you once, and from then on Latest File
reads it too. Change that answer in System Settings → Privacy & Security → Files and Folders → Sparewatt.

## Deleting things

- Clearing a cache (after a confirmation), Downloads tidy-up and the Shelf's Trash button **move files to the Trash**,
  so they can be put back.
- The one thing that deletes outright: a cache **size limit** you set empties that cache when it grows past the limit —
  only ever inside `~/Library/Caches`.
- Quitting an app from Sparewatt is a normal quit (the app can ask to save). Force Quit asks you first.
- *Uninstall Sparewatt…* (Dashboard → This App) moves the files you tick to the Trash; the settings, if ticked, are
  cleared from macOS's settings store rather than moved, so export them first if you may want them again.
