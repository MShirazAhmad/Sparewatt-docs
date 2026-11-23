# Developer guide

For people who run their own servers, scripts and scheduled jobs on a Mac, and want Sparewatt to start, stop, watch
and report on them. It covers setting up switches, showing a job's progress and log, driving Sparewatt from scripts,
and where each feature is documented.

- [Set up a switch](#set-up-a-switch)
- [Choose the running check](#choose-the-running-check)
- [Show progress for a long job](#show-progress-for-a-long-job)
- [Point the log button at the right log](#point-the-log-button-at-the-right-log)
- [Worked example: a nightly cloud backup](#worked-example-a-nightly-cloud-backup)
- [More status commands](#more-status-commands)
- [Write switches.json by hand or from a script](#write-switchesjson-by-hand-or-from-a-script)
- [Drive Sparewatt from scripts](#drive-sparewatt-from-scripts)
- [When a switch misbehaves](#when-a-switch-misbehaves)
- [Every feature, and where it is explained](#every-feature-and-where-it-is-explained)

---

## Set up a switch

A switch is three things: how to start something, how to stop it, and how to tell whether it is running.

1. Open the dashboard (⌥⌘R) → **Switches** → **Add switch**. Pick a preset close to what you run, or *Any command*.
2. Fill in the fields:

| Field | What to type |
|---|---|
| Name, group, icon | how it is listed; switches with the same group sit under one heading |
| Start command | the command you would type in Terminal |
| Stop command | how to stop it; leave empty and Sparewatt stops what the start command launched |
| Run in folder | the project folder, when the command needs one |
| Running when | the check that says it is on ([below](#choose-the-running-check)) |
| Open in browser | its address, if it has a web page |
| Status command, Log file | for jobs that report progress ([below](#show-progress-for-a-long-job)) |
| Stop on battery | stop when you unplug, start again on the charger |
| Start when Sparewatt starts | turn on at launch |

3. Click **Test** next to the check, with the service running and again with it stopped. It should say *Running now*
   and *Not running now*.
4. **Add**, then flip the switch.

Commands run as you, in your login shell (`zsh -l`), so tools installed with Homebrew, pyenv or nvm are found.
Everything the start and stop commands print goes to `~/Library/Logs/Sparewatt/<name>.log`.

The full field list and the presets are on the [Switches](../features/10%20Switches.md) page.

## Choose the running check

| What you run | Check to use | Value |
|---|---|---|
| A server on a port | A port answers | `8000` |
| A server with a health address | A web address answers | `http://127.0.0.1:11434/api/version` |
| A script with no port | A process is running | text from its command line, e.g. `sync_photos.py` |
| A launchd job | A command succeeds | `launchctl print gui/$(id -u)/com.example.backup \| grep -q "state = running"` |
| A Docker container | A command succeeds | `docker ps -q -f name=db -f status=running \| grep -q .` |
| A Homebrew service | A port answers, or A command succeeds | `brew services list \| grep -q "^redis *started"` |
| A one-off command Sparewatt starts | Started by this app | nothing |

A command check has 4 seconds and counts as on when it exits with 0. Prefer a port or process check where one fits:
they cost less than starting a command every 10 seconds.

## Show progress for a long job

*From Sparewatt 1.30.*

On and off is enough for a server. A backup, a download or a queue should also say how far it has got. Give the switch
a **status command**: any command that prints one line about the job.

- While the switch is on, Sparewatt runs it at every check and shows the last line it printed under the switch's name.
- If that line has a percentage (`42%`), a bar is drawn too.
- If it prints nothing, the row shows *On since 09:12* as before.

The simplest status command reads the end of the log the job already writes:

```
tail -n 1 ~/Library/Logs/my-job.log
```

When the log mixes progress lines with other lines, keep only the progress ones:

```
tail -n 200 ~/Library/Logs/my-job.log | grep '%' | tail -n 1
```

Rules that keep it cheap and readable:

- It must end within 4 seconds. Read the tail of a log; don't scan a whole large file.
- One short line. Only the last line with text is shown, up to 160 characters.
- It runs only while the switch is on, every 10 seconds while a panel or the dashboard is open, otherwise once a minute.
- Use **Test** in the editor to see exactly what the row will show.

## Point the log button at the right log

Each row has a log button. By default it opens the switch's own log, which holds what the start and stop commands
printed. That is the right log for a server started directly (`ollama serve`, `python manage.py runserver`).

It is the wrong log for anything started through a manager. `launchctl kickstart …`, `brew services start …` and
`docker start …` print a line and return; the service writes its log elsewhere. Put that path under **Log file**:

| Started with | Its log is usually |
|---|---|
| launchd (`launchctl`) | the `StandardOutPath` / `StandardErrorPath` in its plist, or the file the script writes |
| Homebrew services | `$(brew --prefix)/var/log/<name>.log` |
| rclone, rsync | the file given to `--log-file` |
| Docker | no file: use `docker logs`, e.g. status command `docker logs --tail 1 db 2>&1` |

Sparewatt opens that file and never writes to it.

## Worked example: a nightly cloud backup

A script backs a folder up to cloud storage with rclone. launchd runs it every night under the label
`com.example.backup`. The goal: one switch that shows whether a backup is running, starts or stops one by hand, shows
how far it is, and opens the real log.

**1. Make the job write progress.** In the script, give rclone a log file and a short stats interval:

```
rclone sync ~/Documents remote:Documents \
  --stats 30s --stats-one-line \
  --log-level INFO --log-file "$HOME/Library/Logs/backup.log"
```

Every 30 seconds rclone then adds a line like:

```
2026/11/23 09:14:02 INFO  :     1.204 GiB / 4.011 GiB, 30%, 2.114 MiB/s, ETA 22m7s
```

**2. Add the switch.**

| Field | Value |
|---|---|
| Name / group | `Cloud backup` / `Backups` |
| Start command | `launchctl kickstart gui/$(id -u)/com.example.backup` |
| Stop command | `launchctl kill TERM gui/$(id -u)/com.example.backup` |
| Running when | A command succeeds: `launchctl print gui/$(id -u)/com.example.backup \| grep -q "state = running"` |
| Status command | `tail -n 400 ~/Library/Logs/backup.log \| grep -E 'INFO +: +[0-9.]+ ?[A-Za-z]* / ' \| tail -n 1 \| sed -E 's/^.*INFO +: +//'` |
| Log file | `~/Library/Logs/backup.log` |

**3. What you get.** While a backup runs, the row reads `1.204 GiB / 4.011 GiB, 30%, 2.114 MiB/s, ETA 22m7s` with a
bar at 30%, in the dashboard and in the menu bar panel. The log button opens `backup.log`. When the run ends the
switch goes off by itself, because the check no longer finds the job running. The nightly schedule stays with launchd:
the switch only watches the job and lets you start or stop a run.

Good to know: rclone's percentage is of the files it has found so far. With a large folder it can read 100% early and
drop again as more files are found.

## More status commands

| Job | Status command | Row shows |
|---|---|---|
| rsync with `--info=progress2 --log-file` or output sent to a file | `tail -c 200 ~/Library/Logs/rsync.log` | `1,204,011,008  30%  2.11MB/s  0:22:07` |
| A download with curl or wget writing to a log | `tail -c 200 ~/Library/Logs/download.log` | the progress line being redrawn |
| A model being pulled | `tail -n 1 ~/Library/Logs/pull.log` | `pulling 8eeb52dfb3bb: 61%` |
| A queue of files | `echo "$(ls ~/queue/done \| wc -l \| tr -d ' ') of $(ls ~/queue/all \| wc -l \| tr -d ' ') files"` | `37 of 120 files` |
| The same, with a bar | `d=$(ls ~/queue/done \| wc -l); a=$(ls ~/queue/all \| wc -l); echo "$d of $a files, $((100*d/a))%"` | `37 of 120 files, 30%` |
| A server's request count | `curl -s -m 2 http://127.0.0.1:8000/health` | whatever one line it returns |
| A Docker container | `docker logs --tail 1 db 2>&1` | its latest log line |
| A job that writes its own status file | `cat ~/.cache/my-job/status.txt` | that line |

Tools that redraw one progress line (curl, wget, rsync) separate the redraws with carriage returns, not new lines;
Sparewatt shows what was drawn last. `tail -c 200` reads the end of such a log quickly.

Your own script can report in the simplest way: write one line to a status file whenever it makes progress, and use
`cat` on it as the status command.

## Write switches.json by hand or from a script

Switches are kept in `~/Library/Application Support/Sparewatt/switches.json`, a plain list you can edit, generate or
copy to another Mac. After changing it, use **Reload from file** in the Switches page's menu.

```
[
  {
    "name": "Cloud backup",
    "group": "Backups",
    "icon": "icloud.and.arrow.up",
    "start": "launchctl kickstart gui/$(id -u)/com.example.backup",
    "stop": "launchctl kill TERM gui/$(id -u)/com.example.backup",
    "check": "command",
    "checkValue": "launchctl print gui/$(id -u)/com.example.backup | grep -q \"state = running\"",
    "status": "tail -n 1 ~/Library/Logs/backup.log",
    "logFile": "~/Library/Logs/backup.log"
  }
]
```

| Key | Values | Default |
|---|---|---|
| `name` | text | `Unnamed switch` |
| `start` | command | empty |
| `stop` | command | empty: stop what `start` launched |
| `check` | `port`, `url`, `process`, `command`, `none` | `port` |
| `checkValue` | port number, address, process text or command | empty |
| `group` | text | `Services` |
| `icon` | an SF Symbols name | `switch.2` |
| `openURL` | address | empty |
| `folder` | path, `~` allowed | home |
| `status` | command (from 1.30) | empty |
| `logFile` | path, `~` allowed (from 1.30) | empty |
| `stopOnBattery`, `startWithApp` | `true` / `false` | `false` |
| `id` | any unique text | made for you |

A key you leave out takes its default. An entry that is not a switch is skipped, and the file as it was is kept as
`switches.json.bak` before anything is saved over it. More in [Where Sparewatt keeps its data](../reference/Data%20files.md).

## Drive Sparewatt from scripts

| You want to | Use |
|---|---|
| Turn a switch on or off from a script, Shortcuts or a hotkey tool | `open "sparewatt://switch/Cloud%20backup/on"` (also `/off`, `/toggle`): [Links for Shortcuts and scripts](../reference/Links%20for%20Shortcuts%20and%20scripts.md) |
| Open a panel or a dashboard page | `sparewatt://panel/switches`, `sparewatt://dashboard/switches` |
| Read battery %, time left, watts and more as plain values | `GET http://127.0.0.1:7319/now` once *Reading values in Shortcuts* is on: [Reading values in Shortcuts](../features/12%20AI%20Assistant.md#reading-values-in-shortcuts) |
| Let an AI assistant read readings and switch states | the built-in MCP server; `list_switches` includes each switch's status line and progress: [AI Assistant](../features/12%20AI%20Assistant.md) |
| Change energy mode, Extreme Saver, keep awake or a profile | their `sparewatt://` links, same reference page |
| Move your set-up to another Mac | *Export settings…* on This App: [Your settings](../features/11%20Dashboard%2C%20history%20and%20this%20app.md#your-settings-export-import-welcome-again) |

## When a switch misbehaves

| You see | Likely cause | What to do |
|---|---|---|
| *Didn't come up — see its log* | the start command failed, or the check looks in the wrong place | open the log; run **Test** on the check while the service runs |
| *Start command ended with code N* | the command exited at once with an error | the log has its message; check the folder and the path |
| *Still running — check the stop command* | the stop command didn't stop it | run the stop command in Terminal and read what it says |
| On, but no status line | the status command printed nothing or took over 4 seconds | **Test** it in the editor; read less of the log |
| A status line but no bar | the line has no percentage between 0 and 100 | add one to the line, as in the queue example above |
| The log button opens an almost empty file | the service writes its log elsewhere | set **Log file** |
| A command works in Terminal but not here | it relies on something set only in an interactive shell | put it in `~/.zprofile`, or use full paths |

More in [Troubleshooting](09%20Troubleshooting.md).

## Every feature, and where it is explained

| Feature | Page |
|---|---|
| Menu bar readings, panels, colours, warnings | [Menu bar](../features/01%20Menu%20bar.md) |
| Processor, graphics, memory | [Processor, graphics and memory](../features/02%20Processor%2C%20graphics%20and%20memory.md) |
| Temperature, fans, network, data per app, storage, other disks | [Temperature, network and storage space](../features/03%20Temperature%2C%20network%20and%20storage%20space.md) |
| Which process is using what; quitting; Watchlist | [Who is using it](../features/04%20Who%20is%20using%20it.md) |
| Battery state, charge plan, wear, what keeps the Mac awake | [Battery](../features/05%20Battery.md) |
| Power flow, chargers, watts per app, idle apps | [Power](../features/06%20Power.md) |
| Energy modes, On Battery settings, Extreme Saver, keep awake, profiles | [Power controls](../features/07%20Power%20controls.md) |
| Notifications and their buttons | [Alerts and notifications](../features/08%20Alerts%20and%20notifications.md) |
| Latest File, Shelf, caches, Downloads tidy-up, clipboard | [Files and storage](../features/09%20Files%20and%20storage.md) |
| Switches, progress and logs | [Switches](../features/10%20Switches.md) |
| Dashboard, history, share cards, widgets, settings export | [Dashboard, history and this app](../features/11%20Dashboard%2C%20history%20and%20this%20app.md) |
| MCP server and values for Shortcuts | [AI Assistant](../features/12%20AI%20Assistant.md) |
| Every program Sparewatt starts and every file it touches | [What Sparewatt runs and reads](10%20What%20Sparewatt%20runs%20and%20reads.md) |
| Data files, links, keyboard shortcuts | [Data files](../reference/Data%20files.md), [Links](../reference/Links%20for%20Shortcuts%20and%20scripts.md), [Keyboard shortcuts](../reference/Keyboard%20shortcuts.md) |
