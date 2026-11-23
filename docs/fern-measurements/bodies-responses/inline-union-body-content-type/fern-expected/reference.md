# Reference
## Verifications
<details><summary><code>client.verifications.<a href="src/fern/verifications/client.py#L34-L63">add_verification</a>(...)</code></summary>
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

<details><summary><code>client.verifications.<a href="src/fern/verifications/client.py#L65-L94">recheck_verification</a>(...)</code></summary>
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

<details><summary><code>client.verifications.<a href="src/fern/verifications/client.py#L96-L125">send_reminder</a>(...)</code></summary>
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

<details><summary><code>client.verifications.<a href="src/fern/verifications/client.py#L127-L156">send_notice</a>(...)</code></summary>
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
from fern.verifications import SendNoticeRequest_Email

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.verifications.send_notice(
    request=SendNoticeRequest_Email(
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

**request:** `SendNoticeRequest` — Either address to notify.
    
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

<details><summary><code>client.verifications.<a href="src/fern/verifications/client.py#L158-L187">add_contact</a>(...)</code></summary>
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
from fern.verifications import AddContactRequest_Email

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.verifications.add_contact(
    request=AddContactRequest_Email(
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

**request:** `AddContactRequest` 
    
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

<details><summary><code>client.verifications.<a href="src/fern/verifications/client.py#L189-L218">add_tagged_contact</a>(...)</code></summary>
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
from fern.verifications import AddTaggedContactRequest_Email

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.verifications.add_tagged_contact(
    request=AddTaggedContactRequest_Email(
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

**request:** `AddTaggedContactRequest` 
    
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

