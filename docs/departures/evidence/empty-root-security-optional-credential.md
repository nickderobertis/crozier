# `empty-root-security-optional-credential`

**Kind:** `usefulness`. crozier reads an empty root `security` list the way
OpenAPI defines it, so the operations it leaves unauthenticated can be called
without a credential.

## The shape

RS-Server (corpus row 3477) declares root `security: []`, one `apiKey` header
scheme (`x-api-key`), 68 operations with `security: [{API key
authentication: []}]` and 10 with no `security` of their own (`GET /auth/me`,
`GET /catalog/_mgmt/ping`, `GET /catalog/_mgmt/health` and seven `/dpr/*`
operations). Under OpenAPI an empty root list and an absent one mean the same:
those 10 operations need no credential.

The certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) makes
the credential optional when the root `security` is absent and some operation
declares none: every such registered corpus golden (`get-a-room`, `khoainats`,
`worldcoin-signup-sequencer`, `swagger-petstore` and 27 more) has
`typing.Optional[...] = None`. On RS-Server, the only corpus document whose
root `security` is `[]`, the pair writes `api_key: str` and sets the header
unconditionally. crozier writes the optional credential for both spellings. The
planner ruled that crozier keeps it.

## The command and its result

Over the committed `rs-server` corpus document, with the corpus's settings,
against its golden as the certified pair generates it:

```text
$ crozier generate --no-config --spec tests/fixtures/corpus-sources/rs-server/openapi.json --output /tmp/rs --package-name fern --project-name default_package_name
$ diff tests/fixtures/rs-server/expected/src/fern/client.py /tmp/rs/src/fern/client.py
48c48
<     api_key : str
---
>     api_key : typing.Optional[str]
87c87
<         api_key: str,
---
>         api_key: typing.Optional[str] = None,
289c289
<     api_key : str
---
>     api_key : typing.Optional[str]
328c328
<         api_key: str,
---
>         api_key: typing.Optional[str] = None,
$ diff tests/fixtures/rs-server/expected/src/fern/core/client_wrapper.py /tmp/rs/src/fern/core/client_wrapper.py
14c14
<         api_key: str,
---
>         api_key: typing.Optional[str] = None,
43c43,44
<         headers["x-api-key"] = self.api_key
---
>         if self.api_key is not None:
>             headers["x-api-key"] = self.api_key
69c70
<         api_key: str,
---
>         api_key: typing.Optional[str] = None,
103c104
<         api_key: str,
---
>         api_key: typing.Optional[str] = None,
```

The first line of each file (a comment) and `client_wrapper.py`'s
`X-Crozier-*` header lines are other entries' business. Every other difference
is this departure. The rule reads the parsed source document
(`crate::ir::empty_root_security_credentials`). It applies only where root
`security` is `[]`, some operation declares no `security` of its own, and no
operation declares an empty one. An operation's own `security: []` already
makes the pair's credential optional, as `audiobookshelf` shows.

## Behaviour

`sdk_env_empty_root_security_client_calls_unsecured_operations_without_a_key`
in `crates/crozier-e2e/tests/e2e.rs` generates the SDK from RS-Server's document and
drives it against a local HTTP server. A client built with no key calls
`GET /catalog/_mgmt/ping` and sends no `x-api-key` header. A client built with
a key sends it on a secured operation.
