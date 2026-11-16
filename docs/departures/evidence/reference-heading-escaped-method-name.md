# Escaped method names in reference headings

**Kind:** `fern-defect`. Measured at Fern CLI 5.200.0 / fern-python-sdk 5.41.25.

When an operation's method name would shadow a Python keyword or builtin, Fern's
generated client escapes it with a trailing `_`. Its `reference.md` heading
names the method without the escape. The Apideck ATS golden
(`tests/fixtures/apideck.com-ats/expected`) writes

```text
<details><summary><code>client.applicants.<a href="src/fern/applicants/client.py">all</a>(...) -> GetApplicantsResponse</code></summary>
```

while `src/fern/applicants/client.py` defines `def all_(` (line 55) and no
`all`. The usage example under the same heading calls
`client.applicants.all_(...)`. At this pair Fern anchors every other heading at
its method's lines (`#L<start>-L<end>`); these headings get no anchor, because
the name Fern looks up is not defined in the file.

Calling the documented method on the real generated SDK fails:

```text
$ python -B -c "
import sys; sys.path.insert(0, 'tests/fixtures/apideck.com-ats/expected/src')
from fern import FernApi
client = FernApi(api_key='k', apideck_consumer_id='c', apideck_app_id='a')
print('all_:', callable(client.applicants.all_))
client.applicants.all
"
all_: True
AttributeError: 'ApplicantsClient' object has no attribute 'all'. Did you mean: 'all_'?
```

The census over every committed reference tree at this pair (1194 trees: the
corpus goldens and overlays, the measurements, and the handwritten, authored,
probe and departure-evidence trees) finds 77 such headings, every one without
an anchor. By name: `all` 59, `import` 3, and `uuid`, `map`, `long`, `int`,
`float`, `bool` and `async` 2 each, `del` 1. Overlay trees are counted by the
files they carry; compared whole, as the gate rebuilds them, they hold more.

The census reads each tree's `reference.md` headings and, for each, the methods
of the first class not named `Async…` in the linked client (by `ast`), and
counts a heading whose name the client lacks but defines with a trailing `_`:

```text
$ find tests/fixtures docs -name reference.md \( -path '*expected*' -o -path '*fern-reference*' \) | python3 -c '
import ast, re, sys, pathlib
n = 0
for ref in map(pathlib.Path, sys.stdin.read().split()):
    for href, name in re.findall(r"<summary><code>client\.[\w.]*<a href=\"([^\"#]*)[^\"]*\">(\w+)</a>", ref.read_text()):
        client = ref.parent / href
        if not client.is_file():
            continue
        cls = next((c for c in ast.parse(client.read_text()).body if isinstance(c, ast.ClassDef) and not c.name.startswith("Async")), None)
        names = {m.name for m in getattr(cls, "body", []) if isinstance(m, (ast.FunctionDef, ast.AsyncFunctionDef))}
        n += name not in names and name + "_" in names
print(n)'
77
```

The departures ledger pins 75 occurrences in the trees the gates compare. Seven
of the census's headings are in two superseded measurement trees no gate
compares (`superseded-fixtures/depot-bin-ledger` 6, `ferry-berth-desk` 1).

crozier names the method the client defines and anchors the link at its lines,
found as for every other heading. The rule admits only a `reference.md` heading
whose method name, less its trailing `_`, is Fern's, where crozier's linked
client defines the escaped name, the link carries a `#L<start>-L<end>` range,
and every other byte of the line is Fern's. Its unit test rejects another
module, a method the client does not define, a name needing no escape, a
missing or malformed range, and any other change on the line; the corpus and
handwritten comparisons apply it over complete trees, and the departures
ledger pins each occurrence.
