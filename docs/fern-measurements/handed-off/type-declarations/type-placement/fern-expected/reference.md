# Reference
<details><summary><code>client.<a href="src/fern/client.py">check_health</a>(...) -> CheckHealthResponse</code></summary>
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

client.check_health()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**depth:** `typing.Optional[CheckHealthRequestDepth]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Parcels
<details><summary><code>client.parcels.<a href="src/fern/parcels/client.py">list_parcels</a>(...) -> typing.List[str]</code></summary>
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

client.parcels.list_parcels()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**priority:** `typing.Optional[ListParcelsRequestPriority]` — Sorting priority.
    
</dd>
</dl>

<dl>
<dd>

**carrier:** `typing.Optional[ListParcelsRequestCarrier]` — Carrier to filter by.
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — One label or several to print.
    
</dd>
</dl>

<dl>
<dd>

**label_style:** `typing.Optional[ListParcelsRequestLabelStyle]` — How the labels are printed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Letters
<details><summary><code>client.letters.<a href="src/fern/letters/client.py">list_letters</a>(...) -> typing.List[str]</code></summary>
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

client.letters.list_letters()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**priority:** `typing.Optional[ListLettersRequestPriority]` — Sorting priority.
    
</dd>
</dl>

<dl>
<dd>

**carrier:** `typing.Optional[ListLettersRequestCarrier]` — Carrier to filter by.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Depots Sacks
<details><summary><code>client.depots.sacks.<a href="src/fern/depots/sacks/client.py">list</a>(...) -> typing.List[str]</code></summary>
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

client.depots.sacks.list(
    depot_id="depotId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**depot_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[ListSacksRequestPriority]` — Sorting priority.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

