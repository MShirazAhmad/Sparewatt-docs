# macOS disk-space / folder-size apps: features, status and user pain points (as of 2026-11)

Scope: DaisyDisk, GrandPerspective, OmniDiskSweeper, Disk Inventory X, CleanMyMac (Space Lens), the macOS Storage settings, and Finder's "Calculate all sizes". The research used about 13 tool calls. Reddit threads could not be read directly because the mirror sites blocked automated fetches. Much of the comparison material comes from vendor or competitor blogs (MacPaw, Nektony, Mole, DissectMac), so their rankings are flagged as biased.

## Core features, pricing and maintenance status per app

### Takeaway
DaisyDisk (paid, one-time licence) and GrandPerspective (free, or paid on the App Store) are actively maintained in 2026. OmniDiskSweeper is free and updated slowly. The original Disk Inventory X is abandoned (Intel-only v1.3) and survives only as community forks. CleanMyMac is subscription-priced and its Space Lens is one module of a larger suite. Apple's built-in tools are free, but they are coarse or slow.

### Cited Findings
- **DaisyDisk.** One-time purchase that covers several personal Macs, with a money-back window. "Actively maintained": v4.34.2 shipped in July 2026, and 4.34 added APFS clone accounting and hard-link/clone detection. It has an administrator scan mode for unreadable files — [Mole blog (competitor)](https://mole.fit/blog/daisydisk-alternative.md)
- The DaisyDisk version reported in June 2026 was 4.33.3 — [Gizmodo](https://gizmodo.com/download/daisydisk). Rosetta Check reports 4.34.2 builds in Aug–Sep 2026 — [Rosetta Check](https://rosettacheck.com/apps/g9734m3i)
- **DaisyDisk price:** a $9.99 one-time figure appears only on a competitor-affiliated blog and is unverified — [diskcleaner-site](https://diskcleaner-site.pages.dev/blog/best-one-time-purchase-mac-cleaner)
- The DaisyDisk trial scans and previews, but deleting files needs a licence. In the trial, hidden and purgeable space is only detected. Revealing it and purging it need the full version — [DaisyDisk guide: full vs trial](https://daisydiskapp.com/guide/full-vs-trial)
- The standalone (non-App-Store) DaisyDisk can show hidden space, purge purgeable space and scan as administrator. It also added a preference tab to help users grant Full Disk Access (Mojave and later) — [DaisyDisk guide](https://daisydiskapp.com/guide/disks-overview)
- **GrandPerspective.** Treemap view. Free on SourceForge and paid on the App Store ("the same app either way"). It offers "scan compression with quick refresh" and hard-link analysis — [Mole blog](https://mole.fit/blog/daisydisk-alternative.md)
- GrandPerspective 3.7.2 was released on 31 May 2026 and 3.8.0 on 24 Aug 2026; 3.8.0 requires macOS 14 or later — [softantenna](https://softantenna.com/softwares/6661-grandperspective). The readme lists macOS 11+ and Apple silicon or Intel — [SourceForge docs](https://sourceforge.net/p/grandperspectiv/documentation)
- **OmniDiskSweeper.** Free. Sits on Omni's side-project page; "treat it as maintained slowly". An updated build in September 2025 requires macOS 14+ — [Mole blog](https://mole.fit/blog/daisydisk-alternative.md)
- **Disk Inventory X.** The last official version, 1.3, is Intel-only, has no native Apple Silicon build and is described as abandoned — [Rosetta Check](https://rosettacheck.com/apps/com.derlien.DiskInventoryX); [Does It ARM](https://cf.doesitarm.com/app/disk-inventory-x)
- Disk Inventory X has community revivals: "Xs" (a modernization for Apple Silicon) and "Y" (a Swift rewrite), plus a "Z". One commenter calls the Xs UI buggy, and its releases are sparse — [Mac Power Users forum](https://talk.macpowerusers.com/t/disk-inventory-x-resurrected-as-xs-modernization-and-y-rewrite/47391)
- **CleanMyMac Space Lens.** Reviewers praise the visualization as "genuinely useful for quickly identifying storage hogs". Another critic says its design "has much to be desired" — [TechRadar](https://www.techradar.com/reviews/cleanmymac-x-for-mac-review); [softwarehow](https://softwarehow.com/?p=9900)
- CleanMyMac pricing is a subscription. A Capterra reviewer's main complaint is "they require a subscription" — [Capterra](https://www.capterra.com/p/232745/CleanMyMac-X/reviews/?page=10); [G2](https://www.g2.com/products/cleanmymac/reviews)
- **macOS Storage settings** is free and built in. Its limit is "System Data", which Apple says macOS manages — [Mole blog](https://mole.fit/blog/daisydisk-alternative.md)
- **Finder "Calculate all sizes"** (List View, Cmd-J) is set per folder and off by default because calculating all sizes can slow the Mac down — [MacRumors how-to](https://macrumors.com/how-to/view-folder-sizes-on-your-mac); [MacMost](https://macmost.com/how-to-view-folder-sizes.html)
- Adjacent options: ncdu (free CLI with parallel scanning, JSON export/import, and apparent size vs disk usage) and Mole (one-time purchase) — [Mole blog](https://mole.fit/blog/daisydisk-alternative.md)

### Inferences
- The market has split into polished paid scanners (DaisyDisk), free utilitarian ones (GrandPerspective, OmniDiskSweeper), suites (CleanMyMac) and abandonware (Disk Inventory X). None of them is a persistent, lightweight monitor.

### Gaps
- No official 2026 DaisyDisk or CleanMyMac price list was retrieved; check the vendor pages.
- No release notes for OmniDiskSweeper were found beyond the competitor's summary.

## Common complaints / struggling points

### Takeaway
The most documented pain points are four. "System Data" and purgeable space are opaque and misreported. Finder folder sizes are slow and go stale. CleanMyMac's subscription and cancellation practices draw complaints. Different tools report different totals because of APFS snapshots and clones. I found no sources with hard scan-speed benchmarks.

### Cited Findings
- **System Data confusion.** Eclectic Light calls System Data "an etcetera, a ragbag including all sorts of files". It says the figure is "little more than a guesstimate", and Storage Settings totals often differ from Disk Utility's — [Eclectic Light, Feb 2025](https://eclecticlight.co/2025/02/11/what-is-system-data-in-storage-settings/)
- APFS/Time Machine snapshots keep deleted data for up to 24 h, and that space often shows up as System Data — [Eclectic Light](https://eclecticlight.co/2025/02/11/what-is-system-data-in-storage-settings/)
- Users report System Data of 142 GB, and in one case over 700 GB — [Apple Community 255156745](https://discussions.apple.com/thread/255156745); [Apple Community JP 255224518](https://discussions-jp-prz.apple.com/thread/255224518). System Data takes "a third of my local storage" — [MPU forum](https://talk.macpowerusers.com/t/system-data-takes-up-a-third-of-my-local-storage/43291)
- System Data can balloon past 100 GB because of update files and Spotlight/iCloud reindexing, and Apple offers no delete button — [Macworld](https://www.macworld.com/article/676493/how-to-delete-system-data-mac.html,)
- Purgeable space is reclaimed when macOS decides; users cannot force it in Settings. One Apple Community answer gives the rule of thumb "Free storage = Available − Purgeable" — [Apple Community](https://discussions.apple.com/thread/255937840)
- Even DaisyDisk cannot scan purgeable space on APFS: it sits "outside of any scannable area" and appears as a single hidden-space item — [DaisyDisk guide](https://daisydiskapp.com/guide/purgeable-space)
- **Inaccurate or inconsistent sizes.** Different tools report different totals for the same volume because they count size differently (apparent size vs allocated size, clones) — [Mole blog](https://mole.fit/blog/daisydisk-alternative.md). DaisyDisk added clone accounting only in 4.34 (2026) — same source
- **Finder sizes are slow and stale.** "Calculate all sizes" can significantly slow Finder when it opens folders with many items (older thread) — [Apple Community 250622175](https://discussions.apple.com/thread/250622175?page=1). After a change, Finder shows the old value until it recalculates — [MacRumors forum](https://forums.macrumors.com/threads/view-folder-sizes-on-your-mac.2148110). Finder figures "are only refreshed periodically" — [Eclectic Light](https://eclecticlight.co/2025/02/11/what-is-system-data-in-storage-settings/)
- **CleanMyMac upselling and subscriptions.** Trustpilot reviewers report cancellation trouble, charges after cancelling, and in Jan 2026 being told to "calm down". MacPaw replies that no support contact is needed to cancel — [Trustpilot](https://www.trustpilot.com/review/www.macpaw.com?page=7). I found no source that documents upsell prompts inside Space Lens itself.
- **Full Disk Access.** DaisyDisk ships a helper tab for adding itself to FDA — [DaisyDisk guide](https://daisydiskapp.com/guide/disks-overview). Nektony's help pages also document FDA requirements — [Nektony help](https://nektony.com/help/disk-inspector/technical-information). Mole flags items it cannot size with a badge instead of silently dropping them — [Mole blog](https://mole.fit/blog/daisydisk-alternative.md)
- **Scan speed.** Blog ratings conflict: DissectMac rates OmniDiskSweeper "Fast" and GrandPerspective "Moderate" — [DissectMac (vendor)](https://dissectmac-com.pages.dev/blog/daisydisk-alternatives). A Chinese review calls DaisyDisk very fast — [sspai](https://sspai.com/post/40503)

### Inferences
- Users' biggest confusion is not "which folder is big" but "where did space go that no scanner can see" (snapshots, purgeable space, System Data). A tool that explicitly reconciles the scanned total with the volume's used total would address a real gap.
- The FDA friction is real enough that vendors build onboarding for it.

### Gaps
- No primary Reddit quotes on scan speed or rescan frustration could be retrieved; the mirrors blocked the fetch.
- No independent timed benchmarks were found.

## Incremental scanning / caching

### Takeaway
None of the major GUI analyzers documents a persistent cache with FSEvents-based incremental refresh; each rescans on demand. Caching shows up only in niche tools: diskr (a Rust CLI using FSEvents history) and Mole (cached results, re-measured after 6 h). GrandPerspective has a "quick refresh" of a saved scan.

### Cited Findings
- diskr keeps cached sizes between runs. On relaunch it uses the change history to revalidate only the directories that changed, and it uses getattrlistbulk for logical and allocated sizes — [docs.rs diskr](https://docs.rs/crate/diskr/latest)
- Mole: "results are cached and re-measured in the background after 6 hours", so a total can be briefly out of date — [Mole blog](https://mole.fit/blog/daisydisk-alternative.md)
- GrandPerspective: "scan compression with quick refresh" — [Mole blog](https://mole.fit/blog/daisydisk-alternative.md)
- ncdu has no built-in cache, but it can export and import scans (JSON or binary) — same source
- Free Disk Space for Mac cannot retain data from a previous scan and rescans on every launch — [Softpedia](https://mac.softpedia.com/get/Utilities/Free-Disk-Space.shtml)

### Inferences
- A menu-bar app that keeps a size cache and uses FSEvents to update only the changed subtrees would be different from DaisyDisk, GrandPerspective and OmniDiskSweeper, which all rescan whole trees on demand.

### Gaps
- I could not confirm from DaisyDisk's own docs whether it caches between sessions; no source says so either way.

## Gaps a menu-bar "biggest folders, cached, time-limited" monitor could fill

### Takeaway
Existing menu-bar disk apps show free space or threshold alerts (Disk-O, FreeSpace, DiskTree, ClearDisk), and one tracks folder growth (DiskPulse). The full analyzers are open-a-window, scan-everything tools. No mainstream tool combines a cached, always-on "top N biggest or fastest-growing folders" list with a bounded scan budget.

### Cited Findings
- Menu-bar options are mostly free-space gauges: Disk-O (free space in the menu bar), FreeSpace (all volumes, red threshold warning), DiskTree (ring that turns amber/red, treemap, 7-day free-space history), and ClearDisk (developer caches, 80%/90% thresholds) — [Softpedia Disk-O](https://mac.softpedia.com/get/System-Utilities/Disk-O.shtml); [FreeSpace App Store](https://apps.apple.com/au/app/freespace/id457520846); [DiskTree releases](https://github.com/Ryware/DiskTree/releases); [ClearDisk](https://awesome.ecosyste.ms/projects/github.com%2Fbysiber%2Fcleardisk)
- DiskPulse ($4.99, Mac App Store) tracks growth of chosen folders on a schedule and alerts on large new files — [App Store](https://apps.apple.com/app/diskpulse/id6761638331)
- Disk Buddy's author built it to "actively monitor my disk space" instead of waiting for the "disk almost full" warning — [r/MacOSApps, Jan 2025](https://redlib.ssps.io/r/MacOSApps/comments/1i0mv1c/track_your_disk_space)
- Disko's author built it because macOS lacks a quick built-in way to see which folders are largest — [r/macapps, Mar 2025](https://reddit.fsky.io/r/macapps/comments/1jf4ra0/disko_an_opensource_disk_usage_analyzer_without)

### Inferences
- Opportunity areas:
  1. Cached top-N folders in the menu bar, refreshed incrementally through FSEvents.
  2. A hard time or IO budget per refresh, so a 1 TB home folder never causes a long full scan.
  3. Growth deltas ("+12 GB in ~/Library/Caches since yesterday").
  4. A reconciliation line ("scanned 410 GB; volume used 520 GB; ~110 GB snapshots/purgeable/System Data") with an explanation.
  5. Graceful handling when Full Disk Access is missing: badge the unreadable areas instead of under-reporting them.
  6. Allocated-size, clone-aware counting.
  7. No subscription and no upsell, since CleanMyMac's model is a known irritant.
- The time-limit idea is new: none of the sources describes a budgeted or partial scan.

### Gaps
- No user survey data was found on demand for a menu-bar folder-size view specifically. The evidence is indirect, from developer launch posts.
