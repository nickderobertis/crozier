# Reference
## authorization
<details><summary><code>client.authorization.<a href="src/fern/authorization/client.py#L31-L68">login</a>(...) -> LoginResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets an API key from username and password
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

client.authorization.login(
    password="test-password",
    username="name@example.com",
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

**password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` 
    
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

<details><summary><code>client.authorization.<a href="src/fern/authorization/client.py#L70-L123">o_auth2client_credentials</a>(...) -> OAuth2TokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exchanges client credentials for an access token. Parameters must be sent as application/x-www-form-urlencoded.
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
from fern.authorization import OAuth2ClientCredentialsRequestGrantType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authorization.o_auth2client_credentials(
    client_id="d37ae69a-c739-44e9-9722-81a4cb7aeb67",
    client_secret="2a40832d028a3e24a717f023fdcaa8ab452dd12223d472aff38223ffdfeee4bf",
    grant_type=OAuth2ClientCredentialsRequestGrantType.CLIENT_CREDENTIALS,
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

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**grant_type:** `OAuth2ClientCredentialsRequestGrantType` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Space-delimited scopes.
    
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

## billing_account
<details><summary><code>client.billing_account.<a href="src/fern/billing_account/client.py#L28-L54">get_billing_accounts</a>() -> GetBillingAccountsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Billing Accounts accessible by the api_key
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

client.billing_account.get_billing_accounts()

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

<details><summary><code>client.billing_account.<a href="src/fern/billing_account/client.py#L56-L86">get_billing_account</a>(...) -> GetBillingAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Billing Account Information
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

client.billing_account.get_billing_account(
    billing_account_uid="00000000-0000-0000-000000000001",
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

**billing_account_uid:** `str` 
    
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

<details><summary><code>client.billing_account.<a href="src/fern/billing_account/client.py#L88-L131">get_billing_account_balance_history</a>(...) -> GetBillingAccountBalanceHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Billing Account Balance history
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

client.billing_account.get_billing_account_balance_history(
    billing_account_uid="00000000-0000-0000-000000000001",
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

**billing_account_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[int]` — Start date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — End date for filtering results, specified as a Unix timestamp
    
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

## Description
<details><summary><code>client.description.<a href="src/fern/description/client.py#L30-L56">list_global_descriptions</a>() -> DescriptionRecordList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List metadata for all global description records.
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

client.description.list_global_descriptions()

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

<details><summary><code>client.description.<a href="src/fern/description/client.py#L58-L88">get_global_description</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a global description record. Returns the raw content with its stored Content-Type.
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

client.description.get_global_description(
    description_name="descriptionName",
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

**description_name:** `str` 
    
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

<details><summary><code>client.description.<a href="src/fern/description/client.py#L90-L117">set_global_description</a>(...) -> DescriptionRecord</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace a global description record, Blues staff only (up to 10MB). The request Content-Type is stored and returned on GET; when omitted it is detected (JSON or text).
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
client.description.set_global_description(...)
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

**description_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — The description content (up to 10MB). The request Content-Type is stored and returned on GET; when omitted it is detected (JSON or text).
    
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

<details><summary><code>client.description.<a href="src/fern/description/client.py#L119-L148">delete_global_description</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a global description record by name (Blues staff only).
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

client.description.delete_global_description(
    description_name="_health.qo",
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

**description_name:** `str` 
    
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

<details><summary><code>client.description.<a href="src/fern/description/client.py#L150-L180">list_project_descriptions</a>(...) -> DescriptionRecordList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List metadata for all description records in a project.
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

client.description.list_project_descriptions(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
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

<details><summary><code>client.description.<a href="src/fern/description/client.py#L182-L221">get_project_description</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a project description record. Returns the raw content with its stored Content-Type.
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

client.description.get_project_description(
    project_or_product_uid="projectOrProductUID",
    description_name="descriptionName",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description_name:** `str` 
    
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

<details><summary><code>client.description.<a href="src/fern/description/client.py#L223-L253">set_project_description</a>(...) -> DescriptionRecord</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or replace a project description record (up to 10MB). The request Content-Type is stored and returned on GET; when omitted it is detected (JSON or text).
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
client.description.set_project_description(...)
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — The description content (up to 10MB). The request Content-Type is stored and returned on GET; when omitted it is detected (JSON or text).
    
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

<details><summary><code>client.description.<a href="src/fern/description/client.py#L255-L293">delete_project_description</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a project description record by name.
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

client.description.delete_project_description(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    description_name="_health.qo",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description_name:** `str` 
    
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

## organization
<details><summary><code>client.organization.<a href="src/fern/organization/client.py#L28-L52">get_organizations</a>() -> GetOrganizationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Organizations accessible by the api_key
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

client.organization.get_organizations()

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

<details><summary><code>client.organization.<a href="src/fern/organization/client.py#L54-L84">get_organization</a>(...) -> GetOrganizationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Organization Information
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

client.organization.get_organization(
    organization_uid="00000000-0000-0000-000000000001",
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

**organization_uid:** `str` 
    
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

<details><summary><code>client.organization.<a href="src/fern/organization/client.py#L86-L129">get_organization_balance_history</a>(...) -> GetOrganizationBalanceHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Organization Balance history
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

client.organization.get_organization_balance_history(
    organization_uid="00000000-0000-0000-000000000001",
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

**organization_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[int]` — Start date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — End date for filtering results, specified as a Unix timestamp
    
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

## device
<details><summary><code>client.device.<a href="src/fern/device/client.py#L48-L92">get_device_environment_variables_by_pin</a>(...) -> GetDeviceEnvironmentVariablesByPinResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get environment variables of a device with device pin authorization
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

client.device.get_device_environment_variables_by_pin(
    product_uid="com.blues.bridge:sensors",
    device_uid="dev:000000000000000",
    auth_token="X-Auth-Token",
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

**product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**auth_token:** `str` — For accessing endpoints by Device pin.
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L94-L151">set_device_environment_variables_by_pin</a>(...) -> EnvironmentVariables</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set environment variables of a device with device pin authorization
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

client.device.set_device_environment_variables_by_pin(
    product_uid="com.blues.bridge:sensors",
    device_uid="dev:000000000000000",
    auth_token="X-Auth-Token",
    environment_variables={
        "key": "value"
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

**product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**auth_token:** `str` — For accessing endpoints by Device pin.
    
</dd>
</dl>

<dl>
<dd>

**request:** `EnvironmentVariables` 
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L153-L240">get_devices</a>(...) -> GetDevicesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Devices of a Project
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

client.device.get_devices(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A Device UID.
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Tag filter
    
</dd>
</dl>

<dl>
<dd>

**serial_number:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Serial number filter
    
</dd>
</dl>

<dl>
<dd>

**fleet_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**notecard_firmware:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Firmware version filter
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Location filter
    
</dd>
</dl>

<dl>
<dd>

**host_firmware:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Host firmware filter
    
</dd>
</dl>

<dl>
<dd>

**product_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**sku:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — SKU filter
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L242-L275">get_device</a>(...) -> Device</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Device
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

client.device.get_device(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L277-L309">delete_device</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Device
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

client.device.delete_device(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L311-L343">disable_device</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disable Device
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

client.device.disable_device(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L345-L377">enable_device</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enable Device
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

client.device.enable_device(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L379-L412">get_device_environment_hierarchy</a>(...) -> EnvTreeJsonNode</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.device.get_device_environment_hierarchy(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L414-L449">get_device_environment_variables</a>(...) -> GetDeviceEnvironmentVariablesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get environment variables of a device
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

client.device.get_device_environment_variables(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L451-L502">set_device_environment_variables</a>(...) -> EnvironmentVariables</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set environment variables of a device
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

client.device.set_device_environment_variables(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
    environment_variables={
        "key": "value"
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `EnvironmentVariables` 
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L504-L548">delete_device_environment_variable</a>(...) -> EnvironmentVariables</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete environment variable of a device
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

client.device.delete_device_environment_variable(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
    key="key",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — The environment variable key to delete.
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L550-L597">list_notefiles</a>(...) -> NotefileList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists .qi and .db files for the device
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

client.device.list_notefiles(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**files:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — One or more files to obtain change information from.
    
</dd>
</dl>

<dl>
<dd>

**pending:** `typing.Optional[bool]` — show only files that are pending sync to the Notecard
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L599-L641">delete_notefiles</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes Notefiles and the Notes they contain.
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

client.device.delete_notefiles(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**files:** `typing.Optional[typing.List[str]]` — Name of notefiles to delete
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L643-L701">get_device_health_log</a>(...) -> GetDeviceHealthLogResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Device Health Log
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

client.device.get_device_health_log(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[int]` — Start date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — End date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**log_type:** `typing.Optional[typing.Union[GetDeviceHealthLogRequestLogTypeItem, typing.Sequence[GetDeviceHealthLogRequestLogTypeItem]]]` — Return only specified log types
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L703-L754">get_device_journeys</a>(...) -> GetDeviceJourneysResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the list of journeys for a device, derived from events whose body contains `journey` and `jcount` fields. Returns journey metadata only (no event payloads). Capped at 100 most recent journeys; `has_more` is true when the cap is hit.
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

client.device.get_device_journeys(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[int]` — Start date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — End date for filtering results, specified as a Unix timestamp
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L756-L811">get_device_journey</a>(...) -> GetDeviceJourneyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single journey for a device along with its events. The events array is paginated via `pageSize` / `pageNum`; use `journey.has_more` to detect additional pages.
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

client.device.get_device_journey(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
    journey_id=1000000,
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**journey_id:** `int` — Identifier of the journey, taken from the numeric `journey` field in the event body (a Unix timestamp marking the start of the journey).
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` 
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L813-L848">get_device_latest_events</a>(...) -> GetDeviceLatestEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Device Latest Events
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

client.device.get_device_latest_events(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L850-L892">create_notefile</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an empty Notefile on the device.
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

client.device.create_notefile(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
    notefile_id="notefileID",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**notefile_id:** `str` 
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L894-L955">get_notefile</a>(...) -> GetNotefileResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

For .qi files, returns the queued up notes.  For .db files, returns all notes in the notefile
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

client.device.get_notefile(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
    notefile_id="notefileID",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**notefile_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**max:** `typing.Optional[int]` — The maximum number of Notes to return in the request.
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` — true to return deleted notes.
    
</dd>
</dl>

<dl>
<dd>

**delete:** `typing.Optional[bool]` — true to delete the notes returned by the request.
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L957-L1007">add_qi_note</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a Note to a Notefile, creating the Notefile if it doesn't yet exist.
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

client.device.add_qi_note(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
    notefile_id="notefileID",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**notefile_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `NoteInput` 
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L1009-L1070">get_db_note</a>(...) -> GetDbNoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a note from a .db or .qi notefile
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

client.device.get_db_note(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
    notefile_id="notefileID",
    note_id="noteID",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**notefile_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**delete:** `typing.Optional[bool]` — Whether to delete the note from the DB notefile
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` — Whether to return deleted notes
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L1072-L1132">add_db_note</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a Note to a .db notefile.  if noteID is '-' then payload is ignored and empty notefile is created
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

client.device.add_db_note(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
    notefile_id="notefileID",
    note_id="noteID",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**notefile_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `NoteInput` 
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L1134-L1194">update_db_note</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a note in a .db or .qi notefile
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

client.device.update_db_note(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
    notefile_id="notefileID",
    note_id="noteID",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**notefile_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `NoteInput` 
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L1196-L1242">delete_note</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a note from a .db or .qi notefile
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

client.device.delete_note(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
    notefile_id="notefileID",
    note_id="noteID",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**notefile_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**note_id:** `str` 
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L1244-L1279">get_device_plans</a>(...) -> GetDevicePlansResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Data Plans associated with the device, this include the primary sim, any external sim, as well as any satellite connections.
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

client.device.get_device_plans(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L1281-L1338">provision_device</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provision Device for a Project
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

client.device.provision_device(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
    product_uid="product_uid",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**product_uid:** `str` — The ProductUID that the device should use.
    
</dd>
</dl>

<dl>
<dd>

**device_sn:** `typing.Optional[str]` — The serial number to assign to the device.
    
</dd>
</dl>

<dl>
<dd>

**fleet_uids:** `typing.Optional[typing.List[str]]` — The fleetUIDs to provision the device to.
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L1340-L1375">get_device_public_key</a>(...) -> GetDevicePublicKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Device Public Key
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

client.device.get_device_public_key(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L1377-L1441">get_device_sessions</a>(...) -> GetDeviceSessionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Device Sessions
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

client.device.get_device_sessions(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[int]` — Start date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — End date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**first_sync:** `typing.Optional[bool]` — When true, filters results to only show first sync sessions
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L1443-L1485">signal_device</a>(...) -> SignalDeviceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a signal from Notehub to a Notecard.
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

client.device.signal_device(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L1487-L1528">get_device_public_keys</a>(...) -> GetDevicePublicKeysResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Device Public Keys of a Project
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

client.device.get_device_public_keys(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` 
    
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

<details><summary><code>client.device.<a href="src/fern/device/client.py#L1530-L1618">get_fleet_devices</a>(...) -> GetFleetDevicesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Devices of a Fleet within a Project
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

client.device.get_fleet_devices(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    fleet_uid="fleetUID",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fleet_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A Device UID.
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Tag filter
    
</dd>
</dl>

<dl>
<dd>

**serial_number:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Serial number filter
    
</dd>
</dl>

<dl>
<dd>

**notecard_firmware:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Firmware version filter
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Location filter
    
</dd>
</dl>

<dl>
<dd>

**host_firmware:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Host firmware filter
    
</dd>
</dl>

<dl>
<dd>

**product_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**sku:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — SKU filter
    
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

## webhook
<details><summary><code>client.webhook.<a href="src/fern/webhook/client.py#L30-L76">create_legacy_webhook_event</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Legacy endpoint for sending an event from a webhook, associated with the given device (provisioning it if necessary). The request body is a Note-shaped object containing the notefile name, body, and optional payload.
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

client.webhook.create_legacy_webhook_event(
    product_uid="com.blues.bridge:sensors",
    device_uid="dev:000000000000000",
    request={
        "body": {"key": "value"},
        "file": "data.qo",
        "payload": "SGVsbG8sIFdvcmxkIQ=="
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

**product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
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

<details><summary><code>client.webhook.<a href="src/fern/webhook/client.py#L78-L120">update_legacy_webhook_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Legacy endpoint for opening or updating a webhook session for the given device (provisioning the device if necessary). Used by external services that need to maintain a callable session against a device behind a webhook.
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

client.webhook.update_legacy_webhook_session(
    product_uid="com.blues.bridge:sensors",
    device_uid="dev:000000000000000",
    request={
        "key": "value"
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

**product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
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

<details><summary><code>client.webhook.<a href="src/fern/webhook/client.py#L122-L169">create_webhook_device_event_by_product</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sends an event to be processed by the specified webhook, addressed by productUID, associated with the given device (provisioning it if necessary). The entire request body becomes the event body. The webhook's configured JSONata transform, if any, is applied before routing.
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

client.webhook.create_webhook_device_event_by_product(
    product_uid="com.blues.bridge:sensors",
    webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
    device_uid="dev:000000000000000",
    request={
        "key": "value"
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

**product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_uid:** `str` — Webhook UID
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
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

<details><summary><code>client.webhook.<a href="src/fern/webhook/client.py#L171-L214">create_webhook_event_by_product</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sends an event to be processed by the specified webhook, addressed by productUID. The entire request body becomes the event body. The webhook's configured JSONata transform, if any, is applied before routing. The event is not associated with a specific device.
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

client.webhook.create_webhook_event_by_product(
    product_uid="com.blues.bridge:sensors",
    webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
    request={
        "key": "value"
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

**product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_uid:** `str` — Webhook UID
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
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

<details><summary><code>client.webhook.<a href="src/fern/webhook/client.py#L216-L252">get_webhook_settings_by_product</a>(...) -> WebhookSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the configuration settings for the specified webhook, addressed by productUID.
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

client.webhook.get_webhook_settings_by_product(
    product_uid="com.blues.bridge:sensors",
    webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
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

**product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_uid:** `str` — Webhook UID
    
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

<details><summary><code>client.webhook.<a href="src/fern/webhook/client.py#L254-L307">update_webhook_settings_by_product</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the configuration settings for the specified webhook, addressed by productUID. Update body will completely replace the existing settings.
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

client.webhook.update_webhook_settings_by_product(
    product_uid="com.blues.bridge:sensors",
    webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
    disabled=False,
    transform="{\"device\":body.end_device_ids.dev_eui,\"sn\":body.end_device_ids.device_id,\"body\":body.uplink_message.decoded_payload,\"details\":body}",
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

**product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_uid:** `str` — Webhook UID
    
</dd>
</dl>

<dl>
<dd>

**request:** `WebhookSettings` 
    
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

<details><summary><code>client.webhook.<a href="src/fern/webhook/client.py#L309-L339">get_webhooks</a>(...) -> GetWebhooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all webhooks for the specified project
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

client.webhook.get_webhooks(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
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

<details><summary><code>client.webhook.<a href="src/fern/webhook/client.py#L341-L375">get_webhook</a>(...) -> WebhookSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the configuration settings for the specified webhook
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

client.webhook.get_webhook(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_uid:** `str` — Webhook UID
    
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

<details><summary><code>client.webhook.<a href="src/fern/webhook/client.py#L377-L433">create_webhook</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a webhook for the specified product with the given name. The name | must be unique within the project.
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

client.webhook.create_webhook(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_uid:** `str` — Webhook UID
    
</dd>
</dl>

<dl>
<dd>

**request:** `WebhookSettings` 
    
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

<details><summary><code>client.webhook.<a href="src/fern/webhook/client.py#L435-L493">update_webhook</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the configuration settings for the specified webhook. | Webhook will be created if it does not exist. Update body will completely replace the existing settings.
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

client.webhook.update_webhook(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
    disabled=False,
    transform="{\"device\":body.end_device_ids.dev_eui,\"sn\":body.end_device_ids.device_id,\"body\":body.uplink_message.decoded_payload,\"details\":body}",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_uid:** `str` — Webhook UID
    
</dd>
</dl>

<dl>
<dd>

**request:** `WebhookSettings` 
    
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

<details><summary><code>client.webhook.<a href="src/fern/webhook/client.py#L495-L530">delete_webhook</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the specified webhook
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

client.webhook.delete_webhook(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_uid:** `str` — Webhook UID
    
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

## external devices
<details><summary><code>client.external_devices.<a href="src/fern/external_devices/client.py#L30-L379">create_event_ext_device</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an event using specified webhook
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

client.external_devices.create_event_ext_device(
    product_uid="com.blues.bridge:sensors",
    device_uid="dev:000000000000000",
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

**product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `Event` 
    
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

<details><summary><code>client.external_devices.<a href="src/fern/external_devices/client.py#L381-L670">ext_device_session_close</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Closes the session for the specified device if open
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

client.external_devices.ext_device_session_close(
    product_uid="com.blues.bridge:sensors",
    device_uid="dev:000000000000000",
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

**product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DeviceSession` 
    
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

<details><summary><code>client.external_devices.<a href="src/fern/external_devices/client.py#L672-L961">ext_device_session_open</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a Session for the specified device.  | If a session is currently open it will be closed and a new one opened.
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

client.external_devices.ext_device_session_open(
    product_uid="com.blues.bridge:sensors",
    device_uid="dev:000000000000000",
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

**product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DeviceSession` 
    
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

## project
<details><summary><code>client.project.<a href="src/fern/project/client.py#L67-L97">get_project_by_product</a>(...) -> Project</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a Project by ProductUID
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

client.project.get_project_by_product(
    product_uid="com.blues.airnote",
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

**product_uid:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L99-L123">get_projects</a>() -> GetProjectsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Projects accessible by the api_key
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

client.project.get_projects()

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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L125-L162">create_project</a>(...) -> Project</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a Project
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

client.project.create_project(
    billing_account_uid="billing_account_uid",
    label="label",
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

**billing_account_uid:** `str` — The billing account UID for the project. The caller of the API must be able to create projects within the billing account, otherwise an error will be returned.
    
</dd>
</dl>

<dl>
<dd>

**label:** `str` — The label for the project.
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L164-L194">get_project</a>(...) -> Project</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a Project by ProjectUID
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

client.project.get_project(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L196-L225">delete_project</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a Project by ProjectUID
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

client.project.delete_project(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L227-L258">get_aws_role_config</a>(...) -> AwsRoleConfig</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the AWS Account ID and External ID needed to configure an IAM role
trust policy for role-based authentication on AWS routes.
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

client.project.get_aws_role_config(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L260-L318">clone_project</a>(...) -> Project</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Clone a Project
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

client.project.clone_project(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    billing_account_uid="billing_account_uid",
    label="label",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**billing_account_uid:** `str` — The billing account UID for the project. The caller of the API must be able to create projects within the billing account, otherwise an error will be returned.
    
</dd>
</dl>

<dl>
<dd>

**label:** `str` — The label for the project.
    
</dd>
</dl>

<dl>
<dd>

**disable_clone_fleets:** `typing.Optional[bool]` — Whether to disallow the cloning of the fleets from the parent project.  Default is false if not specified.
    
</dd>
</dl>

<dl>
<dd>

**disable_clone_routes:** `typing.Optional[bool]` — Whether to disallow the cloning of the routes from the parent project.  Default is false if not specified.
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L320-L365">get_device_dfu_history</a>(...) -> DeviceDfuHistory</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get device DFU history for host or Notecard firmware
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
from fern.project import GetDeviceDfuHistoryRequestFirmwareType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.project.get_device_dfu_history(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
    firmware_type=GetDeviceDfuHistoryRequestFirmwareType.HOST,
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**firmware_type:** `GetDeviceDfuHistoryRequestFirmwareType` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L367-L412">get_device_dfu_status</a>(...) -> DeviceDfuStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get device DFU history for host or Notecard firmware
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
from fern.project import GetDeviceDfuStatusRequestFirmwareType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.project.get_device_dfu_status(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
    firmware_type=GetDeviceDfuStatusRequestFirmwareType.HOST,
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**firmware_type:** `GetDeviceDfuStatusRequestFirmwareType` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L414-L449">get_device_fleets</a>(...) -> GetDeviceFleetsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Device Fleets
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

client.project.get_device_fleets(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L451-L495">add_device_to_fleets</a>(...) -> AddDeviceToFleetsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add Device to Fleets
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

client.project.add_device_to_fleets(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
    fleet_uids=[
        "fleet_uids"
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fleet_uids:** `typing.List[str]` — The fleetUIDs to add to the device.
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L497-L541">delete_device_from_fleets</a>(...) -> DeleteDeviceFromFleetsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove Device from Fleets
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

client.project.delete_device_from_fleets(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    device_uid="dev:000000000000000",
    fleet_uids=[
        "fleet_uids"
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fleet_uids:** `typing.List[str]` — The fleetUIDs to remove from the device.
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L543-L641">perform_dfu_action</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update/cancel host or notecard firmware updates
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
from fern.project import PerformDfuActionRequestFirmwareType, PerformDfuActionRequestAction

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.project.perform_dfu_action(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    firmware_type=PerformDfuActionRequestFirmwareType.HOST,
    action=PerformDfuActionRequestAction.UPDATE,
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**firmware_type:** `PerformDfuActionRequestFirmwareType` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `PerformDfuActionRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A Device UID.
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Tag filter
    
</dd>
</dl>

<dl>
<dd>

**serial_number:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Serial number filter
    
</dd>
</dl>

<dl>
<dd>

**fleet_uid:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**notecard_firmware:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Firmware version filter
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Location filter
    
</dd>
</dl>

<dl>
<dd>

**host_firmware:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Host firmware filter
    
</dd>
</dl>

<dl>
<dd>

**product_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**sku:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — SKU filter
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` — The name of the firmware file
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L643-L745">get_devices_dfu_history</a>(...) -> DeviceDfuHistoryPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get host or Notecard DFU history for all devices that match the filter criteria
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
from fern.project import GetDevicesDfuHistoryRequestFirmwareType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.project.get_devices_dfu_history(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    firmware_type=GetDevicesDfuHistoryRequestFirmwareType.HOST,
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**firmware_type:** `GetDevicesDfuHistoryRequestFirmwareType` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetDevicesDfuHistoryRequestSortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetDevicesDfuHistoryRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A Device UID.
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Tag filter
    
</dd>
</dl>

<dl>
<dd>

**serial_number:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Serial number filter
    
</dd>
</dl>

<dl>
<dd>

**fleet_uid:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**notecard_firmware:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Firmware version filter
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Location filter
    
</dd>
</dl>

<dl>
<dd>

**host_firmware:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Host firmware filter
    
</dd>
</dl>

<dl>
<dd>

**product_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**sku:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — SKU filter
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L747-L849">get_devices_dfu_status</a>(...) -> DeviceDfuStatusPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get host or Notecard DFU history for all devices that match the filter criteria
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
from fern.project import GetDevicesDfuStatusRequestFirmwareType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.project.get_devices_dfu_status(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    firmware_type=GetDevicesDfuStatusRequestFirmwareType.HOST,
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**firmware_type:** `GetDevicesDfuStatusRequestFirmwareType` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetDevicesDfuStatusRequestSortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetDevicesDfuStatusRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A Device UID.
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Tag filter
    
</dd>
</dl>

<dl>
<dd>

**serial_number:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Serial number filter
    
</dd>
</dl>

<dl>
<dd>

**fleet_uid:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**notecard_firmware:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Firmware version filter
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Location filter
    
</dd>
</dl>

<dl>
<dd>

**host_firmware:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Host firmware filter
    
</dd>
</dl>

<dl>
<dd>

**product_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**sku:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — SKU filter
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L851-L881">get_project_environment_hierarchy</a>(...) -> EnvTreeJsonNode</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.project.get_project_environment_hierarchy(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L883-L915">get_project_environment_variables</a>(...) -> EnvironmentVariables</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get environment variables of a project
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

client.project.get_project_environment_variables(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L917-L963">set_project_environment_variables</a>(...) -> EnvironmentVariables</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set environment variables of a project
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

client.project.set_project_environment_variables(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    environment_variables={
        "key": "value"
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `EnvironmentVariables` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L965-L1001">delete_project_environment_variable</a>(...) -> EnvironmentVariables</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an environment variable of a project by key
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

client.project.delete_project_environment_variable(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    key="key",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — The environment variable key to delete.
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1003-L1078">get_firmware_info</a>(...) -> typing.List[FirmwareInfo]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Available Firmware Information
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

client.project.get_firmware_info(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    filename="notecard-7.2.2.16518$20240410043100.bin",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**product:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**firmware_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**target:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**md5:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**unpublished:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetFirmwareInfoRequestSortBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetFirmwareInfoRequestSortOrder]` — Sort order (asc for ascending, desc for descending)
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1080-L1110">download_firmware</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download firmware binary
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
client.project.download_firmware(...)
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**firmware_type:** `DownloadFirmwareRequestFirmwareType` 
    
</dd>
</dl>

<dl>
<dd>

**filename:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1112-L1175">update_firmware</a>(...) -> FirmwareInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the metadata of an existing host firmware entry. The filename must be the full stored filename including the timestamp suffix (e.g. test$20260324190911.bin) as returned by the firmware upload or list endpoints.
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
from fern.project import UpdateFirmwareRequestFirmwareType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.project.update_firmware(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    firmware_type=UpdateFirmwareRequestFirmwareType.HOST,
    filename="filename",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**firmware_type:** `UpdateFirmwareRequestFirmwareType` 
    
</dd>
</dl>

<dl>
<dd>

**filename:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**info:** `typing.Optional[typing.Dict[str, typing.Any]]` — Arbitrary JSON metadata associated with this firmware entry.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Notes describing this firmware version.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — The firmware version string.
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1177-L1224">upload_firmware</a>(...) -> FirmwareInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload firmware binary
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
client.project.upload_firmware(...)
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**firmware_type:** `UploadFirmwareRequestFirmwareType` 
    
</dd>
</dl>

<dl>
<dd>

**filename:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — contents of the firmware binary
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Firmware version (optional). If not provided, the version will be extracted from firmware binary if available, otherwise left empty
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Optional notes describing what's different about this firmware version
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1226-L1270">delete_firmware</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a host firmware binary. The filename must be the full stored filename including the timestamp suffix (e.g. test$20260324190911.bin) as returned by the firmware upload or list endpoints.
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
from fern.project import DeleteFirmwareRequestFirmwareType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.project.delete_firmware(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    firmware_type=DeleteFirmwareRequestFirmwareType.HOST,
    filename="filename",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**firmware_type:** `DeleteFirmwareRequestFirmwareType` 
    
</dd>
</dl>

<dl>
<dd>

**filename:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1272-L1302">get_fleets</a>(...) -> GetFleetsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Project Fleets
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

client.project.get_fleets(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1304-L1357">create_fleet</a>(...) -> Fleet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Fleet
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

client.project.create_fleet(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connectivity_assurance:** `typing.Optional[FleetConnectivityAssurance]` 
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — The label, or name,  for the Fleet.
    
</dd>
</dl>

<dl>
<dd>

**smart_rule:** `typing.Optional[FleetRule]` 
    
</dd>
</dl>

<dl>
<dd>

**smart_rule_enabled:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1359-L1392">get_fleet</a>(...) -> Fleet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Fleet
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

client.project.get_fleet(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    fleet_uid="fleetUID",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fleet_uid:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1394-L1467">update_fleet</a>(...) -> Fleet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Fleet
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

client.project.update_fleet(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    fleet_uid="fleetUID",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fleet_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**add_devices:** `typing.Optional[typing.List[str]]` — List of DeviceUIDs to add to fleet
    
</dd>
</dl>

<dl>
<dd>

**connectivity_assurance:** `typing.Optional[FleetConnectivityAssurance]` 
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — The label for the Fleet.
    
</dd>
</dl>

<dl>
<dd>

**remove_devices:** `typing.Optional[typing.List[str]]` — List of DeviceUIDs to remove from fleet
    
</dd>
</dl>

<dl>
<dd>

**smart_rule:** `typing.Optional[FleetRule]` 
    
</dd>
</dl>

<dl>
<dd>

**smart_rule_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**watchdog_mins:** `typing.Optional[int]` — A watchdog timer is used to generate an event every N minutes of inactivity. 0 means no watchdog
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1469-L1501">delete_fleet</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Fleet
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

client.project.delete_fleet(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    fleet_uid="fleetUID",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fleet_uid:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1503-L1536">get_fleet_environment_hierarchy</a>(...) -> EnvTreeJsonNode</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.project.get_fleet_environment_hierarchy(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    fleet_uid="fleetUID",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fleet_uid:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1538-L1573">get_fleet_environment_variables</a>(...) -> EnvironmentVariables</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get environment variables of a fleet
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

client.project.get_fleet_environment_variables(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    fleet_uid="fleetUID",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fleet_uid:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1575-L1626">set_fleet_environment_variables</a>(...) -> EnvironmentVariables</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set environment variables of a fleet
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

client.project.set_fleet_environment_variables(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    fleet_uid="fleetUID",
    environment_variables={
        "key": "value"
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fleet_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `EnvironmentVariables` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1628-L1672">delete_fleet_environment_variable</a>(...) -> EnvironmentVariables</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete environment variables of a fleet
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

client.project.delete_fleet_environment_variable(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    fleet_uid="fleetUID",
    key="key",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fleet_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — The environment variable key to delete.
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1674-L1705">set_global_event_transformation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the project-level event JSONata transformation
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

client.project.set_global_event_transformation(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1707-L1738">disable_global_event_transformation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disable the project-level event JSONata transformation
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

client.project.disable_global_event_transformation(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1740-L1771">enable_global_event_transformation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enable the project-level event JSONata transformation
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

client.project.enable_global_event_transformation(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1773-L1803">get_project_members</a>(...) -> GetProjectMembersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Project Members
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

client.project.get_project_members(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1805-L1835">get_products</a>(...) -> GetProductsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Products within a Project
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

client.project.get_products(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1837-L1894">create_product</a>(...) -> Product</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Product within a Project
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

client.project.create_product(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    label="label",
    product_uid="product_uid",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**label:** `str` — The label for the Product.
    
</dd>
</dl>

<dl>
<dd>

**product_uid:** `str` — The requested uid for the Product. Will be prefixed with the user's reversed email.
    
</dd>
</dl>

<dl>
<dd>

**auto_provision_fleets:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**disable_devices_by_default:** `typing.Optional[bool]` — If `true`, devices provisioned to this product will be automatically disabled by default.
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1896-L1930">delete_product</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a product
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

client.project.delete_product(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    product_uid="com.blues.bridge:sensors",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**product_uid:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1932-L1960">get_notefile_schemas</a>(...) -> typing.List[NotefileSchema]</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.project.get_notefile_schemas(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1962-L1992">get_project_secrets</a>(...) -> GetProjectSecretsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all secrets for a project (metadata only, values are never returned)
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

client.project.get_project_secrets(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L1994-L2039">create_project_secret</a>(...) -> ProjectSecret</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new project secret
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

client.project.create_project_secret(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    name="name",
    value="value",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The secret name (alphanumeric and underscores only).
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — The secret value (encrypted at rest, never returned after creation).
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L2041-L2086">update_project_secret</a>(...) -> ProjectSecret</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the value of an existing project secret
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

client.project.update_project_secret(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    secret_name="secretName",
    value="value",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**secret_name:** `str` — The name of the secret.
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — The new secret value (encrypted at rest, never returned).
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py#L2088-L2123">delete_project_secret</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a project secret by name
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

client.project.delete_project_secret(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    secret_name="secretName",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**secret_name:** `str` — The name of the secret.
    
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

## Alert
<details><summary><code>client.alert.<a href="src/fern/alert/client.py#L26-L74">get_alerts</a>(...) -> GetAlertsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get list of defined Alerts
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

client.alert.get_alerts(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**monitor_uid:** `typing.Optional[str]` 
    
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

## event
<details><summary><code>client.event.<a href="src/fern/event/client.py#L38-L152">get_events</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Events of a Project
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
client.event.get_events(...)
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A Device UID.
    
</dd>
</dl>

<dl>
<dd>

**sensor_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A sensor UID to filter events by, matched exactly against the event sensor field. The value may carry any prefix.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetEventsRequestSortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetEventsRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[int]` — Start date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — End date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**date_type:** `typing.Optional[GetEventsRequestDateType]` — Which date to filter on, either 'captured' or 'uploaded'.  This will apply to the startDate and endDate parameters
    
</dd>
</dl>

<dl>
<dd>

**system_files_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**files:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[GetEventsRequestFormat]` — Response format (JSON or CSV)
    
</dd>
</dl>

<dl>
<dd>

**serial_number:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by Serial Number
    
</dd>
</dl>

<dl>
<dd>

**fleet_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by Fleet UID
    
</dd>
</dl>

<dl>
<dd>

**session_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by Session UID
    
</dd>
</dl>

<dl>
<dd>

**event_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by Event UID
    
</dd>
</dl>

<dl>
<dd>

**select_fields:** `typing.Optional[str]` — Comma-separated list of fields to select from JSON payload (e.g., "field1,field2.subfield,field3"), this will reflect the columns in the CSV output.
    
</dd>
</dl>

<dl>
<dd>

**device_ui_ds:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Deprecated.
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[str]` — Deprecated.
    
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

<details><summary><code>client.event.<a href="src/fern/event/client.py#L154-L226">get_events_by_cursor</a>(...) -> GetEventsByCursorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Events of a Project by cursor
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

client.event.get_events_by_cursor(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    files="_health.qo, data.qo",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A cursor, which can be obtained from the `next_cursor` value from a previous call to this endpoint. The results set returned will include this event as its first result if the given identifier is actually the UID of an event. If this event UID is not found, the parameter is ignored and the results set is the same as if the parameter was not included.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetEventsByCursorRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**system_files_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**files:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fleet_uid:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A Device UID.
    
</dd>
</dl>

<dl>
<dd>

**sensor_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A sensor UID to filter events by, matched exactly against the event sensor field. The value may carry any prefix.
    
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

<details><summary><code>client.event.<a href="src/fern/event/client.py#L228-L263">get_route_logs_by_event</a>(...) -> typing.List[RouteLog]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Route Logs by Event UID
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

client.event.get_route_logs_by_event(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    event_uid="4506f411-dea6-44a0-9743-1130f57d7747",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**event_uid:** `str` 
    
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

<details><summary><code>client.event.<a href="src/fern/event/client.py#L265-L378">get_fleet_events</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Events of a Fleet
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
client.event.get_fleet_events(...)
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fleet_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A Device UID.
    
</dd>
</dl>

<dl>
<dd>

**sensor_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A sensor UID to filter events by, matched exactly against the event sensor field. The value may carry any prefix.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetFleetEventsRequestSortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetFleetEventsRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[int]` — Start date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — End date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**date_type:** `typing.Optional[GetFleetEventsRequestDateType]` — Which date to filter on, either 'captured' or 'uploaded'.  This will apply to the startDate and endDate parameters
    
</dd>
</dl>

<dl>
<dd>

**system_files_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**files:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[GetFleetEventsRequestFormat]` — Response format (JSON or CSV)
    
</dd>
</dl>

<dl>
<dd>

**serial_number:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by Serial Number
    
</dd>
</dl>

<dl>
<dd>

**session_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by Session UID
    
</dd>
</dl>

<dl>
<dd>

**event_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by Event UID
    
</dd>
</dl>

<dl>
<dd>

**select_fields:** `typing.Optional[str]` — Comma-separated list of fields to select from JSON payload (e.g., "field1,field2.subfield,field3"), this will reflect the columns in the CSV output.
    
</dd>
</dl>

<dl>
<dd>

**device_ui_ds:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Deprecated.
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[str]` — Deprecated.
    
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

<details><summary><code>client.event.<a href="src/fern/event/client.py#L380-L463">get_fleet_events_by_cursor</a>(...) -> GetFleetEventsByCursorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Events of a Fleet by cursor
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

client.event.get_fleet_events_by_cursor(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    fleet_uid="fleetUID",
    files="_health.qo, data.qo",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fleet_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A cursor, which can be obtained from the `next_cursor` value from a previous call to this endpoint. The results set returned will include this event as its first result if the given identifier is actually the UID of an event. If this event UID is not found, the parameter is ignored and the results set is the same as if the parameter was not included.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetFleetEventsByCursorRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**system_files_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**files:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A Device UID.
    
</dd>
</dl>

<dl>
<dd>

**sensor_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A sensor UID to filter events by, matched exactly against the event sensor field. The value may carry any prefix.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[int]` — Start date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — End date for filtering results, specified as a Unix timestamp
    
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

## jobs
<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py#L40-L70">get_jobs</a>(...) -> GetJobsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all batch jobs for a project
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

client.jobs.get_jobs(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py#L72-L145">create_job</a>(...) -> CreateJobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new batch job with an optional name
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
from fern import FernApi, BatchJobRequests, JobDefinitionSelect
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.create_job(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    name="name",
    comment="Set environment variables on all devices in a fleet",
    default_requests=BatchJobRequests(
        vars_to_set={
            "firmware_channel": "production",
            "log_level": "1"
        },
    ),
    select=JobDefinitionSelect(
        devices_in_fleets=[
            "fleet:00000000-0000-0000-0000-000000000000"
        ],
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name for the job
    
</dd>
</dl>

<dl>
<dd>

**request:** `JobDefinition` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py#L147-L181">get_job</a>(...) -> JobDetail</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific batch job definition
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

client.jobs.get_job(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    job_uid="my-reconciliation-job",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**job_uid:** `str` — Unique identifier for a batch job
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py#L183-L217">delete_job</a>(...) -> DeleteJobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a batch job
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

client.jobs.delete_job(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    job_uid="my-reconciliation-job",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**job_uid:** `str` — Unique identifier for a batch job
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py#L219-L263">run_job</a>(...) -> RunJobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a batch job
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

client.jobs.run_job(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    job_uid="my-reconciliation-job",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**job_uid:** `str` — Unique identifier for a batch job
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — Run job in dry-run mode without making actual changes
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py#L265-L313">get_job_runs</a>(...) -> GetJobRunsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all runs for a specific job
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

client.jobs.get_job_runs(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    job_uid="my-reconciliation-job",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**job_uid:** `str` — Unique identifier for a batch job
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Filter runs by status
    
</dd>
</dl>

<dl>
<dd>

**dry_run:** `typing.Optional[bool]` — Filter runs by dry run flag
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py#L315-L359">get_job_run</a>(...) -> JobRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the result of a job execution
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

client.jobs.get_job_run(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    report_uid="my-reconciliation-job-1707654321000",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**report_uid:** `str` — Unique identifier for a job run report
    
</dd>
</dl>

<dl>
<dd>

**view:** `typing.Optional[GetJobRunRequestView]` — Controls the level of detail returned: 'summary' returns metadata only, 'detail' returns the full result payload
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py#L361-L394">delete_job_run</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the results of a job run
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

client.jobs.delete_job_run(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    report_uid="my-reconciliation-job-1707654321000",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**report_uid:** `str` — Unique identifier for a job run report
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py#L396-L430">cancel_job_run</a>(...) -> CancelJobRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel a running job execution
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

client.jobs.cancel_job_run(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    report_uid="my-reconciliation-job-1707654321000",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**report_uid:** `str` — Unique identifier for a job run report
    
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

## Monitor
<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L37-L67">get_monitors</a>(...) -> typing.List[Monitor]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get list of defined Monitors
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

client.monitor.get_monitors(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L69-L211">create_monitor</a>(...) -> Monitor</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Monitor
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
from fern import FernApi, SlackWebHookNotification
from fern.environment import FernApiEnvironment
from fern.monitor import CreateMonitorSourceType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.monitor.create_monitor(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    alert_routes=[
        SlackWebHookNotification()
    ],
    description="description",
    name="name",
    source_type=CreateMonitorSourceType.EVENT,
    threshold=1,
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**alert_routes:** `typing.List[CreateMonitorAlertRoutesItem]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source_type:** `CreateMonitorSourceType` — The type of source to monitor. Supported values are "event" and "heartbeat".
    
</dd>
</dl>

<dl>
<dd>

**threshold:** `int` — The type of condition to apply to the value selected by the source_selector
    
</dd>
</dl>

<dl>
<dd>

**aggregate_function:** `typing.Optional[CreateMonitorAggregateFunction]` — Aggregate function to apply to the selected values before applying the condition. [none, sum, average, max, min]
    
</dd>
</dl>

<dl>
<dd>

**aggregate_window:** `typing.Optional[str]` — The time window to aggregate the selected values. It follows the format of a number followed by a time unit
    
</dd>
</dl>

<dl>
<dd>

**alert:** `typing.Optional[bool]` — If true, the monitor is in alert state.
    
</dd>
</dl>

<dl>
<dd>

**condition_type:** `typing.Optional[CreateMonitorConditionType]` — A comparison operation to apply to the value selected by the source_selector [greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to]
    
</dd>
</dl>

<dl>
<dd>

**disabled:** `typing.Optional[bool]` — If true, the monitor will not be evaluated.
    
</dd>
</dl>

<dl>
<dd>

**fleet_filter:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**last_routed_at:** `typing.Optional[str]` — The last time the monitor was evaluated and routed.
    
</dd>
</dl>

<dl>
<dd>

**notefile_filter:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**per_device:** `typing.Optional[bool]` — Only relevant when using an aggregate_function. If true, the monitor will be evaluated per device, | rather than across the set of selected devices. If true then if a single device matches the specified criteria, | and alert will be created, otherwise the aggregate function will be applied across all devices.
    
</dd>
</dl>

<dl>
<dd>

**routing_cooldown_period:** `typing.Optional[str]` — The time period to wait before routing another event after the monitor | has been triggered. It follows the format of a number followed by a time unit.
    
</dd>
</dl>

<dl>
<dd>

**silenced:** `typing.Optional[bool]` — If true, alerts will be created, but no notifications will be sent.
    
</dd>
</dl>

<dl>
<dd>

**source_selector:** `typing.Optional[str]` — A valid JSONata expression that selects the value to monitor from the source. | It should return a single, numeric value.
    
</dd>
</dl>

<dl>
<dd>

**uid:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**usage_scope:** `typing.Optional[str]` — For usage monitors: the scope of aggregation. Supported values are "device" and "fleet".
    
</dd>
</dl>

<dl>
<dd>

**usage_type:** `typing.Optional[str]` — For usage monitors: the type of data usage to monitor. Supported values are "cellular" and "satellite".
    
</dd>
</dl>

<dl>
<dd>

**usage_window:** `typing.Optional[int]` — For usage monitors: the rolling time window in days to sum usage over (e.g. 30 for 30 days).
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L213-L246">get_monitor</a>(...) -> Monitor</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Monitor
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

client.monitor.get_monitor(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    monitor_uid="monitor:8bAdf00d-000f-51c-af-01d5eaf00dbad",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**monitor_uid:** `str` 
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L248-L388">update_monitor</a>(...) -> Monitor</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Monitor
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

client.monitor.update_monitor(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    monitor_uid="monitor:8bAdf00d-000f-51c-af-01d5eaf00dbad",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**monitor_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `Monitor` 
    
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

<details><summary><code>client.monitor.<a href="src/fern/monitor/client.py#L390-L425">delete_monitor</a>(...) -> Monitor</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Monitor
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

client.monitor.delete_monitor(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    monitor_uid="monitor:8bAdf00d-000f-51c-af-01d5eaf00dbad",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**monitor_uid:** `str` 
    
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

## route
<details><summary><code>client.route.<a href="src/fern/route/client.py#L51-L81">get_routes</a>(...) -> typing.List[NotehubRouteSummary]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all Routes within a Project
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

client.route.get_routes(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
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

**project_or_product_uid:** `str` 
    
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

<details><summary><code>client.route.<a href="src/fern/route/client.py#L83-L218">create_route</a>(...) -> NotehubRoute</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Route within a Project
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
from fern import FernApi, HttpRoute
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.route.create_route(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    http=HttpRoute(
        disable_http_headers=False,
        fleets=[
            "fleet:1042ddc5-3b2c-4cec-b1fb-d3040538094d"
        ],
        http_headers={
            "X-My-Header": "value"
        },
        throttle_ms=100,
        timeout=5000,
        url="https://example.com/ingest",
    ),
    label="Route Label",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `NotehubRoute` 
    
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

<details><summary><code>client.route.<a href="src/fern/route/client.py#L220-L253">get_route</a>(...) -> NotehubRoute</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get single route within a project
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

client.route.get_route(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    route_uid="route:cbd20093cba58392c9f9bbdd0cdeb1a0",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**route_uid:** `str` 
    
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

<details><summary><code>client.route.<a href="src/fern/route/client.py#L255-L386">update_route</a>(...) -> NotehubRoute</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update route by UID
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

client.route.update_route(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    route_uid="route:cbd20093cba58392c9f9bbdd0cdeb1a0",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**route_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `NotehubRoute` 
    
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

<details><summary><code>client.route.<a href="src/fern/route/client.py#L388-L420">delete_route</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete single route within a project
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

client.route.delete_route(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    route_uid="route:cbd20093cba58392c9f9bbdd0cdeb1a0",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**route_uid:** `str` 
    
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

<details><summary><code>client.route.<a href="src/fern/route/client.py#L422-L520">get_route_logs_by_route</a>(...) -> typing.List[RouteLog]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Route Logs by Route UID
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

client.route.get_route_logs_by_route(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    route_uid="route:cbd20093cba58392c9f9bbdd0cdeb1a0",
    files="_health.qo, data.qo",
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**route_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A Device UID.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetRouteLogsByRouteRequestSortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetRouteLogsByRouteRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[int]` — Start date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — End date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**system_files_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**most_recent_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**files:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**routing_status:** `typing.Optional[typing.Union[GetRouteLogsByRouteRequestRoutingStatusItem, typing.Sequence[GetRouteLogsByRouteRequestRoutingStatusItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**response_status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
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

## usage
<details><summary><code>client.usage.<a href="src/fern/usage/client.py#L37-L111">get_data_usage</a>(...) -> GetDataUsageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get data usage in bytes for a project with time range and period aggregation
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
from fern.usage import GetDataUsageRequestPeriod

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.usage.get_data_usage(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    period=GetDataUsageRequestPeriod.DAY,
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `GetDataUsageRequestPeriod` — Period type for aggregation
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[int]` — Start date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — End date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A Device UID.
    
</dd>
</dl>

<dl>
<dd>

**fleet_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by Fleet UID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of data points returned
    
</dd>
</dl>

<dl>
<dd>

**aggregate:** `typing.Optional[GetDataUsageRequestAggregate]` — Aggregation level for results
    
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

<details><summary><code>client.usage.<a href="src/fern/usage/client.py#L113-L202">get_events_usage</a>(...) -> UsageEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get events usage for a project with time range and period aggregation, when endDate is 0 or unspecified the current time is implied
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
from fern.usage import GetEventsUsageRequestPeriod

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.usage.get_events_usage(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    period=GetEventsUsageRequestPeriod.DAY,
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `GetEventsUsageRequestPeriod` — Period type for aggregation
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[int]` — Start date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — End date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A Device UID.
    
</dd>
</dl>

<dl>
<dd>

**fleet_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by Fleet UID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of data points returned
    
</dd>
</dl>

<dl>
<dd>

**aggregate:** `typing.Optional[GetEventsUsageRequestAggregate]` — Aggregation level for results
    
</dd>
</dl>

<dl>
<dd>

**notefile:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter to specific notefiles
    
</dd>
</dl>

<dl>
<dd>

**skip_recent_data:** `typing.Optional[bool]` — When true, skips fetching recent data from raw event tables and only returns data from summary tables. Use this for better performance on large projects.
    
</dd>
</dl>

<dl>
<dd>

**include_notefiles:** `typing.Optional[bool]` — Include per-notefile event counts in the response
    
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

<details><summary><code>client.usage.<a href="src/fern/usage/client.py#L204-L278">get_route_logs_usage</a>(...) -> GetRouteLogsUsageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get route logs usage for a project with time range and period aggregation, when endDate is 0 or unspecified the current time is implied
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
from fern.usage import GetRouteLogsUsageRequestPeriod

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.usage.get_route_logs_usage(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    period=GetRouteLogsUsageRequestPeriod.DAY,
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `GetRouteLogsUsageRequestPeriod` — Period type for aggregation
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[int]` — Start date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — End date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**route_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A Route UID.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of data points returned
    
</dd>
</dl>

<dl>
<dd>

**aggregate:** `typing.Optional[GetRouteLogsUsageRequestAggregate]` — Aggregation level for results
    
</dd>
</dl>

<dl>
<dd>

**skip_recent_data:** `typing.Optional[bool]` — When true, skips fetching recent data from raw event tables and only returns data from summary tables. Use this for better performance on large projects.
    
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

<details><summary><code>client.usage.<a href="src/fern/usage/client.py#L280-L359">get_sessions_usage</a>(...) -> GetSessionsUsageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get sessions usage for a project with time range and period aggregation, when endDate is 0 or unspecified the current time is implied
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
from fern.usage import GetSessionsUsageRequestPeriod

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.usage.get_sessions_usage(
    project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
    period=GetSessionsUsageRequestPeriod.DAY,
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

**project_or_product_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `GetSessionsUsageRequestPeriod` — Period type for aggregation
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[int]` — Start date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[int]` — End date for filtering results, specified as a Unix timestamp
    
</dd>
</dl>

<dl>
<dd>

**device_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A Device UID.
    
</dd>
</dl>

<dl>
<dd>

**fleet_uid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by Fleet UID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of data points returned
    
</dd>
</dl>

<dl>
<dd>

**aggregate:** `typing.Optional[GetSessionsUsageRequestAggregate]` — Aggregation level for results
    
</dd>
</dl>

<dl>
<dd>

**skip_recent_data:** `typing.Optional[bool]` — When true, skips fetching recent data from raw event tables and only returns data from summary tables. Use this for better performance on large projects.
    
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

