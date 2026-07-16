# Reference
## Config
<details><summary><code>client.config.<a href="src/fern/config/client.py">get_config</a>() -> Config</code></summary>
<dl>
<dd>

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

client.config.get_config()

```
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

## Connection
<details><summary><code>client.connection.<a href="src/fern/connection/client.py">get_connections</a>(...) -> ConnectionCollection</code></summary>
<dl>
<dd>

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

client.connection.get_connections()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 

The name of the field to order the results by.
Prefix a field name with `-` to reverse the sort order.

*New in version 2.1.0*
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connection.<a href="src/fern/connection/client.py">post_connection</a>(...) -> Connection</code></summary>
<dl>
<dd>

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

client.connection.post_connection()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Connection` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connection.<a href="src/fern/connection/client.py">test_connection</a>(...) -> ConnectionTest</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Test a connection.

*New in version 2.2.0*
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

client.connection.test_connection()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Connection` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connection.<a href="src/fern/connection/client.py">get_connection</a>(...) -> Connection</code></summary>
<dl>
<dd>

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

client.connection.get_connection(
    connection_id="connection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `str` — The connection ID.
    
</dd>
</dl>

<dl>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connection.delete_connection(
    connection_id="connection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `str` — The connection ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connection.<a href="src/fern/connection/client.py">patch_connection</a>(...) -> Connection</code></summary>
<dl>
<dd>

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

client.connection.patch_connection(
    connection_id_="connection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `str` — The connection ID.
    
</dd>
</dl>

<dl>
<dd>

**request:** `Connection` 
    
</dd>
</dl>

<dl>
<dd>

**update_mask:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

The fields to update on the resource. If absent or empty, all modifiable fields are updated.
A comma-separated list of fully qualified names of fields.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DAG
<details><summary><code>client.dag.<a href="src/fern/dag/client.py">get_dag_source</a>(...) -> GetDagSourceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a source code using file token.
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

client.dag.get_dag_source(
    file_token="file_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_token:** `str` 

The key containing the encrypted path to the file. Encryption and decryption take place only on
the server. This prevents the client from reading an non-DAG file. This also ensures API
extensibility, because the format of encrypted data may change.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dag.<a href="src/fern/dag/client.py">get_dags</a>(...) -> DagCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List DAGs in the database.
`dag_id_pattern` can be set to match dags of a specific pattern
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

client.dag.get_dags()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 

The name of the field to order the results by.
Prefix a field name with `-` to reverse the sort order.

*New in version 2.1.0*
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

List of tags to filter results.

*New in version 2.2.0*
    
</dd>
</dl>

<dl>
<dd>

**only_active:** `typing.Optional[bool]` 

Only filter active DAGs.

*New in version 2.1.1*
    
</dd>
</dl>

<dl>
<dd>

**dag_id_pattern:** `typing.Optional[str]` — If set, only return DAGs with dag_ids matching this pattern.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dag.<a href="src/fern/dag/client.py">patch_dags</a>(...) -> DagCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update DAGs of a given dag_id_pattern using UpdateMask.
This endpoint allows specifying `~` as the dag_id_pattern to update all DAGs.
*New in version 2.3.0*
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

client.dag.patch_dags(
    dag_id_pattern="dag_id_pattern",
    is_paused=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id_pattern:** `str` — If set, only update DAGs with dag_ids matching this pattern.
    
</dd>
</dl>

<dl>
<dd>

**request:** `Dag` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

List of tags to filter results.

*New in version 2.2.0*
    
</dd>
</dl>

<dl>
<dd>

**update_mask:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

The fields to update on the resource. If absent or empty, all modifiable fields are updated.
A comma-separated list of fully qualified names of fields.
    
</dd>
</dl>

<dl>
<dd>

**only_active:** `typing.Optional[bool]` 

Only filter active DAGs.

*New in version 2.1.1*
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dag.<a href="src/fern/dag/client.py">get_dag</a>(...) -> Dag</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Presents only information available in database (DAGModel).
If you need detailed information, consider using GET /dags/{dag_id}/details.
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

client.dag.get_dag(
    dag_id="dag_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dag.<a href="src/fern/dag/client.py">delete_dag</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes all metadata related to the DAG, including finished DAG Runs and Tasks.
Logs are not deleted. This action cannot be undone.

*New in version 2.2.0*
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

client.dag.delete_dag(
    dag_id="dag_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dag.<a href="src/fern/dag/client.py">patch_dag</a>(...) -> Dag</code></summary>
<dl>
<dd>

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

client.dag.patch_dag(
    dag_id_="dag_id",
    is_paused=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**request:** `Dag` 
    
</dd>
</dl>

<dl>
<dd>

**update_mask:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

The fields to update on the resource. If absent or empty, all modifiable fields are updated.
A comma-separated list of fully qualified names of fields.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dag.<a href="src/fern/dag/client.py">post_clear_task_instances</a>(...) -> TaskInstanceReferenceCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Clears a set of task instances associated with the DAG for a specified date range.
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

client.dag.post_clear_task_instances(
    dag_id="dag_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**dag_run_id:** `typing.Optional[str]` — The DagRun ID for this task instance
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` 

If set, don't actually run this operation. The response will contain a list of task instances
planned to be cleaned, but not modified in any way.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — The maximum execution date to clear.
    
</dd>
</dl>

<dl>
<dd>

**include_downstream:** `typing.Optional[bool]` — If set to true, downstream tasks are also affected.
    
</dd>
</dl>

<dl>
<dd>

**include_future:** `typing.Optional[bool]` — If set to True, also tasks from future DAG Runs are affected.
    
</dd>
</dl>

<dl>
<dd>

**include_parentdag:** `typing.Optional[bool]` — Clear tasks in the parent dag of the subdag.
    
</dd>
</dl>

<dl>
<dd>

**include_past:** `typing.Optional[bool]` — If set to True, also tasks from past DAG Runs are affected.
    
</dd>
</dl>

<dl>
<dd>

**include_subdags:** `typing.Optional[bool]` — Clear tasks in subdags and clear external tasks indicated by ExternalTaskMarker.
    
</dd>
</dl>

<dl>
<dd>

**include_upstream:** `typing.Optional[bool]` — If set to true, upstream tasks are also affected.
    
</dd>
</dl>

<dl>
<dd>

**only_failed:** `typing.Optional[bool]` — Only clear failed tasks.
    
</dd>
</dl>

<dl>
<dd>

**only_running:** `typing.Optional[bool]` — Only clear running tasks.
    
</dd>
</dl>

<dl>
<dd>

**reset_dag_runs:** `typing.Optional[bool]` — Set state of DAG runs to RUNNING.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — The minimum execution date to clear.
    
</dd>
</dl>

<dl>
<dd>

**task_ids:** `typing.Optional[typing.List[str]]` 

A list of task ids to clear.

*New in version 2.1.0*
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dag.<a href="src/fern/dag/client.py">get_dag_details</a>(...) -> DagDetail</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The response contains many DAG attributes, so the response can be large. If possible, consider using GET /dags/{dag_id}.
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

client.dag.get_dag_details(
    dag_id="dag_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dag.<a href="src/fern/dag/client.py">get_tasks</a>(...) -> TaskCollection</code></summary>
<dl>
<dd>

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

client.dag.get_tasks(
    dag_id="dag_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 

The name of the field to order the results by.
Prefix a field name with `-` to reverse the sort order.

*New in version 2.1.0*
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dag.<a href="src/fern/dag/client.py">get_task</a>(...) -> Task</code></summary>
<dl>
<dd>

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

client.dag.get_task(
    dag_id="dag_id",
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**task_id:** `str` — The task ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dag.<a href="src/fern/dag/client.py">post_set_task_instances_state</a>(...) -> TaskInstanceReferenceCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the state for multiple task instances simultaneously.
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

client.dag.post_set_task_instances_state(
    dag_id="dag_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**dag_run_id:** `typing.Optional[str]` 

The task instance's DAG run ID. Either set this or execution_date but not both.

*New in version 2.3.0*
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` 

If set, don't actually run this operation. The response will contain a list of task instances
planned to be affected, but won't be modified in any way.
    
</dd>
</dl>

<dl>
<dd>

**execution_date:** `typing.Optional[str]` — The execution date. Either set this or dag_run_id but not both.
    
</dd>
</dl>

<dl>
<dd>

**include_downstream:** `typing.Optional[bool]` — If set to true, downstream tasks are also affected.
    
</dd>
</dl>

<dl>
<dd>

**include_future:** `typing.Optional[bool]` — If set to True, also tasks from future DAG Runs are affected.
    
</dd>
</dl>

<dl>
<dd>

**include_past:** `typing.Optional[bool]` — If set to True, also tasks from past DAG Runs are affected.
    
</dd>
</dl>

<dl>
<dd>

**include_upstream:** `typing.Optional[bool]` — If set to true, upstream tasks are also affected.
    
</dd>
</dl>

<dl>
<dd>

**new_state:** `typing.Optional[UpdateTaskInstancesStateNewState]` — Expected new state.
    
</dd>
</dl>

<dl>
<dd>

**task_id:** `typing.Optional[str]` — The task ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DagWarning
<details><summary><code>client.dag_warning.<a href="src/fern/dag_warning/client.py">get_dag_warnings</a>(...) -> DagWarningCollection</code></summary>
<dl>
<dd>

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

client.dag_warning.get_dag_warnings()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `typing.Optional[str]` — If set, only return DAG warnings with this dag_id.
    
</dd>
</dl>

<dl>
<dd>

**warning_type:** `typing.Optional[str]` — If set, only return DAG warnings with this type.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 

The name of the field to order the results by.
Prefix a field name with `-` to reverse the sort order.

*New in version 2.1.0*
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DAGRun
<details><summary><code>client.dag_run.<a href="src/fern/dag_run/client.py">get_dag_runs</a>(...) -> DagRunCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows specifying `~` as the dag_id to retrieve DAG runs for all DAGs.
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

client.dag_run.get_dag_runs(
    dag_id="dag_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**execution_date_gte:** `typing.Optional[datetime.datetime]` 

Returns objects greater or equal to the specified date.

This can be combined with execution_date_lte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**execution_date_lte:** `typing.Optional[datetime.datetime]` 

Returns objects less than or equal to the specified date.

This can be combined with execution_date_gte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**start_date_gte:** `typing.Optional[datetime.datetime]` 

Returns objects greater or equal the specified date.

This can be combined with start_date_lte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**start_date_lte:** `typing.Optional[datetime.datetime]` 

Returns objects less or equal the specified date.

This can be combined with start_date_gte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**end_date_gte:** `typing.Optional[datetime.datetime]` 

Returns objects greater or equal the specified date.

This can be combined with start_date_lte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**end_date_lte:** `typing.Optional[datetime.datetime]` 

Returns objects less than or equal to the specified date.

This can be combined with start_date_gte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The value can be repeated to retrieve multiple matching values (OR condition).
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 

The name of the field to order the results by.
Prefix a field name with `-` to reverse the sort order.

*New in version 2.1.0*
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dag_run.<a href="src/fern/dag_run/client.py">post_dag_run</a>(...) -> DagRun</code></summary>
<dl>
<dd>

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

client.dag_run.post_dag_run(
    dag_id_="dag_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**request:** `DagRun` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dag_run.<a href="src/fern/dag_run/client.py">get_dag_run</a>(...) -> DagRun</code></summary>
<dl>
<dd>

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

client.dag_run.get_dag_run(
    dag_id="dag_id",
    dag_run_id="dag_run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**dag_run_id:** `str` — The DAG run ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dag_run.<a href="src/fern/dag_run/client.py">delete_dag_run</a>(...)</code></summary>
<dl>
<dd>

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

client.dag_run.delete_dag_run(
    dag_id="dag_id",
    dag_run_id="dag_run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**dag_run_id:** `str` — The DAG run ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dag_run.<a href="src/fern/dag_run/client.py">update_dag_run_state</a>(...) -> DagRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify a DAG run.

*New in version 2.2.0*
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

client.dag_run.update_dag_run_state(
    dag_id="dag_id",
    dag_run_id="dag_run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**dag_run_id:** `str` — The DAG run ID.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[UpdateDagRunStateState]` — The state to set this DagRun
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dag_run.<a href="src/fern/dag_run/client.py">clear_dag_run</a>(...) -> DagRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Clear a DAG run.

*New in version 2.4.0*
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

client.dag_run.clear_dag_run(
    dag_id="dag_id",
    dag_run_id="dag_run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**dag_run_id:** `str` — The DAG run ID.
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` 

If set, don't actually run this operation. The response will contain a list of task instances
planned to be cleaned, but not modified in any way.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dag_run.<a href="src/fern/dag_run/client.py">set_dag_run_note</a>(...) -> DagRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the manual user note of a DagRun.

*New in version 2.5.0*
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

client.dag_run.set_dag_run_note(
    dag_id="dag_id",
    dag_run_id="dag_run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**dag_run_id:** `str` — The DAG run ID.
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` — Custom notes left by users for this Dag Run.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dag_run.<a href="src/fern/dag_run/client.py">get_upstream_dataset_events</a>(...) -> DatasetEventCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get datasets for a dag run.

*New in version 2.4.0*
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

client.dag_run.get_upstream_dataset_events(
    dag_id="dag_id",
    dag_run_id="dag_run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**dag_run_id:** `str` — The DAG run ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dag_run.<a href="src/fern/dag_run/client.py">get_dag_runs_batch</a>(...) -> DagRunCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limit.
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

client.dag_run.get_dag_runs_batch()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_ids:** `typing.Optional[typing.List[str]]` 

Return objects with specific DAG IDs.
The value can be repeated to retrieve multiple matching values (OR condition).
    
</dd>
</dl>

<dl>
<dd>

**end_date_gte:** `typing.Optional[datetime.datetime]` 

Returns objects greater or equal the specified date.

This can be combined with end_date_lte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**end_date_lte:** `typing.Optional[datetime.datetime]` 

Returns objects less than or equal to the specified date.

This can be combined with end_date_gte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**execution_date_gte:** `typing.Optional[datetime.datetime]` 

Returns objects greater or equal to the specified date.

This can be combined with execution_date_lte key to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**execution_date_lte:** `typing.Optional[datetime.datetime]` 

Returns objects less than or equal to the specified date.

This can be combined with execution_date_gte key to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 

The name of the field to order the results by. Prefix a field name
with `-` to reverse the sort order.

*New in version 2.1.0*
    
</dd>
</dl>

<dl>
<dd>

**page_limit:** `typing.Optional[int]` — The numbers of items to return.
    
</dd>
</dl>

<dl>
<dd>

**page_offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**start_date_gte:** `typing.Optional[datetime.datetime]` 

Returns objects greater or equal the specified date.

This can be combined with start_date_lte key to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**start_date_lte:** `typing.Optional[datetime.datetime]` 

Returns objects less or equal the specified date.

This can be combined with start_date_gte parameter to receive only the selected period
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[typing.List[str]]` 

Return objects with specific states.
The value can be repeated to retrieve multiple matching values (OR condition).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TaskInstance
<details><summary><code>client.task_instance.<a href="src/fern/task_instance/client.py">get_task_instances</a>(...) -> TaskInstanceCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows specifying `~` as the dag_id, dag_run_id to retrieve DAG runs for all DAGs and DAG runs.
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

client.task_instance.get_task_instances(
    dag_id="dag_id",
    dag_run_id="dag_run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**dag_run_id:** `str` — The DAG run ID.
    
</dd>
</dl>

<dl>
<dd>

**execution_date_gte:** `typing.Optional[datetime.datetime]` 

Returns objects greater or equal to the specified date.

This can be combined with execution_date_lte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**execution_date_lte:** `typing.Optional[datetime.datetime]` 

Returns objects less than or equal to the specified date.

This can be combined with execution_date_gte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**start_date_gte:** `typing.Optional[datetime.datetime]` 

Returns objects greater or equal the specified date.

This can be combined with start_date_lte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**start_date_lte:** `typing.Optional[datetime.datetime]` 

Returns objects less or equal the specified date.

This can be combined with start_date_gte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**end_date_gte:** `typing.Optional[datetime.datetime]` 

Returns objects greater or equal the specified date.

This can be combined with start_date_lte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**end_date_lte:** `typing.Optional[datetime.datetime]` 

Returns objects less than or equal to the specified date.

This can be combined with start_date_gte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**duration_gte:** `typing.Optional[float]` 

Returns objects greater than or equal to the specified values.

This can be combined with duration_lte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**duration_lte:** `typing.Optional[float]` 

Returns objects less than or equal to the specified values.

This can be combined with duration_gte parameter to receive only the selected range.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The value can be repeated to retrieve multiple matching values (OR condition).
    
</dd>
</dl>

<dl>
<dd>

**pool:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The value can be repeated to retrieve multiple matching values (OR condition).
    
</dd>
</dl>

<dl>
<dd>

**queue:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The value can be repeated to retrieve multiple matching values (OR condition).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.task_instance.<a href="src/fern/task_instance/client.py">get_task_instance</a>(...) -> TaskInstance</code></summary>
<dl>
<dd>

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

client.task_instance.get_task_instance(
    dag_id="dag_id",
    dag_run_id="dag_run_id",
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**dag_run_id:** `str` — The DAG run ID.
    
</dd>
</dl>

<dl>
<dd>

**task_id:** `str` — The task ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.task_instance.<a href="src/fern/task_instance/client.py">patch_task_instance</a>(...) -> TaskInstanceReference</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the state for single task instance.
*New in version 2.5.0*
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

client.task_instance.patch_task_instance(
    dag_id="dag_id",
    dag_run_id="dag_run_id",
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**dag_run_id:** `str` — The DAG run ID.
    
</dd>
</dl>

<dl>
<dd>

**task_id:** `str` — The task ID.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateTaskInstance` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.task_instance.<a href="src/fern/task_instance/client.py">get_extra_links</a>(...) -> ExtraLinkCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List extra links for task instance.
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

client.task_instance.get_extra_links(
    dag_id="dag_id",
    dag_run_id="dag_run_id",
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**dag_run_id:** `str` — The DAG run ID.
    
</dd>
</dl>

<dl>
<dd>

**task_id:** `str` — The task ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.task_instance.<a href="src/fern/task_instance/client.py">get_mapped_task_instances</a>(...) -> TaskInstanceCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of all mapped task instances.

*New in version 2.3.0*
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

client.task_instance.get_mapped_task_instances(
    dag_id="dag_id",
    dag_run_id="dag_run_id",
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**dag_run_id:** `str` — The DAG run ID.
    
</dd>
</dl>

<dl>
<dd>

**task_id:** `str` — The task ID.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**execution_date_gte:** `typing.Optional[datetime.datetime]` 

Returns objects greater or equal to the specified date.

This can be combined with execution_date_lte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**execution_date_lte:** `typing.Optional[datetime.datetime]` 

Returns objects less than or equal to the specified date.

This can be combined with execution_date_gte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**start_date_gte:** `typing.Optional[datetime.datetime]` 

Returns objects greater or equal the specified date.

This can be combined with start_date_lte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**start_date_lte:** `typing.Optional[datetime.datetime]` 

Returns objects less or equal the specified date.

This can be combined with start_date_gte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**end_date_gte:** `typing.Optional[datetime.datetime]` 

Returns objects greater or equal the specified date.

This can be combined with start_date_lte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**end_date_lte:** `typing.Optional[datetime.datetime]` 

Returns objects less than or equal to the specified date.

This can be combined with start_date_gte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**duration_gte:** `typing.Optional[float]` 

Returns objects greater than or equal to the specified values.

This can be combined with duration_lte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**duration_lte:** `typing.Optional[float]` 

Returns objects less than or equal to the specified values.

This can be combined with duration_gte parameter to receive only the selected range.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The value can be repeated to retrieve multiple matching values (OR condition).
    
</dd>
</dl>

<dl>
<dd>

**pool:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The value can be repeated to retrieve multiple matching values (OR condition).
    
</dd>
</dl>

<dl>
<dd>

**queue:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The value can be repeated to retrieve multiple matching values (OR condition).
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 

The name of the field to order the results by.
Prefix a field name with `-` to reverse the sort order.

*New in version 2.1.0*
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.task_instance.<a href="src/fern/task_instance/client.py">get_log</a>(...) -> GetLogResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get logs for a specific task instance and its try number.
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

client.task_instance.get_log(
    dag_id="dag_id",
    dag_run_id="dag_run_id",
    task_id="task_id",
    task_try_number=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**dag_run_id:** `str` — The DAG run ID.
    
</dd>
</dl>

<dl>
<dd>

**task_id:** `str` — The task ID.
    
</dd>
</dl>

<dl>
<dd>

**task_try_number:** `int` — The task try number.
    
</dd>
</dl>

<dl>
<dd>

**full_content:** `typing.Optional[bool]` 

A full content will be returned.
By default, only the first fragment will be returned.
    
</dd>
</dl>

<dl>
<dd>

**map_index:** `typing.Optional[int]` — Filter on map index for mapped task.
    
</dd>
</dl>

<dl>
<dd>

**token:** `typing.Optional[str]` 

A token that allows you to continue fetching logs.
If passed, it will specify the location from which the download should be continued.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.task_instance.<a href="src/fern/task_instance/client.py">set_task_instance_note</a>(...) -> TaskInstance</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the manual user note of a non-mapped Task Instance.

*New in version 2.5.0*
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

client.task_instance.set_task_instance_note(
    dag_id="dag_id",
    dag_run_id="dag_run_id",
    task_id="task_id",
    note="note",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**dag_run_id:** `str` — The DAG run ID.
    
</dd>
</dl>

<dl>
<dd>

**task_id:** `str` — The task ID.
    
</dd>
</dl>

<dl>
<dd>

**request:** `SetTaskInstanceNote` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.task_instance.<a href="src/fern/task_instance/client.py">get_mapped_task_instance</a>(...) -> TaskInstance</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a mapped task instance.

*New in version 2.3.0*
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

client.task_instance.get_mapped_task_instance(
    dag_id="dag_id",
    dag_run_id="dag_run_id",
    task_id="task_id",
    map_index=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**dag_run_id:** `str` — The DAG run ID.
    
</dd>
</dl>

<dl>
<dd>

**task_id:** `str` — The task ID.
    
</dd>
</dl>

<dl>
<dd>

**map_index:** `int` — The map index.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.task_instance.<a href="src/fern/task_instance/client.py">patch_mapped_task_instance</a>(...) -> TaskInstanceReference</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the state for single mapped task instance.
*New in version 2.5.0*
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

client.task_instance.patch_mapped_task_instance(
    dag_id="dag_id",
    dag_run_id="dag_run_id",
    task_id="task_id",
    map_index=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**dag_run_id:** `str` — The DAG run ID.
    
</dd>
</dl>

<dl>
<dd>

**task_id:** `str` — The task ID.
    
</dd>
</dl>

<dl>
<dd>

**map_index:** `int` — The map index.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateTaskInstance` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.task_instance.<a href="src/fern/task_instance/client.py">set_mapped_task_instance_note</a>(...) -> TaskInstance</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the manual user note of a mapped Task Instance.

*New in version 2.5.0*
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

client.task_instance.set_mapped_task_instance_note(
    dag_id="dag_id",
    dag_run_id="dag_run_id",
    task_id="task_id",
    map_index=1,
    note="note",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**dag_run_id:** `str` — The DAG run ID.
    
</dd>
</dl>

<dl>
<dd>

**task_id:** `str` — The task ID.
    
</dd>
</dl>

<dl>
<dd>

**map_index:** `int` — The map index.
    
</dd>
</dl>

<dl>
<dd>

**request:** `SetTaskInstanceNote` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.task_instance.<a href="src/fern/task_instance/client.py">get_task_instances_batch</a>(...) -> TaskInstanceCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List task instances from all DAGs and DAG runs.
This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limits.
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

client.task_instance.get_task_instances_batch()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_ids:** `typing.Optional[typing.List[str]]` 

Return objects with specific DAG IDs.
The value can be repeated to retrieve multiple matching values (OR condition).
    
</dd>
</dl>

<dl>
<dd>

**duration_gte:** `typing.Optional[float]` 

Returns objects greater than or equal to the specified values.

This can be combined with duration_lte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**duration_lte:** `typing.Optional[float]` 

Returns objects less than or equal to the specified values.

This can be combined with duration_gte parameter to receive only the selected range.
    
</dd>
</dl>

<dl>
<dd>

**end_date_gte:** `typing.Optional[datetime.datetime]` 

Returns objects greater or equal the specified date.

This can be combined with start_date_lte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**end_date_lte:** `typing.Optional[datetime.datetime]` 

Returns objects less than or equal to the specified date.

This can be combined with start_date_gte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**execution_date_gte:** `typing.Optional[datetime.datetime]` 

Returns objects greater or equal to the specified date.

This can be combined with execution_date_lte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**execution_date_lte:** `typing.Optional[datetime.datetime]` 

Returns objects less than or equal to the specified date.

This can be combined with execution_date_gte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**pool:** `typing.Optional[typing.List[str]]` — The value can be repeated to retrieve multiple matching values (OR condition).
    
</dd>
</dl>

<dl>
<dd>

**queue:** `typing.Optional[typing.List[str]]` — The value can be repeated to retrieve multiple matching values (OR condition).
    
</dd>
</dl>

<dl>
<dd>

**start_date_gte:** `typing.Optional[datetime.datetime]` 

Returns objects greater or equal the specified date.

This can be combined with start_date_lte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**start_date_lte:** `typing.Optional[datetime.datetime]` 

Returns objects less or equal the specified date.

This can be combined with start_date_gte parameter to receive only the selected period.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[typing.List[TaskState]]` — The value can be repeated to retrieve multiple matching values (OR condition).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## XCom
<details><summary><code>client.x_com.<a href="src/fern/x_com/client.py">get_xcom_entries</a>(...) -> XComCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCOM entries for for all DAGs, DAG runs and task instances. XCom values won't be returned as they can be large. Use this endpoint to get a list of XCom entries and then fetch individual entry to get value.
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

client.x_com.get_xcom_entries(
    dag_id="dag_id",
    dag_run_id="dag_run_id",
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**dag_run_id:** `str` — The DAG run ID.
    
</dd>
</dl>

<dl>
<dd>

**task_id:** `str` — The task ID.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.x_com.<a href="src/fern/x_com/client.py">get_xcom_entry</a>(...) -> XCom</code></summary>
<dl>
<dd>

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

client.x_com.get_xcom_entry(
    dag_id="dag_id",
    dag_run_id="dag_run_id",
    task_id="task_id",
    xcom_key="xcom_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dag_id:** `str` — The DAG ID.
    
</dd>
</dl>

<dl>
<dd>

**dag_run_id:** `str` — The DAG run ID.
    
</dd>
</dl>

<dl>
<dd>

**task_id:** `str` — The task ID.
    
</dd>
</dl>

<dl>
<dd>

**xcom_key:** `str` — The XCom key.
    
</dd>
</dl>

<dl>
<dd>

**deserialize:** `typing.Optional[bool]` 

Whether to deserialize an XCom value when using a custom XCom backend.

The XCom API endpoint calls `orm_deserialize_value` by default since an XCom may contain value
that is potentially expensive to deserialize in the web server. Setting this to true overrides
the consideration, and calls `deserialize_value` instead.

This parameter is not meaningful when using the default XCom backend.

*New in version 2.4.0*
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Dataset
<details><summary><code>client.dataset.<a href="src/fern/dataset/client.py">get_datasets</a>(...) -> DatasetCollection</code></summary>
<dl>
<dd>

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

client.dataset.get_datasets()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 

The name of the field to order the results by.
Prefix a field name with `-` to reverse the sort order.

*New in version 2.1.0*
    
</dd>
</dl>

<dl>
<dd>

**uri_pattern:** `typing.Optional[str]` — If set, only return datasets with uris matching this pattern.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dataset.<a href="src/fern/dataset/client.py">get_dataset_events</a>(...) -> DatasetEventCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get dataset events
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

client.dataset.get_dataset_events()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 

The name of the field to order the results by.
Prefix a field name with `-` to reverse the sort order.

*New in version 2.1.0*
    
</dd>
</dl>

<dl>
<dd>

**dataset_id:** `typing.Optional[int]` — The Dataset ID that updated the dataset.
    
</dd>
</dl>

<dl>
<dd>

**source_dag_id:** `typing.Optional[str]` — The DAG ID that updated the dataset.
    
</dd>
</dl>

<dl>
<dd>

**source_task_id:** `typing.Optional[str]` — The task ID that updated the dataset.
    
</dd>
</dl>

<dl>
<dd>

**source_run_id:** `typing.Optional[str]` — The DAG run ID that updated the dataset.
    
</dd>
</dl>

<dl>
<dd>

**source_map_index:** `typing.Optional[int]` — The map index that updated the dataset.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dataset.<a href="src/fern/dataset/client.py">get_dataset</a>(...) -> Dataset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a dataset by uri.
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

client.dataset.get_dataset(
    uri="uri",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**uri:** `str` — The encoded Dataset URI
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EventLog
<details><summary><code>client.event_log.<a href="src/fern/event_log/client.py">get_event_logs</a>(...) -> EventLogCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List log entries from event log.
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

client.event_log.get_event_logs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 

The name of the field to order the results by.
Prefix a field name with `-` to reverse the sort order.

*New in version 2.1.0*
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_log.<a href="src/fern/event_log/client.py">get_event_log</a>(...) -> EventLog</code></summary>
<dl>
<dd>

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

client.event_log.get_event_log(
    event_log_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event_log_id:** `int` — The event log ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Monitoring
<details><summary><code>client.monitoring.<a href="src/fern/monitoring/client.py">get_health</a>() -> HealthInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of Airflow's metadatabase and scheduler. It includes info about
metadatabase and last heartbeat of scheduler.
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

client.monitoring.get_health()

```
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

<details><summary><code>client.monitoring.<a href="src/fern/monitoring/client.py">get_version</a>() -> VersionInfo</code></summary>
<dl>
<dd>

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

client.monitoring.get_version()

```
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

## ImportError
<details><summary><code>client.import_error.<a href="src/fern/import_error/client.py">get_import_errors</a>(...) -> ImportErrorCollection</code></summary>
<dl>
<dd>

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

client.import_error.get_import_errors()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 

The name of the field to order the results by.
Prefix a field name with `-` to reverse the sort order.

*New in version 2.1.0*
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.import_error.<a href="src/fern/import_error/client.py">get_import_error</a>(...) -> ImportError</code></summary>
<dl>
<dd>

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

client.import_error.get_import_error(
    import_error_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**import_error_id:** `int` — The import error ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Permission
<details><summary><code>client.permission.<a href="src/fern/permission/client.py">get_permissions</a>(...) -> ActionCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of permissions.

*New in version 2.1.0*
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

client.permission.get_permissions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Plugin
<details><summary><code>client.plugin.<a href="src/fern/plugin/client.py">get_plugins</a>(...) -> PluginCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of loaded plugins.

*New in version 2.1.0*
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

client.plugin.get_plugins()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.pool.<a href="src/fern/pool/client.py">get_pools</a>(...) -> PoolCollection</code></summary>
<dl>
<dd>

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

client.pool.get_pools()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 

The name of the field to order the results by.
Prefix a field name with `-` to reverse the sort order.

*New in version 2.1.0*
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pool.<a href="src/fern/pool/client.py">post_pool</a>(...) -> Pool</code></summary>
<dl>
<dd>

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

client.pool.post_pool()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Pool` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pool.<a href="src/fern/pool/client.py">get_pool</a>(...) -> Pool</code></summary>
<dl>
<dd>

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

client.pool.get_pool(
    pool_name="pool_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pool_name:** `str` — The pool name.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pool.<a href="src/fern/pool/client.py">delete_pool</a>(...)</code></summary>
<dl>
<dd>

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

client.pool.delete_pool(
    pool_name="pool_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pool_name:** `str` — The pool name.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pool.<a href="src/fern/pool/client.py">patch_pool</a>(...) -> Pool</code></summary>
<dl>
<dd>

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

client.pool.patch_pool(
    pool_name="pool_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pool_name:** `str` — The pool name.
    
</dd>
</dl>

<dl>
<dd>

**request:** `Pool` 
    
</dd>
</dl>

<dl>
<dd>

**update_mask:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

The fields to update on the resource. If absent or empty, all modifiable fields are updated.
A comma-separated list of fully qualified names of fields.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Provider
<details><summary><code>client.provider.<a href="src/fern/provider/client.py">get_providers</a>() -> GetProvidersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of providers.

*New in version 2.1.0*
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

client.provider.get_providers()

```
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

## Role
<details><summary><code>client.role.<a href="src/fern/role/client.py">get_roles</a>(...) -> RoleCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of roles.

*New in version 2.1.0*
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

client.role.get_roles()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 

The name of the field to order the results by.
Prefix a field name with `-` to reverse the sort order.

*New in version 2.1.0*
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.role.<a href="src/fern/role/client.py">post_role</a>(...) -> Role</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new role.

*New in version 2.1.0*
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

client.role.post_role()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Role` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.role.<a href="src/fern/role/client.py">get_role</a>(...) -> Role</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a role.

*New in version 2.1.0*
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

client.role.get_role(
    role_name="role_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**role_name:** `str` — The role name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.role.<a href="src/fern/role/client.py">delete_role</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a role.

*New in version 2.1.0*
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

client.role.delete_role(
    role_name="role_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**role_name:** `str` — The role name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.role.<a href="src/fern/role/client.py">patch_role</a>(...) -> Role</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a role.

*New in version 2.1.0*
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

client.role.patch_role(
    role_name="role_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**role_name:** `str` — The role name
    
</dd>
</dl>

<dl>
<dd>

**request:** `Role` 
    
</dd>
</dl>

<dl>
<dd>

**update_mask:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

The fields to update on the resource. If absent or empty, all modifiable fields are updated.
A comma-separated list of fully qualified names of fields.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## User
<details><summary><code>client.user.<a href="src/fern/user/client.py">get_users</a>(...) -> UserCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of users.

*New in version 2.1.0*
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

client.user.get_users()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 

The name of the field to order the results by.
Prefix a field name with `-` to reverse the sort order.

*New in version 2.1.0*
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/fern/user/client.py">post_user</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new user with unique username and email.

*New in version 2.2.0*
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

client.user.post_user()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `User` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/fern/user/client.py">get_user</a>(...) -> UserCollectionItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a user with a specific username.

*New in version 2.1.0*
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

client.user.get_user(
    username="username",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `str` 

The username of the user.

*New in version 2.1.0*
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/fern/user/client.py">delete_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a user with a specific username.

*New in version 2.2.0*
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

client.user.delete_user(
    username="username",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `str` 

The username of the user.

*New in version 2.1.0*
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/fern/user/client.py">patch_user</a>(...) -> Role</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update fields for a user.

*New in version 2.2.0*
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

client.user.patch_user(
    username_="username",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `str` 

The username of the user.

*New in version 2.1.0*
    
</dd>
</dl>

<dl>
<dd>

**request:** `User` 
    
</dd>
</dl>

<dl>
<dd>

**update_mask:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

The fields to update on the resource. If absent or empty, all modifiable fields are updated.
A comma-separated list of fully qualified names of fields.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Variable
<details><summary><code>client.variable.<a href="src/fern/variable/client.py">get_variables</a>(...) -> VariableCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The collection does not contain data. To get data, you must get a single entity.
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

client.variable.get_variables()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 

The name of the field to order the results by.
Prefix a field name with `-` to reverse the sort order.

*New in version 2.1.0*
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.variable.<a href="src/fern/variable/client.py">post_variables</a>(...) -> Variable</code></summary>
<dl>
<dd>

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

client.variable.post_variables()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Variable` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.variable.<a href="src/fern/variable/client.py">get_variable</a>(...) -> Variable</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a variable by key.
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

client.variable.get_variable(
    variable_key="variable_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**variable_key:** `str` — The variable Key.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.variable.<a href="src/fern/variable/client.py">delete_variable</a>(...)</code></summary>
<dl>
<dd>

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

client.variable.delete_variable(
    variable_key="variable_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**variable_key:** `str` — The variable Key.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.variable.<a href="src/fern/variable/client.py">patch_variable</a>(...) -> Variable</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a variable by key.
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

client.variable.patch_variable(
    variable_key="variable_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**variable_key:** `str` — The variable Key.
    
</dd>
</dl>

<dl>
<dd>

**request:** `Variable` 
    
</dd>
</dl>

<dl>
<dd>

**update_mask:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

The fields to update on the resource. If absent or empty, all modifiable fields are updated.
A comma-separated list of fully qualified names of fields.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

