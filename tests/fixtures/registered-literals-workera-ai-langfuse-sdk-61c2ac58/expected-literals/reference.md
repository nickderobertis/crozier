# Reference
## Annotationqueues
<details><summary><code>client.annotationqueues.<a href="src/fern/annotationqueues/client.py">listqueues</a>(...) -> PaginatedAnnotationQueues</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all annotation queues
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.annotationqueues.listqueues()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — page number, starts at 1
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — limit of items per page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.annotationqueues.<a href="src/fern/annotationqueues/client.py">getqueue</a>(...) -> AnnotationQueue</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an annotation queue by ID
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.annotationqueues.getqueue(
    queue_id="queueId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**queue_id:** `str` — The unique identifier of the annotation queue
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.annotationqueues.<a href="src/fern/annotationqueues/client.py">listqueueitems</a>(...) -> PaginatedAnnotationQueueItems</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get items for a specific annotation queue
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.annotationqueues.listqueueitems(
    queue_id="queueId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**queue_id:** `str` — The unique identifier of the annotation queue
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[AnnotationQueueStatus]` — Filter by status
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — page number, starts at 1
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — limit of items per page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.annotationqueues.<a href="src/fern/annotationqueues/client.py">createqueueitem</a>(...) -> AnnotationQueueItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add an item to an annotation queue
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.annotationqueues.createqueueitem(
    queue_id="queueId",
    object_id="objectId",
    object_type="TRACE",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**queue_id:** `str` — The unique identifier of the annotation queue
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `AnnotationQueueObjectType` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[AnnotationQueueStatus]` — Defaults to PENDING for new queue items
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.annotationqueues.<a href="src/fern/annotationqueues/client.py">getqueueitem</a>(...) -> AnnotationQueueItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific item from an annotation queue
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.annotationqueues.getqueueitem(
    queue_id="queueId",
    item_id="itemId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**queue_id:** `str` — The unique identifier of the annotation queue
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `str` — The unique identifier of the annotation queue item
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.annotationqueues.<a href="src/fern/annotationqueues/client.py">deletequeueitem</a>(...) -> DeleteAnnotationQueueItemResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove an item from an annotation queue
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.annotationqueues.deletequeueitem(
    queue_id="queueId",
    item_id="itemId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**queue_id:** `str` — The unique identifier of the annotation queue
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `str` — The unique identifier of the annotation queue item
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.annotationqueues.<a href="src/fern/annotationqueues/client.py">updatequeueitem</a>(...) -> AnnotationQueueItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an annotation queue item
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.annotationqueues.updatequeueitem(
    queue_id="queueId",
    item_id="itemId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**queue_id:** `str` — The unique identifier of the annotation queue
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `str` — The unique identifier of the annotation queue item
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[AnnotationQueueStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Comments
<details><summary><code>client.comments.<a href="src/fern/comments/client.py">get</a>(...) -> GetCommentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all comments
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.comments.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number, starts at 1.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit of items per page. If you encounter api issues due to too large page sizes, try to reduce the limit
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `typing.Optional[str]` — Filter comments by object type (trace, observation, session, prompt).
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `typing.Optional[str]` — Filter comments by object id. If objectType is not provided, an error will be thrown.
    
</dd>
</dl>

<dl>
<dd>

**author_user_id:** `typing.Optional[str]` — Filter comments by author user id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.comments.<a href="src/fern/comments/client.py">create</a>(...) -> CreateCommentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a comment. Comments may be attached to different object types (trace, observation, session, prompt).
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.comments.create(
    project_id="projectId",
    object_type="objectType",
    object_id="objectId",
    content="content",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` — The id of the project to attach the comment to.
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `str` — The type of the object to attach the comment to (trace, observation, session, prompt).
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `str` — The id of the object to attach the comment to. If this does not reference a valid existing object, an error will be thrown.
    
</dd>
</dl>

<dl>
<dd>

**content:** `str` — The content of the comment. May include markdown. Currently limited to 3000 characters.
    
</dd>
</dl>

<dl>
<dd>

**author_user_id:** `typing.Optional[str]` — The id of the user who created the comment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.comments.<a href="src/fern/comments/client.py">get_by_id</a>(...) -> Comment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a comment by id
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.comments.get_by_id(
    comment_id="commentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**comment_id:** `str` — The unique langfuse identifier of a comment
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Datasetitems
<details><summary><code>client.datasetitems.<a href="src/fern/datasetitems/client.py">list</a>(...) -> PaginatedDatasetItems</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get dataset items
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.datasetitems.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**source_trace_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**source_observation_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — page number, starts at 1
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — limit of items per page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasetitems.<a href="src/fern/datasetitems/client.py">create</a>(...) -> DatasetItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a dataset item
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.datasetitems.create(
    dataset_name="datasetName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**expected_output:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**source_trace_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**source_observation_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Dataset items are upserted on their id. Id needs to be unique (project-level) and cannot be reused across datasets.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[DatasetStatus]` — Defaults to ACTIVE for newly created items
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasetitems.<a href="src/fern/datasetitems/client.py">get</a>(...) -> DatasetItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a dataset item
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.datasetitems.get(
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

<details><summary><code>client.datasetitems.<a href="src/fern/datasetitems/client.py">delete</a>(...) -> DeleteDatasetItemResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a dataset item and all its run items. This action is irreversible.
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.datasetitems.delete(
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

## Datasetrunitems
<details><summary><code>client.datasetrunitems.<a href="src/fern/datasetrunitems/client.py">create</a>(...) -> DatasetRunItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a dataset run item
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.datasetrunitems.create(
    run_name="runName",
    dataset_item_id="datasetItemId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**dataset_item_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**run_description:** `typing.Optional[str]` — Description of the run. If run exists, description will be updated.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Any]` — Metadata of the dataset run, updates run if run already exists
    
</dd>
</dl>

<dl>
<dd>

**observation_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**trace_id:** `typing.Optional[str]` — traceId should always be provided. For compatibility with older SDK versions it can also be inferred from the provided observationId.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">list</a>(...) -> PaginatedDatasets</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all datasets
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.datasets.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — page number, starts at 1
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — limit of items per page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">create</a>(...) -> Dataset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a dataset
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.datasets.create(
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

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">get</a>(...) -> Dataset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a dataset
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.datasets.get(
    dataset_name="datasetName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">getrun</a>(...) -> DatasetRunWithItems</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a dataset run and its items
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.datasets.getrun(
    dataset_name="datasetName",
    run_name="runName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**run_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">deleterun</a>(...) -> DeleteDatasetRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a dataset run and all its run items. This action is irreversible.
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.datasets.deleterun(
    dataset_name="datasetName",
    run_name="runName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**run_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.datasets.<a href="src/fern/datasets/client.py">getruns</a>(...) -> PaginatedDatasetRuns</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get dataset runs
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.datasets.getruns(
    dataset_name="datasetName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — page number, starts at 1
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — limit of items per page
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.health.<a href="src/fern/health/client.py">health</a>() -> HealthResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check health of API and database
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.health.health()

```
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

## Ingestion
<details><summary><code>client.ingestion.<a href="src/fern/ingestion/client.py">batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Batched ingestion for Langfuse Tracing.
If you want to use tracing via the API, such as to build your own Langfuse client implementation, this is the only API route you need to implement.

Within each batch, there can be multiple events.
Each event has a type, an id, a timestamp, metadata and a body.
Internally, we refer to this as the "event envelope" as it tells us something about the event but not the trace.
We use the event id within this envelope to deduplicate messages to avoid processing the same event twice, i.e. the event id should be unique per request.
The event.body.id is the ID of the actual trace and will be used for updates and will be visible within the Langfuse App.
I.e. if you want to update a trace, you'd use the same body id, but separate event IDs.

Notes:
- Introduction to data model: https://langfuse.com/docs/tracing-data-model
- Batch sizes are limited to 3.5 MB in total. You need to adjust the number of events per batch accordingly.
- The API does not return a 4xx status code for input errors. Instead, it responds with a 207 status code, which includes a list of the encountered errors.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, IngestionEventZero, TraceBody
import datetime

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.ingestion.batch(
    batch=[
        IngestionEventZero(
            body=TraceBody(
                id="abcdef-1234-5678-90ab",
                timestamp=datetime.datetime.fromisoformat("2022-01-01T00:00:00+00:00"),
                name="My Trace",
                user_id="1234-5678-90ab-cdef",
                input="My input",
                output="My output",
                session_id="1234-5678-90ab-cdef",
                release="1.0.0",
                version="1.0.0",
                metadata="My metadata",
                tags=[
                    "tag1",
                    "tag2"
                ],
                environment="production",
                public=True,
            ),
            id="abcdef-1234-5678-90ab",
            timestamp="2022-01-01T00:00:00.000Z",
            type="trace-create",
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

**batch:** `typing.List[IngestionEvent]` — Batch of tracing events to be ingested. Discriminated by attribute `type`.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Any]` — Optional. Metadata field used by the Langfuse SDKs for debugging.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Media
<details><summary><code>client.media.<a href="src/fern/media/client.py">get</a>(...) -> GetMediaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a media record
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.media.get(
    media_id="mediaId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**media_id:** `str` — The unique langfuse identifier of a media record
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.media.<a href="src/fern/media/client.py">patch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patch a media record
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
import datetime

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.media.patch(
    media_id="mediaId",
    uploaded_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    upload_http_status=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**media_id:** `str` — The unique langfuse identifier of a media record
    
</dd>
</dl>

<dl>
<dd>

**uploaded_at:** `datetime.datetime` — The date and time when the media record was uploaded
    
</dd>
</dl>

<dl>
<dd>

**upload_http_status:** `int` — The HTTP status code of the upload
    
</dd>
</dl>

<dl>
<dd>

**upload_http_error:** `typing.Optional[str]` — The HTTP error message of the upload
    
</dd>
</dl>

<dl>
<dd>

**upload_time_ms:** `typing.Optional[int]` — The time in milliseconds it took to upload the media record
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.media.<a href="src/fern/media/client.py">getuploadurl</a>(...) -> GetMediaUploadUrlResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a presigned upload URL for a media record
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.media.getuploadurl(
    trace_id="traceId",
    content_type="image/png",
    content_length=1,
    sha256hash="sha256Hash",
    field="field",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trace_id:** `str` — The trace ID associated with the media record
    
</dd>
</dl>

<dl>
<dd>

**content_type:** `MediaContentType` 
    
</dd>
</dl>

<dl>
<dd>

**content_length:** `int` — The size of the media record in bytes
    
</dd>
</dl>

<dl>
<dd>

**sha256hash:** `str` — The SHA-256 hash of the media record
    
</dd>
</dl>

<dl>
<dd>

**field:** `str` — The trace / observation field the media record is associated with. This can be one of `input`, `output`, `metadata`
    
</dd>
</dl>

<dl>
<dd>

**observation_id:** `typing.Optional[str]` — The observation ID associated with the media record. If the media record is associated directly with a trace, this will be null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Metrics
<details><summary><code>client.metrics.<a href="src/fern/metrics/client.py">daily</a>(...) -> DailyMetrics</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get daily metrics of the Langfuse project
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.metrics.daily()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — page number, starts at 1
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — limit of items per page
    
</dd>
</dl>

<dl>
<dd>

**trace_name:** `typing.Optional[str]` — Optional filter by the name of the trace
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Optional filter by the userId associated with the trace
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` — Optional filter for metrics where traces include all of these tags
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` — Optional filter for metrics where events include any of these environments
    
</dd>
</dl>

<dl>
<dd>

**from_timestamp:** `typing.Optional[datetime.datetime]` — Optional filter to only include traces and observations on or after a certain datetime (ISO 8601)
    
</dd>
</dl>

<dl>
<dd>

**to_timestamp:** `typing.Optional[datetime.datetime]` — Optional filter to only include traces and observations before a certain datetime (ISO 8601)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Models
<details><summary><code>client.models.<a href="src/fern/models/client.py">list</a>(...) -> PaginatedModels</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all models
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.models.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — page number, starts at 1
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — limit of items per page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/fern/models/client.py">create</a>(...) -> Model</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a model
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.models.create(
    model_name="modelName",
    match_pattern="matchPattern",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model_name:** `str` — Name of the model definition. If multiple with the same name exist, they are applied in the following order: (1) custom over built-in, (2) newest according to startTime where model.startTime<observation.startTime
    
</dd>
</dl>

<dl>
<dd>

**match_pattern:** `str` — Regex pattern which matches this model definition to generation.model. Useful in case of fine-tuned models. If you want to exact match, use `(?i)^modelname$`
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — Apply only to generations which are newer than this ISO date.
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[ModelUsageUnit]` — Unit used by this model.
    
</dd>
</dl>

<dl>
<dd>

**input_price:** `typing.Optional[float]` — Price (USD) per input unit
    
</dd>
</dl>

<dl>
<dd>

**output_price:** `typing.Optional[float]` — Price (USD) per output unit
    
</dd>
</dl>

<dl>
<dd>

**total_price:** `typing.Optional[float]` — Price (USD) per total units. Cannot be set if input or output price is set.
    
</dd>
</dl>

<dl>
<dd>

**tokenizer_id:** `typing.Optional[str]` — Optional. Tokenizer to be applied to observations which match to this model. See docs for more details.
    
</dd>
</dl>

<dl>
<dd>

**tokenizer_config:** `typing.Optional[typing.Any]` — Optional. Configuration for the selected tokenizer. Needs to be JSON. See docs for more details.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/fern/models/client.py">get</a>(...) -> Model</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a model
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.models.get(
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

<details><summary><code>client.models.<a href="src/fern/models/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a model. Cannot delete models managed by Langfuse. You can create your own definition with the same modelName to override the definition though.
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.models.delete(
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

## Observations
<details><summary><code>client.observations.<a href="src/fern/observations/client.py">get</a>(...) -> ObservationsView</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a observation
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.observations.get(
    observation_id="observationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**observation_id:** `str` — The unique langfuse identifier of an observation, can be an event, span or generation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.observations.<a href="src/fern/observations/client.py">getmany</a>(...) -> ObservationsViews</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of observations
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.observations.getmany()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number, starts at 1.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit of items per page. If you encounter api issues due to too large page sizes, try to reduce the limit.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**trace_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_observation_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` — Optional filter for observations where the environment is one of the provided values.
    
</dd>
</dl>

<dl>
<dd>

**from_start_time:** `typing.Optional[datetime.datetime]` — Retrieve only observations with a start_time or or after this datetime (ISO 8601).
    
</dd>
</dl>

<dl>
<dd>

**to_start_time:** `typing.Optional[datetime.datetime]` — Retrieve only observations with a start_time before this datetime (ISO 8601).
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Optional filter to only include observations with a certain version.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.projects.<a href="src/fern/projects/client.py">get</a>() -> Projects</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Project associated with API key
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.projects.get()

```
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

## Promptversion
<details><summary><code>client.promptversion.<a href="src/fern/promptversion/client.py">update</a>(...) -> Prompt</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update labels for a specific prompt version
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.promptversion.update(
    name="name",
    version=1,
    new_labels=[
        "newLabels"
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

**name:** `str` — The name of the prompt
    
</dd>
</dl>

<dl>
<dd>

**version:** `int` — Version of the prompt to update
    
</dd>
</dl>

<dl>
<dd>

**new_labels:** `typing.List[str]` — New labels for the prompt version. Labels are unique across versions. The "latest" label is reserved and managed by Langfuse.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.prompts.<a href="src/fern/prompts/client.py">get</a>(...) -> Prompt</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a prompt
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.prompts.get(
    prompt_name="promptName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt_name:** `str` — The name of the prompt
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` — Version of the prompt to be retrieved.
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — Label of the prompt to be retrieved. Defaults to "production" if no label or version is set.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompts.<a href="src/fern/prompts/client.py">list</a>(...) -> PromptMetaListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of prompt names with versions and labels
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.prompts.list()

```
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

**label:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — page number, starts at 1
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — limit of items per page
    
</dd>
</dl>

<dl>
<dd>

**from_updated_at:** `typing.Optional[datetime.datetime]` — Optional filter to only include prompt versions created/updated on or after a certain datetime (ISO 8601)
    
</dd>
</dl>

<dl>
<dd>

**to_updated_at:** `typing.Optional[datetime.datetime]` — Optional filter to only include prompt versions created/updated before a certain datetime (ISO 8601)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.prompts.<a href="src/fern/prompts/client.py">create</a>(...) -> Prompt</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new version for the prompt with the given `name`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, CreatePromptRequestZero, ChatMessage

client = FernApi(
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.prompts.create(
    request=CreatePromptRequestZero(
        name="name",
        prompt=[
            ChatMessage(
                role="role",
                content="content",
            )
        ],
        type="chat",
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

**request:** `CreatePromptRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Scoreconfigs
<details><summary><code>client.scoreconfigs.<a href="src/fern/scoreconfigs/client.py">get</a>(...) -> ScoreConfigs</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all score configs
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.scoreconfigs.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number, starts at 1.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit of items per page. If you encounter api issues due to too large page sizes, try to reduce the limit
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scoreconfigs.<a href="src/fern/scoreconfigs/client.py">create</a>(...) -> ScoreConfig</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a score configuration (config). Score configs are used to define the structure of scores
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.scoreconfigs.create(
    name="name",
    data_type="NUMERIC",
)

```
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

**data_type:** `ScoreDataType` 
    
</dd>
</dl>

<dl>
<dd>

**categories:** `typing.Optional[typing.List[ConfigCategory]]` — Configure custom categories for categorical scores. Pass a list of objects with `label` and `value` properties. Categories are autogenerated for boolean configs and cannot be passed
    
</dd>
</dl>

<dl>
<dd>

**min_value:** `typing.Optional[float]` — Configure a minimum value for numerical scores. If not set, the minimum value defaults to -∞
    
</dd>
</dl>

<dl>
<dd>

**max_value:** `typing.Optional[float]` — Configure a maximum value for numerical scores. If not set, the maximum value defaults to +∞
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description is shown across the Langfuse UI and can be used to e.g. explain the config categories in detail, why a numeric range was set, or provide additional context on config name or usage
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scoreconfigs.<a href="src/fern/scoreconfigs/client.py">get_by_id</a>(...) -> ScoreConfig</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a score config
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.scoreconfigs.get_by_id(
    config_id="configId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**config_id:** `str` — The unique langfuse identifier of a score config
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Score
<details><summary><code>client.score.<a href="src/fern/score/client.py">get</a>(...) -> GetScoresResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of scores
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.score.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number, starts at 1.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit of items per page. If you encounter api issues due to too large page sizes, try to reduce the limit.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Retrieve only scores with this userId associated to the trace.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Retrieve only scores with this name.
    
</dd>
</dl>

<dl>
<dd>

**from_timestamp:** `typing.Optional[datetime.datetime]` — Optional filter to only include scores created on or after a certain datetime (ISO 8601)
    
</dd>
</dl>

<dl>
<dd>

**to_timestamp:** `typing.Optional[datetime.datetime]` — Optional filter to only include scores created before a certain datetime (ISO 8601)
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` — Optional filter for scores where the environment is one of the provided values.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[ScoreSource]` — Retrieve only scores from a specific source.
    
</dd>
</dl>

<dl>
<dd>

**operator:** `typing.Optional[str]` — Retrieve only scores with <operator> value.
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[float]` — Retrieve only scores with <operator> value.
    
</dd>
</dl>

<dl>
<dd>

**score_ids:** `typing.Optional[str]` — Comma-separated list of score IDs to limit the results to.
    
</dd>
</dl>

<dl>
<dd>

**config_id:** `typing.Optional[str]` — Retrieve only scores with a specific configId.
    
</dd>
</dl>

<dl>
<dd>

**queue_id:** `typing.Optional[str]` — Retrieve only scores with a specific annotation queueId.
    
</dd>
</dl>

<dl>
<dd>

**data_type:** `typing.Optional[ScoreDataType]` — Retrieve only scores with a specific dataType.
    
</dd>
</dl>

<dl>
<dd>

**trace_tags:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` — Only scores linked to traces that include all of these tags will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.score.<a href="src/fern/score/client.py">create</a>(...) -> CreateScoreResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a score
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.score.create(
    trace_id="cdef-1234-5678-90ab",
    name="novelty",
    value=1.1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trace_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `CreateScoreValue` — The value of the score. Must be passed as string for categorical scores, and numeric for boolean and numeric scores. Boolean score values must equal either 1 or 0 (true or false)
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**observation_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[str]` — The environment of the score. Can be any lowercase alphanumeric string with hyphens and underscores that does not start with 'langfuse'.
    
</dd>
</dl>

<dl>
<dd>

**data_type:** `typing.Optional[ScoreDataType]` — The data type of the score. When passing a configId this field is inferred. Otherwise, this field must be passed or will default to numeric.
    
</dd>
</dl>

<dl>
<dd>

**config_id:** `typing.Optional[str]` — Reference a score config on a score. The unique langfuse identifier of a score config. When passing this field, the dataType and stringValue fields are automatically populated.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.score.<a href="src/fern/score/client.py">get_by_id</a>(...) -> Score</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a score
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.score.get_by_id(
    score_id="scoreId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**score_id:** `str` — The unique langfuse identifier of a score
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.score.<a href="src/fern/score/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a score
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.score.delete(
    score_id="scoreId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**score_id:** `str` — The unique langfuse identifier of a score
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sessions
<details><summary><code>client.sessions.<a href="src/fern/sessions/client.py">list</a>(...) -> PaginatedSessions</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get sessions
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.sessions.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number, starts at 1
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit of items per page. If you encounter api issues due to too large page sizes, try to reduce the limit.
    
</dd>
</dl>

<dl>
<dd>

**from_timestamp:** `typing.Optional[datetime.datetime]` — Optional filter to only include sessions created on or after a certain datetime (ISO 8601)
    
</dd>
</dl>

<dl>
<dd>

**to_timestamp:** `typing.Optional[datetime.datetime]` — Optional filter to only include sessions created before a certain datetime (ISO 8601)
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` — Optional filter for sessions where the environment is one of the provided values.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sessions.<a href="src/fern/sessions/client.py">get</a>(...) -> SessionWithTraces</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a session. Please note that `traces` on this endpoint are not paginated, if you plan to fetch large sessions, consider `GET /api/public/traces?sessionId=<sessionId>`
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.sessions.get(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The unique id of a session
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Trace
<details><summary><code>client.trace.<a href="src/fern/trace/client.py">get</a>(...) -> TraceWithFullDetails</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific trace
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.trace.get(
    trace_id="traceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trace_id:** `str` — The unique langfuse identifier of a trace
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trace.<a href="src/fern/trace/client.py">delete</a>(...) -> DeleteTraceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific trace
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.trace.delete(
    trace_id="traceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trace_id:** `str` — The unique langfuse identifier of the trace to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trace.<a href="src/fern/trace/client.py">list</a>(...) -> Traces</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get list of traces
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.trace.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number, starts at 1
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit of items per page. If you encounter api issues due to too large page sizes, try to reduce the limit.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**from_timestamp:** `typing.Optional[datetime.datetime]` — Optional filter to only include traces with a trace.timestamp on or after a certain datetime (ISO 8601)
    
</dd>
</dl>

<dl>
<dd>

**to_timestamp:** `typing.Optional[datetime.datetime]` — Optional filter to only include traces with a trace.timestamp before a certain datetime (ISO 8601)
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Format of the string [field].[asc/desc]. Fields: id, timestamp, name, userId, release, version, public, bookmarked, sessionId. Example: timestamp.asc
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` — Only traces that include all of these tags will be returned.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Optional filter to only include traces with a certain version.
    
</dd>
</dl>

<dl>
<dd>

**release:** `typing.Optional[str]` — Optional filter to only include traces with a certain release.
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` — Optional filter for traces where the environment is one of the provided values.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trace.<a href="src/fern/trace/client.py">deletemultiple</a>(...) -> DeleteTraceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete multiple traces
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.trace.deletemultiple(
    trace_ids=[
        "traceIds"
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

**trace_ids:** `typing.List[str]` — List of trace IDs to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

