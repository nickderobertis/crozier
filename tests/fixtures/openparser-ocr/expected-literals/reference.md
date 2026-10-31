# Reference
## models
<details><summary><code>client.models.<a href="src/fern/models/client.py">list_ocr_models</a>() -> OcrModelsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the hosted OCR model registry with current capabilities, option defaults,
retail page prices, and availability. Clients should discover this endpoint instead of
hard-coding model IDs or provider-specific options.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.models.list_ocr_models()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/fern/models/client.py">list_llm_models</a>(...) -> OcrLlmModelsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a cached, normalized OpenRouter catalog filtered to models that advertise
strict structured output (`structured_outputs` + `response_format`), have valid finite
provider-list cost (internally) that is converted to customer retail rates, produce text, and are not expired.

Default `mode=suggested` returns a short recommended subset. `mode=search` discovers the
full compatible catalog with optional `q` / pagination. Field grounding and schema
suggestion remain restricted to certified models.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.models.list_llm_models()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mode:** `typing.Optional[ListLlmModelsRequestMode]` 

`suggested` (default): short recommended subset.
`search`: full compatible catalog filtered by `q`.
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Case-insensitive substring match against id, label, or provider. Used with `mode=search`.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — 1-based page index when paginating search results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size for search; ignored for suggested mode (bounded server-side).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## parse
<details><summary><code>client.parse.<a href="src/fern/parse/client.py">sync</a>(...) -> ParseResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Admit a parse job, wait up to the sync wait limit, and return the selected terminal parse
representation when ready. `output_format` defaults to the versioned provider-neutral
`openparser@1`; `raw` returns a stable provider envelope around the selected provider's
untouched successful result. Terminal `failed` within the wait window returns `422`
`ErrorResponse`; terminal `indeterminate` returns `504` `ErrorResponse`. Returns `202`
with a durable job reference and `Location` if the wait limit expires first.

Example (`multipart/form-data`):

```bash
curl -X POST 'https://api.openparser.dev/parse' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -H "Idempotency-Key: $(uuidgen 2>/dev/null || openssl rand -hex 16)" \
  -F 'request={"ocr_model":"paddleocr-vl-1.6","output_format":"openparser@1"};type=application/json' \
  -F 'file=@./document.pdf'
```
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ParseRequest
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.parse.sync(
    idempotency_key="7f9f2f3d-0f8a-4f0a-9a2b-2f6f0a7d2c11",
    file="example_file",
    request=ParseRequest(
        ocr_model="ocr_model",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
request body for a given tenant and operation.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ParseRequest` 
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` 

Source document bytes (PDF, PNG, or JPEG). Required unless `request.file_id`
references an existing Eigenpal reusable file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.parse.<a href="src/fern/parse/client.py">async</a>(...) -> JobAccepted</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Admit a durable parse job and return immediately.

Example (`multipart/form-data`):

```bash
curl -X POST 'https://api.openparser.dev/parse/async' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -H "Idempotency-Key: $(uuidgen 2>/dev/null || openssl rand -hex 16)" \
  -F 'request={"ocr_model":"paddleocr-vl-1.6","output_format":"openparser@1"};type=application/json' \
  -F 'file=@./document.pdf'
```
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ParseRequest
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.parse.async_(
    idempotency_key="7f9f2f3d-0f8a-4f0a-9a2b-2f6f0a7d2c11",
    file="example_file",
    request=ParseRequest(
        ocr_model="ocr_model",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
request body for a given tenant and operation.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ParseRequest` 
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` 

Source document bytes (PDF, PNG, or JPEG). Required unless `request.file_id`
references an existing Eigenpal reusable file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.parse.<a href="src/fern/parse/client.py">batch</a>(...) -> BatchJobAccepted</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Admit up to 100 parse child jobs in one durable batch. Every uploaded file must be mapped
exactly once by `file_index`. Partial child failures are preserved in batch results.
Parent status derivation for mixed outcomes is defined on `JobStatus`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ParseBatchRequest, ParseBatchRequestItemsItem
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.parse.batch(
    idempotency_key="7f9f2f3d-0f8a-4f0a-9a2b-2f6f0a7d2c11",
    files=["example_files"],
    request=ParseBatchRequest(
        items=[
            ParseBatchRequestItemsItem(
                client_item_id="client_item_id",
                ocr_model="ocr_model",
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
request body for a given tenant and operation.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ParseBatchRequest` 
    
</dd>
</dl>

<dl>
<dd>

**files:** `typing.Optional[typing.List[core.File]]` 

Ordered uploaded files referenced by `file_index` in the batch request. Each file
is limited to 50 MiB and total multipart body content is limited to 100 MiB.
Omit when every batch item supplies `file_id` instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## extract
<details><summary><code>client.extract.<a href="src/fern/extract/client.py">sync</a>(...) -> ExtractionTerminalResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Admit a single extract job from file bytes, `file_id`, or a tenant-owned succeeded
`parse_job_id`, then run schema-constrained OpenRouter extraction via `llm_model`. A
`parse_job_id` source reuses the canonical ParsedDocument (from dual artifacts or legacy
`result_json`) without OCR or another page charge; historical raw-only parses return
`422 canonical_result_unavailable`. Wait up to the sync wait limit and return
`ExtractionTerminalResult` when ready. Terminal `failed` within the wait window returns
`422`; terminal `indeterminate` returns `504`. Returns `202` with a durable job reference
and `Location` if the wait expires.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ExtractRequest
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.extract.sync(
    idempotency_key="7f9f2f3d-0f8a-4f0a-9a2b-2f6f0a7d2c11",
    file="example_file",
    request=ExtractRequest(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
request body for a given tenant and operation.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ExtractRequest` 
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` 

Source document bytes (PDF, PNG, or JPEG). Required unless `request.file_id`
references an existing Eigenpal reusable file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.extract.<a href="src/fern/extract/client.py">async</a>(...) -> JobAccepted</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Admit a durable single extract job from file bytes, `file_id`, or `parse_job_id` and
return immediately. Parse reuse does not run OCR or add a page charge; OpenRouter usage
remains billable.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ExtractRequest
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.extract.async_(
    idempotency_key="7f9f2f3d-0f8a-4f0a-9a2b-2f6f0a7d2c11",
    file="example_file",
    request=ExtractRequest(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
request body for a given tenant and operation.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ExtractRequest` 
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` 

Source document bytes (PDF, PNG, or JPEG). Required unless `request.file_id`
references an existing Eigenpal reusable file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.extract.<a href="src/fern/extract/client.py">batch</a>(...) -> BatchJobAccepted</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Admit up to 100 file-backed extract child jobs in one durable batch. Every item uses
`file_index` or `file_id`; `parse_job_id` reuse is single-extract-only and is not accepted
in batch. Partial child failures are preserved. Parent status derivation follows
`JobStatus`; billing is evaluated per child.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ExtractBatchRequest, ExtractBatchRequestItemsItem
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.extract.batch(
    idempotency_key="7f9f2f3d-0f8a-4f0a-9a2b-2f6f0a7d2c11",
    files=["example_files"],
    request=ExtractBatchRequest(
        items=[
            ExtractBatchRequestItemsItem(
                client_item_id="client_item_id",
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
request body for a given tenant and operation.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ExtractBatchRequest` 
    
</dd>
</dl>

<dl>
<dd>

**files:** `typing.Optional[typing.List[core.File]]` 

Ordered uploaded files referenced by `file_index` in the batch request. Each file
is limited to 50 MiB and total multipart body content is limited to 100 MiB.
Omit when every batch item supplies `file_id` instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.extract.<a href="src/fern/extract/client.py">suggest_schema</a>(...) -> SuggestSchemaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Suggest an extraction JSON Schema from a tenant-owned succeeded parse result.
Optional `hint` is capped at 500 characters. Definitive failures return
`schema_suggestion_failed`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.extract.suggest_schema(
    parse_job_id="parse_job_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**parse_job_id:** `str` — Prefixed id (`opj_…`) of a succeeded `parse` job in the same tenant.
    
</dd>
</dl>

<dl>
<dd>

**hint:** `typing.Optional[str]` — Optional free-text guidance for the suggestion model (max 500 characters).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## jobs
<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">list_jobs</a>(...) -> JobListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Tenant-scoped chronological list of top-level OCR jobs (batch children are omitted).
Returns lightweight summaries only — full results remain on `GET /jobs/{id}`.
Cursor pagination is stable newest-first with an `id` tie-break. Optional `status`
and `operation` filters are validated strictly; unknown values return `400`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.list_jobs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

Opaque pagination cursor from a prior `JobListResponse.next_cursor`. Jobs are
returned newest-first (`created_at` descending, `id` descending tie-break).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of job summaries to return.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[JobStatus]` 

Optional filter by public job status. Admission-phase (`admitting`) jobs are
never listed.
    
</dd>
</dl>

<dl>
<dd>

**operation:** `typing.Optional[JobOperation]` — Optional filter by job operation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">get_job</a>(...) -> Job</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Tenant-scoped durable job read. Jobs belonging to another tenant return `404`. Batch jobs
include cursor-paginated child summaries. Playground tokens (`ocr:playground`) and `ocr:full`
keys are both accepted. Successful parse jobs return the originally requested `output_format`
in `result`; use `GET /jobs/{id}/result?format=` to select an alternate stored representation
without re-running OCR.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.get_job(
    id="opj_V1StGXR8_Z5jdHi6B-myT",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `JobId` — Durable OCR job identifier (`opj_…`).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque pagination cursor for batch child summaries.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of batch child summaries to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">get_extraction_review</a>(...) -> ExtractionReview</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the immutable machine output beside the current corrected output and append-only
review events. A succeeded extraction with no confirmations returns a synthesized pending review
at version 0. Cross-tenant and unknown jobs return `404`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.get_extraction_review(
    id="opj_V1StGXR8_Z5jdHi6B-myT",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `JobId` — Durable OCR job identifier (`opj_…`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">update_extraction_review</a>(...) -> ExtractionReview</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Confirm that a field should say a given value, signed by the caller, without mutating the
machine result. `expected_version` provides optimistic concurrency; stale writes return `409`.
Every confirmation and retraction appends an actor- and timestamp-attributed event.

A confirmation whose value matches what extraction produced is a plain sign-off; one that
differs also corrects the field. There is no separate approval: who stands behind a value is
derived from live confirmations. Retractions are applied first, then confirmations.

A retraction peels the caller's own current tip on that path and restores the value the
confirmation replaced. Two retractions of the same path undo two confirmations, in order. A
retraction cannot be combined with a confirmation on the same or overlapping path. The tip is
not retractable when someone else made it, or when a later overlapping confirmation named a
different value. A co-signature of the same value becomes the tip, so only that co-signer can
take it back. Completing the review still freezes everything. Provide at least one
confirmation or retraction.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.update_extraction_review(
    id="opj_V1StGXR8_Z5jdHi6B-myT",
    expected_version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `JobId` — Durable OCR job identifier (`opj_…`).
    
</dd>
</dl>

<dl>
<dd>

**expected_version:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**confirmations:** `typing.Optional[typing.List[UpdateExtractionReviewRequestConfirmationsItem]]` — Fields the caller is signing. A value that matches the standing field is a sign-off; a different value also corrects it.
    
</dd>
</dl>

<dl>
<dd>

**retractions:** `typing.Optional[typing.List[UpdateExtractionReviewRequestRetractionsItem]]` — JSON Pointers whose current tip the caller is taking back. Each entry peels one confirmation. The restored value is the one recorded on that confirmation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">complete_extraction_review</a>(...) -> ExtractionReview</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Finalize a pending review as approved or rejected. A completed review is frozen: field
confirmations are rejected until it is reopened. Uses the same optimistic version check as
field confirmations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.complete_extraction_review(
    id="opj_V1StGXR8_Z5jdHi6B-myT",
    expected_version=1,
    status="approved",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `JobId` — Durable OCR job identifier (`opj_…`).
    
</dd>
</dl>

<dl>
<dd>

**expected_version:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `CompleteExtractionReviewRequestStatus` 
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">reopen_extraction_review</a>(...) -> ExtractionReview</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Take a sign-off back so the run returns to `pending` and its fields can be reviewed again.
Only the reviewer who completed the run may reopen it. Both events stay in the log, so the
trail shows the run was signed off and then reopened, while the review status and the
lineage decision follow the live completion. Uses the same optimistic version check as
field confirmations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.reopen_extraction_review(
    id="opj_V1StGXR8_Z5jdHi6B-myT",
    expected_version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `JobId` — Durable OCR job identifier (`opj_…`).
    
</dd>
</dl>

<dl>
<dd>

**expected_version:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">get_job_result</a>(...) -> ParseResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the selected parse wire body for a tenant-owned succeeded parse job.
`format` defaults to the job's original `output_format`. Fresh dual-artifact parses
can serve either `openparser@1` or `raw` from object storage without re-running HPS
or charging pages. Historical jobs only serve the representation already present in
`result_json`; unavailable alternates return `422 result_format_unavailable` with
guidance. Non-terminal jobs return `409 job_not_terminal`. Playground tokens
(`ocr:playground`) and `ocr:full` keys are both accepted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.get_job_result(
    id="opj_V1StGXR8_Z5jdHi6B-myT",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `JobId` — Durable OCR job identifier (`opj_…`).
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[OcrOutputFormat]` 

Parse representation to return. Defaults to the job's original `output_format`
when omitted. Fresh parses store both representations as immutable object-store
artifacts; historical jobs only expose the representation already present in
`result_json`. Requesting an unavailable alternate returns `422` and never
re-runs OCR.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">get_job_source</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stream the retained source document for a parse or single-document extract job. Jobs without
retained source bytes return `404 source_not_available`. Check `has_source` on `GET /jobs/{id}`
before calling. Playground tokens (`ocr:playground`) and `ocr:full` keys are both accepted,
matching other job read routes. Optional `Range` requests may return `206` partial content or
`416` when the range is unsatisfiable.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.get_job_source(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `JobId` — Durable OCR job identifier (`opj_…`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## files
<details><summary><code>client.files.<a href="src/fern/files/client.py">create_file</a>(...) -> PublicFile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload bytes directly to OpenParser's Eigenpal-compatible tenant file pool. Files may be
reused by later parse or extract requests through `file_id`; bytes do not pass through
Vercel.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.create_file(
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/fern/files/client.py">get_file</a>(...) -> PublicFile</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.get_file(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Tenant-scoped reusable file identifier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/fern/files/client.py">delete_file</a>(...) -> DeleteFileResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.delete_file(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Tenant-scoped reusable file identifier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/fern/files/client.py">get_file_content</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.get_file_content(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Tenant-scoped reusable file identifier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## pipelines
<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">list_extraction_pipelines</a>() -> ExtractionPipelineListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return active (non-deleted) pipelines for the authenticated tenant, newest updates first.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pipelines.list_extraction_pipelines()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">create_extraction_pipeline</a>(...) -> ExtractionPipeline</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Persist a tenant-scoped extraction configuration (OCR model, LLM model, schema,
repair/grounding/reasoning). Validated with the same admission gates as extract.
Playground tokens and `ocr:full` keys are both accepted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pipelines.create_extraction_pipeline(
    name="name",
    ocr_model="ocr_model",
    llm_model="llm_model",
    schema={
        "key": "value"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**ocr_model:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**llm_model:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**schema:** `typing.Dict[str, typing.Any]` 

JSON Schema object describing fields to extract. Root must be an object schema with
explicit `properties` and at least one named property. Admission applies the same
strict structured-output normalization as extract.
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ocr_options:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**llm_options:** `typing.Optional[CreateExtractionPipelineRequestLlmOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**repair_attempts:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**grounding:** `typing.Optional[CreateExtractionPipelineRequestGrounding]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">get_extraction_pipeline</a>(...) -> ExtractionPipeline</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return one active pipeline. Missing, deleted, and cross-tenant ids return
`404 pipeline_not_found`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pipelines.get_extraction_pipeline(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `ExtractionPipelineId` — Tenant-scoped saved extraction pipeline identifier (`oppl_…`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">delete_extraction_pipeline</a>(...) -> DeleteExtractionPipelineResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Marks the pipeline deleted. Subsequent extract admits with that id return
`404 pipeline_not_found`. Historical jobs retain snapshotted config.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pipelines.delete_extraction_pipeline(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `ExtractionPipelineId` — Tenant-scoped saved extraction pipeline identifier (`oppl_…`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">update_extraction_pipeline</a>(...) -> ExtractionPipeline</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patch one or more fields, re-validate the effective merged config, and atomically
increment `version`. In-flight and completed jobs keep their admit-time snapshots.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pipelines.update_extraction_pipeline(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `ExtractionPipelineId` — Tenant-scoped saved extraction pipeline identifier (`oppl_…`).
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ocr_model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ocr_options:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**llm_model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**llm_options:** `typing.Optional[UpdateExtractionPipelineRequestLlmOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**schema:** `typing.Optional[typing.Dict[str, typing.Any]]` 

Replacement extraction schema. Root must be an object schema with explicit `properties`
and at least one named property. Merged pipeline config is re-validated on every update.
    
</dd>
</dl>

<dl>
<dd>

**repair_attempts:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**grounding:** `typing.Optional[UpdateExtractionPipelineRequestGrounding]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

