# macOS menu bar system monitors: fact sheets and user pain points (as of 2026-11-03)

Scope: iStat Menus (Bjango), Stats (exelban), eul, MenuMeters, iStatistica / iStatistica Pro, plus other options found (Sensei, TeenyStat, mac-stats). About 15 tool calls. Reddit could not be read directly, so Reddit evidence is thin. Some MacRumors forum pages returned HTTP 403.

## Q1. Fact sheets: features, pricing, maintenance

### Takeaway
iStat Menus (paid, one-time licence, version 7.5) is the most complete option: rules/notifications, history, fan control and a combined menu. Stats (free, MIT, about 43k stars) is the default free choice and is actively maintained by one developer. eul is effectively stale, MenuMeters is minimal but still releasing, and iStatistica Pro is a cheaper App Store option that needs a separate sensors plugin.

### Cited Findings
**iStat Menus 7 (Bjango)**
- Current version is 7.5 and requires macOS 13.5+. Menu items cover CPU (per core, top apps), GPU, memory, disks, network, sensors, battery, weather, clocks/world clocks and a new Astronomy item. There are "Rules" alerts for CPU, GPU, memory, disk, network, sensors, battery, power, weather, public IP changes and internet outages. History graphs, fan control with temperature- or battery-based ramps, and a "Combined" mode that merges several items into one menu bar item are included. There is a 14-day trial — [Bjango](https://bjango.com/mac/istatmenus/)
- Pricing at the v7 launch (July/Aug 2024) was $11.99 new and $9.99 to upgrade — [Michael Tsai](https://mjtsai.com/blog/2024/08/01/istat-menus-7). Bjango's current page shows Single and Family (up to 5 people) licences without a visible price in the fetched page — [Bjango](https://bjango.com/mac/istatmenus/)
- It is also on Setapp at $9.99/mo, bundled with more than 250 other apps — [Bjango](https://bjango.com/mac/istatmenus/)
- Weather is a separate subscription after the 6 months included with every licence. The App Store shows $4.99/yr or $0.99/mo — [App Store](https://apps.apple.com/app/id6499559693); [Bjango](https://bjango.com/mac/istatmenus/)
- Bjango's reason for the paid upgrade: years of work, plus the need to buy at least one of each new Mac model per generation to support its sensors. iStat Menus 6 buyers from 1 Jan 2024 got v7 free — [Bjango help](https://bjango.com/help/istatmenus7/update/)
- In the MacRumors forum, the developers said they do not want or need to move to a subscription — [MacRumors thread](https://forums.macrumors.com/threads/istat-menus-7-0-brings-comprehensive-redesign-and-new-features.2432615/) (via search summary; the page itself returned 403)

**Stats (exelban/stats)**
- Free, MIT licence, about 43.1k stars, 1.6k forks. Supports macOS 12+ and does not support beta macOS. Modules: CPU, GPU, memory, disk, network, battery, fan control ("not maintained", legacy), sensors (temperature, voltage, power), Bluetooth devices and a multi-timezone clock. Also offers desktop/Dock widgets — [GitHub README](https://github.com/exelban/stats)
- One developer maintains it. Pull requests are generally not accepted without a prior issue. There is a Sponsor button — [GitHub README](https://github.com/exelban/stats)
- It is actively maintained. Issues were opened and labelled in Oct–Nov 2026 (e.g. #3723 "GPU Module: Broken in the latest release", 2 Nov 2026), and only 16 issues are open — [GitHub issues](https://github.com/exelban/stats/issues?q=is%3Aissue+is%3Aopen+sort%3Acomments-desc)

**eul (gao-sun/eul)**
- MIT licence, about 10k stars, 68 open issues, no GitHub releases listed. The README says the App Store version "is out-dated" and "Some features are disabled due to the removal of all SMC calls" (which means no temperature or fan data). Widgets cover battery, CPU, memory and network, plus Bluetooth battery levels — [GitHub](https://github.com/gao-sun/eul)
- AlternativeTo marks it as discontinued — [AlternativeTo](https://alternativeto.net/software/eul/about/)

**MenuMeters (yujitach fork)**
- Free and open source. Shows CPU, memory, disk and network. Latest release is 2.1.7, which fixes a PPP-related crash (the page did not give the year). Apple silicon history: preliminary support in 2.1.1 ("If the app crashes, please open it in Rosetta"), CPU frequency in 2.1.2.x, CPU temperature in 2.1.3, a chooser for which temperature sensor to use in 2.1.4, and a fix for M1 Pro/Max crashes in 2.1.5 — [GitHub releases](https://github.com/yujitach/MenuMeters/releases)

**iStatistica / iStatistica Pro (ImageTasks)**
- iStatistica Pro is $9.99 on the US App Store. Temperatures and fans need a separate "iStatistica Sensors Plugin". It supports Apple silicon and includes an "Apple Silicon Profiler" — [App Store](https://apps.apple.com/app/id1447778660); [imagetasks](https://imagetasks.com/istatistica)
- The developer also sells iStatistica Core, which runs on Apple silicon only and needs macOS 13+ — [imagetasks](https://www.imagetasks.com/istatistica/core)

**Others mentioned in 2026 reviews**
- Sensei (diagnostics plus monitoring) and TeenyStat (a minimal monitor) are named as alternatives. One 2026 review rates Stats as the best free option and iStat Menus as the pick when rules, weather, fan control or deep menu bar customisation matter — [Cindori review](https://cindori.com/reviews/best-istat-menus-alternatives-mac); [TeenyStat comparison](https://teenystat-website.pages.dev/articles/teenystat-vs-stats-vs-istat-menus-mac-system-monitor/) (both are vendor-written, so they are biased)

### Inferences
- The market splits into one polished paid app (iStat Menus), one dominant free app (Stats), and a long tail of stale or minimal apps.
- Fan control is a weak spot even in Stats, which keeps it as a legacy, unsupported module.

### Gaps
- I could not confirm iStat Menus' current 2026 price; the Bjango page rendered without prices.
- I could not get a year for MenuMeters 2.1.7, or the last commit date for eul.
- I did not verify iStatistica Pro's update cadence.

## Q2. What users complain about most

### Takeaway
The top complaint for Stats by far, measured by GitHub reactions, is missing or broken sensors on each new Apple silicon generation. The second is OS-update breakage, especially menu bar items not appearing under macOS 26 Tahoe's new Menu Bar permission. Overhead, notch crowding and iStat Menus pricing come up, but less often and less loudly.

### Cited Findings
**Sensors on Apple silicon (recurs with every chip generation)**
- The most-reacted Stats issues: #210 "No sensors - Apple Silicon" (98 reactions, 2021), #2249 "No sensors for M4" (61, Feb 2025) and #1286 "sensors on m2, currently report broken values" (32, 2023) — [GitHub issues by reactions](https://github.com/exelban/stats/issues?q=is%3Aissue+sort%3Areactions-%2B1-desc)
- The maintainer's explanation: Apple silicon sensors are thermal zones, not individual cores, and "Apple changes sensor keys with each new SoC", so matching them takes time — [Stats README](https://github.com/exelban/stats)
- Bjango cites the same cost: it has to buy each new Mac to support its sensors — [Bjango help](https://bjango.com/help/istatmenus7/update/)
- Current: #3621 "CPU Power Showing 0.00W" (Sep 2026, 14 comments, the most-discussed open issue) — [GitHub open issues](https://github.com/exelban/stats/issues?q=is%3Aissue+is%3Aopen+sort%3Acomments-desc)
- eul dropped all SMC calls, so it has no temperature or fan data — [eul README](https://github.com/gao-sun/eul)

**Breakage after macOS updates**
- Stats #3120 "Menu bar items not showing on macOS 26.4 (Tahoe)" (Apr 2026, M5 MacBook). The cause turned out to be Tahoe's System Settings → Menu Bar permission. Duplicates include #3138, #2704, #2823 and #2623. The thread became heated and was locked on 26 May 2026 — [GitHub #3120](https://github.com/exelban/stats/issues/3120)
- #2768 "Widget doesn't show up on login in menubar" (39 reactions, Nov 2025). #2131, menu bar icons not greyed out on the inactive screen (Sequoia, 21 reactions). #2115, desktop widgets show "No data" (Sequoia, 18). #2146, performance and internet problems after the Sequoia update (15) — [GitHub](https://github.com/exelban/stats/issues?q=is%3Aissue+sort%3Areactions-%2B1-desc)
- #3716: the fan helper's SMAppService returns `.notFound` and register() fails with EPERM on macOS 27.0 (Oct 2026). #2977: fan control spins the fan to 100% after sleep (14 reactions, Mar 2026) — [GitHub](https://github.com/exelban/stats/issues?q=is%3Aissue+is%3Aopen+sort%3Acomments-desc)
- The Stats README now has a FAQ entry telling users to enable Stats in the macOS 26 Menu Bar setting — [README](https://github.com/exelban/stats)

**Monitor's own CPU, memory and energy overhead**
- Stats' own README says the Sensors and Bluetooth modules are the most inefficient, and turning them off can cut CPU and power use "by up to 50%" — [README](https://github.com/exelban/stats)
- #3713 (Oct 2026): settings pages and disabled Sensors views take about 160 MB at launch — [GitHub](https://github.com/exelban/stats/issues?q=is%3Aissue+is%3Aopen+sort%3Acomments-desc)
- An older report, #29 (2020, Catalina), complained of high CPU and battery use — [GitHub #29](https://github.com/exelban/stats/issues/29)
- A MacRumors user reported a Stats memory leak that they patched themselves. iStat Menus users there said it is not resource-heavy ("even Activity Monitor is using more resources"), and suggested lowering the refresh rate. Nobody gave measured numbers — [MacRumors](https://forums.macrumors.com/threads/istats-menu-vs-stats-which-is-better-battery-consumption.2354863/)

**Menu bar crowding and the notch**
- macOS hides overflow menu bar items behind the notch with no indicator. Tahoe added System Settings → Menu Bar ("Allow in the menu bar"), but still has no overflow indicator. Users rely on Bartender, Ice, Hidden Bar or Lounge — [Badgeify](https://badgeify.app/how-to-fix-mac-menu-bar-icons-disappearing-behind-notch/); [OWC blog](https://eshop.macsales.com/blog/97824-macos-tahoe-makes-it-extremely-easy-to-clean-up-a-messy-menu-bar/) (blogs, not Apple documentation)
- A comparison article notes that graphs and labels from monitors "fighting with the clock, Wi-Fi, Control Center" on notched MacBooks — [TeenyStat comparison](https://teenystat-website.pages.dev/articles/teenystat-vs-stats-vs-istat-menus-mac-system-monitor/) (vendor source)
- Stats #3708: the stack widget's width jitters when values change and shifts other menu bar items — [GitHub](https://github.com/exelban/stats/issues?q=is%3Aissue+is%3Aopen+sort%3Acomments-desc)
- iStat Menus' Combined mode is its answer to crowding — [Bjango](https://bjango.com/mac/istatmenus/)

**Pricing (iStat Menus)**
- The backlash is mild and centres on the weather subscription, not the core licence. One user dropped the app because "many of the features that were once free became paid" — [MacRumors](https://forums.macrumors.com/threads/istats-menu-vs-stats-which-is-better-battery-consumption.2354863/); MacRumors v7 thread summarised via search: [link](https://forums.macrumors.com/threads/istat-menus-7-0-brings-comprehensive-redesign-and-new-features.2432615/)
- Users switching to Stats say it "is totally fine for my needs" — [MacRumors](https://forums.macrumors.com/threads/menu-bar-monitoring-app-istat-menus-vs-stats.2342009/)

**Add-on and extra-install friction**
- iStatistica needs a separate sensors plugin — [App Store / softpedia via search](https://apps.apple.com/app/id1447778660)
- Stats' fan control needs a privileged helper, which is broken on macOS 27 (#3716, above).

### Inferences
- The biggest recurring pain is fragile data acquisition: private SMC/IOReport keys change with each chip, and helpers and permissions change with each OS. Users cannot tell whether a "0.00W" or a missing item is a real reading or a bug.
- Tahoe's Menu Bar permission is a new source of "app is running but invisible" confusion. It looks like breakage to users even when the app works.

### Gaps
- I could not reach Reddit (r/macapps, r/mac) directly or read App Store reviews, so there is no quantified Reddit sentiment.
- I found no measured, comparable CPU/energy numbers for the monitors themselves.
- The MacRumors iStat Menus 7 thread returned 403, so I could not get exact quotes about the redesign.

## Q3. Systemic vs app-specific complaints, and unmet requests

### Takeaway
Sensors breaking with each new chip, OS-update or permission breakage, notch/menu bar space and overhead affect every app. Pricing (iStat), the stale App Store build (eul) and the required plugin (iStatistica) are specific to one app. Users repeatedly ask for usage history, smarter alerts, aggregated sensors and per-interface network detail. These are open for years in Stats and only iStat Menus delivers them, and only partly.

### Cited Findings
- Systemic sensor fragility: Stats' README and Bjango's help page both blame per-SoC sensor changes — [Stats](https://github.com/exelban/stats); [Bjango](https://bjango.com/help/istatmenus7/update/). MenuMeters needed several releases to add Apple silicon temperature and a sensor chooser — [MenuMeters](https://github.com/yujitach/MenuMeters/releases). eul gave up on SMC — [eul](https://github.com/gao-sun/eul)
- Long-open requests in Stats:
  - #1194 usage history in the expanded window (open since Nov 2022)
  - #1558 average temperature across all sensors (Jul 2023, 12 comments)
  - #2436 sustained-threshold CPU warnings ("more than x seconds", Mar 2025)
  - #3401 battery usage history
  - #3450 everyday network usage totals
  - #3721 multiple network interfaces and IPs
  - #3645 configurable colour thresholds

  — [GitHub open issues](https://github.com/exelban/stats/issues?q=is%3Aissue+is%3Aopen+sort%3Acomments-desc)
- Even an iStat Menus fan wished for recording process samples from the menu instead of keeping Activity Monitor open — [Michael Tsai](https://mjtsai.com/blog/2024/08/01/istat-menus-7)
- A reviewer says Stats lacks iStat's configurable sensor dropdowns, notifications and history — [Cindori](https://cindori.com/reviews/best-istat-menus-alternatives-mac)

### Inferences
- Gaps no app fills well, which a newcomer could target:
  - Debounced, sustained-threshold alerts that act on a process, not just notify
  - Longer-term history and per-process attribution
  - Notch-aware compact display (one combined item that tells you when it is hidden)
  - Clear "sensor unsupported on this chip" states instead of 0 or blank
  - Low self-overhead, shown as a published number

### Gaps
- I have no direct user-voted ranking of feature requests outside the Stats tracker.
