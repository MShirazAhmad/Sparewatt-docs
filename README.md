<p align="center"><img src="images/icon.png" width="128" alt="Sparewatt icon"></p>

<h1 align="center">Sparewatt documentation</h1>

<p align="center">
<a href="https://github.com/MShirazAhmad/Sparewatt-docs/releases/latest"><img src="https://img.shields.io/github/downloads/MShirazAhmad/Sparewatt-docs/total?label=downloads&color=2ea44f&style=for-the-badge" alt="Total downloads"></a>
<a href="https://github.com/MShirazAhmad/Sparewatt-docs/releases/latest"><img src="https://img.shields.io/github/v/release/MShirazAhmad/Sparewatt-docs?label=latest" alt="Latest release"></a>
<img src="https://img.shields.io/badge/macOS-14%2B-blue" alt="macOS 14 or later">
<img src="https://img.shields.io/badge/price-free-brightgreen" alt="Free">
</p>

<p align="center">How to use Sparewatt, the macOS menu bar app that shows what your Mac's processor, graphics, memory, storage, battery and power are doing — and helps you keep battery time for the things you actually use.</p>

<p align="center"><img src="images/linkedin-cover.jpg" width="900" alt="Sparewatt: a free menu bar monitor and power saver for macOS"></p>

<p align="center"><img src="images/sparewatt-demo.gif" width="900" alt="Sparewatt in 30 seconds"></p>

This repository holds **documentation only** — no app code. The app itself lives in its own repository.

## Why I built Sparewatt

I used to pay for several small Mac apps, each for a feature or two: one for clipboard history, one for drag and
drop, another for power management. My 16-inch MacBook Pro (2021) has an M1 Max chip and 64 GB of memory, and I work it hard.
As soon as I unplugged it, the battery ran out in about an hour — even though its battery health was above 90%.

My hobby is playing with offline AI models (LLMs) and MCP connections, so whenever my Mac is idle I keep its graphics
chip running at 100%. Over time I found that many of these services stay running in the background, keeping ports
busy. When I wanted to use the laptop on battery for a long stretch, it still drained very fast, and I had no way of
finding out why. So I put everything I needed into the menu bar:

- **Switch** — turn any background service on or off with one click, to save battery when I need to. ([Switches](features/10%20Switches.md))
- **GPU / CPU** — see and track whether some unknown service is wasting the graphics chip or processor.
- **RAM** — quickly check whether an LLM model is loaded in memory.
- **Storage free** — the free space itself, not the percentage full.
- **Net** — internet traffic, up and down.
- **Battery status** — true tracking from the battery's measured charge (mAh), not just a rounded percentage.
- **Adapter** — clearly shows where the power comes from and which part is taking it. ([Power](features/06%20Power.md))

So I started listing what I actually needed. When I need the battery to last, which app should I close? Which apps
can keep running without costing much? What is quietly draining it right now? I kept asking an AI coding assistant to
add one more feature, then another, and along the way those small requests became an app of my own.

Today Sparewatt helps the same Mac last **more than five hours on battery**. It also lets me run heavy work safely:
offline AI models that keep the graphics chip at 100%, and MCP servers (the small services AI assistants connect to)
that I turn on and off with **[Switches](features/10%20Switches.md)** — and that can switch themselves off when I unplug. When
something power-hungry is running, Sparewatt [shows me which app or service it is](features/06%20Power.md#power-per-app-share-of-battery-drain), and I can
[hunt it down and stop it](features/04%20Who%20is%20using%20it.md#look-closer-then-quit-or-force-quit).

## Features

**[Every feature in detail](features/README.md)** — purpose, what it does, use cases, benefits, settings and limits, with a
catalogue and everyday scenarios ("a full day on battery", "the battery drops overnight", "running local AI models").

| Area | Page |
|---|---|
| Menu bar: readings, grouped item with outline, hover panels, colours, warnings | [Menu bar](features/01%20Menu%20bar.md) |
| Processor, graphics, memory | [Processor, graphics and memory](features/02%20Processor%2C%20graphics%20and%20memory.md) |
| Temperature and fans, network, storage space | [Temperature, network and storage space](features/03%20Temperature%2C%20network%20and%20storage%20space.md) |
| Named processes, quitting, background normals, Watchlist | [Who is using it](features/04%20Who%20is%20using%20it.md) |
| Battery state, charge plan, wear, overnight drain | [Battery](features/05%20Battery.md) |
| Power flow, USB power out, power per app, idle apps | [Power](features/06%20Power.md) |
| Energy modes, On Battery settings, Extreme Saver, profiles | [Power controls](features/07%20Power%20controls.md) |
| Every notification | [Alerts and notifications](features/08%20Alerts%20and%20notifications.md) |
| Latest File, Shelf, caches, Downloads tidy-up, clipboard | [Files and storage](features/09%20Files%20and%20storage.md) |
| Local services on/off | [Switches](features/10%20Switches.md) |
| Dashboard, Mac health, history, Startup Items, This App | [Dashboard, history and this app](features/11%20Dashboard%2C%20history%20and%20this%20app.md) |
| AI Assistant: an MCP server for Claude Code, Codex and other assistants | [AI Assistant](features/12%20AI%20Assistant.md) |

## Guide

| Page | What it covers |
|---|---|
| [Getting started](guide/01%20Getting%20started.md) | install, first launch, the unsigned-app warning, updating from 1.4 |
| [Menu bar and panels](guide/02%20Menu%20bar%20and%20panels.md) | the menu bar item, hover panels, what each part shows |
| [Battery and power](guide/03%20Battery%20and%20power.md) | power per app, idle-app suggestions, charge plan, wear, charger and sleep checks |
| [Controls](guide/04%20Controls.md) | energy modes, On Battery settings, Extreme Saver, profiles, Watchlist, Switches, alerts |
| [Files and storage](guide/05%20Files%20and%20storage.md) | Latest File, the Shelf, Downloads tidy-up, caches, folder sizes, clipboard |
| [Dashboard and history](guide/06%20Dashboard%20and%20history.md) | the dashboard window, history charts, battery stretches, CSV export, Mac health |
| [How the estimates work](guide/07%20How%20the%20estimates%20work.md) | energy impact, watts per app, battery time gained, the idle-app rule |
| [Privacy and permissions](guide/08%20Privacy%20and%20permissions.md) | what stays on your Mac, which prompts appear and why |
| [Troubleshooting](guide/09%20Troubleshooting.md) | hidden menu bar item, missing readings, password and permission prompts |

## Reference

- [Keyboard shortcuts](reference/Keyboard%20shortcuts.md)
- [Where Sparewatt keeps its data](reference/Data%20files.md)
- [Changelog](CHANGELOG.md)
- [Research](research/README.md) — notes on similar Mac apps and what their users complain about, written while designing Sparewatt

## Screenshots

| Processor | Memory | Temperature & fans |
|---|---|---|
| <img src="images/screenshots/panel-cpu.png" width="260"> | <img src="images/screenshots/panel-memory.png" width="260"> | <img src="images/screenshots/panel-temperature.png" width="260"> |

| Battery | Power | Graphics | Network |
|---|---|---|---|
| <img src="images/screenshots/panel-battery.png" width="200"> | <img src="images/screenshots/panel-power.png" width="200"> | <img src="images/screenshots/panel-graphics.png" width="200"> | <img src="images/screenshots/panel-network.png" width="200"> |

| History | On Battery settings |
|---|---|
| <img src="images/screenshots/dashboard-history.png" width="440"> | <img src="images/screenshots/dashboard-on-battery.png" width="440"> |

Screenshots were taken before the rename; apart from the name, the app looks the same.

## License

Sparewatt is **free to download and use**. It is not open source: its code is private, and all rights are reserved.
You may share the official download unchanged and free of charge; you may not sell it, distribute changed copies, or
reverse engineer it. It comes as is, without warranty. These pages are © 2026 Shiraz Ahmad.
