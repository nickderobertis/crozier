//! The registered real specifications that prove parity shapes with no
//! hand-written fixture of their own.
//!
//! Each witness's golden is byte-compared whole by its corpus test; this holds
//! the claim that the golden is a proof of the shape: the committed source
//! still declares the shape's whole trigger, and the golden still carries the
//! output the shape is about. The witnesses and the search that found them are
//! `docs/openapi-surface/witness-search-prove-matches/README.md`'s.

use super::{corpus_spec, fixture_dir};

/// One witness: the shape, the registered corpus, what its source declares and
/// what its golden says.
struct Witness {
    shape: &'static str,
    corpus: &'static str,
    /// The source's trigger, read off the parsed document; `Err` names what is
    /// missing.
    declares: fn(&serde_json::Value) -> Result<(), String>,
    /// `(golden-relative file, text it must contain, text it must not)`.
    golden: &'static [(
        &'static str,
        &'static [&'static str],
        &'static [&'static str],
    )],
}

fn at<'a>(value: &'a serde_json::Value, pointer: &str) -> Result<&'a serde_json::Value, String> {
    value
        .pointer(pointer)
        .ok_or_else(|| format!("declares nothing at {pointer}"))
}

fn expect(holds: bool, what: &str) -> Result<(), String> {
    if holds {
        Ok(())
    } else {
        Err(what.to_string())
    }
}

fn not_required(schema: &serde_json::Value, name: &str) -> bool {
    !schema["required"]
        .as_array()
        .is_some_and(|required| required.iter().any(|entry| entry == name))
}

const WITNESSES: &[Witness] = &[
    Witness {
        shape: "dotted-mapping-key-variant-class-name",
        corpus: "truefoundry-trueforge",
        declares: |doc| {
            let union = at(doc, "/components/schemas/ActionRequiredEvent")?;
            expect(union["oneOf"].is_array(), "ActionRequiredEvent is a oneOf")?;
            expect(
                union["discriminator"]["mapping"]["mcp.auth_required"]
                    == "#/components/schemas/MCPAuthRequiredEvent",
                "the dotted mapping key mcp.auth_required names MCPAuthRequiredEvent",
            )
        },
        golden: &[(
            "src/fern/types/action_required_event.py",
            &[
                "class ActionRequiredEvent_McpAuthRequired(UniversalBaseModel):",
                "type: typing.Literal[\"mcp.auth_required\"] = \"mcp.auth_required\"",
            ],
            &["ActionRequiredEvent_McpAuthRequiredEvent"],
        )],
    },
    Witness {
        shape: "literal-enum-description-omitted",
        corpus: "groupe-psa",
        declares: |doc| {
            let schema = at(doc, "/components/schemas/ChargingStatusEnum")?;
            expect(
                schema["type"] == "string"
                    && schema["enum"].is_array()
                    && schema["description"] == "status of charging system.",
                "ChargingStatusEnum is a described string enum",
            )
        },
        golden: &[(
            "expected-literals/src/fern/types/charging_status_enum.py",
            &["ChargingStatusEnum = typing.Union[\n    typing.Literal[\"Disconnected\", \"InProgress\", \"Failure\", \"Stopped\", \"Finished\"], typing.Any\n]"],
            &["status of charging system."],
        ), (
            "expected/src/fern/types/charging_status_enum.py",
            &["class ChargingStatusEnum(enum.StrEnum):\n    \"\"\"\n    status of charging system.\n    \"\"\""],
            &[],
        )],
    },
    Witness {
        shape: "open-object-body-example-extra-keys-dropped",
        corpus: "mockserver",
        declares: |doc| {
            let media = at(
                doc,
                "/paths/~1mockserver~1oidc/put/requestBody/content/application~1json",
            )?;
            let properties = media["schema"]["properties"]
                .as_object()
                .ok_or("the body declares no properties")?;
            expect(
                media["schema"]["additionalProperties"] == true,
                "the body is open (additionalProperties: true)",
            )?;
            expect(
                media["example"]["subject"].is_string() && !properties.contains_key("subject"),
                "the example's `subject` is outside the body's properties",
            )
        },
        golden: &[(
            "src/fern/oidc/client.py",
            &["client.oidc.mock_oidc_provider(\n            issuer=\"http://localhost:1080\",\n            client_id=\"my-app\",\n            scopes=[\"openid\", \"profile\", \"email\"],\n            token_expiry_seconds=7200,\n        )"],
            &["subject=", "audience="],
        )],
    },
    Witness {
        shape: "required-and-nullable-property-defaults-none",
        corpus: "apideck.com-crm",
        declares: |doc| {
            expect(
                doc["openapi"].as_str().is_some_and(|v| v.starts_with("3.0")),
                "the document is OpenAPI 3.0",
            )?;
            let lead = at(doc, "/components/schemas/Lead")?;
            expect(
                !not_required(lead, "company_name")
                    && lead["properties"]["company_name"]["nullable"] == true,
                "Lead.company_name is required and nullable: true",
            )
        },
        golden: &[(
            "src/fern/types/lead.py",
            &["    company_name: typing.Optional[str] = None\n"],
            &[],
        )],
    },
    Witness {
        shape: "snake-case-component-name-pascal-class",
        corpus: "paloalto-remote-networks",
        declares: |doc| {
            expect(
                at(doc, "/components/schemas/generic_error")?["type"] == "object",
                "generic_error is an object component",
            )
        },
        golden: &[(
            "src/fern/types/generic_error.py",
            &["class GenericError(UniversalBaseModel):"],
            &[],
        )],
    },
    Witness {
        shape: "variant-optional-const-discriminant-merged",
        corpus: "letta",
        declares: |doc| {
            let union = at(doc, "/components/schemas/LettaStreamingResponse")?;
            expect(
                union["discriminator"]["propertyName"] == "message_type",
                "LettaStreamingResponse is discriminated on message_type",
            )?;
            let variant = at(doc, "/components/schemas/SystemMessage")?;
            expect(
                variant["properties"]["message_type"]["const"] == "system_message"
                    && not_required(variant, "message_type"),
                "SystemMessage declares message_type as an optional const",
            )
        },
        golden: &[(
            "src/fern/types/letta_streaming_response.py",
            &["class LettaStreamingResponse_SystemMessage(UniversalBaseModel):\n    \"\"\"\n    Streaming response type for Server-Sent Events (SSE) endpoints.\n    Each event in the stream will be one of these types.\n    \"\"\"\n\n    message_type: typing.Literal[\"system_message\"] = \"system_message\"\n    id: str\n"],
            &[],
        )],
    },
];

fn parse(path: &std::path::Path) -> serde_json::Value {
    let text =
        std::fs::read_to_string(path).unwrap_or_else(|error| panic!("{}: {error}", path.display()));
    if path.extension().is_some_and(|ext| ext == "json") {
        serde_json::from_str(&text).unwrap_or_else(|error| panic!("{}: {error}", path.display()))
    } else {
        serde_yaml_ng::from_str(&text).unwrap_or_else(|error| panic!("{}: {error}", path.display()))
    }
}

/// What keeps `witness` from proving its shape, read off its committed source
/// and golden.
fn witness_failures(witness: &Witness) -> Vec<String> {
    let name = format!("{} ({})", witness.shape, witness.corpus);
    let Some(spec) = corpus_spec(witness.corpus) else {
        return vec![format!("{name}: no committed source")];
    };
    let mut failures = Vec::new();
    if let Err(missing) = (witness.declares)(&parse(&spec)) {
        failures.push(format!(
            "{name}: its source no longer declares the shape: {missing}"
        ));
    }
    for (file, present, absent) in witness.golden {
        let path = if file.starts_with("expected") {
            fixture_dir(witness.corpus).join(file)
        } else {
            fixture_dir(witness.corpus).join("expected").join(file)
        };
        let Ok(text) = std::fs::read_to_string(&path) else {
            failures.push(format!("{name}: its golden has no {file}"));
            continue;
        };
        for needle in *present {
            if !text.contains(needle) {
                failures.push(format!("{name}: {file} no longer carries {needle:?}"));
            }
        }
        for needle in *absent {
            if text.contains(needle) {
                failures.push(format!("{name}: {file} now carries {needle:?}"));
            }
        }
    }
    failures
}

/// Every registered witness still declares its shape's whole trigger, and its
/// golden — which its corpus test compares byte for byte — still carries the
/// output the shape is about.
#[test]
fn prove_matches_real_witnesses_declare_their_shapes() {
    let failures: Vec<String> = WITNESSES.iter().flat_map(witness_failures).collect();
    assert!(failures.is_empty(), "{}", failures.join("\n"));
}

/// The check is not vacuous: a source that stops declaring the trigger, or a
/// golden that stops carrying the output, is reported.
#[test]
fn a_witness_that_stops_declaring_its_shape_fails() {
    let source = Witness {
        declares: |_| Err("the trigger".into()),
        ..WITNESSES[0]
    };
    assert!(witness_failures(&source)
        .iter()
        .any(|failure| failure.contains("no longer declares the shape")),);
    let golden = Witness {
        golden: &[(
            "src/fern/types/action_required_event.py",
            &["class ActionRequiredEvent_NoSuchVariant("],
            &["class ActionRequiredEvent_McpAuthRequired("],
        )],
        ..WITNESSES[0]
    };
    let failures = witness_failures(&golden);
    assert_eq!(2, failures.len(), "{failures:?}");
}
