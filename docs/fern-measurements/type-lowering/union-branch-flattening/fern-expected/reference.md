# Reference
## Ramps
<details><summary><code>client.ramps.<a href="src/fern/ramps/client.py#L34-L92">create_ramp</a>(...) -> Ramp</code></summary>
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

client.ramps.create_ramp(
    amount="amount",
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

**amount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[RampRequestDirection]` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[FiatSource]` 
    
</dd>
</dl>

<dl>
<dd>

**destination:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**payment_instructions:** `typing.Optional[RampRequestPaymentInstructions]` 
    
</dd>
</dl>

<dl>
<dd>

**hops:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ramps.<a href="src/fern/ramps/client.py#L94-L116">list_methods</a>() -> typing.List[RampMethod]</code></summary>
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

client.ramps.list_methods()

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

<details><summary><code>client.ramps.<a href="src/fern/ramps/client.py#L118-L140">list_tickets</a>() -> typing.List[Ticket]</code></summary>
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

client.ramps.list_tickets()

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

