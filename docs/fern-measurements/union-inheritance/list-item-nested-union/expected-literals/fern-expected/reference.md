# Reference
<details><summary><code>client.<a href="src/fern/client.py#L111-L148">patch_shelf_entries</a>(...)</code></summary>
<dl>
<dd>

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

client.patch_shelf_entries(
    shelf_id="shelfId",
    entries=[],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**shelf_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**entries:** `typing.List[PatchShelfEntriesRequestEntriesItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py#L150-L187">patch_shelf_tags</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PatchShelfTagsRequestTagsItemPayload
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.patch_shelf_tags(
    shelf_id="shelfId",
    tags=[
        PatchShelfTagsRequestTagsItemPayload(
            label="label",
            operation="create",
            payload=None,
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

**shelf_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.List[PatchShelfTagsRequestTagsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py#L189-L225">patch_shelf_notes</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PatchShelfNotesRequestNotesItem
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.patch_shelf_notes(
    shelf_id="shelfId",
    notes=[
        PatchShelfNotesRequestNotesItem(
            label="label",
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

**shelf_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.List[PatchShelfNotesRequestNotesItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

