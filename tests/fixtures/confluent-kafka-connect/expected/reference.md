# Reference
## Connectors (connect/v1)
<details><summary><code>client.connectors_connect_v1.<a href="src/fern/connectors_connect_v1/client.py">list_connectv1connectors</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Retrieve a list of "names" of the active connectors. You can then make a [read request](#operation/readConnectv1Connector) for a specific connector by name.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connectors_connect_v1.list_connectv1connectors(
    environment_id="environment_id",
    kafka_cluster_id="kafka_cluster_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — The unique identifier of the environment this resource belongs to.
    
</dd>
</dl>

<dl>
<dd>

**kafka_cluster_id:** `str` — The unique identifier for the Kafka cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connectors_connect_v1.<a href="src/fern/connectors_connect_v1/client.py">create_connectv1connector</a>(...) -> ConnectV1ConnectorWithOffsets</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Create a new connector. Returns the new connector information if successful.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connectors_connect_v1.create_connectv1connector(
    environment_id="environment_id",
    kafka_cluster_id="kafka_cluster_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — The unique identifier of the environment this resource belongs to.
    
</dd>
</dl>

<dl>
<dd>

**kafka_cluster_id:** `str` — The unique identifier for the Kafka cluster.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the connector to create.
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[InlineObjectConfig]` — Configuration parameters for the connector. All values should be strings.
    
</dd>
</dl>

<dl>
<dd>

**offsets:** `typing.Optional[typing.List[InlineObjectOffsetsItem]]` — Array of offsets which are categorised into partitions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connectors_connect_v1.<a href="src/fern/connectors_connect_v1/client.py">list_connectv1connectors_with_expansions</a>(...) -> ConnectV1ConnectorExpansionMap</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Retrieve an object with the queried expansions of all connectors. Without `expand` query parameter, this list connector’s endpoint will return a [list of only the connector names](#operation/listConnectv1Connectors).
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connectors_connect_v1.list_connectv1connectors_with_expansions(
    environment_id="environment_id",
    kafka_cluster_id="kafka_cluster_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — The unique identifier of the environment this resource belongs to.
    
</dd>
</dl>

<dl>
<dd>

**kafka_cluster_id:** `str` — The unique identifier for the Kafka cluster.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[ListConnectv1ConnectorsWithExpansionsRequestExpand]` 

- id : Returns metadata of each connector such as id and id type.
- info : Returns metadata of each connector such as the configuration, task
information, and type of connector.
- status : Returns additional state information of each connector including their status and tasks.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connectors_connect_v1.<a href="src/fern/connectors_connect_v1/client.py">get_connectv1connector_config</a>(...) -> GetConnectv1ConnectorConfigResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Get the configuration for the connector.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connectors_connect_v1.get_connectv1connector_config(
    environment_id="environment_id",
    kafka_cluster_id="kafka_cluster_id",
    connector_name="connector_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — The unique identifier of the environment this resource belongs to.
    
</dd>
</dl>

<dl>
<dd>

**kafka_cluster_id:** `str` — The unique identifier for the Kafka cluster.
    
</dd>
</dl>

<dl>
<dd>

**connector_name:** `str` — The unique name of the connector.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connectors_connect_v1.<a href="src/fern/connectors_connect_v1/client.py">create_or_update_connectv1connector_config</a>(...) -> ConnectV1Connector</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new connector using the given configuration, or update the configuration for an existing connector. Returns information about the connector after the change has been made.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connectors_connect_v1.create_or_update_connectv1connector_config(
    environment_id="environment_id",
    kafka_cluster_id="kafka_cluster_id",
    connector_name="connector_name",
    connector_class="GcsSink",
    name="MyGcsLogsBucketConnector",
    kafka_api_key="****************",
    kafka_api_secret="****************",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — The unique identifier of the environment this resource belongs to.
    
</dd>
</dl>

<dl>
<dd>

**kafka_cluster_id:** `str` — The unique identifier for the Kafka cluster.
    
</dd>
</dl>

<dl>
<dd>

**connector_name:** `str` — The unique name of the connector.
    
</dd>
</dl>

<dl>
<dd>

**connector_class:** `str` — \[Required for Managed Connector, Ignored for Custom Connector\] The connector class name. E.g. BigQuerySink, GcsSink, etc.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name or alias of the class (plugin) for this connector.
    
</dd>
</dl>

<dl>
<dd>

**kafka_api_key:** `str` — The kafka cluster api key.
    
</dd>
</dl>

<dl>
<dd>

**kafka_api_secret:** `str` — The kafka cluster api secret key.
    
</dd>
</dl>

<dl>
<dd>

**confluent_connector_type:** `typing.Optional[str]` — \[Required for Custom Connector\] The connector type.
    
</dd>
</dl>

<dl>
<dd>

**confluent_custom_plugin_id:** `typing.Optional[str]` — \[Required for Custom Connector\] The custom plugin id of custom connector, e.g., `ccp-lq5m06`
    
</dd>
</dl>

<dl>
<dd>

**confluent_custom_connection_endpoints:** `typing.Optional[str]` — \[Optional for Custom Connector\] Egress endpoint(s) for the connector to use when attaching to the sink or source data system.
    
</dd>
</dl>

<dl>
<dd>

**confluent_custom_schema_registry_auto:** `typing.Optional[str]` — \[Optional for Custom Connector\] Automatically add the required schema registry properties in a custom connector config if schema registry is enabled.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connectors_connect_v1.<a href="src/fern/connectors_connect_v1/client.py">read_connectv1connector</a>(...) -> ConnectV1Connector</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Get information about the connector.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connectors_connect_v1.read_connectv1connector(
    environment_id="environment_id",
    kafka_cluster_id="kafka_cluster_id",
    connector_name="connector_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — The unique identifier of the environment this resource belongs to.
    
</dd>
</dl>

<dl>
<dd>

**kafka_cluster_id:** `str` — The unique identifier for the Kafka cluster.
    
</dd>
</dl>

<dl>
<dd>

**connector_name:** `str` — The unique name of the connector.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connectors_connect_v1.<a href="src/fern/connectors_connect_v1/client.py">delete_connectv1connector</a>(...) -> InlineResponse200</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Delete a connector. Halts all tasks and deletes the connector configuration.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connectors_connect_v1.delete_connectv1connector(
    environment_id="environment_id",
    kafka_cluster_id="kafka_cluster_id",
    connector_name="connector_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — The unique identifier of the environment this resource belongs to.
    
</dd>
</dl>

<dl>
<dd>

**kafka_cluster_id:** `str` — The unique identifier for the Kafka cluster.
    
</dd>
</dl>

<dl>
<dd>

**connector_name:** `str` — The unique name of the connector.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Lifecycle (connect/v1)
<details><summary><code>client.lifecycle_connect_v1.<a href="src/fern/lifecycle_connect_v1/client.py">pause_connectv1connector</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Pause the connector and its tasks. Stops message processing until the connector is resumed. This call is asynchronous and the tasks will not transition to PAUSED state at the same time.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.lifecycle_connect_v1.pause_connectv1connector(
    environment_id="environment_id",
    kafka_cluster_id="kafka_cluster_id",
    connector_name="connector_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — The unique identifier of the environment this resource belongs to.
    
</dd>
</dl>

<dl>
<dd>

**kafka_cluster_id:** `str` — The unique identifier for the Kafka cluster.
    
</dd>
</dl>

<dl>
<dd>

**connector_name:** `str` — The unique name of the connector.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lifecycle_connect_v1.<a href="src/fern/lifecycle_connect_v1/client.py">resume_connectv1connector</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Resume a paused connector or do nothing if the connector is not paused. This call is asynchronous and the tasks will not transition to RUNNING state at the same time.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.lifecycle_connect_v1.resume_connectv1connector(
    environment_id="environment_id",
    kafka_cluster_id="kafka_cluster_id",
    connector_name="connector_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — The unique identifier of the environment this resource belongs to.
    
</dd>
</dl>

<dl>
<dd>

**kafka_cluster_id:** `str` — The unique identifier for the Kafka cluster.
    
</dd>
</dl>

<dl>
<dd>

**connector_name:** `str` — The unique name of the connector.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Status (connect/v1)
<details><summary><code>client.status_connect_v1.<a href="src/fern/status_connect_v1/client.py">read_connectv1connector_status</a>(...) -> InlineResponse2001</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get current status of the connector. This includes whether it is running, failed, or paused. Also includes which worker it is assigned to, error information if it has failed, and the state of all its tasks.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.status_connect_v1.read_connectv1connector_status(
    environment_id="environment_id",
    kafka_cluster_id="kafka_cluster_id",
    connector_name="connector_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — The unique identifier of the environment this resource belongs to.
    
</dd>
</dl>

<dl>
<dd>

**kafka_cluster_id:** `str` — The unique identifier for the Kafka cluster.
    
</dd>
</dl>

<dl>
<dd>

**connector_name:** `str` — The unique name of the connector.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.status_connect_v1.<a href="src/fern/status_connect_v1/client.py">list_connectv1connector_tasks</a>(...) -> ConnectV1Connectors</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Get a list of tasks currently running for the connector.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.status_connect_v1.list_connectv1connector_tasks(
    environment_id="environment_id",
    kafka_cluster_id="kafka_cluster_id",
    connector_name="connector_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — The unique identifier of the environment this resource belongs to.
    
</dd>
</dl>

<dl>
<dd>

**kafka_cluster_id:** `str` — The unique identifier for the Kafka cluster.
    
</dd>
</dl>

<dl>
<dd>

**connector_name:** `str` — The unique name of the connector.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Managed Connector Plugins (connect/v1)
<details><summary><code>client.managed_connector_plugins_connect_v1.<a href="src/fern/managed_connector_plugins_connect_v1/client.py">list_connectv1connector_plugins</a>(...) -> typing.List[InlineResponse2002]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Return a list of Managed Connector plugins installed in the Kafka Connect cluster.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.managed_connector_plugins_connect_v1.list_connectv1connector_plugins(
    environment_id="environment_id",
    kafka_cluster_id="kafka_cluster_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — The unique identifier of the environment this resource belongs to.
    
</dd>
</dl>

<dl>
<dd>

**kafka_cluster_id:** `str` — The unique identifier for the Kafka cluster.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.managed_connector_plugins_connect_v1.<a href="src/fern/managed_connector_plugins_connect_v1/client.py">validate_connectv1connector_plugin</a>(...) -> InlineResponse2003</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Validate the provided configuration values against the configuration definition. This API performs per config validation and returns suggested values and validation error messages.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.managed_connector_plugins_connect_v1.validate_connectv1connector_plugin(
    environment_id="environment_id",
    kafka_cluster_id="kafka_cluster_id",
    plugin_name="plugin_name",
    request={
        "cloud.environment": "prod",
        "cloud.provider": "aws",
        "connector.class": "GcsSink",
        "data.format": "BYTES",
        "flush.size": "500",
        "gcs.bucket.name": "APILogsBucket",
        "gcs.credentials.config": "****************",
        "kafka.api.key": "****************",
        "kafka.api.secret": "****************",
        "kafka.endpoint": "SASL_SSL://pkc-xxxxx.us-west-2.aws.confluent.cloud:9092",
        "kafka.region": "us-west-2",
        "name": "MyGcsLogsBucketConnector",
        "tasks.max": "2",
        "time.interval": "DAILY",
        "topics": "APILogsTopic"
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

**environment_id:** `str` — The unique identifier of the environment this resource belongs to.
    
</dd>
</dl>

<dl>
<dd>

**kafka_cluster_id:** `str` — The unique identifier for the Kafka cluster.
    
</dd>
</dl>

<dl>
<dd>

**plugin_name:** `str` — The unique name of the connector plugin.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, str]` — Configuration parameters for the connector. All values should be strings.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Offsets (connect/v1)
<details><summary><code>client.offsets_connect_v1.<a href="src/fern/offsets_connect_v1/client.py">get_connectv1connector_offsets</a>(...) -> ConnectV1ConnectorOffsets</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)

Get the current offsets for the connector. The offsets provide information on the point in the source system, 
from which the connector is pulling in data. The offsets of a connector are continuously observed periodically and are queryable via this API.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.offsets_connect_v1.get_connectv1connector_offsets(
    environment_id="environment_id",
    kafka_cluster_id="kafka_cluster_id",
    connector_name="connector_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — The unique identifier of the environment this resource belongs to.
    
</dd>
</dl>

<dl>
<dd>

**kafka_cluster_id:** `str` — The unique identifier for the Kafka cluster.
    
</dd>
</dl>

<dl>
<dd>

**connector_name:** `str` — The unique name of the connector.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.offsets_connect_v1.<a href="src/fern/offsets_connect_v1/client.py">alter_connectv1connector_offsets_request</a>(...) -> ConnectV1AlterOffsetRequestInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)

Request to alter the offsets of a connector. This supports the ability to PATCH/DELETE the offsets of a connector.
Note, you will see momentary downtime as this will internally stop the connector, while the offsets are being altered.
You can only make one alter offsets request at a time for a connector.
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
from fern import FernApi, ConnectV1AlterOffsetRequestType
from fern.environment import FernApiEnvironment
from fern.offsets_connect_v1 import ConnectV1AlterOffsetRequestOffsetsItem

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.offsets_connect_v1.alter_connectv1connector_offsets_request(
    environment_id="environment_id",
    kafka_cluster_id="kafka_cluster_id",
    connector_name="connector_name",
    type=ConnectV1AlterOffsetRequestType.PATCH,
    offsets=[
        ConnectV1AlterOffsetRequestOffsetsItem(
            partition={
                "kafka_partition": 0,
                "kafka_topic": "topic_A"
            },
            offset={
                "kafka_offset": 1000
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

**environment_id:** `str` — The unique identifier of the environment this resource belongs to.
    
</dd>
</dl>

<dl>
<dd>

**kafka_cluster_id:** `str` — The unique identifier for the Kafka cluster.
    
</dd>
</dl>

<dl>
<dd>

**connector_name:** `str` — The unique name of the connector.
    
</dd>
</dl>

<dl>
<dd>

**type:** `ConnectV1AlterOffsetRequestType` 
    
</dd>
</dl>

<dl>
<dd>

**offsets:** `typing.Optional[typing.List[ConnectV1AlterOffsetRequestOffsetsItem]]` — Array of offsets which are categorised into partitions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.offsets_connect_v1.<a href="src/fern/offsets_connect_v1/client.py">get_connectv1connector_offsets_request_status</a>(...) -> ConnectV1AlterOffsetStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)

Get the status of the previous alter offset request.
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.offsets_connect_v1.get_connectv1connector_offsets_request_status(
    environment_id="environment_id",
    kafka_cluster_id="kafka_cluster_id",
    connector_name="connector_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_id:** `str` — The unique identifier of the environment this resource belongs to.
    
</dd>
</dl>

<dl>
<dd>

**kafka_cluster_id:** `str` — The unique identifier for the Kafka cluster.
    
</dd>
</dl>

<dl>
<dd>

**connector_name:** `str` — The unique name of the connector.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

