# Reference
## Verifications
<details><summary><code>client.verifications.<a href="src/fern/verifications/client.py#L31-L60">add_verification</a>(...)</code></summary>
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
from fern.verifications import AddVerificationRequest_Email

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.verifications.add_verification(
    request=AddVerificationRequest_Email(
        email="email",
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

**request:** `AddVerificationRequest` 
    
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

<details><summary><code>client.verifications.<a href="src/fern/verifications/client.py#L62-L91">recheck_verification</a>(...)</code></summary>
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
from fern.verifications import RecheckVerificationRequest_Email

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.verifications.recheck_verification(
    request=RecheckVerificationRequest_Email(
        email="email",
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

**request:** `RecheckVerificationRequest` 
    
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

<details><summary><code>client.verifications.<a href="src/fern/verifications/client.py#L93-L122">send_reminder</a>(...)</code></summary>
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
from fern.verifications import SendReminderRequest_Email

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.verifications.send_reminder(
    request=SendReminderRequest_Email(
        email="email",
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

**request:** `SendReminderRequest` 
    
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

