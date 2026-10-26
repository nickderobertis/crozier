# Reference
## Pots
<details><summary><code>client.pots.<a href="src/fern/pots/client.py">record_pot</a>(...) -> Pot</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PotOuterCoat_Matte
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.pots.record_pot(
    potter="potter",
    outer_coat=PotOuterCoat_Matte(
        tooth=1,
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

**request:** `Pot` 
    
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

<details><summary><code>client.pots.<a href="src/fern/pots/client.py">recoat_pot</a>(...) -> Pot</code></summary>
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
from fern.pots import RecoatPotRequestCoat_Matte

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.pots.recoat_pot(
    pot_id="potId",
    coat=RecoatPotRequestCoat_Matte(
        tooth=1,
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

**pot_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**coat:** `RecoatPotRequestCoat` — The fresh coat to apply.
    
</dd>
</dl>

<dl>
<dd>

**previous_coat:** `typing.Optional[Coat]` 
    
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

