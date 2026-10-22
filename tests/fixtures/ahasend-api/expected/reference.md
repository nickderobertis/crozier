# Reference
## Utility
<details><summary><code>client.utility.<a href="src/fern/utility/client.py">ping</a>() -> SuccessResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Health check endpoint that returns a simple pong response
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.utility.ping()

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## API Keys
<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">get_api_keys</a>(...) -> PaginatedApiKeysResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of API keys for the account
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.get_api_keys(
    account_id="account_id",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Pagination cursor for the previous page.
    
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

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">create_api_key</a>(...) -> CreateApiKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new API key with the specified scopes
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.create_api_key(
    account_id="account_id",
    idempotency_key="user-12345-create-domain-20240101",
    label="Production API Key",
    scopes=[
        "messages:send:all",
        "domains:read"
    ],
    ip_allow_list=[
        "203.0.113.0/24",
        "198.51.100.7"
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateApiKeyRequest` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

Optional idempotency key for safe request retries. Must be a unique string for each logical request.
An identical request with a completed stored outcome returns the original status and body. An in-progress
execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
so successful encrypted replay responses for those operations expire after 5 minutes.
    
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

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">get_api_key</a>(...) -> ApiKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a specific API key by ID
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.get_api_key(
    account_id="account_id",
    key_id="key_id",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**key_id:** `str` — API Key ID
    
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

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">update_api_key</a>(...) -> ApiKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing API key's label and scopes
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
from fern import FernApi, UpdateApiKeyRequestLabel
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.update_api_key(
    account_id="account_id",
    key_id="key_id",
    request=UpdateApiKeyRequestLabel(
        label="label",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**key_id:** `str` — API Key ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateApiKeyRequest` 
    
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

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">delete_api_key</a>(...) -> SuccessResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an API key
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.delete_api_key(
    account_id="account_id",
    key_id="key_id",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**key_id:** `str` — API Key ID
    
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

## Domains
<details><summary><code>client.domains.<a href="src/fern/domains/client.py">get_domains</a>(...) -> PaginatedDomainsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of domains for the account
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.domains.get_domains(
    account_id="account_id",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**dns_valid:** `typing.Optional[bool]` — Filter results by DNS validation status
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return (1-100)
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Pagination cursor for the previous page.
    
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

<details><summary><code>client.domains.<a href="src/fern/domains/client.py">create_domain</a>(...) -> Domain</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new domain
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.domains.create_domain(
    account_id="account_id",
    idempotency_key="user-12345-create-domain-20240101",
    domain="example.com",
    tracking_subdomain="click",
    return_path_subdomain="mail",
    subscription_subdomain="preferences",
    media_subdomain="media",
    dkim_rotation_interval_days=45,
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**domain:** `str` — Fully qualified domain name
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

Optional idempotency key for safe request retries. Must be a unique string for each logical request.
An identical request with a completed stored outcome returns the original status and body. An in-progress
execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
so successful encrypted replay responses for those operations expire after 5 minutes.
    
</dd>
</dl>

<dl>
<dd>

**dkim_private_key:** `typing.Optional[str]` 

DKIM Private Key for the domain. Only RSA keys with a minimum key size of 1024 bits are supported.

**Note:** This parameter is only supported on [Platform Partner](https://ahasend.com/partners) accounts.

<Note>Key size of at least 1024 bits is supported; 2048 bit keys are strongly recommended for improved security.</Note>
    
</dd>
</dl>

<dl>
<dd>

**tracking_subdomain:** `typing.Optional[str]` — Optional custom tracking subdomain. Omit to use the default on create. Applies to both manual-DNS and managed-DNS domains.
    
</dd>
</dl>

<dl>
<dd>

**return_path_subdomain:** `typing.Optional[str]` — Optional custom return-path subdomain. Omit to use the default on create. Applies to both manual-DNS and managed-DNS domains.
    
</dd>
</dl>

<dl>
<dd>

**subscription_subdomain:** `typing.Optional[str]` — Optional custom subscription management subdomain. Omit to use the default on create. Applies to both manual-DNS and managed-DNS domains.
    
</dd>
</dl>

<dl>
<dd>

**media_subdomain:** `typing.Optional[str]` — Optional custom media subdomain. Omit to use the default on create. Applies to both manual-DNS and managed-DNS domains.
    
</dd>
</dl>

<dl>
<dd>

**dkim_rotation_interval_days:** `typing.Optional[int]` — Optional custom DKIM rotation interval in days. Only supported for managed DNS domains on eligible plans.
    
</dd>
</dl>

<dl>
<dd>

**dkim_selector:** `typing.Optional[str]` 

Optional custom DKIM selector for the domain. Omit, send null, or send an empty or whitespace-only string to use the default selector (no per-domain override); the value is trimmed before it is interpreted, so whitespace-only input is treated as empty.

When provided, it is normalized to lowercase and must be a single DNS label: 1-62 characters using lowercase letters, numbers, and hyphens only, without a leading or trailing hyphen.

**Note:** This parameter is only supported on [Platform Partner](https://ahasend.com/partners) accounts.
    
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

<details><summary><code>client.domains.<a href="src/fern/domains/client.py">get_domain</a>(...) -> Domain</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a specific domain by name
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.domains.get_domain(
    account_id="account_id",
    domain="domain",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**domain:** `str` — Domain name
    
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

<details><summary><code>client.domains.<a href="src/fern/domains/client.py">update_domain</a>(...) -> Domain</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates DNS domain settings such as custom subdomains and DKIM rotation interval.
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.domains.update_domain(
    account_id="account_id",
    domain="domain",
    tracking_subdomain="click",
    return_path_subdomain="mail",
    subscription_subdomain="preferences",
    media_subdomain="media",
    dkim_rotation_interval_days=45,
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**domain:** `str` — Domain name
    
</dd>
</dl>

<dl>
<dd>

**tracking_subdomain:** `typing.Optional[str]` — Optional custom tracking subdomain. Omit to leave the current value unchanged. Applies to both manual-DNS and managed-DNS domains.
    
</dd>
</dl>

<dl>
<dd>

**return_path_subdomain:** `typing.Optional[str]` — Optional custom return-path subdomain. Omit to leave the current value unchanged. Applies to both manual-DNS and managed-DNS domains.
    
</dd>
</dl>

<dl>
<dd>

**subscription_subdomain:** `typing.Optional[str]` — Optional custom subscription management subdomain. Omit to leave the current value unchanged. Applies to both manual-DNS and managed-DNS domains.
    
</dd>
</dl>

<dl>
<dd>

**media_subdomain:** `typing.Optional[str]` — Optional custom media subdomain. Omit to leave the current value unchanged. Applies to both manual-DNS and managed-DNS domains.
    
</dd>
</dl>

<dl>
<dd>

**dkim_rotation_interval_days:** `typing.Optional[int]` — Optional custom DKIM rotation interval in days. Omit to leave the current value unchanged. Only supported for managed DNS domains on eligible plans.
    
</dd>
</dl>

<dl>
<dd>

**dkim_selector:** `typing.Optional[str]` 

Optional custom DKIM selector for the domain. Omit or send null to leave the current value unchanged; send an empty or whitespace-only string to clear the override and revert to the default selector. The value is trimmed before it is interpreted, so whitespace-only input clears the override just like an empty string.

When provided, it is normalized to lowercase and must be a single DNS label: 1-62 characters using lowercase letters, numbers, and hyphens only, without a leading or trailing hyphen. It cannot be changed once the selector locks after DNS verification or while a DKIM key rotation is in progress.

**Note:** This parameter is only supported on [Platform Partner](https://ahasend.com/partners) accounts.
    
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

<details><summary><code>client.domains.<a href="src/fern/domains/client.py">delete_domain</a>(...) -> SuccessResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a domain
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.domains.delete_domain(
    account_id="account_id",
    domain="domain",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**domain:** `str` — Domain name
    
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

<details><summary><code>client.domains.<a href="src/fern/domains/client.py">check_domain_dns</a>(...) -> Domain</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Triggers a DNS validation check for the domain. If the domain was checked within the last 60 seconds, the cached validation result is returned instead of performing a fresh lookup.
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.domains.check_domain_dns(
    account_id="account_id",
    domain="domain",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**domain:** `str` — Domain name
    
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

## Messages
<details><summary><code>client.messages.<a href="src/fern/messages/client.py">get_messages</a>(...) -> PaginatedMessagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of message summaries for the account. Can be filtered by various parameters.

`messages:read:all` can read across the account. Domain-scoped keys see
only messages for domains authorized by their matching read roles.
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
from fern import FernApi
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.messages.get_messages(
    account_id="account_id",
    status="Bounced,Failed",
    tags="billing,urgent",
    from_time=datetime.datetime.fromisoformat("2023-12-25T10:30:00+00:00"),
    to_time=datetime.datetime.fromisoformat("2023-12-26T10:30:00+00:00"),
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 

Filter by comma-separated list of message statuses. Allowed values are:
`Received`, `Delivered`, `Deferred`, `Bounced`, `Failed`, `Suppressed`,
`Sandbox Delivered`, `Sandbox Deferred`, `Sandbox Failed`, `Sandbox Bounced`,
and `Sandbox Suppressed`.
    
</dd>
</dl>

<dl>
<dd>

**sender:** `typing.Optional[str]` — Sender email address (must be from domain in API key scopes)
    
</dd>
</dl>

<dl>
<dd>

**recipient:** `typing.Optional[str]` — Recipient email address
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[str]` — Filter by subject text
    
</dd>
</dl>

<dl>
<dd>

**message_id_header:** `typing.Optional[str]` — Filter by message ID header (same ID returned by CreateMessage API)
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[str]` — Filter by comma-separated list of tags (max 20)
    
</dd>
</dl>

<dl>
<dd>

**from_time:** `typing.Optional[datetime.datetime]` — Filter messages created after this time (RFC3339 format)
    
</dd>
</dl>

<dl>
<dd>

**to_time:** `typing.Optional[datetime.datetime]` — Filter messages created before this time (RFC3339 format)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return (1-100)
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Pagination cursor for the previous page.
    
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

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">create_message</a>(...) -> CreateMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates and sends a message to one or more recipients. This API cannot be used if you want to send a conversational/P2P message and set CC or BCC. Use [Create Conversation Message](https://ahasend.com/docs/api-reference/messages/create-conversation) instead.

**Validation Requirements:**
- Either `text_content` or `html_content` is required
- `from.email` must be from a domain you own with valid DNS records
- `retention.metadata` must be between 1 and 30 days
- `retention.data` must be between 0 and 30 days
- If `reply_to` is provided, do not include `reply-to` in headers
- `message-id` header will be ignored and automatically generated
- Schedule times must be in RFC3339 format
- `schedule.first_attempt` must be in the future and within 7 days of the request
- `schedule.expires` must be in the future and within 8 days of the request

Authorization uses the domain in `from.email`: either
`messages:send:all` or the matching domain-specific send role is
sufficient.
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
from fern import FernApi, Address, Recipient
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.messages.create_message(
    account_id="account_id",
    idempotency_key="user-12345-create-domain-20240101",
    from_=Address(
        email="noreply@example.com",
        name="Example Corp",
    ),
    recipients=[
        Recipient(
            email="user@example.com",
            name="John Doe",
        )
    ],
    subject="Welcome to Example Corp",
    text_content="Welcome {{first_name}}!",
    html_content="<h1>Welcome {{first_name}}!</h1>",
    substitutions={
        "first_name": "John"
    },
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**from:** `Address` 
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.List[Recipient]` — This does not set the To header to multiple addresses, it sends a separate message for each recipient
    
</dd>
</dl>

<dl>
<dd>

**subject:** `str` — Email subject line
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

Optional idempotency key for safe request retries. Must be a unique string for each logical request.
An identical request with a completed stored outcome returns the original status and body. An in-progress
execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
so successful encrypted replay responses for those operations expire after 5 minutes.
    
</dd>
</dl>

<dl>
<dd>

**reply_to:** `typing.Optional[Address]` — If provided, the reply-to header in headers array must not be provided
    
</dd>
</dl>

<dl>
<dd>

**text_content:** `typing.Optional[str]` — Plain text content. Required if html_content is empty
    
</dd>
</dl>

<dl>
<dd>

**html_content:** `typing.Optional[str]` — HTML content. Required if text_content is empty
    
</dd>
</dl>

<dl>
<dd>

**amp_content:** `typing.Optional[str]` — AMP HTML content
    
</dd>
</dl>

<dl>
<dd>

**attachments:** `typing.Optional[typing.List[Attachment]]` — File attachments. For inline images, set the attachment's `content_id` to a value wrapped in angle brackets (e.g. `<image1@example.com>`) and reference it from `html_content` with `cid:` (e.g. `<img src="cid:image1@example.com">`).
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.Dict[str, str]]` — Custom email headers. reply-to header cannot be provided if reply_to is provided, message-id will be ignored and automatically generated
    
</dd>
</dl>

<dl>
<dd>

**substitutions:** `typing.Optional[typing.Dict[str, typing.Any]]` — Global substitutions, recipient substitutions override global
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — Tags for categorizing messages
    
</dd>
</dl>

<dl>
<dd>

**sandbox:** `typing.Optional[bool]` — If true, the message will be sent to the sandbox environment
    
</dd>
</dl>

<dl>
<dd>

**sandbox_result:** `typing.Optional[CreateMessageRequestSandboxResult]` — The result of the sandbox send
    
</dd>
</dl>

<dl>
<dd>

**tracking:** `typing.Optional[Tracking]` — Tracking settings for the message, overrides default account settings
    
</dd>
</dl>

<dl>
<dd>

**retention:** `typing.Optional[Retention]` — Retention settings for the message, overrides default account settings
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[MessageSchedule]` — Schedule for message delivery
    
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

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">create_conversation_message</a>(...) -> CreateMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates and sends a conversational message (with support for CC and BCC) to one or more recipients. This API does not support template substitutions, use [Create Message](https://ahasend.com/docs/api-reference/messages/create-message) instead if you need substitutions.

**Validation Requirements:**
- Either `text_content` or `html_content` is required
- `from.email` must be from a domain you own with valid DNS records
- `retention.metadata` must be between 1 and 30 days
- `retention.data` must be between 0 and 30 days
- If the `reply_to` parameter is provided, do not include `reply-to` in headers
- If the `cc` parameter is provided, do not include `cc` in headers
- `message-id` header will be ignored and automatically generated
- Schedule times must be in RFC3339 format
- `schedule.first_attempt` must be in the future and within 7 days of the request
- `schedule.expires` must be in the future and within 8 days of the request

Authorization uses the domain in `from.email`: either
`messages:send:all` or the matching domain-specific send role is
sufficient.
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
from fern import FernApi, Address
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.messages.create_conversation_message(
    account_id="account_id",
    idempotency_key="user-12345-create-domain-20240101",
    from_=Address(
        email="noreply@example.com",
        name="Example Corp",
    ),
    to=[
        Address(
            email="user@example.com",
            name="John Doe",
        ),
        Address(
            email="someone@example.com",
            name="Jane Doe",
        )
    ],
    cc=[
        Address(
            email="hr@example.com",
            name="Example Corp HR",
        )
    ],
    bcc=[
        Address(
            email="bcc@example.com",
            name="BCC Recipient",
        )
    ],
    subject="Welcome to Example Corp",
    text_content="Dear John and Jane, welcome to Example Corp!",
    html_content="<h1>Dear John and Jane, welcome to Example Corp!</h1>",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**from:** `Address` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.List[Address]` — This parameter can set the `To` header to multiple addresses. The combined to, cc, and bcc recipient count must not exceed 50.
    
</dd>
</dl>

<dl>
<dd>

**subject:** `str` — Email subject line
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

Optional idempotency key for safe request retries. Must be a unique string for each logical request.
An identical request with a completed stored outcome returns the original status and body. An in-progress
execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
so successful encrypted replay responses for those operations expire after 5 minutes.
    
</dd>
</dl>

<dl>
<dd>

**cc:** `typing.Optional[typing.List[Address]]` — This parameter can set the `CC` header to multiple addresses. Do not include `cc` in the headers array. The combined to, cc, and bcc recipient count must not exceed 50.
    
</dd>
</dl>

<dl>
<dd>

**bcc:** `typing.Optional[typing.List[Address]]` — This parameter can set the `To` header to multiple addresses. The combined to, cc, and bcc recipient count must not exceed 50.
    
</dd>
</dl>

<dl>
<dd>

**reply_to:** `typing.Optional[Address]` — If provided, the reply-to header in headers array must not be provided
    
</dd>
</dl>

<dl>
<dd>

**text_content:** `typing.Optional[str]` — Plain text content. Required if html_content is empty
    
</dd>
</dl>

<dl>
<dd>

**html_content:** `typing.Optional[str]` — HTML content. Required if text_content is empty
    
</dd>
</dl>

<dl>
<dd>

**amp_content:** `typing.Optional[str]` — AMP HTML content
    
</dd>
</dl>

<dl>
<dd>

**attachments:** `typing.Optional[typing.List[Attachment]]` — File attachments. For inline images, set the attachment's `content_id` to a value wrapped in angle brackets (e.g. `<image1@example.com>`) and reference it from `html_content` with `cid:` (e.g. `<img src="cid:image1@example.com">`).
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.Dict[str, str]]` — Custom email headers. `cc` and `reply-to` headers cannot be provided if `reply_to` or `cc` parameters are provided, message-id will be ignored and automatically generated
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — Tags for categorizing messages
    
</dd>
</dl>

<dl>
<dd>

**sandbox:** `typing.Optional[bool]` — If true, the message will be sent to the sandbox environment
    
</dd>
</dl>

<dl>
<dd>

**sandbox_result:** `typing.Optional[CreateConversationMessageRequestSandboxResult]` — The result of the sandbox send
    
</dd>
</dl>

<dl>
<dd>

**tracking:** `typing.Optional[Tracking]` — Tracking settings for the message, overrides default account settings
    
</dd>
</dl>

<dl>
<dd>

**retention:** `typing.Optional[Retention]` — Retention settings for the message, overrides default account settings
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[MessageSchedule]` — Schedule for message delivery
    
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

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">get_message</a>(...) -> Message</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the complete message by its ID, including raw content and parsed content structure.
Access requires `messages:read:all` or a read role matching the
message's sender domain.
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.messages.get_message(
    account_id="account_id",
    message_id="message_id",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `str` — Message API ID. Accepts the generated Message-ID returned by [Create Message API](https://ahasend.com/docs/api-reference/messages/create-message), for example `<uuid@example.com>`, or the bare UUID portion.
    
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

<details><summary><code>client.messages.<a href="src/fern/messages/client.py">cancel_message</a>(...) -> SuccessResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels a scheduled message. Access requires `messages:cancel:all` or a
cancel role matching the message's sender domain.
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.messages.cancel_message(
    account_id="account_id",
    message_id="message_id",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `str` — Message API ID. Accepts the generated Message-ID returned by [Create Message API](https://ahasend.com/docs/api-reference/messages/create-message), for example `<uuid@example.com>`, or the bare UUID portion.
    
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

## Accounts
<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">get_account</a>(...) -> Account</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns account information
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.accounts.get_account(
    account_id="account_id",
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

**account_id:** `str` — Account ID
    
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

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">update_account</a>(...) -> Account</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates account settings

**Validation Requirements:**
- `name` must be maximum 255 characters
- `website` must be a valid URL
- `message_metadata_retention` must be between 1 and 30 days
- `message_data_retention` must be between 0 and 30 days
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.accounts.update_account(
    account_id="account_id",
    name="Updated Company Name",
    website="https://example.com",
    track_opens=True,
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Account name
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` — Account website URL
    
</dd>
</dl>

<dl>
<dd>

**about:** `typing.Optional[str]` — Account description (used for account verification)
    
</dd>
</dl>

<dl>
<dd>

**track_opens:** `typing.Optional[bool]` — Default open tracking setting
    
</dd>
</dl>

<dl>
<dd>

**track_clicks:** `typing.Optional[bool]` — Default click tracking setting
    
</dd>
</dl>

<dl>
<dd>

**reject_bad_recipients:** `typing.Optional[bool]` — Whether to reject bad recipients
    
</dd>
</dl>

<dl>
<dd>

**reject_mistyped_recipients:** `typing.Optional[bool]` — Whether to reject mistyped recipients
    
</dd>
</dl>

<dl>
<dd>

**message_metadata_retention:** `typing.Optional[int]` — Default message metadata retention in days
    
</dd>
</dl>

<dl>
<dd>

**message_data_retention:** `typing.Optional[int]` — Default message data retention in days
    
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

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">get_account_members</a>(...) -> AccountMembersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of account members
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.accounts.get_account_members(
    account_id="account_id",
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

**account_id:** `str` — Account ID
    
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

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">add_account_member</a>(...) -> UserAccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new member to the account

**Validation Requirements:**
- `email` must be a valid email address
- `role` must be one of: Administrator, Developer, Analyst, Billing Manager
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
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.accounts import AddMemberRequestRole

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.accounts.add_account_member(
    account_id="account_id",
    idempotency_key="user-12345-create-domain-20240101",
    email="user@example.com",
    name="John Doe",
    role=AddMemberRequestRole.DEVELOPER,
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — Email address of the user to add
    
</dd>
</dl>

<dl>
<dd>

**role:** `AddMemberRequestRole` — Role to assign to the user
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

Optional idempotency key for safe request retries. Must be a unique string for each logical request.
An identical request with a completed stored outcome returns the original status and body. An in-progress
execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
so successful encrypted replay responses for those operations expire after 5 minutes.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Display name for the user
    
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

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">remove_account_member</a>(...) -> SuccessResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a member from the account

**Restrictions:**
- You cannot delete yourself
- You cannot delete the account owner
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.accounts.remove_account_member(
    account_id="account_id",
    user_id="user_id",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — User ID
    
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

## SubAccounts
<details><summary><code>client.sub_accounts.<a href="src/fern/sub_accounts/client.py">list_sub_accounts</a>(...) -> PaginatedSubAccountsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a cursor-paginated list of sub accounts under the parent account. Soft-deleted sub accounts are not included; usage billed for sub accounts deleted during the current period is reported by the usage endpoint's `removed_sub_accounts` aggregate.
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sub_accounts.list_sub_accounts(
    account_id="account_id",
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

**account_id:** `str` — Parent account ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return (1-100)
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Pagination cursor for the next page. Provide the value from `next_cursor` in the response.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Pagination cursor for the previous page. Provide the value from `previous_cursor` in the response.
    
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

<details><summary><code>client.sub_accounts.<a href="src/fern/sub_accounts/client.py">create_sub_account</a>(...) -> SubAccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new sub account under the parent account
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sub_accounts.create_sub_account(
    account_id="account_id",
    idempotency_key="user-12345-create-domain-20240101",
    name="Acme Subsidiary",
    website="acme.example.com",
    monthly_credit=0,
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

**account_id:** `str` — Parent account ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable name for the sub account; leading and trailing whitespace is trimmed and the result must not be blank
    
</dd>
</dl>

<dl>
<dd>

**website:** `str` — Account website domain
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

Optional idempotency key for safe request retries. Must be a unique string for each logical request.
An identical request with a completed stored outcome returns the original status and body. An in-progress
execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
so successful encrypted replay responses for those operations expire after 5 minutes.
    
</dd>
</dl>

<dl>
<dd>

**monthly_credit:** `typing.Optional[int]` — Optional monthly cap; 0 means no cap
    
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

<details><summary><code>client.sub_accounts.<a href="src/fern/sub_accounts/client.py">get_sub_accounts_usage</a>(...) -> SubAccountUsageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns current billing-period usage and proportional allocated cost for the parent and active sub accounts
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sub_accounts.get_sub_accounts_usage(
    account_id="account_id",
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

**account_id:** `str` — Parent account ID
    
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

<details><summary><code>client.sub_accounts.<a href="src/fern/sub_accounts/client.py">get_sub_account</a>(...) -> SubAccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a specific sub account under the parent account
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sub_accounts.get_sub_account(
    account_id="account_id",
    sub_account_id="sub_account_id",
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

**account_id:** `str` — Parent account ID
    
</dd>
</dl>

<dl>
<dd>

**sub_account_id:** `str` — Sub account ID
    
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

<details><summary><code>client.sub_accounts.<a href="src/fern/sub_accounts/client.py">update_sub_account</a>(...) -> SubAccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a sub account's editable settings
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
from fern import FernApi, UpdateSubAccountRequestName
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sub_accounts.update_sub_account(
    account_id="account_id",
    sub_account_id="sub_account_id",
    request=UpdateSubAccountRequestName(
        name="name",
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

**account_id:** `str` — Parent account ID
    
</dd>
</dl>

<dl>
<dd>

**sub_account_id:** `str` — Sub account ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateSubAccountRequest` 
    
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

<details><summary><code>client.sub_accounts.<a href="src/fern/sub_accounts/client.py">delete_sub_account</a>(...) -> SuccessResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft-deletes a sub account under the parent account
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sub_accounts.delete_sub_account(
    account_id="account_id",
    sub_account_id="sub_account_id",
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

**account_id:** `str` — Parent account ID
    
</dd>
</dl>

<dl>
<dd>

**sub_account_id:** `str` — Sub account ID
    
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

<details><summary><code>client.sub_accounts.<a href="src/fern/sub_accounts/client.py">suspend_sub_account</a>(...) -> SubAccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Suspends a sub account under the parent account
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sub_accounts.suspend_sub_account(
    account_id="account_id",
    sub_account_id="sub_account_id",
    reason="Customer requested temporary pause",
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

**account_id:** `str` — Parent account ID
    
</dd>
</dl>

<dl>
<dd>

**sub_account_id:** `str` — Sub account ID
    
</dd>
</dl>

<dl>
<dd>

**reason:** `str` — Reason shown on the sub account suspension record
    
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

<details><summary><code>client.sub_accounts.<a href="src/fern/sub_accounts/client.py">unsuspend_sub_account</a>(...) -> SubAccount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unsuspends a sub account under the parent account
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sub_accounts.unsuspend_sub_account(
    account_id="account_id",
    sub_account_id="sub_account_id",
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

**account_id:** `str` — Parent account ID
    
</dd>
</dl>

<dl>
<dd>

**sub_account_id:** `str` — Sub account ID
    
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

<details><summary><code>client.sub_accounts.<a href="src/fern/sub_accounts/client.py">list_sub_account_api_keys</a>(...) -> PaginatedApiKeysResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a cursor-paginated list of API keys owned by a sub account. The `secret_key` field is omitted from list responses.
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sub_accounts.list_sub_account_api_keys(
    account_id="account_id",
    sub_account_id="sub_account_id",
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

**account_id:** `str` — Parent account ID
    
</dd>
</dl>

<dl>
<dd>

**sub_account_id:** `str` — Sub account ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return (1-100)
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Pagination cursor for the next page. Provide the value from `next_cursor` in the response.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Pagination cursor for the previous page. Provide the value from `previous_cursor` in the response.
    
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

<details><summary><code>client.sub_accounts.<a href="src/fern/sub_accounts/client.py">create_sub_account_api_key</a>(...) -> CreateSubAccountApiKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an API key owned by the sub account. Parent credentials must belong to the parent account and include `sub-account-api-keys:write`; sub-account credentials cannot manage nested API keys. The returned `secret_key` authenticates as the child account and should be stored immediately.

Bootstrap example:
1. Create the sub account with `POST /v2/accounts/{account_id}/sub-accounts` and a unique `Idempotency-Key`.
2. Create the bootstrap child API key with this endpoint and a different unique `Idempotency-Key`.
3. Store the one-time `secret_key` from the `201` response. Exact idempotent replays within 5 minutes return the same `secret_key`.
4. Use that child secret with the child `sub_account_id` as the `account_id` on ordinary v2 routes.
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sub_accounts.create_sub_account_api_key(
    account_id="account_id",
    sub_account_id="sub_account_id",
    idempotency_key="user-12345-create-domain-20240101",
    label="Bootstrap key",
    scopes=[
        "messages:send:all",
        "domains:read"
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

**account_id:** `str` — Parent account ID
    
</dd>
</dl>

<dl>
<dd>

**sub_account_id:** `str` — Sub account ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateApiKeyRequest` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

Optional idempotency key for safe request retries. Must be a unique string for each logical request.
An identical request with a completed stored outcome returns the original status and body. An in-progress
execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
so successful encrypted replay responses for those operations expire after 5 minutes.
    
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

<details><summary><code>client.sub_accounts.<a href="src/fern/sub_accounts/client.py">get_sub_account_api_key</a>(...) -> ApiKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a specific API key owned by a sub account. The `secret_key` field is omitted from read responses.
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sub_accounts.get_sub_account_api_key(
    account_id="account_id",
    sub_account_id="sub_account_id",
    key_id="key_id",
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

**account_id:** `str` — Parent account ID
    
</dd>
</dl>

<dl>
<dd>

**sub_account_id:** `str` — Sub account ID
    
</dd>
</dl>

<dl>
<dd>

**key_id:** `str` — API key ID
    
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

<details><summary><code>client.sub_accounts.<a href="src/fern/sub_accounts/client.py">update_sub_account_api_key</a>(...) -> ApiKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the label and scopes for an API key owned by a sub account. Updated scopes are validated against the child account.
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
from fern import FernApi, UpdateApiKeyRequestLabel
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sub_accounts.update_sub_account_api_key(
    account_id="account_id",
    sub_account_id="sub_account_id",
    key_id="key_id",
    request=UpdateApiKeyRequestLabel(
        label="Updated bootstrap key",
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

**account_id:** `str` — Parent account ID
    
</dd>
</dl>

<dl>
<dd>

**sub_account_id:** `str` — Sub account ID
    
</dd>
</dl>

<dl>
<dd>

**key_id:** `str` — API key ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateApiKeyRequest` 
    
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

<details><summary><code>client.sub_accounts.<a href="src/fern/sub_accounts/client.py">delete_sub_account_api_key</a>(...) -> SuccessResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an API key owned by a sub account.
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sub_accounts.delete_sub_account_api_key(
    account_id="account_id",
    sub_account_id="sub_account_id",
    key_id="key_id",
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

**account_id:** `str` — Parent account ID
    
</dd>
</dl>

<dl>
<dd>

**sub_account_id:** `str` — Sub account ID
    
</dd>
</dl>

<dl>
<dd>

**key_id:** `str` — API key ID
    
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

## Suppressions
<details><summary><code>client.suppressions.<a href="src/fern/suppressions/client.py">get_suppressions</a>(...) -> PaginatedSuppressionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of suppressions for the account

**Query Parameters:**
- `domain`: Filter by domain (optional)
- `email`: Filter by email (optional)
- `from_time`: Filter suppressions created after this time (RFC3339 format, optional)
- `to_time`: Filter suppressions created before this time (RFC3339 format, optional)
- `limit`: Maximum number of items to return (1-100, default: 100)
- `after`: Pagination cursor for the next page
- `before`: Pagination cursor for the previous page
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.suppressions.get_suppressions(
    account_id="account_id",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[str]` — Filter by domain
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Email address
    
</dd>
</dl>

<dl>
<dd>

**from_time:** `typing.Optional[datetime.datetime]` — Filter suppressions created after this time (RFC3339 format)
    
</dd>
</dl>

<dl>
<dd>

**to_time:** `typing.Optional[datetime.datetime]` — Filter suppressions created before this time (RFC3339 format)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return (1-100)
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Pagination cursor for the previous page. Provide the value provided in `previous_cursor` from the response.
    
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

<details><summary><code>client.suppressions.<a href="src/fern/suppressions/client.py">create_suppression</a>(...) -> CreateSuppressionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new suppression for an email address

**Validation Requirements:**
- `email` must be a valid email address
- `expires_at` must be in RFC3339 format
- `domain` is optional - if not provided, applies to all account domains
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
from fern import FernApi
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.suppressions.create_suppression(
    account_id="account_id",
    idempotency_key="user-12345-create-domain-20240101",
    email="user@example.com",
    domain="example.com",
    reason="User requested removal",
    expires_at=datetime.datetime.fromisoformat("2024-12-25T10:30:00+00:00"),
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — Email address to suppress
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `datetime.datetime` — When the suppression expires (RFC3339 format)
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

Optional idempotency key for safe request retries. Must be a unique string for each logical request.
An identical request with a completed stored outcome returns the original status and body. An in-progress
execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
so successful encrypted replay responses for those operations expire after 5 minutes.
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[str]` — Domain for which to suppress the email
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` — Reason for suppression
    
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

<details><summary><code>client.suppressions.<a href="src/fern/suppressions/client.py">delete_suppression</a>(...) -> SuccessResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes suppressions for an email address

**Query Parameters:**
- `email`: Required email address to delete from suppression list
- `domain`: Optional domain filter to delete suppressions for specific domain only
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.suppressions.delete_suppression(
    account_id="account_id",
    email="email",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — Email address
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[str]` — Optional domain filter
    
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

<details><summary><code>client.suppressions.<a href="src/fern/suppressions/client.py">delete_all_suppressions</a>(...) -> SuccessResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes all suppressions for the account

**Query Parameters:**
- `domain`: Optional domain filter to delete suppressions for specific domain only
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.suppressions.delete_all_suppressions(
    account_id="account_id",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[str]` — Optional domain filter
    
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

## Routes
<details><summary><code>client.routes.<a href="src/fern/routes/client.py">get_routes</a>(...) -> PaginatedRoutesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of routes for the account. A domain-scoped key must
provide the matching `domain` query parameter; the global read role can
list without that filter.
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.routes.get_routes(
    account_id="account_id",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[str]` — Domain to filter routes by. Required when using a domain-scoped routes:read:{domain} API key.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return (1-100)
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Pagination cursor for the previous page.
    
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

<details><summary><code>client.routes.<a href="src/fern/routes/client.py">create_route</a>(...) -> CreatedRoute</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new route for inbound email routing. Authorization uses the
domain in `recipient`: the global write role or its matching
domain-specific write role is sufficient.
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.routes.create_route(
    account_id="account_id",
    idempotency_key="user-12345-create-domain-20240101",
    name="Support Route",
    url="https://example.com/webhook",
    recipient="support@example.com",
    enabled=True,
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Route name
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — Webhook URL for the route
    
</dd>
</dl>

<dl>
<dd>

**recipient:** `str` — Recipient filter
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

Optional idempotency key for safe request retries. Must be a unique string for each logical request.
An identical request with a completed stored outcome returns the original status and body. An in-progress
execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
so successful encrypted replay responses for those operations expire after 5 minutes.
    
</dd>
</dl>

<dl>
<dd>

**attachments:** `typing.Optional[bool]` — Whether to include attachments in webhooks
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[bool]` — Whether to include headers in webhooks
    
</dd>
</dl>

<dl>
<dd>

**group_by_message_id:** `typing.Optional[bool]` — Whether to group by message ID
    
</dd>
</dl>

<dl>
<dd>

**strip_replies:** `typing.Optional[bool]` — Whether to strip reply content
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the route is enabled
    
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

<details><summary><code>client.routes.<a href="src/fern/routes/client.py">get_route</a>(...) -> Route</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a specific route by ID. Access requires the global read role or
a read role matching the route's recipient domain.
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.routes.get_route(
    account_id="account_id",
    route_id="route_id",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**route_id:** `str` — Route ID
    
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

<details><summary><code>client.routes.<a href="src/fern/routes/client.py">update_route</a>(...) -> Route</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing route. A domain-scoped key must authorize the
existing recipient domain and, when `recipient` changes, the new domain;
`routes:write:all` satisfies both checks.
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.routes.update_route(
    account_id="account_id",
    route_id="route_id",
    name="Updated Support Route",
    enabled=False,
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**route_id:** `str` — Route ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Route name
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — Webhook URL for the route
    
</dd>
</dl>

<dl>
<dd>

**recipient:** `typing.Optional[str]` — Recipient filter
    
</dd>
</dl>

<dl>
<dd>

**attachments:** `typing.Optional[bool]` — Whether to include attachments in webhooks
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[bool]` — Whether to include headers in webhooks
    
</dd>
</dl>

<dl>
<dd>

**group_by_message_id:** `typing.Optional[bool]` — Whether to group by message ID
    
</dd>
</dl>

<dl>
<dd>

**strip_replies:** `typing.Optional[bool]` — Whether to strip reply content
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the route is enabled
    
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

<details><summary><code>client.routes.<a href="src/fern/routes/client.py">delete_route</a>(...) -> SuccessResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a route. Access requires the global delete role or a delete role
matching the route's recipient domain.
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.routes.delete_route(
    account_id="account_id",
    route_id="route_id",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**route_id:** `str` — Route ID
    
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

## Webhooks
<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">get_webhooks</a>(...) -> PaginatedWebhooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of webhooks for the account

The global read role sees all webhooks. Domain-scoped read roles return
only webhooks associated with at least one authorized domain.

**Query Parameters:**
- `enabled`: Filter by enabled status
- Event filters: `on_reception`, `on_delivered`, `on_transient_error`, `on_failed`, `on_bounced`, `on_suppressed`, `on_opened`, `on_clicked`, `on_suppression_created`, `on_dns_error`
- `limit`: Maximum number of items to return (1-100, default: 100)
- `after`: Pagination cursor for the next page
- `before`: Pagination cursor for the previous page
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.get_webhooks(
    account_id="account_id",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Filter by enabled status
    
</dd>
</dl>

<dl>
<dd>

**on_reception:** `typing.Optional[bool]` — Filter by reception event trigger
    
</dd>
</dl>

<dl>
<dd>

**on_delivered:** `typing.Optional[bool]` — Filter by delivery event trigger
    
</dd>
</dl>

<dl>
<dd>

**on_transient_error:** `typing.Optional[bool]` — Filter by transient error event trigger
    
</dd>
</dl>

<dl>
<dd>

**on_failed:** `typing.Optional[bool]` — Filter by failure event trigger
    
</dd>
</dl>

<dl>
<dd>

**on_bounced:** `typing.Optional[bool]` — Filter by bounce event trigger
    
</dd>
</dl>

<dl>
<dd>

**on_suppressed:** `typing.Optional[bool]` — Filter by suppression event trigger
    
</dd>
</dl>

<dl>
<dd>

**on_opened:** `typing.Optional[bool]` — Filter by open event trigger
    
</dd>
</dl>

<dl>
<dd>

**on_clicked:** `typing.Optional[bool]` — Filter by click event trigger
    
</dd>
</dl>

<dl>
<dd>

**on_suppression_created:** `typing.Optional[bool]` — Filter by suppression creation event trigger
    
</dd>
</dl>

<dl>
<dd>

**on_dns_error:** `typing.Optional[bool]` — Filter by DNS error event trigger
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return (1-100)
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Pagination cursor for the previous page.
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">create_webhook</a>(...) -> CreatedWebhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new webhook for event notifications. A `scoped` webhook
requires at least one domain and the key must have write permission for
every supplied domain. A `global` webhook requires
`webhooks:write:all`; supplied domains are accepted but ignored, and
the response contains `domains: []`.
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
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.webhooks import CreateWebhookRequestScope

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.create_webhook(
    account_id="account_id",
    idempotency_key="user-12345-create-domain-20240101",
    name="Delivery Webhook",
    url="https://example.com/webhook",
    enabled=True,
    on_delivered=True,
    scope=CreateWebhookRequestScope.GLOBAL,
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Webhook name
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — Webhook URL
    
</dd>
</dl>

<dl>
<dd>

**scope:** `CreateWebhookRequestScope` — Webhook scope
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

Optional idempotency key for safe request retries. Must be a unique string for each logical request.
An identical request with a completed stored outcome returns the original status and body. An in-progress
execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
so successful encrypted replay responses for those operations expire after 5 minutes.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the webhook is enabled
    
</dd>
</dl>

<dl>
<dd>

**on_reception:** `typing.Optional[bool]` — Trigger on message reception
    
</dd>
</dl>

<dl>
<dd>

**on_delivered:** `typing.Optional[bool]` — Trigger on message delivery
    
</dd>
</dl>

<dl>
<dd>

**on_transient_error:** `typing.Optional[bool]` — Trigger on transient errors
    
</dd>
</dl>

<dl>
<dd>

**on_failed:** `typing.Optional[bool]` — Trigger on permanent failures
    
</dd>
</dl>

<dl>
<dd>

**on_bounced:** `typing.Optional[bool]` — Trigger on bounces
    
</dd>
</dl>

<dl>
<dd>

**on_suppressed:** `typing.Optional[bool]` — Trigger on suppressions
    
</dd>
</dl>

<dl>
<dd>

**on_opened:** `typing.Optional[bool]` — Trigger on opens
    
</dd>
</dl>

<dl>
<dd>

**on_clicked:** `typing.Optional[bool]` — Trigger on clicks
    
</dd>
</dl>

<dl>
<dd>

**on_suppression_created:** `typing.Optional[bool]` — Trigger on suppression creation
    
</dd>
</dl>

<dl>
<dd>

**on_dns_error:** `typing.Optional[bool]` — Trigger on DNS errors
    
</dd>
</dl>

<dl>
<dd>

**domains:** `typing.Optional[typing.List[str]]` 

For `scoped`, a non-empty array is required. For `global`, this may
be omitted, null, empty, or non-empty; supplied values are accepted
but ignored.
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">get_webhook</a>(...) -> Webhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a specific webhook by ID. Access requires the global read role
or a read role matching at least one associated domain.
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.get_webhook(
    account_id="account_id",
    webhook_id="webhook_id",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**webhook_id:** `str` — Webhook ID
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">update_webhook</a>(...) -> Webhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing webhook. Omitted or null fields are unchanged.
Omitted/null `domains` preserves associations, while `[]` clears the
associations of a resulting-scoped webhook. Moving from global to
scoped requires a non-empty `domains` array in the same request. Moving
to global clears associations and ignores supplied domains.

A domain-scoped key must be authorized for the existing webhook and
every newly supplied domain; changing to global requires
`webhooks:write:all`.

**Note:** The webhook secret is not updatable
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.update_webhook(
    account_id="account_id",
    webhook_id="webhook_id",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**webhook_id:** `str` — Webhook ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Webhook name
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — Webhook URL
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the webhook is enabled
    
</dd>
</dl>

<dl>
<dd>

**on_reception:** `typing.Optional[bool]` — Trigger on message reception
    
</dd>
</dl>

<dl>
<dd>

**on_delivered:** `typing.Optional[bool]` — Trigger on message delivery
    
</dd>
</dl>

<dl>
<dd>

**on_transient_error:** `typing.Optional[bool]` — Trigger on transient errors
    
</dd>
</dl>

<dl>
<dd>

**on_failed:** `typing.Optional[bool]` — Trigger on permanent failures
    
</dd>
</dl>

<dl>
<dd>

**on_bounced:** `typing.Optional[bool]` — Trigger on bounces
    
</dd>
</dl>

<dl>
<dd>

**on_suppressed:** `typing.Optional[bool]` — Trigger on suppressions
    
</dd>
</dl>

<dl>
<dd>

**on_opened:** `typing.Optional[bool]` — Trigger on opens
    
</dd>
</dl>

<dl>
<dd>

**on_clicked:** `typing.Optional[bool]` — Trigger on clicks
    
</dd>
</dl>

<dl>
<dd>

**on_suppression_created:** `typing.Optional[bool]` — Trigger on suppression creation
    
</dd>
</dl>

<dl>
<dd>

**on_dns_error:** `typing.Optional[bool]` — Trigger on DNS errors
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[UpdateWebhookRequestScope]` — Webhook scope. Omit or send null to keep the current scope.
    
</dd>
</dl>

<dl>
<dd>

**domains:** `typing.Optional[typing.List[str]]` 

Omit or send null to leave domain associations unchanged. An array
replaces associations when the resulting scope is `scoped`; `[]`
explicitly clears them. Changing a global webhook to `scoped`
requires a non-empty array in the same request and otherwise
returns HTTP 400. Changing to `global` clears all associations;
supplied domains are ignored when the resulting scope is global.
    
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">delete_webhook</a>(...) -> SuccessResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a webhook. Access requires the global delete role or a delete
role matching at least one associated domain.
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.delete_webhook(
    account_id="account_id",
    webhook_id="webhook_id",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**webhook_id:** `str` — Webhook ID
    
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

## SMTP Credentials
<details><summary><code>client.smtp_credentials.<a href="src/fern/smtp_credentials/client.py">get_smtp_credentials</a>(...) -> PaginatedSmtpCredentialsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of SMTP credentials for the account. The global read role
sees all credentials; domain-scoped roles return credentials associated
with at least one authorized domain.
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.smtp_credentials.get_smtp_credentials(
    account_id="account_id",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return (1-100)
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Pagination cursor for the previous page.
    
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

<details><summary><code>client.smtp_credentials.<a href="src/fern/smtp_credentials/client.py">create_smtp_credential</a>(...) -> CreatedSmtpCredential</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new SMTP credential for SMTP authentication. A `scoped`
credential requires at least one domain and the key must have write
permission for every supplied domain. A `global` credential requires
`smtp-credentials:write:all`; supplied domains are accepted but ignored,
and the response contains `domains: []`. SMTP credentials have no
update endpoint.
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
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.smtp_credentials import CreateSmtpCredentialRequestScope

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.smtp_credentials.create_smtp_credential(
    account_id="account_id",
    idempotency_key="user-12345-create-domain-20240101",
    name="Production SMTP",
    scope=CreateSmtpCredentialRequestScope.GLOBAL,
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Credential name
    
</dd>
</dl>

<dl>
<dd>

**scope:** `CreateSmtpCredentialRequestScope` — Credential scope - "global" or "scoped"
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

Optional idempotency key for safe request retries. Must be a unique string for each logical request.
An identical request with a completed stored outcome returns the original status and body. An in-progress
execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
so successful encrypted replay responses for those operations expire after 5 minutes.
    
</dd>
</dl>

<dl>
<dd>

**sandbox:** `typing.Optional[bool]` — Whether this is a sandbox credential
    
</dd>
</dl>

<dl>
<dd>

**domains:** `typing.Optional[typing.List[str]]` 

For `scoped`, a non-empty array is required. For `global`, this may
be omitted, null, empty, or non-empty; supplied values are accepted
but ignored.
    
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

<details><summary><code>client.smtp_credentials.<a href="src/fern/smtp_credentials/client.py">get_smtp_credential</a>(...) -> SmtpCredential</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a specific SMTP credential by ID. Access requires the global
read role or a read role matching at least one associated domain.
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.smtp_credentials.get_smtp_credential(
    account_id="account_id",
    smtp_credential_id="smtp_credential_id",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**smtp_credential_id:** `str` — SMTP Credential ID
    
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

<details><summary><code>client.smtp_credentials.<a href="src/fern/smtp_credentials/client.py">delete_smtp_credential</a>(...) -> SuccessResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an SMTP credential. Access requires the global delete role or a
delete role matching at least one associated domain.
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.smtp_credentials.delete_smtp_credential(
    account_id="account_id",
    smtp_credential_id="smtp_credential_id",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**smtp_credential_id:** `str` — SMTP Credential ID
    
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

## Statistics
<details><summary><code>client.statistics.<a href="src/fern/statistics/client.py">get_deliverability_statistics</a>(...) -> DeliverabilityStatisticsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns transactional deliverability statistics grouped by status

The global statistics role can query all sender domains. A
domain-scoped key is limited to authorized domains and must authorize
every comma-separated value supplied in `sender_domain`.

**Query Parameters:**
- `from_time`: Filter statistics after this date (RFC3339 format)
- `to_time`: Filter statistics before this date (RFC3339 format)
- `sender_domain`: Filter by sender domain
- `recipient_domains`: Filter by recipient domain
- `tags`: Filter by tags (comma-separated)
- `group_by`: Group by time period (hour, day, week, month)
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.statistics.get_deliverability_statistics(
    account_id="account_id",
    recipient_domains="gmail.com,googlemail.com",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**from_time:** `typing.Optional[datetime.datetime]` — Filter statistics after this datetime (RFC3339 format)
    
</dd>
</dl>

<dl>
<dd>

**to_time:** `typing.Optional[datetime.datetime]` — Filter statistics before this datetime (RFC3339 format)
    
</dd>
</dl>

<dl>
<dd>

**sender_domain:** `typing.Optional[str]` — Comma-separated sender domains; the key must authorize every requested domain
    
</dd>
</dl>

<dl>
<dd>

**recipient_domains:** `typing.Optional[str]` — Filter by a comma separated list of recipient domains
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[str]` — Filter by tags (comma-separated)
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `typing.Optional[GetDeliverabilityStatisticsRequestGroupBy]` — Group by time period
    
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

<details><summary><code>client.statistics.<a href="src/fern/statistics/client.py">get_bounce_statistics</a>(...) -> BounceStatisticsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns transactional bounce statistics grouped by classification

The global statistics role can query all sender domains. A
domain-scoped key is limited to authorized domains and must authorize
every comma-separated value supplied in `sender_domain`.

**Query Parameters:**
- `from_time`: Filter statistics after this date (RFC3339 format)
- `to_time`: Filter statistics before this date (RFC3339 format)
- `sender_domain`: Filter by sender domain
- `recipient_domains`: Filter by recipient domain
- `tags`: Filter by tags (comma-separated)
- `group_by`: Group by time period (hour, day, week, month)
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.statistics.get_bounce_statistics(
    account_id="account_id",
    recipient_domains="gmail.com,googlemail.com",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**from_time:** `typing.Optional[datetime.datetime]` — Filter statistics after this datetime (RFC3339 format)
    
</dd>
</dl>

<dl>
<dd>

**to_time:** `typing.Optional[datetime.datetime]` — Filter statistics before this datetime (RFC3339 format)
    
</dd>
</dl>

<dl>
<dd>

**sender_domain:** `typing.Optional[str]` — Comma-separated sender domains; the key must authorize every requested domain
    
</dd>
</dl>

<dl>
<dd>

**recipient_domains:** `typing.Optional[str]` — Filter by a comma separated list of recipient domains
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[str]` — Filter by tags (comma-separated)
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `typing.Optional[GetBounceStatisticsRequestGroupBy]` — Group by time period
    
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

<details><summary><code>client.statistics.<a href="src/fern/statistics/client.py">get_delivery_time_statistics</a>(...) -> DeliveryTimeStatisticsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns transactional delivery time statistics grouped by recipient domain

The global statistics role can query all sender domains. A
domain-scoped key is limited to authorized domains and must authorize
every comma-separated value supplied in `sender_domain`.

**Query Parameters:**
- `from_time`: Filter statistics after this date (RFC3339 format)
- `to_time`: Filter statistics before this date (RFC3339 format)
- `sender_domain`: Filter by sender domain
- `recipient_domains`: Filter by recipient domains
- `tags`: Filter by tags (comma-separated)
- `group_by`: Group by time period (hour, day, week, month)
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
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.statistics.get_delivery_time_statistics(
    account_id="account_id",
    recipient_domains="gmail.com,googlemail.com",
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

**account_id:** `str` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**from_time:** `typing.Optional[datetime.datetime]` — Filter statistics after this datetime (RFC3339 format)
    
</dd>
</dl>

<dl>
<dd>

**to_time:** `typing.Optional[datetime.datetime]` — Filter statistics before this datetime (RFC3339 format)
    
</dd>
</dl>

<dl>
<dd>

**sender_domain:** `typing.Optional[str]` — Comma-separated sender domains; the key must authorize every requested domain
    
</dd>
</dl>

<dl>
<dd>

**recipient_domains:** `typing.Optional[str]` — Filter by a comma separated list of recipient domains
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[str]` — Filter by tags (comma-separated)
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `typing.Optional[GetDeliveryTimeStatisticsRequestGroupBy]` — Group by time period
    
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

