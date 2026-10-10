# Header defaults overridden by an operation: refuse

The [fresh probe](probe.yml) is valid OpenAPI 3.0.3: the
[validation log](evidence/spec-validation.log) records validation with
openapi-spec-validator 0.7.2. The
[Operation Object parameter rule](https://spec.openapis.org/oas/v3.0.3.html#operation-object)
permits an operation parameter to override the path parameter with the same
name and location. GET inherits `X-Projection` default `radial`; PUT overrides
it with `linear`. Both values match their string schemas. Fern checking the
inherited example against the overridden default is a Fern limitation, rather
than a specification fault. Its [certified log](evidence/pinned-fern.log)
records the example-check refusal with exit 1 and no SDK output.

The SDK evaluation used the compiled baseline at
`5f2240263` with the same probe, package `fern`, project `default_package_name`,
packaged layout, default settings. It imports and makes both public method
calls successfully, returning their declared string-list responses. With the
SDK's declared dependencies including its optional HTTP backend and pinned
mypy 1.13.0 installed, [type checking](evidence/baseline-mypy.log) reports zero
errors across 30 source files.

The [wire assertion](evidence/declared-default-wire.py), driven through the
real generated methods and an HTTP transport, [fails on the baseline](evidence/baseline-wire.log):
it records GET `radial` and PUT `radial`, whereas the specification declares
PUT `linear`. Thus the valid-specification finding holds, but the generated-SDK
wire finding does not. The conjunction required for default generation fails;
this class is `refuse` in both default and fern-strict modes. The finished
binary rejects before writing output. An equal-default control still generates
in both modes in `parameter_header_refusals_keep_adjacent_controls_generating`.

Fern measurement settings: CLI 5.67.1, Python SDK 5.20.0, packaged layout,
organization `fern`, client `FernApi`, `python_enums`, extra fields `allow`,
default retries 2, no audience filter. No real-document population is known.
