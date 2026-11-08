# Menu bar and panels

## One item, many readings

By default every reading sits in **one compact menu bar item**, drawn side by side without macOS's gaps. Hover over a
part to open its panel; the panel stays open while the pointer is over it, and scrolls inside when it is taller than the
screen. Panels are kept short: details sit behind disclosures (▸) that remember whether you opened them, in tooltips
(hover a figure or a title for what it means), or on the dashboard.

Prefer separate items you can ⌘-drag? Dashboard → **Menu Bar** → *Look* → turn off **Group all items into one**.

| Part | Shows | Its panel |
|---|---|---|
| CPU | processor load | 2-minute graph, average and peak, the apps using the processor most, each core (performance and efficiency) |
| GPU | graphics load | the same for the graphics chip; optionally the memory it holds |
| RAM | memory used | apps / system / compressed / cached / free, swap, memory pressure, the apps using the most memory |
| STORAGE | storage used (or free, or read/write speed during big copies) | where the space went, app caches with size limits, Downloads tidy-up, biggest folders |
| TEMP | processor temperature | processor, graphics, battery and storage temperatures, fan speeds, every sensor |
| NET (off by default) | download / upload speed | live diagram, a 2-minute strip with the peak, the apps using the network most |
| BATT | real fill to 0.1% and the true charge state (steps aside on a Mac with no battery) | health, capacity, recharges, charge plan, devices' batteries, energy mode, Extreme Saver |
| Power (3:01 LEFT / 5:02 TO FULL / MAC USES) | time left or to full, with battery watts in or out (the Mac's draw when the battery rests, and always on a Mac with no battery) | live flow diagram, power per app, idle-app suggestions |
| SWITCH | how many of your Switches are on (n/total; glows red when one failed); steps aside while none is on, changing or failed | a row per group with its count; the switches that are on, with toggles; click a group for all |
| FILES | how many files are on the Shelf; steps aside while the Shelf is empty | Latest File, the Shelf, the clipboard |

FILES and SWITCH come back by themselves when there is something to show. To keep them always, use Dashboard → **Menu
Bar** → *Items* → *Files: show even when the Shelf is empty* and *Switches: show even when none is on*. Figures move
only on a real change (2 points, 2°, 2 W, 30% for network speed) or after 10 seconds, and the menu bar redraws them at
most every 4 seconds (at once when the charger, charging, a warning or Extreme Saver changes), so the bar stays calm.

## Charge states, in plain words

The battery part shows what the current is actually doing, not just what macOS's icon says:
**Charging**, **Topping up**, **On hold** (Optimized Battery Charging), **At limit** (Charge Limit), **Full**, or the
time left on battery. If the reported state and the measured current disagree for a minute, the Battery panel says so.

## Where each row comes from

Every list says what a row is: an app (with its icon), an Apple app, a part of macOS with a plain-words name
("Draws everything on screen", "Spotlight search indexing"), a command-line tool, or a folder. Click a row of any
"Using … most" list to see its processes and quit the ones you own (see [Battery and power](03%20Battery%20and%20power.md)).

## Colours and warnings

- **Glow red behind an item when it needs attention** — processor, memory, storage, battery and temperature limits you choose
  (Dashboard → Menu Bar → *Alerts*).
- **Colours by value** — optional green → red bands per item, each with its own four limits (Dashboard → Menu Bar →
  *Colours*).
- **Battery and power: a glow and a line** — a glow in a colour from how many hours a full battery would last at the
  last minute's drain, fading out as the drain gets lighter, and a thin line as long as the watts. On the charger the
  line shows how fast it charges.

## Keys inside a panel

A panel you opened by clicking its item or with a shortcut takes the keyboard. (One that opened because the pointer
passed over the item doesn't: it never takes the keyboard from the app you're typing in.)

| Key | What it does |
|---|---|
| ← → | the panel to the left or right, going round at the ends |
| Esc | closes the panel |
| D | this panel's page in the dashboard |
| ⌘, | Settings |
| Tab | moves through the rows you can click |
| Return or Space | presses the row you're on |

Buttons and switches join the Tab order when *Keyboard navigation* is on in System Settings → Keyboard.

## Display settings in macOS

Sparewatt follows System Settings → Accessibility → Display. *Increase contrast* gives cards edges and diagrams stronger
lines. *Differentiate without colour* adds a shape wherever colour was doing the talking, including a `▲` or `!` after a
figure in the menu bar. *Reduce transparency* makes the floating shelf and the menu bar's glow solid. *Reduce motion*
makes the live diagrams still pictures.

## Look and speed

Dashboard → Menu Bar → *Look*: words or small icons, text size, update speed (every 1, 2, 5 or 10 seconds — slower uses
a little less battery), and a last-minute trend line on one item.
