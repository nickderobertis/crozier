# Reference
## attempt
<details><summary><code>client.attempt.<a href="src/fern/attempt/client.py">save_stats</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import AttemptStats, FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.attempt.save_stats(
    attempt_number=1,
    job_id=1000000,
    stats=AttemptStats(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attempt_number:** `AttemptNumber` 
    
</dd>
</dl>

<dl>
<dd>

**job_id:** `JobId` 
    
</dd>
</dl>

<dl>
<dd>

**stats:** `AttemptStats` 
    
</dd>
</dl>

<dl>
<dd>

**stream_stats:** `typing.Optional[typing.Sequence[AttemptStreamStats]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attempt.<a href="src/fern/attempt/client.py">save_sync_config</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import AttemptSyncConfig, FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.attempt.save_sync_config(
    attempt_number=1,
    job_id=1000000,
    sync_config=AttemptSyncConfig(
        destination_configuration={"user": "charles"},
        source_configuration={"user": "charles"},
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

**attempt_number:** `AttemptNumber` 
    
</dd>
</dl>

<dl>
<dd>

**job_id:** `JobId` 
    
</dd>
</dl>

<dl>
<dd>

**sync_config:** `AttemptSyncConfig` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attempt.<a href="src/fern/attempt/client.py">set_workflow_in_attempt</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.attempt.set_workflow_in_attempt(
    attempt_number=1,
    job_id=1000000,
    workflow_id="workflowId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attempt_number:** `AttemptNumber` 
    
</dd>
</dl>

<dl>
<dd>

**job_id:** `JobId` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_id:** `WorkflowId` 
    
</dd>
</dl>

<dl>
<dd>

**processing_task_queue:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## connection
<details><summary><code>client.connection.<a href="src/fern/connection/client.py">create_connection</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import ConnectionStatus, FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.connection.create_connection(
    destination_id="destinationId",
    source_id="sourceId",
    status=ConnectionStatus.ACTIVE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**destination_id:** `DestinationId` 
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `SourceId` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `ConnectionStatus` 
    
</dd>
</dl>

<dl>
<dd>

**geography:** `typing.Optional[Geography]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Optional name of the connection
    
</dd>
</dl>

<dl>
<dd>

**namespace_definition:** `typing.Optional[NamespaceDefinitionType]` 
    
</dd>
</dl>

<dl>
<dd>

**namespace_format:** `typing.Optional[str]` — Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.
    
</dd>
</dl>

<dl>
<dd>

**non_breaking_changes_preference:** `typing.Optional[NonBreakingChangesPreference]` 
    
</dd>
</dl>

<dl>
<dd>

**notify_schema_changes:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**operation_ids:** `typing.Optional[typing.Sequence[OperationId]]` 
    
</dd>
</dl>

<dl>
<dd>

**prefix:** `typing.Optional[str]` — Prefix that will be prepended to the name of each stream when it is written to the destination.
    
</dd>
</dl>

<dl>
<dd>

**resource_requirements:** `typing.Optional[ResourceRequirements]` 
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[ConnectionSchedule]` 
    
</dd>
</dl>

<dl>
<dd>

**schedule_data:** `typing.Optional[ConnectionScheduleData]` 
    
</dd>
</dl>

<dl>
<dd>

**schedule_type:** `typing.Optional[ConnectionScheduleType]` 
    
</dd>
</dl>

<dl>
<dd>

**source_catalog_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sync_catalog:** `typing.Optional[AirbyteCatalog]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connection.<a href="src/fern/connection/client.py">delete_connection</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.connection.delete_connection(
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `ConnectionId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connection.<a href="src/fern/connection/client.py">get_connection</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.connection.get_connection(
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `ConnectionId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connection.<a href="src/fern/connection/client.py">list_connections_for_workspace</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List connections for workspace. Does not return deleted connections.
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
    token="YOUR_TOKEN",
)
client.connection.list_connections_for_workspace(
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connection.<a href="src/fern/connection/client.py">list_all_connections_for_workspace</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List connections for workspace, including deleted connections.
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
    token="YOUR_TOKEN",
)
client.connection.list_all_connections_for_workspace(
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connection.<a href="src/fern/connection/client.py">reset_connection</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.connection.reset_connection(
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `ConnectionId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connection.<a href="src/fern/connection/client.py">search_connections</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.connection.search_connections()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `typing.Optional[ConnectionId]` 
    
</dd>
</dl>

<dl>
<dd>

**destination:** `typing.Optional[DestinationSearch]` 
    
</dd>
</dl>

<dl>
<dd>

**destination_id:** `typing.Optional[DestinationId]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**namespace_definition:** `typing.Optional[NamespaceDefinitionType]` 
    
</dd>
</dl>

<dl>
<dd>

**namespace_format:** `typing.Optional[str]` — Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.
    
</dd>
</dl>

<dl>
<dd>

**prefix:** `typing.Optional[str]` — Prefix that will be prepended to the name of each stream when it is written to the destination.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[ConnectionSchedule]` 
    
</dd>
</dl>

<dl>
<dd>

**schedule_data:** `typing.Optional[ConnectionScheduleData]` 
    
</dd>
</dl>

<dl>
<dd>

**schedule_type:** `typing.Optional[ConnectionScheduleType]` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[SourceSearch]` 
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `typing.Optional[SourceId]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ConnectionStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connection.<a href="src/fern/connection/client.py">sync_connection</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.connection.sync_connection(
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `ConnectionId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connection.<a href="src/fern/connection/client.py">update_connection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply a patch-style update to a connection. Only fields present on the update request body will be updated.
Note that if a catalog is present in the request body, the connection's entire catalog will be replaced
with the catalog from the request. This means that to modify a single stream, the entire new catalog
containing the updated stream needs to be sent.
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
    token="YOUR_TOKEN",
)
client.connection.update_connection(
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `ConnectionId` 
    
</dd>
</dl>

<dl>
<dd>

**breaking_change:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**geography:** `typing.Optional[Geography]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name that will be set to this connection
    
</dd>
</dl>

<dl>
<dd>

**namespace_definition:** `typing.Optional[NamespaceDefinitionType]` 
    
</dd>
</dl>

<dl>
<dd>

**namespace_format:** `typing.Optional[str]` — Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.
    
</dd>
</dl>

<dl>
<dd>

**non_breaking_changes_preference:** `typing.Optional[NonBreakingChangesPreference]` 
    
</dd>
</dl>

<dl>
<dd>

**notify_schema_changes:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**operation_ids:** `typing.Optional[typing.Sequence[OperationId]]` 
    
</dd>
</dl>

<dl>
<dd>

**prefix:** `typing.Optional[str]` — Prefix that will be prepended to the name of each stream when it is written to the destination.
    
</dd>
</dl>

<dl>
<dd>

**resource_requirements:** `typing.Optional[ResourceRequirements]` 
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[ConnectionSchedule]` 
    
</dd>
</dl>

<dl>
<dd>

**schedule_data:** `typing.Optional[ConnectionScheduleData]` 
    
</dd>
</dl>

<dl>
<dd>

**schedule_type:** `typing.Optional[ConnectionScheduleType]` 
    
</dd>
</dl>

<dl>
<dd>

**source_catalog_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ConnectionStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**sync_catalog:** `typing.Optional[AirbyteCatalog]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## destination_definition_specification
<details><summary><code>client.destination_definition_specification.<a href="src/fern/destination_definition_specification/client.py">get_destination_definition_specification</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination_definition_specification.get_destination_definition_specification(
    destination_definition_id="destinationDefinitionId",
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**destination_definition_id:** `DestinationDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## destination_definition
<details><summary><code>client.destination_definition.<a href="src/fern/destination_definition/client.py">create_custom_destination_definition</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import DestinationDefinitionCreate, FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.destination_definition.create_custom_destination_definition(
    destination_definition=DestinationDefinitionCreate(
        docker_image_tag="dockerImageTag",
        docker_repository="dockerRepository",
        documentation_url="documentationUrl",
        name="name",
    ),
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**destination_definition:** `DestinationDefinitionCreate` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.destination_definition.<a href="src/fern/destination_definition/client.py">delete_destination_definition</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination_definition.delete_destination_definition(
    destination_definition_id="destinationDefinitionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**destination_definition_id:** `DestinationDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.destination_definition.<a href="src/fern/destination_definition/client.py">get_destination_definition</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination_definition.get_destination_definition(
    destination_definition_id="destinationDefinitionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**destination_definition_id:** `DestinationDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.destination_definition.<a href="src/fern/destination_definition/client.py">get_destination_definition_for_workspace</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination_definition.get_destination_definition_for_workspace(
    destination_definition_id="destinationDefinitionId",
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**destination_definition_id:** `DestinationDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.destination_definition.<a href="src/fern/destination_definition/client.py">grant_destination_definition_to_workspace</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination_definition.grant_destination_definition_to_workspace(
    destination_definition_id="destinationDefinitionId",
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**destination_definition_id:** `DestinationDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.destination_definition.<a href="src/fern/destination_definition/client.py">list_destination_definitions</a>()</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination_definition.list_destination_definitions()

```
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

<details><summary><code>client.destination_definition.<a href="src/fern/destination_definition/client.py">list_destination_definitions_for_workspace</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination_definition.list_destination_definitions_for_workspace(
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.destination_definition.<a href="src/fern/destination_definition/client.py">list_latest_destination_definitions</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guaranteed to retrieve the latest information on supported destinations.
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
    token="YOUR_TOKEN",
)
client.destination_definition.list_latest_destination_definitions()

```
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

<details><summary><code>client.destination_definition.<a href="src/fern/destination_definition/client.py">list_private_destination_definitions</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination_definition.list_private_destination_definitions(
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.destination_definition.<a href="src/fern/destination_definition/client.py">revoke_destination_definition_from_workspace</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination_definition.revoke_destination_definition_from_workspace(
    destination_definition_id="destinationDefinitionId",
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**destination_definition_id:** `DestinationDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.destination_definition.<a href="src/fern/destination_definition/client.py">update_destination_definition</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination_definition.update_destination_definition(
    destination_definition_id="destinationDefinitionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**destination_definition_id:** `DestinationDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**docker_image_tag:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**resource_requirements:** `typing.Optional[ActorDefinitionResourceRequirements]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## destination_oauth
<details><summary><code>client.destination_oauth.<a href="src/fern/destination_oauth/client.py">complete_destination_o_auth</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination_oauth.complete_destination_o_auth(
    destination_definition_id="destinationDefinitionId",
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**destination_definition_id:** `DestinationDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**destination_id:** `typing.Optional[DestinationId]` 
    
</dd>
</dl>

<dl>
<dd>

**o_auth_input_configuration:** `typing.Optional[OAuthInputConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**query_params:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The query parameters present in the redirect URL after a user granted consent e.g auth code
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — When completing OAuth flow to gain an access token, some API sometimes requires to verify that the app re-send the redirectUrl that was used when consent was given.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.destination_oauth.<a href="src/fern/destination_oauth/client.py">get_destination_o_auth_consent</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination_oauth.get_destination_o_auth_consent(
    destination_definition_id="destinationDefinitionId",
    redirect_url="redirectUrl",
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**destination_definition_id:** `DestinationDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `str` — The url to redirect to after getting the user consent
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**destination_id:** `typing.Optional[DestinationId]` 
    
</dd>
</dl>

<dl>
<dd>

**o_auth_input_configuration:** `typing.Optional[OAuthInputConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.destination_oauth.<a href="src/fern/destination_oauth/client.py">set_instancewide_destination_oauth_params</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination_oauth.set_instancewide_destination_oauth_params(
    destination_definition_id="destinationDefinitionId",
    params={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**destination_definition_id:** `DestinationDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Dict[str, typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## destination
<details><summary><code>client.destination.<a href="src/fern/destination/client.py">check_connection_to_destination</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination.check_connection_to_destination(
    destination_id="destinationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**destination_id:** `DestinationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.destination.<a href="src/fern/destination/client.py">check_connection_to_destination_for_update</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination.check_connection_to_destination_for_update(
    connection_configuration={"user": "charles"},
    destination_id="destinationId",
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

**connection_configuration:** `DestinationConfiguration` 
    
</dd>
</dl>

<dl>
<dd>

**destination_id:** `DestinationId` 
    
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

<details><summary><code>client.destination.<a href="src/fern/destination/client.py">clone_destination</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination.clone_destination(
    destination_clone_id="destinationCloneId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**destination_clone_id:** `DestinationId` 
    
</dd>
</dl>

<dl>
<dd>

**destination_configuration:** `typing.Optional[DestinationCloneConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.destination.<a href="src/fern/destination/client.py">create_destination</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination.create_destination(
    connection_configuration={"user": "charles"},
    destination_definition_id="destinationDefinitionId",
    name="name",
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_configuration:** `DestinationConfiguration` 
    
</dd>
</dl>

<dl>
<dd>

**destination_definition_id:** `DestinationDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.destination.<a href="src/fern/destination/client.py">delete_destination</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination.delete_destination(
    destination_id="destinationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**destination_id:** `DestinationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.destination.<a href="src/fern/destination/client.py">get_destination</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination.get_destination(
    destination_id="destinationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**destination_id:** `DestinationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.destination.<a href="src/fern/destination/client.py">list_destinations_for_workspace</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination.list_destinations_for_workspace(
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.destination.<a href="src/fern/destination/client.py">search_destinations</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination.search_destinations()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_configuration:** `typing.Optional[DestinationConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**destination_definition_id:** `typing.Optional[DestinationDefinitionId]` 
    
</dd>
</dl>

<dl>
<dd>

**destination_id:** `typing.Optional[DestinationId]` 
    
</dd>
</dl>

<dl>
<dd>

**destination_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `typing.Optional[WorkspaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.destination.<a href="src/fern/destination/client.py">update_destination</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.destination.update_destination(
    connection_configuration={"user": "charles"},
    destination_id="destinationId",
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

**connection_configuration:** `DestinationConfiguration` 
    
</dd>
</dl>

<dl>
<dd>

**destination_id:** `DestinationId` 
    
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

## health
<details><summary><code>client.health.<a href="src/fern/health/client.py">get_health_check</a>()</code></summary>
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
    token="YOUR_TOKEN",
)
client.health.get_health_check()

```
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

## Jobs
<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">cancel_job</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.jobs.cancel_job(
    id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `JobId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">get_job_info</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.jobs.get_job_info(
    id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `JobId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">get_job_debug_info</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.jobs.get_job_debug_info(
    id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `JobId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">get_last_replication_job</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.jobs.get_last_replication_job(
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `ConnectionId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">get_job_info_light</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.jobs.get_job_info_light(
    id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `JobId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">get_attempt_normalization_statuses_for_job</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.jobs.get_attempt_normalization_statuses_for_job(
    id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `JobId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">list_jobs_for</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, JobConfigType

client = FernApi(
    token="YOUR_TOKEN",
)
client.jobs.list_jobs_for(
    config_id="configId",
    config_types=[JobConfigType.CHECK_CONNECTION_SOURCE],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**config_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**config_types:** `typing.Sequence[JobConfigType]` 
    
</dd>
</dl>

<dl>
<dd>

**including_job_id:** `typing.Optional[JobId]` — If the job with this ID exists for the specified connection, returns the number of pages of jobs necessary to include this job. Returns an empty list if this job is specified and cannot be found in this connection.
    
</dd>
</dl>

<dl>
<dd>

**pagination:** `typing.Optional[Pagination]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Logs
<details><summary><code>client.logs.<a href="src/fern/logs/client.py">get_logs</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, LogType

client = FernApi(
    token="YOUR_TOKEN",
)
client.logs.get_logs(
    log_type=LogType.SERVER,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**log_type:** `LogType` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Notifications
<details><summary><code>client.notifications.<a href="src/fern/notifications/client.py">try_notification_config</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, NotificationType

client = FernApi(
    token="YOUR_TOKEN",
)
client.notifications.try_notification_config(
    notification_type=NotificationType.SLACK,
    send_on_failure=True,
    send_on_success=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**notification_type:** `NotificationType` 
    
</dd>
</dl>

<dl>
<dd>

**send_on_failure:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**send_on_success:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**customerio_configuration:** `typing.Optional[CustomerioNotificationConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**slack_configuration:** `typing.Optional[SlackNotificationConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Openapi
## Operation
<details><summary><code>client.operation.<a href="src/fern/operation/client.py">check_operation</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, OperatorType

client = FernApi(
    token="YOUR_TOKEN",
)
client.operation.check_operation(
    operator_type=OperatorType.NORMALIZATION,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**operator_type:** `OperatorType` 
    
</dd>
</dl>

<dl>
<dd>

**dbt:** `typing.Optional[OperatorDbt]` 
    
</dd>
</dl>

<dl>
<dd>

**normalization:** `typing.Optional[OperatorNormalization]` 
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `typing.Optional[OperatorWebhook]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.operation.<a href="src/fern/operation/client.py">create_operation</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, OperatorConfiguration, OperatorType

client = FernApi(
    token="YOUR_TOKEN",
)
client.operation.create_operation(
    name="name",
    operator_configuration=OperatorConfiguration(
        operator_type=OperatorType.NORMALIZATION,
    ),
    workspace_id="workspaceId",
)

```
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

**operator_configuration:** `OperatorConfiguration` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.operation.<a href="src/fern/operation/client.py">delete_operation</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.operation.delete_operation(
    operation_id="operationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**operation_id:** `OperationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.operation.<a href="src/fern/operation/client.py">get_operation</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.operation.get_operation(
    operation_id="operationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**operation_id:** `OperationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.operation.<a href="src/fern/operation/client.py">list_operations_for_connection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List operations for connection.
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
    token="YOUR_TOKEN",
)
client.operation.list_operations_for_connection(
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `ConnectionId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.operation.<a href="src/fern/operation/client.py">update_operation</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, OperatorConfiguration, OperatorType

client = FernApi(
    token="YOUR_TOKEN",
)
client.operation.update_operation(
    name="name",
    operation_id="operationId",
    operator_configuration=OperatorConfiguration(
        operator_type=OperatorType.NORMALIZATION,
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**operation_id:** `OperationId` 
    
</dd>
</dl>

<dl>
<dd>

**operator_configuration:** `OperatorConfiguration` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Scheduler
<details><summary><code>client.scheduler.<a href="src/fern/scheduler/client.py">execute_destination_check_connection</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.scheduler.execute_destination_check_connection(
    connection_configuration={"user": "charles"},
    destination_definition_id="destinationDefinitionId",
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_configuration:** `DestinationConfiguration` 
    
</dd>
</dl>

<dl>
<dd>

**destination_definition_id:** `DestinationDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**destination_id:** `typing.Optional[DestinationId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scheduler.<a href="src/fern/scheduler/client.py">execute_source_check_connection</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.scheduler.execute_source_check_connection(
    connection_configuration={"user": "charles"},
    source_definition_id="sourceDefinitionId",
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_configuration:** `SourceConfiguration` 
    
</dd>
</dl>

<dl>
<dd>

**source_definition_id:** `SourceDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `typing.Optional[SourceId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scheduler.<a href="src/fern/scheduler/client.py">execute_source_discover_schema</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.scheduler.execute_source_discover_schema(
    connection_configuration={"user": "charles"},
    source_definition_id="sourceDefinitionId",
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_configuration:** `SourceConfiguration` 
    
</dd>
</dl>

<dl>
<dd>

**source_definition_id:** `SourceDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `typing.Optional[SourceId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## source_definition_specification
<details><summary><code>client.source_definition_specification.<a href="src/fern/source_definition_specification/client.py">get_source_definition_specification</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source_definition_specification.get_source_definition_specification(
    source_definition_id="sourceDefinitionId",
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_definition_id:** `SourceDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## source_definition
<details><summary><code>client.source_definition.<a href="src/fern/source_definition/client.py">create_custom_source_definition</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SourceDefinitionCreate

client = FernApi(
    token="YOUR_TOKEN",
)
client.source_definition.create_custom_source_definition(
    source_definition=SourceDefinitionCreate(
        docker_image_tag="dockerImageTag",
        docker_repository="dockerRepository",
        documentation_url="documentationUrl",
        name="name",
    ),
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_definition:** `SourceDefinitionCreate` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source_definition.<a href="src/fern/source_definition/client.py">delete_source_definition</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source_definition.delete_source_definition(
    source_definition_id="sourceDefinitionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_definition_id:** `SourceDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source_definition.<a href="src/fern/source_definition/client.py">get_source_definition</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source_definition.get_source_definition(
    source_definition_id="sourceDefinitionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_definition_id:** `SourceDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source_definition.<a href="src/fern/source_definition/client.py">get_source_definition_for_workspace</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source_definition.get_source_definition_for_workspace(
    source_definition_id="sourceDefinitionId",
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_definition_id:** `SourceDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source_definition.<a href="src/fern/source_definition/client.py">grant_source_definition_to_workspace</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source_definition.grant_source_definition_to_workspace(
    source_definition_id="sourceDefinitionId",
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_definition_id:** `SourceDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source_definition.<a href="src/fern/source_definition/client.py">list_source_definitions</a>()</code></summary>
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
    token="YOUR_TOKEN",
)
client.source_definition.list_source_definitions()

```
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

<details><summary><code>client.source_definition.<a href="src/fern/source_definition/client.py">list_source_definitions_for_workspace</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source_definition.list_source_definitions_for_workspace(
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source_definition.<a href="src/fern/source_definition/client.py">list_latest_source_definitions</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Guaranteed to retrieve the latest information on supported sources.
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
    token="YOUR_TOKEN",
)
client.source_definition.list_latest_source_definitions()

```
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

<details><summary><code>client.source_definition.<a href="src/fern/source_definition/client.py">list_private_source_definitions</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source_definition.list_private_source_definitions(
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source_definition.<a href="src/fern/source_definition/client.py">revoke_source_definition_from_workspace</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source_definition.revoke_source_definition_from_workspace(
    source_definition_id="sourceDefinitionId",
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_definition_id:** `SourceDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source_definition.<a href="src/fern/source_definition/client.py">update_source_definition</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source_definition.update_source_definition(
    docker_image_tag="dockerImageTag",
    source_definition_id="sourceDefinitionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**docker_image_tag:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source_definition_id:** `SourceDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**resource_requirements:** `typing.Optional[ActorDefinitionResourceRequirements]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## source_oauth
<details><summary><code>client.source_oauth.<a href="src/fern/source_oauth/client.py">complete_source_o_auth</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source_oauth.complete_source_o_auth(
    source_definition_id="sourceDefinitionId",
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_definition_id:** `SourceDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**o_auth_input_configuration:** `typing.Optional[OAuthInputConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**query_params:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The query parameters present in the redirect URL after a user granted consent e.g auth code
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — When completing OAuth flow to gain an access token, some API sometimes requires to verify that the app re-send the redirectUrl that was used when consent was given.
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `typing.Optional[SourceId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source_oauth.<a href="src/fern/source_oauth/client.py">get_source_o_auth_consent</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source_oauth.get_source_o_auth_consent(
    redirect_url="redirectUrl",
    source_definition_id="sourceDefinitionId",
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**redirect_url:** `str` — The url to redirect to after getting the user consent
    
</dd>
</dl>

<dl>
<dd>

**source_definition_id:** `SourceDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**o_auth_input_configuration:** `typing.Optional[OAuthInputConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `typing.Optional[SourceId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source_oauth.<a href="src/fern/source_oauth/client.py">set_instancewide_source_oauth_params</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source_oauth.set_instancewide_source_oauth_params(
    params={"key": "value"},
    source_definition_id="sourceDefinitionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**params:** `typing.Dict[str, typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**source_definition_id:** `SourceDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## source
<details><summary><code>client.source.<a href="src/fern/source/client.py">check_connection_to_source</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source.check_connection_to_source(
    source_id="sourceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_id:** `SourceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source.<a href="src/fern/source/client.py">check_connection_to_source_for_update</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source.check_connection_to_source_for_update(
    connection_configuration={"user": "charles"},
    name="name",
    source_id="sourceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_configuration:** `SourceConfiguration` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `SourceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source.<a href="src/fern/source/client.py">clone_source</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source.clone_source(
    source_clone_id="sourceCloneId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_clone_id:** `SourceId` 
    
</dd>
</dl>

<dl>
<dd>

**source_configuration:** `typing.Optional[SourceCloneConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source.<a href="src/fern/source/client.py">create_source</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source.create_source(
    connection_configuration={"user": "charles"},
    name="name",
    source_definition_id="sourceDefinitionId",
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_configuration:** `SourceConfiguration` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source_definition_id:** `SourceDefinitionId` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source.<a href="src/fern/source/client.py">delete_source</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source.delete_source(
    source_id="sourceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_id:** `SourceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source.<a href="src/fern/source/client.py">discover_schema_for_source</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source.discover_schema_for_source(
    source_id="sourceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_id:** `SourceId` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**disable_cache:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**notify_schema_change:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source.<a href="src/fern/source/client.py">get_source</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source.get_source(
    source_id="sourceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_id:** `SourceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source.<a href="src/fern/source/client.py">list_sources_for_workspace</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List sources for workspace. Does not return deleted sources.
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
    token="YOUR_TOKEN",
)
client.source.list_sources_for_workspace(
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source.<a href="src/fern/source/client.py">get_most_recent_source_actor_catalog</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source.get_most_recent_source_actor_catalog(
    source_id="sourceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_id:** `SourceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source.<a href="src/fern/source/client.py">search_sources</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source.search_sources()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_configuration:** `typing.Optional[SourceConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**source_definition_id:** `typing.Optional[SourceDefinitionId]` 
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `typing.Optional[SourceId]` 
    
</dd>
</dl>

<dl>
<dd>

**source_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**workspace_id:** `typing.Optional[WorkspaceId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source.<a href="src/fern/source/client.py">update_source</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.source.update_source(
    connection_configuration={"user": "charles"},
    name="name",
    source_id="sourceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_configuration:** `SourceConfiguration` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `SourceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source.<a href="src/fern/source/client.py">write_discover_catalog_result</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import AirbyteCatalog, AirbyteStreamAndConfiguration, FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.source.write_discover_catalog_result(
    catalog=AirbyteCatalog(
        streams=[AirbyteStreamAndConfiguration()],
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

**catalog:** `AirbyteCatalog` 
    
</dd>
</dl>

<dl>
<dd>

**configuration_hash:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**connector_version:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `typing.Optional[SourceId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## state
<details><summary><code>client.state.<a href="src/fern/state/client.py">create_or_update_state</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import ConnectionState, ConnectionStateType, FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.state.create_or_update_state(
    connection_id="connectionId",
    connection_state=ConnectionState(
        connection_id="connectionId",
        state_type=ConnectionStateType.GLOBAL,
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

**connection_id:** `ConnectionId` 
    
</dd>
</dl>

<dl>
<dd>

**connection_state:** `ConnectionState` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.state.<a href="src/fern/state/client.py">get_state</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.state.get_state(
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `ConnectionId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## web_backend
<details><summary><code>client.web_backend.<a href="src/fern/web_backend/client.py">check_updates</a>()</code></summary>
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
    token="YOUR_TOKEN",
)
client.web_backend.check_updates()

```
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

<details><summary><code>client.web_backend.<a href="src/fern/web_backend/client.py">create_connection</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import ConnectionStatus, FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.web_backend.create_connection(
    destination_id="destinationId",
    source_id="sourceId",
    status=ConnectionStatus.ACTIVE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**destination_id:** `DestinationId` 
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `SourceId` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `ConnectionStatus` 
    
</dd>
</dl>

<dl>
<dd>

**geography:** `typing.Optional[Geography]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Optional name of the connection
    
</dd>
</dl>

<dl>
<dd>

**namespace_definition:** `typing.Optional[NamespaceDefinitionType]` 
    
</dd>
</dl>

<dl>
<dd>

**namespace_format:** `typing.Optional[str]` — Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.
    
</dd>
</dl>

<dl>
<dd>

**non_breaking_changes_preference:** `typing.Optional[NonBreakingChangesPreference]` 
    
</dd>
</dl>

<dl>
<dd>

**operation_ids:** `typing.Optional[typing.Sequence[OperationId]]` 
    
</dd>
</dl>

<dl>
<dd>

**operations:** `typing.Optional[typing.Sequence[OperationCreate]]` 
    
</dd>
</dl>

<dl>
<dd>

**prefix:** `typing.Optional[str]` — Prefix that will be prepended to the name of each stream when it is written to the destination.
    
</dd>
</dl>

<dl>
<dd>

**resource_requirements:** `typing.Optional[ResourceRequirements]` 
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[ConnectionSchedule]` 
    
</dd>
</dl>

<dl>
<dd>

**schedule_data:** `typing.Optional[ConnectionScheduleData]` 
    
</dd>
</dl>

<dl>
<dd>

**schedule_type:** `typing.Optional[ConnectionScheduleType]` 
    
</dd>
</dl>

<dl>
<dd>

**source_catalog_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sync_catalog:** `typing.Optional[AirbyteCatalog]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.web_backend.<a href="src/fern/web_backend/client.py">get_connection</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.web_backend.get_connection(
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `ConnectionId` 
    
</dd>
</dl>

<dl>
<dd>

**with_refreshed_catalog:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.web_backend.<a href="src/fern/web_backend/client.py">list_connections_for_workspace</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.web_backend.list_connections_for_workspace(
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**destination_id:** `typing.Optional[typing.Sequence[DestinationId]]` 
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `typing.Optional[typing.Sequence[SourceId]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.web_backend.<a href="src/fern/web_backend/client.py">update_connection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply a patch-style update to a connection. Only fields present on the update request body will be updated.
Any operations that lack an ID will be created. Then, the newly created operationId will be applied to the
connection along with the rest of the operationIds in the request body.
Apply a patch-style update to a connection. Only fields present on the update request body will be updated.
Note that if a catalog is present in the request body, the connection's entire catalog will be replaced
with the catalog from the request. This means that to modify a single stream, the entire new catalog
containing the updated stream needs to be sent.
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
    token="YOUR_TOKEN",
)
client.web_backend.update_connection(
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `ConnectionId` 
    
</dd>
</dl>

<dl>
<dd>

**geography:** `typing.Optional[Geography]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name that will be set to the connection
    
</dd>
</dl>

<dl>
<dd>

**namespace_definition:** `typing.Optional[NamespaceDefinitionType]` 
    
</dd>
</dl>

<dl>
<dd>

**namespace_format:** `typing.Optional[str]` — Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.
    
</dd>
</dl>

<dl>
<dd>

**non_breaking_changes_preference:** `typing.Optional[NonBreakingChangesPreference]` 
    
</dd>
</dl>

<dl>
<dd>

**notify_schema_changes:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**operations:** `typing.Optional[typing.Sequence[WebBackendOperationCreateOrUpdate]]` 
    
</dd>
</dl>

<dl>
<dd>

**prefix:** `typing.Optional[str]` — Prefix that will be prepended to the name of each stream when it is written to the destination.
    
</dd>
</dl>

<dl>
<dd>

**resource_requirements:** `typing.Optional[ResourceRequirements]` 
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[ConnectionSchedule]` 
    
</dd>
</dl>

<dl>
<dd>

**schedule_data:** `typing.Optional[ConnectionScheduleData]` 
    
</dd>
</dl>

<dl>
<dd>

**schedule_type:** `typing.Optional[ConnectionScheduleType]` 
    
</dd>
</dl>

<dl>
<dd>

**skip_reset:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**source_catalog_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ConnectionStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**sync_catalog:** `typing.Optional[AirbyteCatalog]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.web_backend.<a href="src/fern/web_backend/client.py">list_geographies</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all available geographies in which a data sync can run.
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
    token="YOUR_TOKEN",
)
client.web_backend.list_geographies()

```
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

<details><summary><code>client.web_backend.<a href="src/fern/web_backend/client.py">get_state_type</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.web_backend.get_state_type(
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `ConnectionId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.web_backend.<a href="src/fern/web_backend/client.py">get_workspace_state</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.web_backend.get_workspace_state(
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## workspace
<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py">create_workspace</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.workspace.create_workspace(
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anonymous_data_collection:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**default_geography:** `typing.Optional[Geography]` 
    
</dd>
</dl>

<dl>
<dd>

**display_setup_wizard:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**news:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**notifications:** `typing.Optional[typing.Sequence[Notification]]` 
    
</dd>
</dl>

<dl>
<dd>

**security_updates:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_configs:** `typing.Optional[typing.Sequence[WebhookConfigWrite]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py">delete_workspace</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.workspace.delete_workspace(
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py">get_workspace</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.workspace.get_workspace(
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py">get_workspace_by_connection_id</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.workspace.get_workspace_by_connection_id(
    connection_id="connectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `ConnectionId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py">get_workspace_by_slug</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.workspace.get_workspace_by_slug(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py">list_workspaces</a>()</code></summary>
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
    token="YOUR_TOKEN",
)
client.workspace.list_workspaces()

```
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

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py">update_workspace_feedback</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.workspace.update_workspace_feedback(
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py">update_workspace</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.workspace.update_workspace(
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**anonymous_data_collection:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**default_geography:** `typing.Optional[Geography]` 
    
</dd>
</dl>

<dl>
<dd>

**display_setup_wizard:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**initial_setup_complete:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**news:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**notifications:** `typing.Optional[typing.Sequence[Notification]]` 
    
</dd>
</dl>

<dl>
<dd>

**security_updates:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_configs:** `typing.Optional[typing.Sequence[WebhookConfigWrite]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workspace.<a href="src/fern/workspace/client.py">update_workspace_name</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
)
client.workspace.update_workspace_name(
    name="name",
    workspace_id="workspaceId",
)

```
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

**workspace_id:** `WorkspaceId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

