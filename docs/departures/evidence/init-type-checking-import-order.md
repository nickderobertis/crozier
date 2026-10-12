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

## Reordered client imports beside another difference

A root package whose tag subpackages re-export their hoisted types orders the
root client's and environment's statements differently. Fern sorts them by
module among the tag subpackages'; crozier writes them ahead of every one. The
handed-off `kompaz` witness shows it:

```text
$ diff <(sed -n '/^if typing.TYPE_CHECKING:/,/^_dynamic_imports/p' preview/fern-python-sdk/src/fern/__init__.py) \
       <(sed -n '/^if typing.TYPE_CHECKING:/,/^_dynamic_imports/p' crozier/src/fern/__init__.py)
6,7d5
<         BadRequestErrorBody,
<         NotFoundErrorBody,
9d6
<         UnauthorizedErrorBody,
17d13
<     from .auth import AuthMeResponse
19a16
>     from .auth import AuthMeResponse
```

The `.auth`, `.client` and `.environment` statements are the same text on both
sides, one permutation of each other. The three `*ErrorBody` names are a
separate generator residual (Fern hoists the document's `application/problem+json`
component responses as models), so the blocks do not sort to the same text.
The rule then takes the window of statements that moves, here
`from .auth` through `from .environment`, as one departure at crozier's first
line of it. It does so only when the statements moving are the root client's
and environment's alone and every statement in the window is identical on both
sides. The `*ErrorBody` lines stay a difference, so the file still fails:
`crozier compare` reports `init-type-checking-import-order` at
`src/fern/__init__.py` line 20 and still lists the file as differing.
`init_import_order_admits_reordered_statements_beside_another_difference` in
`src/parity.rs` holds both halves, and that a tag subpackage's statement moving,
or a moved statement importing another name, is no departure.
