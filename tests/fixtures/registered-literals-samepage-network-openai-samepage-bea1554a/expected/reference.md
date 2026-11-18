# Reference
<details><summary><code>client.<a href="src/fern/client.py#L112-L132">notebooks</a>() -> NotebooksGetResponse</code></summary>
<dl>
<dd>

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

client.notebooks()

```
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

<details><summary><code>client.<a href="src/fern/client.py#L134-L167">page</a>(...) -> PagePostResponse</code></summary>
<dl>
<dd>

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

client.page(
    notebook_uuid="notebookUuid",
    notebook_page_id="notebookPageId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**notebook_uuid:** `str` — The application to request. Must be in UUID format.
    
</dd>
</dl>

<dl>
<dd>

**notebook_page_id:** `str` — The page from the application to request
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py#L169-L226">query</a>(...) -> QueryPostResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, QueryRequestConditionsItem
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.query(
    targets=[
        "targets"
    ],
    conditions=[
        QueryRequestConditionsItem(
            source="source",
            target="target",
            relation="relation",
        )
    ],
    return_node="returnNode",
    label="label",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**targets:** `typing.List[str]` — The notebook ids this query should target.
    
</dd>
</dl>

<dl>
<dd>

**conditions:** `typing.List[QueryRequestConditionsItem]` — The conditions that muse be met to satisfy the query
    
</dd>
</dl>

<dl>
<dd>

**return_node:** `str` — The node acting as the source of the entire query
    
</dd>
</dl>

<dl>
<dd>

**label:** `str` — The human-readable label to assign to this query
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

