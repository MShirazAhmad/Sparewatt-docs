# Menu bar space managers and drag shelves / recent-file grabbers (state as of 2026-11)

Note: this was a short research pass (about 12 tool calls). Several sources are forums, vendor pages or one third-party blog, and each is labelled as such. Older items are dated.

## Menu bar managers: features, pricing, maintenance, complaints (notch, crowding, Bartender ownership, OS breakage, performance, grouping)

### Takeaway
Menu bar managers break on almost every major macOS release because they rely on undocumented menu bar internals. In 2026 a reported macOS 27 change (the whole bar drawn as one window) broke Bartender, Ice, Hidden Bar, Barbee and others at once. Ice has had no macOS 27 release, and development reportedly moved to the Thaw fork. The 2024 Bartender sale, where the app needed always-on Screen Recording permission and new owners were not disclosed, still shapes trust. The notch hiding icons is the most common reason people install these apps.

### Cited Findings
**Bartender (2024 ownership controversy, older but still relevant)**
- June 2024: Bartender 5 changed owners without an announcement. MacUpdater flagged that the owner name had changed twice. — [MacRumors, 2024-06-04](https://www.macrumors.com/2024/06/04/bartender-mac-app-new-owner/)
- The concern was that Bartender needs Screen Recording permission at all times, while users did not know who owned it. Some forum posters said the requirement dated back to Catalina, before the sale, and nobody reported misuse. — [MacRumors forum thread](https://forums.macrumors.com/threads/psa-bartender-mac-app-under-new-ownership-but-lack-of-transparency-raises-concerns.2428159); [MPU Talk thread](https://talk.macpowerusers.com/t/bartender-change-of-ownership-potential-security-issue/37431)
- Users advised pinning an old build (5.0.49 to 5.0.51) and moving to Ice, Hidden Bar or iBar. One aggregator names the buyer as Applause, a US firm that buys indie apps (secondary source, not confirmed). — [gearandgrit](https://gearandgrit.com/bartender-app-ownership-change-and-alternatives); [r/macapps mirror, 2024-06-04](https://lr.eu.psf.lt/r/macapps/comments/1d7zjv8/bartender_5_not_safe_anymore_warning_from/l7678id)
- Current vendor site: Bartender 6 is the macOS 26 (Tahoe) version. Bartender 7 is built for macOS 27, says it "can function without Screen Recording" by showing app icons instead of item images, and lists a "Beat the notch" feature. A Bartender 7 one-time purchase includes Bartender 6. Prices did not load ("Loading price"). — [macbartender.com](https://www.macbartender.com/)

**Breakage on new macOS versions (2026)**
- A third-party blog (macos-tahoe.com, 2026-09-30, not Apple; it cites a BetterTouchTool forum post and macworld.info) says macOS 27 draws the whole menu bar as one window. Managers that found icons by their per-item windows broke at the first beta in June: Bartender, Ice, Hidden Bar, Barbee, Thaw and others. — [macos-tahoe.com](https://macos-tahoe.com/blog/macos-27-menu-bar-apps-broken-bartender-ice-icons-hidden-behind-notch-fix-2026/)
- The same source reports this status. Bartender 7 works, but groups are unavailable and iStat Menus and Setapp have issues. Thaw works on its 3.0 alpha (alpha 7, 25 Sep). Hidden Bar 1.11.1 works, but only outside the App Store, needs Accessibility permission, and cannot hide the clock, Wi-Fi, Sound or Control Center. Barbee and SaneBar are broken with no confirmed fix. — [macos-tahoe.com](https://macos-tahoe.com/blog/macos-27-menu-bar-apps-broken-bartender-ice-icons-hidden-behind-notch-fix-2026/)
- On Tahoe (2025), Bartender rewrote Bartender 6 "from the ground up" for Tahoe and Liquid Glass. — [search summary of macbartender.com](https://www.macbartender.com/)

**Ice (jordanbaird): free, open source**
- Releases page: latest stable is 0.11.12 ("Latest"). Tahoe pre-releases: 0.11.13-dev.1 (20 Jun 2025) had "limited support", and 0.11.13-dev.2 (16 Sep 2025) "fixes a majority of known issues introduced in macOS 26 Tahoe". There is a known brightness mismatch with the transparent bar. The project has 401 open issues and 50 open PRs. — [Ice releases](https://github.com/jordanbaird/Ice/releases)
- Ice has had no macOS 27 release. Bug reports #954 (8 Jun 2026) and #996 (17 Sep 2026) are reportedly open with no maintainer reply, and development reportedly moved to the Thaw fork. — [macos-tahoe.com](https://macos-tahoe.com/blog/macos-27-menu-bar-apps-broken-bartender-ice-icons-hidden-behind-notch-fix-2026/)
- Thaw (stonerl), an Ice fork, lists Tahoe fixes: items not showing, crashes, memory leaks. Its known issues include re-hiding failing on multi-monitor setups. — [Thaw 1.0.0-beta.1](https://newreleases.io/project/github/stonerl/Thaw/release/1.0.0-beta.1)
- MacRumors users were split during the 2025 Tahoe betas. Some said Ice worked well, others that it "still needed work". One post says the developer at first doubted he could adapt Ice to Tahoe. — [MacRumors macOS 26 apps thread p.14](https://forums.macrumors.com/threads/macos-26-beta-1-working-and-non-working-apps-thread.2458467/page-14)
- Ice can show hidden icons in a second row below the menu bar, which gets around the notch. — [MacRumors Ice vs HiddenBar](https://forums.macrumors.com/threads/ice-vs-hiddenbar.2471612)

**macOS built-in controls**
- Tahoe (macOS 26) added System Settings > Menu Bar for hiding or showing items in one place and letting items live in Control Center. Control Center itself cannot be hidden. The article says nothing about reordering or the notch. — [OWC blog](https://eshop.macsales.com/blog/97824-macos-tahoe-makes-it-extremely-easy-to-clean-up-a-messy-menu-bar/)
- One reviewer says the built-in option removed their need for a third-party manager. — [search summary; OWC / pipedot](https://pipedot.org/735XY)
- macOS 27 reportedly adds a double-arrow overflow button by the notch that reveals hidden icons. It cannot be customized and is not in Apple's documentation (secondary reports). "Scale to fit below built-in camera" helps app menus, not status icons. — [macos-tahoe.com](https://macos-tahoe.com/blog/macos-27-menu-bar-apps-broken-bartender-ice-icons-hidden-behind-notch-fix-2026/)

**Notch and missing icons**
- Users report on Apple Discussions and MacRumors that top-right icons (Wi-Fi etc.) go missing. — [Apple Discussions](https://discussions.apple.com/thread/256265881); [MacRumors missing items](https://forums.macrumors.com/threads/missing-menu-bar-items.2461953)
- New entrants sell notch handling as their main feature: Lounge has a "Notch-Aware Panel" on hover, and SaneBar claims notch-icon recovery (vendor claims). — [Product Hunt Lounge 2](https://www.producthunt.com/products/lounge-2); [SaneBar](https://sanebar-site.pages.dev/)

### Inferences
- Any app that moves or hides other apps' icons will break each year. An app that only shrinks its own footprint (one status item instead of N) does not depend on those internals, so it is the robust fix for crowding.
- Combining many monitor items (CPU, RAM, network, battery) into one item directly cuts the number of icons the notch can hide. Managers only hide icons; they do not reduce them.
- Permission trust is a live differentiator. Bartender 7 now advertises working without Screen Recording, which suggests the vendor saw demand. A monitor that needs no Screen Recording or Accessibility permission has a clear selling point.

### Gaps
- Barbee: I found no current pricing or maintenance source beyond the secondary "broken on macOS 27" claim.
- Current Bartender 6/7 prices did not load on the vendor page.
- I did not verify the macos-tahoe.com claims about macOS 27 architecture and Ice issues #954 and #996 against primary GitHub pages. Treat them as one secondary source.
- I found no measured performance data (CPU or battery) for Bartender or Ice. Performance complaints are not cited here.

## Drag shelves / recent-file grabbers: features, pricing, complaints, and how users grab "the latest file"

### Takeaway
Dropover, Yoink and Dropzone are mature drag shelves, and the complaints about them are mild: focus disruption, and Dropzone's shelf being less handy than a floating box. The gap is "give me the newest file right now". macOS's screenshot thumbnail is draggable but disappears after a few seconds, and other apps (Dropbox) have hijacked it. Users install single-purpose tools such as EasyShot, or Dropover's screenshot shelves, to fill that gap.

### Cited Findings
- Dropover: shake a file with the mouse to summon a shelf at the cursor, which users cite as its edge over Yoink. It also offers multiple shelves, cloud upload for share links, and a share extension. It is on the Mac App Store as free with in-app purchases. — [Product Hunt reviews](https://www.producthunt.com/products/dropover/reviews); [App Store](https://apps.apple.com/app/id1355679052)
- Product Hunt's summary of Dropover reviews names "focus disruption" as the main con. — [Product Hunt reviews](https://www.producthunt.com/posts/dropover-2/reviews)
- Dropover 4.15+ can open a new shelf with each screenshot automatically, and its docs advise turning off macOS's floating thumbnail so Dropover catches captures faster. — [Dropover KB: Screenshot Shelves](https://dropoverapp.com/kb/screenshots)
- A Setapp reviewer (March 2026) said Yoink's floating box is "a considerable improvement" over Dropzone's shelf and would switch back if Dropzone had a floating target. — [Setapp Dropzone reviews](https://setapp.com/de/apps/dropzone/customer-reviews)
- An App Store reviewer called Dropover much higher quality than Dropzone's Drop Bar, while noting that Dropzone does more than shelving. — [search summary of App Store / Setapp reviews](https://apps.apple.com/app/id1355679052)
- Yoink (Eternal Storms): an undated blog sale lists Mac at $7.99 (sale $5.99). It is also in a developer bundle. These prices may be stale. — [Eternal Storms blog](https://blog.eternalstorms.at/?p=1698); [bundle](https://apps.apple.com/app-bundle/id1439311326?l=en&mt=12)
- macOS's built-in screenshot thumbnail can be dragged to Finder or any app that accepts the file, but it vanishes after a few seconds. — [search summary; Dropbox forum thread](https://www.dropboxforum.com/discussions/101001016/please-revert-the-new-screenshot-feature-on-macos-or-at-least-give-us-the-option/827159)
- Dropbox's screenshot popup broke the drag workflow. One user wrote: "now, your stupid popup shows up and drag and drop doesn't work". Others said "Show floating thumbnail" kept switching itself off. — [Dropbox forum](https://www.dropboxforum.com/discussions/101001016/please-revert-the-new-screenshot-feature-on-macos-or-at-least-give-us-the-option/827159)
- EasyShot (Show HN) exists only to keep a screenshot thumbnail on screen until it is dragged somewhere, which is evidence that the disappearing thumbnail frustrates users. — [HN Showcase](https://hnshowcase.com/post/47436732/easyshot-macos-screenshot-thumbnails-that-don-t-disappear-af)

### Inferences
- Current routes to the newest file: (a) drag the native thumbnail within about 5 s; (b) open Finder or a Downloads Stack in the Dock and sort by date; (c) a shelf app that captures screenshots automatically (Dropover); (d) a single-purpose sticky-thumbnail tool (EasyShot). None of these covers screenshots and downloads together in one always-there spot.
- A "Latest File" drag card in a menu bar panel, watching the screenshot folder and Downloads, would combine (a) to (d). Watching Desktop or Downloads triggers macOS folder-access (TCC) prompts, so a careful first-run explanation matters. (This is an inference; I found no cited complaint about this.)

### Gaps
- No sources found on Raycast or Alfred "latest file/screenshot" features, Dock Stacks complaints, or privacy prompts for Desktop and Downloads in shelf apps.
- Current Dropover Pro, Dropzone 4 and Yoink prices were not confirmed.
- Product Hunt and Setapp review samples are small (about 17 reviews), so they are not representative.

## Gaps a system-monitor app with one grouped menu bar item, hover panels and a "Latest File" card could fill

### Takeaway
Two pains overlap here: too many icons (made worse by the notch and by managers that break every year) and no quick way to grab the newest file. One self-contained status item avoids both without needing other apps' internals or Screen Recording.

### Cited Findings
- Managers break every year and hide or move icons rather than reduce them (see section 1). — [macos-tahoe.com](https://macos-tahoe.com/blog/macos-27-menu-bar-apps-broken-bartender-ice-icons-hidden-behind-notch-fix-2026/)
- Users distrust apps with broad permissions after the Bartender case. — [MacRumors 2024](https://www.macrumors.com/2024/06/04/bartender-mac-app-new-owner/)
- Notch-aware hover panels are an emerging pattern (Lounge). — [Product Hunt Lounge 2](https://www.producthunt.com/products/lounge-2)
- A screenshot that stays put until dragged is wanted badly enough to justify standalone apps. — [EasyShot](https://hnshowcase.com/post/47436732/easyshot-macos-screenshot-thumbnails-that-don-t-disappear-af); [Dropover KB](https://dropoverapp.com/kb/screenshots)

### Inferences
- Positioning: "one icon instead of six; no Screen Recording; no Accessibility; survives macOS updates because it only owns its own item."
- A Latest File card covering both screenshots and Downloads (with "reveal" and "copy path") fills a gap no single surveyed tool covers.
- Risk: users who already run Bartender or Ice may hide the item itself. It is worth testing with the macOS 27 overflow button.

### Gaps
- No user survey data on how many menu bar items a typical user has, or how often items are hidden by the notch.
