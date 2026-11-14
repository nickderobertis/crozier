# Reference
<details><summary><code>client.<a href="src/fern/client.py#L98-L131">order_print</a>(...) -> OrderPrintResponse</code></summary>
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

client.order_print()

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

**finish:** `typing.Optional[OrderPrintRequestFinish]` — The paper finish; which ones apply depends on the stock.
    
</dd>
</dl>

<dl>
<dd>

**dpi:** `typing.Optional[float]` 
    
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

