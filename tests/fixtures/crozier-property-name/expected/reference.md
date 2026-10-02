# Reference
## Practice
<details><summary><code>client.practice.<a href="src/fern/practice/client.py">create_service_metadata</a>(...) -> PracticeServiceMetadata</code></summary>
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

client.practice.create_service_metadata(
    practice_id="practice_id",
    practice_service_metadata_create_practice_id="practice_id",
    service_name="service_name",
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

**practice_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**practice_service_metadata_create_practice_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**service_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**duration_minutes:** `typing.Optional[int]` 
    
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

<details><summary><code>client.practice.<a href="src/fern/practice/client.py">create_intent</a>(...) -> PracticeIntent</code></summary>
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

client.practice.create_intent(
    practice_id="practice_id",
    practice_intent_create_practice_id="practice_id",
    intent="intent",
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

**practice_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**practice_intent_create_practice_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**intent:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` 
    
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

<details><summary><code>client.practice.<a href="src/fern/practice/client.py">create_insurance_product</a>(...) -> PracticeEvent</code></summary>
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

client.practice.create_insurance_product(
    practice_id="practice_id",
    insurance_product_practice_id="practice_id",
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

**practice_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**insurance_product_practice_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**coverage:** `typing.Optional[CreateInsuranceProductRequestCoverage]` 
    
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

<details><summary><code>client.practice.<a href="src/fern/practice/client.py">create_note</a>(...)</code></summary>
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

client.practice.create_note(
    practice_id="practice_id",
    note_practice_id="practice_id",
    body="body",
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

**practice_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**note_practice_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `str` 
    
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

