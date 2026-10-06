# Reference
## Exposures
<details><summary><code>client.exposures.<a href="src/fern/exposures/client.py">list_exposures</a>(...) -> typing.List[str]</code></summary>
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

client.exposures.list_exposures(
    gains=[
        1
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

**filters:** `typing.Optional[typing.Union[ListExposuresRequestFiltersItem, typing.Sequence[ListExposuresRequestFiltersItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**gains:** `typing.Optional[typing.Union[ListExposuresRequestGainsItem, typing.Sequence[ListExposuresRequestGainsItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Targets
<details><summary><code>client.targets.<a href="src/fern/targets/client.py">list_targets</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.targets import ListTargetsRequestKindsItemZero

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.targets.list_targets(
    kinds=[
        ListTargetsRequestKindsItemZero.NEBULA
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

**kinds:** `typing.Optional[typing.Union[ListTargetsRequestKindsItem, typing.Sequence[ListTargetsRequestKindsItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

