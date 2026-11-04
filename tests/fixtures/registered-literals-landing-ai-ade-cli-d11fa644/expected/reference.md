# Reference
## Parse
<details><summary><code>client.parse.<a href="src/fern/parse/client.py">run_sync</a>(...) -> ParseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Parse a document and return the parse response inline.
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

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.parse.run_sync(
    document="example_document",
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

**document:** `typing.Optional[core.File]` — The file to parse. The file must be a PDF or image; see the list of [supported file types](https://docs.landing.ai/dpt3/file-types). Provide either `document` or `document_url`, not both.
    
</dd>
</dl>

<dl>
<dd>

**document_url:** `typing.Optional[str]` — A publicly accessible URL to the file to parse. The file must be a PDF or image; see the list of [supported file types](https://docs.landing.ai/dpt3/file-types). Provide either `document` or `document_url`, not both.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — The DPT-3 model snapshot to use for this request. Accepts a dated snapshot (for example, `dpt-3-pro-20260710`), the `dpt-3-pro-latest` alias, or the bare `dpt-3-pro` family name (equivalent to `dpt-3-pro-latest`). Defaults to the latest DPT-3 Pro snapshot.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[ParseRunSyncRequestOptions]` — Optional object that customizes the parse. Use it to select which pages to process, adjust how content appears in the Markdown, or control how much detail the response includes. Sent as a JSON-serialized string in form data.
    
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

<details><summary><code>client.parse.<a href="src/fern/parse/client.py">list_jobs</a>(...) -> ParseListJobsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.parse.list_jobs()

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

**page:** `typing.Optional[int]` — Page number (0-indexed).
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items per page.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Filter by job status.
    
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

<details><summary><code>client.parse.<a href="src/fern/parse/client.py">create_job</a>(...) -> ParseCreateJobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Parse a document asynchronously. Returns a job ID; use it to poll for the job's status and retrieve the parse result once processing completes.
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

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.parse.create_job(
    document="example_document",
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

**document:** `typing.Optional[core.File]` — The file to parse. The file must be a PDF or image; see the list of [supported file types](https://docs.landing.ai/dpt3/file-types). Provide either `document` or `document_url`, not both.
    
</dd>
</dl>

<dl>
<dd>

**document_url:** `typing.Optional[str]` — A publicly accessible URL to the file to parse. The file must be a PDF or image; see the list of [supported file types](https://docs.landing.ai/dpt3/file-types). Provide either `document` or `document_url`, not both.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — The DPT-3 model snapshot to use for this request. Accepts a dated snapshot (for example, `dpt-3-pro-20260710`), the `dpt-3-pro-latest` alias, or the bare `dpt-3-pro` family name (equivalent to `dpt-3-pro-latest`). Defaults to the latest DPT-3 Pro snapshot.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[ParseCreateJobRequestOptions]` — Optional object that customizes the parse. Use it to select which pages to process, adjust how content appears in the Markdown, or control how much detail the response includes. Sent as a JSON-serialized string in form data.
    
</dd>
</dl>

<dl>
<dd>

**output_save_url:** `typing.Optional[str]` — Public URL the full response is delivered to; the API response then carries ``output_url`` instead of inline data.
    
</dd>
</dl>

<dl>
<dd>

**service_tier:** `typing.Optional[ParseCreateJobRequestServiceTier]` — Async service tier (``POST /jobs`` only). ``priority`` runs in the fast lane at the sync billing rate; absent → ``standard``.
    
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

<details><summary><code>client.parse.<a href="src/fern/parse/client.py">get_job</a>(...) -> ParseGetJobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of an async parse job. Once the job has ``completed``, ``result`` carries the parse response (or ``output_url`` when ``output_save_url`` was set). Partial success (some pages failed) is reported in ``result.metadata.failed_pages``.
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

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.parse.get_job(
    job_id="job_id",
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

**job_id:** `str` — The identifier of the job to retrieve, as returned by the create-job request.
    
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

## Extract
<details><summary><code>client.extract.<a href="src/fern/extract/client.py">v2extract_run_sync</a>(...) -> V2ExtractRunSyncResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Extract structured data from a Markdown document according to a JSON schema, with character-span grounding into the source Markdown. Runs synchronously and returns the result inline.
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

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.extract.v2extract_run_sync(
    schema={
        "properties": {"revenue": {"description": "Q1 revenue figure", "type": "string"}, "summary": {"description": "Executive summary", "type": "string"}},
        "type": "object"
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

**schema:** `typing.Dict[str, typing.Any]` — JSON Schema describing the fields to extract. The schema must be an object type with a ``properties`` map of field names to their types and descriptions.
    
</dd>
</dl>

<dl>
<dd>

**markdown:** `typing.Optional[str]` — Markdown string to extract from, or a multipart FILE part carrying the markdown (large inputs — uploads are staged by the gateway). Can come from any source — LandingAI parse output, a third-party parser, or hand-authored text. When the markdown was produced by ``POST /v2/parse``, it ends with a ``<!-- doc_id=<id> -->`` comment that the service reads automatically and echoes as ``metadata.doc_id``.
    
</dd>
</dl>

<dl>
<dd>

**markdown_url:** `typing.Optional[str]` — URL to fetch the markdown from. Must be a public http(s) URL; private/loopback IPs are rejected at submit time.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — The version of the model to use for extraction. Use ``extract-latest`` to use the latest version.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[V2ExtractOptions]` — Extraction options (``strict``). Omit for defaults.
    
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

<details><summary><code>client.extract.<a href="src/fern/extract/client.py">v2extract_list_jobs</a>(...) -> V2ExtractListJobsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List your Extract jobs, newest first.
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

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.extract.v2extract_list_jobs()

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

**page:** `typing.Optional[int]` — Page number (0-indexed).
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items per page.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Filter by job status.
    
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

<details><summary><code>client.extract.<a href="src/fern/extract/client.py">v2extract_create_job</a>(...) -> V2ExtractCreateJobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Extract structured data from a Markdown document according to a JSON schema, with character-span grounding into the source Markdown. Runs asynchronously and returns a job ID; use it to poll for status and retrieve the result once processing completes.
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

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.extract.v2extract_create_job(
    schema={
        "properties": {"revenue": {"description": "Q1 revenue figure", "type": "string"}, "summary": {"description": "Executive summary", "type": "string"}},
        "type": "object"
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

**schema:** `typing.Dict[str, typing.Any]` — JSON Schema describing the fields to extract. The schema must be an object type with a ``properties`` map of field names to their types and descriptions.
    
</dd>
</dl>

<dl>
<dd>

**markdown:** `typing.Optional[str]` — Markdown string to extract from, or a multipart FILE part carrying the markdown (large inputs — uploads are staged by the gateway). Can come from any source — LandingAI parse output, a third-party parser, or hand-authored text. When the markdown was produced by ``POST /v2/parse``, it ends with a ``<!-- doc_id=<id> -->`` comment that the service reads automatically and echoes as ``metadata.doc_id``.
    
</dd>
</dl>

<dl>
<dd>

**markdown_url:** `typing.Optional[str]` — URL to fetch the markdown from. Must be a public http(s) URL; private/loopback IPs are rejected at submit time.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — The version of the model to use for extraction. Use ``extract-latest`` to use the latest version.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[V2ExtractOptions]` — Extraction options (``strict``). Omit for defaults.
    
</dd>
</dl>

<dl>
<dd>

**output_save_url:** `typing.Optional[str]` — URL to save the result to — e.g. a presigned S3 PUT URL. Async jobs only. When set, the finished result is delivered (HTTP PUT) to this URL and the completed job reports ``output_url`` instead of an inline ``result``. Must be a public http(s) URL; private/loopback IPs are rejected at submit time.
    
</dd>
</dl>

<dl>
<dd>

**service_tier:** `typing.Optional[V2ExtractCreateJobRequestServiceTier]` — Async service tier. ``priority`` runs in the fast lane at the sync billing rate; absent → ``standard``.
    
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

<details><summary><code>client.extract.<a href="src/fern/extract/client.py">v2extract_get_job</a>(...) -> V2ExtractGetJobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of an async Extract job, including its result once the job has completed.
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

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.extract.v2extract_get_job(
    job_id="job_id",
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

**job_id:** `str` — The identifier of the job to retrieve, as returned by the create-job request.
    
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

## V2Workflow
<details><summary><code>client.v2workflow.<a href="src/fern/v2workflow/client.py">run_sync</a>(...) -> V2WorkflowRunSyncResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run synchronously and return the result inline.

Accepts ``application/json`` (the request fields as the body) or
``multipart/form-data`` (file fields are staged automatically).

Returns **504** if the work does not finish within the wait
window — long-running work belongs on the async ``POST
{path}/jobs`` route, which returns 202 immediately and is polled
via ``GET {path}/jobs/{job_id}``. On a 504 the workflow is
CANCELLED (a sync caller can never collect the result); a retry
starts the work over as a fresh job.
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
from fern import FernApi, WorkflowDocumentInput, PrebuiltWorkflowStep, PrebuiltWorkflowStepName

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.v2workflow.run_sync(
    inputs={
        "report": WorkflowDocumentInput(
            document="report_pdf",
        )
    },
    steps=[
        PrebuiltWorkflowStep(
            name=PrebuiltWorkflowStepName.PARSE_EXTRACT,
            document="$inputs.report",
            schema={
                "properties": {"revenue": {"type": "string"}},
                "type": "object"
            },
        )
    ],
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

**inputs:** `typing.Dict[str, WorkflowDocumentInput]` — Named document sources. Each key is a logical name referenced from steps as ``"$inputs.<name>"``. The gateway stages binary multipart uploads internally before the workflow runs.
    
</dd>
</dl>

<dl>
<dd>

**steps:** `typing.List[PrebuiltWorkflowStep]` — Phase 1: a single prebuilt-pipeline step (name must be ``"parse-extract"``). Its result appears in ``output`` under the step's name.
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Optional projection map. Keys are caller-chosen response field names; values are ``$output.<step>.<field>...`` references. Omitted → full results tree returned under ``output``.
    
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

<details><summary><code>client.v2workflow.<a href="src/fern/v2workflow/client.py">list_jobs</a>(...) -> V2WorkflowListJobsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.v2workflow.list_jobs()

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

**page:** `typing.Optional[int]` — Page number (0-indexed).
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items per page.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Filter by job status.
    
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

<details><summary><code>client.v2workflow.<a href="src/fern/v2workflow/client.py">create_job</a>(...) -> V2WorkflowCreateJobResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, WorkflowDocumentInput, PrebuiltWorkflowStep, PrebuiltWorkflowStepName

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.v2workflow.create_job(
    inputs={
        "report": WorkflowDocumentInput(
            document="report_pdf",
        )
    },
    steps=[
        PrebuiltWorkflowStep(
            name=PrebuiltWorkflowStepName.PARSE_EXTRACT,
            document="$inputs.report",
            schema={
                "properties": {"revenue": {"type": "string"}},
                "type": "object"
            },
        )
    ],
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

**inputs:** `typing.Dict[str, WorkflowDocumentInput]` — Named document sources. Each key is a logical name referenced from steps as ``"$inputs.<name>"``. The gateway stages binary multipart uploads internally before the workflow runs.
    
</dd>
</dl>

<dl>
<dd>

**steps:** `typing.List[PrebuiltWorkflowStep]` — Phase 1: a single prebuilt-pipeline step (name must be ``"parse-extract"``). Its result appears in ``output`` under the step's name.
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Optional projection map. Keys are caller-chosen response field names; values are ``$output.<step>.<field>...`` references. Omitted → full results tree returned under ``output``.
    
</dd>
</dl>

<dl>
<dd>

**service_tier:** `typing.Optional[V2WorkflowCreateJobRequestServiceTier]` — Async service tier. ``priority`` runs in the fast lane at the sync billing rate; absent → ``standard``.
    
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

<details><summary><code>client.v2workflow.<a href="src/fern/v2workflow/client.py">get_job</a>(...) -> V2WorkflowGetJobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Poll a job.

Returns ``{job_id, status, created_at}`` plus ``completed_at`` and
``result`` (on ``completed``) or ``error: {code, message}`` (on
``failed``). Statuses: ``pending`` → ``processing`` →
``completed`` | ``failed``.
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

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.v2workflow.get_job(
    job_id="job_id",
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

**job_id:** `str` — The identifier of the job to retrieve, as returned by the create-job request.
    
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

## Ground
<details><summary><code>client.ground.<a href="src/fern/ground/client.py">v2ground_run_sync</a>(...) -> V2GroundRunSyncResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Map extracted fields to the document blocks they were quoted from. Takes the extraction_metadata from an extract call and the structure tree from the parse call the markdown came from, and returns, for every extracted field, the overlapping blocks with their ids, page numbers, and bounding boxes. Runs synchronously and returns the result inline.
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

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.ground.v2ground_run_sync(
    extraction_metadata={
        "invoice_number": {"ranges": [{"end": 31, "start": 13}], "value": "INV-042"}
    },
    structure={
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

**extraction_metadata:** `typing.Dict[str, typing.Any]` — The ``extraction_metadata`` object returned by ``POST /v2/extract`` (or the pipeline's extract step): a tree mirroring your extraction schema whose leaves are ``{value, ranges}`` objects, where ``ranges`` are ``{start, end}`` Unicode code point offsets into the parse markdown.
    
</dd>
</dl>

<dl>
<dd>

**structure:** `typing.Dict[str, typing.Any]` — The ``structure`` tree from the parse response the extraction was produced from. Every block in the tree carries its ``grounding`` (``{page, range, box}``) inline; block ids in the response resolve against this exact tree.
    
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

<details><summary><code>client.ground.<a href="src/fern/ground/client.py">v2ground_list_jobs</a>(...) -> V2GroundListJobsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List your Ground jobs, newest first.
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

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.ground.v2ground_list_jobs()

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

**page:** `typing.Optional[int]` — Page number (0-indexed).
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items per page.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Filter by job status.
    
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

<details><summary><code>client.ground.<a href="src/fern/ground/client.py">v2ground_create_job</a>(...) -> V2GroundCreateJobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Map extracted fields to the document blocks they were quoted from. Takes the extraction_metadata from an extract call and the structure tree from the parse call the markdown came from, and returns, for every extracted field, the overlapping blocks with their ids, page numbers, and bounding boxes. Runs asynchronously and returns a job ID; use it to poll for status and retrieve the result once processing completes.
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

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.ground.v2ground_create_job(
    extraction_metadata={
        "invoice_number": {"ranges": [{"end": 31, "start": 13}], "value": "INV-042"}
    },
    structure={
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

**extraction_metadata:** `typing.Dict[str, typing.Any]` — The ``extraction_metadata`` object returned by ``POST /v2/extract`` (or the pipeline's extract step): a tree mirroring your extraction schema whose leaves are ``{value, ranges}`` objects, where ``ranges`` are ``{start, end}`` Unicode code point offsets into the parse markdown.
    
</dd>
</dl>

<dl>
<dd>

**structure:** `typing.Dict[str, typing.Any]` — The ``structure`` tree from the parse response the extraction was produced from. Every block in the tree carries its ``grounding`` (``{page, range, box}``) inline; block ids in the response resolve against this exact tree.
    
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

<details><summary><code>client.ground.<a href="src/fern/ground/client.py">v2ground_get_job</a>(...) -> V2GroundGetJobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of an async Ground job, including its result once the job has completed.
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

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.ground.v2ground_get_job(
    job_id="job_id",
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

**job_id:** `str` — The identifier of the job to retrieve, as returned by the create-job request.
    
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

## Files
<details><summary><code>client.files.<a href="src/fern/files/client.py">stage_file</a>(...) -> typing.Dict[str, str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stage bytes on the data plane; pass the returned ``file_ref`` in
job inputs (the contract request types take ``*_ref`` fields).
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

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.files.stage_file(
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

