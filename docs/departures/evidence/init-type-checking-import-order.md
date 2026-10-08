# `init-type-checking-import-order`

**Kind:** `ordering`. crozier sorts a lazy `__init__.py`'s `TYPE_CHECKING`
imports.

## The command and its result

Over the committed `alma-france` corpus document, with the corpus's settings:

```text
$ spec=$(python3 tools/corpus/corpus_sources.py prepare --fixture alma-france --output /tmp/alma-src)
$ crozier generate --spec "$spec" --output /tmp/alma --package-name fern --project-name default_package_name
$ diff <(sed -n '/^if typing.TYPE_CHECKING:/,/^_dynamic_imports/p' tests/fixtures/alma-france/expected/src/fern/__init__.py) \
       <(sed -n '/^if typing.TYPE_CHECKING:/,/^_dynamic_imports/p' /tmp/alma/src/fern/__init__.py)
27d26
<     from .balance_transactions import ListbalancetransactionsResponse
29a29
>     from .balance_transactions import ListbalancetransactionsResponse
```

The two blocks import the same names, one statement in another place; sorted by
`ruff check --select I --fix`, they are the same text. The block runs only under
a type checker, so the order changes nothing the SDK does. crozier emits its
imports sorted (`src/emit.rs`, the lazy-loader assembly), and the rule takes the
block's differing lines as one departure, at crozier's first one, only when the
two blocks sort to the same text.
