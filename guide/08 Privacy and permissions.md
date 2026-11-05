# Privacy and permissions

## What stays on your Mac

Everything. Sparewatt collects nothing and sends nothing. The only network request it can make is the once-a-day
update check against GitHub, which is **off** by default.

The clipboard history is kept in memory only (never written to disk) and skips passwords.

## Prompts you may see

| Prompt | When | Why |
|---|---|---|
| "macOS cannot verify the developer" | first launch | the app is not signed with an Apple Developer ID ([Getting started](01%20Getting%20started.md)) |
| Administrator password | changing an energy mode, On Battery settings, Extreme Saver | these use macOS's own `pmset`, which needs an administrator each time |
| "Sparewatt wants to control System Events" | turning *Start Sparewatt when you log in* on or off, or opening that setting | login items are read and set through System Events |

Reading the numbers needs no permission.

## Folders

The storage list skips folders macOS protects (Desktop, Documents, Downloads, Library, Pictures, Movies, Music).
Latest File and Downloads tidy-up find files through Spotlight, so Sparewatt never opens those folders itself.

## Deleting things

- Clearing a cache and Downloads tidy-up **move files to the Trash** — nothing is deleted outright.
- Automatic cache size limits delete only inside `~/Library/Caches`.
- Quitting an app from Sparewatt is a normal quit (the app can ask to save). Force Quit asks you first.
