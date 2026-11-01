# Reference
<details><summary><code>client.<a href="src/fern/client.py">list_passages</a>(...) -> typing.List[Passage]</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.list_passages(
    lock_id="lockId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**lock_id:** `str` 


        The lock to read, by its painted number.
        (ex. /L7)
        
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[str]` — 
Upstream or downstream.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Plain description without a leading break.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">book_passage</a>(...) -> Passage</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.book_passage(
    lock_id="lockId",
    boat_name="boatName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**lock_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**boat_name:** `str` 


        The boat's registered name.
        
    
</dd>
</dl>

<dl>
<dd>

**draught:** `typing.Optional[float]` — 
Depth below the waterline, in metres.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

