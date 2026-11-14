# Reference anchors in a corrected client

**Kind:** `fern-defect`. Measured at Fern CLI 5.200.0 / fern-python-sdk 5.41.25.

At this pair each `reference.md` heading links the method it documents by line
range: `src/fern/client.py#L116-L154` is the method's `def` line through its
last line. Fern counts those lines in its own client. Where crozier corrects
that client under another departure, the lines move. The handwritten
`twin-key-relay` golden is one case: its credential keyword is repeated in the
client constructor's docstring example (`repeated-credential-example-keyword`),
so Fern's `relay_message` runs from line 116 to 154 of its client, and from line
115 to 152 of crozier's.

```text
$ crozier generate --spec docs/openapi-surface/handwritten/twin-key-relay/openapi.yml \
    --output /tmp/tkr --package-name fern --project-name default_package_name
$ diff docs/openapi-surface/handwritten/twin-key-relay/fern-expected/reference.md /tmp/tkr/reference.md
2c2
< <details><summary><code>client.<a href="src/fern/client.py#L116-L154">relay_message</a>(...)</code></summary>
---
> <details><summary><code>client.<a href="src/fern/client.py#L115-L152">relay_message</a>(...)</code></summary>
20d19
<     api_key="<X-Api-Key>",
```

In crozier's client, Fern's range starts on line 116, the `*,` inside the
method's signature, and ends on line 154, two lines past the method's last
line (152, its `return`), so it does not link the method the heading
documents.

The rule admits a `reference.md` heading only where the two lines are equal
but for the range, Fern's range is exactly the documented method's lines in
Fern's linked client, and crozier's is exactly that method's lines in
crozier's. A changed range on either side, any other change on the line, or a
missing range is no departure; the unit test checks each. The line differences
in the client itself are each accounted for by their own departure, and the
departures ledger pins every occurrence of this one.

At Fern CLI 5.200.0 / fern-python-sdk 5.41.25 the departures ledger pins 1040
occurrences, each a heading whose client carries another departure above or
inside the documented method.
