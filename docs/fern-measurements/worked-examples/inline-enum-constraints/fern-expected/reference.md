# Reference
<details><summary><code>client.<a href="src/fern/client.py#L105-L169">book_passage</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PassageGate, PassageLane, PassageSide, PassagePilot, PassageWindow

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.book_passage(
    vessel="vessel",
    gate=PassageGate.UPPER,
    lane=PassageLane.EAST,
    side=PassageSide.PORT,
    pilot=PassagePilot.HARBOUR,
    window=PassageWindow.SLACK,
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

**vessel:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**gate:** `PassageGate` — Its own `not` rejects the first member.
    
</dd>
</dl>

<dl>
<dd>

**lane:** `PassageLane` — The first member already satisfies the pattern.
    
</dd>
</dl>

<dl>
<dd>

**side:** `PassageSide` — No member satisfies the pattern, so the first stands.
    
</dd>
</dl>

<dl>
<dd>

**pilot:** `PassagePilot` — A format no member is decided against, so the first stands.
    
</dd>
</dl>

<dl>
<dd>

**window:** `PassageWindow` — Locks never open at slack water.
    
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

<details><summary><code>client.<a href="src/fern/client.py#L171-L201">book_mooring</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, BookMooringRequestTide

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.book_mooring(
    berth="berth",
    tide=BookMooringRequestTide.SLACK,
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

**berth:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tide:** `BookMooringRequestTide` 
    
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

