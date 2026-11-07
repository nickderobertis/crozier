# Reference
<details><summary><code>client.<a href="src/fern/client.py">run_task</a>(...) -> TaskRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run a task
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
    environment=FernApiEnvironment.CLOUD,
)

client.run_task(
    prompt="Find the top 3 posts on Hacker News.",
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

**prompt:** `str` — 
The goal or task description for Skyvern to accomplish
    
</dd>
</dl>

<dl>
<dd>

**user_agent:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — 
The starting URL for the task. If not provided, Skyvern will attempt to determine an appropriate URL
    
</dd>
</dl>

<dl>
<dd>

**engine:** `typing.Optional[RunEngine]` — 
The engine that powers the agent task. The default value is `skyvern-1.0`, which is good for simple tasks like filling a form, or searching for information on Google. `skyvern-2.0` remains available for existing V2 workflows and explicitly requested V2 task runs. The `openai-cua` engine uses OpenAI's CUA model. The `anthropic-cua` uses Anthropic's Claude Sonnet 3.7 model with the computer use tool.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title for the task
    
</dd>
</dl>

<dl>
<dd>

**proxy_location:** `typing.Optional[TaskRunRequestInputProxyLocation]` 


Geographic Proxy location to route the browser traffic through. This is only available in Skyvern Cloud.

Available geotargeting options:
- RESIDENTIAL: the default value. Skyvern Cloud uses a random US residential proxy.
- RESIDENTIAL_ES: Spain
- RESIDENTIAL_IE: Ireland
- RESIDENTIAL_GB: United Kingdom
- RESIDENTIAL_IN: India
- RESIDENTIAL_JP: Japan
- RESIDENTIAL_FR: France
- RESIDENTIAL_DE: Germany
- RESIDENTIAL_NZ: New Zealand
- RESIDENTIAL_PH: Philippines
- RESIDENTIAL_KR: South Korea
- RESIDENTIAL_SA: Saudi Arabia
- RESIDENTIAL_ZA: South Africa
- RESIDENTIAL_AR: Argentina
- RESIDENTIAL_AU: Australia
- RESIDENTIAL_BR: Brazil
- RESIDENTIAL_TR: Turkey
- RESIDENTIAL_CA: Canada
- RESIDENTIAL_MX: Mexico
- RESIDENTIAL_IT: Italy
- RESIDENTIAL_NL: Netherlands
- RESIDENTIAL_ISP: ISP proxy
- US-CA: California (deprecated, routes through RESIDENTIAL_ISP)
- US-NY: New York (deprecated, routes through RESIDENTIAL_ISP)
- US-TX: Texas (deprecated, routes through RESIDENTIAL_ISP)
- US-FL: Florida (deprecated, routes through RESIDENTIAL_ISP)
- US-WA: Washington (deprecated, routes through RESIDENTIAL_ISP)
- NONE: No proxy

For self-hosted deployments, you can pass a custom proxy URL as a dict: {"url": "http://user:password@proxy.example.com:8080"}. This routes the browser through your own proxy server and takes precedence over any globally configured proxy pool.
 Can also be a GeoTarget object for granular city/state targeting: {"country": "US", "subdivision": "CA", "city": "San Francisco"}
    
</dd>
</dl>

<dl>
<dd>

**data_extraction_schema:** `typing.Optional[TaskRunRequestInputDataExtractionSchema]` — 
The schema for data to be extracted from the webpage. If you're looking for consistent data schema being returned by the agent, it's highly recommended to use https://json-schema.org/.
    
</dd>
</dl>

<dl>
<dd>

**error_code_mapping:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — 
Custom mapping of error codes to error messages if Skyvern encounters an error.
    
</dd>
</dl>

<dl>
<dd>

**max_steps:** `typing.Optional[int]` — 
Maximum number of steps the task can take. Task will fail if it exceeds this number. Cautions: you are charged per step so please set this number to a reasonable value. Contact sales@skyvern.com for custom pricing.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — 
After a run is finished, send an update to this URL. Refer to https://www.skyvern.com/docs/running-tasks/webhooks-faq for more details.
    
</dd>
</dl>

<dl>
<dd>

**totp_identifier:** `typing.Optional[str]` — 
Identifier for the TOTP/2FA/MFA code when the code is pushed to Skyvern. Refer to https://www.skyvern.com/docs/credentials/totp#option-3-push-code-to-skyvern for more details.
    
</dd>
</dl>

<dl>
<dd>

**totp_url:** `typing.Optional[str]` — 
URL that serves TOTP/2FA/MFA codes for Skyvern to use during the workflow run. Refer to https://www.skyvern.com/docs/credentials/totp#option-2-get-code-from-your-endpoint for more details.
    
</dd>
</dl>

<dl>
<dd>

**browser_session_id:** `typing.Optional[str]` — 
Run the task or workflow in the specific Skyvern browser session. Having a browser session can persist the real-time state of the browser, so that the next run can continue from where the previous run left off.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[typing.Dict[str, typing.Any]]` — 
Optional model configuration.
    
</dd>
</dl>

<dl>
<dd>

**extra_http_headers:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — The extra HTTP headers for the requests in browser.
    
</dd>
</dl>

<dl>
<dd>

**cdp_connect_headers:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — HTTP headers attached ONLY to the CDP WebSocket handshake when connecting to a remote browser via browser_address. Use this for browser-provider auth (e.g., x-api-key for Skyvern Cloud, Browserless, or similar). These headers are NEVER forwarded to target websites.
    
</dd>
</dl>

<dl>
<dd>

**publish_workflow:** `typing.Optional[bool]` — Deprecated. Whether to publish a `skyvern-2.0` task as a reusable workflow. For backwards compatibility, this routes the request through the legacy `skyvern-2.0` publish path. Prefer creating reusable workflows through the workflow APIs.
    
</dd>
</dl>

<dl>
<dd>

**include_action_history_in_verification:** `typing.Optional[bool]` — Whether to include action history when verifying that the task is complete
    
</dd>
</dl>

<dl>
<dd>

**max_screenshot_scrolls:** `typing.Optional[int]` — The maximum number of scrolls for the post action screenshot. When it's None or 0, it takes the current viewpoint screenshot.
    
</dd>
</dl>

<dl>
<dd>

**browser_address:** `typing.Optional[str]` — The CDP address for the task.
    
</dd>
</dl>

<dl>
<dd>

**run_with:** `typing.Optional[str]` — Whether to run the task with agent or code. Null means use the default.
    
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

<details><summary><code>client.<a href="src/fern/client.py">run_workflow</a>(...) -> WorkflowRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run an agent
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
    environment=FernApiEnvironment.CLOUD,
)

client.run_workflow(
    agent_id="wpid_123",
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

**agent_id:** `str` — ID of the agent to run. Starts with `wpid_`. `workflow_id` is accepted as an alias.
    
</dd>
</dl>

<dl>
<dd>

**template:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**max_steps_override:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**user_agent:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.Dict[str, typing.Any]]` — Parameters to pass to the workflow
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title for this workflow run
    
</dd>
</dl>

<dl>
<dd>

**proxy_location:** `typing.Optional[WorkflowRunRequestInputProxyLocation]` 


Geographic Proxy location to route the browser traffic through. This is only available in Skyvern Cloud.

Available geotargeting options:
- RESIDENTIAL: the default value. Skyvern Cloud uses a random US residential proxy.
- RESIDENTIAL_ES: Spain
- RESIDENTIAL_IE: Ireland
- RESIDENTIAL_GB: United Kingdom
- RESIDENTIAL_IN: India
- RESIDENTIAL_JP: Japan
- RESIDENTIAL_FR: France
- RESIDENTIAL_DE: Germany
- RESIDENTIAL_NZ: New Zealand
- RESIDENTIAL_PH: Philippines
- RESIDENTIAL_KR: South Korea
- RESIDENTIAL_SA: Saudi Arabia
- RESIDENTIAL_ZA: South Africa
- RESIDENTIAL_AR: Argentina
- RESIDENTIAL_AU: Australia
- RESIDENTIAL_BR: Brazil
- RESIDENTIAL_TR: Turkey
- RESIDENTIAL_CA: Canada
- RESIDENTIAL_MX: Mexico
- RESIDENTIAL_IT: Italy
- RESIDENTIAL_NL: Netherlands
- RESIDENTIAL_ISP: ISP proxy
- US-CA: California (deprecated, routes through RESIDENTIAL_ISP)
- US-NY: New York (deprecated, routes through RESIDENTIAL_ISP)
- US-TX: Texas (deprecated, routes through RESIDENTIAL_ISP)
- US-FL: Florida (deprecated, routes through RESIDENTIAL_ISP)
- US-WA: Washington (deprecated, routes through RESIDENTIAL_ISP)
- NONE: No proxy

For self-hosted deployments, you can pass a custom proxy URL as a dict: {"url": "http://user:password@proxy.example.com:8080"}. This routes the browser through your own proxy server and takes precedence over any globally configured proxy pool.
 Can also be a GeoTarget object for granular city/state targeting: {"country": "US", "subdivision": "CA", "city": "San Francisco"}
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — URL to send workflow status updates to after a run is finished. Refer to https://www.skyvern.com/docs/running-tasks/webhooks-faq for webhook questions.
    
</dd>
</dl>

<dl>
<dd>

**totp_url:** `typing.Optional[str]` — 
URL that serves TOTP/2FA/MFA codes for Skyvern to use during the workflow run. Refer to https://www.skyvern.com/docs/credentials/totp#option-2-get-code-from-your-endpoint for more details.
    
</dd>
</dl>

<dl>
<dd>

**totp_identifier:** `typing.Optional[str]` — 
Identifier for the TOTP/2FA/MFA code when the code is pushed to Skyvern. Refer to https://www.skyvern.com/docs/credentials/totp#option-3-push-code-to-skyvern for more details.
    
</dd>
</dl>

<dl>
<dd>

**browser_session_id:** `typing.Optional[str]` — ID of a Skyvern browser session to reuse, having it continue from the current screen state
    
</dd>
</dl>

<dl>
<dd>

**browser_profile_id:** `typing.Optional[str]` — ID of a browser profile to reuse for this workflow run
    
</dd>
</dl>

<dl>
<dd>

**max_screenshot_scrolls:** `typing.Optional[int]` — The maximum number of scrolls for the post action screenshot. When it's None or 0, it takes the current viewpoint screenshot.
    
</dd>
</dl>

<dl>
<dd>

**max_elapsed_time_minutes:** `typing.Optional[int]` — Timeout this workflow run after the configured elapsed runtime in minutes. When omitted, the platform default is 240 minutes. The maximum configurable value is 480 minutes.
    
</dd>
</dl>

<dl>
<dd>

**extra_http_headers:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — The extra HTTP headers for the requests in browser.
    
</dd>
</dl>

<dl>
<dd>

**cdp_connect_headers:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — HTTP headers attached ONLY to the CDP WebSocket handshake when connecting to a remote browser via browser_address. Use this for browser-provider auth (e.g., x-api-key for Skyvern Cloud, Browserless, or similar). These headers are NEVER forwarded to target websites.
    
</dd>
</dl>

<dl>
<dd>

**browser_address:** `typing.Optional[str]` — The CDP address for the workflow run.
    
</dd>
</dl>

<dl>
<dd>

**ai_fallback:** `typing.Optional[bool]` — Whether to fallback to AI if the workflow run fails.
    
</dd>
</dl>

<dl>
<dd>

**run_with:** `typing.Optional[str]` — Whether to run the workflow with agent or code. Null inherits from the workflow setting.
    
</dd>
</dl>

<dl>
<dd>

**run_metadata:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — String key/value metadata to attach to this workflow run for analytics tag filtering.
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_run</a>(...) -> GetRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get run information (task run, workflow run)
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_run(
    run_id="tsk_123",
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

**run_id:** `str` — The id of the task run or the workflow run.
    
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

<details><summary><code>client.<a href="src/fern/client.py">cancel_run</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel a run (task or workflow)
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
    environment=FernApiEnvironment.CLOUD,
)

client.cancel_run(
    run_id="run_id",
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

**run_id:** `str` — The id of the task run or the workflow run to cancel.
    
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

<details><summary><code>client.<a href="src/fern/client.py">bulk_cancel_runs</a>(...) -> BulkCancelRunsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel multiple runs (tasks or workflows) in a single request
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
    environment=FernApiEnvironment.CLOUD,
)

client.bulk_cancel_runs(
    run_ids=[
        "run_ids"
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

**run_ids:** `typing.List[str]` — List of run IDs to cancel
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_workflows</a>(...) -> typing.List[Workflow]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all workflows with the latest version for the organization.

Search semantics:
- If `search_key` is provided, its value is used as a unified search term for
  `workflows.title`, `folders.title`, and workflow parameter metadata (key, description, and default_value for
  `WorkflowParameterModel`).
- Falls back to deprecated `title` (title-only search) if `search_key` is not provided.
- Parameter metadata search excludes soft-deleted parameter rows across all parameter tables.
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_workflows()

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

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**only_saved_tasks:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**only_workflows:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**only_templates:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**search_key:** `typing.Optional[str]` — Case-insensitive substring search across: workflow title, folder name, and parameter metadata (key, description, default_value). A workflow is returned if any of these fields match. Soft-deleted parameter definitions are excluded. Takes precedence over the deprecated `title` parameter.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Deprecated: use search_key instead. Falls back to title-only search if search_key is not provided.
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` — Filter workflows by folder ID
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[WorkflowStatus]]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — Filter by tags. Each term is a label (`production`), a group (`env:*`), or a group:label (`env:prod`). Repeat the param or comma-separate (`?tags=env:prod,env:staging`). AND across distinct terms, OR within a group's labels (`?tags=customer:acme,env:prod,env:staging` -> customer=acme AND env in (prod, staging)). A label term matches the value across any/no group. Matches current tag values only. Not supported with `template=true`.
    
</dd>
</dl>

<dl>
<dd>

**template:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">create_workflow</a>(...) -> Workflow</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new agent
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
    environment=FernApiEnvironment.CLOUD,
)

client.create_workflow()

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

**request:** `WorkflowRequest` 
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` — Optional folder ID to assign the workflow to
    
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

<details><summary><code>client.<a href="src/fern/client.py">update_workflow</a>(...) -> Workflow</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an agent
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
    environment=FernApiEnvironment.CLOUD,
)

client.update_workflow(
    workflow_id="wpid_123",
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

**workflow_id:** `str` — The ID of the agent to update. Starts with `wpid_`.
    
</dd>
</dl>

<dl>
<dd>

**request:** `WorkflowRequest` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_workflow</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an agent
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
    environment=FernApiEnvironment.CLOUD,
)

client.delete_workflow(
    workflow_id="wpid_123",
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

**workflow_id:** `str` — The ID of the agent to delete. Starts with `wpid_`.
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_folders</a>(...) -> typing.List[Folder]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all folders for the organization
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_folders()

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

**page:** `typing.Optional[int]` — Page number
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of folders per page
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search folders by title or description
    
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

<details><summary><code>client.<a href="src/fern/client.py">create_folder</a>(...) -> Folder</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new folder to organize workflows
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
    environment=FernApiEnvironment.CLOUD,
)

client.create_folder(
    title="title",
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

**title:** `str` — Folder title
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Folder description
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_folder</a>(...) -> Folder</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific folder by ID
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_folder(
    folder_id="fld_123",
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

**folder_id:** `str` — Folder ID
    
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

<details><summary><code>client.<a href="src/fern/client.py">update_folder</a>(...) -> Folder</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a folder's title or description
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
    environment=FernApiEnvironment.CLOUD,
)

client.update_folder(
    folder_id="fld_123",
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

**folder_id:** `str` — Folder ID
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Folder title
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Folder description
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_folder</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a folder. Optionally delete all workflows in the folder.
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
    environment=FernApiEnvironment.CLOUD,
)

client.delete_folder(
    folder_id="fld_123",
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

**folder_id:** `str` — Folder ID
    
</dd>
</dl>

<dl>
<dd>

**delete_workflows:** `typing.Optional[bool]` — If true, also delete all workflows in this folder
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_run_tags</a>(...) -> RunTagsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the current tag state for a workflow run.
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_run_tags(
    workflow_run_id="wr_123",
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

**workflow_run_id:** `str` — Workflow run ID
    
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

<details><summary><code>client.<a href="src/fern/client.py">apply_run_tags</a>(...) -> RunTagsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Atomically apply tag changes to a workflow run. Sets and deletes happen in one transaction; same-key collisions resolve set-wins.
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
    environment=FernApiEnvironment.CLOUD,
)

client.apply_run_tags(
    workflow_run_id="wr_123",
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

**workflow_run_id:** `str` — Workflow run ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `TagApplyRequest` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_run_tag</a>(...) -> RunTagsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft-delete a single grouped tag from a workflow run. Writes a DELETE event row.
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
    environment=FernApiEnvironment.CLOUD,
)

client.delete_run_tag(
    workflow_run_id="wr_123",
    key="env",
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

**workflow_run_id:** `str` — Workflow run ID
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Tag key to delete
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_run_tag_history</a>(...) -> RunTagHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Chronological tag-event log for a workflow run (newest first). Includes SET and DELETE events.
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_run_tag_history(
    workflow_run_id="wr_123",
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

**workflow_run_id:** `str` — Workflow run ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max events to return
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[datetime.datetime]` — Only return events at or after this timestamp
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` — Filter to events for a single tag key
    
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

<details><summary><code>client.<a href="src/fern/client.py">list_tag_keys</a>() -> typing.List[TagKey]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all tag keys registered for the organization with their descriptions.
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
    environment=FernApiEnvironment.CLOUD,
)

client.list_tag_keys()

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

<details><summary><code>client.<a href="src/fern/client.py">delete_tag_key</a>(...) -> TagKeyDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a tag key from the organization registry and remove that tag from every workflow that currently has it (cascade). Returns how many workflows the tag was removed from.
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
    environment=FernApiEnvironment.CLOUD,
)

client.delete_tag_key(
    key="env",
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

**key:** `str` — Tag key to delete
    
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

<details><summary><code>client.<a href="src/fern/client.py">update_tag_key</a>(...) -> TagKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the description for a tag key.
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
    environment=FernApiEnvironment.CLOUD,
)

client.update_tag_key(
    key="key",
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

**key:** `str` — Tag key to update
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Free-form description (max 500 chars). Pass null to clear.
    
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

<details><summary><code>client.<a href="src/fern/client.py">list_tag_values</a>(...) -> typing.List[TagValue]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the palette color and current workflow usage count for each grouped tag (key, value) for the organization. The frontend joins these onto tags by (key, value); workflow_count is the number of non-deleted workflows carrying the label and powers the per-label usage and delete blast-radius warnings.
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
    environment=FernApiEnvironment.CLOUD,
)

client.list_tag_values()

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

**key:** `typing.Optional[str]` — Filter to values for a single tag key
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_tag_value</a>(...) -> TagValueDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft-delete a grouped tag (key, value) and remove that label from every workflow carrying it (cascade). The value rides in the body so values containing '/' stay addressable. Returns how many workflows the label was removed from.
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
    environment=FernApiEnvironment.CLOUD,
)

client.delete_tag_value(
    key="env",
    value="value",
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

**key:** `str` — Tag key (group)
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — Tag value (label) under the key to soft-delete.
    
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

<details><summary><code>client.<a href="src/fern/client.py">update_tag_value</a>(...) -> TagValue</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Recolor a grouped tag (key, value). The value is supplied in the body so values containing '/' stay addressable. The new color must be a palette name.
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
    environment=FernApiEnvironment.CLOUD,
)

client.update_tag_value(
    key="env",
    value="value",
    color="color",
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

**key:** `str` — Tag key (group)
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — Tag value (label) under the key to recolor.
    
</dd>
</dl>

<dl>
<dd>

**color:** `str` — Palette color name to assign to this (key, value).
    
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

<details><summary><code>client.<a href="src/fern/client.py">rename_tag_value</a>(...) -> TagValueRenameResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rename a grouped tag (key, value) to (key, new_value). The cascade re-tags every workflow carrying the old label; the new label inherits the old color. Both values ride in the body so values containing '/' stay addressable. Rejects with 409 when the new value already exists for the key.
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
    environment=FernApiEnvironment.CLOUD,
)

client.rename_tag_value(
    key="env",
    value="value",
    new_value="new_value",
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

**key:** `str` — Tag key (group)
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — Current tag value (label) under the key to rename.
    
</dd>
</dl>

<dl>
<dd>

**new_value:** `str` — New tag value (label) to rename it to.
    
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

<details><summary><code>client.<a href="src/fern/client.py">batch_get_workflow_tags</a>(...) -> WorkflowTagsBatchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Batch fetch current tags for many workflows. Avoids N+1 on the workflows-list page.
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
    environment=FernApiEnvironment.CLOUD,
)

client.batch_get_workflow_tags()

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

**workflow_permanent_ids:** `typing.Optional[str]` — Comma-separated workflow permanent IDs
    
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

<details><summary><code>client.<a href="src/fern/client.py">batch_get_workflow_tags_post</a>(...) -> WorkflowTagsBatchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Batch fetch current tags for many workflows (POST variant for id lists exceeding URL length).
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
    environment=FernApiEnvironment.CLOUD,
)

client.batch_get_workflow_tags_post()

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

**workflow_permanent_ids:** `typing.Optional[typing.List[str]]` — Workflow permanent IDs to fetch tags for.
    
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

<details><summary><code>client.<a href="src/fern/client.py">batch_get_run_tags</a>(...) -> RunTagsBatchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Batch fetch current tags for many workflow runs. Avoids N+1 on run-list pages.
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
    environment=FernApiEnvironment.CLOUD,
)

client.batch_get_run_tags()

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

**workflow_run_ids:** `typing.Optional[str]` — Comma-separated workflow run IDs
    
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

<details><summary><code>client.<a href="src/fern/client.py">batch_get_run_tags_post</a>(...) -> RunTagsBatchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Batch fetch current tags for many workflow runs (POST variant for id lists exceeding URL length).
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
    environment=FernApiEnvironment.CLOUD,
)

client.batch_get_run_tags_post()

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

**workflow_run_ids:** `typing.Optional[typing.List[str]]` — Workflow run IDs to fetch tags for.
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_run_artifacts</a>(...) -> typing.List[Artifact]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get artifacts for a run
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_run_artifacts(
    run_id="run_id",
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

**run_id:** `str` — The id of the task run or the workflow run.
    
</dd>
</dl>

<dl>
<dd>

**artifact_type:** `typing.Optional[typing.List[ArtifactType]]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">retry_run_webhook</a>(...) -> RunWebhookReplayResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retry sending the webhook for a run
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
from fern import FernApi, RetryRunWebhookRequest
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.CLOUD,
)

client.retry_run_webhook(
    run_id="tsk_123",
    request=RetryRunWebhookRequest(),
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

**run_id:** `str` — The id of the task run or the workflow run.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[RetryRunWebhookRequest]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_run_timeline</a>(...) -> typing.List[WorkflowRunTimeline]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get timeline for a run (workflow run or task_v2 run)
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_run_timeline(
    run_id="wr_123",
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

**run_id:** `str` — The id of the workflow run or task_v2 run.
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_version</a>() -> typing.Dict[str, str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current Skyvern server version (git SHA for official builds).
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_version()

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

<details><summary><code>client.<a href="src/fern/client.py">get_runs_v2</a>(...) -> typing.List[TaskRunListItem]</code></summary>
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_runs_v2()

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

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[RunStatus]]` 
    
</dd>
</dl>

<dl>
<dd>

**search_key:** `typing.Optional[str]` — Case-insensitive substring search (min 3 chars for trigram index).
    
</dd>
</dl>

<dl>
<dd>

**run_type:** `typing.Optional[typing.List[RunType]]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">upload_file</a>(...) -> UploadFileResponse</code></summary>
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
    environment=FernApiEnvironment.CLOUD,
)

client.upload_file(
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

<details><summary><code>client.<a href="src/fern/client.py">list_browser_profiles</a>(...) -> typing.List[BrowserProfile]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all browser profiles for the organization
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
    environment=FernApiEnvironment.CLOUD,
)

client.list_browser_profiles()

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

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**include_deleted:** `typing.Optional[bool]` — Include deleted browser profiles
    
</dd>
</dl>

<dl>
<dd>

**search_key:** `typing.Optional[str]` — Case-insensitive substring search across: browser profile name and description. A profile is returned if either field matches.
    
</dd>
</dl>

<dl>
<dd>

**managed:** `typing.Optional[bool]` — Omit to return all profiles; false returns only user-created profiles; true returns only auto-managed profiles.
    
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

<details><summary><code>client.<a href="src/fern/client.py">create_browser_profile</a>(...) -> BrowserProfile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a blank browser profile, or create one from a persistent browser session or workflow run.
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
    environment=FernApiEnvironment.CLOUD,
)

client.create_browser_profile(
    name="name",
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

**name:** `str` — Name for the browser profile
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional profile description
    
</dd>
</dl>

<dl>
<dd>

**browser_session_id:** `typing.Optional[str]` — Persistent browser session to convert into a profile. Omit for a blank profile.
    
</dd>
</dl>

<dl>
<dd>

**workflow_run_id:** `typing.Optional[str]` — Workflow run whose persisted session should be captured. Omit for a blank profile.
    
</dd>
</dl>

<dl>
<dd>

**proxy_location:** `typing.Optional[CreateBrowserProfileRequestProxyLocation]` — Optional proxy location for this profile's pinned proxy identity.
    
</dd>
</dl>

<dl>
<dd>

**proxy_session_id:** `typing.Optional[str]` — Explicit sticky-session id for this profile's pinned proxy identity.
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_browser_profile</a>(...) -> BrowserProfile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific browser profile by ID
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_browser_profile(
    profile_id="bp_123456",
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

**profile_id:** `str` — The ID of the browser profile. browser_profile_id starts with `bp_`
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_browser_profile</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a browser profile (soft delete)
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
    environment=FernApiEnvironment.CLOUD,
)

client.delete_browser_profile(
    profile_id="bp_123456",
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

**profile_id:** `str` — The ID of the browser profile to delete. browser_profile_id starts with `bp_`
    
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

<details><summary><code>client.<a href="src/fern/client.py">update_browser_profile</a>(...) -> BrowserProfile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a browser profile's name and/or description
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
    environment=FernApiEnvironment.CLOUD,
)

client.update_browser_profile(
    profile_id="bp_123456",
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

**profile_id:** `str` — The ID of the browser profile to update. browser_profile_id starts with `bp_`
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — New name for the browser profile
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — New description for the browser profile
    
</dd>
</dl>

<dl>
<dd>

**proxy_location:** `typing.Optional[UpdateBrowserProfileRequestProxyLocation]` — Optional proxy location for this profile's pinned proxy identity.
    
</dd>
</dl>

<dl>
<dd>

**proxy_session_id:** `typing.Optional[str]` — Opaque Skyvern-managed proxy sticky-session id.
    
</dd>
</dl>

<dl>
<dd>

**rotate_proxy_session_id:** `typing.Optional[bool]` — Rotate the Skyvern-managed proxy sticky-session id for this profile.
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_browser_sessions</a>() -> typing.List[BrowserSessionResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all active browser sessions for the organization
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_browser_sessions()

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

<details><summary><code>client.<a href="src/fern/client.py">create_browser_session</a>(...) -> BrowserSessionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a browser session that persists across multiple runs
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
    environment=FernApiEnvironment.CLOUD,
)

client.create_browser_session()

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

**url:** `typing.Optional[str]` — Optional URL to open when the standalone browser session starts.
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[int]` — Timeout in minutes for the session. Timeout is applied after the session is started. Must be between 5 and 240. Defaults to 60.
    
</dd>
</dl>

<dl>
<dd>

**proxy_location:** `typing.Optional[CreateBrowserSessionRequestProxyLocation]` 


Geographic Proxy location to route the browser traffic through. This is only available in Skyvern Cloud.

Available geotargeting options:
- RESIDENTIAL: the default value. Skyvern Cloud uses a random US residential proxy.
- RESIDENTIAL_ES: Spain
- RESIDENTIAL_IE: Ireland
- RESIDENTIAL_GB: United Kingdom
- RESIDENTIAL_IN: India
- RESIDENTIAL_JP: Japan
- RESIDENTIAL_FR: France
- RESIDENTIAL_DE: Germany
- RESIDENTIAL_NZ: New Zealand
- RESIDENTIAL_PH: Philippines
- RESIDENTIAL_KR: South Korea
- RESIDENTIAL_SA: Saudi Arabia
- RESIDENTIAL_ZA: South Africa
- RESIDENTIAL_AR: Argentina
- RESIDENTIAL_AU: Australia
- RESIDENTIAL_BR: Brazil
- RESIDENTIAL_TR: Turkey
- RESIDENTIAL_CA: Canada
- RESIDENTIAL_MX: Mexico
- RESIDENTIAL_IT: Italy
- RESIDENTIAL_NL: Netherlands
- RESIDENTIAL_ISP: ISP proxy
- US-CA: California (deprecated, routes through RESIDENTIAL_ISP)
- US-NY: New York (deprecated, routes through RESIDENTIAL_ISP)
- US-TX: Texas (deprecated, routes through RESIDENTIAL_ISP)
- US-FL: Florida (deprecated, routes through RESIDENTIAL_ISP)
- US-WA: Washington (deprecated, routes through RESIDENTIAL_ISP)
- NONE: No proxy

For self-hosted deployments, you can pass a custom proxy URL as a dict: {"url": "http://user:password@proxy.example.com:8080"}. This routes the browser through your own proxy server and takes precedence over any globally configured proxy pool.
 Can also be a GeoTarget object for granular city/state targeting: {"country": "US", "subdivision": "CA", "city": "San Francisco"}, or a custom proxy URL dict for self-hosted deployments: {"url": "http://user:password@proxy.example.com:8080"}
    
</dd>
</dl>

<dl>
<dd>

**proxy_session_id:** `typing.Optional[str]` — Opaque Skyvern-managed proxy sticky-session id for pinned Residential ISP sessions.
    
</dd>
</dl>

<dl>
<dd>

**extensions:** `typing.Optional[typing.List[Extensions]]` — A list of extensions to install in the browser session.
    
</dd>
</dl>

<dl>
<dd>

**browser_type:** `typing.Optional[PersistentBrowserType]` — The type of browser to use for the session.
    
</dd>
</dl>

<dl>
<dd>

**browser_profile_id:** `typing.Optional[str]` — ID of a browser profile to load into this session (restores cookies, localStorage, etc.). browser_profile_id starts with `bp_`.
    
</dd>
</dl>

<dl>
<dd>

**generate_browser_profile:** `typing.Optional[bool]` — When true, the session's browser profile (cookies, localStorage, etc.) is saved to storage when the session ends so it can be turned into a reusable browser profile. Defaults to false to avoid storing profiles for sessions that never need them. Sessions started with a browser_profile_id always persist their profile regardless of this flag.
    
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

<details><summary><code>client.<a href="src/fern/client.py">close_browser_session</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Close a session. Once closed, the session cannot be used again.
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
    environment=FernApiEnvironment.CLOUD,
)

client.close_browser_session(
    browser_session_id="pbs_123456",
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

**browser_session_id:** `str` — The ID of the browser session to close. completed_at will be set when the browser session is closed. browser_session_id starts with `pbs_`
    
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

<details><summary><code>client.<a href="src/fern/client.py">extend_browser_session</a>(...) -> BrowserSessionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Extend a live browser session by a number of minutes. Sessions are created with a timeout of at most 240 minutes and can be extended, one or more times, up to a total lifetime of 360 minutes (6 hours). The minutes are added to the session's current deadline. A request for more than the remaining headroom is granted the remainder, and the response carries a warning. The response's `timeout` is the session's new total budget in minutes, counted from when the session started.
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
    environment=FernApiEnvironment.CLOUD,
)

client.extend_browser_session(
    browser_session_id="pbs_123456",
    additional_minutes=1,
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

**browser_session_id:** `str` — The ID of the browser session. browser_session_id starts with `pbs_`
    
</dd>
</dl>

<dl>
<dd>

**additional_minutes:** `int` — Minutes to add to the session's current deadline. A session can be extended, one or more times, up to a total lifetime of 360 minutes (6 hours) counted from when it started; a request for more than the remaining headroom is granted the remainder and the response carries a warning.
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_browser_session</a>(...) -> BrowserSessionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details about a specific browser session, including the browser address for cdp connection.
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_browser_session(
    browser_session_id="pbs_123456",
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

**browser_session_id:** `str` — The ID of the browser session. browser_session_id starts with `pbs_`
    
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

<details><summary><code>client.<a href="src/fern/client.py">update_browser_session</a>(...) -> BrowserSessionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a live browser session. Currently supports toggling generate_browser_profile, which is read when the session ends to decide whether to save its browser profile.
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
    environment=FernApiEnvironment.CLOUD,
)

client.update_browser_session(
    browser_session_id="pbs_123456",
    generate_browser_profile=True,
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

**browser_session_id:** `str` — The ID of the browser session. browser_session_id starts with `pbs_`
    
</dd>
</dl>

<dl>
<dd>

**generate_browser_profile:** `bool` — Enable or disable saving this session's browser profile when it ends. Can be toggled while the session is still alive; the value is read at session teardown.
    
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

<details><summary><code>client.<a href="src/fern/client.py">send_totp_code</a>(...) -> TotpCode</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Forward a TOTP (2FA, MFA) email or sms message containing the code to Skyvern. This endpoint stores the code in database so that Skyvern can use it while running tasks/workflows.
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
    environment=FernApiEnvironment.CLOUD,
)

client.send_totp_code(
    totp_identifier="john.doe@example.com",
    content="Hello, your verification code is 123456",
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

**totp_identifier:** `str` — The identifier of the TOTP code. It can be the email address, phone number, or the identifier of the user.
    
</dd>
</dl>

<dl>
<dd>

**content:** `str` — The content of the TOTP code. It can be the email content that contains the TOTP code, or the sms message that contains the TOTP code. Skyvern will automatically extract the TOTP code from the content.
    
</dd>
</dl>

<dl>
<dd>

**task_id:** `typing.Optional[str]` — The task_id the totp code is for. It can be the task_id of the task that the TOTP code is for.
    
</dd>
</dl>

<dl>
<dd>

**workflow_id:** `typing.Optional[str]` — The workflow ID the TOTP code is for. It can be the workflow ID of the workflow that the TOTP code is for.
    
</dd>
</dl>

<dl>
<dd>

**workflow_run_id:** `typing.Optional[str]` — The workflow run id that the TOTP code is for. It can be the workflow run id of the workflow run that the TOTP code is for.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` — An optional field. The source of the TOTP code. e.g. email, sms, etc.
    
</dd>
</dl>

<dl>
<dd>

**expired_at:** `typing.Optional[datetime.datetime]` — The timestamp when the TOTP code expires
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[OtpType]` — Deprecated compatibility field. Skyvern auto-detects the OTP type from content, so this value does not constrain extraction.
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_credentials</a>(...) -> typing.List[CredentialResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a paginated list of credentials for the current organization
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_credentials(
    page=1,
    page_size=10,
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

**page:** `typing.Optional[int]` — Page number for pagination
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items per page
    
</dd>
</dl>

<dl>
<dd>

**vault_type:** `typing.Optional[CredentialVaultType]` — Filter credentials by vault type (e.g. 'skyvern', 'custom', 'bitwarden', 'azure_vault')
    
</dd>
</dl>

<dl>
<dd>

**credential_type:** `typing.Optional[SkyvernForgeSdkSchemasCredentialsCredentialType]` — Filter credentials by type (e.g. 'password', 'credit_card', 'secret')
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Case-insensitive search across credential name, username, secret label, and card details
    
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

<details><summary><code>client.<a href="src/fern/client.py">create_credential</a>(...) -> CredentialResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new credential for the current organization
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
from fern import FernApi, NonEmptyPasswordCredential
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.CLOUD,
)

client.create_credential(
    name="Amazon Login",
    credential_type="password",
    credential=NonEmptyPasswordCredential(
        password="securepassword123",
        username="user@example.com",
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

**request:** `CreateCredentialRequest` — The credential data to create
    
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

<details><summary><code>client.<a href="src/fern/client.py">update_credential</a>(...) -> CredentialResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Overwrites the stored credential data (e.g. username/password) while keeping the same credential_id.
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
from fern import FernApi, NonEmptyPasswordCredential
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.CLOUD,
)

client.update_credential(
    credential_id="cred_1234567890",
    name="Amazon Login",
    credential_type="password",
    credential=NonEmptyPasswordCredential(
        password="securepassword123",
        username="user@example.com",
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

**credential_id:** `str` — The unique identifier of the credential to update
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateCredentialRequest` — The new credential data to store
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_credential</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a specific credential by its ID
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
    environment=FernApiEnvironment.CLOUD,
)

client.delete_credential(
    credential_id="cred_1234567890",
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

**credential_id:** `str` — The unique identifier of the credential to delete
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_credential</a>(...) -> CredentialResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a specific credential by its ID
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_credential(
    credential_id="cred_1234567890",
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

**credential_id:** `str` — The unique identifier of the credential
    
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

<details><summary><code>client.<a href="src/fern/client.py">list_custom_llms</a>() -> CustomLlmListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the custom LLM configurations available to the current organization.
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
    environment=FernApiEnvironment.CLOUD,
)

client.list_custom_llms()

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

<details><summary><code>client.<a href="src/fern/client.py">create_custom_llm</a>(...) -> CustomLlmResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a custom LLM configuration for the current organization.
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
from fern import FernApi, CustomLlmConfig
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.CLOUD,
)

client.create_custom_llm(
    config=CustomLlmConfig(
        display_name="display_name",
        provider="openai_compatible",
        model_name="model_name",
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

**config:** `CustomLlmConfig` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">update_custom_llm</a>(...) -> CustomLlmResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a custom LLM configuration for the current organization.
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
from fern import FernApi, CustomLlmConfig
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.CLOUD,
)

client.update_custom_llm(
    custom_llm_id="custom_llm_id",
    config=CustomLlmConfig(
        display_name="display_name",
        provider="openai_compatible",
        model_name="model_name",
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

**custom_llm_id:** `str` — The custom LLM id.
    
</dd>
</dl>

<dl>
<dd>

**config:** `CustomLlmConfig` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_custom_llm</a>(...) -> ClearOrganizationAuthTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a custom LLM configuration for the current organization.
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
    environment=FernApiEnvironment.CLOUD,
)

client.delete_custom_llm(
    custom_llm_id="custom_llm_id",
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

**custom_llm_id:** `str` — The custom LLM id.
    
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

<details><summary><code>client.<a href="src/fern/client.py">login</a>(...) -> WorkflowRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Log in to a website using either credential stored in Skyvern, Bitwarden, 1Password, or Azure Vault
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
    environment=FernApiEnvironment.CLOUD,
)

client.login(
    credential_type="skyvern",
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

**credential_type:** `SkyvernSchemasCredentialTypeCredentialType` — Where to get the credential from
    
</dd>
</dl>

<dl>
<dd>

**user_agent:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — Website URL
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — Webhook URL to send status updates
    
</dd>
</dl>

<dl>
<dd>

**proxy_location:** `typing.Optional[ProxyLocation]` — Proxy location to use
    
</dd>
</dl>

<dl>
<dd>

**totp_identifier:** `typing.Optional[str]` — Identifier for TOTP (Time-based One-Time Password) if required
    
</dd>
</dl>

<dl>
<dd>

**totp_url:** `typing.Optional[str]` — TOTP URL to fetch one-time passwords
    
</dd>
</dl>

<dl>
<dd>

**browser_session_id:** `typing.Optional[str]` — ID of the browser session to use, which is prefixed by `pbs_` e.g. `pbs_123456`
    
</dd>
</dl>

<dl>
<dd>

**browser_profile_id:** `typing.Optional[str]` — ID of a browser profile to reuse for this run
    
</dd>
</dl>

<dl>
<dd>

**browser_address:** `typing.Optional[str]` — The CDP address for the task.
    
</dd>
</dl>

<dl>
<dd>

**extra_http_headers:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Additional HTTP headers to include in requests
    
</dd>
</dl>

<dl>
<dd>

**cdp_connect_headers:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — HTTP headers attached ONLY to the CDP WebSocket handshake when connecting to a remote browser via browser_address. Never forwarded to target websites.
    
</dd>
</dl>

<dl>
<dd>

**max_screenshot_scrolling_times:** `typing.Optional[int]` — Maximum number of times to scroll for screenshots
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` — Login instructions. Skyvern has default prompt/instruction for login if this field is not provided.
    
</dd>
</dl>

<dl>
<dd>

**credential_id:** `typing.Optional[str]` — ID of the Skyvern credential to use for login.
    
</dd>
</dl>

<dl>
<dd>

**bitwarden_collection_id:** `typing.Optional[str]` — Bitwarden collection ID. You can find it in the Bitwarden collection URL. e.g. `https://vault.bitwarden.com/vaults/collection_id/items`
    
</dd>
</dl>

<dl>
<dd>

**bitwarden_item_id:** `typing.Optional[str]` — Bitwarden item ID
    
</dd>
</dl>

<dl>
<dd>

**onepassword_vault_id:** `typing.Optional[str]` — 1Password vault ID
    
</dd>
</dl>

<dl>
<dd>

**onepassword_item_id:** `typing.Optional[str]` — 1Password item ID
    
</dd>
</dl>

<dl>
<dd>

**azure_vault_name:** `typing.Optional[str]` — Azure Vault Name
    
</dd>
</dl>

<dl>
<dd>

**azure_vault_username_key:** `typing.Optional[str]` — Azure Vault username key
    
</dd>
</dl>

<dl>
<dd>

**azure_vault_password_key:** `typing.Optional[str]` — Azure Vault password key
    
</dd>
</dl>

<dl>
<dd>

**azure_vault_totp_secret_key:** `typing.Optional[str]` — Azure Vault TOTP secret key
    
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

<details><summary><code>client.<a href="src/fern/client.py">download_files</a>(...) -> WorkflowRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download a file from a website by navigating and clicking download buttons
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
    environment=FernApiEnvironment.CLOUD,
)

client.download_files(
    navigation_goal="navigation_goal",
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

**navigation_goal:** `str` — Instructions for navigating to and downloading the file
    
</dd>
</dl>

<dl>
<dd>

**user_agent:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — Website URL
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — Webhook URL to send status updates
    
</dd>
</dl>

<dl>
<dd>

**proxy_location:** `typing.Optional[ProxyLocation]` — Proxy location to use
    
</dd>
</dl>

<dl>
<dd>

**totp_identifier:** `typing.Optional[str]` — Identifier for TOTP (Time-based One-Time Password) if required
    
</dd>
</dl>

<dl>
<dd>

**totp_url:** `typing.Optional[str]` — TOTP URL to fetch one-time passwords
    
</dd>
</dl>

<dl>
<dd>

**browser_session_id:** `typing.Optional[str]` — ID of the browser session to use, which is prefixed by `pbs_` e.g. `pbs_123456`
    
</dd>
</dl>

<dl>
<dd>

**browser_profile_id:** `typing.Optional[str]` — ID of a browser profile to reuse for this run
    
</dd>
</dl>

<dl>
<dd>

**browser_address:** `typing.Optional[str]` — The CDP address for the task.
    
</dd>
</dl>

<dl>
<dd>

**extra_http_headers:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Additional HTTP headers to include in requests
    
</dd>
</dl>

<dl>
<dd>

**cdp_connect_headers:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — HTTP headers attached ONLY to the CDP WebSocket handshake when connecting to a remote browser via browser_address. Never forwarded to target websites.
    
</dd>
</dl>

<dl>
<dd>

**max_screenshot_scrolling_times:** `typing.Optional[int]` — Maximum number of times to scroll for screenshots
    
</dd>
</dl>

<dl>
<dd>

**download_suffix:** `typing.Optional[str]` — Suffix or complete filename for the downloaded file
    
</dd>
</dl>

<dl>
<dd>

**download_timeout:** `typing.Optional[float]` — Timeout in seconds for the download operation
    
</dd>
</dl>

<dl>
<dd>

**max_steps_per_run:** `typing.Optional[int]` — Maximum number of steps to execute
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_scripts</a>(...) -> typing.List[Script]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a paginated list of scripts for the current organization
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_scripts(
    page=1,
    page_size=10,
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

**page:** `typing.Optional[int]` — Page number for pagination
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items per page
    
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

<details><summary><code>client.<a href="src/fern/client.py">create_script</a>(...) -> CreateScriptResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new script with optional files and metadata
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
    environment=FernApiEnvironment.CLOUD,
)

client.create_script()

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

**workflow_id:** `typing.Optional[str]` — Associated workflow ID
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `typing.Optional[str]` — Associated run ID
    
</dd>
</dl>

<dl>
<dd>

**files:** `typing.Optional[typing.List[ScriptFileCreate]]` — Array of files to include in the script
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_script</a>(...) -> Script</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a specific script by its ID
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_script(
    script_id="s_abc123",
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

**script_id:** `str` — The unique identifier of the script
    
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

<details><summary><code>client.<a href="src/fern/client.py">deploy_script</a>(...) -> CreateScriptResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deploy a script with updated files, creating a new version
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
from fern import FernApi, ScriptFileCreate
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.CLOUD,
)

client.deploy_script(
    script_id="s_abc123",
    files=[
        ScriptFileCreate(
            path="src/main.py",
            content="content",
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

**script_id:** `str` — The unique identifier of the script
    
</dd>
</dl>

<dl>
<dd>

**files:** `typing.List[ScriptFileCreate]` — Array of files to include in the script
    
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

<details><summary><code>client.<a href="src/fern/client.py">run_sdk_action</a>(...) -> RunSdkActionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a single SDK action with the specified parameters
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
from fern import FernApi, RunSdkActionRequestAction_AiAct
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.CLOUD,
)

client.run_sdk_action(
    url="url",
    action=RunSdkActionRequestAction_AiAct(),
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

**url:** `str` — The URL where the action should be executed
    
</dd>
</dl>

<dl>
<dd>

**action:** `RunSdkActionRequestAction` — The action to execute with its specific parameters
    
</dd>
</dl>

<dl>
<dd>

**browser_session_id:** `typing.Optional[str]` — The browser session ID
    
</dd>
</dl>

<dl>
<dd>

**browser_address:** `typing.Optional[str]` — The browser address
    
</dd>
</dl>

<dl>
<dd>

**workflow_run_id:** `typing.Optional[str]` — Optional workflow run ID to continue an existing workflow run
    
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

<details><summary><code>client.<a href="src/fern/client.py">update_workflow_folder</a>(...) -> Workflow</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a workflow's folder assignment for the latest version
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
    environment=FernApiEnvironment.CLOUD,
)

client.update_workflow_folder(
    workflow_permanent_id="wpid_123",
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

**workflow_permanent_id:** `str` — Workflow permanent ID
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` — Folder ID to assign workflow to. Set to null to remove from folder.
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_workflow_tags</a>(...) -> TagsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the current tag state for a workflow.
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_workflow_tags(
    workflow_permanent_id="wpid_123",
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

**workflow_permanent_id:** `str` — Workflow permanent ID
    
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

<details><summary><code>client.<a href="src/fern/client.py">apply_workflow_tags</a>(...) -> TagsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Atomically apply tag changes to a workflow. Sets and deletes happen in one transaction; same-key collisions resolve set-wins.
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
    environment=FernApiEnvironment.CLOUD,
)

client.apply_workflow_tags(
    workflow_permanent_id="wpid_123",
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

**workflow_permanent_id:** `str` — Workflow permanent ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `TagApplyRequest` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">delete_workflow_tag</a>(...) -> TagsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft-delete a single tag from a workflow. Writes a DELETE event row.
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
    environment=FernApiEnvironment.CLOUD,
)

client.delete_workflow_tag(
    workflow_permanent_id="wpid_123",
    key="env",
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

**workflow_permanent_id:** `str` — Workflow permanent ID
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Tag key to delete
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_workflow_tag_history</a>(...) -> TagHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Chronological tag-event log for a workflow (newest first). Includes SET and DELETE events.
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_workflow_tag_history(
    workflow_permanent_id="wpid_123",
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

**workflow_permanent_id:** `str` — Workflow permanent ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max events to return
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[datetime.datetime]` — Only return events at or after this timestamp
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` — Filter to events for a single tag key
    
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

<details><summary><code>client.<a href="src/fern/client.py">retry_workflow_run</a>(...) -> WorkflowRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retry a workflow run using the original run parameters.
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
    environment=FernApiEnvironment.CLOUD,
)

client.retry_workflow_run(
    workflow_run_id="wr_123",
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

**workflow_run_id:** `str` — The id of the workflow run to retry.
    
</dd>
</dl>

<dl>
<dd>

**max_steps_override:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**user_agent:** `typing.Optional[str]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_workflow_runs</a>(...) -> typing.List[WorkflowRun]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List workflow runs across all workflows for the current organization.

Results are paginated and can be filtered by **status**, **search_key**, and **error_code**. All filters are combined with **AND** logic — a run must match every supplied filter to be returned.

### search_key

A case-insensitive substring search that matches against **any** of the following fields:

| Searched field | Description |
|---|---|
| `workflow_run_id` | The unique run identifier (e.g. `wr_123…`) |
| Parameter **key** | The `key` of any workflow parameter definition associated with the run |
| Parameter **description** | The `description` of any workflow parameter definition |
| Run parameter **value** | The actual value supplied for any parameter when the run was created |
| `extra_http_headers` | Extra HTTP headers attached to the run (searched as raw JSON text) |

Soft-deleted parameter definitions are excluded from key/description matching. A run is returned if **any** of the fields above contain the search term.

### error_code

An **exact-match** filter against the `error_code` field inside each task's `errors` JSON array. A run matches if **any** of its tasks contains an error object with a matching `error_code` value. Error codes are user-defined strings set during workflow execution (e.g. `INVALID_CREDENTIALS`, `LOGIN_FAILED`, `CAPTCHA_DETECTED`).

### Combining filters

All query parameters use AND logic:
- `?status=failed` — only failed runs
- `?status=failed&error_code=LOGIN_FAILED` — failed runs **and** have a LOGIN_FAILED error
- `?status=failed&error_code=LOGIN_FAILED&search_key=prod_credential` — all three conditions must match
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_workflow_runs()

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

**page:** `typing.Optional[int]` — Page number for pagination.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of runs to return per page.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[WorkflowRunStatus]]` — Filter by one or more run statuses.
    
</dd>
</dl>

<dl>
<dd>

**search_key:** `typing.Optional[str]` — Case-insensitive substring search across: workflow run ID, parameter key, parameter description, run parameter value, and extra HTTP headers. A run is returned if any of these fields match. Soft-deleted parameter definitions are excluded from key/description matching.
    
</dd>
</dl>

<dl>
<dd>

**error_code:** `typing.Optional[str]` — Exact-match filter on the error_code field inside each task's errors JSON array. A run matches if any of its tasks contains an error with a matching error_code. Error codes are user-defined strings set during workflow execution.
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_workflow_runs_by_id</a>(...) -> typing.List[WorkflowRun]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List runs for a specific workflow.

Supports filtering by **status**, **search_key**, and **error_code**. All filters are combined with **AND** logic.

### search_key

Case-insensitive substring search across: workflow run ID, parameter key, parameter description, run parameter value, and extra HTTP headers. Soft-deleted parameter definitions are excluded.

### error_code

Exact-match filter on the `error_code` field inside each task's `errors` JSON array. A run matches if any of its tasks contains an error with a matching `error_code`.
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_workflow_runs_by_id(
    workflow_id="workflow_id",
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

**workflow_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for pagination.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of runs to return per page.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[WorkflowRunStatus]]` — Filter by one or more run statuses.
    
</dd>
</dl>

<dl>
<dd>

**search_key:** `typing.Optional[str]` — Case-insensitive substring search across: workflow run ID, parameter key, parameter description, run parameter value, and extra HTTP headers. A run is returned if any of these fields match. Soft-deleted parameter definitions are excluded from key/description matching.
    
</dd>
</dl>

<dl>
<dd>

**error_code:** `typing.Optional[str]` — Exact-match filter on the error_code field inside each task's errors JSON array. A run matches if any of its tasks contains an error with a matching error_code. Error codes are user-defined strings set during workflow execution.
    
</dd>
</dl>

<dl>
<dd>

**created_at_start:** `typing.Optional[datetime.datetime]` — Only include runs created at or after this UTC timestamp (ISO 8601).
    
</dd>
</dl>

<dl>
<dd>

**created_at_end:** `typing.Optional[datetime.datetime]` — Only include runs created strictly before this UTC timestamp (ISO 8601).
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_workflow</a>(...) -> Workflow</code></summary>
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_workflow(
    workflow_permanent_id="workflow_permanent_id",
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

**workflow_permanent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**template:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_workflow_versions</a>(...) -> typing.List[Workflow]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all versions of a workflow by its permanent ID.
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
    environment=FernApiEnvironment.CLOUD,
)

client.get_workflow_versions(
    workflow_permanent_id="workflow_permanent_id",
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

**workflow_permanent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**template:** `typing.Optional[bool]` 
    
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

## Artifacts
<details><summary><code>client.artifacts.<a href="src/fern/artifacts/client.py">get_artifact_content</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download the raw content of an artifact (supports bundled artifacts).
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
    environment=FernApiEnvironment.CLOUD,
)

client.artifacts.get_artifact_content(
    artifact_id="artifact_id",
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

**artifact_id:** `str` 
    
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

## Scripts
<details><summary><code>client.scripts.<a href="src/fern/scripts/client.py">run_script</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run a script
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
    environment=FernApiEnvironment.CLOUD,
)

client.scripts.run_script(
    script_id="s_abc123",
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

**script_id:** `str` — The unique identifier of the script
    
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

## Schedules
<details><summary><code>client.schedules.<a href="src/fern/schedules/client.py">list_all</a>(...) -> OrganizationScheduleListResponse</code></summary>
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
    environment=FernApiEnvironment.CLOUD,
)

client.schedules.list_all()

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

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[SchedulesListAllRequestStatus]` — Filter by status: 'active' or 'paused'
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search by workflow title or schedule name
    
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

<details><summary><code>client.schedules.<a href="src/fern/schedules/client.py">list</a>(...) -> WorkflowScheduleListResponse</code></summary>
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
    environment=FernApiEnvironment.CLOUD,
)

client.schedules.list(
    workflow_permanent_id="workflow_permanent_id",
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

**workflow_permanent_id:** `str` 
    
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

<details><summary><code>client.schedules.<a href="src/fern/schedules/client.py">create</a>(...) -> WorkflowScheduleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a cron or fixed-interval schedule that runs the given agent automatically with a fixed set of parameters. An interval schedule first runs at first_fire_at, or one interval after creation. Returns the stored schedule and its next upcoming run times.
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
    environment=FernApiEnvironment.CLOUD,
)

client.schedules.create(
    workflow_permanent_id="workflow_permanent_id",
    timezone="timezone",
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

**workflow_permanent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `WorkflowScheduleUpsertRequest` 
    
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

<details><summary><code>client.schedules.<a href="src/fern/schedules/client.py">get</a>(...) -> WorkflowScheduleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch one schedule belonging to an agent. Returns the schedule's cron expression or interval, timezone, parameters, enabled state, and next upcoming run times.
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
    environment=FernApiEnvironment.CLOUD,
)

client.schedules.get(
    workflow_permanent_id="workflow_permanent_id",
    workflow_schedule_id="workflow_schedule_id",
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

**workflow_permanent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_schedule_id:** `str` 
    
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

<details><summary><code>client.schedules.<a href="src/fern/schedules/client.py">update</a>(...) -> WorkflowScheduleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replace a schedule's cron expression or interval, timezone, run parameters, and enabled state. Returns the updated schedule and its next upcoming run times.
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
    environment=FernApiEnvironment.CLOUD,
)

client.schedules.update(
    workflow_permanent_id="workflow_permanent_id",
    workflow_schedule_id="workflow_schedule_id",
    timezone="timezone",
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

**workflow_permanent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_schedule_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `WorkflowScheduleUpsertRequest` 
    
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

<details><summary><code>client.schedules.<a href="src/fern/schedules/client.py">delete</a>(...) -> DeleteScheduleResponse</code></summary>
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
    environment=FernApiEnvironment.CLOUD,
)

client.schedules.delete(
    workflow_permanent_id="workflow_permanent_id",
    workflow_schedule_id="workflow_schedule_id",
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

**workflow_permanent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_schedule_id:** `str` 
    
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

<details><summary><code>client.schedules.<a href="src/fern/schedules/client.py">enable</a>(...) -> WorkflowScheduleResponse</code></summary>
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
    environment=FernApiEnvironment.CLOUD,
)

client.schedules.enable(
    workflow_permanent_id="workflow_permanent_id",
    workflow_schedule_id="workflow_schedule_id",
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

**workflow_permanent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_schedule_id:** `str` 
    
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

<details><summary><code>client.schedules.<a href="src/fern/schedules/client.py">disable</a>(...) -> WorkflowScheduleResponse</code></summary>
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
    environment=FernApiEnvironment.CLOUD,
)

client.schedules.disable(
    workflow_permanent_id="workflow_permanent_id",
    workflow_schedule_id="workflow_schedule_id",
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

**workflow_permanent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_schedule_id:** `str` 
    
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

## Agents
<details><summary><code>client.agents.<a href="src/fern/agents/client.py">reset_workflow_browser_profile</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Clear the persisted browser profile for a workflow that uses `Save & Reuse Session`. The next run will start from a fresh browser state. Use when a saved profile is corrupted.
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
    environment=FernApiEnvironment.CLOUD,
)

client.agents.reset_workflow_browser_profile(
    workflow_permanent_id="wpid_123",
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

**workflow_permanent_id:** `str` — The permanent ID of the workflow. Starts with `wpid_`.
    
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

