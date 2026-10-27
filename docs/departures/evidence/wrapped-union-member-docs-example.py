# llmlint: ignore-file[new_code_lands_in_a_project] documentary evidence kept beside the departure note it supports, like the other docs/departures/evidence scripts: no Nx target runs it, and the note records running it explicitly against the committed certified output.
"""Compile the certified README and reference examples of a wrapped union member.

Run with any Python 3 to show the certified examples are not Python. Run with an
interpreter that has the certified SDK installed (`pip install <fern-expected>`)
to also bind the corrected constructor and serialize it.
"""
import pathlib
import re

root = pathlib.Path(__file__).resolve().parents[2]
tree = root / 'openapi-surface/handwritten/tidepool-survey-log/fern-expected'
snippets = []
for name in ('README.md', 'reference.md'):
    text = (tree / name).read_text(encoding='utf-8')
    for block in re.findall(r'```python\n(.*?)```', text, flags=re.S):
        if 'SurveyEntry_Level(' in block:
            snippets.append((name, block))
assert len(snippets) == 3, snippets
for name, block in snippets:
    assert re.search(r'SurveyEntry_Level\(\n\s+level=,\n', block), block
    try:
        compile(block, name, 'exec')
    except SyntaxError as error:
        print(f'{name}: certified example does not compile: {error.msg} (line {error.lineno})')
    else:
        raise AssertionError(f'{name}: certified example compiled')
corrected = 'from fern import SurveyEntry_Level\nentry = SurveyEntry_Level(value=1.1)\n'
compile(corrected, 'corrected', 'exec')
try:
    import fern  # noqa: F401 -- imported only to learn whether the certified SDK is installed
except ImportError:
    print('certified SDK not installed: binding not checked')
else:
    from fern import SurveyEntry_Level

    namespace = {}
    exec(corrected, namespace)
    entry = namespace['entry']
    assert entry.value == 1.1 and entry.entry_type == 'level'
    print('corrected:', entry.dict(by_alias=True))
    try:
        SurveyEntry_Level(level=1.1)
    except Exception as error:  # pydantic's ValidationError
        print('certified keyword rejected by the certified SDK:', type(error).__name__)
    else:
        raise AssertionError('certified keyword accepted')
