# corpus-licensing

- A project apart from the offline corpus scripts because its lint and suite
  drive the real `git`.
- The suite writes only a scratch repository holding the real script and a copy
  of every tracked Markdown document, never the checkout: Nx runs other gate
  targets beside it, and they read `docs/` and the index while it runs.
