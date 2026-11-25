# A docstring example whose string literal escapes a character

DRAFT — the parent node completes this note with the certified-pair run.

The registered `registered-literals-marcelo-earth-generative-manim-8e1e6b29`
golden documents `render_video` with a declared multi-line `code` value. Its
`README.md` and `reference.md` pass
`code="from manim import *\nclass GenScene(Scene):\n…"`, and both client
docstrings (`src/fern/client.py`, sync and async) carry the same bytes inside an
ordinary triple-quoted docstring. Python evaluates that docstring before
`help()` or an IDE shows it, so the reader is shown the escape as a real line
break inside the string argument.

Executed over the committed golden (Fern's bytes): evaluate the sync docstring
with `ast.get_docstring`, take the text after `Examples\n--------`, strip its
eight-space indent, and `ast.parse` it:

```
SyntaxError: unterminated string literal (detected at line 5) line 5
```

The same steps over crozier's tree, whose docstring doubles every backslash in
the example (`code="from manim import *\\nclass …"`), parse, and the evaluated
example is byte-identical to the README's call.
