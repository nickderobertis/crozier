# Reference
<details><summary><code>client.<a href="src/fern/client.py">check_service_health_get</a>() -> str</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.check_service_health_get()

```
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

<details><summary><code>client.<a href="src/fern/client.py">get_service_metadata_meta_get</a>() -> BaseMeta</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.get_service_metadata_meta_get()

```
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

<details><summary><code>client.<a href="src/fern/client.py">list_tasks_task_get</a>() -> typing.List[TaskGet]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.list_tasks_task_get()

```
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

<details><summary><code>client.<a href="src/fern/client.py">get_task_status_task_task_id_get</a>(...) -> TaskStatus</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.get_task_status_task_task_id_get(
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

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">remove_task_task_task_id_delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.remove_task_task_task_id_delete(
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

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_task_result_task_task_id_result_get</a>(...) -> GetTaskResultTaskTaskIdResultGetResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.get_task_result_task_task_id_result_get(
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

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Computations
<details><summary><code>client.computations.<a href="src/fern/computations/client.py">create_or_update_or_start_computation</a>(...) -> ComputationGet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create and optionally start a new computation
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.computations.create_or_update_or_start_computation(
    user_id=1,
    project_id="project_id",
    product_name="product_name",
    product_api_base_url="product_api_base_url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `UserIdInt` 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**product_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**product_api_base_url:** `str` — Base url of the product
    
</dd>
</dl>

<dl>
<dd>

**start_pipeline:** `typing.Optional[bool]` — if True the computation pipeline will start right away
    
</dd>
</dl>

<dl>
<dd>

**subgraph:** `typing.Optional[typing.List[str]]` — An optional set of nodes that must be executed, if empty the whole pipeline is executed
    
</dd>
</dl>

<dl>
<dd>

**force_restart:** `typing.Optional[bool]` — if True will force re-running all dependent nodes
    
</dd>
</dl>

<dl>
<dd>

**simcore_user_agent:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**use_on_demand_clusters:** `typing.Optional[bool]` — if True, a cluster will be created as necessary (wallet_id cannot be None)
    
</dd>
</dl>

<dl>
<dd>

**wallet_info:** `typing.Optional[WalletInfoInput]` — contains information about the wallet used to bill the running service
    
</dd>
</dl>

<dl>
<dd>

**collection_run_id:** `typing.Optional[str]` — In case start_pipeline is True, this is the collection run id to which the comp run belongs.
    
</dd>
</dl>

<dl>
<dd>

**encryption:** `typing.Optional[JobEncryptionContextMetadata]` — Optional job encryption context to decrypt input files and encrypt output files
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.computations.<a href="src/fern/computations/client.py">get_computation</a>(...) -> ComputationGet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a computation pipeline state
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.computations.get_computation(
    project_id="project_id",
    user_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserIdInt` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.computations.<a href="src/fern/computations/client.py">delete_computation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a computation pipeline
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.computations.delete_computation(
    project_id="project_id",
    user_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserIdInt` 
    
</dd>
</dl>

<dl>
<dd>

**force:** `typing.Optional[bool]` — if True then the pipeline will be removed even if it is running
    
</dd>
</dl>

<dl>
<dd>

**wait_for:** `typing.Optional[str]` — timeout when waiting for pipeline to stop
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.computations.<a href="src/fern/computations/client.py">stop_computation</a>(...) -> ComputationGet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stops a computation pipeline
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.computations.stop_computation(
    project_id="project_id",
    user_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserIdInt` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.computations.<a href="src/fern/computations/client.py">get_all_tasks_log_files_v2computations_project_id_tasks_logfile_get</a>(...) -> typing.List[TaskLogFileGet]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns download links to log-files of each task in a computation.
Each log is only available when the corresponding task is done
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.computations.get_all_tasks_log_files_v2computations_project_id_tasks_logfile_get(
    project_id="project_id",
    user_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserIdInt` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.computations.<a href="src/fern/computations/client.py">get_task_log_file</a>(...) -> TaskLogFileGet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a link to download logs file of a give task.
The log is only available when the task is done
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.computations.get_task_log_file(
    project_id="project_id",
    node_uuid="node_uuid",
    user_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**node_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserIdInt` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.computations.<a href="src/fern/computations/client.py">get_batch_tasks_outputs_v2computations_project_id_tasks_outputs_batch_get_post</a>(...) -> TasksOutputs</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.computations.get_batch_tasks_outputs_v2computations_project_id_tasks_outputs_batch_get_post(
    project_id="project_id",
    nodes_ids=[
        "nodes_ids"
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

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**nodes_ids:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DynamicServices
<details><summary><code>client.dynamic_services.<a href="src/fern/dynamic_services/client.py">list_tracked_dynamic_services</a>(...) -> typing.List[RunningDynamicServiceDetails]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.dynamic_services.list_tracked_dynamic_services()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `typing.Optional[UserIdInt]` 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dynamic_services.<a href="src/fern/dynamic_services/client.py">create_dynamic_service</a>(...) -> RunningDynamicServiceDetails</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, WalletInfoInput, PricingInfo, HardwareInfo
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.dynamic_services.create_dynamic_service(
    dynamic_sidecar_request_dns="x-dynamic-sidecar-request-dns",
    dynamic_sidecar_request_scheme="x-dynamic-sidecar-request-scheme",
    simcore_user_agent="x-simcore-user-agent",
    service_key="service_key",
    service_version="service_version",
    user_id=234,
    project_id="dd1d04d9-d704-4f7e-8f0f-1ca60cc771fe",
    service_uuid="service_uuid",
    service_resources={
        "container": {"boot_modes": ["CPU"], "image": "simcore/services/dynamic/jupyter-math:2.0.5", "resources": {"CPU": {"limit": 0.1, "reservation": 0.1}, "RAM": {"limit": 2147483648, "reservation": 2147483648}}}
    },
    product_name="osparc",
    product_api_base_url="https://api.local/",
    can_save=True,
    wallet_info=WalletInfoInput(
        wallet_id=1,
        wallet_name="My Wallet",
        wallet_credit_amount="10",
    ),
    pricing_info=PricingInfo(
        pricing_plan_id=1,
        pricing_unit_id=1,
        pricing_unit_cost_id=1,
    ),
    hardware_info=HardwareInfo(
        aws_ec2instances=[
            "c6a.4xlarge"
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

**dynamic_sidecar_request_dns:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**dynamic_sidecar_request_scheme:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**simcore_user_agent:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**service_key:** `str` — distinctive name for the node based on the docker registry path
    
</dd>
</dl>

<dl>
<dd>

**service_version:** `str` — semantic version number of the node
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `UserIdInt` 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**service_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**service_resources:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**product_name:** `str` — Current product name
    
</dd>
</dl>

<dl>
<dd>

**product_api_base_url:** `str` — Current product API base URL
    
</dd>
</dl>

<dl>
<dd>

**can_save:** `bool` — the service data must be saved when closing
    
</dd>
</dl>

<dl>
<dd>

**service_basepath:** `typing.Optional[str]` — predefined path where the dynamic service should be served. If empty, the service shall use the root endpoint.
    
</dd>
</dl>

<dl>
<dd>

**wallet_info:** `typing.Optional[WalletInfoInput]` — contains information about the wallet used to bill the running service
    
</dd>
</dl>

<dl>
<dd>

**pricing_info:** `typing.Optional[PricingInfo]` — contains pricing information (ex. pricing plan and unit ids)
    
</dd>
</dl>

<dl>
<dd>

**hardware_info:** `typing.Optional[HardwareInfo]` — contains hardware information (ex. aws_ec2_instances)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dynamic_services.<a href="src/fern/dynamic_services/client.py">get_dynamic_sidecar_status</a>(...) -> RunningDynamicServiceDetails</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.dynamic_services.get_dynamic_sidecar_status(
    node_uuid="node_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dynamic_services.<a href="src/fern/dynamic_services/client.py">stop_dynamic_service</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.dynamic_services.stop_dynamic_service(
    node_uuid="node_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**can_save:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dynamic_services.<a href="src/fern/dynamic_services/client.py">service_retrieve_data_on_ports</a>(...) -> RetrieveDataOutEnveloped</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.dynamic_services.service_retrieve_data_on_ports(
    node_uuid="node_uuid",
    port_keys=[
        "port_keys"
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

**node_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**port_keys:** `typing.List[str]` — The port keys to retrieve data from
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dynamic_services.<a href="src/fern/dynamic_services/client.py">service_restart_containers</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.dynamic_services.service_restart_containers(
    node_uuid="node_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dynamic_services.<a href="src/fern/dynamic_services/client.py">update_projects_networks_v2dynamic_services_projects_project_id_networks_patch</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.dynamic_services.update_projects_networks_v2dynamic_services_projects_project_id_networks_patch(
    project_id="project_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dynamic_services.<a href="src/fern/dynamic_services/client.py">get_project_inactivity</a>(...) -> GetProjectInactivityResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.dynamic_services.get_project_inactivity(
    project_id="project_id",
    max_inactivity_seconds=1.1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**max_inactivity_seconds:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DynamicScheduler
<details><summary><code>client.dynamic_scheduler.<a href="src/fern/dynamic_scheduler/client.py">update_service_observation</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.dynamic_scheduler.update_service_observation(
    node_uuid="node_uuid",
    is_disabled=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**is_disabled:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dynamic_scheduler.<a href="src/fern/dynamic_scheduler/client.py">delete_service_containers</a>(...) -> str</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.dynamic_scheduler.delete_service_containers(
    node_uuid="node_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dynamic_scheduler.<a href="src/fern/dynamic_scheduler/client.py">get_service_state</a>(...) -> SchedulerData</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.dynamic_scheduler.get_service_state(
    node_uuid="node_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dynamic_scheduler.<a href="src/fern/dynamic_scheduler/client.py">save_service_state</a>(...) -> str</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.dynamic_scheduler.save_service_state(
    node_uuid="node_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dynamic_scheduler.<a href="src/fern/dynamic_scheduler/client.py">push_service_outputs</a>(...) -> str</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.dynamic_scheduler.push_service_outputs(
    node_uuid="node_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dynamic_scheduler.<a href="src/fern/dynamic_scheduler/client.py">delete_service_docker_resources</a>(...) -> str</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.dynamic_scheduler.delete_service_docker_resources(
    node_uuid="node_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dynamic_scheduler.<a href="src/fern/dynamic_scheduler/client.py">free_reserved_disk_space</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.dynamic_scheduler.free_reserved_disk_space(
    node_uuid="node_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

