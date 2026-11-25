# A docstring example whose string literal escapes a character

The [Logbook document](../../fern-measurements/worked-examples/docstring-example-escapes/openapi.yml)
declares the body property example `"Moored at dawn.\nWind\tNE 12 kn, \"steady\""`.
Fern CLI 5.216.0 with `fernapi/fern-python-sdk` 5.42.0, the certified pair,
generated its [complete tree](../../fern-measurements/worked-examples/docstring-example-escapes/fern-expected/).
`README.md` and `reference.md` pass
`entry="Moored at dawn.\nWind\tNE 12 kn, \"steady\""`, and both `write_entry`
docstrings in `src/fern/client.py` carry
`entry='Moored at dawn.\nWind\tNE 12 kn, "steady"'` inside an ordinary
triple-quoted docstring. Python evaluates that docstring before `help()` or an
IDE shows it, so the reader is shown `\n` as a real line break inside the string
argument, and the example they copy no longer parses.

The check evaluates each docstring with `ast.get_docstring`, takes the text after
`Examples\n        --------\n`, removes its eight-space indent line by line and
parses it:

```python
import ast, sys

for node in ast.walk(ast.parse(open(sys.argv[1]).read())):
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        doc = ast.get_docstring(node, clean=False) or ""
        if "Examples" in doc:
            body = doc.split("Examples\n        --------\n", 1)[1]
            example = "\n".join(line.removeprefix(" " * 8) for line in body.splitlines())
            try:
                ast.parse(example)
                print(f"{node.name}: parses")
            except SyntaxError as error:
                print(f"{node.name}: SyntaxError: {error.msg} (line {error.lineno})")
```

Over the certified tree's `src/fern/client.py` (sync, then async):

```
write_entry: SyntaxError: unterminated string literal (detected at line 7) (line 7)
write_entry: SyntaxError: unterminated string literal (detected at line 12) (line 12)
```

Over crozier's `src/fern/client.py` for the same document, whose docstrings
double each backslash of the example
(`entry='Moored at dawn.\\nWind\\tNE 12 kn, "steady"'`):

```
write_entry: parses
write_entry: parses
```

and the evaluated example is the README's call. A raw docstring would also
stop the evaluation, but it would change the prose escapes the certified pair
writes and crozier matches, so only the example lines are doubled.
`worked_examples::docstring_examples_keep_their_string_escapes` holds the
measurement's tree to the certified pair's through this departure in both enum
modes, and `documentation_audit` audits every golden's docstring examples as
Python evaluates them. The registered marcelo-earth generative-manim golden's
declared multi-line `code` value is the real witness of the same shape.
