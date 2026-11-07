# Reference
## AgentTelemetry
<details><summary><code>client.agent_telemetry.<a href="src/fern/agent_telemetry/client.py">post_api_v1agent_telemetry</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TelemetryData
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.agent_telemetry.post_api_v1agent_telemetry(
    request=[
        TelemetryData()
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

**request:** `typing.List[TelemetryData]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent_telemetry.<a href="src/fern/agent_telemetry/client.py">post_api_v1agent_telemetry_standalone</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TelemetryData
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.agent_telemetry.post_api_v1agent_telemetry_standalone(
    request=[
        TelemetryData()
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

**request:** `typing.List[TelemetryData]` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.agents.<a href="src/fern/agents/client.py">get_api_v1agents_family</a>(...) -> AgentResponse</code></summary>
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

client.agents.get_api_v1agents_family(
    family="family",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**family:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Environments
<details><summary><code>client.environments.<a href="src/fern/environments/client.py">get_api_v1environments</a>(...) -> typing.List[CloudEnvironmentResult]</code></summary>
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

client.environments.get_api_v1environments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**plan_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">post_api_v1environments</a>(...) -> CloudEnvironmentResult</code></summary>
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

client.environments.post_api_v1environments(
    friendly_name="friendlyName",
    type="type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**friendly_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**access:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**analytics_tracking_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**auto_shutdown_delay_minutes:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**billable_owner:** `typing.Optional[BillableOwnerBody]` 
    
</dd>
</dl>

<dl>
<dd>

**connection:** `typing.Optional[ConnectionInfoBody]` 
    
</dd>
</dl>

<dl>
<dd>

**container_image:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**create_as_prebuild:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**dev_container_json:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**dev_container_path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**experimental_features:** `typing.Optional[ExperimentalFeaturesBody]` 
    
</dd>
</dl>

<dl>
<dd>

**features:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**git_hub_api_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**git_hub_app_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**git_hub_pfs_auth_endpoint:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**github_environment_endpoint:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**has_devcontainer_json:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**identity:** `typing.Optional[IdentityBody]` 
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**netmon_correlation_data:** `typing.Optional[NetmonCorrelationDataBody]` 
    
</dd>
</dl>

<dl>
<dd>

**personalization:** `typing.Optional[PersonalizationInfoBody]` 
    
</dd>
</dl>

<dl>
<dd>

**plan_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**platform:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**runtime_constraints:** `typing.Optional[RuntimeConstraintsBody]` 
    
</dd>
</dl>

<dl>
<dd>

**secrets:** `typing.Optional[typing.List[SecretDataBody]]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[SeedInfoBody]` 
    
</dd>
</dl>

<dl>
<dd>

**sku_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**test_account:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**user_tier:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**working_directory:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">get_environment_route</a>(...) -> CloudEnvironmentResult</code></summary>
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

client.environments.get_environment_route(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connect:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**pf_connect:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">delete_api_v1environments_environment_id</a>(...)</code></summary>
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

client.environments.delete_api_v1environments_environment_id(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">patch_api_v1environments_environment_id</a>(...) -> CloudEnvironmentResult</code></summary>
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

client.environments.patch_api_v1environments_environment_id(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**auto_shutdown_delay_minutes:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**failover_details:** `typing.Optional[FailoverDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**friendly_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**plan_access_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**plan_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sku_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">update_environment_route</a>(...) -> CloudEnvironmentResult</code></summary>
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

client.environments.update_environment_route(
    environment_id="environmentId",
    type="type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**payload:** `typing.Optional[EnvironmentRegistrationCallbackPayloadBody]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">get_api_v1environments_environment_id_archive</a>(...) -> UnfilteredCloudEnvironmentResult</code></summary>
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

client.environments.get_api_v1environments_environment_id_archive(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">post_api_v1environments_environment_id_archive</a>(...) -> CloudEnvironmentResult</code></summary>
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

client.environments.post_api_v1environments_environment_id_archive(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">post_api_v1environments_environment_id_export</a>(...) -> CloudEnvironmentResult</code></summary>
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

client.environments.post_api_v1environments_environment_id_export(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">patch_api_v1environments_environment_id_folder</a>(...) -> CloudEnvironmentResult</code></summary>
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

client.environments.patch_api_v1environments_environment_id_folder(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**recent_folder_paths:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">get_api_v1environments_environment_id_heartbeattoken</a>(...) -> CloudEnvironmentResult</code></summary>
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

client.environments.get_api_v1environments_environment_id_heartbeattoken(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">post_api_v1environments_environment_id_notify</a>(...) -> str</code></summary>
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

client.environments.post_api_v1environments_environment_id_notify(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**details:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**display_mode:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**modal:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">put_api_v1environments_environment_id_ports_port</a>(...)</code></summary>
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

client.environments.put_api_v1environments_environment_id_ports_port(
    environment_id="environmentId",
    port=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**port:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**privacy:** `typing.Optional[PrivacyEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**tunnel_type:** `typing.Optional[TunnelType]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">delete_api_v1environments_environment_id_ports_port</a>(...)</code></summary>
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

client.environments.delete_api_v1environments_environment_id_ports_port(
    environment_id="environmentId",
    port=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**port:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">patch_api_v1environments_environment_id_restore</a>(...)</code></summary>
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

client.environments.patch_api_v1environments_environment_id_restore(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">put_api_v1environments_environment_id_secrets</a>(...) -> CloudEnvironmentResult</code></summary>
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

client.environments.put_api_v1environments_environment_id_secrets(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**secrets:** `typing.Optional[typing.List[SecretDataBody]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">post_api_v1environments_environment_id_shutdown</a>(...) -> CloudEnvironmentResult</code></summary>
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

client.environments.post_api_v1environments_environment_id_shutdown(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">post_api_v1environments_environment_id_start</a>(...) -> CloudEnvironmentResult</code></summary>
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

client.environments.post_api_v1environments_environment_id_start(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**access:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">get_api_v1environments_environment_id_state</a>(...)</code></summary>
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

client.environments.get_api_v1environments_environment_id_state(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">get_api_v1environments_environment_id_updates</a>(...) -> CloudEnvironmentResult</code></summary>
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

client.environments.get_api_v1environments_environment_id_updates(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">get_api_v1geneva_actions_environments_storage_environment_id_or_friendly_name_target_blob</a>(...) -> str</code></summary>
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

client.environments.get_api_v1geneva_actions_environments_storage_environment_id_or_friendly_name_target_blob(
    environment_id_or_friendly_name="environmentIdOrFriendlyName",
    target_blob="targetBlob",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id_or_friendly_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**target_blob:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">get_api_v1geneva_actions_environments_environment_id</a>(...) -> CloudEnvironmentResult</code></summary>
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

client.environments.get_api_v1geneva_actions_environments_environment_id(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">delete_api_v1geneva_actions_environments_environment_id</a>(...)</code></summary>
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

client.environments.delete_api_v1geneva_actions_environments_environment_id(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**deletion_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">put_api_v1geneva_actions_environments_environment_id_archive</a>(...) -> CloudEnvironmentResult</code></summary>
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

client.environments.put_api_v1geneva_actions_environments_environment_id_archive(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">put_api_v1geneva_actions_environments_environment_id_shutdown</a>(...) -> CloudEnvironmentResult</code></summary>
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

client.environments.put_api_v1geneva_actions_environments_environment_id_shutdown(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">post_api_v1geneva_actions_environments_environment_id_upload_running_vm_logs</a>(...) -> VmLogsUploadInfo</code></summary>
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

client.environments.post_api_v1geneva_actions_environments_environment_id_upload_running_vm_logs(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.billing.<a href="src/fern/billing/client.py">post_api_v1geneva_actions_billing_resend</a>(...) -> BillSummary</code></summary>
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

client.billing.post_api_v1geneva_actions_billing_resend()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_time:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.billing.<a href="src/fern/billing/client.py">get_api_v1geneva_actions_billing_environment_id</a>(...) -> BillSummary</code></summary>
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

client.billing.get_api_v1geneva_actions_billing_environment_id(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.billing.<a href="src/fern/billing/client.py">get_api_v1geneva_actions_billing_environment_id_state_changes</a>(...) -> EnvironmentStateChange</code></summary>
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

client.billing.get_api_v1geneva_actions_billing_environment_id_state_changes(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.billing.<a href="src/fern/billing/client.py">post_api_v1geneva_actions_billing_environment_id_state_changes</a>(...) -> EnvironmentStateChange</code></summary>
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

client.billing.post_api_v1geneva_actions_billing_environment_id_state_changes(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**new_value:** `typing.Optional[CloudEnvironmentState]` 
    
</dd>
</dl>

<dl>
<dd>

**old_value:** `typing.Optional[CloudEnvironmentState]` 
    
</dd>
</dl>

<dl>
<dd>

**time:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Configuration
<details><summary><code>client.configuration.<a href="src/fern/configuration/client.py">post_api_v1geneva_actions_configuration_target</a>(...) -> SystemConfigurationResponse</code></summary>
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

client.configuration.post_api_v1geneva_actions_configuration_target(
    target="target",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**target:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.configuration.<a href="src/fern/configuration/client.py">get_api_v1geneva_actions_configuration_target_key</a>(...) -> SystemConfigurationResponse</code></summary>
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

client.configuration.get_api_v1geneva_actions_configuration_target_key(
    target="target",
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

**target:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.configuration.<a href="src/fern/configuration/client.py">delete_api_v1geneva_actions_configuration_target_key</a>(...)</code></summary>
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

client.configuration.delete_api_v1geneva_actions_configuration_target_key(
    target="target",
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

**target:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Pools
<details><summary><code>client.pools.<a href="src/fern/pools/client.py">post_api_v1geneva_actions_pools_change_resource_deletion_setting</a>(...) -> SystemConfigurationResponse</code></summary>
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

client.pools.post_api_v1geneva_actions_pools_change_resource_deletion_setting()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**comment:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**pool_code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**pool_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pools.<a href="src/fern/pools/client.py">post_api_v1geneva_actions_pools_pool_code_rotate_pool</a>(...)</code></summary>
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

client.pools.post_api_v1geneva_actions_pools_pool_code_rotate_pool(
    pool_code="poolCode",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pool_code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pools.<a href="src/fern/pools/client.py">post_api_v1geneva_actions_pools_target</a>(...) -> SystemConfigurationResponse</code></summary>
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

client.pools.post_api_v1geneva_actions_pools_target(
    target="target",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**target:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**max_target_count:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**min_target_count:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**pool_code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**pool_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**target_count:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pools.<a href="src/fern/pools/client.py">get_api_v1pools_default</a>(...) -> typing.List[PoolStatusResponseBody]</code></summary>
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

client.pools.get_api_v1pools_default()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sku_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Prebuilds
<details><summary><code>client.prebuilds.<a href="src/fern/prebuilds/client.py">post_api_v1geneva_actions_prebuilds_pools_createorupdatesettings</a>(...)</code></summary>
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

client.prebuilds.post_api_v1geneva_actions_prebuilds_pools_createorupdatesettings()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PoolSettingsBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prebuilds.<a href="src/fern/prebuilds/client.py">post_api_v1geneva_actions_prebuilds_pools_delete</a>(...)</code></summary>
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

client.prebuilds.post_api_v1geneva_actions_prebuilds_pools_delete()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PoolSettingsBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prebuilds.<a href="src/fern/prebuilds/client.py">post_api_v1prebuilds_pools_pool_id_instances</a>(...)</code></summary>
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

client.prebuilds.post_api_v1prebuilds_pools_pool_id_instances(
    pool_id="poolId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pool_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateEnvironmentPoolResourceBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prebuilds.<a href="src/fern/prebuilds/client.py">put_api_v1prebuilds_pools_pool_id_instances</a>(...)</code></summary>
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

client.prebuilds.put_api_v1prebuilds_pools_pool_id_instances(
    pool_id="poolId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pool_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateEnvironmentPoolResourceBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prebuilds.<a href="src/fern/prebuilds/client.py">get_template_info_route</a>(...) -> PrebuildTemplateInfoResult</code></summary>
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

client.prebuilds.get_template_info_route(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Privacy
<details><summary><code>client.privacy.<a href="src/fern/privacy/client.py">post_api_v1geneva_actions_privacy_refresh_profile_telemetry_properties</a>(...) -> RefreshProfileTelemetryPropertiesResponse</code></summary>
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

client.privacy.post_api_v1geneva_actions_privacy_refresh_profile_telemetry_properties()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**partner:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tenant_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**user_ids:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Resources
<details><summary><code>client.resources.<a href="src/fern/resources/client.py">post_api_v1geneva_actions_resources_resource_id_under_investigation</a>(...) -> UnderInvestigationResponseBody</code></summary>
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

client.resources.post_api_v1geneva_actions_resources_resource_id_under_investigation(
    resource_id="resourceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**resource_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## VnetPoolDefinitions
<details><summary><code>client.vnet_pool_definitions.<a href="src/fern/vnet_pool_definitions/client.py">post_api_v1geneva_actions_vnet_pool_definitions</a>(...)</code></summary>
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

client.vnet_pool_definitions.post_api_v1geneva_actions_vnet_pool_definitions(
    dimensions={},
    is_enabled=True,
    location=1,
    subtype=1,
    target_count=1,
    type=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PoolDefinitionInput` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vnet_pool_definitions.<a href="src/fern/vnet_pool_definitions/client.py">delete_api_v1geneva_actions_vnet_pool_definitions</a>(...)</code></summary>
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

client.vnet_pool_definitions.delete_api_v1geneva_actions_vnet_pool_definitions(
    dimensions={},
    is_enabled=True,
    location=1,
    subtype=1,
    target_count=1,
    type=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PoolDefinitionInput` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## HeartBeat
<details><summary><code>client.heart_beat.<a href="src/fern/heart_beat/client.py">post_api_v1heart_beat</a>(...)</code></summary>
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

client.heart_beat.post_api_v1heart_beat()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_version:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**collected_data_list:** `typing.Optional[typing.List[CollectedData]]` 
    
</dd>
</dl>

<dl>
<dd>

**environment_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**resource_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**time_stamp:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Locations
<details><summary><code>client.locations.<a href="src/fern/locations/client.py">get_api_v1locations</a>() -> LocationsResult</code></summary>
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

client.locations.get_api_v1locations()

```
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

<details><summary><code>client.locations.<a href="src/fern/locations/client.py">get_api_v1locations_location</a>(...) -> LocationInfoResult</code></summary>
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

client.locations.get_api_v1locations_location(
    location="location",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**plan_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sas
<details><summary><code>client.sas.<a href="src/fern/sas/client.py">get_api_v1sas</a>() -> typing.List[ScopedSecretResultBody]</code></summary>
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

client.sas.get_api_v1sas()

```
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
<details><summary><code>client.secrets.<a href="src/fern/secrets/client.py">get_api_v1secrets</a>(...) -> typing.List[ScopedSecretResultBody]</code></summary>
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

client.secrets.get_api_v1secrets()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**plan_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.secrets.<a href="src/fern/secrets/client.py">post_api_v1secrets</a>(...) -> ScopedSecretResultBody</code></summary>
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

client.secrets.post_api_v1secrets()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**plan_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.List[SecretFilterBody]]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[SecretScope]` 
    
</dd>
</dl>

<dl>
<dd>

**secret_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[SecretType]` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.secrets.<a href="src/fern/secrets/client.py">put_api_v1secrets_secret_id</a>(...) -> ScopedSecretResultBody</code></summary>
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

client.secrets.put_api_v1secrets_secret_id(
    secret_id="secretId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**secret_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**plan_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.List[SecretFilterBody]]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[SecretScope]` 
    
</dd>
</dl>

<dl>
<dd>

**secret_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.secrets.<a href="src/fern/secrets/client.py">delete_api_v1secrets_secret_id</a>(...)</code></summary>
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

client.secrets.delete_api_v1secrets_secret_id(
    secret_id="secretId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**secret_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**plan_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[SecretScope]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tenant
<details><summary><code>client.tenant.<a href="src/fern/tenant/client.py">get_api_v1tenant_tenant_id</a>(...) -> TenantInfoResult</code></summary>
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

client.tenant.get_api_v1tenant_tenant_id(
    tenant_id="tenantId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenant.<a href="src/fern/tenant/client.py">put_api_v1tenant_tenant_id</a>(...)</code></summary>
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

client.tenant.put_api_v1tenant_tenant_id(
    tenant_id="tenantId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenant.<a href="src/fern/tenant/client.py">delete_api_v1tenant_tenant_id</a>(...)</code></summary>
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

client.tenant.delete_api_v1tenant_tenant_id(
    tenant_id="tenantId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tokens
<details><summary><code>client.tokens.<a href="src/fern/tokens/client.py">post_api_v1tokens_plans_plan_name_delete_all_codespaces</a>(...)</code></summary>
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

client.tokens.post_api_v1tokens_plans_plan_name_delete_all_codespaces(
    plan_name="planName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**plan_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expiration:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/fern/tokens/client.py">post_api_v1tokens_plans_plan_name_read_all_codespaces</a>(...)</code></summary>
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

client.tokens.post_api_v1tokens_plans_plan_name_read_all_codespaces(
    plan_name="planName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**plan_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expiration:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/fern/tokens/client.py">post_api_v1tokens_plans_plan_name_write_codespaces</a>(...)</code></summary>
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

client.tokens.post_api_v1tokens_plans_plan_name_write_codespaces(
    plan_name="planName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**plan_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expiration:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/fern/tokens/client.py">post_api_v1tokens_plans_plan_name_write_delegates</a>(...)</code></summary>
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

client.tokens.post_api_v1tokens_plans_plan_name_write_delegates(
    plan_name="planName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**plan_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `IssueDelegatePlanAccessTokenBody` 
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/fern/tokens/client.py">put_api_v1tokens_subscriptions_subscription_id_resource_groups_resource_group_providers_provider_namespace_plans_resource_name</a>(...)</code></summary>
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

client.tokens.put_api_v1tokens_subscriptions_subscription_id_resource_groups_resource_group_providers_provider_namespace_plans_resource_name(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    provider_namespace="providerNamespace",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**provider_namespace:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PlanResource` 
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[PlanResourceHeaders]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tunnel
<details><summary><code>client.tunnel.<a href="src/fern/tunnel/client.py">get_api_v1tunnel_environment_id_port_info</a>(...) -> TunnelPortInfoResult</code></summary>
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

client.tunnel.get_api_v1tunnel_environment_id_port_info(
    environment_id="environmentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**port_number:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## UserSubscriptions
<details><summary><code>client.user_subscriptions.<a href="src/fern/user_subscriptions/client.py">post_api_v1user_subscriptions</a>(...)</code></summary>
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

client.user_subscriptions.post_api_v1user_subscriptions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_subscriptions.<a href="src/fern/user_subscriptions/client.py">delete_api_v1user_subscriptions</a>(...)</code></summary>
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

client.user_subscriptions.delete_api_v1user_subscriptions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## NetworkSettings
<details><summary><code>client.network_settings.<a href="src/fern/network_settings/client.py">put_api_v1subscriptions_subscription_id_providers_git_hub_network_resource_type_subscription_life_cycle_notification</a>(...)</code></summary>
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

client.network_settings.put_api_v1subscriptions_subscription_id_providers_git_hub_network_resource_type_subscription_life_cycle_notification(
    subscription_id="subscriptionId",
    resource_type="resourceType",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `RpSubscriptionNotification` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_settings.<a href="src/fern/network_settings/client.py">post_api_v1subscriptions_subscription_id_providers_git_hub_network_resource_type_resource_read_begin</a>(...)</code></summary>
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

client.network_settings.post_api_v1subscriptions_subscription_id_providers_git_hub_network_resource_type_resource_read_begin(
    subscription_id="subscriptionId",
    resource_type="resourceType",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `NetworkSettingsResourceList` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_settings.<a href="src/fern/network_settings/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_read_begin</a>(...)</code></summary>
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

client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_read_begin(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_type="resourceType",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `NetworkSettingsResourceList` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_settings.<a href="src/fern/network_settings/client.py">put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name</a>(...)</code></summary>
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

client.network_settings.put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_type="resourceType",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `NetworkSettingsResource` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_settings.<a href="src/fern/network_settings/client.py">delete_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name</a>(...)</code></summary>
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

client.network_settings.delete_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_type="resourceType",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `NetworkSettingsResource` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_settings.<a href="src/fern/network_settings/client.py">patch_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name</a>(...)</code></summary>
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

client.network_settings.patch_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_type="resourceType",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `NetworkSettingsResource` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_settings.<a href="src/fern/network_settings/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_creation_completed</a>(...)</code></summary>
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

client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_creation_completed(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_type="resourceType",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_settings.<a href="src/fern/network_settings/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_creation_validate</a>(...)</code></summary>
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

client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_creation_validate(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_type="resourceType",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `NetworkSettingsResource` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_settings.<a href="src/fern/network_settings/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_deletion_completed</a>(...)</code></summary>
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

client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_deletion_completed(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_type="resourceType",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_settings.<a href="src/fern/network_settings/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_deletion_validate</a>(...)</code></summary>
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

client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_deletion_validate(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_type="resourceType",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `NetworkSettingsResource` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_settings.<a href="src/fern/network_settings/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_patch_completed</a>(...)</code></summary>
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

client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_patch_completed(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_type="resourceType",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_settings.<a href="src/fern/network_settings/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_patch_validate</a>(...)</code></summary>
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

client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_patch_validate(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_type="resourceType",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `NetworkSettingsResource` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.network_settings.<a href="src/fern/network_settings/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_read_begin</a>(...)</code></summary>
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

client.network_settings.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_git_hub_network_resource_type_resource_name_resource_read_begin(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_type="resourceType",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `NetworkSettingsResource` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Plans
<details><summary><code>client.plans.<a href="src/fern/plans/client.py">put_api_v1subscriptions_subscription_id_providers_microsoft_codespaces_plans_subscription_life_cycle_notification</a>(...)</code></summary>
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

client.plans.put_api_v1subscriptions_subscription_id_providers_microsoft_codespaces_plans_subscription_life_cycle_notification(
    subscription_id="subscriptionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `RpSubscriptionNotification` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_providers_microsoft_codespaces_plans_resource_read_begin</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_providers_microsoft_codespaces_plans_resource_read_begin(
    subscription_id="subscriptionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PlanResourceList` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">put_api_v1subscriptions_subscription_id_providers_microsoft_vs_online_plans_subscription_life_cycle_notification</a>(...)</code></summary>
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

client.plans.put_api_v1subscriptions_subscription_id_providers_microsoft_vs_online_plans_subscription_life_cycle_notification(
    subscription_id="subscriptionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `RpSubscriptionNotification` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_providers_microsoft_vs_online_plans_resource_read_begin</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_providers_microsoft_vs_online_plans_resource_read_begin(
    subscription_id="subscriptionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PlanResourceList` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_read_begin</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_read_begin(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PlanResourceList` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name</a>(...)</code></summary>
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

client.plans.put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PlanResource` 
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[PlanResourceHeaders]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_all_codespaces</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_all_codespaces(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expiration:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_all_environments</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_all_environments(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expiration:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_all_codespaces</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_all_codespaces(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expiration:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_all_environments</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_all_environments(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expiration:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_delegates</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_read_delegates(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_creation_completed</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_creation_completed(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_creation_validate</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_creation_validate(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PlanResource` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_deletion_validate</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_deletion_validate(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_patch_completed</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_patch_completed(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PlanResourceUpdateBody` 
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[PlanResourceHeaders]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_patch_validate</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_patch_validate(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PlanResourceUpdateBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_read_begin</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_resource_read_begin(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PlanResource` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_codespaces</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_codespaces(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expiration:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_delegates</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_delegates(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `IssueDelegatePlanAccessTokenBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_environments</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_codespaces_plans_resource_name_write_environments(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expiration:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_read_begin</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_read_begin(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PlanResourceList` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name</a>(...)</code></summary>
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

client.plans.put_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PlanResource` 
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[PlanResourceHeaders]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_all_codespaces</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_all_codespaces(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expiration:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_all_environments</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_all_environments(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expiration:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_all_codespaces</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_all_codespaces(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expiration:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_all_environments</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_all_environments(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expiration:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_delegates</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_read_delegates(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_creation_completed</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_creation_completed(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_creation_validate</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_creation_validate(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PlanResource` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_deletion_validate</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_deletion_validate(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_patch_completed</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_patch_completed(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PlanResourceUpdateBody` 
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[PlanResourceHeaders]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_patch_validate</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_patch_validate(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PlanResourceUpdateBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_read_begin</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_resource_read_begin(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PlanResource` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_codespaces</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_codespaces(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expiration:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_delegates</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_delegates(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `IssueDelegatePlanAccessTokenBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_environments</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_groups_resource_group_providers_microsoft_vs_online_plans_resource_name_write_environments(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expiration:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_delegates</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_group_providers_microsoft_codespaces_plans_resource_name_delete_delegates(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/fern/plans/client.py">post_api_v1subscriptions_subscription_id_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_delegates</a>(...)</code></summary>
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

client.plans.post_api_v1subscriptions_subscription_id_resource_group_providers_microsoft_vs_online_plans_resource_name_delete_delegates(
    subscription_id="subscriptionId",
    resource_group="resourceGroup",
    resource_name="resourceName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Pool
<details><summary><code>client.pool.<a href="src/fern/pool/client.py">get_api_v1tenant_tenant_id_pool_pool_name</a>(...) -> PoolResult</code></summary>
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

client.pool.get_api_v1tenant_tenant_id_pool_pool_name(
    tenant_id="tenantId",
    pool_name="poolName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**pool_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pool.<a href="src/fern/pool/client.py">put_api_v1tenant_tenant_id_pool_pool_name</a>(...) -> PoolResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, VmSpecs
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pool.put_api_v1tenant_tenant_id_pool_pool_name(
    tenant_id="tenantId",
    pool_name="poolName",
    pool_group_name="poolGroupName",
    vm_specs=VmSpecs(
        disk_type=1,
        image_resource_id="imageResourceId",
        size="size",
        subnet_resource_id="subnetResourceId",
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

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**pool_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateOrUpdatePoolBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pool.<a href="src/fern/pool/client.py">delete_api_v1tenant_tenant_id_pool_pool_name</a>(...)</code></summary>
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

client.pool.delete_api_v1tenant_tenant_id_pool_pool_name(
    tenant_id="tenantId",
    pool_name="poolName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**pool_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pool.<a href="src/fern/pool/client.py">patch_api_v1tenant_tenant_id_pool_pool_name</a>(...) -> PoolResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, VmSpecs
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pool.patch_api_v1tenant_tenant_id_pool_pool_name(
    tenant_id="tenantId",
    pool_name="poolName",
    pool_group_name="poolGroupName",
    vm_specs=VmSpecs(
        disk_type=1,
        image_resource_id="imageResourceId",
        size="size",
        subnet_resource_id="subnetResourceId",
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

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**pool_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateOrUpdatePoolBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PoolGroup
<details><summary><code>client.pool_group.<a href="src/fern/pool_group/client.py">get_api_v1tenant_tenant_id_pool_group_pool_group_name</a>(...) -> PoolGroupResult</code></summary>
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

client.pool_group.get_api_v1tenant_tenant_id_pool_group_pool_group_name(
    tenant_id="tenantId",
    pool_group_name="poolGroupName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**pool_group_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pool_group.<a href="src/fern/pool_group/client.py">put_api_v1tenant_tenant_id_pool_group_pool_group_name</a>(...)</code></summary>
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

client.pool_group.put_api_v1tenant_tenant_id_pool_group_pool_group_name(
    tenant_id="tenantId",
    pool_group_name="poolGroupName",
    display_name="displayName",
    region=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**pool_group_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `AzureLocation` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pool_group.<a href="src/fern/pool_group/client.py">delete_api_v1tenant_tenant_id_pool_group_pool_group_name</a>(...)</code></summary>
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

client.pool_group.delete_api_v1tenant_tenant_id_pool_group_pool_group_name(
    tenant_id="tenantId",
    pool_group_name="poolGroupName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**pool_group_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pool_group.<a href="src/fern/pool_group/client.py">patch_api_v1tenant_tenant_id_pool_group_pool_group_name</a>(...)</code></summary>
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

client.pool_group.patch_api_v1tenant_tenant_id_pool_group_pool_group_name(
    tenant_id="tenantId",
    pool_group_name="poolGroupName",
    display_name="displayName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**pool_group_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Vm
<details><summary><code>client.vm.<a href="src/fern/vm/client.py">get_api_v1tenant_tenant_id_pool_pool_name_vm</a>(...) -> typing.List[VmResult]</code></summary>
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

client.vm.get_api_v1tenant_tenant_id_pool_pool_name_vm(
    tenant_id="tenantId",
    pool_name="poolName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**pool_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vm.<a href="src/fern/vm/client.py">get_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name</a>(...) -> VmResult</code></summary>
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

client.vm.get_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
    tenant_id="tenantId",
    pool_name="poolName",
    vm_name="vmName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**pool_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**vm_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vm.<a href="src/fern/vm/client.py">put_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name</a>(...) -> VmResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, UserIdentity
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.vm.put_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
    tenant_id="tenantId",
    pool_name="poolName",
    vm_name="vmName",
    user=UserIdentity(
        user_principal_name="userPrincipalName",
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

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**pool_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**vm_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**user:** `UserIdentity` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vm.<a href="src/fern/vm/client.py">delete_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name</a>(...)</code></summary>
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

client.vm.delete_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
    tenant_id="tenantId",
    pool_name="poolName",
    vm_name="vmName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**pool_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**vm_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vm.<a href="src/fern/vm/client.py">post_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name_start</a>(...)</code></summary>
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

client.vm.post_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name_start(
    tenant_id="tenantId",
    pool_name="poolName",
    vm_name="vmName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**pool_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**vm_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vm.<a href="src/fern/vm/client.py">post_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name_stop</a>(...)</code></summary>
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

client.vm.post_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name_stop(
    tenant_id="tenantId",
    pool_name="poolName",
    vm_name="vmName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**pool_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**vm_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PrebuildsV
<details><summary><code>client.prebuilds_v.<a href="src/fern/prebuilds_v/client.py">post_api_v2prebuilds_delete</a>(...)</code></summary>
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

client.prebuilds_v.post_api_v2prebuilds_delete(
    branch_name="branchName",
    repo_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**branch_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**repo_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**dev_container_path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prebuild_configuration_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prebuilds_v.<a href="src/fern/prebuilds_v/client.py">delete_api_v2prebuilds_repository_repo_id_branch_branch_name</a>(...)</code></summary>
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

client.prebuilds_v.delete_api_v2prebuilds_repository_repo_id_branch_branch_name(
    repo_id=1000000,
    branch_name="branchName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**repo_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**branch_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prebuilds_v.<a href="src/fern/prebuilds_v/client.py">post_api_v2prebuilds_templates</a>(...) -> CreateTemplateResult</code></summary>
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

client.prebuilds_v.post_api_v2prebuilds_templates(
    friendly_name="friendlyName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**friendly_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**dev_container_path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**experimental_features:** `typing.Optional[ExperimentalFeaturesBody]` 
    
</dd>
</dl>

<dl>
<dd>

**features:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**git_hub_prebuild_instance_endpoint:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**git_hub_prebuild_template_endpoint:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**plan_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[SeedInfoBody]` 
    
</dd>
</dl>

<dl>
<dd>

**storage_type:** `typing.Optional[StorageType]` 
    
</dd>
</dl>

<dl>
<dd>

**template_info:** `typing.Optional[PrebuildTemplateInfo]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prebuilds_v.<a href="src/fern/prebuilds_v/client.py">get_prebuild_readiness_skus_route</a>(...) -> PrebuildReadinessResult</code></summary>
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

client.prebuilds_v.get_prebuild_readiness_skus_route(
    repo_id="repoId",
    branch_name="branchName",
    prebuild_hash="prebuildHash",
    location="location",
    dev_container_path="devContainerPath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**repo_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**branch_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**prebuild_hash:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**location:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**dev_container_path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**storage_type:** `typing.Optional[StorageType]` 
    
</dd>
</dl>

<dl>
<dd>

**fast_path_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prebuilds_v.<a href="src/fern/prebuilds_v/client.py">post_api_v2prebuilds_templates_updatemaxversions</a>(...)</code></summary>
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

client.prebuilds_v.post_api_v2prebuilds_templates_updatemaxversions(
    branch_name="branchName",
    max_prebuild_template_versions=1,
    repo_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**branch_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**max_prebuild_template_versions:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**repo_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**dev_container_path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prebuilds_v.<a href="src/fern/prebuilds_v/client.py">post_api_v2prebuilds_templates_template_id_updatestatus</a>(...)</code></summary>
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

client.prebuilds_v.post_api_v2prebuilds_templates_template_id_updatestatus(
    template_id="templateId",
    is_success=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**is_success:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Health
<details><summary><code>client.health.<a href="src/fern/health/client.py">get_health</a>()</code></summary>
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

client.health.get_health()

```
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

## Netmon
<details><summary><code>client.netmon.<a href="src/fern/netmon/client.py">get_internal_netmon_correlation</a>(...) -> str</code></summary>
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

client.netmon.get_internal_netmon_correlation()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mac_address:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Warmup
<details><summary><code>client.warmup.<a href="src/fern/warmup/client.py">get_warmup</a>()</code></summary>
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

client.warmup.get_warmup()

```
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

