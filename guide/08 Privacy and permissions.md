# Privacy and permissions

## What stays on your Mac

Everything. Sparewatt collects nothing and sends nothing about you. It makes only two kinds of network request, both
your choice:

- the once-a-day update check against GitHub, **off** by default;
- a [Switch](../features/10%20Switches.md) whose running check is *a web address answers* asks that address (usually a
  server on your own Mac) every 10 seconds.

The clipboard history is kept in memory only and skips passwords. Entries you **pin** are saved, as plain text, in
Sparewatt's settings so they survive a restart — don't pin secrets.

## Prompts you may see

| Prompt | When | Why |
|---|---|---|
| "macOS cannot verify the developer" | first launch | the app is not signed with an Apple Developer ID ([Getting started](01%20Getting%20started.md)) |
| Administrator password | changing an energy mode, On Battery settings, Extreme Saver | these use macOS's own `pmset`, which needs an administrator each time |
| "Sparewatt wants to control System Events" | turning *Start Sparewatt when you log in* on or off, or opening that setting | login items are read and set through System Events |
| "Sparewatt would like to access files in your Downloads folder" | the first *Look* in Downloads tidy-up | it reads the folder to find old installers and duplicate downloads |

Reading the numbers needs no permission.

## Folders

The storage list skips folders macOS protects (Desktop, Documents, Downloads, Library, Pictures, Movies, Music).
Latest File finds files through Spotlight, so it never opens those folders itself. Downloads tidy-up is the exception:
it reads your Downloads folder when you click *Look*, after macOS has asked you once. Change that answer in System
Settings → Privacy & Security → Files and Folders → Sparewatt.

## Deleting things

- Clearing a cache (after a confirmation), Downloads tidy-up and the Shelf's Trash button **move files to the Trash**,
  so they can be put back.
- The one thing that deletes outright: a cache **size limit** you set empties that cache when it grows past the limit —
  only ever inside `~/Library/Caches`.
- Quitting an app from Sparewatt is a normal quit (the app can ask to save). Force Quit asks you first.
