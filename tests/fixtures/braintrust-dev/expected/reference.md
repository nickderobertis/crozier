# Reference
## Projects
<details><summary><code>client.projects.<a href="src/fern/projects/client.py">get_project</a>(...) -> GetProjectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all projects. The projects are sorted by creation date, with the most recently-created projects coming first
</dd>
</dl>
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

client.projects.get_project()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**project_name:** `typing.Optional[ProjectName]` — Name of the project to search for
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">post_project</a>(...) -> Project</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new project. If there is an existing project with the same name as the one specified in the request, will return the existing project unmodified
</dd>
</dl>
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

client.projects.post_project(
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

**name:** `str` — Name of the project
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Textual description of the project
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[str]` — For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the project belongs in.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">get_project_id</a>(...) -> Project</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a project object by its id
</dd>
</dl>
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

client.projects.get_project_id(
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

**project_id:** `ProjectIdParam` — Project id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">delete_project_id</a>(...) -> Project</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a project object by its id
</dd>
</dl>
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

client.projects.delete_project_id(
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

**project_id:** `ProjectIdParam` — Project id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">patch_project_id</a>(...) -> Project</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update a project object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.
</dd>
</dl>
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

client.projects.patch_project_id(
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

**project_id:** `ProjectIdParam` — Project id
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the project
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[PatchProjectSettings]` — Project settings. Patch operations replace all settings, so make sure you include all settings you want to keep.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.logs.<a href="src/fern/logs/client.py">post_project_logs_id_insert</a>(...) -> InsertEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Insert a set of events into the project logs
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, InsertProjectLogsEvent
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.logs.post_project_logs_id_insert(
    project_id="project_id",
    events=[
        InsertProjectLogsEvent()
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

**project_id:** `ProjectIdParam` — Project id
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.List[InsertProjectLogsEvent]` — A list of project logs events to insert
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.logs.<a href="src/fern/logs/client.py">get_project_logs_id_fetch</a>(...) -> FetchProjectLogsEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the events in a project logs. Equivalent to the POST form of the same path, but with the parameters in the URL query rather than in the request body. For more complex queries, use the `POST /btql` endpoint.
</dd>
</dl>
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

client.logs.get_project_logs_id_fetch(
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

**project_id:** `ProjectIdParam` — Project id
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[FetchLimitParam]` 

limit the number of traces fetched

Fetch queries may be paginated if the total result size is expected to be large (e.g. project_logs which accumulate over a long time). Note that fetch queries only support pagination in descending time order (from latest to earliest `_xact_id`. Furthermore, later pages may return rows which showed up in earlier pages, except with an earlier `_xact_id`. This happens because pagination occurs over the whole version history of the event log. You will most likely want to exclude any such duplicate, outdated rows (by `id`) from your combined result set.

The `limit` parameter controls the number of full traces to return. So you may end up with more individual rows than the specified limit if you are fetching events containing traces.
    
</dd>
</dl>

<dl>
<dd>

**max_xact_id:** `typing.Optional[MaxXactId]` 

DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in favor of the explicit 'cursor' returned by object fetch requests. Please prefer the 'cursor' argument going forwards.

Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

Since a paginated fetch query returns results in order from latest to earliest, the cursor for the next page can be found as the row with the minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit` for an overview of paginating fetch queries.
    
</dd>
</dl>

<dl>
<dd>

**max_root_span_id:** `typing.Optional[MaxRootSpanId]` 

DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in favor of the explicit 'cursor' returned by object fetch requests. Please prefer the 'cursor' argument going forwards.

Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

Since a paginated fetch query returns results in order from latest to earliest, the cursor for the next page can be found as the row with the minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit` for an overview of paginating fetch queries.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[Version]` 

Retrieve a snapshot of events from a past time

The version id is essentially a filter on the latest event transaction id. You can use the `max_xact_id` returned by a past fetch as the version to reproduce that exact fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.logs.<a href="src/fern/logs/client.py">post_project_logs_id_fetch</a>(...) -> FetchProjectLogsEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the events in a project logs. Equivalent to the GET form of the same path, but with the parameters in the request body rather than in the URL query. For more complex queries, use the `POST /btql` endpoint.
</dd>
</dl>
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

client.logs.post_project_logs_id_fetch(
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

**project_id:** `ProjectIdParam` — Project id
    
</dd>
</dl>

<dl>
<dd>

**request:** `FetchEventsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.logs.<a href="src/fern/logs/client.py">post_project_logs_id_feedback</a>(...) -> FeedbackResponseSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Log feedback for a set of project logs events
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, FeedbackProjectLogsItem
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.logs.post_project_logs_id_feedback(
    project_id="project_id",
    feedback=[
        FeedbackProjectLogsItem(
            id="id",
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

**project_id:** `ProjectIdParam` — Project id
    
</dd>
</dl>

<dl>
<dd>

**feedback:** `typing.List[FeedbackProjectLogsItem]` — A list of project logs feedback items
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Experiments
<details><summary><code>client.experiments.<a href="src/fern/experiments/client.py">get_experiment</a>(...) -> GetExperimentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all experiments. The experiments are sorted by creation date, with the most recently-created experiments coming first
</dd>
</dl>
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

client.experiments.get_experiment()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitWithDefaultParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**experiment_name:** `typing.Optional[ExperimentName]` — Name of the experiment to search for
    
</dd>
</dl>

<dl>
<dd>

**project_name:** `typing.Optional[ProjectName]` — Name of the project to search for
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[ProjectIdQuery]` — Project id
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.experiments.<a href="src/fern/experiments/client.py">post_experiment</a>(...) -> Experiment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new experiment. If there is an existing experiment in the project with the same name as the one specified in the request, will return the existing experiment unmodified
</dd>
</dl>
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

client.experiments.post_experiment(
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

**project_id:** `str` — Unique identifier for the project that the experiment belongs under
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the experiment. Within a project, experiment names are unique
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Textual description of the experiment
    
</dd>
</dl>

<dl>
<dd>

**repo_info:** `typing.Optional[RepoInfo]` 
    
</dd>
</dl>

<dl>
<dd>

**base_exp_id:** `typing.Optional[str]` — Id of default base experiment to compare against when viewing this experiment
    
</dd>
</dl>

<dl>
<dd>

**dataset_id:** `typing.Optional[str]` — Identifier of the linked dataset, or null if the experiment is not linked to a dataset
    
</dd>
</dl>

<dl>
<dd>

**dataset_version:** `typing.Optional[str]` — Version number of the linked dataset the experiment was run against. This can be used to reproduce the experiment after the dataset has been modified.
    
</dd>
</dl>

<dl>
<dd>

**parameters_id:** `typing.Optional[str]` — Identifier of the linked saved parameters object, or null if the experiment is not linked to saved parameters
    
</dd>
</dl>

<dl>
<dd>

**parameters_version:** `typing.Optional[str]` — Version number of the linked saved parameters object the experiment was run against.
    
</dd>
</dl>

<dl>
<dd>

**public:** `typing.Optional[bool]` — Whether or not the experiment is public. Public experiments can be viewed by anybody inside or outside the organization
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — User-controlled metadata about the experiment
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — A list of tags for the experiment
    
</dd>
</dl>

<dl>
<dd>

**ensure_new:** `typing.Optional[bool]` — Normally, creating an experiment with the same name as an existing experiment will return the existing one un-modified. But if `ensure_new` is true, registration will generate a new experiment with a unique name in case of a conflict.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.experiments.<a href="src/fern/experiments/client.py">get_experiment_id</a>(...) -> Experiment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an experiment object by its id
</dd>
</dl>
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

client.experiments.get_experiment_id(
    experiment_id="experiment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**experiment_id:** `ExperimentIdParam` — Experiment id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.experiments.<a href="src/fern/experiments/client.py">delete_experiment_id</a>(...) -> Experiment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an experiment object by its id
</dd>
</dl>
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

client.experiments.delete_experiment_id(
    experiment_id="experiment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**experiment_id:** `ExperimentIdParam` — Experiment id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.experiments.<a href="src/fern/experiments/client.py">patch_experiment_id</a>(...) -> Experiment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update an experiment object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.
</dd>
</dl>
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

client.experiments.patch_experiment_id(
    experiment_id="experiment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**experiment_id:** `ExperimentIdParam` — Experiment id
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the experiment. Within a project, experiment names are unique
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Textual description of the experiment
    
</dd>
</dl>

<dl>
<dd>

**repo_info:** `typing.Optional[RepoInfo]` 
    
</dd>
</dl>

<dl>
<dd>

**base_exp_id:** `typing.Optional[str]` — Id of default base experiment to compare against when viewing this experiment
    
</dd>
</dl>

<dl>
<dd>

**dataset_id:** `typing.Optional[str]` — Identifier of the linked dataset, or null if the experiment is not linked to a dataset
    
</dd>
</dl>

<dl>
<dd>

**dataset_version:** `typing.Optional[str]` — Version number of the linked dataset the experiment was run against. This can be used to reproduce the experiment after the dataset has been modified.
    
</dd>
</dl>

<dl>
<dd>

**parameters_id:** `typing.Optional[str]` — Identifier of the linked saved parameters object, or null if the experiment is not linked to saved parameters
    
</dd>
</dl>

<dl>
<dd>

**parameters_version:** `typing.Optional[str]` — Version number of the linked saved parameters object the experiment was run against.
    
</dd>
</dl>

<dl>
<dd>

**public:** `typing.Optional[bool]` — Whether or not the experiment is public. Public experiments can be viewed by anybody inside or outside the organization
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — User-controlled metadata about the experiment
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — A list of tags for the experiment
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.experiments.<a href="src/fern/experiments/client.py">post_experiment_id_insert</a>(...) -> InsertEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Insert a set of events into the experiment
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, InsertExperimentEvent
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.experiments.post_experiment_id_insert(
    experiment_id="experiment_id",
    events=[
        InsertExperimentEvent()
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

**experiment_id:** `ExperimentIdParam` — Experiment id
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.List[InsertExperimentEvent]` — A list of experiment events to insert
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.experiments.<a href="src/fern/experiments/client.py">get_experiment_id_fetch</a>(...) -> FetchExperimentEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the events in an experiment. Equivalent to the POST form of the same path, but with the parameters in the URL query rather than in the request body. For more complex queries, use the `POST /btql` endpoint.
</dd>
</dl>
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

client.experiments.get_experiment_id_fetch(
    experiment_id="experiment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**experiment_id:** `ExperimentIdParam` — Experiment id
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[FetchLimitParam]` 

limit the number of traces fetched

Fetch queries may be paginated if the total result size is expected to be large (e.g. project_logs which accumulate over a long time). Note that fetch queries only support pagination in descending time order (from latest to earliest `_xact_id`. Furthermore, later pages may return rows which showed up in earlier pages, except with an earlier `_xact_id`. This happens because pagination occurs over the whole version history of the event log. You will most likely want to exclude any such duplicate, outdated rows (by `id`) from your combined result set.

The `limit` parameter controls the number of full traces to return. So you may end up with more individual rows than the specified limit if you are fetching events containing traces.
    
</dd>
</dl>

<dl>
<dd>

**max_xact_id:** `typing.Optional[MaxXactId]` 

DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in favor of the explicit 'cursor' returned by object fetch requests. Please prefer the 'cursor' argument going forwards.

Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

Since a paginated fetch query returns results in order from latest to earliest, the cursor for the next page can be found as the row with the minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit` for an overview of paginating fetch queries.
    
</dd>
</dl>

<dl>
<dd>

**max_root_span_id:** `typing.Optional[MaxRootSpanId]` 

DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in favor of the explicit 'cursor' returned by object fetch requests. Please prefer the 'cursor' argument going forwards.

Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

Since a paginated fetch query returns results in order from latest to earliest, the cursor for the next page can be found as the row with the minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit` for an overview of paginating fetch queries.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[Version]` 

Retrieve a snapshot of events from a past time

The version id is essentially a filter on the latest event transaction id. You can use the `max_xact_id` returned by a past fetch as the version to reproduce that exact fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.experiments.<a href="src/fern/experiments/client.py">post_experiment_id_fetch</a>(...) -> FetchExperimentEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the events in an experiment. Equivalent to the GET form of the same path, but with the parameters in the request body rather than in the URL query. For more complex queries, use the `POST /btql` endpoint.
</dd>
</dl>
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

client.experiments.post_experiment_id_fetch(
    experiment_id="experiment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**experiment_id:** `ExperimentIdParam` — Experiment id
    
</dd>
</dl>

<dl>
<dd>

**request:** `FetchEventsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.experiments.<a href="src/fern/experiments/client.py">post_experiment_id_feedback</a>(...) -> FeedbackResponseSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Log feedback for a set of experiment events
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, FeedbackExperimentItem
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.experiments.post_experiment_id_feedback(
    experiment_id="experiment_id",
    feedback=[
        FeedbackExperimentItem(
            id="id",
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

**experiment_id:** `ExperimentIdParam` — Experiment id
    
</dd>
</dl>

<dl>
<dd>

**feedback:** `typing.List[FeedbackExperimentItem]` — A list of experiment feedback items
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.experiments.<a href="src/fern/experiments/client.py">get_experiment_id_summarize</a>(...) -> SummarizeExperimentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Summarize experiment
</dd>
</dl>
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

client.experiments.get_experiment_id_summarize(
    experiment_id="experiment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**experiment_id:** `ExperimentIdParam` — Experiment id
    
</dd>
</dl>

<dl>
<dd>

**summarize_scores:** `typing.Optional[SummarizeScores]` — Whether to summarize the scores and metrics. If false (or omitted), only the metadata will be returned.
    
</dd>
</dl>

<dl>
<dd>

**comparison_experiment_id:** `typing.Optional[ComparisonExperimentId]` — The experiment to compare against, if summarizing scores and metrics. If omitted, will fall back to the `base_exp_id` stored in the experiment metadata, and then to the most recent experiment run in the same project. Must pass `summarize_scores=true` for this id to be used
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Datasets
<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">get_dataset</a>(...) -> GetDatasetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all datasets. The datasets are sorted by creation date, with the most recently-created datasets coming first
</dd>
</dl>
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

client.datasets.get_dataset()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**dataset_name:** `typing.Optional[DatasetName]` — Name of the dataset to search for
    
</dd>
</dl>

<dl>
<dd>

**project_name:** `typing.Optional[ProjectName]` — Name of the project to search for
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[ProjectIdQuery]` — Project id
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">post_dataset</a>(...) -> Dataset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new dataset. If there is an existing dataset in the project with the same name as the one specified in the request, will return the existing dataset unmodified
</dd>
</dl>
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

client.datasets.post_dataset(
    project_id="project_id",
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

**project_id:** `str` — Unique identifier for the project that the dataset belongs under
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the dataset. Within a project, dataset names are unique
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Textual description of the dataset
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — A list of tags for the dataset
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — User-controlled metadata about the dataset
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">get_dataset_id</a>(...) -> Dataset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a dataset object by its id
</dd>
</dl>
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

client.datasets.get_dataset_id(
    dataset_id="dataset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `DatasetIdParam` — Dataset id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">delete_dataset_id</a>(...) -> Dataset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a dataset object by its id
</dd>
</dl>
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

client.datasets.delete_dataset_id(
    dataset_id="dataset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `DatasetIdParam` — Dataset id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">patch_dataset_id</a>(...) -> Dataset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update a dataset object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.
</dd>
</dl>
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

client.datasets.patch_dataset_id(
    dataset_id="dataset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `DatasetIdParam` — Dataset id
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the dataset. Within a project, dataset names are unique
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Textual description of the dataset
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — A list of tags for the dataset
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — User-controlled metadata about the dataset
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">post_dataset_id_insert</a>(...) -> InsertEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Insert a set of events into the dataset
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, InsertDatasetEvent
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.datasets.post_dataset_id_insert(
    dataset_id="dataset_id",
    events=[
        InsertDatasetEvent()
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

**dataset_id:** `DatasetIdParam` — Dataset id
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.List[InsertDatasetEvent]` — A list of dataset events to insert
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">get_dataset_id_fetch</a>(...) -> FetchDatasetEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the events in a dataset. Equivalent to the POST form of the same path, but with the parameters in the URL query rather than in the request body. For more complex queries, use the `POST /btql` endpoint.
</dd>
</dl>
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

client.datasets.get_dataset_id_fetch(
    dataset_id="dataset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `DatasetIdParam` — Dataset id
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[FetchLimitParam]` 

limit the number of traces fetched

Fetch queries may be paginated if the total result size is expected to be large (e.g. project_logs which accumulate over a long time). Note that fetch queries only support pagination in descending time order (from latest to earliest `_xact_id`. Furthermore, later pages may return rows which showed up in earlier pages, except with an earlier `_xact_id`. This happens because pagination occurs over the whole version history of the event log. You will most likely want to exclude any such duplicate, outdated rows (by `id`) from your combined result set.

The `limit` parameter controls the number of full traces to return. So you may end up with more individual rows than the specified limit if you are fetching events containing traces.
    
</dd>
</dl>

<dl>
<dd>

**max_xact_id:** `typing.Optional[MaxXactId]` 

DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in favor of the explicit 'cursor' returned by object fetch requests. Please prefer the 'cursor' argument going forwards.

Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

Since a paginated fetch query returns results in order from latest to earliest, the cursor for the next page can be found as the row with the minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit` for an overview of paginating fetch queries.
    
</dd>
</dl>

<dl>
<dd>

**max_root_span_id:** `typing.Optional[MaxRootSpanId]` 

DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in favor of the explicit 'cursor' returned by object fetch requests. Please prefer the 'cursor' argument going forwards.

Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

Since a paginated fetch query returns results in order from latest to earliest, the cursor for the next page can be found as the row with the minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit` for an overview of paginating fetch queries.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[Version]` 

Retrieve a snapshot of events from a past time

The version id is essentially a filter on the latest event transaction id. You can use the `max_xact_id` returned by a past fetch as the version to reproduce that exact fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">post_dataset_id_fetch</a>(...) -> FetchDatasetEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the events in a dataset. Equivalent to the GET form of the same path, but with the parameters in the request body rather than in the URL query. For more complex queries, use the `POST /btql` endpoint.
</dd>
</dl>
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

client.datasets.post_dataset_id_fetch(
    dataset_id="dataset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `DatasetIdParam` — Dataset id
    
</dd>
</dl>

<dl>
<dd>

**request:** `FetchEventsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">post_dataset_id_feedback</a>(...) -> FeedbackResponseSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Log feedback for a set of dataset events
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, FeedbackDatasetItem
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.datasets.post_dataset_id_feedback(
    dataset_id="dataset_id",
    feedback=[
        FeedbackDatasetItem(
            id="id",
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

**dataset_id:** `DatasetIdParam` — Dataset id
    
</dd>
</dl>

<dl>
<dd>

**feedback:** `typing.List[FeedbackDatasetItem]` — A list of dataset feedback items
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">get_dataset_id_summarize</a>(...) -> SummarizeDatasetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Summarize dataset
</dd>
</dl>
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

client.datasets.get_dataset_id_summarize(
    dataset_id="dataset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `DatasetIdParam` — Dataset id
    
</dd>
</dl>

<dl>
<dd>

**summarize_data:** `typing.Optional[SummarizeData]` — Whether to summarize the data. If false (or omitted), only the metadata will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Prompts
<details><summary><code>client.prompts.<a href="src/fern/prompts/client.py">get_prompt</a>(...) -> GetPromptResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all prompts. The prompts are sorted by creation date, with the most recently-created prompts coming first
</dd>
</dl>
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

client.prompts.get_prompt()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**prompt_name:** `typing.Optional[PromptName]` — Name of the prompt to search for
    
</dd>
</dl>

<dl>
<dd>

**project_name:** `typing.Optional[ProjectName]` — Name of the project to search for
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[ProjectIdQuery]` — Project id
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[Slug]` — Retrieve prompt with a specific slug
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[PromptVersion]` 

Retrieve prompt at a specific version.

The version id can either be a transaction id (e.g. '1000192656880881099') or a version identifier (e.g. '81cd05ee665fdfb3').
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[PromptEnvironment]` 

Filter by environment slug. Cannot be used together with `version`.

For `GET /v1/prompt`, environment resolution currently requires the request to match a single prompt. If multiple prompts match, the endpoint returns `400` (for example when `limit=1` is not set). Use `limit=1` or other filters (for example `slug`, `project_id`) to narrow results.
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompts.<a href="src/fern/prompts/client.py">post_prompt</a>(...) -> Prompt</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new prompt. If there is an existing prompt in the project with the same slug as the one specified in the request, will return the existing prompt unmodified
</dd>
</dl>
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

client.prompts.post_prompt(
    project_id="project_id",
    name="name",
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

**request:** `CreatePrompt` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompts.<a href="src/fern/prompts/client.py">put_prompt</a>(...) -> Prompt</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace prompt. If there is an existing prompt in the project with the same slug as the one specified in the request, will replace the existing prompt with the provided fields
</dd>
</dl>
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

client.prompts.put_prompt(
    project_id="project_id",
    name="name",
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

**request:** `CreatePrompt` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompts.<a href="src/fern/prompts/client.py">get_prompt_id</a>(...) -> Prompt</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a prompt object by its id
</dd>
</dl>
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

client.prompts.get_prompt_id(
    prompt_id="prompt_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt_id:** `PromptIdParam` — Prompt id
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[PromptVersion]` 

Retrieve prompt at a specific version.

The version id can either be a transaction id (e.g. '1000192656880881099') or a version identifier (e.g. '81cd05ee665fdfb3').
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[PromptEnvironment]` 

Filter by environment slug. Cannot be used together with `version`.

For `GET /v1/prompt`, environment resolution currently requires the request to match a single prompt. If multiple prompts match, the endpoint returns `400` (for example when `limit=1` is not set). Use `limit=1` or other filters (for example `slug`, `project_id`) to narrow results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompts.<a href="src/fern/prompts/client.py">delete_prompt_id</a>(...) -> Prompt</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a prompt object by its id
</dd>
</dl>
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

client.prompts.delete_prompt_id(
    prompt_id="prompt_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt_id:** `PromptIdParam` — Prompt id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompts.<a href="src/fern/prompts/client.py">patch_prompt_id</a>(...) -> Prompt</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update a prompt object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.
</dd>
</dl>
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

client.prompts.patch_prompt_id(
    prompt_id="prompt_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt_id:** `PromptIdParam` — Prompt id
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the prompt
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` — Unique identifier for the prompt
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Textual description of the prompt
    
</dd>
</dl>

<dl>
<dd>

**prompt_data:** `typing.Optional[PromptDataNullish]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — A list of tags for the prompt
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Roles
<details><summary><code>client.roles.<a href="src/fern/roles/client.py">get_role</a>(...) -> GetRoleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all roles. The roles are sorted by creation date, with the most recently-created roles coming first
</dd>
</dl>
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

client.roles.get_role()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**role_name:** `typing.Optional[RoleName]` — Name of the role to search for
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/fern/roles/client.py">post_role</a>(...) -> Role</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new role. If there is an existing role with the same name as the one specified in the request, will return the existing role unmodified
</dd>
</dl>
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

client.roles.post_role(
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

**request:** `CreateRole` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/fern/roles/client.py">put_role</a>(...) -> Role</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace role. If there is an existing role with the same name as the one specified in the request, will replace the existing role with the provided fields
</dd>
</dl>
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

client.roles.put_role(
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

**request:** `CreateRole` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/fern/roles/client.py">get_role_id</a>(...) -> Role</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a role object by its id
</dd>
</dl>
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

client.roles.get_role_id(
    role_id="role_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**role_id:** `RoleIdParam` — Role id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/fern/roles/client.py">delete_role_id</a>(...) -> Role</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a role object by its id
</dd>
</dl>
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

client.roles.delete_role_id(
    role_id="role_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**role_id:** `RoleIdParam` — Role id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/fern/roles/client.py">patch_role_id</a>(...) -> Role</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update a role object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.
</dd>
</dl>
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

client.roles.patch_role_id(
    role_id="role_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**role_id:** `RoleIdParam` — Role id
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Textual description of the role
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the role
    
</dd>
</dl>

<dl>
<dd>

**add_member_permissions:** `typing.Optional[typing.List[PatchRoleAddMemberPermissionsItem]]` — A list of permissions to add to the role
    
</dd>
</dl>

<dl>
<dd>

**remove_member_permissions:** `typing.Optional[typing.List[PatchRoleRemoveMemberPermissionsItem]]` — A list of permissions to remove from the role
    
</dd>
</dl>

<dl>
<dd>

**add_member_roles:** `typing.Optional[typing.List[str]]` — A list of role IDs to add to the role's inheriting-from set
    
</dd>
</dl>

<dl>
<dd>

**remove_member_roles:** `typing.Optional[typing.List[str]]` — A list of role IDs to remove from the role's inheriting-from set
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Groups
<details><summary><code>client.groups.<a href="src/fern/groups/client.py">get_group</a>(...) -> GetGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all groups. The groups are sorted by creation date, with the most recently-created groups coming first
</dd>
</dl>
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

client.groups.get_group()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[GroupName]` — Name of the group to search for
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">post_group</a>(...) -> Group</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new group. If there is an existing group with the same name as the one specified in the request, will return the existing group unmodified
</dd>
</dl>
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

client.groups.post_group(
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

**request:** `CreateGroup` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">put_group</a>(...) -> Group</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace group. If there is an existing group with the same name as the one specified in the request, will replace the existing group with the provided fields
</dd>
</dl>
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

client.groups.put_group(
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

**request:** `CreateGroup` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">get_group_id</a>(...) -> Group</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a group object by its id
</dd>
</dl>
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

client.groups.get_group_id(
    group_id="group_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupIdParam` — Group id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">delete_group_id</a>(...) -> Group</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a group object by its id
</dd>
</dl>
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

client.groups.delete_group_id(
    group_id="group_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupIdParam` — Group id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">patch_group_id</a>(...) -> Group</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update a group object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.
</dd>
</dl>
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

client.groups.patch_group_id(
    group_id="group_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `GroupIdParam` — Group id
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Textual description of the group
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the group
    
</dd>
</dl>

<dl>
<dd>

**add_member_users:** `typing.Optional[typing.List[str]]` — A list of user IDs to add to the group
    
</dd>
</dl>

<dl>
<dd>

**remove_member_users:** `typing.Optional[typing.List[str]]` — A list of user IDs to remove from the group
    
</dd>
</dl>

<dl>
<dd>

**add_member_groups:** `typing.Optional[typing.List[str]]` — A list of group IDs to add to the group's inheriting-from set
    
</dd>
</dl>

<dl>
<dd>

**remove_member_groups:** `typing.Optional[typing.List[str]]` — A list of group IDs to remove from the group's inheriting-from set
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Acls
<details><summary><code>client.acls.<a href="src/fern/acls/client.py">get_acl</a>(...) -> GetAclResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all acls. The acls are sorted by creation date, with the most recently-created acls coming first
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AclObjectType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.acls.get_acl(
    object_type=AclObjectType.ORGANIZATION,
    object_id="object_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_type:** `AclObjectType` — The object type that the ACL applies to
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `AclObjectId` — The id of the object the ACL applies to
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[AclListUserId]` — Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will be provided
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[AclListGroupId]` — Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will be provided
    
</dd>
</dl>

<dl>
<dd>

**permission:** `typing.Optional[AclListPermission]` 

Each permission permits a certain type of operation on an object in the system

Permissions can be assigned to to objects on an individual basis, or grouped into roles
    
</dd>
</dl>

<dl>
<dd>

**restrict_object_type:** `typing.Optional[AclListRestrictObjectType]` — The object type that the ACL applies to
    
</dd>
</dl>

<dl>
<dd>

**role_id:** `typing.Optional[AclListRoleId]` — Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be provided
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.acls.<a href="src/fern/acls/client.py">post_acl</a>(...) -> Acl</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new acl. If there is an existing acl with the same contents as the one specified in the request, will return the existing acl unmodified
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AclObjectType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.acls.post_acl(
    object_type=AclObjectType.ORGANIZATION,
    object_id="object_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `AclItem` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.acls.<a href="src/fern/acls/client.py">delete_acl</a>(...) -> Acl</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a single acl
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AclObjectType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.acls.delete_acl(
    object_type=AclObjectType.ORGANIZATION,
    object_id="object_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `AclItem` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.acls.<a href="src/fern/acls/client.py">get_acl_id</a>(...) -> Acl</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an acl object by its id
</dd>
</dl>
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

client.acls.get_acl_id(
    acl_id="acl_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**acl_id:** `AclIdParam` — Acl id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.acls.<a href="src/fern/acls/client.py">delete_acl_id</a>(...) -> Acl</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an acl object by its id
</dd>
</dl>
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

client.acls.delete_acl_id(
    acl_id="acl_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**acl_id:** `AclIdParam` — Acl id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.acls.<a href="src/fern/acls/client.py">acl_batch_update</a>(...) -> AclBatchUpdateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Batch update acls. This operation is idempotent, so adding acls which already exist will have no effect, and removing acls which do not exist will have no effect.
</dd>
</dl>
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

client.acls.acl_batch_update()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**add_acls:** `typing.Optional[typing.List[AclItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**remove_acls:** `typing.Optional[typing.List[AclItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.acls.<a href="src/fern/acls/client.py">acl_list_org</a>(...) -> typing.List[Acl]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all acls in the org. This query requires the caller to have `read_acls` permission at the organization level
</dd>
</dl>
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

client.acls.acl_list_org()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `typing.Optional[AclListOrgObjectType]` — The object type that the ACL applies to
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `typing.Optional[AclListOrgObjectId]` — The id of the object the ACL applies to
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[AclListUserId]` — Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will be provided
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[AclListGroupId]` — Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will be provided
    
</dd>
</dl>

<dl>
<dd>

**permission:** `typing.Optional[AclListPermission]` 

Each permission permits a certain type of operation on an object in the system

Permissions can be assigned to to objects on an individual basis, or grouped into roles
    
</dd>
</dl>

<dl>
<dd>

**restrict_object_type:** `typing.Optional[AclListRestrictObjectType]` — The object type that the ACL applies to
    
</dd>
</dl>

<dl>
<dd>

**role_id:** `typing.Optional[AclListRoleId]` — Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be provided
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users
<details><summary><code>client.users.<a href="src/fern/users/client.py">get_user</a>(...) -> GetUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all users. The users are sorted by creation date, with the most recently-created users coming first
</dd>
</dl>
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

client.users.get_user()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**given_name:** `typing.Optional[UserGivenName]` — Given name of the user to search for. You may pass the param multiple times to filter for more than one given name
    
</dd>
</dl>

<dl>
<dd>

**family_name:** `typing.Optional[UserFamilyName]` — Family name of the user to search for. You may pass the param multiple times to filter for more than one family name
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[UserEmail]` — Email of the user to search for. You may pass the param multiple times to filter for more than one email
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">get_user_id</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a user object by its id
</dd>
</dl>
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

client.users.get_user_id(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `UserIdParam` — User id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ProjectAutomations
<details><summary><code>client.project_automations.<a href="src/fern/project_automations/client.py">get_project_automation</a>(...) -> GetProjectAutomationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all project_automations. The project_automations are sorted by creation date, with the most recently-created project_automations coming first
</dd>
</dl>
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

client.project_automations.get_project_automation()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**project_automation_name:** `typing.Optional[ProjectAutomationName]` — Name of the project_automation to search for
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_automations.<a href="src/fern/project_automations/client.py">post_project_automation</a>(...) -> ProjectAutomation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new project_automation. If there is an existing project_automation with the same name as the one specified in the request, will return the existing project_automation unmodified
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, CreateProjectAutomationConfig_Logs, CreateProjectAutomationConfigLogsAction_Webhook
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.project_automations.post_project_automation(
    project_id="project_id",
    name="name",
    config=CreateProjectAutomationConfig_Logs(
        btql_filter="btql_filter",
        interval_seconds=1.1,
        action=CreateProjectAutomationConfigLogsAction_Webhook(
            url="url",
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

**request:** `CreateProjectAutomation` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_automations.<a href="src/fern/project_automations/client.py">put_project_automation</a>(...) -> ProjectAutomation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace project_automation. If there is an existing project_automation with the same name as the one specified in the request, will replace the existing project_automation with the provided fields
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, CreateProjectAutomationConfig_Logs, CreateProjectAutomationConfigLogsAction_Webhook
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.project_automations.put_project_automation(
    project_id="project_id",
    name="name",
    config=CreateProjectAutomationConfig_Logs(
        btql_filter="btql_filter",
        interval_seconds=1.1,
        action=CreateProjectAutomationConfigLogsAction_Webhook(
            url="url",
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

**request:** `CreateProjectAutomation` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_automations.<a href="src/fern/project_automations/client.py">get_project_automation_id</a>(...) -> ProjectAutomation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a project_automation object by its id
</dd>
</dl>
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

client.project_automations.get_project_automation_id(
    project_automation_id="project_automation_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_automation_id:** `ProjectAutomationIdParam` — ProjectAutomation id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_automations.<a href="src/fern/project_automations/client.py">delete_project_automation_id</a>(...) -> ProjectAutomation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a project_automation object by its id
</dd>
</dl>
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

client.project_automations.delete_project_automation_id(
    project_automation_id="project_automation_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_automation_id:** `ProjectAutomationIdParam` — ProjectAutomation id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_automations.<a href="src/fern/project_automations/client.py">patch_project_automation_id</a>(...) -> ProjectAutomation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update a project_automation object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.
</dd>
</dl>
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

client.project_automations.patch_project_automation_id(
    project_automation_id="project_automation_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_automation_id:** `ProjectAutomationIdParam` — ProjectAutomation id
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the project automation
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Textual description of the project automation
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[PatchProjectAutomationConfig]` — The configuration for the automation rule
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ProjectScores
<details><summary><code>client.project_scores.<a href="src/fern/project_scores/client.py">get_project_score</a>(...) -> GetProjectScoreResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all project_scores. The project_scores are sorted by creation date, with the most recently-created project_scores coming first
</dd>
</dl>
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

client.project_scores.get_project_score()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**project_score_name:** `typing.Optional[ProjectScoreName]` — Name of the project_score to search for
    
</dd>
</dl>

<dl>
<dd>

**project_name:** `typing.Optional[ProjectName]` — Name of the project to search for
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[ProjectIdQuery]` — Project id
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**score_type:** `typing.Optional[GetProjectScoreRequestScoreType]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_scores.<a href="src/fern/project_scores/client.py">post_project_score</a>(...) -> ProjectScore</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new project_score. If there is an existing project_score in the project with the same name as the one specified in the request, will return the existing project_score unmodified
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ProjectScoreType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.project_scores.post_project_score(
    project_id="project_id",
    name="name",
    score_type=ProjectScoreType.SLIDER,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateProjectScore` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_scores.<a href="src/fern/project_scores/client.py">put_project_score</a>(...) -> ProjectScore</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace project_score. If there is an existing project_score in the project with the same name as the one specified in the request, will replace the existing project_score with the provided fields
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ProjectScoreType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.project_scores.put_project_score(
    project_id="project_id",
    name="name",
    score_type=ProjectScoreType.SLIDER,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateProjectScore` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_scores.<a href="src/fern/project_scores/client.py">get_project_score_id</a>(...) -> ProjectScore</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a project_score object by its id
</dd>
</dl>
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

client.project_scores.get_project_score_id(
    project_score_id="project_score_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_score_id:** `ProjectScoreIdParam` — ProjectScore id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_scores.<a href="src/fern/project_scores/client.py">delete_project_score_id</a>(...) -> ProjectScore</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a project_score object by its id
</dd>
</dl>
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

client.project_scores.delete_project_score_id(
    project_score_id="project_score_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_score_id:** `ProjectScoreIdParam` — ProjectScore id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_scores.<a href="src/fern/project_scores/client.py">patch_project_score_id</a>(...) -> ProjectScore</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update a project_score object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.
</dd>
</dl>
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

client.project_scores.patch_project_score_id(
    project_score_id="project_score_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_score_id:** `ProjectScoreIdParam` — ProjectScore id
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the project score
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Textual description of the project score
    
</dd>
</dl>

<dl>
<dd>

**score_type:** `typing.Optional[ProjectScoreType]` 
    
</dd>
</dl>

<dl>
<dd>

**categories:** `typing.Optional[ProjectScoreCategories]` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[ProjectScoreConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ProjectTags
<details><summary><code>client.project_tags.<a href="src/fern/project_tags/client.py">get_project_tag</a>(...) -> GetProjectTagResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all project_tags. The project_tags are sorted by creation date, with the most recently-created project_tags coming first
</dd>
</dl>
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

client.project_tags.get_project_tag()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**project_tag_name:** `typing.Optional[ProjectTagName]` — Name of the project_tag to search for
    
</dd>
</dl>

<dl>
<dd>

**project_name:** `typing.Optional[ProjectName]` — Name of the project to search for
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[ProjectIdQuery]` — Project id
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_tags.<a href="src/fern/project_tags/client.py">post_project_tag</a>(...) -> ProjectTag</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new project_tag. If there is an existing project_tag in the project with the same name as the one specified in the request, will return the existing project_tag unmodified
</dd>
</dl>
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

client.project_tags.post_project_tag(
    project_id="project_id",
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

**request:** `CreateProjectTag` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_tags.<a href="src/fern/project_tags/client.py">put_project_tag</a>(...) -> ProjectTag</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace project_tag. If there is an existing project_tag in the project with the same name as the one specified in the request, will replace the existing project_tag with the provided fields
</dd>
</dl>
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

client.project_tags.put_project_tag(
    project_id="project_id",
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

**request:** `CreateProjectTag` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_tags.<a href="src/fern/project_tags/client.py">get_project_tag_id</a>(...) -> ProjectTag</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a project_tag object by its id
</dd>
</dl>
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

client.project_tags.get_project_tag_id(
    project_tag_id="project_tag_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_tag_id:** `ProjectTagIdParam` — ProjectTag id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_tags.<a href="src/fern/project_tags/client.py">delete_project_tag_id</a>(...) -> ProjectTag</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a project_tag object by its id
</dd>
</dl>
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

client.project_tags.delete_project_tag_id(
    project_tag_id="project_tag_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_tag_id:** `ProjectTagIdParam` — ProjectTag id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project_tags.<a href="src/fern/project_tags/client.py">patch_project_tag_id</a>(...) -> ProjectTag</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update a project_tag object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.
</dd>
</dl>
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

client.project_tags.patch_project_tag_id(
    project_tag_id="project_tag_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_tag_id:** `ProjectTagIdParam` — ProjectTag id
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the project tag
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Textual description of the project tag
    
</dd>
</dl>

<dl>
<dd>

**color:** `typing.Optional[str]` — Color of the tag for the UI
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SpanIframes
<details><summary><code>client.span_iframes.<a href="src/fern/span_iframes/client.py">get_span_iframe</a>(...) -> GetSpanIframeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all span_iframes. The span_iframes are sorted by creation date, with the most recently-created span_iframes coming first
</dd>
</dl>
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

client.span_iframes.get_span_iframe()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**span_iframe_name:** `typing.Optional[SpanIframeName]` — Name of the span_iframe to search for
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.span_iframes.<a href="src/fern/span_iframes/client.py">post_span_iframe</a>(...) -> SpanIFrame</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new span_iframe. If there is an existing span_iframe with the same name as the one specified in the request, will return the existing span_iframe unmodified
</dd>
</dl>
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

client.span_iframes.post_span_iframe(
    project_id="project_id",
    name="name",
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateSpanIFrame` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.span_iframes.<a href="src/fern/span_iframes/client.py">put_span_iframe</a>(...) -> SpanIFrame</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace span_iframe. If there is an existing span_iframe with the same name as the one specified in the request, will replace the existing span_iframe with the provided fields
</dd>
</dl>
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

client.span_iframes.put_span_iframe(
    project_id="project_id",
    name="name",
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateSpanIFrame` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.span_iframes.<a href="src/fern/span_iframes/client.py">get_span_iframe_id</a>(...) -> SpanIFrame</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a span_iframe object by its id
</dd>
</dl>
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

client.span_iframes.get_span_iframe_id(
    span_iframe_id="span_iframe_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**span_iframe_id:** `SpanIframeIdParam` — SpanIframe id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.span_iframes.<a href="src/fern/span_iframes/client.py">delete_span_iframe_id</a>(...) -> SpanIFrame</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a span_iframe object by its id
</dd>
</dl>
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

client.span_iframes.delete_span_iframe_id(
    span_iframe_id="span_iframe_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**span_iframe_id:** `SpanIframeIdParam` — SpanIframe id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.span_iframes.<a href="src/fern/span_iframes/client.py">patch_span_iframe_id</a>(...) -> SpanIFrame</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update a span_iframe object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.
</dd>
</dl>
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

client.span_iframes.patch_span_iframe_id(
    span_iframe_id="span_iframe_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**span_iframe_id:** `SpanIframeIdParam` — SpanIframe id
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the span iframe
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — URL to embed the project viewer in an iframe
    
</dd>
</dl>

<dl>
<dd>

**post_message:** `typing.Optional[bool]` — Whether to post messages to the iframe containing the span's data. This is useful when you want to render more data than fits in the URL.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Textual description of the span iframe
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EvalStatusPages
<details><summary><code>client.eval_status_pages.<a href="src/fern/eval_status_pages/client.py">get_eval_status_page</a>(...) -> GetEvalStatusPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all eval_status_pages. The eval_status_pages are sorted by creation date, with the most recently-created eval_status_pages coming first
</dd>
</dl>
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

client.eval_status_pages.get_eval_status_page()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**eval_status_page_name:** `typing.Optional[EvalStatusPageName]` — Name of the eval_status_page to search for
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.eval_status_pages.<a href="src/fern/eval_status_pages/client.py">post_eval_status_page</a>(...) -> EvalStatusPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new eval_status_page. If there is an existing eval_status_page with the same name as the one specified in the request, will return the existing eval_status_page unmodified
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, EvalStatusPageTheme, EvalStatusPageConfig
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.eval_status_pages.post_eval_status_page(
    project_id="project_id",
    name="name",
    theme=EvalStatusPageTheme.LIGHT,
    config=EvalStatusPageConfig(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateEvalStatusPage` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.eval_status_pages.<a href="src/fern/eval_status_pages/client.py">put_eval_status_page</a>(...) -> EvalStatusPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace eval_status_page. If there is an existing eval_status_page with the same name as the one specified in the request, will replace the existing eval_status_page with the provided fields
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, EvalStatusPageTheme, EvalStatusPageConfig
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.eval_status_pages.put_eval_status_page(
    project_id="project_id",
    name="name",
    theme=EvalStatusPageTheme.LIGHT,
    config=EvalStatusPageConfig(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateEvalStatusPage` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.eval_status_pages.<a href="src/fern/eval_status_pages/client.py">get_eval_status_page_id</a>(...) -> EvalStatusPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a eval_status_page object by its id
</dd>
</dl>
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

client.eval_status_pages.get_eval_status_page_id(
    eval_status_page_id="eval_status_page_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**eval_status_page_id:** `EvalStatusPageIdParam` — EvalStatusPage id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.eval_status_pages.<a href="src/fern/eval_status_pages/client.py">delete_eval_status_page_id</a>(...) -> EvalStatusPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a eval_status_page object by its id
</dd>
</dl>
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

client.eval_status_pages.delete_eval_status_page_id(
    eval_status_page_id="eval_status_page_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**eval_status_page_id:** `EvalStatusPageIdParam` — EvalStatusPage id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.eval_status_pages.<a href="src/fern/eval_status_pages/client.py">patch_eval_status_page_id</a>(...) -> EvalStatusPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update a eval_status_page object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.
</dd>
</dl>
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

client.eval_status_pages.patch_eval_status_page_id(
    eval_status_page_id="eval_status_page_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**eval_status_page_id:** `EvalStatusPageIdParam` — EvalStatusPage id
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the eval status page
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Textual description of the eval status page
    
</dd>
</dl>

<dl>
<dd>

**logo_url:** `typing.Optional[str]` — URL of the logo to display on the page
    
</dd>
</dl>

<dl>
<dd>

**theme:** `typing.Optional[EvalStatusPageTheme]` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[EvalStatusPageConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Functions
<details><summary><code>client.functions.<a href="src/fern/functions/client.py">get_function</a>(...) -> GetFunctionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all functions. The functions are sorted by creation date, with the most recently-created functions coming first
</dd>
</dl>
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

client.functions.get_function()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**function_name:** `typing.Optional[FunctionName]` — Name of the function to search for
    
</dd>
</dl>

<dl>
<dd>

**project_name:** `typing.Optional[ProjectName]` — Name of the project to search for
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[ProjectIdQuery]` — Project id
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[Slug]` — Retrieve prompt with a specific slug
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[PromptVersion]` 

Retrieve prompt at a specific version.

The version id can either be a transaction id (e.g. '1000192656880881099') or a version identifier (e.g. '81cd05ee665fdfb3').
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[PromptEnvironment]` 

Filter by environment slug. Cannot be used together with `version`.

For `GET /v1/prompt`, environment resolution currently requires the request to match a single prompt. If multiple prompts match, the endpoint returns `400` (for example when `limit=1` is not set). Use `limit=1` or other filters (for example `slug`, `project_id`) to narrow results.
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.functions.<a href="src/fern/functions/client.py">post_function</a>(...) -> Function</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new function. If there is an existing function in the project with the same slug as the one specified in the request, will return the existing function unmodified
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, FunctionDataZero, FunctionDataZeroType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.functions.post_function(
    project_id="project_id",
    name="name",
    slug="slug",
    function_data=FunctionDataZero(
        type=FunctionDataZeroType.PROMPT,
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

**request:** `CreateFunction` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.functions.<a href="src/fern/functions/client.py">put_function</a>(...) -> Function</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace function. If there is an existing function in the project with the same slug as the one specified in the request, will replace the existing function with the provided fields
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, FunctionDataZero, FunctionDataZeroType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.functions.put_function(
    project_id="project_id",
    name="name",
    slug="slug",
    function_data=FunctionDataZero(
        type=FunctionDataZeroType.PROMPT,
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

**request:** `CreateFunction` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.functions.<a href="src/fern/functions/client.py">get_function_id</a>(...) -> Function</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a function object by its id
</dd>
</dl>
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

client.functions.get_function_id(
    function_id="function_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**function_id:** `FunctionIdParam` — Function id
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[PromptVersion]` 

Retrieve prompt at a specific version.

The version id can either be a transaction id (e.g. '1000192656880881099') or a version identifier (e.g. '81cd05ee665fdfb3').
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[PromptEnvironment]` 

Filter by environment slug. Cannot be used together with `version`.

For `GET /v1/prompt`, environment resolution currently requires the request to match a single prompt. If multiple prompts match, the endpoint returns `400` (for example when `limit=1` is not set). Use `limit=1` or other filters (for example `slug`, `project_id`) to narrow results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.functions.<a href="src/fern/functions/client.py">delete_function_id</a>(...) -> Function</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a function object by its id
</dd>
</dl>
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

client.functions.delete_function_id(
    function_id="function_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**function_id:** `FunctionIdParam` — Function id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.functions.<a href="src/fern/functions/client.py">patch_function_id</a>(...) -> Function</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update a function object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.
</dd>
</dl>
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

client.functions.patch_function_id(
    function_id="function_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**function_id:** `FunctionIdParam` — Function id
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the prompt
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Textual description of the prompt
    
</dd>
</dl>

<dl>
<dd>

**prompt_data:** `typing.Optional[PromptDataNullish]` 
    
</dd>
</dl>

<dl>
<dd>

**function_data:** `typing.Optional[FunctionDataNullish]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — A list of tags for the prompt
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.functions.<a href="src/fern/functions/client.py">post_function_id_invoke</a>(...) -> typing.Optional[typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invoke a function.
</dd>
</dl>
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

client.functions.post_function_id_invoke(
    function_id="function_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**function_id:** `FunctionIdParam` — Function id
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Optional[typing.Any]` — Argument to the function, which can be any JSON serializable value
    
</dd>
</dl>

<dl>
<dd>

**expected:** `typing.Optional[typing.Any]` — The expected output of the function
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Any relevant metadata. This will be logged and available as the `metadata` argument.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — Any relevant tags to log on the span.
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Optional[typing.List[ChatCompletionMessageParam]]` — If the function is an LLM, additional messages to pass along to it
    
</dd>
</dl>

<dl>
<dd>

**parent:** `typing.Optional[InvokeParent]` 
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Optional[bool]` — Whether to stream the response. If true, results will be returned in the Braintrust SSE format.
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[StreamingMode]` 
    
</dd>
</dl>

<dl>
<dd>

**strict:** `typing.Optional[bool]` — If true, throw an error if one of the variables in the prompt is not present in the input
    
</dd>
</dl>

<dl>
<dd>

**mcp_auth:** `typing.Optional[typing.Dict[str, InvokeApiMcpAuthValue]]` — Map of MCP server URL to auth credentials
    
</dd>
</dl>

<dl>
<dd>

**overrides:** `typing.Optional[typing.Dict[str, typing.Any]]` — Partial function definition to merge with the function being invoked. Fields are validated against the function type's schema at runtime. For facets: { preprocessor?, prompt?, model? }. For prompts: { model?, ... }.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — The version of the function
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Views
<details><summary><code>client.views.<a href="src/fern/views/client.py">get_view</a>(...) -> GetViewResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all views. The views are sorted by creation date, with the most recently-created views coming first
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AclObjectType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.views.get_view(
    object_type=AclObjectType.ORGANIZATION,
    object_id="object_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_type:** `AclObjectType` — The object type that the ACL applies to
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `AclObjectId` — The id of the object the ACL applies to
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**view_name:** `typing.Optional[ViewName]` — Name of the view to search for
    
</dd>
</dl>

<dl>
<dd>

**view_type:** `typing.Optional[ViewType]` — Type of object that the view corresponds to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.views.<a href="src/fern/views/client.py">post_view</a>(...) -> View</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new view. If there is an existing view with the same name as the one specified in the request, will return the existing view unmodified
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AclObjectType, CreateViewViewType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.views.post_view(
    object_type=AclObjectType.ORGANIZATION,
    object_id="object_id",
    view_type=CreateViewViewType.PROJECTS,
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

**request:** `CreateView` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.views.<a href="src/fern/views/client.py">put_view</a>(...) -> View</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace view. If there is an existing view with the same name as the one specified in the request, will replace the existing view with the provided fields
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AclObjectType, CreateViewViewType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.views.put_view(
    object_type=AclObjectType.ORGANIZATION,
    object_id="object_id",
    view_type=CreateViewViewType.PROJECTS,
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

**request:** `CreateView` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.views.<a href="src/fern/views/client.py">get_view_id</a>(...) -> View</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a view object by its id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AclObjectType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.views.get_view_id(
    view_id="view_id",
    object_type=AclObjectType.ORGANIZATION,
    object_id="object_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**view_id:** `ViewIdParam` — View id
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `AclObjectType` — The object type that the ACL applies to
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `AclObjectId` — The id of the object the ACL applies to
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.views.<a href="src/fern/views/client.py">delete_view_id</a>(...) -> View</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a view object by its id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AclObjectType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.views.delete_view_id(
    view_id="view_id",
    object_type=AclObjectType.ORGANIZATION,
    object_id="object_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**view_id:** `ViewIdParam` — View id
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `AclObjectType` 
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `str` — The id of the object the view applies to
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.views.<a href="src/fern/views/client.py">patch_view_id</a>(...) -> View</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update a view object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AclObjectType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.views.patch_view_id(
    view_id="view_id",
    object_type=AclObjectType.ORGANIZATION,
    object_id="object_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**view_id:** `ViewIdParam` — View id
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `AclObjectType` 
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `str` — The id of the object the view applies to
    
</dd>
</dl>

<dl>
<dd>

**view_type:** `typing.Optional[PatchViewViewType]` — Type of object that the view corresponds to.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the view
    
</dd>
</dl>

<dl>
<dd>

**view_data:** `typing.Optional[ViewData]` 
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[ViewOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Identifies the user who created the view
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">get_organization</a>(...) -> GetOrganizationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all organizations. The organizations are sorted by creation date, with the most recently-created organizations coming first
</dd>
</dl>
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

client.organizations.get_organization()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">get_organization_id</a>(...) -> Organization</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an organization object by its id
</dd>
</dl>
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

client.organizations.get_organization_id(
    organization_id="organization_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationIdParam` — Organization id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">patch_organization_id</a>(...) -> Organization</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update an organization object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.
</dd>
</dl>
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

client.organizations.patch_organization_id(
    organization_id="organization_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `OrganizationIdParam` — Organization id
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the organization
    
</dd>
</dl>

<dl>
<dd>

**api_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**is_universal_api:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_dataplane_private:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**proxy_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**realtime_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**image_rendering_mode:** `typing.Optional[ImageRenderingMode]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">patch_organization_members</a>(...) -> PatchOrganizationMembersOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify organization membership
</dd>
</dl>
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

client.organizations.patch_organization_members()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invite_users:** `typing.Optional[PatchOrganizationMembersInviteUsers]` — Users to invite to the organization
    
</dd>
</dl>

<dl>
<dd>

**remove_users:** `typing.Optional[PatchOrganizationMembersRemoveUsers]` — Users to remove from the organization
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[str]` — For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, or in case you want to explicitly assert the organization you are modifying, you may specify the name of the organization.
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `typing.Optional[str]` — For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, or in case you want to explicitly assert the organization you are modifying, you may specify the id of the organization.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ApiKeys
<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">get_api_key</a>(...) -> GetApiKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all api_keys. The api_keys are sorted by creation date, with the most recently-created api_keys coming first
</dd>
</dl>
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

client.api_keys.get_api_key()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**api_key_name:** `typing.Optional[ApiKeyName]` — Name of the api_key to search for
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">post_api_key</a>(...) -> CreateApiKeyOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new api_key. It is possible to have multiple API keys with the same name. There is no de-duplication
</dd>
</dl>
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

client.api_keys.post_api_key(
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

**name:** `str` — Name of the api key. Does not have to be unique
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[str]` — For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the API key belongs in.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">get_api_key_id</a>(...) -> ApiKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an api_key object by its id
</dd>
</dl>
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

client.api_keys.get_api_key_id(
    api_key_id="api_key_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key_id:** `ApiKeyIdParam` — ApiKey id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">delete_api_key_id</a>(...) -> ApiKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an api_key object by its id
</dd>
</dl>
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

client.api_keys.delete_api_key_id(
    api_key_id="api_key_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key_id:** `ApiKeyIdParam` — ApiKey id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ServiceTokens
<details><summary><code>client.service_tokens.<a href="src/fern/service_tokens/client.py">get_service_token</a>(...) -> GetServiceTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all service_tokens. The service_tokens are sorted by creation date, with the most recently-created service_tokens coming first
</dd>
</dl>
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

client.service_tokens.get_service_token()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**service_token_name:** `typing.Optional[ServiceTokenName]` — Name of the service_token to search for
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_tokens.<a href="src/fern/service_tokens/client.py">post_service_token</a>(...) -> CreateServiceTokenOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new service_token. It is possible to have multiple API keys with the same name. There is no de-duplication
</dd>
</dl>
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

client.service_tokens.post_service_token(
    name="name",
    service_account_id="service_account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of the service token. Does not have to be unique
    
</dd>
</dl>

<dl>
<dd>

**service_account_id:** `str` — The service account ID this service token should belong to. You can create a service account in the Braintrust [organization settings page](https://www.braintrustdata.com/app/settings?subroute=service-tokens) or using the [modify organization membership endpoint](https://www.braintrust.dev/docs/api-reference/organizations/modify-organization-membership)
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[str]` — For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the Service token belongs in.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_tokens.<a href="src/fern/service_tokens/client.py">put_service_token</a>(...) -> CreateServiceTokenOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace service_token. If there is an existing service_token with the same name as the one specified in the request, will replace the existing service_token with the provided fields
</dd>
</dl>
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

client.service_tokens.put_service_token(
    name="name",
    service_account_id="service_account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of the service token. Does not have to be unique
    
</dd>
</dl>

<dl>
<dd>

**service_account_id:** `str` — The service account ID this service token should belong to. You can create a service account in the Braintrust [organization settings page](https://www.braintrustdata.com/app/settings?subroute=service-tokens) or using the [modify organization membership endpoint](https://www.braintrust.dev/docs/api-reference/organizations/modify-organization-membership)
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[str]` — For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the Service token belongs in.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_tokens.<a href="src/fern/service_tokens/client.py">delete_service_token</a>(...) -> ServiceToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a single service_token
</dd>
</dl>
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

client.service_tokens.delete_service_token(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the service token.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_tokens.<a href="src/fern/service_tokens/client.py">get_service_token_id</a>(...) -> ServiceToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a service_token object by its id
</dd>
</dl>
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

client.service_tokens.get_service_token_id(
    service_token_id="service_token_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_token_id:** `ServiceTokenIdParam` — ServiceToken id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.service_tokens.<a href="src/fern/service_tokens/client.py">delete_service_token_id</a>(...) -> ServiceToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a service_token object by its id
</dd>
</dl>
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

client.service_tokens.delete_service_token_id(
    service_token_id="service_token_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_token_id:** `ServiceTokenIdParam` — ServiceToken id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AiSecrets
<details><summary><code>client.ai_secrets.<a href="src/fern/ai_secrets/client.py">get_ai_secret</a>(...) -> GetAiSecretResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all ai_secrets. The ai_secrets are sorted by creation date, with the most recently-created ai_secrets coming first
</dd>
</dl>
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

client.ai_secrets.get_ai_secret()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**ai_secret_name:** `typing.Optional[AiSecretName]` — Name of the ai_secret to search for
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**ai_secret_type:** `typing.Optional[AiSecretType]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai_secrets.<a href="src/fern/ai_secrets/client.py">post_ai_secret</a>(...) -> AiSecret</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new ai_secret. If there is an existing ai_secret with the same name as the one specified in the request, will return the existing ai_secret unmodified
</dd>
</dl>
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

client.ai_secrets.post_ai_secret(
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

**request:** `CreateAiSecret` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai_secrets.<a href="src/fern/ai_secrets/client.py">put_ai_secret</a>(...) -> AiSecret</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace ai_secret. If there is an existing ai_secret with the same name as the one specified in the request, will replace the existing ai_secret with the provided fields
</dd>
</dl>
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

client.ai_secrets.put_ai_secret(
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

**request:** `CreateAiSecret` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai_secrets.<a href="src/fern/ai_secrets/client.py">delete_ai_secret</a>(...) -> AiSecret</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a single ai_secret
</dd>
</dl>
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

client.ai_secrets.delete_ai_secret(
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

**name:** `str` — Name of the AI secret
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[str]` — For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the AI Secret belongs in.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai_secrets.<a href="src/fern/ai_secrets/client.py">get_ai_secret_id</a>(...) -> AiSecret</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an ai_secret object by its id
</dd>
</dl>
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

client.ai_secrets.get_ai_secret_id(
    ai_secret_id="ai_secret_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ai_secret_id:** `AiSecretIdParam` — AiSecret id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai_secrets.<a href="src/fern/ai_secrets/client.py">delete_ai_secret_id</a>(...) -> AiSecret</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an ai_secret object by its id
</dd>
</dl>
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

client.ai_secrets.delete_ai_secret_id(
    ai_secret_id="ai_secret_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ai_secret_id:** `AiSecretIdParam` — AiSecret id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ai_secrets.<a href="src/fern/ai_secrets/client.py">patch_ai_secret_id</a>(...) -> AiSecret</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update an ai_secret object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.
</dd>
</dl>
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

client.ai_secrets.patch_ai_secret_id(
    ai_secret_id="ai_secret_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ai_secret_id:** `AiSecretIdParam` — AiSecret id
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the AI secret
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EnvVars
<details><summary><code>client.env_vars.<a href="src/fern/env_vars/client.py">get_env_var</a>(...) -> GetEnvVarResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all env_vars. The env_vars are sorted by creation date, with the most recently-created env_vars coming first
</dd>
</dl>
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

client.env_vars.get_env_var()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**env_var_name:** `typing.Optional[EnvVarName]` — Name of the env_var to search for
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `typing.Optional[EnvVarObjectType]` — The type of the object the environment variable is scoped for
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `typing.Optional[EnvVarObjectId]` — The id of the object the environment variable is scoped for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.env_vars.<a href="src/fern/env_vars/client.py">post_env_var</a>(...) -> EnvVar</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new env_var. If there is an existing env_var with the same name as the one specified in the request, will return the existing env_var unmodified
</dd>
</dl>
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
from fern.env_vars import PostEnvVarRequestObjectType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.env_vars.post_env_var(
    object_type=PostEnvVarRequestObjectType.ORGANIZATION,
    object_id="object_id",
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

**object_type:** `PostEnvVarRequestObjectType` — The type of the object the environment variable is scoped for
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `str` — The id of the object the environment variable is scoped for
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the environment variable
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` — The value of the environment variable. Will be encrypted at rest.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Optional metadata associated with the environment variable when managed via the function secrets API
    
</dd>
</dl>

<dl>
<dd>

**secret_type:** `typing.Optional[str]` — Optional classification for the secret (for example, the AI provider name)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.env_vars.<a href="src/fern/env_vars/client.py">put_env_var</a>(...) -> EnvVar</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace env_var. If there is an existing env_var with the same name as the one specified in the request, will replace the existing env_var with the provided fields
</dd>
</dl>
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
from fern.env_vars import PutEnvVarRequestObjectType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.env_vars.put_env_var(
    object_type=PutEnvVarRequestObjectType.ORGANIZATION,
    object_id="object_id",
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

**object_type:** `PutEnvVarRequestObjectType` — The type of the object the environment variable is scoped for
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `str` — The id of the object the environment variable is scoped for
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the environment variable
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` — The value of the environment variable. Will be encrypted at rest.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Optional metadata associated with the environment variable when managed via the function secrets API
    
</dd>
</dl>

<dl>
<dd>

**secret_type:** `typing.Optional[str]` — Optional classification for the secret (for example, the AI provider name)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.env_vars.<a href="src/fern/env_vars/client.py">get_env_var_id</a>(...) -> EnvVar</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an env_var object by its id
</dd>
</dl>
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

client.env_vars.get_env_var_id(
    env_var_id="env_var_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**env_var_id:** `EnvVarIdParam` — EnvVar id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.env_vars.<a href="src/fern/env_vars/client.py">delete_env_var_id</a>(...) -> EnvVar</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an env_var object by its id
</dd>
</dl>
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

client.env_vars.delete_env_var_id(
    env_var_id="env_var_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**env_var_id:** `EnvVarIdParam` — EnvVar id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.env_vars.<a href="src/fern/env_vars/client.py">patch_env_var_id</a>(...) -> EnvVar</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update an env_var object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.
</dd>
</dl>
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

client.env_vars.patch_env_var_id(
    env_var_id="env_var_id",
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

**env_var_id:** `EnvVarIdParam` — EnvVar id
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the environment variable
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` — The value of the environment variable. Will be encrypted at rest.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Optional metadata associated with the environment variable when managed via the function secrets API
    
</dd>
</dl>

<dl>
<dd>

**secret_type:** `typing.Optional[str]` — Optional classification for the secret (for example, the AI provider name)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## McpServers
<details><summary><code>client.mcp_servers.<a href="src/fern/mcp_servers/client.py">get_mcp_server</a>(...) -> GetMcpServerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all mcp_servers. The mcp_servers are sorted by creation date, with the most recently-created mcp_servers coming first
</dd>
</dl>
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

client.mcp_servers.get_mcp_server()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**mcp_server_name:** `typing.Optional[McpServerName]` — Name of the mcp_server to search for
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mcp_servers.<a href="src/fern/mcp_servers/client.py">post_mcp_server</a>(...) -> McpServer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new mcp_server. If there is an existing mcp_server with the same name as the one specified in the request, will return the existing mcp_server unmodified
</dd>
</dl>
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

client.mcp_servers.post_mcp_server(
    project_id="project_id",
    name="name",
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateMcpServer` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mcp_servers.<a href="src/fern/mcp_servers/client.py">put_mcp_server</a>(...) -> McpServer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace mcp_server. If there is an existing mcp_server with the same name as the one specified in the request, will replace the existing mcp_server with the provided fields
</dd>
</dl>
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

client.mcp_servers.put_mcp_server(
    project_id="project_id",
    name="name",
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateMcpServer` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mcp_servers.<a href="src/fern/mcp_servers/client.py">get_mcp_server_id</a>(...) -> McpServer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a mcp_server object by its id
</dd>
</dl>
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

client.mcp_servers.get_mcp_server_id(
    mcp_server_id="mcp_server_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mcp_server_id:** `McpServerIdParam` — McpServer id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mcp_servers.<a href="src/fern/mcp_servers/client.py">delete_mcp_server_id</a>(...) -> McpServer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a mcp_server object by its id
</dd>
</dl>
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

client.mcp_servers.delete_mcp_server_id(
    mcp_server_id="mcp_server_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mcp_server_id:** `McpServerIdParam` — McpServer id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mcp_servers.<a href="src/fern/mcp_servers/client.py">patch_mcp_server_id</a>(...) -> McpServer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update a mcp_server object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.
</dd>
</dl>
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

client.mcp_servers.patch_mcp_server_id(
    mcp_server_id="mcp_server_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mcp_server_id:** `McpServerIdParam` — McpServer id
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the MCP server. Within a project, MCP server names are unique
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — URL of the MCP server endpoint
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Textual description of the MCP server
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DatasetSnapshots
<details><summary><code>client.dataset_snapshots.<a href="src/fern/dataset_snapshots/client.py">get_dataset_snapshot</a>(...) -> GetDatasetSnapshotResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all dataset_snapshots. The dataset_snapshots are sorted by creation date, with the most recently-created dataset_snapshots coming first
</dd>
</dl>
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

client.dataset_snapshots.get_dataset_snapshot()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[AppLimitParam]` — Limit the number of objects to return
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[StartingAfter]` 

Pagination cursor id.

For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[EndingBefore]` 

Pagination cursor id.

For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[Ids]` — Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times
    
</dd>
</dl>

<dl>
<dd>

**dataset_snapshot_name:** `typing.Optional[DatasetSnapshotName]` — Name of the dataset_snapshot to search for
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dataset_snapshots.<a href="src/fern/dataset_snapshots/client.py">post_dataset_snapshot</a>(...) -> DatasetSnapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new dataset_snapshot. If there is an existing dataset_snapshot with the same name as the one specified in the request, will return the existing dataset_snapshot unmodified
</dd>
</dl>
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

client.dataset_snapshots.post_dataset_snapshot(
    dataset_id="dataset_id",
    name="name",
    xact_id="xact_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateDatasetSnapshot` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dataset_snapshots.<a href="src/fern/dataset_snapshots/client.py">put_dataset_snapshot</a>(...) -> DatasetSnapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace dataset_snapshot. If there is an existing dataset_snapshot with the same name as the one specified in the request, will replace the existing dataset_snapshot with the provided fields
</dd>
</dl>
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

client.dataset_snapshots.put_dataset_snapshot(
    dataset_id="dataset_id",
    name="name",
    xact_id="xact_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateDatasetSnapshot` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dataset_snapshots.<a href="src/fern/dataset_snapshots/client.py">get_dataset_snapshot_id</a>(...) -> DatasetSnapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a dataset_snapshot object by its id
</dd>
</dl>
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

client.dataset_snapshots.get_dataset_snapshot_id(
    dataset_snapshot_id="dataset_snapshot_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_snapshot_id:** `DatasetSnapshotIdParam` — DatasetSnapshot id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dataset_snapshots.<a href="src/fern/dataset_snapshots/client.py">delete_dataset_snapshot_id</a>(...) -> DatasetSnapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a dataset_snapshot object by its id
</dd>
</dl>
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

client.dataset_snapshots.delete_dataset_snapshot_id(
    dataset_snapshot_id="dataset_snapshot_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_snapshot_id:** `DatasetSnapshotIdParam` — DatasetSnapshot id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dataset_snapshots.<a href="src/fern/dataset_snapshots/client.py">patch_dataset_snapshot_id</a>(...) -> DatasetSnapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update a dataset_snapshot object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.
</dd>
</dl>
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

client.dataset_snapshots.patch_dataset_snapshot_id(
    dataset_snapshot_id="dataset_snapshot_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_snapshot_id:** `DatasetSnapshotIdParam` — DatasetSnapshot id
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the dataset snapshot
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Textual description of the dataset snapshot
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.environments.<a href="src/fern/environments/client.py">list_environments</a>(...) -> ListEnvironmentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List out all environments. The environments are sorted by creation date, with the most recently-created environments first.
</dd>
</dl>
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

client.environments.list_environments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[OrgName]` — Filter search results to within a particular organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">create_environment</a>(...) -> Environment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new environment
</dd>
</dl>
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

client.environments.create_environment(
    name="name",
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

**name:** `str` — Name of the environment
    
</dd>
</dl>

<dl>
<dd>

**slug:** `str` — A url-friendly, unique identifier for the environment within an organization
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Textual description of the environment
    
</dd>
</dl>

<dl>
<dd>

**org_name:** `typing.Optional[str]` — For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the environment belongs in.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">get_environment</a>(...) -> Environment</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.environments.get_environment(
    environment_id="environment_id",
)

```
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

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">delete_environment</a>(...) -> Environment</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.environments.delete_environment(
    environment_id="environment_id",
)

```
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

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">update_environment</a>(...) -> Environment</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.environments.update_environment(
    environment_id="environment_id",
)

```
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

**name:** `typing.Optional[str]` — Name of the environment
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` — A url-friendly, unique identifier for the environment within an organization
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Textual description of the environment
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Other
<details><summary><code>client.other.<a href="src/fern/other/client.py">get_index</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Default endpoint. Simply replies with 'Hello, World!'. Authorization is not required
</dd>
</dl>
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

client.other.get_index()

```
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

## CrossObject
<details><summary><code>client.cross_object.<a href="src/fern/cross_object/client.py">post_cross_object_insert</a>(...) -> CrossObjectInsertResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Insert events and feedback across object types
</dd>
</dl>
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

client.cross_object.post_cross_object_insert()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**experiment:** `typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestExperimentValue]]]` — A mapping from experiment id to a set of log events and feedback items to insert
    
</dd>
</dl>

<dl>
<dd>

**dataset:** `typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestDatasetValue]]]` — A mapping from dataset id to a set of log events and feedback items to insert
    
</dd>
</dl>

<dl>
<dd>

**project_logs:** `typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestProjectLogsValue]]]` — A mapping from project id to a set of log events and feedback items to insert
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Proxy
<details><summary><code>client.proxy.<a href="src/fern/proxy/client.py">proxychat_completions</a>(...) -> typing.Optional[typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Proxy a chat/completions request to the specified model, converting its format as needed. Will cache if temperature=0 or seed is set.
</dd>
</dl>
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

client.proxy.proxychat_completions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.proxy.<a href="src/fern/proxy/client.py">proxycompletions</a>(...) -> typing.Optional[typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Proxy a completions request to the specified model, converting its format as needed. Will cache if temperature=0 or seed is set.
</dd>
</dl>
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

client.proxy.proxycompletions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.proxy.<a href="src/fern/proxy/client.py">proxyauto</a>(...) -> typing.Optional[typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Proxy a request to either chat/completions or completions automatically based on the model. Will cache if temperature=0 or seed is set.
</dd>
</dl>
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

client.proxy.proxyauto()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.proxy.<a href="src/fern/proxy/client.py">proxyembeddings</a>(...) -> typing.Optional[typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Proxy an embeddings request to the specified model, converting its format as needed. Will cache automatically.
</dd>
</dl>
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

client.proxy.proxyembeddings()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.proxy.<a href="src/fern/proxy/client.py">proxycredentials</a>(...) -> ProxycredentialsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a temporary credential which can access the proxy for a limited time. The temporary credential will be allowed to make requests on behalf of the Braintrust API key (or model provider API key) provided in the `Authorization` header. See [docs](/docs/deploy/ai-proxy#create-temporary-credentials) for code examples.
</dd>
</dl>
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

client.proxy.proxycredentials()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model:** `typing.Optional[str]` — Granted model name. Null/undefined to grant usage of all models.
    
</dd>
</dl>

<dl>
<dd>

**ttl_seconds:** `typing.Optional[float]` — TTL of the temporary credential. 10 minutes by default.
    
</dd>
</dl>

<dl>
<dd>

**logging:** `typing.Optional[ProxycredentialsRequestLogging]` — If present, proxy will log requests to the given Braintrust project name.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.proxy.<a href="src/fern/proxy/client.py">path</a>(...) -> typing.Optional[typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Any requests which do not match the above paths will be proxied directly to the OpenAI API.
</dd>
</dl>
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

client.proxy.path()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**path:** `typing.List[str]` — The path to proxy
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Evals
<details><summary><code>client.evals.<a href="src/fern/evals/client.py">eval_launch</a>(...) -> SummarizeExperimentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Launch an evaluation. This is the API-equivalent of the `Eval` function that is built into the Braintrust SDK. In the Eval API, you provide pointers to a dataset, task function, and scoring functions. The API will then run the evaluation, create an experiment, and return the results along with a link to the experiment. To learn more about evals, see the [Evals guide](https://www.braintrust.dev/docs/evaluate).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, FunctionIdFunctionId
from fern.environment import FernApiEnvironment
from fern.evals import RunEvalDataDatasetId, RunEvalScoresItemFunctionId

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.evals.eval_launch(
    project_id="project_id",
    data=RunEvalDataDatasetId(
        dataset_id="dataset_id",
    ),
    task=FunctionIdFunctionId(
        function_id="function_id",
    ),
    scores=[
        RunEvalScoresItemFunctionId(
            function_id="function_id",
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

**project_id:** `str` — Unique identifier for the project to run the eval in
    
</dd>
</dl>

<dl>
<dd>

**data:** `RunEvalData` — The dataset to use
    
</dd>
</dl>

<dl>
<dd>

**task:** `FunctionId` 
    
</dd>
</dl>

<dl>
<dd>

**scores:** `typing.List[RunEvalScoresItem]` — The functions to score the eval on
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the eval to run when multiple evals available
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.Dict[str, typing.Any]]` — Values for any parameters used in the eval
    
</dd>
</dl>

<dl>
<dd>

**experiment_name:** `typing.Optional[str]` — An optional name for the experiment created by this eval. If it conflicts with an existing experiment, it will be suffixed with a unique identifier.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Optional experiment-level metadata to store about the evaluation. You can later use this to slice & dice across experiments.
    
</dd>
</dl>

<dl>
<dd>

**parent:** `typing.Optional[RunEvalParent]` — Options for tracing the evaluation
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Optional[bool]` — Whether to stream the results of the eval. If true, the request will return two events: one to indicate the experiment has started, and another upon completion. If false, the request will return the evaluation's summary upon completion.
    
</dd>
</dl>

<dl>
<dd>

**trial_count:** `typing.Optional[float]` — The number of times to run the evaluator per input. This is useful for evaluating applications that have non-deterministic behavior and gives you both a stronger aggregate measure and a sense of the variance in the results.
    
</dd>
</dl>

<dl>
<dd>

**is_public:** `typing.Optional[bool]` — Whether the experiment should be public. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[float]` — The maximum duration, in milliseconds, to run the evaluation. Defaults to undefined, in which case there is no timeout.
    
</dd>
</dl>

<dl>
<dd>

**max_concurrency:** `typing.Optional[float]` — The maximum number of tasks/scorers that will be run concurrently. Defaults to 10. If null is provided, no max concurrency will be used.
    
</dd>
</dl>

<dl>
<dd>

**base_experiment_name:** `typing.Optional[str]` — An optional experiment name to use as a base. If specified, the new experiment will be summarized and compared to this experiment.
    
</dd>
</dl>

<dl>
<dd>

**base_experiment_id:** `typing.Optional[str]` — An optional experiment id to use as a base. If specified, the new experiment will be summarized and compared to this experiment.
    
</dd>
</dl>

<dl>
<dd>

**git_metadata_settings:** `typing.Optional[GitMetadataSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**repo_info:** `typing.Optional[RunEvalRepoInfo]` — Optionally explicitly specify the git metadata for this experiment. This takes precedence over `gitMetadataSettings` if specified.
    
</dd>
</dl>

<dl>
<dd>

**strict:** `typing.Optional[bool]` — If true, throw an error if one of the variables in the prompt is not present in the input
    
</dd>
</dl>

<dl>
<dd>

**stop_token:** `typing.Optional[str]` — The token to stop the run
    
</dd>
</dl>

<dl>
<dd>

**extra_messages:** `typing.Optional[str]` — A template path of extra messages to append to the conversion. These messages will be appended to the end of the conversation, after the last message.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — Optional tags that will be added to the experiment.
    
</dd>
</dl>

<dl>
<dd>

**mcp_auth:** `typing.Optional[typing.Dict[str, RunEvalMcpAuthValue]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

