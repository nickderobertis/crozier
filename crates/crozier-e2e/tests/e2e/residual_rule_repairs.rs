// llmlint: ignore-file[expensive_tests_stay_behind_their_own_edge] Each of these journeys generates one small SDK and reads it, on the crozier-e2e edge every other binary-driving journey shares; splitting that edge is the drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads".
//! Journeys for the generator rules the residual-differences repair corrected:
//! each drives the real binary over a small document and reads the file a user
//! would, beside a control showing the adjacent shape is unchanged.

use super::generate_ok;

fn read(out: &std::path::Path, rel: &str) -> String {
    std::fs::read_to_string(out.join(rel)).unwrap_or_else(|error| panic!("{rel}: {error}"))
}

const HEADER: &str = "openapi: 3.0.3\ninfo: {title: Harbor, version: '1'}\n";

#[test]
fn an_array_alias_docstring_keeps_the_descriptions_trailing_space() {
    let spec = format!(
        "{HEADER}paths:\n  /berths:\n    get:\n      operationId: listBerths\n      tags: [berths]\n      responses:\n        '200':\n          description: ok\n          content:\n            application/json:\n              schema: {{$ref: '#/components/schemas/BerthIds'}}\ncomponents:\n  schemas:\n    BerthIds:\n      type: array\n      description: 'Identifiers of the berths. '\n      items: {{type: string}}\n"
    );
    let (_dir, out) = generate_ok(&spec);
    let alias = read(&out, "src/acme/types/berth_ids.py");
    assert!(alias.contains("Identifiers of the berths. \n"), "{alias}");
}

#[test]
fn a_nullable_object_member_extends_the_parent_while_a_type_array_flattens_it() {
    let parent = "    Vessel:\n      type: object\n      required: [name]\n      properties:\n        name: {type: string}\n";
    let endpoint = |schema: &str| {
        format!(
            "{HEADER}paths:\n  /vessels:\n    get:\n      operationId: getVessel\n      tags: [vessels]\n      responses:\n        '200':\n          description: ok\n          content:\n            application/json:\n              schema: {{$ref: '#/components/schemas/{schema}'}}\ncomponents:\n  schemas:\n{parent}"
        )
    };
    let extended = format!(
        "{}    VesselNullable:\n      type: object\n      allOf:\n        - $ref: '#/components/schemas/Vessel'\n        - nullable: true\n          type: object\n",
        endpoint("VesselNullable")
    );
    let (_dir, out) = generate_ok(&extended);
    let model = read(&out, "src/acme/types/vessel_nullable.py");
    assert!(model.contains("class VesselNullable(Vessel):"), "{model}");

    let flattened = format!(
        "{}    VesselNullable:\n      type: object\n      allOf:\n        - $ref: '#/components/schemas/Vessel'\n        - type: [object, 'null']\n",
        endpoint("VesselNullable")
    )
    .replace("openapi: 3.0.3", "openapi: 3.1.0");
    let (_dir, out) = generate_ok(&flattened);
    let model = read(&out, "src/acme/types/vessel_nullable.py");
    assert!(
        model.contains("class VesselNullable(UniversalBaseModel):"),
        "{model}"
    );
}

#[test]
fn a_referenced_one_of_branch_orders_the_fields_it_lends() {
    let spec = format!(
        r"{HEADER}paths:
  /jobs:
    post:
      operationId: createJob
      tags: [jobs]
      requestBody:
        required: true
        content:
          application/json:
            schema: {{$ref: '#/components/schemas/CloseJob'}}
      responses:
        '200': {{description: ok}}
  /jobs/archive:
    post:
      operationId: archiveJob
      tags: [jobs]
      requestBody:
        required: true
        content:
          application/json:
            schema: {{$ref: '#/components/schemas/CloseJob'}}
      responses:
        '200': {{description: ok}}
components:
  schemas:
    JobTarget:
      type: object
      properties:
        kind: {{type: string}}
        jobId: {{type: string}}
        crewId: {{type: string}}
        ownerId: {{type: string}}
        note: {{type: string}}
    ByJob:
      type: object
      required: [jobId]
      properties:
        jobId: {{type: string}}
        ownerId: {{type: string}}
    ByCrew:
      type: object
      required: [crewId]
      properties:
        jobId: {{type: string}}
        crewId: {{type: string}}
    CloseJob:
      allOf:
        - $ref: '#/components/schemas/JobTarget'
        - type: object
          required: [kind]
          properties:
            kind: {{type: string, enum: [close]}}
        - oneOf:
            - $ref: '#/components/schemas/ByJob'
            - $ref: '#/components/schemas/ByCrew'
"
    );
    let (_dir, out) = generate_ok(&spec);
    let model = read(&out, "src/acme/types/close_job.py");
    let at = |field: &str| {
        model
            .find(field)
            .unwrap_or_else(|| panic!("{field} in {model}"))
    };
    assert!(at("job_id") < at("owner_id"), "{model}");
    assert!(at("owner_id") < at("crew_id"), "{model}");
    assert!(at("crew_id") < at("note:"), "{model}");
}

#[test]
fn an_open_success_object_with_its_own_example_declines_the_request_example() {
    let spec = |additional: &str| {
        format!(
            r"{HEADER}paths:
  /tides:
    post:
      operationId: logTide
      tags: [tides]
      requestBody:
        required: true
        content:
          application/json:
            schema: {{$ref: '#/components/schemas/TideParams'}}
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema: {{$ref: '#/components/schemas/Tide'}}
components:
  schemas:
    Tide:
      type: object
      additionalProperties: {additional}
      required: [id]
      properties:
        id: {{type: string}}
      example: {{id: t-1}}
    TideParams:
      type: object
      required: [station]
      properties:
        station: {{type: string, example: Newport}}
        height: {{type: number, example: 3.2}}
      example: {{station: Newport, height: 3.2}}
"
        )
    };
    let (_dir, out) = generate_ok(&spec("true"));
    let reference = read(&out, "reference.md");
    assert!(reference.contains("station=\"station\","), "{reference}");
    assert!(!reference.contains("height="), "{reference}");

    let (_dir, out) = generate_ok(&spec("false"));
    let reference = read(&out, "reference.md");
    assert!(reference.contains("station=\"Newport\","), "{reference}");
}

#[test]
fn a_union_property_is_worked_from_its_first_members_example_and_a_lone_enum_loses_its_docs() {
    let spec = format!(
        r#"{HEADER}paths:
  /notes:
    post:
      operationId: postNote
      tags: [notes]
      requestBody:
        required: true
        content:
          application/json:
            schema: {{$ref: '#/components/schemas/NoteRequest'}}
      responses:
        '200': {{description: ok}}
components:
  schemas:
    NoteRequest:
      type: object
      required: [body, labels]
      properties:
        body:
          description: The note's text.
          oneOf:
            - {{type: string, example: Hello there}}
            - {{type: array, items: {{type: string}}}}
        labels:
          type: array
          items:
            type: object
            required: [kind]
            properties:
              kind:
                description: The kind of label.
                oneOf:
                  - {{type: string, enum: [plain]}}
"#
    );
    let (_dir, out) = generate_ok(&spec);
    let reference = read(&out, "reference.md");
    assert!(reference.contains("body=\"Hello there\","), "{reference}");
    let item = read(&out, "src/acme/notes/types/note_request_labels_item.py");
    assert!(!item.contains("The kind of label."), "{item}");
}

#[test]
fn an_error_union_naming_a_response_schema_leaves_the_declaration_to_the_earlier_body() {
    let spec = format!(
        r"{HEADER}paths:
  /a:
    get:
      operationId: getA
      tags: [items]
      responses:
        '200': {{description: ok}}
        '404': {{$ref: '#/components/responses/Missing'}}
  /b:
    get:
      operationId: getB
      tags: [items]
      responses:
        '200': {{description: ok}}
        '404':
          description: not here
          content:
            application/json:
              schema:
                oneOf:
                  - $ref: '#/components/responses/Missing/content/application~1json/schema'
                  - $ref: '#/components/schemas/Gone'
components:
  responses:
    Missing:
      description: gone
      content:
        application/json:
          schema:
            type: object
            required: [type]
            properties:
              type: {{type: string, example: 'https://errors/missing'}}
  schemas:
    Gone:
      type: object
      required: [type]
      properties:
        type: {{type: string, example: 'https://errors/gone'}}
"
    );
    let (_dir, out) = generate_ok(&spec);
    let body = read(&out, "src/acme/types/not_found_error_body.py");
    assert!(
        body.contains("class NotFoundErrorBody(UniversalBaseModel):"),
        "{body}"
    );
    assert!(body.contains("type: str"), "{body}");
    assert!(!out.join("src/acme/types/missing.py").exists());
    let gone = read(&out, "src/acme/types/gone.py");
    assert!(gone.contains("type: str"), "{gone}");
}

#[test]
fn an_optional_raw_body_with_code_samples_is_worked_and_without_them_is_not() {
    let spec = |samples: &str| {
        format!(
            r"{HEADER}paths:
  /upload:
    post:
      operationId: upload
      tags: [files]
      x-fern-sdk-group-name: files
      x-fern-sdk-method-name: upload
{samples}      requestBody:
        content:
          application/octet-stream:
            schema: {{type: string, format: binary}}
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema: {{type: object, properties: {{url: {{type: string}}}}}}
"
        )
    };
    let (_dir, out) = generate_ok(&spec(
        "      x-codeSamples:\n        - {lang: python, source: pass}\n",
    ));
    let reference = read(&out, "reference.md");
    assert!(reference.contains("request=b\"string\","), "{reference}");
    let client = read(&out, "src/acme/files/client.py");
    assert!(client.contains("request=b\"string\","), "{client}");

    let (_dir, out) = generate_ok(&spec(""));
    let reference = read(&out, "reference.md");
    assert!(!reference.contains("request=b\"string\","), "{reference}");
}
