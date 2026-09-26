# Reference
<details><summary><code>client.<a href="src/fern/client.py">health_health_get</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Probe the configured database with a 2s timeout.
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

client.health_health_get()

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

## Assets
<details><summary><code>client.assets.<a href="src/fern/assets/client.py">list_assets</a>(...) -> AssetListResponse</code></summary>
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

client.assets.list_assets()

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

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
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

<details><summary><code>client.assets.<a href="src/fern/assets/client.py">delete_asset</a>(...) -> AssetDeleteResponse</code></summary>
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

client.assets.delete_asset(
    asset_id="asset_id",
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

**asset_id:** `str` 
    
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

<details><summary><code>client.assets.<a href="src/fern/assets/client.py">download_asset</a>(...) -> typing.Any</code></summary>
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

client.assets.download_asset(
    asset_id="asset_id",
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

**asset_id:** `str` 
    
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

<details><summary><code>client.assets.<a href="src/fern/assets/client.py">get_asset_edit_context</a>(...) -> AssetEditContext</code></summary>
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

client.assets.get_asset_edit_context(
    asset_id="asset_id",
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

**asset_id:** `str` 
    
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

<details><summary><code>client.assets.<a href="src/fern/assets/client.py">get_asset_image</a>(...) -> typing.Any</code></summary>
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

client.assets.get_asset_image(
    asset_id="asset_id",
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

**asset_id:** `str` 
    
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

## GenerationJobs
<details><summary><code>client.generation_jobs.<a href="src/fern/generation_jobs/client.py">list_generation_jobs</a>(...) -> GenerationJobListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return recent durable generation jobs as queue/history records.
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

client.generation_jobs.list_generation_jobs()

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

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListGenerationJobsApiGenerationJobsGetRequestStatus]` 
    
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

<details><summary><code>client.generation_jobs.<a href="src/fern/generation_jobs/client.py">create_generation_job</a>(...) -> GenerationJobCreated</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GenerationOutputCreate

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.generation_jobs.create_generation_job(
    outputs=[
        GenerationOutputCreate(
            output_key="output_key",
            prompt="prompt",
            template_ref="template_ref",
        )
    ],
    source_image_ref="source_image_ref",
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

**outputs:** `typing.List[GenerationOutputCreate]` 
    
</dd>
</dl>

<dl>
<dd>

**source_image_ref:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_job_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[GenerationJobCreateLocale]` 
    
</dd>
</dl>

<dl>
<dd>

**marketing_kit_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**planner_payload:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**user_prompt:** `typing.Optional[str]` 
    
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

<details><summary><code>client.generation_jobs.<a href="src/fern/generation_jobs/client.py">get_kit_slot_output_image</a>(...) -> typing.Any</code></summary>
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

client.generation_jobs.get_kit_slot_output_image(
    marketing_kit_id=1,
    slot_id="slot_id",
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

**marketing_kit_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**slot_id:** `str` 
    
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

<details><summary><code>client.generation_jobs.<a href="src/fern/generation_jobs/client.py">get_generation_job</a>(...) -> GenerationJobOut</code></summary>
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

client.generation_jobs.get_generation_job(
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

**job_id:** `str` 
    
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

<details><summary><code>client.generation_jobs.<a href="src/fern/generation_jobs/client.py">generation_job_events</a>(...) -> typing.Any</code></summary>
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

client.generation_jobs.generation_job_events(
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

**job_id:** `str` 
    
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

<details><summary><code>client.generation_jobs.<a href="src/fern/generation_jobs/client.py">get_generation_output_image</a>(...) -> typing.Any</code></summary>
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

client.generation_jobs.get_generation_output_image(
    job_id="job_id",
    output_id="output_id",
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

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**output_id:** `str` 
    
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

<details><summary><code>client.generation_jobs.<a href="src/fern/generation_jobs/client.py">start_generation_job</a>(...) -> GenerationJobStartResponse</code></summary>
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

client.generation_jobs.start_generation_job(
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

**job_id:** `str` 
    
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

<details><summary><code>client.generation_jobs.<a href="src/fern/generation_jobs/client.py">stop_generation_job</a>(...) -> GenerationJobStopResponse</code></summary>
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

client.generation_jobs.stop_generation_job(
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

**job_id:** `str` 
    
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

## GenerationPlan
<details><summary><code>client.generation_plan.<a href="src/fern/generation_plan/client.py">create_generation_plan</a>(...) -> GenerationPlanOut</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create the initial editable output plan for the generation workflow.

This endpoint intentionally owns the compatibility/default planning
contract so the frontend can fail loudly when the backend route is broken
instead of silently manufacturing a local plan.
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
from fern import FernApi, ProductProfileIn

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.generation_plan.create_generation_plan(
    kit_client_id="kit_client_id",
    product=ProductProfileIn(),
    source_image_ref="source_image_ref",
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

**kit_client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**product:** `ProductProfileIn` 
    
</dd>
</dl>

<dl>
<dd>

**source_image_ref:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**explicit_template_refs:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[GenerationPlanRequestLocale]` 
    
</dd>
</dl>

<dl>
<dd>

**user_prompt:** `typing.Optional[str]` 
    
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

## Editor
<details><summary><code>client.editor.<a href="src/fern/editor/client.py">get_image_bytes</a>(...) -> typing.Any</code></summary>
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

client.editor.get_image_bytes(
    image_id="image_id",
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

**image_id:** `str` 
    
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

<details><summary><code>client.editor.<a href="src/fern/editor/client.py">start_edit</a>(...) -> EditAccepted</code></summary>
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

client.editor.start_edit(
    image_id="image_id",
    mask_box={
        "key": 1
    },
    new_text="new_text",
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

**image_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**mask_box:** `typing.Dict[str, int]` — x,y,w,h
    
</dd>
</dl>

<dl>
<dd>

**new_text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**kit_id:** `typing.Optional[str]` — Optional kit id for local edit context; safe-character allowlist keeps sidecar references portable.
    
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

<details><summary><code>client.editor.<a href="src/fern/editor/client.py">create_edit_result</a>(...) -> EditResultOut</code></summary>
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

client.editor.create_edit_result(
    image_id="image_id",
    result_data_url="result_data_url",
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

**image_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**result_data_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**source_image_ref:** `typing.Optional[str]` 
    
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

<details><summary><code>client.editor.<a href="src/fern/editor/client.py">get_edit_result_image</a>(...) -> typing.Any</code></summary>
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

client.editor.get_edit_result_image(
    image_id="image_id",
    edit_result_ref="edit_result_ref",
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

**image_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**edit_result_ref:** `str` 
    
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

<details><summary><code>client.editor.<a href="src/fern/editor/client.py">edit_events</a>(...) -> typing.Any</code></summary>
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

client.editor.edit_events(
    image_id="image_id",
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

**image_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**job_id:** `str` 
    
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

<details><summary><code>client.editor.<a href="src/fern/editor/client.py">ocr_image</a>(...) -> OcrResponse</code></summary>
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

client.editor.ocr_image(
    image_id="image_id",
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

**image_id:** `str` 
    
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

<details><summary><code>client.editor.<a href="src/fern/editor/client.py">get_editor_project</a>(...) -> EditorProjectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the saved Viskit editor project JSON for a canonical image id.
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

client.editor.get_editor_project(
    image_id="image_id",
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

**image_id:** `str` 
    
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

<details><summary><code>client.editor.<a href="src/fern/editor/client.py">put_editor_project</a>(...) -> EditorProjectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace the persisted project JSON for a canonical image id.
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

client.editor.put_editor_project(
    image_id="image_id",
    document={
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

**image_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `EditorProjectSaveRequest` 
    
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

<details><summary><code>client.editor.<a href="src/fern/editor/client.py">export_editor_project</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download the saved editor project as project JSON.
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

client.editor.export_editor_project(
    image_id="image_id",
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

**image_id:** `str` 
    
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

<details><summary><code>client.editor.<a href="src/fern/editor/client.py">import_editor_project</a>(...) -> EditorProjectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import project JSON into the persisted editor state for this image.
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

client.editor.import_editor_project(
    image_id="image_id",
    document={
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

**image_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `EditorProjectSaveRequest` 
    
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

<details><summary><code>client.editor.<a href="src/fern/editor/client.py">save_edited_image</a>(...) -> SaveImageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Persist an edit result via an explicit replace-or-copy choice.
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
from fern.editor import SaveImageRequestMode

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.editor.save_edited_image(
    image_id="image_id",
    edit_result_ref="edit_result_ref",
    mode=SaveImageRequestMode.REPLACE,
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

**image_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**edit_result_ref:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**mode:** `SaveImageRequestMode` 
    
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

## Imagegen
<details><summary><code>client.imagegen.<a href="src/fern/imagegen/client.py">list_kits</a>(...) -> KitListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return kits joined with their product catalog row, paginated & filtered.

``thumbs`` is the concatenation of up-to-5 hero png_paths (slot 1..5) and
up-to-9 detail png_paths (M1..M9) — 14 slots total, NULL-padded for any
missing rows.  Callers render placeholder cells for NULL entries.

Standalone generated assets are also returned as catalog entries with
``source_type='asset'`` so non-kit generations remain visible in Catalog.

``recent=true`` preserves the Dashboard contract by returning kit rows
only. Catalog calls leave ``recent`` false and receive kit plus asset rows.

``recent`` is otherwise advisory; sort defaults to ``created_at DESC`` to preserve
the EPIC-7 Dashboard call shape (``?recent=true&limit=6``).  Catalog
(EPIC-8) passes ``offset``, ``status``, ``locale``, ``min_score``,
``category``, ``sort``, ``order`` for filtered/paginated views.
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

client.imagegen.list_kits()

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

**recent:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**min_score:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sku:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListKitsApiKitsGetRequestSort]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListKitsApiKitsGetRequestOrder]` 
    
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

<details><summary><code>client.imagegen.<a href="src/fern/imagegen/client.py">delete_generated_image</a>(...) -> DeleteKitImageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a generated image from a catalog kit slot and delete its PNG.
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

client.imagegen.delete_generated_image(
    db_kit_id=1,
    image_id="image_id",
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

**db_kit_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**image_id:** `str` 
    
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

<details><summary><code>client.imagegen.<a href="src/fern/imagegen/client.py">get_kit_meta</a>(...) -> KitMetaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read result sidecars for *db_kit_id*; 404 if the kit root is unknown.
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

client.imagegen.get_kit_meta(
    db_kit_id=1,
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

**db_kit_id:** `int` 
    
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

<details><summary><code>client.imagegen.<a href="src/fern/imagegen/client.py">get_kit_events</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stream per-image status events for *kit_id* as text/event-stream.

Returns 404 when the kit_id has never been published to the bus
(callers can use this as a "kit not started" signal).  Each line
conforms to the SSE wire format::

    data: {"image_id": "H1", "status": "color_locked", "progress": 0,
           "brand_color_locked": true}
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

client.imagegen.get_kit_events(
    kit_id="kit_id",
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

**kit_id:** `str` 
    
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

<details><summary><code>client.imagegen.<a href="src/fern/imagegen/client.py">post_generate</a>(...) -> GenerateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate the 14-image kit for *kit_id*.
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
from fern import FernApi, SpecIn, DetailSectionIn, DetailSectionInId, ThreePieceIn, HeroSectionIn, HeroSectionInId, SpecInLocale, SellingPointIn, SellingPointInPriority, SkuMetaIn, SkuMetaInProductType
from fern.imagegen import GenerateRequestLocale

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.imagegen.post_generate(
    kit_id="kit_id",
    brand_color_hex="brand_color_hex",
    locale=GenerateRequestLocale.ZH,
    spec=SpecIn(
        detail_sections=[
            DetailSectionIn(
                id=DetailSectionInId.M1,
                three_piece=ThreePieceIn(
                    copy="copy",
                    design_note="design_note",
                    visual="visual",
                ),
            )
        ],
        hero_sections=[
            HeroSectionIn(
                id=HeroSectionInId.H1,
                three_piece=ThreePieceIn(
                    copy="copy",
                    design_note="design_note",
                    visual="visual",
                ),
            )
        ],
        locale=SpecInLocale.ZH,
        selling_points=[
            SellingPointIn(
                evidence="evidence",
                priority=SellingPointInPriority.HIGH,
                title="title",
            )
        ],
        sku_meta=SkuMetaIn(
            brand="brand",
            category="category",
            price=1.1,
            product_type=SkuMetaInProductType.BLUE_HAT,
        ),
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

**kit_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**brand_color_hex:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**locale:** `GenerateRequestLocale` 
    
</dd>
</dl>

<dl>
<dd>

**spec:** `SpecIn` 
    
</dd>
</dl>

<dl>
<dd>

**retrieved_bestseller_ids:** `typing.Optional[typing.List[int]]` 
    
</dd>
</dl>

<dl>
<dd>

**style_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**template_scheme_ref:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**template_slot_overrides:** `typing.Optional[typing.Dict[str, str]]` 
    
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

<details><summary><code>client.imagegen.<a href="src/fern/imagegen/client.py">get_generated_image</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Serve a generated kit image by public kit id and slot id.
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

client.imagegen.get_generated_image(
    kit_id="kit_id",
    image_id="image_id",
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

**kit_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**image_id:** `str` 
    
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
<details><summary><code>client.extract.<a href="src/fern/extract/client.py">warmup_extract_api_kits_warmup_extract_get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Prime the vision provider connection so the first /extract call is warm.

Deliberately uses probe(timeout=5) — a 5s deviation from the 30s default
because this is a best-effort fire-and-forget warmup; we swallow all
failures and always return 204 so the frontend never sees an error.
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

client.extract.warmup_extract_api_kits_warmup_extract_get()

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

<details><summary><code>client.extract.<a href="src/fern/extract/client.py">extract</a>(...) -> ExtractResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Extract per-field inferences from a product image.

Uses the vision provider (registry role "vision"); falls back to "llm" if
the vision role is unavailable (R2 mitigation).

Reserved-prefix guard: POST to kit_id='_warmup' returns 404 — defensive
against POST collision with the GET /_warmup/extract warmup endpoint.
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

client.extract.extract(
    kit_id="kit_id",
    image_url="image_url",
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

**kit_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**image_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
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

## Copywriter
<details><summary><code>client.copywriter.<a href="src/fern/copywriter/client.py">create_spec</a>(...) -> SpecResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate the marketing spec for *kit_id* under the requested locale.
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
from fern import FernApi, SellingPointIn, SellingPointInPriority, SkuMetaIn, SkuMetaInProductType
from fern.copywriter import SpecRequestLocale

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.copywriter.create_spec(
    kit_id="kit_id",
    locale=SpecRequestLocale.ZH,
    selling_points=[
        SellingPointIn(
            evidence="evidence",
            priority=SellingPointInPriority.HIGH,
            title="title",
        )
    ],
    sku_meta=SkuMetaIn(
        brand="brand",
        category="category",
        price=1.1,
        product_type=SkuMetaInProductType.BLUE_HAT,
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

**kit_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**locale:** `SpecRequestLocale` 
    
</dd>
</dl>

<dl>
<dd>

**selling_points:** `typing.List[SellingPointIn]` 
    
</dd>
</dl>

<dl>
<dd>

**sku_meta:** `SkuMetaIn` 
    
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

## Metrics
<details><summary><code>client.metrics.<a href="src/fern/metrics/client.py">get_weekly_metrics</a>() -> WeeklyMetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Aggregate live metrics — current-ISO-week kits + 12-week sparklines.
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

client.metrics.get_weekly_metrics()

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

## Onboarding
<details><summary><code>client.onboarding.<a href="src/fern/onboarding/client.py">get_onboarding_needed</a>() -> OnboardingNeededResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return whether onboarding is needed for this workspace.
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

client.onboarding.get_onboarding_needed()

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

## Providers
<details><summary><code>client.providers.<a href="src/fern/providers/client.py">get_config_state</a>() -> ConfigStateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the on-disk YAML body and its SHA-256 checksum.

Kept for legacy/admin tools that need an explicit config-body save path.
Bootstrapping the live config file is a lifespan concern
(``apps.api.main._bootstrap_config_if_missing``), so this route is
side-effect-free; if the file truly doesn't exist, 404.
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

client.providers.get_config_state()

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

<details><summary><code>client.providers.<a href="src/fern/providers/client.py">save_endpoints</a>(...) -> SaveEndpointsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Save the new config YAML body.  ADR-010 v2 lock+checksum semantics.
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

client.providers.save_endpoints(
    expected_sha256="expected_sha256",
    new_yaml="new_yaml",
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

**expected_sha256:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**new_yaml:** `str` 
    
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

<details><summary><code>client.providers.<a href="src/fern/providers/client.py">get_endpoint</a>(...) -> EndpointStanza</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the structured stanza for *role* so the UI can prefill the edit modal.
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

client.providers.get_endpoint(
    role="role",
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

**role:** `str` 
    
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

<details><summary><code>client.providers.<a href="src/fern/providers/client.py">create_endpoint</a>(...) -> SaveEndpointsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a single role stanza without exposing YAML editing to the UI.
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
from fern.providers import CreateEndpointRequestProtocol

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.providers.create_endpoint(
    role="role",
    api_key="api_key",
    base_url="base_url",
    model="model",
    name="name",
    protocol=CreateEndpointRequestProtocol.OPENAI_COMPATIBLE,
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

**role:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**base_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**protocol:** `CreateEndpointRequestProtocol` 
    
</dd>
</dl>

<dl>
<dd>

**adapter:** `typing.Optional[str]` 
    
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

<details><summary><code>client.providers.<a href="src/fern/providers/client.py">update_endpoint</a>(...) -> SaveEndpointsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replace a single role's stanza.

``api_key`` semantics: ``None``, empty string, and whitespace-only all
mean "preserve the existing env-var binding on disk".  Any other value
is persisted to the secrets store and the YAML's ``api_key_env`` is
rewritten to the derived env name.  To explicitly unbind, DELETE the
role and re-POST.
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
from fern.providers import UpdateEndpointRequestProtocol

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.providers.update_endpoint(
    role="role",
    base_url="base_url",
    model="model",
    name="name",
    protocol=UpdateEndpointRequestProtocol.OPENAI_COMPATIBLE,
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

**role:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**base_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**protocol:** `UpdateEndpointRequestProtocol` 
    
</dd>
</dl>

<dl>
<dd>

**adapter:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**api_key:** `typing.Optional[str]` 
    
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

<details><summary><code>client.providers.<a href="src/fern/providers/client.py">delete_endpoint</a>(...) -> SaveEndpointsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a role's stanza from config.yaml and re-boot the registry.

Read-modify-write under the same lock+checksum protocol as POST.  Missing
role → 404.  Required roles (``REQUIRED_ROLES``) → 409; deleting them
would crash the next startup with ERR-PROV-001.  Use PUT to swap settings.
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

client.providers.delete_endpoint(
    role="role",
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

**role:** `str` 
    
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

<details><summary><code>client.providers.<a href="src/fern/providers/client.py">get_endpoint_secret</a>(...) -> EndpointSecretResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the locally saved secret for *role*.

Only keys saved through ``data/secrets.json`` are revealable.  If the
endpoint is backed by a shell/environment variable, the UI can still probe
it via ``api_key_env`` but the plaintext value is not exposed here.
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

client.providers.get_endpoint_secret(
    role="role",
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

**role:** `str` 
    
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

<details><summary><code>client.providers.<a href="src/fern/providers/client.py">get_provider_health</a>() -> typing.List[ProviderHealthRow]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Per-role health snapshot derived from ``app.state.registry``.

Latency probes are not yet implemented (status/latency_ms stubbed to
None).  When a known role has no binding, the row carries the role
name in ``unbound`` so the frontend can render the warning chip.
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

client.providers.get_provider_health()

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

<details><summary><code>client.providers.<a href="src/fern/providers/client.py">list_provider_models</a>(...) -> ProviderProbeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Probe registry-bound adapter model catalogs.

Each adapter hits its own ``/models`` endpoint (OpenAI: ``{base_url}/models``,
Anthropic: ``{base_url}/v1/models``). Passing ``?role=llm`` probes just one
role so the UI can test a row without waiting for every configured backend.
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

client.providers.list_provider_models()

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

**role:** `typing.Optional[str]` 
    
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

<details><summary><code>client.providers.<a href="src/fern/providers/client.py">probe_candidate</a>(...) -> ProbeCandidateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Probe a candidate (un-registered) endpoint and return its model catalog.

Accepts either an existing ``api_key_env`` name (looked up via
``os.environ``) or an inline ``api_key`` (used directly for the probe but
never persisted).  The inline path lets the AddEndpointModal probe a
freshly-pasted key before the operator commits to saving it.

Adapter contract: ``probe()`` never raises — failures surface as
``ok=False`` with an ``error`` string.
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
from fern.providers import ProbeCandidateRequestProtocol

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.providers.probe_candidate(
    base_url="base_url",
    protocol=ProbeCandidateRequestProtocol.OPENAI_COMPATIBLE,
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

**base_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**protocol:** `ProbeCandidateRequestProtocol` 
    
</dd>
</dl>

<dl>
<dd>

**adapter:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**api_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**api_key_env:** `typing.Optional[str]` 
    
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

<details><summary><code>client.providers.<a href="src/fern/providers/client.py">store_secret</a>(...) -> StoreSecretResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Persist an API key to the gitignored secrets store + inject into env.

Derives a deterministic env-var name from ``role`` + ``name`` so the
operator never has to invent one.  The plaintext key lives only in
``data/secrets.json`` (gitignored); ``config.yaml`` continues to store
only the env-var name per ADR-011.
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

client.providers.store_secret(
    api_key="api_key",
    name="name",
    role="role",
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

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**role:** `str` 
    
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

<details><summary><code>client.providers.<a href="src/fern/providers/client.py">get_provider_summary</a>() -> ProvidersSummaryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Summary of the on-disk ``config.yaml``.
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

client.providers.get_provider_summary()

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

## Queue
<details><summary><code>client.queue.<a href="src/fern/queue/client.py">get_active_queue</a>() -> typing.List[QueueJob]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the snapshot of active kits.  Empty list when idle.
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

client.queue.get_active_queue()

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

## Settings
<details><summary><code>client.settings.<a href="src/fern/settings/client.py">post_settings</a>(...) -> SettingsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read-modify-write the 4 workspace-level options into config.yaml.

Retries up to ``_MAX_CHECKSUM_RETRIES`` times if the config drifted
underneath us (concurrent provider save).  Inode-changed is treated
identically to checksum-mismatch.
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

client.settings.post_settings()

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

**brand_color:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**default_locale:** `typing.Optional[SettingsUpdateDefaultLocale]` 
    
</dd>
</dl>

<dl>
<dd>

**export_preset:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**monthly_cap_usd:** `typing.Optional[float]` 
    
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

## SourceImages
<details><summary><code>client.source_images.<a href="src/fern/source_images/client.py">create_source_image</a>() -> SourceImageOut</code></summary>
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

client.source_images.create_source_image()

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

<details><summary><code>client.source_images.<a href="src/fern/source_images/client.py">create_source_image_from_existing</a>(...) -> SourceImageImportOut</code></summary>
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

client.source_images.create_source_image_from_existing(
    image_id="image_id",
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

**image_id:** `str` 
    
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

<details><summary><code>client.source_images.<a href="src/fern/source_images/client.py">get_source_image</a>(...) -> typing.Any</code></summary>
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

client.source_images.get_source_image(
    source_image_ref="source_image_ref",
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

**source_image_ref:** `str` 
    
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

## Templates
<details><summary><code>client.templates.<a href="src/fern/templates/client.py">get_templates</a>() -> typing.List[TemplateSummary]</code></summary>
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

client.templates.get_templates()

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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">create_template</a>(...) -> TemplateSummary</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.templates import TemplatePayloadLocale

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.templates.create_template(
    locale=TemplatePayloadLocale.ZH,
    name="name",
    prompt_template={
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

**locale:** `TemplatePayloadLocale` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**prompt_template:** `typing.Dict[str, str]` 
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[TemplatePayloadCategory]` 
    
</dd>
</dl>

<dl>
<dd>

**category_tips:** `typing.Optional[typing.Dict[str, str]]` 
    
</dd>
</dl>

<dl>
<dd>

**defaults:** `typing.Optional[typing.Dict[str, str]]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**examples:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**supports_image_reference:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**variants:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">copy_template</a>(...) -> TemplateSummary</code></summary>
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

client.templates.copy_template(
    source_ref="source_ref",
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

**source_ref:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">get_managed_templates</a>() -> typing.List[TemplateSummary]</code></summary>
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

client.templates.get_managed_templates()

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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">preview_template</a>(...) -> PreviewResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.templates import PreviewRequestLocale

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.templates.preview_template(
    locale=PreviewRequestLocale.ZH,
    template_ref="template_ref",
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

**locale:** `PreviewRequestLocale` 
    
</dd>
</dl>

<dl>
<dd>

**template_ref:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**brand_color_hex:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**copy:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**design_note:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sample_brand:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sample_category:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sample_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**style_prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**visual:** `typing.Optional[str]` 
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">list_schemes</a>(...) -> typing.List[SchemeSummary]</code></summary>
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

client.templates.list_schemes()

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

**locale:** `typing.Optional[ListSchemesApiTemplatesSchemesGetRequestLocale]` 
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">create_scheme</a>(...) -> SchemeSummary</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SchemeSlot, SchemeSlotSlotId
from fern.templates import SchemePayloadLocale

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.templates.create_scheme(
    locale=SchemePayloadLocale.ZH,
    name="name",
    slots=[
        SchemeSlot(
            slot_id=SchemeSlotSlotId.H1,
            template_ref="template_ref",
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

**locale:** `SchemePayloadLocale` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**slots:** `typing.List[SchemeSlot]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">delete_template</a>(...) -> typing.Dict[str, bool]</code></summary>
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

client.templates.delete_template(
    template_ref="template_ref",
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

**template_ref:** `str` 
    
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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">update_template</a>(...) -> TemplateSummary</code></summary>
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

client.templates.update_template(
    template_ref="template_ref",
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

**template_ref:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[TemplateUpdateCategory]` 
    
</dd>
</dl>

<dl>
<dd>

**category_tips:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**defaults:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**examples:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt_template:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**supports_image_reference:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**variants:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
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

