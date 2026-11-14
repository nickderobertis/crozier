# Flat-layout reference links

**Kind:** `fern-defect`. Measured at Fern CLI 5.200.0 / fern-python-sdk 5.41.25
(manager ruling c14.0).

Fern's flat tree (a `local-file-system` output) puts the package's modules at
the output root, with no `src/`. Its `reference.md` still links the packaged
path. The `swagger-petstore` flat golden writes

```text
<details><summary><code>client.pet.<a href="src/fern/pet/client.py">add_pet</a>(...) -> Pet</code></summary>
```

and its tree holds `pet/client.py`, not `src/fern/pet/client.py`:

```text
$ ls tests/fixtures/swagger-petstore/expected-flat/
CONTRIBUTING.md README.md __init__.py _default_clients.py client.py core environment.py errors pet reference.md store tests types user
$ test -e tests/fixtures/swagger-petstore/expected-flat/src/fern/pet/client.py || echo absent
absent
```

Because the file is absent, Fern's link also carries no `#L<start>-L<end>`
range, which every packaged heading has at this pair. Across the eight committed
flat goldens there are 119 heading links, and none names a file its tree holds:
`truefoundry-trueforge` 55, `swagger-petstore`, `swagger-petstore-distribution`
and `swagger-petstore-organization` 19 each, `eos.local-extra-fields-forbid` 4,
`client-class-name` 2, `audience-filter-strict` 1, and
`googleapis-youtubeanalytics-v1` none (it documents no method).

The departures ledger pins 122 occurrences: 117 in those goldens, 4 in the
flat measurement trees under `docs/fern-measurements/clients-extensions/`, and
1 in `readme-client-class-casing`'s flat reference tree. The other 2 of
`truefoundry-trueforge`'s headings are streaming methods, pinned as
`stream-reference-return-type`, which judges the flat link the same way.

crozier links the module its flat tree holds and anchors it at the method:
`client.pet.<a href="pet/client.py#L34-L93">add_pet</a>(...)`, lines 34 to 93 of
`pet/client.py` being `add_pet`'s `def` through its `return`.

The rule admits a `reference.md` heading only where Fern's link is exactly
`src/<package>/` before crozier's module path, Fern's own tree lacks that file,
crozier's tree holds the module, crozier's range is exactly the documented
method's lines there, and every other byte of the line is Fern's. The
escaped-method-name and stream-return-type rules judge a flat heading on the
rest of its line the same way. Its unit test rejects a wrong or missing range,
another module or method, any other change, a README line, and a Fern tree
that does hold the linked file.
