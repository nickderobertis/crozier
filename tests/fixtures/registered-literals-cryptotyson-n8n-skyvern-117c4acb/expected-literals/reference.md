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
    environment=FernApiEnvironment.PRODUCTION,
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

**request:** `TaskRunRequest` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">run_workflow</a>(...) -> WorkflowRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run a workflow
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.run_workflow(
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

**request:** `WorkflowRunRequest` 
    
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
    environment=FernApiEnvironment.PRODUCTION,
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
    environment=FernApiEnvironment.PRODUCTION,
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

<details><summary><code>client.<a href="src/fern/client.py">get_workflows</a>(...) -> typing.List[Workflow]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all workflows with the latest version for the organization.
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
    environment=FernApiEnvironment.PRODUCTION,
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

**title:** `typing.Optional[str]` 
    
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

Create a new workflow
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
    environment=FernApiEnvironment.PRODUCTION,
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

Update a workflow
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
    environment=FernApiEnvironment.PRODUCTION,
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

**workflow_id:** `str` — The ID of the workflow to update. Workflow ID starts with `wpid_`.
    
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

Delete a workflow
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
    environment=FernApiEnvironment.PRODUCTION,
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

**workflow_id:** `str` — The ID of the workflow to delete. Workflow ID starts with `wpid_`.
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_artifact</a>(...) -> Artifact</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an artifact
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.get_artifact(
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
    environment=FernApiEnvironment.PRODUCTION,
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

<details><summary><code>client.<a href="src/fern/client.py">retry_run_webhook</a>(...) -> typing.Any</code></summary>
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.retry_run_webhook(
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
    environment=FernApiEnvironment.PRODUCTION,
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
    environment=FernApiEnvironment.PRODUCTION,
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

**timeout:** `typing.Optional[int]` — Timeout in minutes for the session. Timeout is applied after the session is started. Must be between 5 and 240. Defaults to 60.
    
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
    environment=FernApiEnvironment.PRODUCTION,
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
    environment=FernApiEnvironment.PRODUCTION,
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
    environment=FernApiEnvironment.PRODUCTION,
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
    environment=FernApiEnvironment.PRODUCTION,
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.create_credential(
    name="My Credential",
    credential_type="password",
    credential=NonEmptyPasswordCredential(
        password="securepassword123",
        username="user@example.com",
        totp="JBSWY3DPEHPK3PXP",
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

**name:** `str` — Name of the credential
    
</dd>
</dl>

<dl>
<dd>

**credential_type:** `SkyvernForgeSdkSchemasCredentialsCredentialType` — Type of credential to create
    
</dd>
</dl>

<dl>
<dd>

**credential:** `CreateCredentialRequestCredential` — The credential data to store
    
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
    environment=FernApiEnvironment.PRODUCTION,
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
    environment=FernApiEnvironment.PRODUCTION,
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

<details><summary><code>client.<a href="src/fern/client.py">get_projects</a>(...) -> typing.List[Project]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a paginated list of projects for the current organization
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.get_projects(
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

<details><summary><code>client.<a href="src/fern/client.py">create_project</a>(...) -> CreateProjectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new project with optional files and metadata
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.create_project()

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

**files:** `typing.Optional[typing.List[ProjectFile]]` — Array of files to include in the project
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_project</a>(...) -> Project</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a specific project by its ID
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.get_project(
    project_id="proj_abc123",
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

**project_id:** `str` — The unique identifier of the project
    
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

<details><summary><code>client.<a href="src/fern/client.py">deploy_project</a>(...) -> CreateProjectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deploy a project with updated files, creating a new version
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
from fern import FernApi, ProjectFile
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.deploy_project(
    project_id="proj_abc123",
    files=[
        ProjectFile(
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

**project_id:** `str` — The unique identifier of the project
    
</dd>
</dl>

<dl>
<dd>

**files:** `typing.List[ProjectFile]` — Array of files to include in the project
    
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

Log in to a website using either credential stored in Skyvern, Bitwarden or 1Password
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
    environment=FernApiEnvironment.PRODUCTION,
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

**credential_type:** `SkyvernSchemasRunBlocksCredentialType` — Where to get the credential from
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — Website url
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` — Login instructions. Skyvern has default prompt/instruction for login if this field is not provided.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — Webhook URL to send login status updates
    
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

**extra_http_headers:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Additional HTTP headers to include in requests
    
</dd>
</dl>

<dl>
<dd>

**max_screenshot_scrolling_times:** `typing.Optional[int]` — Maximum number of times to scroll for screenshots
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

