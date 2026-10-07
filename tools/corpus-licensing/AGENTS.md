# corpus-licensing

- The lint keeping `docs/corpus-licensing.md` the one statement of which
  licences the corpus admits. It reads the tracked Markdown through
  `git ls-files`, and its suite plants a second enumeration in the real tree and
  stages it, so both drive the real `git`: a project of its own, apart from the
  offline corpus scripts.
- The planted file and its staging are undone by each case's cleanup; a run
  killed mid-case can leave `docs/corpus-licensing-drift-probe-*.md` staged —
  `git rm --cached` it.
