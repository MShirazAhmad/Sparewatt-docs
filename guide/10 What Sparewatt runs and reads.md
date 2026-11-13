# What Sparewatt runs and reads

Everything Sparewatt starts, opens or asks for, in one list. The app shows the same list on its **Privacy** page (Dashboard → Privacy, or This App → *What Sparewatt runs and reads*); both are made from one table in the app, so they agree.

## The network

**Nothing is sent anywhere. The only network requests are the optional update check and Switches' web-address checks.**

- **Update check.** Off unless you turn it on (Menu Bar → General). Once a day it asks GitHub for the latest version number.
- **Switches' web-address checks.** Only for a Switch whose check is “a web address answers”: it asks that address — usually a server on your own Mac — every 10 seconds with a panel open, otherwise every minute.
- **Switches' port checks.** A Switch checked by its port connects to that port on this Mac (127.0.0.1); nothing leaves the Mac.
- **AI Assistant.** Off unless you turn it on. It listens on 127.0.0.1 only, so only programs on this Mac can reach it, and refuses requests from web pages. It answers; it never sends anything by itself.
- **Links you click.** Report a problem, Download and release notes open in your browser; Sparewatt itself sends nothing.

## Programs it starts

All are part of macOS. None runs with more rights than you have, except `pmset` after you type your password.

| Program | When | Why |
|---|---|---|
| `ps` | Every update while a list of apps is showing; every 30 seconds for the background watch; once a minute for Insights; when Extreme Saver pauses or resumes apps. | Lists running programs with their processor and memory use: the “using the most” lists, power per app, alerts, and which apps to pause. |
| `nettop` | One copy runs as long as Sparewatt does, read once a minute; another for one second while the Network panel's app list is open. | macOS's own counter of the internet data each app moves, for “data used per app”. Only bytes per app per day are kept — no addresses or sites. (A second macOS tool, script, gives nettop the kind of input it needs.) |
| `pmset` | As a battery or energy page opens; at most every 30 seconds while the Mac is hot; on battery, for the unused-app suggestions; once an hour for the wake list. | macOS's own power tool: reads the energy settings, why charging is on hold, the speed limit when hot, which apps play sound or video, and when the Mac woke. Changing an energy setting runs it with your password, through macOS's own password dialog. |
| `sh` | Only while Extreme Saver or Last until has apps paused. | A stand-by that wakes the paused apps if Sparewatt is force-quit: it waits for Sparewatt to go, then sends them the wake signal. It reads nothing. |
| `system_profiler` | Every 5 minutes. | Reads the battery level of Bluetooth headphones such as AirPods. |
| `du` | While the Storage folder list or the caches card is shown, at most every 10 minutes (sizes are remembered between runs). | Adds up the size of the folders in your home folder, and of each app's cache. Folders macOS protects (Desktop, Documents, Downloads, Pictures, Movies, Music) are skipped. |
| `tmutil` | Every 30 minutes, and when the Storage page opens. | Time Machine: whether a backup disk is set up, when the last backup was, and how many local snapshots there are. |
| `diskutil` | At launch and every 6 hours. | The internal drive's health (its SMART status). |
| `launchctl` | As the Startup Items page opens. | Which startup items are running now. |
| `zsh` | As you turn a Switch on or off, and to check a Switch whose check is a command (every 10 seconds with a panel open, otherwise every minute). | Runs the commands you typed for that Switch, as you, in its folder. Sparewatt runs no command you didn't write. |
| `pkill` | As a Switch is turned off. | Stops the programs that Switch started. |
| `ditto` | As you click Zip on the Shelf. | Makes the zip file. |
| `osascript` | Only when macOS's notification center can't be used by Sparewatt. | Shows a plain notification banner instead. |

Processor, memory, graphics, temperatures, fans, battery, charger and disk speed are read straight from macOS (IOKit, the SMC sensors and system calls); no tool is started for them. The graphics chip's watts come from macOS's energy counters (IOReport), read only while a panel that shows them is open.

The experimental Power by part card's *Calibrate* changes the screen brightness and the keyboard light and, only if you
tick *Wi-Fi too*, turns Wi-Fi off and on. It puts everything back afterwards.

## Files it reads and writes

| Where | Access | What |
|---|---|---|
| ~/Library/Application Support/Sparewatt | reads and writes | Its own data: history, chargers, data used per app, Switches, insights, unused-app timings, folder sizes, settings backups. |
| ~/Library/Logs/Sparewatt | reads and writes | Crash logs, and what each Switch prints. |
| Its settings, in macOS's settings store | reads and writes | Every setting, the Shelf list, Watchlist rules, profiles and pinned clipboard entries. |
| ~/Library/Caches | reads; moves to the Trash | Each app's cache size. A cache you clear goes to the Trash; a size limit you set empties that cache when it grows past it. |
| ~/Downloads | reads; moves to the Trash | Read when you click Look in Downloads tidy-up (macOS asks first), and by Latest File after that. What you choose to tidy goes to the Trash. |
| Your home folder, through Spotlight | reads | Latest File asks Spotlight for the newest file in the folders you chose; it opens no folder itself. |
| LaunchAgents and LaunchDaemons folders | reads | Startup Items: what is set to start by itself (yours, all users', system-wide). |
| Time Machine's settings file | reads | The last backup's date, only if you gave Sparewatt Full Disk Access. |
| The clipboard | reads | Clipboard history: recent copies, in memory only, passwords skipped. |
| Files you hand it | reads and writes | Files on the Shelf (moved, copied or zipped where you drop them), and settings, history or pictures you export — only where you save them. |

What each file in its own folders holds: [Data files](../reference/Data%20files.md).

## Permissions it may ask for

| Permission | When | Why |
|---|---|---|
| Administrator password | Each time you change an energy mode or the On Battery settings, and when Extreme Saver turns on or off. | These go through macOS's pmset, which needs an administrator. macOS shows the dialog; Sparewatt never sees the password. |
| Downloads folder | The first Look in Downloads tidy-up. | To find old installers and duplicate downloads. Change it in System Settings → Privacy & Security → Files and Folders. |
| Notifications | At first launch; they start out delivered quietly to Notification Center. | For the alerts you set up. Choose banners, or turn them off, in System Settings → Notifications. |
| Login Items | Sometimes, after you turn on “Open Sparewatt when you log in”. | macOS may want you to switch Sparewatt on in System Settings → General → Login Items. |
| Full Disk Access (optional) | Never asked; you can turn it on yourself. | Only to show the last Time Machine backup while the backup disk isn't connected. Nothing else changes without it. |

Reading the numbers needs no permission. More on privacy: [Privacy and permissions](08%20Privacy%20and%20permissions.md).

## Removing Sparewatt

Dashboard → This App → **Uninstall Sparewatt…** lists everything above that Sparewatt keeps on your Mac, with sizes. What you tick goes to the Trash (nothing is deleted outright), the login item and notifications are cleared, and Sparewatt quits. Apps Extreme Saver paused are resumed first; Switches that are on keep running. One date stamp of a few bytes stays (the latest time the Mac's clock showed).
