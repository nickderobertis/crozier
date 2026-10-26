# Reference
<details><summary><code>client.<a href="src/fern/client.py">get_shelf</a>(...) -> Shelf</code></summary>
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

client.get_shelf(
    branch_path_param="branch",
    shelf_path_param="shelf",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**branch_path_param:** `str` — The branch the shelf stands in.
    
</dd>
</dl>

<dl>
<dd>

**shelf_path_param:** `str` — The shelf's code.
    
</dd>
</dl>

<dl>
<dd>

**shelf:** `typing.Optional[str]` — The shelf this one overflows from.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">list_edition_scans</a>(...) -> typing.List[Scan]</code></summary>
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

client.list_edition_scans(
    branch_path_param="branch",
    edition_path_param="edition",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**branch_path_param:** `str` — The branch that scanned the edition.
    
</dd>
</dl>

<dl>
<dd>

**edition_path_param:** `str` — The edition scanned.
    
</dd>
</dl>

<dl>
<dd>

**edition:** `typing.Optional[str]` — The edition the reader app currently shows.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">list_loans</a>(...) -> typing.List[Loan]</code></summary>
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

client.list_loans(
    patron="patron",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**patron:** `str` — The patron whose loans are listed.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — How many loans to list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

