# service-auth-undefined: refuse

Measured against starting commit `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`,
before adding any detector. No generator repair was made.

The [probe measurement](evaluation-logs/service-auth-undefined.log) generates
36 files, imports its package and client, and reports **zero mypy errors**.
The interpreter is CPython 3.12.3, mypy is the SDK's declared 1.13.0, and its
own `pyproject.toml` supplies the configuration. Runtime, optional and dev
dependencies declared there are installed, including `httpx-aiohttp`.

The [wire measurement](evaluation-logs/service-auth-undefined-wire.log) drives
the generated client through `httpx.MockTransport`. The probe declares the
required cookie api key `session`, with wire name `SESSION`. The generated
constructor has no session credential, and `GET /probe` sends no Cookie header.
The declared 204 response parses as `None`. The omitted credential makes the
SDK insufficient even though it imports and type-checks. Supplying an arbitrary
Cookie header through the generic header escape hatch does not represent that
declared credential in the generated API.

Three retrievable population documents from different publishers confirm that
the class cannot remain `generate`:

| Publisher and digest | Import | mypy errors | Offending security declaration |
| --- | --- | --- | --- |
| [watchtrace/watchtrace-platform, `3e0c413424…`](evaluation-logs/service-auth-undefined-3e0c413424c67c2b58e385e6a6dbbffddcefbbf811b2e28003e7a0926f60d600.log) | succeeds | 32 | Required `mutualTLS` client certificate |
| [sn-ravance/Ollama_Docker, `5487bf4381…`](evaluation-logs/service-auth-undefined-5487bf4381fc761ccbf1d955abeb0e4133dd5af6ffc0b9d8b1268038eef0fc7a.log) | succeeds | 10 | Required `mtls` client certificate |
| [benboakye/secure-file-storage-system, `5978c16b64…`](evaluation-logs/service-auth-undefined-5978c16b642ab44cd27129784dba5900366fd6144ed04c6ce1aa963cdb3616ce.log) | succeeds | 22 | Required `mutualTLS` client certificate |

These logs record each immutable source URL and digest, generation, import and
the complete mypy diagnostics under each SDK's own configuration. Their wire
journeys were not run after type-checking failed: no claim about their TLS
handshake or response parsing is made. In particular a MockTransport cannot
establish whether a client certificate is sent. Their nonzero mypy counts are
already enough to require `refuse` under the evaluation rule.

The detector checks document-wide nonempty security on a service with actual
operations when no supported authentication scheme was imported. An unused
cookie scheme is allowed, as is a supported scheme declared after it. A tree
of unresolved Path Item references creates no service: the accepted OneVoice
golden is a witness for that distinction. The probe is refused in both modes,
before any file is rendered or written, and strict mode names `fern-strict`.

The [induced baseline failure](evaluation-logs/service-auth-red.log) runs the
real recovery e2e against the preserved starting binary. It fails because the
baseline writes 36 files instead of refusing. The finished detector's same
journey also removes the security requirement and proves both modes recover
with byte-identical SDKs.

Population strict-mode measurement is in progress; `population_strict` records
zero completed measurements out of the 26 registered documents until that run
is recorded.
