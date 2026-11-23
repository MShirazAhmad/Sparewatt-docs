# AI Assistant

**Purpose.** Let an AI assistant on your Mac — Claude Code, Codex, Cursor, LM Studio or any other app that speaks
MCP (the Model Context Protocol) — see what Sparewatt measures, so you can ask it *"why is my battery draining?"* or
*"what is using all my memory?"* and get an answer from live readings instead of guesses. The same page lets
[Shortcuts read Sparewatt's values](#reading-values-in-shortcuts), for automations of your own.

<p align="center"><img src="../images/screenshots/dashboard-ai-assistant.png" width="760" alt="AI Assistant page"></p>

---

## Turning it on

Dashboard (**⌥⌘R**) → **AI Assistant** → **MCP server**. It is **off** until you turn it on. Once on, the page says
*Listening on 127.0.0.1:7319*, and Sparewatt starts it again every time Sparewatt starts.

- **Port** — 7319 unless you change it (any number from 1024 to 65535). If another app already uses the port, the page
  says so; choose another and the server moves there.
- **Show Instructions** — what to give your assistant (below).

## Connecting an assistant

**Show Instructions** gives you one sentence to paste into any assistant, which then sets itself up:

> Please set up the MCP server named sparewatt at http://127.0.0.1:7319/mcp. It is a streamable HTTP server on this
> computer.

<p align="center"><img src="../images/screenshots/dashboard-connect-assistant.png" width="560" alt="Connect an Assistant"></p>

Or set it up yourself:

| Assistant | How |
|---|---|
| Claude Code | in Terminal: `claude mcp add --transport http sparewatt http://127.0.0.1:7319/mcp` |
| Codex | in `~/.codex/config.toml`: `[mcp_servers.sparewatt]` then `url = "http://127.0.0.1:7319/mcp"` |
| Cursor, LM Studio and others | in their `mcp.json`: `{"mcpServers": {"sparewatt": {"url": "http://127.0.0.1:7319/mcp"}}}` |

If you changed the port, use your port in place of 7319. Each copy button on the page already has the right port.

## What the assistant can do

**Always (reading only):**

| Tool | Gives |
|---|---|
| `get_overview` | everything at a glance: processor, graphics, memory with pressure and swap, storage, battery and charger, power draw, temperatures and fans, network and disk speed, Extreme Saver and energy modes, and the [Mac health](11%20Dashboard%2C%20history%20and%20this%20app.md#overview-and-mac-health) findings |
| `get_top_apps` | the [using the most](04%20Who%20is%20using%20it.md) list for processor, graphics, memory, energy, network or storage, each row explained in plain words |
| `get_app_processes` | every process behind one app (the app and its helpers) |
| `get_battery` | battery now, plus [wear](05%20Battery.md#battery-wear) per day, each stretch on battery and the [battery used per app](06%20Power.md#battery-used-per-app-last-7-days), for up to 30 days |
| `get_history` | the per-minute [History](11%20Dashboard%2C%20history%20and%20this%20app.md#history) (charge, watts, processor, temperature), up to 30 days |
| `get_insights` | unusual background processes, apps busy with no window, swap growth, what woke the Mac, [idle apps](06%20Power.md#idle-apps-on-battery) worth quitting, and your [Watchlist](04%20Who%20is%20using%20it.md#watchlist) with its recent alerts |
| `list_switches` | your [Switches](10%20Switches.md) and whether each is on, with its status line, progress in percent and log file when it has them |
| `open_dashboard` | opens a dashboard page on your screen, to show you something |

**Only with *Allow changes* on** (off until you turn it on):

| Tool | Does |
|---|---|
| `set_switch` | turns one of your Switches on or off |
| `quit_app` | quits an app as if you chose Quit — it can still ask you to save; macOS parts and Sparewatt itself can't be quit |
| `set_extreme_saver` | turns [Extreme Saver](07%20Power%20controls.md#extreme-saver) on or off — macOS asks you for your password (not on a Mac with no battery) |
| `set_energy_mode` | sets the [energy mode](07%20Power%20controls.md) for battery or charger (only the charger, wall power, on a Mac with no battery) — macOS asks you for your password |

With *Allow changes* off, these tools answer that changes are off, and the assistant can tell you where to allow them.

## Reading values in Shortcuts

`sparewatt://` [links](../reference/Links%20for%20Shortcuts%20and%20scripts.md) send commands. To get a figure back into a
shortcut (battery %, time left, processor use and so on), turn on **Let Shortcuts read values** in the *Shortcuts*
section of this page. It is **off** until you turn it on. It uses the same port as the MCP server and works whether or
not the MCP server is on.

- **One value:** add **Get Contents of URL** with `http://127.0.0.1:7319/now/battery_percent`. The result is the value as
  text (`82`), ready for **If**, **Calculate** or **Speak Text**.
- **Every value:** `http://127.0.0.1:7319/now` gives them all as a dictionary. Follow it with **Get Dictionary Value**
  and one of the keys below.

The page shows both addresses with copy buttons, with your port in them.

| Key | Gives |
|---|---|
| `battery_percent` | the charge, 0–100 |
| `battery_state` | the charge state in the menu bar's words: *On battery*, *Charging*, *Not charging* … |
| `plugged_in` | `true` or `false` |
| `time_left_minutes`, `time_left` | the battery time left, in minutes and the way Sparewatt writes it (`3h 10m`) |
| `time_to_full_minutes` | minutes until full, while charging |
| `battery_health_percent`, `battery_cycles` | wear: the full charge against a new battery's, and the cycle count |
| `mac_watts` | the Mac's power draw now |
| `processor_percent`, `graphics_percent`, `memory_percent` | load, 0–100 |
| `memory_pressure` | `normal`, `raised` or `critical` |
| `swap_gb`, `storage_free_gb` | swap in use, and free space on the startup disk |
| `processor_temperature_c` | the processor's temperature in °C |
| `download_mb_per_s`, `upload_mb_per_s` | network speed now |
| `energy_mode` | the energy mode in use now: *Automatic*, *Low Power* or *High Power* |
| `extreme_saver`, `keep_awake` | `true` or `false` |
| `profile` | the [profile](07%20Power%20controls.md#profiles) last applied |
| `time` | when the values were read |

A figure that doesn't exist right now (no battery, no time left while charging) is empty as text and `null` in the
dictionary, so a key never goes missing. Each read shows in *Activity* below, as *read battery_percent* from
*Shortcuts*.

**Why a web address and not Shortcuts actions of their own:** macOS runs an app's own Shortcuts actions only for apps
signed through an Apple developer account, which Sparewatt isn't yet.

## Activity

The page lists each assistant that connected, every tool it called and every value Shortcuts read since Sparewatt
started, newest first, with a mark for anything refused. Kept in memory only.

## Benefits

- Ask questions in plain words and get answers from real readings: *"Which app cost the most battery this week?"*,
  *"Is my Mac hot because of the GPU?"*, *"Did anything wake the Mac overnight?"*
- Works with whichever assistant you use; nothing is tied to one AI company.
- The assistant sees the same explanations you see, so it doesn't misread cryptic process names.

## Good to know

- **This Mac only.** The server listens on 127.0.0.1, so other computers can't reach it. Requests from web pages are
  refused, so a website can't read it through your browser.
- **No password.** While the server is on, any program running on this Mac as you can read these figures. Turn it off
  when you don't need it. The same goes for *Let Shortcuts read values*, which has the same protections: this Mac only,
  and every request from a web page is refused.
- **Never shared:** the clipboard, the Shelf and Latest File.
- Where the reading goes after that is up to your assistant: a cloud AI sends what it reads to its company like
  anything else you ask it.
- The server uses MCP's streamable HTTP transport. Old clients that only speak the earlier HTTP+SSE transport need a
  bridge such as `mcp-remote`.
