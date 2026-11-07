# Links for Shortcuts and scripts

Sparewatt opens `sparewatt://` links, so a Shortcut, a script, a launcher or a link in a note can drive it. A link does
what the matching button does, with the same password prompts, panels and dashboard pages.

## How to use them

- **Shortcuts:** add the **Open URLs** action and type the link, e.g. `sparewatt://extreme-saver/toggle`.
- **Terminal or a script:** `open "sparewatt://extreme-saver/toggle"`.
- **A link in a note:** clicking `sparewatt://dashboard/history` opens that dashboard page.

If Sparewatt isn't running, the link starts it and runs once the menu bar item is drawn (about 3 seconds).

## Every link

| Link | Does |
|---|---|
| `sparewatt://extreme-saver/on` · `/off` · `/toggle` | Extreme Saver on, off, or the other way (macOS asks for your password, as the switch does) |
| `sparewatt://energy-mode/battery/low` · `/automatic` · `/high` | the energy mode on battery (asks for your password) |
| `sparewatt://energy-mode/charger/low` · `/automatic` · `/high` | the energy mode on the charger (asks for your password) |
| `sparewatt://panel/<name>` | opens a menu bar panel: `power`, `battery`, `cpu`, `gpu`, `memory`, `storage`, `temperature`, `network`, `files`, `switches`; the matching dashboard page if that part is hidden |
| `sparewatt://dashboard` | opens the dashboard |
| `sparewatt://dashboard/<page>` | opens one page: `overview`, `cpu`, `gpu`, `memory`, `storage`, `temperature`, `network`, `battery`, `power`, `history`, `on-battery`, `extreme-saver`, `watchlist`, `profiles`, `menu-bar`, `this-app`, `startup-items`, `switches`, `assistant` |
| `sparewatt://switch/<name>/on` · `/off` · `/toggle` | turns one of your [Switches](../features/10%20Switches.md) on or off by its name |
| `sparewatt://share` · `/day` · `/week` | opens the dashboard's share sheet on the ["My Mac today"](../features/11%20Dashboard%2C%20history%20and%20this%20app.md#my-mac-today-share-card) card (`share` alone, or `/day`) or the ["My Mac this week"](../features/11%20Dashboard%2C%20history%20and%20this%20app.md#my-mac-this-week-card) card |

## Details

- **Any case:** `sparewatt://Panel/CPU` works too. `auto`, `low-power` and `high-power` also work for energy modes.
- **Page names:** a page's title in lower case with dashes works as well: `processor`, `power-flow`,
  `shelf-profiles-alerts`.
- **Switch names** keep their spelling; write a space as `%20` (`sparewatt://switch/My%20Server/on`) and a slash in a
  name as `%2F`. An exact match is tried first, then the same name in any case. `on` does nothing when the switch is
  already on, and `off` when it is off.
- **Nothing happens** for a link Sparewatt doesn't understand, or for an energy mode that is already set.
- Notifications use the same links to say which panel a click opens; the Monday summary uses `sparewatt://share/week`.

See also [Keyboard shortcuts](Keyboard%20shortcuts.md).
