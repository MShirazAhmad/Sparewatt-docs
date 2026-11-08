# macOS battery, power and thermal apps: features, pricing, status and user pain points (as of 2026-11)

Scope: AlDente (AppHouseKitchen), Battery Toolkit (mhaeuser), coconutBattery, Sensei (Cindori), TG Pro (Tunabelly), Hot (macmade), FanControl / Macs Fan Control (crystalidea) plus open-source fan tools, and Apple's built-in Optimized Battery Charging and Charge Limit (macOS Tahoe 26.4). Apple silicon only. Research ran on 2026-11-03 with about 15 web searches and fetches. Many findings come from vendor pages and a few forum threads, not from broad review samples. Reddit could not be reached directly, so Reddit-specific evidence is thin.

## Per-app fact sheets (features, pricing, maintenance)

### Takeaway
Charge limiting is now split. Apple ships a basic 80–100% limit. Third-party limiters such as AlDente, batt and the `battery` CLI still offer more, but on macOS 27 they broke because Apple locked down the SMC charge-control keys. Thermal tools (TG Pro, Macs Fan Control) are actively updated for M4 and M5, but Apple silicon sensor coverage is messy and needs vendor work for each chip generation.

### Cited Findings
**Apple built-in (Optimized Battery Charging + Charge Limit, macOS 26.4)**
- Charge Limit is a slider from 80 to 100% in 5% steps (80/85/90/95/100), found at System Settings > Battery > (i) next to Charging. It first appeared in the 26.4 beta in Feb 2026. — [MacRumors](https://www.macrumors.com/2026/02/16/mac-charge-limit-macos-tahoe-26-4/)
- It sits alongside Optimized Battery Charging, which "still regularly" lets the battery reach 100%. Charge Limit is a hard cap. — [MacRumors](https://www.macrumors.com/2026/02/16/mac-charge-limit-macos-tahoe-26-4/)
- Charge Limit can also be set from Shortcuts. — [WebSearch summary of 26.4 coverage, incl. AppleInsider](https://appleinsider.com/articles/26/02/17/macos-tahoe-264-adds-a-charge-limit-slider-to-preserve-your-macbook-battery)
- 26.4 also added a "slow charger" indicator. — [MacRumors forum thread](https://forums.macrumors.com/threads/macos-tahoe-26-4-adds-slow-charger-indicator-for-macbooks.2479897/)

**AlDente (AppHouseKitchen)**
- Pro pricing: €11.49/yr subscription, €23.99 lifetime, or via Setapp (€9.99/mo). One license covers up to 3 macOS user accounts. The pricing page's Free and Pro feature lists look identical (charge limit, discharge, sailing mode, scheduling, Shortcuts), so it does not show which features are Pro-only. — [AppHouseKitchen pricing](https://apphousekitchen.com/pricing/)
- An earlier deal listing showed Pro at $18 (down from $25). — [Slickdeals](https://slickdeals.net/f/17097655-aldente-pro-all-in-one-charge-limiter-app-for-macbooks-30-off)
- After Apple's limit shipped, the vendor listed features Apple lacks: a power/battery analytics dashboard, a customizable menu bar, health-over-time charts, Power Mode, heat protection, advanced automation, and MagSafe LED control. The vendor calls Apple's version "minimal configuration, customization, and basic features only". — [AppHouseKitchen "We Got Sherlocked — Or Did We?"](https://apphousekitchen.com/we-got-sherlocked-or-did-we/)
- Maintenance: actively released (1.37.x and 1.39.x lines). Latest versions affected on macOS 27 are listed below. — [newreleases.io 1.37.2](https://newreleases.io/project/github/AppHouseKitchen/AlDente-Battery_Care_and_Monitoring/release/1.37.2); [macos-tahoe.com](https://macos-tahoe.com/blog/macos-27-battery-charge-limit-apps-broken-aldente-batt-charging-to-100-fix-2026/)

**Battery Toolkit (mhaeuser)**
- Free, BSD-3-Clause, Apple silicon only.
- Features: an upper limit (minimum 50%) and a lower resume limit (minimum 20%), turning the power adapter off without unplugging, and manual menu bar commands (full charge, stop charging).
- Limitations: it cannot control charging while the Mac is shut down (a shut-down Mac charges to 100%). The lower limit is not honored on cold boot. Sleep is disabled while charging. Turning off the adapter exits clamshell mode. Optimized Charging must be turned off.
- The app is not notarized, so on macOS 15+ the user must click "Open Anyway". It uses a privileged XPC daemon.
- **The project was archived on 2026-03-21.** — [GitHub mhaeuser/Battery-Toolkit](https://github.com/mhaeuser/Battery-Toolkit)
- A community fork targets macOS 27, but only on the forker's own tested Mac. — [macos-tahoe.com](https://macos-tahoe.com/blog/macos-27-battery-charge-limit-apps-broken-aldente-batt-charging-to-100-fix-2026/)

**coconutBattery**
- Shows battery health and capacity for the Mac and connected iOS devices. It runs universal on Apple silicon (v4.3.1 noted). — [FileHorse](https://mac.filehorse.com/download-coconutbattery)
- Pricing conflicts across sources: a €12.95 one-time v4 upgrade ([ifun.de](https://www.ifun.de/akku-informant-coconutbattery-in-version-4-0-verfuegbar-244221/)) versus $9.95 with a 14-day trial ([Macworld](https://www.macworld.com/article/542901/coconutbattery-review-mac-gems.html)). The current official price was not confirmed.

**Sensei (Cindori)**
- An all-in-one maintenance and monitoring app: thermal dashboard (sensors, fans), live CPU/GPU, drive health, and a battery page with health, time remaining and raw battery temperature. — [The Sweet Setup](https://thesweetsetup.com/sensei-an-all-in-one-mac-maintenance-dashboard/)
- Pricing: $59 one-time or $29/yr, 3 seats. Some Reddit users objected to the subscription. — [r/macapps mirror](https://reddit.fsky.io/r/macapps/comments/1jcub7q/sensei_do_you_need_it); [Macworld review (2020, older)](https://www.macworld.com/article/3530148/sensei-review-gorgeous-mac-performance-utility-hamstrung-by-thunderbolt.html)
- Licensing bug: the app can show "Expired" after a subscription renewal, and the fix is to deactivate and re-enter the license. — [Cindori support](https://cindori.com/support/sensei/general/subscription-license-expired)

**TG Pro (Tunabelly)**
- Temperature monitoring plus fan control, with M1–M4 support and later an M5 release. — [Tunabelly](https://tunabellysoftware.com/tgpro/); [M5 tag](https://www.tunabellysoftware.com/blog/files/tag-m5.html)
- M4 fan control history: on macOS 15, fans could only be controlled when the hardware itself wanted cooling (v2.93). v2.95 allowed running fans the hardware had turned off. v2.97 added full fan control on all M4 Macs. — [Tunabelly blog](https://www.tunabellysoftware.com/blog/files/tgpro-m4-fan-control.html); [applech2](https://applech2.com/archives/20250310-tg-pro-support-apple-m4-fan-control.html)
- Sensor quirks, per the vendor: GPU core sensors stop reporting at low load; there was an M4 Max GPU sensor bug (fixed in 2.96); and duplicate SSD sensors appeared on the 2025 Mac Studio M4 Max. — [Tunabelly M4 tag](https://www.tunabellysoftware.com/blog/files/tag-m4.html)
- The vendor's "most accurate" claim for M3 is self-reported. — [Tunabelly M3 post](https://www.tunabellysoftware.com/blog/files/tg-pro-apple-silicon-m3-series-support.html)

**Hot (macmade / XS-Labs)**
- Free and MIT-licensed, about 2.5k GitHub stars. On Intel it shows CPU temperature and speed limit.
- **On Apple silicon it can only show the system "thermal pressure" level** (per-core speed and temperature are not exposed), and the text turns orange when pressure is not nominal. — [GitHub macmade/Hot](https://github.com/macmade/Hot)

**Macs Fan Control (crystalidea) and open-source "FanControl"-style tools**
- v1.5.17 added M3/M4 temperature sensors. v1.5.18 added full fan control on M3/M4 MacBook Pro, the Mac Studio M4 Max and MacBook Air M4 support. v1.5.21 (Apr 2026) added the M5 Pro/Max MacBook Pro. — [crystalidea release notes](https://crystalidea.com/macs-fan-control/release-notes)
- Open-source alternatives all need a root helper:
  - xiachufang/MacFanControl requires macOS 26 and uses an SMAppService root LaunchDaemon. — [GitHub](https://github.com/xiachufang/MacFanControl)
  - SoloFan needs admin rights and warns that "some temperature keys may not work" on Apple silicon. — [GitHub](https://github.com/soloteamdev/solofan)
  - jbforge/mac-fan-control binaries are unsigned. — [GitHub](https://github.com/jbforge/mac-fan-control/releases)

### Inferences
- Every tool that writes to the SMC (charge control, fan control) needs a privileged helper. That makes admin prompts, notarization and security friction universal to this category.
- Read-only monitors such as coconutBattery and Hot avoid the helper but lose the ability to act.

### Gaps
- Current coconutBattery price and Plus tier: sources conflict.
- AlDente Free versus Pro feature split: the pricing page is ambiguous. My recollection that Free equals the charge limit only is not verified here.
- A dedicated product named "FanControl" for macOS was not identified. Macs Fan Control is assumed to be the intended app.

## Common complaints and struggling points

### Takeaway
The biggest pain points are three:
- Limits silently not holding, especially after macOS updates (macOS 27 broke nearly every third-party limiter in 2026), or when the Mac is asleep or shut down.
- Confusing charge-state signals: the amber LED, "on hold" versus charging, and whether the battery is bypassed.
- Feature regressions that the vendor confirms only after users report them.

Temperature apps struggle with Apple silicon sensor exposure from one chip generation to the next.

### Cited Findings
- **macOS 27 breakage (2026, current):**
  - AlDente issues #1771 (M3 Air, the 78% limit reached 94%, discharge misbehaved), #1775 (M1 Pro, "EC charge control does not work at all"), #1817 (Pro 1.39.1 on RC, contradictory status messages, the 56% limit was not enforced), #1840 and #1841 (1.39.4 on 27.0 and 27.0.1, charging past the limit). No developer reply was visible on the newest issues.
  - batt #152: charge keys appear gated "likely behind an entitlement check" and writes fail as "not privileged" even as root. PR 154 added an adapter-cutoff mode that only works while the Mac is awake.
  - The `battery` CLI maintainer rejected adapter cutoff because it causes "constant micro-cycling".
  - Legacy keys (CHTE, CH0B, CH0C, CH0I) return nothing; newer keys (bfD0, bfE0, bfF0) are locked.
  - Status: a third-party blog compiling developer reports, not Apple-confirmed. — [macos-tahoe.com](https://macos-tahoe.com/blog/macos-27-battery-charge-limit-apps-broken-aldente-batt-charging-to-100-fix-2026/)
- **Status text lies:** for AlDente on macOS 27, the blog reports "the app's status text can still look normal" while the Mac is overcharging. — [macos-tahoe.com](https://macos-tahoe.com/blog/macos-27-battery-charge-limit-apps-broken-aldente-batt-charging-to-100-fix-2026/)
- **Older update breakage (macOS 12.6 era, older):** AlDente #768 "stops working after macOS update", charging to 100%; the maintainer blamed macOS. — [GitHub #768](https://github.com/AppHouseKitchen/AlDente-Charge-Limiter/issues/768)
- **Charger not detected after sleep (older):** AlDente #733 reports a USB-C charger not detected after wake until a reboot, even with a 100% limit. — [GitHub #733](https://github.com/AppHouseKitchen/AlDente-Charge-Limiter/issues/733)
- **Paid feature broken (2023, older):** Sailing Mode in Pro 1.22 did not survive a restart, and the Mac charged from 40 to 84%. The user wrote it was "just like have a free version"; the maintainer confirmed and fixed it. — [GitHub discussion #1007](https://www.github.com/AppHouseKitchen/AlDente-Charge-Limiter/discussions/1007)
- **Limit not held when asleep or off:** a Trustpilot 1-star review says AlDente sometimes charges to 100% while the Mac is asleep or shut down, and that the menu bar icon can't be removed from the Dock. — [Trustpilot](https://se.trustpilot.com/review/apphousekitchen.com)
- **Battery Toolkit documents the same limits by design:** a shut-down Mac charges to 100%, and the lower limit is ignored on cold boot. — [GitHub](https://github.com/mhaeuser/Battery-Toolkit)
- **Conflicts with Optimized Charging:** AlDente advises turning off Apple's Optimized Charging because it slows charging past the limit. — [AlDente commit mirror](https://cdn05042023.gitlink.org.cn/dnrops/AlDente/commit/6c9206fa6e44fbf92b5a00d363134bf877bba251) Battery Toolkit says the same. — [GitHub](https://github.com/mhaeuser/Battery-Toolkit)
- **Apple's limit confuses users (2026):**
  - An M4 Air owner at 80% asked "do we still bypass the battery when plugged in, or is it now just constantly cycling around 79-80%".
  - The MagSafe LED "glows orange all the time like it is charging".
  - The same user felt the Mac "seems to run hotter"; another user disputed this.
  - A reply quoted Apple that the LED stays amber "whether charging or on hold", and that at the limit the Mac "will run off of the power supply".
  - Behavior reportedly changed in 26.5 (details not given). — [MacRumors forum](https://forums.macrumors.com/threads/80-charging-running-hotter-still-bypassing-battery.2480121/)
- **Optimized Charging is distrusted:** a MacRumors commenter says Optimized Battery Charging always charges their Mac to 100% anyway. — [MacRumors](https://www.macrumors.com/2026/02/16/mac-charge-limit-macos-tahoe-26-4/)
- **Health and percentage numbers disagree:** an Apple Communities thread asks why coconutBattery's state of charge differs from macOS's. A MacRumors user notes that coconutBattery and AlDente values "can shift day to day". — [Apple Communities](https://discussions.apple.com/thread/255654391); [MacRumors forum](https://spy.macrumors.com/threads/why-would-you-keep-the-macbook-always-plugged-in-whenever-possible-for-long-periods.2466498/page-3)
- **Sensors on Apple silicon:**
  - Hot cannot show CPU temperature at all on Apple silicon, only thermal pressure. — [GitHub Hot](https://github.com/macmade/Hot)
  - GPU sensors go silent at low load. — [Tunabelly](https://www.tunabellysoftware.com/blog/files/tag-m4.html)
  - One tool reports 291 raw sensors on an M4 Pro versus about 20 in curated lists. — [search summary of TG Pro/M4 sources](https://www.tunabellysoftware.com/blog/files/tag-m4.html) (the attribution of this figure is uncertain)
  - Open-source fan tools warn that temperature keys may not work. — [SoloFan](https://github.com/soloteamdev/solofan)
- **Fan control needed workarounds per OS and chip:** on macOS 15 and M4, fans could not be forced on until TG Pro v2.95/2.97. — [Tunabelly](https://www.tunabellysoftware.com/blog/files/tgpro-m4-fan-control.html)
- **Install friction:** Battery Toolkit is not notarized ("Open Anyway"), needs a privileged daemon, and requires a special uninstall step. — [GitHub](https://github.com/mhaeuser/Battery-Toolkit) jbforge fan control is unsigned. — [GitHub](https://github.com/jbforge/mac-fan-control/releases)
- **Pricing backlash:** Reddit objections to Sensei's subscription. — [r/macapps mirror](https://reddit.fsky.io/r/macapps/comments/1jcub7q/sensei_do_you_need_it) AlDente now sells both a subscription and a lifetime license. — [pricing](https://apphousekitchen.com/pricing/)

### Inferences
- The defining failure of 2026 is apps whose UI reports "limit active" while the hardware is not obeying. An app that cross-checks the measured current (is the battery actually charging?) against the intended state would address it directly.
- Most charge confusion comes from three hidden variables: is the adapter powering the system, is the battery charging, and is the battery being held. Neither Apple nor the apps surface all three clearly.

### Gaps
- No evidence was found on battery drain caused by the apps themselves (AlDente, TG Pro). Direct Reddit and App Store review access was not obtained.
- No independent accuracy comparison of TG Pro, Macs Fan Control and Sensei temperatures on M-series chips was found.

## Has Apple's Charge Limit (26.4) reduced the need for third-party limiters, and what gaps remain?

### Takeaway
For the basic "cap at 80%" use case: yes. On macOS 27 it is the only limiter reported to work reliably, now that SMC keys are locked. Gaps remain:
- No limit below 80%.
- No sailing range or discharge, and no heat protection.
- No power-flow or adapter-watt view, and no health history.
- An opaque charge state.
- Unclear behavior when the Mac is shut down.

### Cited Findings
- The minimum is 80%. A user who sets 50% in AlDente wants lower. — [MacRumors](https://www.macrumors.com/2026/02/16/mac-charge-limit-macos-tahoe-26-4/)
- After macOS 27 broke third-party apps, Apple's built-in limit is presented as the "safe alternative". Some CLI projects now propose wrapping macOS's own limit (battery PRs 479 and 480). — [macos-tahoe.com](https://macos-tahoe.com/blog/macos-27-battery-charge-limit-apps-broken-aldente-batt-charging-to-100-fix-2026/)
- The vendor's list of missing features is in the AlDente fact sheet above. — [AppHouseKitchen](https://apphousekitchen.com/we-got-sherlocked-or-did-we/)
- One user suspects Apple's limit depends on macOS running, so it may not hold while the Mac is shut down; the user was unsure. — [MacRumors forum](https://forums.macrumors.com/threads/macos-tahoe-26-4-adds-slow-charger-indicator-for-macbooks.2479897/page-2)
- Bypass versus cycling at the limit is unclear to users, and the LED stays amber. — [MacRumors forum](https://forums.macrumors.com/threads/80-charging-running-hotter-still-bypassing-battery.2480121/)

### Inferences
- The third-party value is moving from enforcing the limit (now Apple's job, and increasingly locked) to explaining and visualizing what is happening: power flow, holds, heat, and health trends.
- A new app that reads state rather than writes to the SMC avoids both the helper and the macOS 27 breakage.

### Gaps
- What changed in 26.5 regarding bypass behavior is unknown.
- Whether third parties can read or set Apple's limit through public API, beyond Shortcuts, is unconfirmed.

## Unmet user requests

### Takeaway
Users repeatedly ask what the battery is actually doing right now: charging, held, bypassed or cycling, and why. No app or Apple surfaces this with confidence, especially when apps and macOS disagree.

### Cited Findings
- The question "bypass or constantly cycling around 79-80%" goes unanswered by the UI, and the LED is ambiguous. — [MacRumors forum](https://forums.macrumors.com/threads/80-charging-running-hotter-still-bypassing-battery.2480121/)
- Users want honest status. AlDente's status can "look normal" while overcharging, and #1817 reports contradictory status messages. — [macos-tahoe.com](https://macos-tahoe.com/blog/macos-27-battery-charge-limit-apps-broken-aldente-batt-charging-to-100-fix-2026/)
- Users want consistent health and percentage figures, because apps and macOS disagree. — [Apple Communities](https://discussions.apple.com/thread/255654391)
- Users want limits below 80% without root helpers. — [MacRumors](https://www.macrumors.com/2026/02/16/mac-charge-limit-macos-tahoe-26-4/)
- Users want real Apple silicon temperatures in simple monitors (Hot only shows pressure). — [GitHub Hot](https://github.com/macmade/Hot)

### Inferences
- Opportunity: a read-only menu bar view of power flow (adapter W → system W, battery ±W), the charge state in plain words ("held at 80% by macOS Charge Limit; running on adapter"), a drain-rate graph per app, and a mismatch alarm when the intended limit and the measured current disagree.

### Gaps
- No direct sourced demand found for drain-rate visualisation or per-app battery attribution. These are inferred, not quoted. Reddit and App Store review mining is needed to confirm.
