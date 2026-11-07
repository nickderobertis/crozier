# Reference
<details><summary><code>client.<a href="src/fern/client.py">get_v1</a>() -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an empty response.
</dd>
</dl>
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

client.get_v1()

```
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

## TaskDirectives
<details><summary><code>client.task_directives.<a href="src/fern/task_directives/client.py">post_v1query_task_directives</a>(...) -> PostV1QueryTaskDirectivesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queries and returns a list of task directive objects based on the provided criteria. See `FindObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#findobject>`_, `TaskDirectiveObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskdirectiveobject>`_.
</dd>
</dl>
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

client.task_directives.post_v1query_task_directives(
    query={
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

**request:** `FindObject` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.task_directives.<a href="src/fern/task_directives/client.py">get_v1task_directives_task_id</a>(...) -> TaskDirectiveObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the task directive that matches the specified task ID. See `TaskDirectiveObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskdirectiveobject>`_.
</dd>
</dl>
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

client.task_directives.get_v1task_directives_task_id(
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

**task_id:** `str` — The ID of the task directive
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.task_directives.<a href="src/fern/task_directives/client.py">post_v1task_directives_task_id_actions_add_workers</a>(...) -> TaskforceObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new taskforce (and associated workers) for an existing task directive. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.
</dd>
</dl>
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

client.task_directives.post_v1task_directives_task_id_actions_add_workers(
    task_id="task_id",
    cluster_location="cluster_location",
    n_workers=None,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` — The ID of the task directive to which the taskforce (and workers) will be added.
    
</dd>
</dl>

<dl>
<dd>

**cluster_location:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**n_workers:** `typing.Optional[int]` — The number of workers in this taskforce's HTCondor cluster (immutable).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Taskforces
<details><summary><code>client.taskforces.<a href="src/fern/taskforces/client.py">post_v1query_taskforces</a>(...) -> PostV1QueryTaskforcesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queries and returns a list of taskforce objects based on the provided criteria. See `FindObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#findobject>`_, `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.
</dd>
</dl>
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

client.taskforces.post_v1query_taskforces(
    query={
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

**request:** `FindObject` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.taskforces.<a href="src/fern/taskforces/client.py">get_v1taskforces_taskforce_uuid</a>(...) -> TaskforceObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the taskforce object that matches the specified taskforce UUID. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.
</dd>
</dl>
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

client.taskforces.get_v1taskforces_taskforce_uuid(
    taskforce_uuid="taskforce_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**taskforce_uuid:** `str` — UUID of the taskforce.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Workflows
<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">post_v1query_workflows</a>(...) -> PostV1QueryWorkflowsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queries and returns a list of workflow objects based on the provided criteria. See `FindObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#findobject>`_, `WorkflowObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#workflowobject>`_.
</dd>
</dl>
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

client.workflows.post_v1query_workflows(
    query={
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

**request:** `FindObject` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">post_v1workflows</a>(...) -> PostV1WorkflowsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new workflow along with its associated task directives and taskforces. See `WorkflowObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#workflowobject>`_, `TaskDirectiveObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskdirectiveobject>`_, `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.workflows import PostV1WorkflowsRequestTasksItem, PostV1WorkflowsRequestTasksItemWorkerConfig

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.workflows.post_v1workflows(
    tasks=[
        PostV1WorkflowsRequestTasksItem(
            cluster_locations=[
                "cluster_locations"
            ],
            task_image="task_image",
            task_args="task_args",
            input_queue_aliases=[
                "input_queue_aliases"
            ],
            output_queue_aliases=[
                "output_queue_aliases"
            ],
            worker_config=PostV1WorkflowsRequestTasksItemWorkerConfig(
                do_transfer_worker_stdouterr=True,
                max_worker_runtime=1,
                n_cores=1,
                priority=1,
                worker_disk="worker_disk",
                worker_memory="worker_memory",
                condor_requirements="condor_requirements",
            ),
        )
    ],
    public_queue_aliases=[
        "public_queue_aliases"
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

**tasks:** `typing.List[PostV1WorkflowsRequestTasksItem]` 
    
</dd>
</dl>

<dl>
<dd>

**public_queue_aliases:** `typing.List[str]` — User-defined aliases for queues listed in 'input_queue_aliases' and 'output_queue_aliases' that will be used externally. The actual IDs will be generated after submission.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[int]` — The workflow's priority level relative to other workflows.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">get_v1workflows_workflow_id</a>(...) -> WorkflowObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the workflow object that matches the specified workflow ID. See `WorkflowObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#workflowobject>`_.
</dd>
</dl>
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

client.workflows.get_v1workflows_workflow_id(
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

**workflow_id:** `str` — The ID of the workflow object
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">post_v1workflows_workflow_id_actions_abort</a>(...) -> DeactivatedWorkflowResponseObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Aborts the specified workflow, marks it as deactivated, and sends stop commands to the associated taskforces. See `DeactivatedWorkflowResponseObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#deactivatedworkflowresponseobject>`_.
</dd>
</dl>
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

client.workflows.post_v1workflows_workflow_id_actions_abort(
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

**workflow_id:** `str` — The ID of the workflow object
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workflows.<a href="src/fern/workflows/client.py">post_v1workflows_workflow_id_actions_finished</a>(...) -> DeactivatedWorkflowResponseObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Marks the specified workflow as finished, marks it as deactivated, and sends stop commands to the associated taskforces. See `DeactivatedWorkflowResponseObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#deactivatedworkflowresponseobject>`_.
</dd>
</dl>
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

client.workflows.post_v1workflows_workflow_id_actions_finished(
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

**workflow_id:** `str` — The ID of the workflow object
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.openapi.<a href="src/fern/openapi/client.py">get_v1schema_openapi</a>() -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the OpenAPI schema.
</dd>
</dl>
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

client.openapi.get_v1schema_openapi()

```
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

## TmsInternal
<details><summary><code>client.tms_internal.<a href="src/fern/tms_internal/client.py">post_v1tms_condor_complete_taskforces_taskforce_uuid</a>(...) -> PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

For internal use only (TMS): Updates the specified taskforce with the completion timestamp of the HTCondor cluster. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.
</dd>
</dl>
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

client.tms_internal.post_v1tms_condor_complete_taskforces_taskforce_uuid(
    taskforce_uuid="taskforce_uuid",
    condor_complete_ts=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**taskforce_uuid:** `str` — UUID of the taskforce.
    
</dd>
</dl>

<dl>
<dd>

**condor_complete_ts:** `int` — The time when the taskforce's HTCondor cluster ended.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tms_internal.<a href="src/fern/tms_internal/client.py">post_v1tms_condor_rm_taskforces_taskforce_uuid</a>(...) -> PostV1TmsCondorRmTaskforcesTaskforceUuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

For internal use only (TMS): Confirms that a taskforce has been removed on HTCondor. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.
</dd>
</dl>
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

client.tms_internal.post_v1tms_condor_rm_taskforces_taskforce_uuid(
    taskforce_uuid="taskforce_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**taskforce_uuid:** `str` — UUID of the taskforce.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tms_internal.<a href="src/fern/tms_internal/client.py">post_v1tms_condor_rm_taskforces_taskforce_uuid_failed</a>(...) -> PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

For internal use only (TMS): Communicates that a taskforce failed to be removed on HTCondor. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.
</dd>
</dl>
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

client.tms_internal.post_v1tms_condor_rm_taskforces_taskforce_uuid_failed(
    taskforce_uuid="taskforce_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**taskforce_uuid:** `str` — UUID of the taskforce.
    
</dd>
</dl>

<dl>
<dd>

**error:** `typing.Optional[str]` — A description of why the taskforce could not be removed from HTCondor.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tms_internal.<a href="src/fern/tms_internal/client.py">post_v1tms_condor_submit_taskforces_taskforce_uuid</a>(...) -> PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

For internal use only (TMS): Confirms that a taskforce has been submitted to HTCondor for execution. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.
</dd>
</dl>
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

client.tms_internal.post_v1tms_condor_submit_taskforces_taskforce_uuid(
    taskforce_uuid_="taskforce_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**taskforce_uuid:** `str` — UUID of the taskforce.
    
</dd>
</dl>

<dl>
<dd>

**request:** `TaskforceObject` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tms_internal.<a href="src/fern/tms_internal/client.py">post_v1tms_condor_submit_taskforces_taskforce_uuid_failed</a>(...) -> PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

For internal use only (TMS): Communicates that a taskforce failed to be submitted to HTCondor for execution. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.
</dd>
</dl>
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

client.tms_internal.post_v1tms_condor_submit_taskforces_taskforce_uuid_failed(
    taskforce_uuid="taskforce_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**taskforce_uuid:** `str` — UUID of the taskforce.
    
</dd>
</dl>

<dl>
<dd>

**error:** `typing.Optional[str]` — A description of why the taskforce could not be submitted to HTCondor.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tms_internal.<a href="src/fern/tms_internal/client.py">get_v1tms_pending_starter_taskforces</a>(...) -> GetV1TmsPendingStarterTaskforcesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

For internal use only (TMS): Retrieves the next taskforce ready to start at the specified HTCondor location. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_, `TaskDirectiveObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskdirectiveobject>`_, `MQProfileObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/mqs-objects.html#mqprofileobject>`_.
</dd>
</dl>
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

client.tms_internal.get_v1tms_pending_starter_taskforces(
    schedd="schedd",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schedd:** `str` — Name of the HTCondor schedd.
    
</dd>
</dl>

<dl>
<dd>

**collector:** `typing.Optional[str]` — Deprecated. Name of the HTCondor collector; no longer used.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tms_internal.<a href="src/fern/tms_internal/client.py">get_v1tms_pending_stopper_taskforces</a>(...) -> GetV1TmsPendingStopperTaskforcesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

For internal use only (TMS): Retrieves the next taskforce ready to stop at the specified HTCondor location. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.
</dd>
</dl>
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

client.tms_internal.get_v1tms_pending_stopper_taskforces(
    schedd="schedd",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schedd:** `str` — Name of the HTCondor schedd.
    
</dd>
</dl>

<dl>
<dd>

**collector:** `typing.Optional[str]` — Deprecated. Name of the HTCondor collector; no longer used.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tms_internal.<a href="src/fern/tms_internal/client.py">post_v1tms_statuses_taskforces</a>(...) -> PostV1TmsStatusesTaskforcesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

For internal use only (TMS): Updates and returns the statuses and errors for the specified taskforces. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.
</dd>
</dl>
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

client.tms_internal.post_v1tms_statuses_taskforces()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**top_task_errors_by_taskforce:** `typing.Optional[typing.Dict[str, typing.Dict[str, int]]]` — The top errors (paired with a count) for each indicated taskforce
    
</dd>
</dl>

<dl>
<dd>

**compound_statuses_by_taskforce:** `typing.Optional[typing.Dict[str, typing.Dict[str, typing.Dict[str, int]]]]` — The compound statuses (status -> state -> count) for the indicated taskforces
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

