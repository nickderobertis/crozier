# Reference
<details><summary><code>client.<a href="src/fern/client.py">record_map_accepted</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, MapAcceptedPlan, MapAcceptedChoiceWindow, MapAcceptedChoiceWindowWindow

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.record_map_accepted(
    plan=MapAcceptedPlan(
        choice=MapAcceptedChoiceWindow(
            window=MapAcceptedChoiceWindowWindow(
                lookback={
                    "days": 20
                },
            ),
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

**plan:** `MapAcceptedPlan` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">record_map_rejected</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, MapRejectedPlan, MapRejectedChoiceWindow, MapRejectedChoiceWindowWindow

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.record_map_rejected(
    plan=MapRejectedPlan(
        choice=MapRejectedChoiceWindow(
            window=MapRejectedChoiceWindowWindow(
                lookback={
                    "days": 20
                },
            ),
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

**plan:** `MapRejectedPlan` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">record_closed_accepted</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ClosedAcceptedPlan, ClosedAcceptedChoiceWindow, ClosedAcceptedChoiceWindowWindow, ClosedAcceptedChoiceWindowWindowLookback

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.record_closed_accepted(
    plan=ClosedAcceptedPlan(
        choice=ClosedAcceptedChoiceWindow(
            window=ClosedAcceptedChoiceWindowWindow(
                lookback=ClosedAcceptedChoiceWindowWindowLookback(
                    days=20,
                ),
            ),
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

**plan:** `ClosedAcceptedPlan` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">record_closed_rejected</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ClosedRejectedPlan, ClosedRejectedChoiceWindow, ClosedRejectedChoiceWindowWindow, ClosedRejectedChoiceWindowWindowLookback

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.record_closed_rejected(
    plan=ClosedRejectedPlan(
        choice=ClosedRejectedChoiceWindow(
            window=ClosedRejectedChoiceWindowWindow(
                lookback=ClosedRejectedChoiceWindowWindowLookback(
                    days=20,
                ),
            ),
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

**plan:** `ClosedRejectedPlan` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">record_null_allowed</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, NullAllowedPlan, NullAllowedChoiceWindow, NullAllowedChoiceWindowWindow

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.record_null_allowed(
    plan=NullAllowedPlan(
        choice=NullAllowedChoiceWindow(
            window=NullAllowedChoiceWindowWindow(
                lookback=20,
            ),
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

**plan:** `NullAllowedPlan` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">record_null_disallowed</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, NullDisallowedPlan, NullDisallowedChoiceWindow, NullDisallowedChoiceWindowWindow

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.record_null_disallowed(
    plan=NullDisallowedPlan(
        choice=NullDisallowedChoiceWindow(
            window=NullDisallowedChoiceWindowWindow(
                lookback=20,
            ),
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

**plan:** `NullDisallowedPlan` 
    
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

