# Reference
## Sweeps
<details><summary><code>client.sweeps.<a href="src/fern/sweeps/client.py">complex</a>(...) -> Complex</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.sweeps.complex_(
    sweep_id="sweepId",
    frequency=1.1,
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

**sweep_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**frequency:** `float` — Sweep frequency in hertz.
    
</dd>
</dl>

<dl>
<dd>

**complex:** `typing.Optional[bool]` — Report the point in rectangular rather than polar form.
    
</dd>
</dl>

<dl>
<dd>

**complex_request_complex:** `typing.Optional[bool]` — Return the conjugate as well.
    
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

<details><summary><code>client.sweeps.<a href="src/fern/sweeps/client.py">calibrate</a>(...)</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.sweeps.calibrate()

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

**complex:** `typing.Optional[bool]` — Apply the correction to the complex plane only.
    
</dd>
</dl>

<dl>
<dd>

**calibration_complex:** `typing.Optional[float]` — Phase correction, in degrees.
    
</dd>
</dl>

<dl>
<dd>

**gain:** `typing.Optional[float]` 
    
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

<details><summary><code>client.sweeps.<a href="src/fern/sweeps/client.py">get_range</a>(...) -> Range</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.sweeps.get_range(
    sweep_id="sweepId",
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

**sweep_id:** `str` 
    
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

