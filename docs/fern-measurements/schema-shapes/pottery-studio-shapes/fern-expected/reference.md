# Reference
## Firings
<details><summary><code>client.firings.<a href="src/fern/firings/client.py">book_firing</a>(...) -> FiringBooking</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

    Books a slot on the shared kiln.
    The slot is held for one hour before it lapses.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, FiringBookingShelf, FiringBookingShelfLevel, FiringBookingEnding_Cooled
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.firings.book_firing(
    potter="potter",
    cone=1,
    shelf=FiringBookingShelf(
        level=FiringBookingShelfLevel.UPPER,
        slot=1,
    ),
    ending=FiringBookingEnding_Cooled(
        hours=1,
    ),
    palette=[
        "palette"
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

**request:** `FiringBooking` 
    
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

## Batches
<details><summary><code>client.batches.<a href="src/fern/batches/client.py">mix_batch</a>(...)</code></summary>
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
from fern.batches import MixBatchRequest_Recipe

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.batches.mix_batch(
    request=MixBatchRequest_Recipe(
        recipe="recipe",
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

**request:** `MixBatchRequest` — How the batch is sourced.
    
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

