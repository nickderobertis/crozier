# Digit-leading method documentation

**Kind:** `fern-defect`. The publisher-authored OnMyShelf API specification at
`onmyshelf/api`, revision `e56b713d272d627a18ba14d3eea992231c550146`, declares
operation IDs beginning with digits. Its complete certified-pair golden is
registered as corpus row 3000, `onmyshelf-api`.

Fern CLI 5.163.1 and Python SDK 5.41.3 generate valid underscore-prefixed SDK
methods. Its README instead calls
`client.borrowers.1fd12f73a7dc29d90f19d587c1c24d15(...)`, and reference headings
omit the prefix too. Python compilation of each of the four affected README
blocks fails with `SyntaxError: invalid decimal literal`. In the actual installed
certified SDK, importing `FernApi` succeeds, and
`inspect.signature(client.borrowers._1fd12f73a7dc29d90f19d587c1c24d15).bind(firstname="Lina")`
succeeds. The method exists; the documented spelling is invalid.

The measurement used the freshly generated complete tree, installed in an
isolated environment. Its runtime output was:

```text
Certified SDK imports; documented operation binds as: _1fd12f73a7dc29d90f19d587c1c24d15 {'firstname': 'Lina'}
SyntaxError invalid decimal literal (certified README block 3, line 4)
SyntaxError invalid decimal literal (certified README block 4, line 4)
SyntaxError invalid decimal literal (certified README block 5, line 1)
SyntaxError invalid decimal literal (certified README block 6, line 6)
Measured invalid documented call blocks: 4
```

The rule admits only aligned README/reference lines whose sole change restores
the underscore for a digit-leading operation ID declared by the source document.
The corresponding identifier must exist as a method in the generated SDK, and
an SDK method override disables this operation-ID rule. No code file is
normalized, and any other change on the line still fails. Unit tests require the
declared source and generated method and reject changed arguments; the corpus
comparison and its adjacent unexplained-byte regression drive complete trees.
