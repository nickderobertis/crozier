# Reference
## Seals
<details><summary><code>client.seals.<a href="src/fern/seals/client.py">verify_seal</a>(...) -> VerifySealResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.seals import VerifySealRequestSeal_Stamp

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.seals.verify_seal(
    seal=VerifySealRequestSeal_Stamp(
        stamp_id="stamp_id",
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

**seal:** `VerifySealRequestSeal` 
    
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

<details><summary><code>client.seals.<a href="src/fern/seals/client.py">verify_logbook</a>(...) -> VerifyLogbookResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, EntryV2, PageV2

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.seals.verify_logbook(
    entry=EntryV2(
        page=PageV2(
            edition="2.0",
            keeper="Morwenna",
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

**entry:** `VerifyLogbookRequestEntry` 
    
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

<details><summary><code>client.seals.<a href="src/fern/seals/client.py">stock_shelf</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.seals import StockShelfRequestShelfValue_Stamp

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.seals.stock_shelf(
    shelf={
        "top": StockShelfRequestShelfValue_Stamp(
            stamp_id="stamp_id",
        )
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

**shelf:** `typing.Dict[str, StockShelfRequestShelfValue]` 
    
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

<details><summary><code>client.seals.<a href="src/fern/seals/client.py">verify_badge</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.seals import VerifyBadgeRequestBadge_Copper

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.seals.verify_badge(
    badge=VerifyBadgeRequestBadge_Copper(
        serial="serial",
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

**badge:** `VerifyBadgeRequestBadge` 
    
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

<details><summary><code>client.seals.<a href="src/fern/seals/client.py">register_seal</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.seals import SealRegistrationSeal_Stamp

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.seals.register_seal(
    seal=SealRegistrationSeal_Stamp(
        stamp_id="stamp_id",
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

**seal:** `SealRegistrationSeal` 
    
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

<details><summary><code>client.seals.<a href="src/fern/seals/client.py">verify_charm</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.seals import VerifyCharmRequestToken_Wax

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.seals.verify_charm(
    token=VerifyCharmRequestToken_Wax(
        colour="colour",
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

**token:** `VerifyCharmRequestToken` 
    
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

<details><summary><code>client.seals.<a href="src/fern/seals/client.py">inspect_charm</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.seals import InspectCharmRequestToken_Wax

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.seals.inspect_charm(
    token=InspectCharmRequestToken_Wax(
        colour="colour",
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

**token:** `InspectCharmRequestToken` 
    
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

