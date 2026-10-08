# corpus-licensing

- The lint keeping `docs/corpus-licensing.md` the one statement of which
  licences the corpus admits. It reads the tracked Markdown through
  `git ls-files`, and its suite plants a second enumeration and stages it, so
  both drive the real `git`: a project of its own, apart from the offline
  corpus scripts.
- The suite writes only a scratch repository holding the real script and a copy
  of every tracked Markdown document, never the checkout: Nx runs other gate
  targets beside it, and they read `docs/` and the index while it runs.
