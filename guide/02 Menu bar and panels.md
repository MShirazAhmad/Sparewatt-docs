# Menu bar and panels

## One item, many readings

By default every reading sits in **one compact menu bar item**, drawn side by side without macOS's gaps. Hover over a
part to open its panel; the panel stays open while the pointer is over it, and scrolls inside when it is taller than the
screen. Panels remember what you opened or ticked.

Prefer separate items you can ⌘-drag? Dashboard → **Menu Bar** → *Look* → turn off **Group all items into one**.

| Part | Shows | Its panel |
|---|---|---|
| CPU | processor load | 2-minute graph, average and peak, the apps using the processor most, each core (performance and efficiency) |
| GPU | graphics load | the same for the graphics chip; optionally the memory it holds |
| RAM | memory used | apps / system / compressed / cached / free, swap, memory pressure, the apps using the most memory |
| STORAGE | storage used (or free, or read/write speed during big copies) | where the space went, app caches with size limits, Downloads tidy-up, biggest folders |
| TEMP | processor temperature | processor, graphics, battery and storage temperatures, fan speeds, every sensor |
| NET (off by default) | download / upload speed | speed graph, the apps using the network most |
| BATT | real fill to 0.1% and the true charge state | health, capacity, recharges, charge plan, energy mode, Extreme Saver |
| Power (3:01 LEFT / 5:02 TO FULL / MAC USES) | time left or to full, with battery watts in or out (the Mac's draw when the battery rests) | live flow diagram, power per app, idle-app suggestions |
| SWITCH | how many of your Switches are on (n/total; glows red when one failed) | toggles for each switch |
| FILES | how many files are on the Shelf | Latest File, the Shelf, the clipboard |

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
  (Dashboard → Menu Bar → *Warnings*).
- **Colours by value** — optional green → red bands per item, each with its own four limits.
- **On battery, glow by drain rate** — the battery and power parts glow in a colour from how many hours a full battery
  would last at the current draw.

## Look and speed

Dashboard → Menu Bar → *Look*: words or small icons, text size, update speed (every 1, 2, 5 or 10 seconds — slower uses
a little less battery), and a last-minute trend line on one item.
