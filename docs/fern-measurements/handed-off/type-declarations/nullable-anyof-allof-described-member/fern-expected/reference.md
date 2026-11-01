# Reference
<details><summary><code>client.<a href="src/fern/client.py">create_plan</a>(...) -> Plan</code></summary>
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

client.create_plan()

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

**course:** `typing.Optional[CreatePlanBodyCourse]` — Which course to plan, if any.
    
</dd>
</dl>

<dl>
<dd>

**diet:** `typing.Optional[CreatePlanBodyDiet]` — Dietary needs the plan must respect.
    
</dd>
</dl>

<dl>
<dd>

**servings:** `typing.Optional[int]` — How many people eat.
    
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

