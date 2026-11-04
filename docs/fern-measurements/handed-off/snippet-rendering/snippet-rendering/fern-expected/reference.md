# Reference
## Manifests
<details><summary><code>client.manifests.<a href="src/fern/manifests/client.py">file_manifest</a>(...) -> Receipt</code></summary>
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
    tenant_code="<X-Tenant-Code>",
    environment=FernApiEnvironment.DEFAULT,
)

client.manifests.file_manifest(
    request={
        "vessel": {"name": "Aurora Borealis of the Northern Fjords", "flag": "Norway"},
        "cargo": [{"code": "C-100", "weight": 12}, {"code": "C-200", "weight": 7}],
        "draft": 8.5
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

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Berths
<details><summary><code>client.berths.<a href="src/fern/berths/client.py">list_berths</a>(...) -> typing.List[Berth]</code></summary>
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
    tenant_code="<X-Tenant-Code>",
    environment=FernApiEnvironment.DEFAULT,
)

client.berths.list_berths(
    zone="zone",
    codes_array=[
        "codes[]"
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

**zone:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**codes_array:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.berths.<a href="src/fern/berths/client.py">release_berths</a>(...)</code></summary>
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
    tenant_code="<X-Tenant-Code>",
    environment=FernApiEnvironment.DEFAULT,
)

client.berths.release_berths(
    ids_array=[
        "B-7"
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

**ids_array:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

