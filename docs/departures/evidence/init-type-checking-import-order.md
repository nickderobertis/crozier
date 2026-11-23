# `init-type-checking-import-order`

**Kind:** `ordering`. crozier sorts a subpackage's lazy `__init__.py`
`TYPE_CHECKING` imports by module; the root package's block is written in the
certified pair's own order and is no part of this departure.

## The command and its result

Over the committed `amazonaws.com-cloudformation` corpus document, with the
corpus's settings:

```text
$ spec=$(just corpus-sources prepare --fixture amazonaws.com-cloudformation --output /tmp/cf-src)
$ crozier generate --spec "$spec" --output /tmp/cf --package-name fern --project-name default_package_name
$ diff <(sed -n '/^if typing.TYPE_CHECKING:/,/^_dynamic_imports/p' tests/fixtures/amazonaws.com-cloudformation/expected/src/fern/types/__init__.py) \
       <(sed -n '/^if typing.TYPE_CHECKING:/,/^_dynamic_imports/p' /tmp/cf/src/fern/types/__init__.py)
2,3d1
<     from .resources_to_import import ResourcesToImport
<     from .resources_to_skip import ResourcesToSkip
882a881,882
>     from .resources_to_import import ResourcesToImport
>     from .resources_to_skip import ResourcesToSkip
```

Re-run against the golden Fern CLI 5.216.0 with `fernapi/fern-python-sdk`
5.42.0 wrote, the diff is exactly this. The two blocks import the same names,
two statements in another place; sorted by `ruff check --select I --fix`, they
are the same text. The block runs only under a type checker, so the order
changes nothing the SDK does. crozier emits its imports sorted (`src/emit.rs`,
the lazy-loader assembly), and the rule takes the block's differing lines as one
departure, at crozier's first one, only when the two blocks sort to the same
text.

## The root package's block

The root `src/<package>/__init__.py` is excluded (`root_package_init` in
`src/departures.rs`). Since issue #920 crozier writes its `TYPE_CHECKING` block
as the certified pair does — `.types`, `.errors`, the `from . import` of the tag
subpackages, then the default clients, the root client, the environment, each
tag subpackage's re-exported types and `__version__` sorted by module — so a
reordering there is a plain difference. The same `alma-france` golden this
record once cited for the root block now compares equal with no departure:

```text
$ spec=$(just corpus-sources prepare --fixture alma-france --output /tmp/alma-src)
$ crozier generate --spec "$spec" --output /tmp/alma --package-name fern --project-name default_package_name
$ diff <(sed -n '/^if typing.TYPE_CHECKING:/,/^_dynamic_imports/p' tests/fixtures/alma-france/expected/src/fern/__init__.py) \
       <(sed -n '/^if typing.TYPE_CHECKING:/,/^_dynamic_imports/p' /tmp/alma/src/fern/__init__.py); echo $?
0
```

`docs/fern-measurements/naming-acceptance/root-import-order/` measures the
order on a from-scratch document (`.agent_runtime` between `._default_clients`
and `.client`, `.version` ahead of `.versions`), and
`crates/crozier-e2e/tests/e2e/naming_acceptance.rs` fails once crozier's old
order is written back into it.

## Reordered statements beside another difference

Where the two blocks do not sort to the same text, the rule takes the window of
statements that moves as one departure at crozier's first line of it, only when
every statement in the window is identical on both sides; every other line
stays a difference, so the file still fails.
`init_import_order_admits_reordered_statements_beside_another_difference` in
`src/parity.rs` holds both halves over a subpackage's block, and that a moved
statement importing another name is no departure.
`init_import_order_is_one_departure_at_crozier_s_first_moved_line` holds that
the same reordering in the root package's block is a difference.
