# Reference
## Environments
<details><summary><code>client.environments.<a href="src/fern/environments/client.py">v1get_a_branch_config</a>(...) -> BranchDetailResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches configurations of the specified database branch
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

client.environments.v1get_a_branch_config(
    branch_id_or_ref="branch_id_or_ref",
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

**branch_id_or_ref:** `str` — Branch ref or deprecated branch ID
    
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

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">v1delete_a_branch</a>(...) -> BranchDeleteResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the specified database branch. By default, deletes immediately. Use force=false to schedule deletion with 1-hour grace period (only when soft deletion is enabled).
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

client.environments.v1delete_a_branch(
    branch_id_or_ref="branch_id_or_ref",
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

**branch_id_or_ref:** `str` — Branch ref or deprecated branch ID
    
</dd>
</dl>

<dl>
<dd>

**force:** `typing.Optional[str]` — If set to false, schedule deletion with 1-hour grace period (only when soft deletion is enabled).
    
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

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">v1update_a_branch_config</a>(...) -> BranchResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the configuration of the specified database branch
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

client.environments.v1update_a_branch_config(
    branch_id_or_ref="branch_id_or_ref",
    branch_name="preview-login-page",
    git_branch="feature/login-page",
    persistent=True,
    request_review=True,
    notify_url="https://example.com/webhooks/branches",
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

**branch_id_or_ref:** `str` — Branch ref or deprecated branch ID
    
</dd>
</dl>

<dl>
<dd>

**branch_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**git_branch:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**reset_on_push:** `typing.Optional[bool]` — This field is deprecated and will be ignored. Use v1-reset-a-branch endpoint directly instead.
    
</dd>
</dl>

<dl>
<dd>

**persistent:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[UpdateBranchBodyStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**request_review:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**notify_url:** `typing.Optional[str]` — HTTP endpoint to receive branch status updates.
    
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

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">v1push_a_branch</a>(...) -> BranchUpdateResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Pushes the specified database branch
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

client.environments.v1push_a_branch(
    branch_id_or_ref="branch_id_or_ref",
    migration_version="20250312000000",
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

**branch_id_or_ref:** `str` — Branch ref or deprecated branch ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `BranchActionBody` 
    
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

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">v1merge_a_branch</a>(...) -> BranchUpdateResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Merges the specified database branch
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

client.environments.v1merge_a_branch(
    branch_id_or_ref="branch_id_or_ref",
    migration_version="20250312000000",
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

**branch_id_or_ref:** `str` — Branch ref or deprecated branch ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `BranchActionBody` 
    
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

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">v1reset_a_branch</a>(...) -> BranchUpdateResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resets the specified database branch
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

client.environments.v1reset_a_branch(
    branch_id_or_ref="branch_id_or_ref",
    migration_version="20250312000000",
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

**branch_id_or_ref:** `str` — Branch ref or deprecated branch ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `BranchActionBody` 
    
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

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">v1restore_a_branch</a>(...) -> BranchRestoreResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels scheduled deletion and restores the branch to active state
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

client.environments.v1restore_a_branch(
    branch_id_or_ref="branch_id_or_ref",
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

**branch_id_or_ref:** `str` — Branch ref or deprecated branch ID
    
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

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">v1diff_a_branch</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Diffs the specified database branch
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

client.environments.v1diff_a_branch(
    branch_id_or_ref="branch_id_or_ref",
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

**branch_id_or_ref:** `str` — Branch ref or deprecated branch ID
    
</dd>
</dl>

<dl>
<dd>

**included_schemas:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**pgdelta:** `typing.Optional[str]` 

Use pg-delta instead of Migra for diffing when true. 
Boolean string.

Truthy values: `true`, `1`, `yes`, `on`, `y`, `enabled`

Falsy values: `false`, `0`, `no`, `off`, `n`, `disabled`
    
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

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">v1list_action_runs</a>(...) -> ListActionRunResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of action runs of the specified project.
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

client.environments.v1list_action_runs(
    ref="abcdefghijklmnopqrst",
    offset=0,
    limit=20,
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` 
    
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

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">v1count_action_runs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the total number of action runs of the specified project.
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

client.environments.v1count_action_runs(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">v1get_action_run</a>(...) -> ActionRunResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current status of the specified action run.
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

client.environments.v1get_action_run(
    ref="abcdefghijklmnopqrst",
    run_id="run_01hq3q9m7y5q7e4a7x2c8m1p4n",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` — Action Run ID
    
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

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">v1update_action_run_status</a>(...) -> UpdateRunStatusResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the status of an ongoing action run.
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

client.environments.v1update_action_run_status(
    ref="abcdefghijklmnopqrst",
    run_id="run_01hq3q9m7y5q7e4a7x2c8m1p4n",
    clone="RUNNING",
    configure="RUNNING",
    migrate="RUNNING",
    deploy="CREATED",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` — Action Run ID
    
</dd>
</dl>

<dl>
<dd>

**clone:** `typing.Optional[UpdateRunStatusBodyClone]` 
    
</dd>
</dl>

<dl>
<dd>

**pull:** `typing.Optional[UpdateRunStatusBodyPull]` 
    
</dd>
</dl>

<dl>
<dd>

**health:** `typing.Optional[UpdateRunStatusBodyHealth]` 
    
</dd>
</dl>

<dl>
<dd>

**configure:** `typing.Optional[UpdateRunStatusBodyConfigure]` 
    
</dd>
</dl>

<dl>
<dd>

**migrate:** `typing.Optional[UpdateRunStatusBodyMigrate]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[UpdateRunStatusBodySeed]` 
    
</dd>
</dl>

<dl>
<dd>

**deploy:** `typing.Optional[UpdateRunStatusBodyDeploy]` 
    
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

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">v1get_action_run_logs</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the logs from the specified action run.
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

client.environments.v1get_action_run_logs(
    ref="ref",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` — Action Run ID
    
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

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">v1list_all_branches</a>(...) -> typing.List[BranchResponseOutput]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all database branches of the specified project.
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

client.environments.v1list_all_branches(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">v1create_a_branch</a>(...) -> BranchResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a database branch from the specified project.
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

client.environments.v1create_a_branch(
    ref="abcdefghijklmnopqrst",
    branch_name="preview-login-page",
    git_branch="feature/login-page",
    persistent=True,
    with_data=False,
    notify_url="https://example.com/webhooks/branches",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**branch_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**git_branch:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**is_default:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**persistent:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**desired_instance_size:** `typing.Optional[CreateBranchBodyDesiredInstanceSize]` 
    
</dd>
</dl>

<dl>
<dd>

**release_channel:** `typing.Optional[CreateBranchBodyReleaseChannel]` — Release channel. If not provided, GA will be used.
    
</dd>
</dl>

<dl>
<dd>

**postgres_engine:** `typing.Optional[CreateBranchBodyPostgresEngine]` — Postgres engine version. If not provided, the latest version will be used.
    
</dd>
</dl>

<dl>
<dd>

**secrets:** `typing.Optional[typing.Dict[str, str]]` 
    
</dd>
</dl>

<dl>
<dd>

**with_data:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**notify_url:** `typing.Optional[str]` — HTTP endpoint to receive branch status updates.
    
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

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">v1disable_preview_branching</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disables preview branching for the specified project
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

client.environments.v1disable_preview_branching(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">v1get_a_branch</a>(...) -> BranchResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches the specified database branch by its name.
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

client.environments.v1get_a_branch(
    ref="abcdefghijklmnopqrst",
    name="preview-login-page",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
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

## Projects
<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1list_all_projects</a>() -> typing.List[V1ProjectWithDatabaseResponseOutput]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all projects you've previously created.
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

client.projects.v1list_all_projects()

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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1create_a_project</a>(...) -> V1ProjectResponseOutput</code></summary>
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

client.projects.v1create_a_project(
    db_pass="correct-horse-battery-staple",
    name="acme-prod",
    organization_slug="tsrqponmlkjihgfedcba",
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

**db_pass:** `str` — Database password
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of your project
    
</dd>
</dl>

<dl>
<dd>

**organization_slug:** `str` — Organization slug
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — Deprecated: Use `organization_slug` instead.
    
</dd>
</dl>

<dl>
<dd>

**plan:** `typing.Optional[V1CreateProjectBodyPlan]` — Subscription Plan is now set on organization level and is ignored in this request
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[V1CreateProjectBodyRegion]` — Region you want your server to reside in. Use region_selection instead.
    
</dd>
</dl>

<dl>
<dd>

**region_selection:** `typing.Optional[V1CreateProjectBodyRegionSelection]` — Region selection. Only one of region or region_selection can be specified.
    
</dd>
</dl>

<dl>
<dd>

**kps_enabled:** `typing.Optional[bool]` — This field is deprecated and is ignored in this request
    
</dd>
</dl>

<dl>
<dd>

**desired_instance_size:** `typing.Optional[V1CreateProjectBodyDesiredInstanceSize]` — Desired instance size. Omit this field to always default to the smallest possible size.
    
</dd>
</dl>

<dl>
<dd>

**template_url:** `typing.Optional[str]` — Template URL used to create the project from the CLI.
    
</dd>
</dl>

<dl>
<dd>

**release_channel:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**postgres_engine:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**high_availability:** `typing.Optional[bool]` — [Experimental] Whether to enable high availability for the project.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1get_available_regions</a>(...) -> RegionsInfoOutput</code></summary>
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

client.projects.v1get_available_regions(
    organization_slug="tsrqponmlkjihgfedcba",
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

**organization_slug:** `str` — Slug of your organization
    
</dd>
</dl>

<dl>
<dd>

**continent:** `typing.Optional[V1GetAvailableRegionsRequestContinent]` — Continent code to determine regional recommendations: NA (North America), SA (South America), EU (Europe), AF (Africa), AS (Asia), OC (Oceania), AN (Antarctica)
    
</dd>
</dl>

<dl>
<dd>

**desired_instance_size:** `typing.Optional[V1GetAvailableRegionsRequestDesiredInstanceSize]` — Desired instance size. Omit this field to always default to the smallest possible size.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1list_all_network_bans</a>(...) -> NetworkBanResponseOutput</code></summary>
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

client.projects.v1list_all_network_bans(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1list_all_network_bans_enriched</a>(...) -> NetworkBanResponseEnrichedOutput</code></summary>
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

client.projects.v1list_all_network_bans_enriched(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1delete_network_bans</a>(...)</code></summary>
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

client.projects.v1delete_network_bans(
    ref="abcdefghijklmnopqrst",
    ipv4addresses=[
        "203.0.113.10"
    ],
    requester_ip=False,
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**ipv4addresses:** `typing.List[str]` — List of IP addresses to unban.
    
</dd>
</dl>

<dl>
<dd>

**requester_ip:** `typing.Optional[bool]` — Include requester's public IP in the list of addresses to unban.
    
</dd>
</dl>

<dl>
<dd>

**identifier:** `typing.Optional[str]` 
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1get_network_restrictions</a>(...) -> NetworkRestrictionsResponseOutput</code></summary>
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

client.projects.v1get_network_restrictions(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1patch_network_restrictions</a>(...) -> NetworkRestrictionsV2ResponseOutput</code></summary>
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
from fern.projects import NetworkRestrictionsPatchRequestAdd, NetworkRestrictionsPatchRequestRemove

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.projects.v1patch_network_restrictions(
    ref="abcdefghijklmnopqrst",
    add=NetworkRestrictionsPatchRequestAdd(
        db_allowed_cidrs=[
            "203.0.113.0/24"
        ],
    ),
    remove=NetworkRestrictionsPatchRequestRemove(
        db_allowed_cidrs=[
            "198.51.100.0/24"
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**add:** `typing.Optional[NetworkRestrictionsPatchRequestAdd]` 
    
</dd>
</dl>

<dl>
<dd>

**remove:** `typing.Optional[NetworkRestrictionsPatchRequestRemove]` 
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1update_network_restrictions</a>(...) -> NetworkRestrictionsResponseOutput</code></summary>
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

client.projects.v1update_network_restrictions(
    ref="abcdefghijklmnopqrst",
    db_allowed_cidrs=[
        "203.0.113.0/24"
    ],
    db_allowed_cidrs_v6=[
        "2001:db8::/32"
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**db_allowed_cidrs:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**db_allowed_cidrs_v6:** `typing.Optional[typing.List[str]]` 
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1get_project</a>(...) -> V1ProjectWithDatabaseResponseOutput</code></summary>
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

client.projects.v1get_project(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1delete_a_project</a>(...) -> V1ProjectRefResponseOutput</code></summary>
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

client.projects.v1delete_a_project(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1update_a_project</a>(...) -> V1ProjectRefResponseOutput</code></summary>
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

client.projects.v1update_a_project(
    ref="abcdefghijklmnopqrst",
    name="Acme Platform",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1upgrade_postgres_version</a>(...) -> ProjectUpgradeInitiateResponseOutput</code></summary>
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

client.projects.v1upgrade_postgres_version(
    ref="abcdefghijklmnopqrst",
    target_version="17",
    release_channel="ga",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**target_version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**release_channel:** `typing.Optional[UpgradeDatabaseBodyReleaseChannel]` 
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1get_postgres_upgrade_eligibility</a>(...) -> ProjectUpgradeEligibilityResponseOutput</code></summary>
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

client.projects.v1get_postgres_upgrade_eligibility(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1get_postgres_upgrade_status</a>(...) -> DatabaseUpgradeStatusResponseOutput</code></summary>
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

client.projects.v1get_postgres_upgrade_status(
    ref="abcdefghijklmnopqrst",
    tracking_id="9f4d3a20-6b2e-4a7e-8c91-1d5f3e7a2b4c",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**tracking_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1get_services_health</a>(...) -> typing.List[V1ServiceHealthResponseOutput]</code></summary>
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

client.projects.v1get_services_health(
    ref="abcdefghijklmnopqrst",
    services="services",
    timeout_ms=2000,
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**services:** `V1GetServicesHealthRequestServices` — Comma-separated list of enums or array of enums.
    
</dd>
</dl>

<dl>
<dd>

**timeout_ms:** `typing.Optional[int]` 
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1pause_a_project</a>(...)</code></summary>
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

client.projects.v1pause_a_project(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1restart_a_project</a>(...)</code></summary>
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

client.projects.v1restart_a_project(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1list_available_restore_versions</a>(...) -> GetProjectAvailableRestoreVersionsResponseOutput</code></summary>
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

client.projects.v1list_available_restore_versions(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1restore_a_project</a>(...)</code></summary>
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

client.projects.v1restore_a_project(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1cancel_a_project_restoration</a>(...)</code></summary>
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

client.projects.v1cancel_a_project_restoration(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1get_project_claim_token</a>(...) -> ProjectClaimTokenResponseOutput</code></summary>
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

client.projects.v1get_project_claim_token(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1create_project_claim_token</a>(...) -> CreateProjectClaimTokenResponseOutput</code></summary>
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

client.projects.v1create_project_claim_token(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1delete_project_claim_token</a>(...)</code></summary>
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

client.projects.v1delete_project_claim_token(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1get_database_disk</a>(...) -> DiskResponseOutput</code></summary>
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

client.projects.v1get_database_disk(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1modify_database_disk</a>(...)</code></summary>
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
from fern.projects import DiskRequestBodyAttributes_Gp3

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.projects.v1modify_database_disk(
    ref="abcdefghijklmnopqrst",
    attributes=DiskRequestBodyAttributes_Gp3(
        iops=3000,
        size_gb=100,
        throughput_mibps=125,
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `DiskRequestBodyAttributes` 
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1get_disk_utilization</a>(...) -> DiskUtilMetricsResponseOutput</code></summary>
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

client.projects.v1get_disk_utilization(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1get_project_disk_autoscale_config</a>(...) -> DiskAutoscaleConfigOutput</code></summary>
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

client.projects.v1get_project_disk_autoscale_config(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">v1get_all_projects_for_organization</a>(...) -> OrganizationProjectsResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of projects for the specified organization.

This endpoint uses offset-based pagination. Use the `offset` parameter to skip a number of projects and the `limit` parameter to control the number of projects returned per page.
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

client.projects.v1get_all_projects_for_organization(
    slug="tsrqponmlkjihgfedcba",
    offset=0,
    limit=20,
    search="acme",
    statuses="ACTIVE_HEALTHY,INACTIVE",
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

**slug:** `str` — Organization slug
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of projects to skip
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of projects to return per page
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search projects by name
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[V1GetAllProjectsForOrganizationRequestSort]` — Sort order for projects
    
</dd>
</dl>

<dl>
<dd>

**statuses:** `typing.Optional[str]` 

A comma-separated list of project statuses to filter by.

The following values are supported: `ACTIVE_HEALTHY`, `INACTIVE`.
    
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

## Organizations
<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">v1list_all_organizations</a>() -> typing.List[OrganizationResponseV1Output]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of organizations that you currently belong to.
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

client.organizations.v1list_all_organizations()

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

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">v1create_an_organization</a>(...) -> OrganizationResponseV1Output</code></summary>
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

client.organizations.v1create_an_organization(
    name="Acme",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">v1get_organization_entitlements</a>(...) -> V1ListEntitlementsResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the entitlements available to the organization based on their plan and any overrides.
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

client.organizations.v1get_organization_entitlements(
    slug="tsrqponmlkjihgfedcba",
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

**slug:** `str` — Organization slug
    
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

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">v1list_organization_members</a>(...) -> typing.List[V1OrganizationMemberResponseOutput]</code></summary>
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

client.organizations.v1list_organization_members(
    slug="tsrqponmlkjihgfedcba",
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

**slug:** `str` — Organization slug
    
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

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">v1get_an_organization</a>(...) -> V1OrganizationSlugResponseOutput</code></summary>
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

client.organizations.v1get_an_organization(
    slug="tsrqponmlkjihgfedcba",
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

**slug:** `str` — Organization slug
    
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

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">v1get_organization_project_claim</a>(...) -> OrganizationProjectClaimResponseOutput</code></summary>
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

client.organizations.v1get_organization_project_claim(
    slug="tsrqponmlkjihgfedcba",
    token="0123456789abcdef0123456789abcdef01234567",
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

**slug:** `str` — Organization slug
    
</dd>
</dl>

<dl>
<dd>

**token:** `str` 
    
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

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">v1claim_project_for_organization</a>(...)</code></summary>
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

client.organizations.v1claim_project_for_organization(
    slug="tsrqponmlkjihgfedcba",
    token="0123456789abcdef0123456789abcdef01234567",
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

**slug:** `str` — Organization slug
    
</dd>
</dl>

<dl>
<dd>

**token:** `str` 
    
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

## OAuth
<details><summary><code>client.o_auth.<a href="src/fern/o_auth/client.py">v1authorize_user</a>(...)</code></summary>
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

client.o_auth.v1authorize_user(
    client_id="66666666-6666-4666-8666-666666666666",
    response_type="code",
    redirect_uri="https://app.acme.com/auth/callback",
    scope="projects:read projects:write",
    state="st_9f4d3a206b2e4a7e8c91",
    response_mode="query",
    code_challenge="Z_P4EKbGwIkA01e3Y5fp4tMCvn_Ae5nUw7qY7XwkTrQ",
    organization_slug="tsrqponmlkjihgfedcba",
    resource="https://mcp.supabase.com/projects",
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

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**response_type:** `V1AuthorizeUserRequestResponseType` 
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**response_mode:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**code_challenge:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**code_challenge_method:** `typing.Optional[V1AuthorizeUserRequestCodeChallengeMethod]` 
    
</dd>
</dl>

<dl>
<dd>

**organization_slug:** `typing.Optional[str]` — Organization slug
    
</dd>
</dl>

<dl>
<dd>

**target_flow:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**resource:** `typing.Optional[str]` — Resource indicator for MCP (Model Context Protocol) clients
    
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

<details><summary><code>client.o_auth.<a href="src/fern/o_auth/client.py">v1exchange_oauth_token</a>(...) -> OAuthTokenResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Supports `authorization_code`, `refresh_token`, and `urn:ietf:params:oauth:grant-type:jwt-bearer` grant types. The `jwt-bearer` grant type (IDJAG — identity-directed JWT assertion) is in beta and available on Team and Enterprise plans only.
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

client.o_auth.v1exchange_oauth_token(
    grant_type="authorization_code",
    client_id="66666666-6666-4666-8666-666666666666",
    client_secret="sb_secret_live_example_9f4d3a206b2e4a7e8c91",
    code="oauth_code_9f4d3a206b2e4a7e8c91",
    code_verifier="qW0Z6d9pQnW0mL1dK1q9wFq6Yz2nV5rA8jT3mP7sH4c",
    redirect_uri="https://app.acme.com/auth/callback",
    scope="projects:read projects:write",
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

**request:** `OAuthTokenBody` 
    
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

<details><summary><code>client.o_auth.<a href="src/fern/o_auth/client.py">v1revoke_token</a>(...)</code></summary>
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

client.o_auth.v1revoke_token(
    client_id="66666666-6666-4666-8666-666666666666",
    client_secret="sb_secret_live_example_9f4d3a206b2e4a7e8c91",
    refresh_token="oauth_refresh_9f4d3a206b2e4a7e8c91",
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

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**refresh_token:** `str` 
    
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

<details><summary><code>client.o_auth.<a href="src/fern/o_auth/client.py">v1oauth_authorize_project_claim</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiates the OAuth authorization flow for the specified provider. After successful authentication, the user can claim ownership of the specified project.
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

client.o_auth.v1oauth_authorize_project_claim(
    project_ref="abcdefghijklmnopqrst",
    client_id="66666666-6666-4666-8666-666666666666",
    response_type="code",
    redirect_uri="https://app.acme.com/auth/callback",
    state="st_9f4d3a206b2e4a7e8c91",
    response_mode="query",
    code_challenge="Z_P4EKbGwIkA01e3Y5fp4tMCvn_Ae5nUw7qY7XwkTrQ",
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

**project_ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**response_type:** `V1OauthAuthorizeProjectClaimRequestResponseType` 
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**response_mode:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**code_challenge:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**code_challenge_method:** `typing.Optional[V1OauthAuthorizeProjectClaimRequestCodeChallengeMethod]` 
    
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

## Database
<details><summary><code>client.database.<a href="src/fern/database/client.py">v1list_all_snippets</a>(...) -> SnippetListOutput</code></summary>
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

client.database.v1list_all_snippets(
    project_ref="abcdefghijklmnopqrst",
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

**project_ref:** `typing.Optional[str]` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[V1ListAllSnippetsRequestSortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[V1ListAllSnippetsRequestSortOrder]` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1get_a_snippet</a>(...) -> SnippetResponseOutput</code></summary>
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

client.database.v1get_a_snippet(
    id="44444444-4444-4444-8444-444444444444",
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

**id:** `str` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1get_jit_access_config</a>(...) -> V1GetJitAccessConfigResponse</code></summary>
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

client.database.v1get_jit_access_config(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1update_jit_access_config</a>(...) -> V1UpdateJitAccessConfigResponse</code></summary>
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

client.database.v1update_jit_access_config(
    ref="abcdefghijklmnopqrst",
    state="enabled",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**state:** `JitAccessRequestRequestState` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1get_ssl_enforcement_config</a>(...) -> SslEnforcementResponseOutput</code></summary>
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

client.database.v1get_ssl_enforcement_config(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1update_ssl_enforcement_config</a>(...) -> SslEnforcementResponseOutput</code></summary>
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
from fern.database import SslEnforcementRequestRequestedConfig

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.database.v1update_ssl_enforcement_config(
    ref="abcdefghijklmnopqrst",
    requested_config=SslEnforcementRequestRequestedConfig(
        database=True,
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**requested_config:** `SslEnforcementRequestRequestedConfig` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1generate_typescript_types</a>(...) -> TypescriptResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the TypeScript types of your schema for use with supabase-js.
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

client.database.v1generate_typescript_types(
    ref="abcdefghijklmnopqrst",
    included_schemas="public,auth",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**included_schemas:** `typing.Optional[str]` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1get_readonly_mode_status</a>(...) -> ReadOnlyStatusResponseOutput</code></summary>
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

client.database.v1get_readonly_mode_status(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1disable_readonly_mode_temporarily</a>(...)</code></summary>
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

client.database.v1disable_readonly_mode_temporarily(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1setup_a_read_replica</a>(...)</code></summary>
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

client.database.v1setup_a_read_replica(
    ref="abcdefghijklmnopqrst",
    read_replica_region="us-west-1",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**read_replica_region:** `SetUpReadReplicaBodyReadReplicaRegion` — Region you want your read replica to reside in
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1remove_a_read_replica</a>(...)</code></summary>
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

client.database.v1remove_a_read_replica(
    ref="abcdefghijklmnopqrst",
    database_identifier="abcdefghijklmnopqrst-rr-us-west-1-abcde",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**database_identifier:** `str` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1create_login_role</a>(...) -> CreateRoleResponseOutput</code></summary>
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

client.database.v1create_login_role(
    ref="abcdefghijklmnopqrst",
    read_only=True,
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**read_only:** `bool` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1delete_login_roles</a>(...) -> DeleteRolesResponseOutput</code></summary>
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

client.database.v1delete_login_roles(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1list_migration_history</a>(...) -> V1ListMigrationsResponseOutput</code></summary>
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

client.database.v1list_migration_history(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1apply_a_migration</a>(...)</code></summary>
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

client.database.v1apply_a_migration(
    ref="abcdefghijklmnopqrst",
    query="create table public.widgets(id bigint primary key);",
    name="create_widgets_table",
    rollback="drop table if exists public.widgets;",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — A unique key to ensure the same migration is tracked only once.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**rollback:** `typing.Optional[str]` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1upsert_a_migration</a>(...)</code></summary>
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

client.database.v1upsert_a_migration(
    ref="abcdefghijklmnopqrst",
    query="create table public.widgets(id bigint primary key);",
    name="create_widgets_table",
    rollback="drop table if exists public.widgets;",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — A unique key to ensure the same migration is tracked only once.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**rollback:** `typing.Optional[str]` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1rollback_migrations</a>(...)</code></summary>
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

client.database.v1rollback_migrations(
    ref="abcdefghijklmnopqrst",
    gte="20250312000000",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**gte:** `str` — Rollback migrations greater or equal to this version
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1get_a_migration</a>(...) -> V1GetMigrationResponseOutput</code></summary>
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

client.database.v1get_a_migration(
    ref="abcdefghijklmnopqrst",
    version="20250312000000",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1patch_a_migration</a>(...)</code></summary>
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

client.database.v1patch_a_migration(
    ref="abcdefghijklmnopqrst",
    version="20250312000000",
    name="create_widgets_table",
    rollback="drop table if exists public.widgets;",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**rollback:** `typing.Optional[str]` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1run_a_query</a>(...)</code></summary>
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

client.database.v1run_a_query(
    ref="abcdefghijklmnopqrst",
    query="select * from pg_stat_activity limit 1;",
    read_only=True,
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.List[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**read_only:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1read_only_query</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

All entity references must be schema qualified.
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

client.database.v1read_only_query(
    ref="abcdefghijklmnopqrst",
    query="select * from pg_stat_activity limit 1;",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.List[typing.Any]]` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1enable_database_webhook</a>(...)</code></summary>
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

client.database.v1enable_database_webhook(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1get_database_metadata</a>(...) -> GetProjectDbMetadataResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This is an **experimental** endpoint. It is subject to change or removal in future versions. Use it with caution, as it may not remain supported or stable.
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

client.database.v1get_database_metadata(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1update_database_password</a>(...) -> V1UpdatePasswordResponseOutput</code></summary>
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

client.database.v1update_database_password(
    ref="abcdefghijklmnopqrst",
    password="correct-horse-battery-staple",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1get_jit_access</a>(...) -> JitAccessResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mappings of roles a user can assume in the project database
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

client.database.v1get_jit_access(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1authorize_jit_access</a>(...) -> JitAuthorizeAccessResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Authorizes the request to assume a role in the project database
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

client.database.v1authorize_jit_access(
    ref="abcdefghijklmnopqrst",
    role="postgres",
    rhost="203.0.113.10",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**role:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**rhost:** `str` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1update_jit_access</a>(...) -> JitAccessResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modifies the roles that can be assumed and for how long
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
from fern.database import UpdateJitAccessBodyRolesItem, UpdateJitAccessBodyRolesItemAllowedNetworks, UpdateJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.database.v1update_jit_access(
    ref="abcdefghijklmnopqrst",
    user_id="55555555-5555-4555-8555-555555555555",
    roles=[
        UpdateJitAccessBodyRolesItem(
            role="postgres",
            expires_at=1740787200,
            allowed_networks=UpdateJitAccessBodyRolesItemAllowedNetworks(
                allowed_cidrs=[
                    UpdateJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem(
                        cidr="203.0.113.0/24",
                    )
                ],
            ),
            branches_only=False,
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.List[UpdateJitAccessBodyRolesItem]` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1list_jit_access</a>(...) -> JitListAccessResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mappings of roles a user can assume in the project database
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

client.database.v1list_jit_access(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1invite_external_jit_access</a>(...) -> InviteExternalUserJitResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invites the external user and sets initial roles that can be assumed and for how long
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
from fern.database import InviteExternalUserJitAccessBodyRolesItem, InviteExternalUserJitAccessBodyRolesItemAllowedNetworks, InviteExternalUserJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.database.v1invite_external_jit_access(
    ref="abcdefghijklmnopqrst",
    email="external-user@somedomain.xyz",
    roles=[
        InviteExternalUserJitAccessBodyRolesItem(
            role="postgres",
            expires_at=1740787200,
            allowed_networks=InviteExternalUserJitAccessBodyRolesItemAllowedNetworks(
                allowed_cidrs=[
                    InviteExternalUserJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem(
                        cidr="203.0.113.0/24",
                    )
                ],
            ),
            branches_only=False,
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.List[InviteExternalUserJitAccessBodyRolesItem]` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1accept_invite_external_jit_access</a>(...) -> JitAccessResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Accepts the invitation to JIT database access
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

client.database.v1accept_invite_external_jit_access(
    ref="abcdefghijklmnopqrst",
    email="external-user@somedomain.xyz",
    token="",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**token:** `str` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1delete_invite_external_jit_access</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revokes and deletes the invitation
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

client.database.v1delete_invite_external_jit_access(
    ref="abcdefghijklmnopqrst",
    invite_id="55555555-5555-4555-8555-555555555555",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**invite_id:** `str` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1delete_jit_access</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove JIT mappings of a user, revoking all JIT database access
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

client.database.v1delete_jit_access(
    ref="abcdefghijklmnopqrst",
    user_id="55555555-5555-4555-8555-555555555555",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1get_database_openapi</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the PostgREST OpenAPI specification for the project. This is the replacement for querying `/rest/v1/` directly with the anon key.
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

client.database.v1get_database_openapi(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**schema:** `typing.Optional[str]` — The database schema to generate the OpenAPI spec for
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1get_project_pgbouncer_config</a>(...) -> V1PgbouncerConfigResponseOutput</code></summary>
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

client.database.v1get_project_pgbouncer_config(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1get_pooler_config</a>(...) -> typing.List[SupavisorConfigResponseOutput]</code></summary>
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

client.database.v1get_pooler_config(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1update_pooler_config</a>(...) -> UpdateSupavisorConfigResponseOutput</code></summary>
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

client.database.v1update_pooler_config(
    ref="abcdefghijklmnopqrst",
    default_pool_size=25,
    pool_mode="transaction",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**default_pool_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**pool_mode:** `typing.Optional[UpdateSupavisorConfigBodyPoolMode]` — Dedicated pooler mode for the project
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1get_postgres_config</a>(...) -> PostgresConfigResponseOutput</code></summary>
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

client.database.v1get_postgres_config(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1update_postgres_config</a>(...) -> PostgresConfigResponseOutput</code></summary>
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

client.database.v1update_postgres_config(
    ref="abcdefghijklmnopqrst",
    max_connections=120,
    shared_buffers="256MB",
    statement_timeout="60000ms",
    work_mem="4MB",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**effective_cache_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**logical_decoding_work_mem:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cron_log_statement:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**log_autovacuum_min_duration:** `typing.Optional[str]` — Default unit: ms
    
</dd>
</dl>

<dl>
<dd>

**log_checkpoints:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**log_connections:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**log_disconnections:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**log_duration:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**log_lock_waits:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**log_recovery_conflict_waits:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**log_replication_commands:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**log_startup_progress_interval:** `typing.Optional[str]` — Default unit: ms
    
</dd>
</dl>

<dl>
<dd>

**log_temp_files:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**maintenance_work_mem:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**track_activity_query_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**max_connections:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_locks_per_transaction:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_logical_replication_workers:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_parallel_maintenance_workers:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_parallel_workers:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_parallel_workers_per_gather:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_replication_slots:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_slot_wal_keep_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**max_standby_archive_delay:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**max_standby_streaming_delay:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**max_sync_workers_per_subscription:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_wal_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**max_wal_senders:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_worker_processes:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**session_replication_role:** `typing.Optional[UpdatePostgresConfigBodySessionReplicationRole]` 
    
</dd>
</dl>

<dl>
<dd>

**shared_buffers:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**statement_timeout:** `typing.Optional[str]` — Default unit: ms
    
</dd>
</dl>

<dl>
<dd>

**track_commit_timestamp:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**wal_keep_size:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**wal_sender_timeout:** `typing.Optional[str]` — Default unit: ms
    
</dd>
</dl>

<dl>
<dd>

**work_mem:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**checkpoint_timeout:** `typing.Optional[str]` — Default unit: s
    
</dd>
</dl>

<dl>
<dd>

**hot_standby_feedback:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**restart_database:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1list_all_backups</a>(...) -> V1BackupsResponseOutput</code></summary>
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

client.database.v1list_all_backups(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1restore_pitr_backup</a>(...)</code></summary>
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

client.database.v1restore_pitr_backup(
    ref="abcdefghijklmnopqrst",
    recovery_time_target_unix=1740787200,
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**recovery_time_target_unix:** `int` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1get_restore_point</a>(...) -> V1RestorePointResponse</code></summary>
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

client.database.v1get_restore_point(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1create_restore_point</a>(...) -> V1RestorePointResponse</code></summary>
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

client.database.v1create_restore_point(
    ref="abcdefghijklmnopqrst",
    name="before-upgrade",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1restore_physical_backup</a>(...)</code></summary>
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

client.database.v1restore_physical_backup(
    ref="abcdefghijklmnopqrst",
    id=12345,
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` 
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1get_backup_schedule</a>(...) -> V1BackupScheduleResponseOutput</code></summary>
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

client.database.v1get_backup_schedule(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1update_backup_schedule</a>(...) -> V1BackupScheduleResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets the time at which the daily backup runs. The change takes effect on the next backup window that includes the new time. If the new time has already passed for today, the first backup at the new time will occur the following day. It can only be updated 3 times per 24 hours.
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

client.database.v1update_backup_schedule(
    ref="abcdefghijklmnopqrst",
    schedule_for="04:00:00",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**schedule_for:** `str` — Time of day to schedule daily backups, in UTC. Format: HH:MM:SS.
    
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

<details><summary><code>client.database.<a href="src/fern/database/client.py">v1undo</a>(...)</code></summary>
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

client.database.v1undo(
    ref="abcdefghijklmnopqrst",
    name="before-upgrade",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
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

## Profile
<details><summary><code>client.profile.<a href="src/fern/profile/client.py">v1get_profile</a>() -> V1ProfileResponseOutput</code></summary>
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

client.profile.v1get_profile()

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

## Secrets
<details><summary><code>client.secrets.<a href="src/fern/secrets/client.py">v1get_project_api_keys</a>(...) -> typing.List[ApiKeyResponseOutput]</code></summary>
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

client.secrets.v1get_project_api_keys(
    ref="abcdefghijklmnopqrst",
    reveal="true",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**reveal:** `typing.Optional[str]` 

Boolean string.

Truthy values: `true`, `1`, `yes`, `on`, `y`, `enabled`

Falsy values: `false`, `0`, `no`, `off`, `n`, `disabled`
    
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

<details><summary><code>client.secrets.<a href="src/fern/secrets/client.py">v1create_project_api_key</a>(...) -> ApiKeyResponseOutput</code></summary>
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

client.secrets.v1create_project_api_key(
    ref="abcdefghijklmnopqrst",
    reveal="true",
    type="secret",
    name="ci_secret_key",
    description="CI deploy key",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**type:** `CreateApiKeyBodyType` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**reveal:** `typing.Optional[str]` 

Boolean string.

Truthy values: `true`, `1`, `yes`, `on`, `y`, `enabled`

Falsy values: `false`, `0`, `no`, `off`, `n`, `disabled`
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**secret_jwt_template:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
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

<details><summary><code>client.secrets.<a href="src/fern/secrets/client.py">v1get_project_legacy_api_keys</a>(...) -> LegacyApiKeysResponseOutput</code></summary>
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

client.secrets.v1get_project_legacy_api_keys(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.secrets.<a href="src/fern/secrets/client.py">v1update_project_legacy_api_keys</a>(...) -> LegacyApiKeysResponseOutput</code></summary>
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

client.secrets.v1update_project_legacy_api_keys(
    ref="abcdefghijklmnopqrst",
    enabled="true",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `str` 

Boolean string.

Truthy values: `true`, `1`, `yes`, `on`, `y`, `enabled`

Falsy values: `false`, `0`, `no`, `off`, `n`, `disabled`
    
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

<details><summary><code>client.secrets.<a href="src/fern/secrets/client.py">v1get_project_api_key</a>(...) -> ApiKeyResponseOutput</code></summary>
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

client.secrets.v1get_project_api_key(
    ref="abcdefghijklmnopqrst",
    id="22222222-2222-4222-8222-222222222222",
    reveal="true",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**reveal:** `typing.Optional[str]` 

Boolean string.

Truthy values: `true`, `1`, `yes`, `on`, `y`, `enabled`

Falsy values: `false`, `0`, `no`, `off`, `n`, `disabled`
    
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

<details><summary><code>client.secrets.<a href="src/fern/secrets/client.py">v1delete_project_api_key</a>(...) -> ApiKeyResponseOutput</code></summary>
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

client.secrets.v1delete_project_api_key(
    ref="abcdefghijklmnopqrst",
    id="22222222-2222-4222-8222-222222222222",
    reason="rotating_key",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**reveal:** `typing.Optional[str]` — Boolean string, true or false
    
</dd>
</dl>

<dl>
<dd>

**was_compromised:** `typing.Optional[str]` — Boolean string, true or false
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` 
    
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

<details><summary><code>client.secrets.<a href="src/fern/secrets/client.py">v1update_project_api_key</a>(...) -> ApiKeyResponseOutput</code></summary>
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

client.secrets.v1update_project_api_key(
    ref="abcdefghijklmnopqrst",
    id="22222222-2222-4222-8222-222222222222",
    reveal="true",
    name="ci_secret_key_rotated",
    description="Rotated after March release",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**reveal:** `typing.Optional[str]` 

Boolean string.

Truthy values: `true`, `1`, `yes`, `on`, `y`, `enabled`

Falsy values: `false`, `0`, `no`, `off`, `n`, `disabled`
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**secret_jwt_template:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
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

<details><summary><code>client.secrets.<a href="src/fern/secrets/client.py">v1get_pgsodium_config</a>(...) -> PgsodiumConfigResponseOutput</code></summary>
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

client.secrets.v1get_pgsodium_config(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.secrets.<a href="src/fern/secrets/client.py">v1update_pgsodium_config</a>(...) -> PgsodiumConfigResponseOutput</code></summary>
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

client.secrets.v1update_pgsodium_config(
    ref="abcdefghijklmnopqrst",
    root_key="0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**root_key:** `str` — The pgsodium root key: 32 bytes, hex-encoded (64 characters).
    
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

<details><summary><code>client.secrets.<a href="src/fern/secrets/client.py">v1list_all_secrets</a>(...) -> typing.List[SecretResponseOutput]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all secrets you've previously added to the specified project.
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

client.secrets.v1list_all_secrets(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.secrets.<a href="src/fern/secrets/client.py">v1bulk_create_secrets</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates multiple secrets and adds them to the specified project.
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
from fern import FernApi, CreateSecretBodyItem
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.secrets.v1bulk_create_secrets(
    ref="abcdefghijklmnopqrst",
    request=[
        CreateSecretBodyItem(
            name="OPENAI_API_KEY",
            value="sk-example-secret",
        ),
        CreateSecretBodyItem(
            name="STRIPE_WEBHOOK_SECRET",
            value="whsec_example",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateSecretBody` 
    
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

<details><summary><code>client.secrets.<a href="src/fern/secrets/client.py">v1bulk_delete_secrets</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes all secrets with the given names from the specified project
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

client.secrets.v1bulk_delete_secrets(
    ref="abcdefghijklmnopqrst",
    request=[
        "OPENAI_API_KEY"
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**request:** `DeleteSecretsBody` 
    
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

## Domains
<details><summary><code>client.domains.<a href="src/fern/domains/client.py">v1get_hostname_config</a>(...) -> UpdateCustomHostnameResponseOutput</code></summary>
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

client.domains.v1get_hostname_config(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.domains.<a href="src/fern/domains/client.py">v1delete_hostname_config</a>(...)</code></summary>
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

client.domains.v1delete_hostname_config(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**remove_addon:** `typing.Optional[str]` — If true, also removes the custom domain add-on from the project subscription.
    
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

<details><summary><code>client.domains.<a href="src/fern/domains/client.py">v1update_hostname_config</a>(...) -> UpdateCustomHostnameResponseOutput</code></summary>
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

client.domains.v1update_hostname_config(
    ref="abcdefghijklmnopqrst",
    custom_hostname="docs.example.com",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**custom_hostname:** `str` 
    
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

<details><summary><code>client.domains.<a href="src/fern/domains/client.py">v1verify_dns_config</a>(...) -> UpdateCustomHostnameResponseOutput</code></summary>
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

client.domains.v1verify_dns_config(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.domains.<a href="src/fern/domains/client.py">v1activate_custom_hostname</a>(...) -> UpdateCustomHostnameResponseOutput</code></summary>
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

client.domains.v1activate_custom_hostname(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.domains.<a href="src/fern/domains/client.py">v1get_vanity_subdomain_config</a>(...) -> VanitySubdomainConfigResponseOutput</code></summary>
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

client.domains.v1get_vanity_subdomain_config(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.domains.<a href="src/fern/domains/client.py">v1deactivate_vanity_subdomain_config</a>(...)</code></summary>
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

client.domains.v1deactivate_vanity_subdomain_config(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.domains.<a href="src/fern/domains/client.py">v1check_vanity_subdomain_availability</a>(...) -> SubdomainAvailabilityResponseOutput</code></summary>
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

client.domains.v1check_vanity_subdomain_availability(
    ref="abcdefghijklmnopqrst",
    vanity_subdomain="acme-prod",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**request:** `VanitySubdomainBody` 
    
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

<details><summary><code>client.domains.<a href="src/fern/domains/client.py">v1activate_vanity_subdomain_config</a>(...) -> ActivateVanitySubdomainResponseOutput</code></summary>
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

client.domains.v1activate_vanity_subdomain_config(
    ref="abcdefghijklmnopqrst",
    vanity_subdomain="acme-prod",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**request:** `VanitySubdomainBody` 
    
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

## Rest
<details><summary><code>client.rest.<a href="src/fern/rest/client.py">v1get_postgrest_service_config</a>(...) -> PostgrestConfigWithJwtSecretResponseOutput</code></summary>
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

client.rest.v1get_postgrest_service_config(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.rest.<a href="src/fern/rest/client.py">v1update_postgrest_service_config</a>(...) -> V1PostgrestConfigResponseOutput</code></summary>
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

client.rest.v1update_postgrest_service_config(
    ref="abcdefghijklmnopqrst",
    db_schema="public,storage",
    max_rows=1000,
    db_pool=20,
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**db_extra_search_path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**db_schema:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**max_rows:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**db_pool:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**db_pool_acquisition_timeout:** `typing.Optional[int]` 
    
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

## Auth
<details><summary><code>client.auth.<a href="src/fern/auth/client.py">v1get_legacy_signing_key</a>(...) -> SigningKeyResponseOutput</code></summary>
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

client.auth.v1get_legacy_signing_key(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">v1create_legacy_signing_key</a>(...) -> SigningKeyResponseOutput</code></summary>
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

client.auth.v1create_legacy_signing_key(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">v1get_project_signing_keys</a>(...) -> SigningKeysResponseOutput</code></summary>
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

client.auth.v1get_project_signing_keys(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">v1create_project_signing_key</a>(...) -> SigningKeyResponseOutput</code></summary>
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

client.auth.v1create_project_signing_key(
    ref="abcdefghijklmnopqrst",
    algorithm="RS256",
    status="standby",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**algorithm:** `CreateSigningKeyBodyAlgorithm` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[CreateSigningKeyBodyStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**private_jwk:** `typing.Optional[CreateSigningKeyBodyPrivateJwk]` 
    
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">v1get_project_signing_key</a>(...) -> SigningKeyResponseOutput</code></summary>
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

client.auth.v1get_project_signing_key(
    ref="abcdefghijklmnopqrst",
    id="33333333-3333-4333-8333-333333333333",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">v1remove_project_signing_key</a>(...) -> SigningKeyResponseOutput</code></summary>
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

client.auth.v1remove_project_signing_key(
    ref="abcdefghijklmnopqrst",
    id="33333333-3333-4333-8333-333333333333",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">v1update_project_signing_key</a>(...) -> SigningKeyResponseOutput</code></summary>
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

client.auth.v1update_project_signing_key(
    ref="abcdefghijklmnopqrst",
    id="33333333-3333-4333-8333-333333333333",
    status="standby",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `UpdateSigningKeyBodyStatus` 
    
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">v1get_auth_service_config</a>(...) -> AuthConfigResponseOutput</code></summary>
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

client.auth.v1get_auth_service_config(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">v1update_auth_service_config</a>(...) -> AuthConfigResponseOutput</code></summary>
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

client.auth.v1update_auth_service_config(
    ref="abcdefghijklmnopqrst",
    site_url="https://app.example.com",
    disable_signup=False,
    jwt_exp=3600,
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**site_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**disable_signup:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**jwt_exp:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**smtp_admin_email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**smtp_host:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**smtp_port:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**smtp_user:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**smtp_pass:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**smtp_max_frequency:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**smtp_sender_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_allow_unverified_email_sign_ins:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_autoconfirm:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_subjects_invite:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_subjects_confirmation:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_subjects_recovery:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_subjects_email_change:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_subjects_magic_link:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_subjects_reauthentication:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_subjects_password_changed_notification:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_subjects_email_changed_notification:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_subjects_phone_changed_notification:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_subjects_mfa_factor_enrolled_notification:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_subjects_mfa_factor_unenrolled_notification:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_subjects_identity_linked_notification:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_subjects_identity_unlinked_notification:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_templates_invite_content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_templates_confirmation_content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_templates_recovery_content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_templates_email_change_content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_templates_magic_link_content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_templates_reauthentication_content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_templates_password_changed_notification_content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_templates_email_changed_notification_content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_templates_phone_changed_notification_content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_templates_mfa_factor_enrolled_notification_content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_templates_mfa_factor_unenrolled_notification_content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_templates_identity_linked_notification_content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_templates_identity_unlinked_notification_content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_notifications_password_changed_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_notifications_email_changed_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_notifications_phone_changed_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_notifications_mfa_factor_enrolled_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_notifications_mfa_factor_unenrolled_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_notifications_identity_linked_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_notifications_identity_unlinked_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**mfa_max_enrolled_factors:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**uri_allow_list:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_anonymous_users_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_email_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_phone_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**saml_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**saml_external_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**security_sb_forwarded_for_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**security_captcha_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**security_captcha_provider:** `typing.Optional[UpdateAuthConfigBodySecurityCaptchaProvider]` 
    
</dd>
</dl>

<dl>
<dd>

**security_captcha_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sessions_timebox:** `typing.Optional[float]` — Session timebox in hours. Maximum 8760 hours (1 year).
    
</dd>
</dl>

<dl>
<dd>

**sessions_inactivity_timeout:** `typing.Optional[float]` — Session inactivity timeout in hours. Maximum 8760 hours (1 year).
    
</dd>
</dl>

<dl>
<dd>

**sessions_single_per_user:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**sessions_tags:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**rate_limit_anonymous_users:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**rate_limit_email_sent:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**rate_limit_sms_sent:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**rate_limit_verify:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**rate_limit_token_refresh:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**rate_limit_otp:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**rate_limit_web3:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_secure_email_change_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**refresh_token_rotation_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**password_hibp_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**password_min_length:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**password_required_characters:** `typing.Optional[UpdateAuthConfigBodyPasswordRequiredCharacters]` 
    
</dd>
</dl>

<dl>
<dd>

**security_manual_linking_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**security_update_password_require_reauthentication:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**security_update_password_require_current_password:** `typing.Optional[bool]` — Require the user's current password when updating their password.
    
</dd>
</dl>

<dl>
<dd>

**security_refresh_token_reuse_interval:** `typing.Optional[int]` — Refresh token reuse interval in seconds. Maximum 300 seconds (5 minutes).
    
</dd>
</dl>

<dl>
<dd>

**mailer_otp_exp:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**mailer_otp_length:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_autoconfirm:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_max_frequency:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_otp_exp:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_otp_length:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_provider:** `typing.Optional[UpdateAuthConfigBodySmsProvider]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_messagebird_access_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_messagebird_originator:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_test_otp:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_test_otp_valid_until:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_textlocal_api_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_textlocal_sender:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_twilio_account_sid:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_twilio_auth_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_twilio_content_sid:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_twilio_message_service_sid:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_twilio_verify_account_sid:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_twilio_verify_auth_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_twilio_verify_message_service_sid:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_vonage_api_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_vonage_api_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_vonage_from:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sms_template:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_mfa_verification_attempt_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_mfa_verification_attempt_uri:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_mfa_verification_attempt_secrets:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_password_verification_attempt_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_password_verification_attempt_uri:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_password_verification_attempt_secrets:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_custom_access_token_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_custom_access_token_uri:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_custom_access_token_secrets:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_send_sms_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_send_sms_uri:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_send_sms_secrets:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_send_email_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_send_email_uri:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_send_email_secrets:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_before_user_created_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_before_user_created_uri:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_before_user_created_secrets:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_after_user_created_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_after_user_created_uri:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**hook_after_user_created_secrets:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_apple_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_apple_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_apple_email_optional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_apple_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_apple_additional_client_ids:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_azure_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_azure_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_azure_email_optional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_azure_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_azure_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_bitbucket_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_bitbucket_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_bitbucket_email_optional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_bitbucket_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_discord_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_discord_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_discord_email_optional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_discord_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_facebook_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_facebook_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_facebook_email_optional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_facebook_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_figma_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_figma_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_figma_email_optional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_figma_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_github_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_github_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_github_email_optional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_github_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_gitlab_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_gitlab_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_gitlab_email_optional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_gitlab_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_gitlab_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_google_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_google_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_google_email_optional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_google_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_google_additional_client_ids:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_google_skip_nonce_check:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_kakao_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_kakao_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_kakao_email_optional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_kakao_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_keycloak_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_keycloak_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_keycloak_email_optional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_keycloak_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_keycloak_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_linkedin_oidc_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_linkedin_oidc_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_linkedin_oidc_email_optional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_linkedin_oidc_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_slack_oidc_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_slack_oidc_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_slack_oidc_email_optional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_slack_oidc_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_notion_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_notion_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_notion_email_optional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_notion_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_slack_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_slack_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_slack_email_optional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_slack_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_spotify_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_spotify_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_spotify_email_optional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_spotify_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_twitch_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_twitch_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_twitch_email_optional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_twitch_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_twitter_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_twitter_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_twitter_email_optional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_twitter_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_x_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_x_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_x_email_optional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_x_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_workos_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_workos_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_workos_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_workos_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_web3solana_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_web3ethereum_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_zoom_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_zoom_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**external_zoom_email_optional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**external_zoom_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**db_max_pool_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**db_max_pool_size_unit:** `typing.Optional[UpdateAuthConfigBodyDbMaxPoolSizeUnit]` 
    
</dd>
</dl>

<dl>
<dd>

**api_max_request_duration:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**mfa_totp_enroll_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**mfa_totp_verify_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**mfa_web_authn_enroll_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**mfa_web_authn_verify_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**passkey_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**webauthn_rp_display_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**webauthn_rp_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**webauthn_rp_origins:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mfa_phone_enroll_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**mfa_phone_verify_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**mfa_phone_max_frequency:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**mfa_phone_otp_length:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**mfa_phone_template:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**nimbus_oauth_client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**nimbus_oauth_client_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**oauth_server_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**oauth_server_allow_dynamic_registration:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**oauth_server_authorization_path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_oauth_enabled:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">v1list_project_tpa_integrations</a>(...) -> typing.List[ThirdPartyAuthOutput]</code></summary>
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

client.auth.v1list_project_tpa_integrations(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">v1create_project_tpa_integration</a>(...) -> ThirdPartyAuthOutput</code></summary>
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

client.auth.v1create_project_tpa_integration(
    ref="abcdefghijklmnopqrst",
    oidc_issuer_url="https://login.acme.com",
    jwks_url="https://login.acme.com/.well-known/jwks.json",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**oidc_issuer_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**jwks_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_jwks:** `typing.Optional[typing.Any]` 
    
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">v1get_project_tpa_integration</a>(...) -> ThirdPartyAuthOutput</code></summary>
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

client.auth.v1get_project_tpa_integration(
    ref="abcdefghijklmnopqrst",
    tpa_id="88888888-8888-4888-8888-888888888888",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**tpa_id:** `str` 
    
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">v1delete_project_tpa_integration</a>(...) -> ThirdPartyAuthOutput</code></summary>
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

client.auth.v1delete_project_tpa_integration(
    ref="abcdefghijklmnopqrst",
    tpa_id="88888888-8888-4888-8888-888888888888",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**tpa_id:** `str` 
    
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">v1list_all_sso_provider</a>(...) -> ListProvidersResponseOutput</code></summary>
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

client.auth.v1list_all_sso_provider(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">v1create_a_sso_provider</a>(...) -> CreateProviderResponseOutput</code></summary>
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
from fern.auth import CreateProviderBodyAttributeMapping, CreateProviderBodyAttributeMappingKeysValue

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.auth.v1create_a_sso_provider(
    ref="abcdefghijklmnopqrst",
    type="saml",
    metadata_url="https://sso.acme.com/metadata.xml",
    domains=[
        "acme.com"
    ],
    attribute_mapping=CreateProviderBodyAttributeMapping(
        keys={
            "email": CreateProviderBodyAttributeMappingKeysValue(
                name="email",
            ),
            "first_name": CreateProviderBodyAttributeMappingKeysValue(
                name="first_name",
            ),
            "last_name": CreateProviderBodyAttributeMappingKeysValue(
                name="last_name",
            )
        },
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**type:** `CreateProviderBodyType` — What type of provider will be created
    
</dd>
</dl>

<dl>
<dd>

**metadata_xml:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**domains:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**attribute_mapping:** `typing.Optional[CreateProviderBodyAttributeMapping]` 
    
</dd>
</dl>

<dl>
<dd>

**name_id_format:** `typing.Optional[CreateProviderBodyNameIdFormat]` 
    
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">v1get_a_sso_provider</a>(...) -> GetProviderResponseOutput</code></summary>
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

client.auth.v1get_a_sso_provider(
    ref="abcdefghijklmnopqrst",
    provider_id="77777777-7777-4777-8777-777777777777",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**provider_id:** `str` 
    
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">v1update_a_sso_provider</a>(...) -> UpdateProviderResponseOutput</code></summary>
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

client.auth.v1update_a_sso_provider(
    ref="abcdefghijklmnopqrst",
    provider_id="77777777-7777-4777-8777-777777777777",
    metadata_url="https://sso.acme.com/metadata.xml",
    domains=[
        "acme.com",
        "contractors.acme.com"
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**provider_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**metadata_xml:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**domains:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**attribute_mapping:** `typing.Optional[UpdateProviderBodyAttributeMapping]` 
    
</dd>
</dl>

<dl>
<dd>

**name_id_format:** `typing.Optional[UpdateProviderBodyNameIdFormat]` 
    
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">v1delete_a_sso_provider</a>(...) -> DeleteProviderResponseOutput</code></summary>
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

client.auth.v1delete_a_sso_provider(
    ref="abcdefghijklmnopqrst",
    provider_id="77777777-7777-4777-8777-777777777777",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**provider_id:** `str` 
    
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

## Billing
<details><summary><code>client.billing.<a href="src/fern/billing/client.py">v1list_project_addons</a>(...) -> ListProjectAddonsResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the billing addons that are currently applied, including the active compute instance size, and lists every addon option that can be provisioned with pricing metadata.
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

client.billing.v1list_project_addons(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.billing.<a href="src/fern/billing/client.py">v1apply_project_addon</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Selects an addon variant, for example scaling the project’s compute instance up or down, and applies it to the project.
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

client.billing.v1apply_project_addon(
    ref="abcdefghijklmnopqrst",
    addon_variant="pitr_7",
    addon_type="pitr",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**addon_variant:** `ApplyProjectAddonBodyAddonVariant` 
    
</dd>
</dl>

<dl>
<dd>

**addon_type:** `ApplyProjectAddonBodyAddonType` 
    
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

<details><summary><code>client.billing.<a href="src/fern/billing/client.py">v1remove_project_addon</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disables the selected addon variant, including rolling the compute instance back to its previous size.
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

client.billing.v1remove_project_addon(
    ref="abcdefghijklmnopqrst",
    addon_variant="ci_micro",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**addon_variant:** `V1RemoveProjectAddonRequestAddonVariant` 
    
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

## Advisors
<details><summary><code>client.advisors.<a href="src/fern/advisors/client.py">v1get_performance_advisors</a>(...) -> V1ProjectAdvisorsResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This is an **experimental** endpoint. It is subject to change or removal in future versions. Use it with caution, as it may not remain supported or stable.
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

client.advisors.v1get_performance_advisors(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.advisors.<a href="src/fern/advisors/client.py">v1get_security_advisors</a>(...) -> V1ProjectAdvisorsResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This is an **experimental** endpoint. It is subject to change or removal in future versions. Use it with caution, as it may not remain supported or stable.
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

client.advisors.v1get_security_advisors(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**lint_type:** `typing.Optional[V1GetSecurityAdvisorsRequestLintType]` 
    
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

## Analytics
<details><summary><code>client.analytics.<a href="src/fern/analytics/client.py">v1get_project_logs_all</a>(...) -> AnalyticsResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Executes a SQL query on the project's logs.

Either the `iso_timestamp_start` and `iso_timestamp_end` parameters must be provided.
If both are not provided, only the last 1 minute of logs will be queried.
The timestamp range must be no more than 24 hours and is rounded to the nearest minute. If the range is more than 24 hours, a validation error will be thrown.

Note: Unless the `sql` parameter is provided, only edge_logs will be queried. See the [log query docs](https://supabase.com/docs/guides/monitoring-and-debugging/logs#logs-explorer) for all available sources.
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
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.analytics.v1get_project_logs_all(
    ref="abcdefghijklmnopqrst",
    sql="select event_message from edge_logs limit 10",
    iso_timestamp_start=datetime.datetime.fromisoformat("2025-03-01T00:00:00+00:00"),
    iso_timestamp_end=datetime.datetime.fromisoformat("2025-03-01T23:59:59+00:00"),
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**sql:** `typing.Optional[str]` — Custom SQL query to execute on the logs. See [querying logs](https://supabase.com/docs/guides/monitoring-and-debugging/logs#querying-with-the-logs-explorer) for more details.
    
</dd>
</dl>

<dl>
<dd>

**iso_timestamp_start:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**iso_timestamp_end:** `typing.Optional[datetime.datetime]` 
    
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

<details><summary><code>client.analytics.<a href="src/fern/analytics/client.py">v1get_project_logs</a>(...) -> AnalyticsResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Executes an SQL or LQL query on the project's unified logs stream.

Either the `iso_timestamp_start` and `iso_timestamp_end` parameters must be provided.
If both are not provided, only the last 1 minute of logs will be queried.
The timestamp range must be no more than 24 hours and is rounded to the nearest minute. If the range is more than 24 hours, a validation error will be thrown.

Filter by the `source` column to specify specific log sources, such as edge_logs, postgres_logs, etc.

Note: SQL must be written in **ClickHouse SQL dialect**.
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
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.analytics.v1get_project_logs(
    ref="abcdefghijklmnopqrst",
    sql="select event_message from edge_logs limit 10",
    iso_timestamp_start=datetime.datetime.fromisoformat("2025-03-01T00:00:00+00:00"),
    iso_timestamp_end=datetime.datetime.fromisoformat("2025-03-01T23:59:59+00:00"),
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**sql:** `typing.Optional[str]` — Custom SQL query to execute on the logs. See [querying logs](https://supabase.com/docs/guides/monitoring-and-debugging/logs#querying-with-the-logs-explorer) for more details.
    
</dd>
</dl>

<dl>
<dd>

**iso_timestamp_start:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**iso_timestamp_end:** `typing.Optional[datetime.datetime]` 
    
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

<details><summary><code>client.analytics.<a href="src/fern/analytics/client.py">v1get_project_usage_api_count</a>(...) -> V1GetUsageApiCountResponseOutput</code></summary>
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

client.analytics.v1get_project_usage_api_count(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[V1GetProjectUsageApiCountRequestInterval]` 
    
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

<details><summary><code>client.analytics.<a href="src/fern/analytics/client.py">v1get_project_usage_request_count</a>(...) -> V1GetUsageApiRequestsCountResponseOutput</code></summary>
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

client.analytics.v1get_project_usage_request_count(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.analytics.<a href="src/fern/analytics/client.py">v1get_project_function_combined_stats</a>(...) -> AnalyticsResponseOutput</code></summary>
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

client.analytics.v1get_project_function_combined_stats(
    ref="abcdefghijklmnopqrst",
    interval="15min",
    function_id="3c078cce-ad70-4148-9f37-4da362789053",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**interval:** `V1GetProjectFunctionCombinedStatsRequestInterval` 
    
</dd>
</dl>

<dl>
<dd>

**function_id:** `str` 
    
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

<details><summary><code>client.analytics.<a href="src/fern/analytics/client.py">v1scrape_project_metrics</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Prometheus scrape endpoint. Returns metrics of a customer project in the Prometheus open exposition format.
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

client.analytics.v1scrape_project_metrics(
    ref="ref",
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

**ref:** `str` — Project ref
    
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

## Edge Functions
<details><summary><code>client.edge_functions.<a href="src/fern/edge_functions/client.py">v1list_all_functions</a>(...) -> typing.List[FunctionResponseOutput]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all functions you've previously added to the specified project.
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

client.edge_functions.v1list_all_functions(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.edge_functions.<a href="src/fern/edge_functions/client.py">v1create_a_function</a>(...) -> FunctionResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is deprecated - use the deploy endpoint. Creates a function and adds it to the specified project.
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

client.edge_functions.v1create_a_function(
    ref="abcdefghijklmnopqrst",
    slug="hello-world",
    name="Hello World",
    entrypoint_path="index.ts",
    import_map_path="import_map.json",
    ezbr_sha256="44c691990518d25498f0fd80cf6631ecf2b58eb9c5eb2a087dd1688f2904dac7",
    v1create_function_body_slug="hello-world",
    v1create_function_body_name="Hello World",
    body="Deno.serve(() => new Response(\'Hello, world!\'))",
    v1create_function_body_verify_jwt=True,
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**v1create_function_body_slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**v1create_function_body_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**verify_jwt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**import_map:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**entrypoint_path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**import_map_path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ezbr_sha256:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**v1create_function_body_verify_jwt:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.edge_functions.<a href="src/fern/edge_functions/client.py">v1bulk_update_functions</a>(...) -> BulkUpdateFunctionResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk update functions. It will create a new function or replace existing. The operation is idempotent. NOTE: You will need to manually bump the version.
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
from fern import FernApi, BulkUpdateFunctionBodyItem
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.edge_functions.v1bulk_update_functions(
    ref="abcdefghijklmnopqrst",
    request=[
        BulkUpdateFunctionBodyItem(
            id="3c078cce-ad70-4148-9f37-4da362789053",
            slug="hello-world",
            name="Hello World",
            status="ACTIVE",
            version=2,
            verify_jwt=True,
            entrypoint_path="index.ts",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**request:** `BulkUpdateFunctionBody` 
    
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

<details><summary><code>client.edge_functions.<a href="src/fern/edge_functions/client.py">v1deploy_a_function</a>(...) -> DeployFunctionResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A new endpoint to deploy functions. It will create if function does not exist.
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
from fern.edge_functions import V1DeployAFunctionRequestMetadata

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.edge_functions.v1deploy_a_function(
    ref="abcdefghijklmnopqrst",
    slug="hello-world",
    file=["example_file"],
    metadata=V1DeployAFunctionRequestMetadata(
        entrypoint_path="entrypoint_path",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.List[core.File]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `V1DeployAFunctionRequestMetadata` 
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**bundle_only:** `typing.Optional[str]` 
    
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

<details><summary><code>client.edge_functions.<a href="src/fern/edge_functions/client.py">v1get_a_function</a>(...) -> FunctionSlugResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a function with the specified slug and project.
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

client.edge_functions.v1get_a_function(
    ref="abcdefghijklmnopqrst",
    function_slug="hello-world",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**function_slug:** `str` — Function slug
    
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

<details><summary><code>client.edge_functions.<a href="src/fern/edge_functions/client.py">v1delete_a_function</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a function with the specified slug from the specified project.
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

client.edge_functions.v1delete_a_function(
    ref="abcdefghijklmnopqrst",
    function_slug="hello-world",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**function_slug:** `str` — Function slug
    
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

<details><summary><code>client.edge_functions.<a href="src/fern/edge_functions/client.py">v1update_a_function</a>(...) -> FunctionSlugResponseOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a function with the specified slug and project.
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

client.edge_functions.v1update_a_function(
    ref="abcdefghijklmnopqrst",
    function_slug="hello-world",
    slug="hello-world",
    name="Hello World",
    entrypoint_path="index.ts",
    import_map_path="import_map.json",
    ezbr_sha256="44c691990518d25498f0fd80cf6631ecf2b58eb9c5eb2a087dd1688f2904dac7",
    v1update_function_body_name="Hello World",
    body="Deno.serve(() => new Response(\'Hello again!\'))",
    v1update_function_body_verify_jwt=True,
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**function_slug:** `str` — Function slug
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**verify_jwt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**import_map:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**entrypoint_path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**import_map_path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ezbr_sha256:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**v1update_function_body_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**v1update_function_body_verify_jwt:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.edge_functions.<a href="src/fern/edge_functions/client.py">v1get_a_function_body</a>(...) -> StreamableFile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a function body for the specified slug and project.
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

client.edge_functions.v1get_a_function_body(
    ref="abcdefghijklmnopqrst",
    function_slug="hello-world",
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**function_slug:** `str` — Function slug
    
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

## Storage
<details><summary><code>client.storage.<a href="src/fern/storage/client.py">v1list_all_buckets</a>(...) -> typing.List[V1StorageBucketResponseOutput]</code></summary>
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

client.storage.v1list_all_buckets(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.storage.<a href="src/fern/storage/client.py">v1get_storage_config</a>(...) -> StorageConfigResponseOutput</code></summary>
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

client.storage.v1get_storage_config(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.storage.<a href="src/fern/storage/client.py">v1update_storage_config</a>(...)</code></summary>
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
from fern.storage import UpdateStorageConfigBodyFeatures, UpdateStorageConfigBodyFeaturesImageTransformation

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.storage.v1update_storage_config(
    ref="abcdefghijklmnopqrst",
    file_size_limit=10485760,
    features=UpdateStorageConfigBodyFeatures(
        image_transformation=UpdateStorageConfigBodyFeaturesImageTransformation(
            enabled=True,
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**file_size_limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**features:** `typing.Optional[UpdateStorageConfigBodyFeatures]` 
    
</dd>
</dl>

<dl>
<dd>

**external:** `typing.Optional[UpdateStorageConfigBodyExternal]` 
    
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

## Realtime
<details><summary><code>client.realtime.<a href="src/fern/realtime/client.py">v1get_realtime_config</a>(...) -> RealtimeConfigResponseOutput</code></summary>
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

client.realtime.v1get_realtime_config(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

<details><summary><code>client.realtime.<a href="src/fern/realtime/client.py">v1update_realtime_config</a>(...)</code></summary>
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

client.realtime.v1update_realtime_config(
    ref="abcdefghijklmnopqrst",
    private_only=False,
    max_concurrent_users=1000,
    max_channels_per_client=100,
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

**ref:** `str` — Project ref
    
</dd>
</dl>

<dl>
<dd>

**private_only:** `typing.Optional[bool]` — Whether to only allow private channels
    
</dd>
</dl>

<dl>
<dd>

**connection_pool:** `typing.Optional[int]` — Sets connection pool size for Realtime Authorization
    
</dd>
</dl>

<dl>
<dd>

**postgres_changes_pool:** `typing.Optional[int]` — Sets connection pool size used to create Postgres Changes subscriptions
    
</dd>
</dl>

<dl>
<dd>

**max_concurrent_users:** `typing.Optional[int]` — Sets maximum number of concurrent users rate limit
    
</dd>
</dl>

<dl>
<dd>

**max_events_per_second:** `typing.Optional[int]` — Sets maximum number of events per second rate per channel limit
    
</dd>
</dl>

<dl>
<dd>

**max_bytes_per_second:** `typing.Optional[int]` — Sets maximum number of bytes per second rate per channel limit
    
</dd>
</dl>

<dl>
<dd>

**max_channels_per_client:** `typing.Optional[int]` — Sets maximum number of channels per client rate limit
    
</dd>
</dl>

<dl>
<dd>

**max_joins_per_second:** `typing.Optional[int]` — Sets maximum number of joins per second rate limit
    
</dd>
</dl>

<dl>
<dd>

**max_presence_events_per_second:** `typing.Optional[int]` — Sets maximum number of presence events per second rate limit
    
</dd>
</dl>

<dl>
<dd>

**max_payload_size_in_kb:** `typing.Optional[int]` — Sets maximum number of payload size in KB rate limit
    
</dd>
</dl>

<dl>
<dd>

**suspend:** `typing.Optional[bool]` — Disables the Realtime service for this project when true. Set to false to re-enable it.
    
</dd>
</dl>

<dl>
<dd>

**presence_enabled:** `typing.Optional[bool]` — Whether to enable presence
    
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

<details><summary><code>client.realtime.<a href="src/fern/realtime/client.py">v1shutdown_realtime</a>(...)</code></summary>
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

client.realtime.v1shutdown_realtime(
    ref="abcdefghijklmnopqrst",
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

**ref:** `str` — Project ref
    
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

