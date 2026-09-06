# Reference
## Aftermarketservices
<details><summary><code>client.aftermarketservices.<a href="src/fern/aftermarketservices/client.py">getcerts</a>() -> SystemObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.aftermarketservices.getcerts()

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

<details><summary><code>client.aftermarketservices.<a href="src/fern/aftermarketservices/client.py">putecu</a>(...) -> AgcoPowerServicesModelsEcu</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, AgcoPowerServicesModelsEcuState
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.aftermarketservices.putecu(
    serial_number_="serialNumber",
    edt_instance_id="EDTInstanceId",
    engine_serial_number="EngineSerialNumber",
    serial_number="SerialNumber",
    state=AgcoPowerServicesModelsEcuState.ACTIVE,
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

**serial_number:** `str` — The serial number of the ECU.
    
</dd>
</dl>

<dl>
<dd>

**edt_instance_id:** `str` — The EDT Instance Id of the kit calling this method.
    
</dd>
</dl>

<dl>
<dd>

**request:** `AgcoPowerServicesModelsEcu` 
    
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

<details><summary><code>client.aftermarketservices.<a href="src/fern/aftermarketservices/client.py">getengineiqacodes</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.aftermarketservices.getengineiqacodes(
    serial_number="serialNumber",
    edt_instance_id="EDTInstanceId",
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

**serial_number:** `str` — The serial number of the engine.
    
</dd>
</dl>

<dl>
<dd>

**edt_instance_id:** `str` — The EDT Instance Id of the kit calling this method.
    
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

<details><summary><code>client.aftermarketservices.<a href="src/fern/aftermarketservices/client.py">putiqacodes</a>(...) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.aftermarketservices.putiqacodes(
    serial_number="serialNumber",
    edt_instance_id="EDTInstanceId",
    request=[
        "string"
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

**serial_number:** `str` — The serial number of the Engine
    
</dd>
</dl>

<dl>
<dd>

**edt_instance_id:** `str` — The EDT Instance Id of the kit calling this method.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[str]` 
    
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

<details><summary><code>client.aftermarketservices.<a href="src/fern/aftermarketservices/client.py">getproductiondata</a>(...) -> typing.List[AgcoPowerServicesModelsProductionData]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.aftermarketservices.getproductiondata(
    serial_number="serialNumber",
    edt_instance_id="EDTInstanceId",
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

**serial_number:** `str` — The serial number of the engine.
    
</dd>
</dl>

<dl>
<dd>

**edt_instance_id:** `str` — The EDT Instance Id of the kit calling this method.
    
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

<details><summary><code>client.aftermarketservices.<a href="src/fern/aftermarketservices/client.py">getconnectionstatus</a>() -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.aftermarketservices.getconnectionstatus()

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

<details><summary><code>client.aftermarketservices.<a href="src/fern/aftermarketservices/client.py">getuserstatus</a>(...) -> AgcoPowerServicesModelsUserStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.aftermarketservices.getuserstatus(
    voucher_code="voucherCode",
    dealer_code="dealerCode",
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

**voucher_code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**dealer_code:** `str` 
    
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

<details><summary><code>client.aftermarketservices.<a href="src/fern/aftermarketservices/client.py">updateuserstatus</a>(...) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.aftermarketservices.updateuserstatus(
    dealer_code="DealerCode",
    voucher_code="VoucherCode",
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

**request:** `AgcoPowerServicesModelsUserStatus` 
    
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

## Authentication
<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">putmanagetokens</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authentication.putmanagetokens(
    user_id=1,
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

**user_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**bearer_action:** `typing.Optional[ApiModelsTokenOptionsBearerAction]` — The action to perform on the bearer token. Optional. Defaults to ‘None’.
    
</dd>
</dl>

<dl>
<dd>

**mac_action:** `typing.Optional[ApiModelsTokenOptionsMacAction]` — The action to perform on the MAC token. Optional. Defaults to ‘None’.
    
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

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">default</a>(...) -> ApiModelsAuthenticatedUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authentication.default(
    password="password",
    username="username",
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

**password:** `str` — A secret word or phrase that must be used to gain admission
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` — A unique ID a user needs to login with
    
</dd>
</dl>

<dl>
<dd>

**bearer_action:** `typing.Optional[ApiModelsCredentialsBearerAction]` — The action to perform on the bearer token. Optional. Defaults to ‘None’.
    
</dd>
</dl>

<dl>
<dd>

**mac_action:** `typing.Optional[ApiModelsCredentialsMacAction]` — The action to perform on the MAC token. Optional. Defaults to ‘None’.
    
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

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">isalive</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authentication.isalive()

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

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">requestpasswordreset</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authentication.requestpasswordreset(
    parameter_name="ParameterName",
    url="Url",
    username="Username",
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

**parameter_name:** `str` — The query string parameter name to use for supplying the password reset token
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — The URL to direct the user to reset the password.
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` — The username to reset the password for
    
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

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py">resetpasword</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authentication.resetpasword(
    new_password="NewPassword",
    token="Token",
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

**new_password:** `str` — The new password
    
</dd>
</dl>

<dl>
<dd>

**token:** `str` — The password reset token
    
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

## Authorizationcategories
<details><summary><code>client.authorizationcategories.<a href="src/fern/authorizationcategories/client.py">get</a>(...) -> ApiIPagedResponseAuthorizationCodesSharedModelsCategory</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcategories.get()

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

**limit:** `typing.Optional[int]` — Optional. The page limit.  If not specified, the default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset.  If not specified, the default page offset is 0.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[int]` — Optional. Filter by categories visible to the provided user with the provided userID.
    
</dd>
</dl>

<dl>
<dd>

**definition_id:** `typing.Optional[str]` — Optional. Filter by categories containing a definition with the provided ID.
    
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

<details><summary><code>client.authorizationcategories.<a href="src/fern/authorizationcategories/client.py">post</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcategories.post()

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

**request:** `AuthorizationCodesSharedModelsCategory` 
    
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

<details><summary><code>client.authorizationcategories.<a href="src/fern/authorizationcategories/client.py">getusers</a>(...) -> ApiIPagedResponseAuthorizationCodesSharedModelsCategoryUserReport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcategories.getusers()

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

**limit:** `typing.Optional[int]` — Optional. Defaults to 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**user_i_ds:** `typing.Optional[str]` — Optional. Includes only users with IDs on the provided comma-separated list.
    
</dd>
</dl>

<dl>
<dd>

**category_i_ds:** `typing.Optional[str]` — Optional. Includes only users with categories with IDs on the provided comma-separated list.
    
</dd>
</dl>

<dl>
<dd>

**include_categories:** `typing.Optional[bool]` — If true, include full Authorization Category detail. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**include_users:** `typing.Optional[bool]` — If true, include full User detail. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**user_search:** `typing.Optional[str]` — Optional. Includes only users with a Name, Username, or Email containing the provided value.
    
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

<details><summary><code>client.authorizationcategories.<a href="src/fern/authorizationcategories/client.py">put</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcategories.put(
    id_="id",
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `AuthorizationCodesSharedModelsCategory` 
    
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

<details><summary><code>client.authorizationcategories.<a href="src/fern/authorizationcategories/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcategories.delete(
    id="id",
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

**id:** `str` — The ID of the authorization category.
    
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

<details><summary><code>client.authorizationcategories.<a href="src/fern/authorizationcategories/client.py">adduser</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcategories.adduser(
    id="id",
    user_id=1,
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

**id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `int` — 
    
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

<details><summary><code>client.authorizationcategories.<a href="src/fern/authorizationcategories/client.py">removeuser</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcategories.removeuser(
    id="id",
    user_id=1,
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

**id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `int` — 
    
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

## Authorizationcodedefinitions
<details><summary><code>client.authorizationcodedefinitions.<a href="src/fern/authorizationcodedefinitions/client.py">getauthorizationcodedefinition</a>(...) -> AuthorizationCodesSharedModelsAuthorizationCodeDefinition</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcodedefinitions.getauthorizationcodedefinition(
    id="id",
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

**id:** `str` — The ID of the authorization code definition.
    
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

<details><summary><code>client.authorizationcodedefinitions.<a href="src/fern/authorizationcodedefinitions/client.py">postauthorizationcodedefinition</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcodedefinitions.postauthorizationcodedefinition(
    name="Name",
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

**request:** `AuthorizationCodesSharedModelsAuthorizationCodeDefinition` 
    
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

<details><summary><code>client.authorizationcodedefinitions.<a href="src/fern/authorizationcodedefinitions/client.py">addcategorytodefinition</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcodedefinitions.addcategorytodefinition(
    id="ID",
    category_id="categoryID",
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**category_id:** `str` — A category ID, as a GUID.
    
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

<details><summary><code>client.authorizationcodedefinitions.<a href="src/fern/authorizationcodedefinitions/client.py">removecategoryfromdefinition</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcodedefinitions.removecategoryfromdefinition(
    id="ID",
    category_id="categoryID",
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**category_id:** `str` — A category ID, as a GUID.
    
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

<details><summary><code>client.authorizationcodedefinitions.<a href="src/fern/authorizationcodedefinitions/client.py">putauthorizationcodedefinition</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcodedefinitions.putauthorizationcodedefinition(
    id_="id",
    name="Name",
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

**id:** `str` — The ID of the authorization code definition.
    
</dd>
</dl>

<dl>
<dd>

**request:** `AuthorizationCodesSharedModelsAuthorizationCodeDefinition` 
    
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

<details><summary><code>client.authorizationcodedefinitions.<a href="src/fern/authorizationcodedefinitions/client.py">deleteauthorizationcodedefinition</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcodedefinitions.deleteauthorizationcodedefinition(
    id="id",
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

**id:** `str` — The ID of the authorization code definition.
    
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

## Authorizationcodes
<details><summary><code>client.authorizationcodes.<a href="src/fern/authorizationcodes/client.py">getauthorizationcodes</a>(...) -> ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Additional searches: validationParameters[Name]=Value and dataParameters[Name]=Value. These can be used to search for authorization codes that have been generated using specified values for data or validation parameters.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcodes.getauthorizationcodes()

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

**code:** `typing.Optional[str]` — Optional. If provided, searches for entities with the provided authorization code.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit.  If not specified, the default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset.  If not specified, the default page offset is 0.
    
</dd>
</dl>

<dl>
<dd>

**definition_id:** `typing.Optional[str]` — Optional. If specified, filters codes by definition id.
    
</dd>
</dl>

<dl>
<dd>

**created_by_user_id:** `typing.Optional[int]` — Optional. If specified, filters codes to those created by the given User ID.
    
</dd>
</dl>

<dl>
<dd>

**deleted_by_user_id:** `typing.Optional[int]` — Optional. If specified, filters codes to those deleted by the given User ID.
    
</dd>
</dl>

<dl>
<dd>

**include_deleted:** `typing.Optional[bool]` — Optional. Whether to include deleted codes. 'False' by default.
    
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

<details><summary><code>client.authorizationcodes.<a href="src/fern/authorizationcodes/client.py">postauthorizationcode</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcodes.postauthorizationcode()

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

**request:** `AuthorizationCodesSharedModelsAuthorizationCode` 
    
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

<details><summary><code>client.authorizationcodes.<a href="src/fern/authorizationcodes/client.py">getauthorizationcode</a>(...) -> AuthorizationCodesSharedModelsAuthorizationCode</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcodes.getauthorizationcode(
    id=1,
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

**id:** `int` — The id of the authorization code.
    
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

<details><summary><code>client.authorizationcodes.<a href="src/fern/authorizationcodes/client.py">putauthorizationcode</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcodes.putauthorizationcode(
    id_=1,
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

**id:** `int` — The id of the authorization code.
    
</dd>
</dl>

<dl>
<dd>

**request:** `AuthorizationCodesSharedModelsAuthorizationCode` 
    
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

<details><summary><code>client.authorizationcodes.<a href="src/fern/authorizationcodes/client.py">deleteauthorizationcode</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcodes.deleteauthorizationcode(
    id=1,
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

**id:** `int` — The id of the authorization code.
    
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

<details><summary><code>client.authorizationcodes.<a href="src/fern/authorizationcodes/client.py">getcontactinformation</a>(...) -> AuthorizationCodesSharedModelsAuthorizationContactInformation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcodes.getcontactinformation(
    id=1,
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

**id:** `int` — The id of the authorization code.
    
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

<details><summary><code>client.authorizationcodes.<a href="src/fern/authorizationcodes/client.py">validateauthorizationcode</a>(...) -> AuthorizationCodesSharedModelsCodeValidationModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcodes.validateauthorizationcode(
    id=1,
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

**id:** `int` 
    
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

## Authorizationcontactinformation
<details><summary><code>client.authorizationcontactinformation.<a href="src/fern/authorizationcontactinformation/client.py">get</a>(...) -> ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcontactinformation.get()

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

**limit:** `typing.Optional[int]` — Optional. The page limit.  If not specified, the default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset.  If not specified, the default page offset is 0.
    
</dd>
</dl>

<dl>
<dd>

**authorization_code:** `typing.Optional[str]` — Optional. Search by authorization code.
    
</dd>
</dl>

<dl>
<dd>

**after_date:** `typing.Optional[datetime.datetime]` — Optional. Include only data for authorization codes created after a provided date.
    
</dd>
</dl>

<dl>
<dd>

**before_date:** `typing.Optional[datetime.datetime]` — Optional. Include only data for authorization codes created before a provided date.
    
</dd>
</dl>

<dl>
<dd>

**dealer_code:** `typing.Optional[str]` — Optional. Search by dealer code.
    
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

<details><summary><code>client.authorizationcontactinformation.<a href="src/fern/authorizationcontactinformation/client.py">post</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authorizationcontactinformation.post(
    authorization_code_id=1,
    contact="Contact",
    dealer_code="DealerCode",
    dealership="Dealership",
    phone="Phone",
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

**request:** `AuthorizationCodesSharedModelsAuthorizationContactInformation` 
    
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

## Brands
<details><summary><code>client.brands.<a href="src/fern/brands/client.py">brands</a>() -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.brands.brands()

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

## Bundles
<details><summary><code>client.bundles.<a href="src/fern/bundles/client.py">getbundles</a>(...) -> ApiPagedResponseUpdateSystemModelsBundle</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.bundles.getbundles()

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

**update_group_id:** `typing.Optional[str]` — Optional. Filter by UpdateGroup ID.
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Optional. Filter by active status.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
</dd>
</dl>

<dl>
<dd>

**bundle_number:** `typing.Optional[int]` — Optional. If provided, filters by BundleNumber.
    
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

<details><summary><code>client.bundles.<a href="src/fern/bundles/client.py">postbundle</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.bundles.postbundle(
    bundle_number=1,
    description="Description",
    update_group_id="UpdateGroupID",
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

**request:** `UpdateSystemModelsBundle` 
    
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

<details><summary><code>client.bundles.<a href="src/fern/bundles/client.py">getbundle</a>(...) -> UpdateSystemModelsBundle</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.bundles.getbundle(
    id="ID",
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

**id:** `str` — The Bundle ID
    
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

<details><summary><code>client.bundles.<a href="src/fern/bundles/client.py">putbundle</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.bundles.putbundle(
    id="ID",
    bundle_number=1,
    description="Description",
    update_group_id="UpdateGroupID",
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

**id:** `str` — The unique ID of the Bundle
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateSystemModelsBundle` 
    
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

<details><summary><code>client.bundles.<a href="src/fern/bundles/client.py">deletebundle</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.bundles.deletebundle(
    id="ID",
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

**id:** `str` — The Bundle ID to Delete
    
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

## Clients
<details><summary><code>client.clients.<a href="src/fern/clients/client.py">get</a>(...) -> UpdateSystemModelsClient</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.clients.get(
    id="ID",
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

**id:** `str` — The Client ID
    
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

<details><summary><code>client.clients.<a href="src/fern/clients/client.py">put</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.clients.put(
    id="ID",
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

**id:** `str` — The Client ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateSystemModelsClient` 
    
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

<details><summary><code>client.clients.<a href="src/fern/clients/client.py">getavailablesubscriptions</a>(...) -> ApiPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.clients.getavailablesubscriptions(
    id="ID",
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

**id:** `str` — The Client ID
    
</dd>
</dl>

<dl>
<dd>

**update_group_id:** `typing.Optional[str]` — Optional. Filter by Update Group.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
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

<details><summary><code>client.clients.<a href="src/fern/clients/client.py">getsubscriptions</a>(...) -> ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.clients.getsubscriptions(
    id="ID",
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

**id:** `str` — The Client ID
    
</dd>
</dl>

<dl>
<dd>

**update_group_id:** `typing.Optional[str]` — Optional. Filter by Update Group.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
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

## Updatesystem
<details><summary><code>client.updatesystem.<a href="src/fern/updatesystem/client.py">getcachedfiles</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.updatesystem.getcachedfiles(
    client_id="ClientID",
    expired=True,
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

**client_id:** `str` — The ClientID of the Client
    
</dd>
</dl>

<dl>
<dd>

**expired:** `bool` — Only Expired Files (true|false)
    
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

<details><summary><code>client.updatesystem.<a href="src/fern/updatesystem/client.py">getcheckin</a>(...) -> UpdateSystemModelsCheckinResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.updatesystem.getcheckin(
    client_id="ClientID",
    preview=True,
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

**client_id:** `str` — The Client ID to check-in.  If this is a new client ID it will be added to Clients.
    
</dd>
</dl>

<dl>
<dd>

**preview:** `bool` — Get Pkgs w\o updating Datetimes(true|false)
    
</dd>
</dl>

<dl>
<dd>

**run_all_inventories:** `typing.Optional[bool]` — Force return inventories. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `typing.Optional[str]` — Optional. The 'NextTransactionID' from the previous check-in. Used to detect duplicate client IDs.
    
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

## Packagereports
<details><summary><code>client.packagereports.<a href="src/fern/packagereports/client.py">default</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.packagereports.default(
    client_id="ClientID",
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

**client_id:** `str` — The Client ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateSystemModelsPackageReport` 
    
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

<details><summary><code>client.packagereports.<a href="src/fern/packagereports/client.py">batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, UpdateSystemModelsPackageReport
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.packagereports.batch(
    client_id="ClientID",
    request=[
        UpdateSystemModelsPackageReport()
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

**client_id:** `str` — The Client ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[UpdateSystemModelsPackageReport]` 
    
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

## Contentdefinitions
<details><summary><code>client.contentdefinitions.<a href="src/fern/contentdefinitions/client.py">putcontentdefinitionattributes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.contentdefinitions.putcontentdefinitionattributes(
    request=[
        ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute(
            name="Name",
        )
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

**request:** `typing.List[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]` 
    
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

<details><summary><code>client.contentdefinitions.<a href="src/fern/contentdefinitions/client.py">putcontentdefinitionattributeasync</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentdefinitions.putcontentdefinitionattributeasync(
    content_definition_attribute_id=1,
    name="Name",
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

**content_definition_attribute_id:** `int` — The ID of the Attribute to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute` 
    
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

<details><summary><code>client.contentdefinitions.<a href="src/fern/contentdefinitions/client.py">deletecontentdefinitionattribute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentdefinitions.deletecontentdefinitionattribute(
    content_definition_attribute_id=1,
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

**content_definition_attribute_id:** `int` — The ID of the Attribute to remove.
    
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

<details><summary><code>client.contentdefinitions.<a href="src/fern/contentdefinitions/client.py">getcontentdefinitions</a>(...) -> ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a collection of ContentDefinitions. When successful, the response is a PagedResponse of ContentDefinitions.
            If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentdefinitions.getcontentdefinitions()

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

**limit:** `typing.Optional[int]` — Optional. The page limit.  If not specified, the default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset.  If not specified, the default page offset is 0.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[int]` — Optional. Filter by UserID.
    
</dd>
</dl>

<dl>
<dd>

**include_attributes:** `typing.Optional[str]` — Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Optional. Filter by Name. Supports beginning and ending wildcard (*).
    
</dd>
</dl>

<dl>
<dd>

**type_id:** `typing.Optional[int]` — Optional. Filter by TypeID.
    
</dd>
</dl>

<dl>
<dd>

**package_type_id:** `typing.Optional[str]` — Optional. Filter by PackageTypeID.
    
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

<details><summary><code>client.contentdefinitions.<a href="src/fern/contentdefinitions/client.py">postcontentdefinition</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a ContentDefinition.  The body of the POST is the ContentDefinition to create.
            The ContentDefinitionID will be assigned on creation of the Job.  When successful, the response
            is the JobID.  If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentdefinitions.postcontentdefinition(
    description="Description",
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

**request:** `ContentSubmissionSharedBusinessEntitiesContentDefinition` 
    
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

<details><summary><code>client.contentdefinitions.<a href="src/fern/contentdefinitions/client.py">getcontentdefinition</a>(...) -> ContentSubmissionSharedBusinessEntitiesContentDefinition</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a ContentDefinition by ID. When successful, the response is the requested ContentDefinition.
            If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentdefinitions.getcontentdefinition(
    content_definition_id=1,
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

**content_definition_id:** `int` — The ID of the ContentDefinition to get.
    
</dd>
</dl>

<dl>
<dd>

**include_attributes:** `typing.Optional[str]` — Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.
    
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

<details><summary><code>client.contentdefinitions.<a href="src/fern/contentdefinitions/client.py">putcontentdefinition</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a ContentDefinition.  The body of the PUT is the updated ContentDefinition.  
            When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentdefinitions.putcontentdefinition(
    content_definition_id_=1,
    description="Description",
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

**content_definition_id:** `int` — The ID of the ContentDefinition to update
    
</dd>
</dl>

<dl>
<dd>

**request:** `ContentSubmissionSharedBusinessEntitiesContentDefinition` 
    
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

<details><summary><code>client.contentdefinitions.<a href="src/fern/contentdefinitions/client.py">deletecontentdefinition</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an ContentDefinition. When successful, the response is empty.  If unsuccessful, an appropriate
            ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentdefinitions.deletecontentdefinition(
    content_definition_id=1,
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

**content_definition_id:** `int` — The ID of the ContentDefinition to delete
    
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

<details><summary><code>client.contentdefinitions.<a href="src/fern/contentdefinitions/client.py">getcontentdefinitionattributes</a>(...) -> ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentdefinitions.getcontentdefinitionattributes(
    content_definition_id=1,
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

**content_definition_id:** `int` — The ID of the ContentDefinition.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit.  If not specified, the default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset.  If not specified, the default page offset is 0.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Optional. Filter the attributes by Name.
    
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

<details><summary><code>client.contentdefinitions.<a href="src/fern/contentdefinitions/client.py">postcontentdefinitionattribute</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentdefinitions.postcontentdefinitionattribute(
    content_definition_id_=1,
    name="Name",
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

**content_definition_id:** `int` — The ID of the ContentDefinition
    
</dd>
</dl>

<dl>
<dd>

**request:** `ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute` 
    
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

<details><summary><code>client.contentdefinitions.<a href="src/fern/contentdefinitions/client.py">postcontentdefinitionattributes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.contentdefinitions.postcontentdefinitionattributes(
    content_definition_id=1,
    request=[
        ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute(
            name="Name",
        )
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

**content_definition_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute]` 
    
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

## Contentrelease
<details><summary><code>client.contentrelease.<a href="src/fern/contentrelease/client.py">getcontentreleaseversion</a>(...) -> ContentSubmissionSharedBusinessEntitiesContentReleaseVersion</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a ContentReleaseVersion by ID. When successful, the response is the requested ContentReleaseVersion.
            If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentrelease.getcontentreleaseversion(
    content_release_id=1,
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

**content_release_id:** `int` — The ID of the ContentReleaseVersion to get.
    
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

<details><summary><code>client.contentrelease.<a href="src/fern/contentrelease/client.py">postcontentrelease</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a ContentReleaseVersion.  The body of the POST is the ContentReleaseVersion to create.
            The ContentReleaseId will be assigned on creation of the Job.  When successful, the response
            is the contentReleaseId.  If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentrelease.postcontentrelease()

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

**request:** `ContentSubmissionSharedBusinessEntitiesContentReleaseVersion` 
    
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

<details><summary><code>client.contentrelease.<a href="src/fern/contentrelease/client.py">putcontentdefinition</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a ContentReleaseVersion.  The body of the PUT is the updated ContentReleaseVersion.  
            When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentrelease.putcontentdefinition(
    content_release_id_=1,
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

**content_release_id:** `int` — The ID of the ContentReleaseVersion to update
    
</dd>
</dl>

<dl>
<dd>

**request:** `ContentSubmissionSharedBusinessEntitiesContentReleaseVersion` 
    
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

<details><summary><code>client.contentrelease.<a href="src/fern/contentrelease/client.py">deletecontentreleaseversionn</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an ContentReleaseVersion. When successful, the response is empty.  If unsuccessful, an appropriate
            ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentrelease.deletecontentreleaseversionn(
    content_release_id=1,
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

**content_release_id:** `int` — The ID of the ContentReleaseVersion to delete
    
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

## Contentsubmissions
<details><summary><code>client.contentsubmissions.<a href="src/fern/contentsubmissions/client.py">putcontentsubmissionattributes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.contentsubmissions.putcontentsubmissionattributes(
    request=[
        ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute(
            name="Name",
        )
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

**request:** `typing.List[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]` 
    
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

<details><summary><code>client.contentsubmissions.<a href="src/fern/contentsubmissions/client.py">putcontentsubmissionattributeasync</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentsubmissions.putcontentsubmissionattributeasync(
    content_submission_attribute_id=1,
    name="Name",
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

**content_submission_attribute_id:** `int` — The ID of the Attribute to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute` 
    
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

<details><summary><code>client.contentsubmissions.<a href="src/fern/contentsubmissions/client.py">deletecontentsubmissionattribute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentsubmissions.deletecontentsubmissionattribute(
    content_submission_attribute_id=1,
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

**content_submission_attribute_id:** `int` — The ID of the Attribute to remove.
    
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

<details><summary><code>client.contentsubmissions.<a href="src/fern/contentsubmissions/client.py">getcontentsubmissions</a>(...) -> ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmission</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a collection of ContentSubmissions. When successful, the response is a PagedResponse of ContentSubmissions. Additional searches: attributes[Name]=Value. This can be used to search for submissions that have the specified values for attributes. Beginning and ending wildcard (*) supported for value.
            If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentsubmissions.getcontentsubmissions()

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

**limit:** `typing.Optional[int]` — Optional. The page limit.  If not specified, the default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset.  If not specified, the default page offset is 0.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[int]` — Optional. Filter by UserID.
    
</dd>
</dl>

<dl>
<dd>

**content_definition_id:** `typing.Optional[int]` — Optional. Filter by ContentDefinitionID
    
</dd>
</dl>

<dl>
<dd>

**include_attributes:** `typing.Optional[str]` — Names of Attributes to include when retrieving this submission. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.
    
</dd>
</dl>

<dl>
<dd>

**release_id:** `typing.Optional[int]` — Optional. Filter the submissions by whether they are part of the Release with the specified Release ID.
    
</dd>
</dl>

<dl>
<dd>

**type_id:** `typing.Optional[int]` — Optional. Filter submissions by their ContentDefinition's Type ID.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` — Optional. Filter submissions by their Version.
    
</dd>
</dl>

<dl>
<dd>

**include_definition:** `typing.Optional[bool]` — Optional. If true, includes the ContentDefinition for each submission.
    
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

<details><summary><code>client.contentsubmissions.<a href="src/fern/contentsubmissions/client.py">postcontentsubmission</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a ContentSubmission.  The body of the POST is the ContentSubmission to create.
            The ContentSubmissionID will be assigned on creation of the Job.  When successful, the response
            is the ContentSubmissionID.  If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentsubmissions.postcontentsubmission()

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

**request:** `ContentSubmissionSharedBusinessEntitiesContentSubmission` 
    
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

<details><summary><code>client.contentsubmissions.<a href="src/fern/contentsubmissions/client.py">getcontentsubmission</a>(...) -> ContentSubmissionSharedBusinessEntitiesContentSubmission</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a ContentSubmission by ID. When successful, the response is the requested ContentSubmission.
            If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentsubmissions.getcontentsubmission(
    content_submission_id=1,
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

**content_submission_id:** `int` — The ID of the ContentSubmission to get.
    
</dd>
</dl>

<dl>
<dd>

**include_attributes:** `typing.Optional[str]` — Names of Attributes to include when retrieving this submission. This should be a comma-separated list.
    
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

<details><summary><code>client.contentsubmissions.<a href="src/fern/contentsubmissions/client.py">putcontentsubmission</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a ContentSubmission.  The body of the PUT is the updated ContentSubmission.  
            When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentsubmissions.putcontentsubmission(
    content_submission_id_=1,
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

**content_submission_id:** `int` — The ID of the ContentSubmission to update
    
</dd>
</dl>

<dl>
<dd>

**request:** `ContentSubmissionSharedBusinessEntitiesContentSubmission` 
    
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

<details><summary><code>client.contentsubmissions.<a href="src/fern/contentsubmissions/client.py">deletecontentsubmission</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an ContentSubmission. When successful, the response is empty.  If unsuccessful, an appropriate
            ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentsubmissions.deletecontentsubmission(
    content_submission_id=1,
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

**content_submission_id:** `int` — The ID of the ContentSubmission to delete
    
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

<details><summary><code>client.contentsubmissions.<a href="src/fern/contentsubmissions/client.py">getcontentsubmissionattributes</a>(...) -> ApiPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentsubmissions.getcontentsubmissionattributes(
    content_submission_id=1,
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

**content_submission_id:** `int` — The ID of the ContentSubmission.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit.  If not specified, the default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset.  If not specified, the default page offset is 0.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Optional. Filter the attributes by Name.
    
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

<details><summary><code>client.contentsubmissions.<a href="src/fern/contentsubmissions/client.py">postcontentsubmissionattribute</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentsubmissions.postcontentsubmissionattribute(
    content_submission_id_=1,
    name="Name",
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

**content_submission_id:** `int` — The ID of the ContentSubmission
    
</dd>
</dl>

<dl>
<dd>

**request:** `ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute` 
    
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

<details><summary><code>client.contentsubmissions.<a href="src/fern/contentsubmissions/client.py">postcontentsubmissionattributes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.contentsubmissions.postcontentsubmissionattributes(
    content_submission_id=1,
    request=[
        ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute(
            name="Name",
        )
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

**content_submission_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]` 
    
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

<details><summary><code>client.contentsubmissions.<a href="src/fern/contentsubmissions/client.py">getcontentsubmissionstatus</a>(...) -> BuildSystemSharedInterfacesIJobRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentsubmissions.getcontentsubmissionstatus(
    content_submission_id=1,
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

**content_submission_id:** `int` — The ID of the ContentSubmission to get.
    
</dd>
</dl>

<dl>
<dd>

**include_activity_run_details:** `typing.Optional[bool]` — True to include all status details if JobRun. Defaults to false
    
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

## Contentsubmissiontypes
<details><summary><code>client.contentsubmissiontypes.<a href="src/fern/contentsubmissiontypes/client.py">getcontentsubmissiontypes</a>(...) -> typing.List[ContentSubmissionSharedBusinessEntitiesContentSubmissionType]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentsubmissiontypes.getcontentsubmissiontypes()

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

**enabled:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.contentsubmissiontypes.<a href="src/fern/contentsubmissiontypes/client.py">postcontentsubmissiontype</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentsubmissiontypes.postcontentsubmissiontype(
    description="Description",
    name="Name",
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

**request:** `ContentSubmissionSharedBusinessEntitiesContentSubmissionType` 
    
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

<details><summary><code>client.contentsubmissiontypes.<a href="src/fern/contentsubmissiontypes/client.py">getcontentsubmissiontype</a>(...) -> ContentSubmissionSharedBusinessEntitiesContentSubmissionType</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentsubmissiontypes.getcontentsubmissiontype(
    id=1,
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

**id:** `int` — The ID of the Content Submission Type
    
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

<details><summary><code>client.contentsubmissiontypes.<a href="src/fern/contentsubmissiontypes/client.py">putcontentsubmissiontype</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentsubmissiontypes.putcontentsubmissiontype(
    id_=1,
    description="Description",
    name="Name",
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

**id:** `int` — The ID of the Content Submission Type
    
</dd>
</dl>

<dl>
<dd>

**request:** `ContentSubmissionSharedBusinessEntitiesContentSubmissionType` 
    
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

<details><summary><code>client.contentsubmissiontypes.<a href="src/fern/contentsubmissiontypes/client.py">deletecontentsubmissiontype</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.contentsubmissiontypes.deletecontentsubmissiontype(
    id=1,
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

**id:** `int` — The ID of the Content Submission Type
    
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

## Dealerbycountry
<details><summary><code>client.dealerbycountry.<a href="src/fern/dealerbycountry/client.py">getcountries</a>(...) -> ApiPagedResponseDealerDbModelsDealersPerCountry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.dealerbycountry.getcountries()

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

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
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

## Dealers
<details><summary><code>client.dealers.<a href="src/fern/dealers/client.py">getdealers</a>(...) -> ApiPagedResponseDealerDbModelsDealer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.dealers.getdealers()

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

**brand:** `typing.Optional[str]` — The brand to filter by.
    
</dd>
</dl>

<dl>
<dd>

**shipping_country:** `typing.Optional[str]` — The country to filter by.
    
</dd>
</dl>

<dl>
<dd>

**dealer_name:** `typing.Optional[str]` — The partial Dealer Name to filter by. Wildcard supported (*).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
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

<details><summary><code>client.dealers.<a href="src/fern/dealers/client.py">getdealerbydealercode</a>(...) -> DealerDbModelsDealer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.dealers.getdealerbydealercode(
    dealer_code="DealerCode",
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

**dealer_code:** `str` — The Dealer Code to Search for
    
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

## Fileuploadindexfields
<details><summary><code>client.fileuploadindexfields.<a href="src/fern/fileuploadindexfields/client.py">get</a>(...) -> ApiPagedResponseCommunicationModelsFileUploadIndexField</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.fileuploadindexfields.get()

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

**limit:** `typing.Optional[int]` — Optional. Limit number of results returned. The default value is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. Offset for the results returned. The default value is 0.
    
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

## Fileuploadtypes
<details><summary><code>client.fileuploadtypes.<a href="src/fern/fileuploadtypes/client.py">get</a>(...) -> ApiPagedResponseCommunicationModelsFileUploadType</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.fileuploadtypes.get()

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

**limit:** `typing.Optional[int]` — Optional. Limit number of results returned. The default value is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. Offset for the results returned. The default value is 0.
    
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

## Fileuploads
<details><summary><code>client.fileuploads.<a href="src/fern/fileuploads/client.py">postreport</a>(...) -> ApiPagedResponseCommunicationModelsFileUpload</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.fileuploads.postreport()

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

**field_filters:** `typing.Optional[typing.List[CommunicationModelsFieldFilter]]` — Optional. Filter results by field values. Multiple filters are combined with 'AND' logic.
    
</dd>
</dl>

<dl>
<dd>

**include_index_fields:** `typing.Optional[typing.List[str]]` 

Optional. The index data fields to include in the results.  
            By default any index data fields included in FieldFilters will be included.
    
</dd>
</dl>

<dl>
<dd>

**include_stored_data_fields:** `typing.Optional[typing.List[str]]` 

Optional. The stored data fields to include in the results. 
            By default stored data fields are omitted in the result.
            Limit must be 25 or less to return stored data fields.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. Limit number of results returned. The default value is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. Offset for the results returned. The default value is 0.
    
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

## Files
<details><summary><code>client.files.<a href="src/fern/files/client.py">getfiles</a>(...) -> ApiIPagedResponseGlobalResourcesSharedModelsFileDownload</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.files.getfiles()

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

**include_deleted:** `typing.Optional[bool]` — Indicates whether to include files marked as removed.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">postfile</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, GlobalResourcesSharedModelsFileDownloadState
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.files.postfile(
    crc="CRC",
    content_type="ContentType",
    description="Description",
    is_public=True,
    name="Name",
    path="Path",
    state=GlobalResourcesSharedModelsFileDownloadState.CREATED,
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

**request:** `GlobalResourcesSharedModelsFileDownload` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">getfile</a>(...) -> GlobalResourcesSharedModelsFileDownload</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.files.getfile(
    id="ID",
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

**id:** `str` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">putfile</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the metadata for a file. Size may not be modified by the client. 
                Set status to 'Available' to publish a file. The file must be uploaded.
                Set status to 'Created' to reset a file's contents and re-upload. 
                A file may only be 'Removed' by the DELETE method.
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
from fern import FernApi, GlobalResourcesSharedModelsFileDownloadState
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.files.putfile(
    id_="ID",
    crc="CRC",
    content_type="ContentType",
    description="Description",
    is_public=True,
    name="Name",
    path="Path",
    state=GlobalResourcesSharedModelsFileDownloadState.CREATED,
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

**id:** `str` — The file's id
    
</dd>
</dl>

<dl>
<dd>

**request:** `GlobalResourcesSharedModelsFileDownload` 
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">deletefile</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.files.deletefile(
    id="ID",
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

**id:** `str` — The file's id.
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">getfilecontents</a>(...) -> SystemObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.files.getfilecontents(
    id="ID",
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

**id:** `str` — The file's metadata.
    
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

<details><summary><code>client.files.<a href="src/fern/files/client.py">putfilecontents</a>(...) -> SystemObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.files.putfilecontents(
    id="ID",
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

**id:** `str` — The file's metadata.
    
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

## Globalimagecategories
<details><summary><code>client.globalimagecategories.<a href="src/fern/globalimagecategories/client.py">getfiles</a>(...) -> ApiIPagedResponseGlobalResourcesSharedModelsGlobalImageCategory</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.globalimagecategories.getfiles()

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

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
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

<details><summary><code>client.globalimagecategories.<a href="src/fern/globalimagecategories/client.py">postfile</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.globalimagecategories.postfile(
    name="Name",
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

**request:** `GlobalResourcesSharedModelsGlobalImageCategory` 
    
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

<details><summary><code>client.globalimagecategories.<a href="src/fern/globalimagecategories/client.py">getfile</a>(...) -> GlobalResourcesSharedModelsGlobalImageCategory</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.globalimagecategories.getfile(
    id="ID",
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

**id:** `str` — The file's id.
    
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

## Globalimages
<details><summary><code>client.globalimages.<a href="src/fern/globalimages/client.py">getglobalimages</a>(...) -> ApiIPagedResponseGlobalResourcesSharedModelsGlobalImage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.globalimages.getglobalimages()

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

**search:** `typing.Optional[str]` — Optional. Searches for matching global images with the matching Category Name, Publisher or Description
    
</dd>
</dl>

<dl>
<dd>

**category_id:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**publisher:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**include_deleted:** `typing.Optional[bool]` — Indicates whether to include GlobalImages marked as removed.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
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

<details><summary><code>client.globalimages.<a href="src/fern/globalimages/client.py">postglobalimage</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, GlobalResourcesSharedModelsGlobalImageState
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.globalimages.postglobalimage(
    crc="CRC",
    description="Description",
    height=1,
    name="Name",
    state=GlobalResourcesSharedModelsGlobalImageState.CREATED,
    thumbnail_crc="ThumbnailCRC",
    width=1,
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

**request:** `GlobalResourcesSharedModelsGlobalImage` 
    
</dd>
</dl>

<dl>
<dd>

**override_publisher_or_date:** `typing.Optional[bool]` — Whether to set the publisher and date to the provided values.
    
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

<details><summary><code>client.globalimages.<a href="src/fern/globalimages/client.py">getglobalimage</a>(...) -> GlobalResourcesSharedModelsGlobalImage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.globalimages.getglobalimage(
    id="ID",
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

**id:** `str` — The GlobalImage's id.
    
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

<details><summary><code>client.globalimages.<a href="src/fern/globalimages/client.py">putglobalimage</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the metadata for an image. Size may not be modified by the client. 
                Set status to 'Available' to publish an image. Both the image and thumbnail must be uploaded.
                Set status to 'Created' to reset an image's contents and re-upload. 
                A file may only be 'Removed' by the DELETE method.
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
from fern import FernApi, GlobalResourcesSharedModelsGlobalImageState
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.globalimages.putglobalimage(
    id_="ID",
    crc="CRC",
    description="Description",
    height=1,
    name="Name",
    state=GlobalResourcesSharedModelsGlobalImageState.CREATED,
    thumbnail_crc="ThumbnailCRC",
    width=1,
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

**id:** `str` — The GlobalImage's id.
    
</dd>
</dl>

<dl>
<dd>

**request:** `GlobalResourcesSharedModelsGlobalImage` 
    
</dd>
</dl>

<dl>
<dd>

**override_publisher_or_date:** `typing.Optional[bool]` — Whether to set the publisher and date to the provided values.
    
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

<details><summary><code>client.globalimages.<a href="src/fern/globalimages/client.py">deletefile</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.globalimages.deletefile(
    id="ID",
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

**id:** `str` — The GlobalImage's id.
    
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

<details><summary><code>client.globalimages.<a href="src/fern/globalimages/client.py">getglobalimagecontents</a>(...) -> SystemObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.globalimages.getglobalimagecontents(
    id="ID",
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

**id:** `str` — The global image metadata id.
    
</dd>
</dl>

<dl>
<dd>

**is_full_image:** `typing.Optional[bool]` — Indicated whether to download the full image or the thumbnail. Defaults to 'true'.
    
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

<details><summary><code>client.globalimages.<a href="src/fern/globalimages/client.py">putglobalimagecontents</a>(...) -> SystemObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Both the image and thumbnail must be uploaded.
                Set isFullImage = 'True' for Full Image, isFullImage = 'False' for Thumbnail
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
    environment=FernApiEnvironment.DEFAULT,
)

client.globalimages.putglobalimagecontents(
    id="ID",
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

**id:** `str` — The global image metadata id.
    
</dd>
</dl>

<dl>
<dd>

**is_full_image:** `typing.Optional[bool]` — Indicated whether this is the full image or the thumbnail. Defaults to 'true'.
    
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

## Languages
<details><summary><code>client.languages.<a href="src/fern/languages/client.py">getlanguages</a>(...) -> ApiIPagedResponseGlobalResourcesSharedModelsLanguage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.languages.getlanguages()

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

**limit:** `typing.Optional[int]` — limit the number of Language objects returned. Optional (defaults to 10).
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — the number of Language objects to skip. Optional (defaults to 0).
    
</dd>
</dl>

<dl>
<dd>

**include_deleted:** `typing.Optional[bool]` — whether to include languages marked as deleted. Defaults to false
    
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

<details><summary><code>client.languages.<a href="src/fern/languages/client.py">createlanguage</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.languages.createlanguage(
    description="Description",
    locale_id=1,
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

**request:** `GlobalResourcesSharedModelsLanguage` 
    
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

<details><summary><code>client.languages.<a href="src/fern/languages/client.py">getlanguage</a>(...) -> GlobalResourcesSharedModelsLanguage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.languages.getlanguage(
    locale_id=1,
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

**locale_id:** `int` — 
    
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

<details><summary><code>client.languages.<a href="src/fern/languages/client.py">updatelanguage</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.languages.updatelanguage(
    locale_id_=1,
    description="Description",
    locale_id=1,
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

**locale_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request:** `GlobalResourcesSharedModelsLanguage` 
    
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

<details><summary><code>client.languages.<a href="src/fern/languages/client.py">deletelanguage</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.languages.deletelanguage(
    locale_id=1,
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

**locale_id:** `int` — 
    
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

## Licenseactivations
<details><summary><code>client.licenseactivations.<a href="src/fern/licenseactivations/client.py">post</a>(...) -> DealerDbModelsLicenseActivation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.licenseactivations.post(
    dealer_code="DealerCode",
    postal_code="PostalCode",
    system_info="SystemInfo",
    voucher_code="VoucherCode",
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

**dealer_code:** `str` — The Dealer Code of the dealer activating the license
    
</dd>
</dl>

<dl>
<dd>

**postal_code:** `str` — The dealer's postal code (zip code)
    
</dd>
</dl>

<dl>
<dd>

**system_info:** `str` — Information about  the system being activated
    
</dd>
</dl>

<dl>
<dd>

**voucher_code:** `str` — The Voucher Code to use for activation
    
</dd>
</dl>

<dl>
<dd>

**license_activation_type:** `typing.Optional[DealerDbModelsLicenseActivationCreateLicenseActivationType]` — The type of license to create (e.g. EDT, EDT Lite)
    
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

<details><summary><code>client.licenseactivations.<a href="src/fern/licenseactivations/client.py">postregisteredtlite</a>(...) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.licenseactivations.postregisteredtlite(
    expiration_date=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    instance_id="InstanceID",
    voucher_code="VoucherCode",
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

**expiration_date:** `datetime.datetime` — The date at which the content of the EDT Lite expires.
    
</dd>
</dl>

<dl>
<dd>

**instance_id:** `str` — The identifier for the EDT Lite.
    
</dd>
</dl>

<dl>
<dd>

**voucher_code:** `str` — The voucher code with which the EDT Lite was created.
    
</dd>
</dl>

<dl>
<dd>

**dealer_code:** `typing.Optional[str]` — The dealer code with which the EDT Lite was created.
    
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

<details><summary><code>client.licenseactivations.<a href="src/fern/licenseactivations/client.py">put</a>(...) -> DealerDbModelsLicenseActivation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.licenseactivations.put(
    id="ID",
    license_version="LicenseVersion",
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

**id:** `str` — The ID of the license.
    
</dd>
</dl>

<dl>
<dd>

**license_version:** `str` — The license version to update
    
</dd>
</dl>

<dl>
<dd>

**system_info:** `typing.Optional[str]` — Information about  the system being activated
    
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

<details><summary><code>client.licenseactivations.<a href="src/fern/licenseactivations/client.py">putconfirm</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.licenseactivations.putconfirm(
    id="ID",
    license_version="LicenseVersion",
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

**id:** `str` — The ID of the license
    
</dd>
</dl>

<dl>
<dd>

**license_version:** `str` — The license version to confirm
    
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

## Licenses
<details><summary><code>client.licenses.<a href="src/fern/licenses/client.py">get</a>(...) -> DealerDbModelsLicense</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.licenses.get(
    id="ID",
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

**id:** `str` — The ID of the license to get.
    
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

## Logs
<details><summary><code>client.logs.<a href="src/fern/logs/client.py">getlogs</a>(...) -> ApiPagedResponseApiModelsLog</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.logs.getlogs()

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

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
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

<details><summary><code>client.logs.<a href="src/fern/logs/client.py">postlog</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.logs.postlog(
    message="Message",
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

**message:** `str` — Message to enter into the log
    
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

<details><summary><code>client.logs.<a href="src/fern/logs/client.py">getlog</a>(...) -> ApiModelsLog</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.logs.getlog(
    id="ID",
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

**id:** `str` — The Log ID
    
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

## Notifications
<details><summary><code>client.notifications.<a href="src/fern/notifications/client.py">postmail</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.notifications.postmail(
    is_body_html=True,
    message_body="MessageBody",
    subject="Subject",
    to_addresses=[
        "To_Addresses"
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

**is_body_html:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**message_body:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**subject:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**to_addresses:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cc_addresses:** `typing.Optional[typing.List[str]]` 
    
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

## Packagetypes
<details><summary><code>client.packagetypes.<a href="src/fern/packagetypes/client.py">get</a>(...) -> UpdateSystemModelsPackageType</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.packagetypes.get(
    id="ID",
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

**id:** `str` — The Package Type ID
    
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

<details><summary><code>client.packagetypes.<a href="src/fern/packagetypes/client.py">post</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.packagetypes.post(
    description="Description",
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

**request:** `UpdateSystemModelsPackageType` 
    
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

<details><summary><code>client.packagetypes.<a href="src/fern/packagetypes/client.py">put</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.packagetypes.put(
    id="ID",
    description="Description",
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

**id:** `str` — The ID of the Package Type
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateSystemModelsPackageType` 
    
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

<details><summary><code>client.packagetypes.<a href="src/fern/packagetypes/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.packagetypes.delete(
    id="ID",
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

**id:** `str` — The Package Type ID
    
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

<details><summary><code>client.packagetypes.<a href="src/fern/packagetypes/client.py">addpackagetypeuser</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.packagetypes.addpackagetypeuser(
    id="id",
    user_id=1,
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

**id:** `str` — The ID of the Package Type
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `int` — The userID to link to the package type
    
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

<details><summary><code>client.packagetypes.<a href="src/fern/packagetypes/client.py">removepackagetypeuser</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.packagetypes.removepackagetypeuser(
    id="id",
    user_id=1,
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

**id:** `str` — The ID of the Package Type
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `int` — The userID to link to the package type
    
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

## Packagetypetobundles
<details><summary><code>client.packagetypetobundles.<a href="src/fern/packagetypetobundles/client.py">get</a>(...) -> ApiPagedResponseUpdateSystemModelsPackageTypeIDtoBundle</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.packagetypetobundles.get()

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

**bundle_id:** `typing.Optional[str]` — Optional. Filter by BundleID.
    
</dd>
</dl>

<dl>
<dd>

**package_type_id:** `typing.Optional[str]` — Optional. Filter by PackageTypeID.
    
</dd>
</dl>

<dl>
<dd>

**package_version:** `typing.Optional[int]` — Optional. Filter by PackageVersion.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
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

<details><summary><code>client.packagetypetobundles.<a href="src/fern/packagetypetobundles/client.py">post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.packagetypetobundles.post(
    bundle_id="BundleID",
    package_type_id="PackageTypeID",
    package_version=1,
    priority=1,
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

**request:** `UpdateSystemModelsPackageTypeIDtoBundle` 
    
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

<details><summary><code>client.packagetypetobundles.<a href="src/fern/packagetypetobundles/client.py">put</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.packagetypetobundles.put(
    bundle_id="BundleID",
    package_type_id="PackageTypeID",
    package_version=1,
    priority=1,
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

**request:** `UpdateSystemModelsPackageTypeIDtoBundle` 
    
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

<details><summary><code>client.packagetypetobundles.<a href="src/fern/packagetypetobundles/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.packagetypetobundles.delete(
    bundle_id="BundleID",
    package_type_id="PackageTypeID",
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

**bundle_id:** `str` — The BundleID
    
</dd>
</dl>

<dl>
<dd>

**package_type_id:** `str` — The PackageTypeID
    
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

## Packages
<details><summary><code>client.packages.<a href="src/fern/packages/client.py">getpackages</a>(...) -> ApiPagedResponseUpdateSystemModelsPackage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.packages.getpackages()

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

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
</dd>
</dl>

<dl>
<dd>

**package_type_id:** `typing.Optional[str]` — Optional. If provided, filters by PackageTypeID.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` — Optional. If provided, filters by Version.
    
</dd>
</dl>

<dl>
<dd>

**released:** `typing.Optional[bool]` — Optional. If provided, filters by Released.
    
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

<details><summary><code>client.packages.<a href="src/fern/packages/client.py">postpackage</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.packages.postpackage(
    crc="CRC",
    description="Description",
    package_type_id="PackageTypeID",
    release_date=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    url="Url",
    version=1,
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

**request:** `UpdateSystemModelsPackage` 
    
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

<details><summary><code>client.packages.<a href="src/fern/packages/client.py">getpackage</a>(...) -> UpdateSystemModelsPackage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.packages.getpackage(
    id="ID",
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

**id:** `str` — The Package ID to Search for
    
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

<details><summary><code>client.packages.<a href="src/fern/packages/client.py">putpackage</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.packages.putpackage(
    id="ID",
    crc="CRC",
    description="Description",
    package_type_id="PackageTypeID",
    release_date=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    url="Url",
    version=1,
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

**id:** `str` — The unique ID of the Package
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateSystemModelsPackage` 
    
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

<details><summary><code>client.packages.<a href="src/fern/packages/client.py">deletepackage</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.packages.deletepackage(
    id="ID",
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

**id:** `str` — The Package ID to Delete
    
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

## Permissions
<details><summary><code>client.permissions.<a href="src/fern/permissions/client.py">getpermissions</a>(...) -> ApiPagedResponseApiModelsPermission</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.permissions.getpermissions()

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

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter by permission name. Supports ending wildcard (*). Optional.
    
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

<details><summary><code>client.permissions.<a href="src/fern/permissions/client.py">postpermission</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, ApiModelsPermissionDataRequired
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.permissions.postpermission(
    data_required=ApiModelsPermissionDataRequired.YES,
    name="Name",
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

**request:** `ApiModelsPermission` 
    
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

<details><summary><code>client.permissions.<a href="src/fern/permissions/client.py">getpermission</a>(...) -> ApiModelsPermission</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.permissions.getpermission(
    id=1,
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

**id:** `int` — Id of Permission
    
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

<details><summary><code>client.permissions.<a href="src/fern/permissions/client.py">putpermission</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, ApiModelsPermissionDataRequired
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.permissions.putpermission(
    id_=1,
    data_required=ApiModelsPermissionDataRequired.YES,
    name="Name",
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

**id:** `int` — Id of Permission
    
</dd>
</dl>

<dl>
<dd>

**request:** `ApiModelsPermission` 
    
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

<details><summary><code>client.permissions.<a href="src/fern/permissions/client.py">deletepermission</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.permissions.deletepermission(
    id=1,
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

**id:** `int` — Id of Permission
    
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

## Prioritypackages
<details><summary><code>client.prioritypackages.<a href="src/fern/prioritypackages/client.py">getprioritypackages</a>(...) -> ApiPagedResponseUpdateSystemModelsPriorityPackage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.prioritypackages.getprioritypackages()

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

**client_id:** `typing.Optional[str]` — Optional. Filter priority packages by ClientID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[PriorityPackagesGetPriorityPackagesRequestStatus]` — Optional. Filter returned packages by status. By default only active packages will be returned.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
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

<details><summary><code>client.prioritypackages.<a href="src/fern/prioritypackages/client.py">postprioritypackages</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.prioritypackages.postprioritypackages(
    client_id="ClientID",
    package_id="PackageID",
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

**request:** `UpdateSystemModelsPriorityPackage` 
    
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

<details><summary><code>client.prioritypackages.<a href="src/fern/prioritypackages/client.py">getprioritypackage</a>(...) -> UpdateSystemModelsPriorityPackage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.prioritypackages.getprioritypackage(
    id="ID",
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

**id:** `str` — The Priority Package ID
    
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

<details><summary><code>client.prioritypackages.<a href="src/fern/prioritypackages/client.py">deleteprioritypackages</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.prioritypackages.deleteprioritypackages(
    id="ID",
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

**id:** `str` — The Priority Package ID
    
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

## Release
<details><summary><code>client.release.<a href="src/fern/release/client.py">getreleases</a>(...) -> ApiPagedResponseContentSubmissionSharedBusinessEntitiesRelease</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a collection of Release. When successful, the response is a PagedResponse of Release.
            If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.release.getreleases()

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

**limit:** `typing.Optional[int]` — Optional. The page limit.  If not specified, the default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset.  If not specified, the default page offset is 0.
    
</dd>
</dl>

<dl>
<dd>

**visible:** `typing.Optional[bool]` — Optional. Filter by visible.
    
</dd>
</dl>

<dl>
<dd>

**bundle_id:** `typing.Optional[str]` — Optional. Filter by BundleID.
    
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

<details><summary><code>client.release.<a href="src/fern/release/client.py">postrelease</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a Release.  The body of the POST is the Release to create.
            The ReleaseId will be assigned on creation of the Job.  When successful, the response
            is the Release Id.  If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.release.postrelease()

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

**request:** `ContentSubmissionSharedBusinessEntitiesRelease` 
    
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

<details><summary><code>client.release.<a href="src/fern/release/client.py">getrelease</a>(...) -> ContentSubmissionSharedBusinessEntitiesRelease</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a Release by ID. When successful, the response is the requested Release.
            If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.release.getrelease(
    release_id=1,
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

**release_id:** `int` — The ID of the Release to get.
    
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

<details><summary><code>client.release.<a href="src/fern/release/client.py">postreleasebundle</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.release.postreleasebundle(
    release_id=1,
    bundle_id="BundleId",
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

**release_id:** `int` — The release identifier.
    
</dd>
</dl>

<dl>
<dd>

**bundle_id:** `str` — The bundle identifier.
    
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

<details><summary><code>client.release.<a href="src/fern/release/client.py">deletereleasebundle</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.release.deletereleasebundle(
    release_id=1,
    bundle_id="BundleId",
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

**release_id:** `int` — The release identifier.
    
</dd>
</dl>

<dl>
<dd>

**bundle_id:** `str` — The bundle identifier.
    
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

<details><summary><code>client.release.<a href="src/fern/release/client.py">putcontentdefinition</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a Release.  The body of the PUT is the updated Release.  
            When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.release.putcontentdefinition(
    release_id_=1,
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

**release_id:** `int` — The ID of the Release to update
    
</dd>
</dl>

<dl>
<dd>

**request:** `ContentSubmissionSharedBusinessEntitiesRelease` 
    
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

## Reporting
<details><summary><code>client.reporting.<a href="src/fern/reporting/client.py">bundlestatussummary</a>(...) -> ApiPagedResponseUpdateSystemModelsPackageStatusSummary</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.reporting.bundlestatussummary(
    bundle_id="BundleID",
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

**bundle_id:** `str` — The BundleID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
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

<details><summary><code>client.reporting.<a href="src/fern/reporting/client.py">bundlesinupdategroup</a>(...) -> ApiPagedResponseUpdateSystemModelsBundle</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.reporting.bundlesinupdategroup(
    id="ID",
    include_inactive=True,
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

**id:** `str` — The UpdateGroupID
    
</dd>
</dl>

<dl>
<dd>

**include_inactive:** `bool` — Include Inactive Bundles (true|false)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
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

<details><summary><code>client.reporting.<a href="src/fern/reporting/client.py">clientinfo</a>(...) -> UpdateSystemModelsClientInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.reporting.clientinfo(
    client_id="ClientID",
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

**client_id:** `str` — The Client ID
    
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

<details><summary><code>client.reporting.<a href="src/fern/reporting/client.py">currentpackagesinupdategroup</a>(...) -> typing.List[UpdateSystemModelsPackage]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.reporting.currentpackagesinupdategroup(
    id="ID",
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

**id:** `str` — The UpdateGroupID
    
</dd>
</dl>

<dl>
<dd>

**subscription_type_filter:** `typing.Optional[ReportingCurrentPackagesInUpdateGroupRequestSubscriptionTypeFilter]` — Optional.  The subscription type filter to use.  By default the Default packages (Required and IncludeByDefault) will be returned.
    
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

<details><summary><code>client.reporting.<a href="src/fern/reporting/client.py">getclient</a>(...) -> UpdateSystemModelsClient</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.reporting.getclient(
    id="ID",
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

**id:** `str` — The Client ID
    
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

<details><summary><code>client.reporting.<a href="src/fern/reporting/client.py">getsubscriptions</a>(...) -> ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.reporting.getsubscriptions()

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

**client_id:** `typing.Optional[str]` — Optional. Filter by Client ID
    
</dd>
</dl>

<dl>
<dd>

**update_group_id:** `typing.Optional[str]` — Optional. Filter by Update Group ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
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

<details><summary><code>client.reporting.<a href="src/fern/reporting/client.py">packagestatussummary</a>(...) -> UpdateSystemModelsPackageStatusSummary</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.reporting.packagestatussummary(
    package_id="PackageID",
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

**package_id:** `str` — The Package ID
    
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

<details><summary><code>client.reporting.<a href="src/fern/reporting/client.py">registeredclients</a>(...) -> ApiPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.reporting.registeredclients()

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

**update_group_id:** `typing.Optional[str]` — Optional but required when including any or all of following parameters: ReportValue, ReportResult, ReportResultIsValid. The Update Group ID. If not provided, all clients will be returned.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Optional. Filter where ClientID matches a value. Wildcards are supported (*).
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` — Optional. Filter where Tag matches a value. Wildcards are supported (*).
    
</dd>
</dl>

<dl>
<dd>

**report_result:** `typing.Optional[str]` — Optional and UpdateGroupID must be included. Filter where ReportResult matches a value. Wildcards are supported (*).
    
</dd>
</dl>

<dl>
<dd>

**report_result_is_valid:** `typing.Optional[bool]` — Optional and UpdateGroupID must be included. When 'true' filters results where ReportResult equals ReportResultExpected.  When 'false' filters results where ValueToValidate does not equal ReportResults.
    
</dd>
</dl>

<dl>
<dd>

**report_value:** `typing.Optional[str]` — Optional and UpdateGroupID must be included. Filter where ReportValue matches a value. Wildcards are supported (*).
    
</dd>
</dl>

<dl>
<dd>

**last_check_in_before:** `typing.Optional[datetime.datetime]` — Optional. Filter where LastCheckIn occured before the provided date.
    
</dd>
</dl>

<dl>
<dd>

**last_check_in_after:** `typing.Optional[datetime.datetime]` — Optional. Filter where LastCheckIn occured after the provided date.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 

Optional. Specify the order in which results should be returned. Use this format: [FieldName] [ASC|ASCENDING|DESC|DESCENDING],...   
            If sort direction is not provided for a field, it will be sorted ascending.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
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

<details><summary><code>client.reporting.<a href="src/fern/reporting/client.py">updategroups</a>(...) -> ApiPagedResponseUpdateSystemModelsUpdateGroup</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.reporting.updategroups()

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

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
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

<details><summary><code>client.reporting.<a href="src/fern/reporting/client.py">updatemetrics</a>(...) -> UpdateSystemModelsUpdateMetricsData</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.reporting.updatemetrics(
    update_group_id="UpdateGroupID",
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

**update_group_id:** `str` — The UpdateType in which clients must be for the report to include them.
    
</dd>
</dl>

<dl>
<dd>

**bundle_number:** `typing.Optional[int]` — Optional. Tells us which chart to show based upon filter.
    
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

## Roles
<details><summary><code>client.roles.<a href="src/fern/roles/client.py">getroles</a>(...) -> ApiPagedResponseApiModelsRole</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.roles.getroles()

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

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Optional. Finds a role with the given name.
    
</dd>
</dl>

<dl>
<dd>

**permission_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**permission_name:** `typing.Optional[str]` — Optional. Filters roles by whether they contain the provided permission.
    
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

<details><summary><code>client.roles.<a href="src/fern/roles/client.py">postrole</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.roles.postrole(
    description="Description",
    name="Name",
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

**request:** `ApiModelsRole` 
    
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

<details><summary><code>client.roles.<a href="src/fern/roles/client.py">getrole</a>(...) -> ApiModelsRole</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.roles.getrole(
    id=1,
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

**id:** `int` — The role's id
    
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

<details><summary><code>client.roles.<a href="src/fern/roles/client.py">putrole</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.roles.putrole(
    id_=1,
    description="Description",
    name="Name",
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

**id:** `int` — The role's id
    
</dd>
</dl>

<dl>
<dd>

**request:** `ApiModelsRole` 
    
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

<details><summary><code>client.roles.<a href="src/fern/roles/client.py">deleterole</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.roles.deleterole(
    id=1,
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

**id:** `int` — The role's id
    
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

<details><summary><code>client.roles.<a href="src/fern/roles/client.py">getrolepermissions</a>(...) -> ApiPagedResponseApiModelsPermission</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.roles.getrolepermissions(
    id=1,
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

**id:** `int` — The id of the Role
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter by permission name. Optional.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
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

<details><summary><code>client.roles.<a href="src/fern/roles/client.py">putrolepermissions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, ApiModelsRolePermissionChange, ApiModelsRolePermissionChangeAction
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.roles.putrolepermissions(
    id=1,
    request=[
        ApiModelsRolePermissionChange(
            action=ApiModelsRolePermissionChangeAction.GRANT,
            permission="Permission",
        )
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

**id:** `int` — The id of the Role
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[ApiModelsRolePermissionChange]` 
    
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

## Userpermissions
<details><summary><code>client.userpermissions.<a href="src/fern/userpermissions/client.py">getusers</a>(...) -> ApiPagedResponseApiModelsUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.userpermissions.getusers(
    id=1,
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

**id:** `int` — The Role's ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The page offset. The default page offset is 0.
    
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

<details><summary><code>client.userpermissions.<a href="src/fern/userpermissions/client.py">put</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, ApiModelsUserRoleChange, ApiModelsUserRoleChangeAction
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.userpermissions.put(
    id=1,
    request=[
        ApiModelsUserRoleChange(
            action=ApiModelsUserRoleChangeAction.GRANT,
            name="Name",
        )
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

**id:** `int` — The User's ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[ApiModelsUserRoleChange]` 
    
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

<details><summary><code>client.userpermissions.<a href="src/fern/userpermissions/client.py">getpermissions</a>(...) -> ApiPagedResponseApiModelsUserEffectivePermission</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.userpermissions.getpermissions(
    id=1,
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

**id:** `int` — The User's ID
    
</dd>
</dl>

<dl>
<dd>

**permission:** `typing.Optional[str]` — Filter by permission name. Supports ending wildcard (*). Optional.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The page offset. The default page offset is 0.
    
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

<details><summary><code>client.userpermissions.<a href="src/fern/userpermissions/client.py">getcurrentuserroles</a>(...) -> ApiPagedResponseApiModelsRole</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.userpermissions.getcurrentuserroles()

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

**role:** `typing.Optional[str]` — Filter by role name. Supports ending wildcard (*). Optional.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The page offset. The default page offset is 0.
    
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

<details><summary><code>client.userpermissions.<a href="src/fern/userpermissions/client.py">getroles</a>(...) -> ApiPagedResponseApiModelsRole</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.userpermissions.getroles(
    id=1,
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

**id:** `int` — The User's ID
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[str]` — Filter by role name. Supports ending wildcard (*). Optional.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The page offset. The default page offset is 0.
    
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

## Stringdefinitions
<details><summary><code>client.stringdefinitions.<a href="src/fern/stringdefinitions/client.py">getdefinitions</a>(...) -> ApiIPagedResponseGlobalResourcesSharedModelsStringDefinition</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.stringdefinitions.getdefinitions()

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

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10. Ignored if 'stringIds' is provided.
    
</dd>
</dl>

<dl>
<dd>

**modified_after_timestamp:** `typing.Optional[str]` — Optional. Return only the StringDefinition objects that have a Timestamp value greater than that provided. This will be an encoded byte array.
    
</dd>
</dl>

<dl>
<dd>

**include_translations:** `typing.Optional[bool]` — Optional. Indicates whether to include the StringTranslations for the StringDefinition. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**string_text:** `typing.Optional[str]` — Optional. The text for which to search in the StringDefinition object’s translations. Only StringDefinition objects for matching StringTranslation objects are returned. Does not filter if no value is provided. Supports beginning and/or ending wildcards. includeTranslations must be true.
    
</dd>
</dl>

<dl>
<dd>

**description_text:** `typing.Optional[str]` — Optional. The text for which to search in the StringDefinition description field. Only matching objects are returned. Does not filter if no value is provided. Supports beginning and/or ending wildcards.
    
</dd>
</dl>

<dl>
<dd>

**use_full_text:** `typing.Optional[bool]` — Optional. This flag is used to determin whether to use the FullText Search or not.
    
</dd>
</dl>

<dl>
<dd>

**include_deleted_languages:** `typing.Optional[bool]` — Optional. Indicates whether to include languages marked as deleted. includeTranslations must be true. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**language_ids:** `typing.Optional[str]` — Optional. A comma-delimited list of language ids. Only StringTranslation objects with a matching language id will be returned. Optional. By default all locales are returned. includeTranslations must be true. The StringDefinition is still returned even if the filtered translations list is empty.
    
</dd>
</dl>

<dl>
<dd>

**string_ids:** `typing.Optional[str]` — Optional. A comma-delimited list of string ids. Up to 40 string IDs may be provided. May not be used with 'modifiedAfterTimestamp', 'stringText', 'descriptionText', or 'useFullText'.
    
</dd>
</dl>

<dl>
<dd>

**matching_translations_only:** `typing.Optional[bool]` — Optional. If false, all translations for returned String Definitions are included. Must be used with 'stringText' provided and 'includeTranslations' = true.
    
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

<details><summary><code>client.stringdefinitions.<a href="src/fern/stringdefinitions/client.py">postdefinition</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, GlobalResourcesSharedModelsStringDefinition
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.stringdefinitions.postdefinition(
    request=[
        GlobalResourcesSharedModelsStringDefinition(
            description_for_translator="DescriptionForTranslator",
        )
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

**request:** `typing.List[GlobalResourcesSharedModelsStringDefinition]` 
    
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

<details><summary><code>client.stringdefinitions.<a href="src/fern/stringdefinitions/client.py">updatedefinitions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, GlobalResourcesSharedModelsStringDefinition
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.stringdefinitions.updatedefinitions(
    request=[
        GlobalResourcesSharedModelsStringDefinition(
            description_for_translator="DescriptionForTranslator",
        )
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

**request:** `typing.List[GlobalResourcesSharedModelsStringDefinition]` 
    
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

<details><summary><code>client.stringdefinitions.<a href="src/fern/stringdefinitions/client.py">getdefinition</a>(...) -> GlobalResourcesSharedModelsStringDefinition</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.stringdefinitions.getdefinition(
    id="ID",
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**include_translations:** `typing.Optional[bool]` — Optional. Indicates whether to include the StringTranslations for the StringDefinition. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**include_deleted_languages:** `typing.Optional[bool]` — Optional. Indicates whether to include languages marked as deleted. includeTranslations must be true. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**language_ids:** `typing.Optional[str]` — Optional. A comma-delimited list of language ids. Only StringTranslation objects with a matching language id will be returned. Optional. By default all locales are returned. includeTranslations must be true. The StringDefinition is still returned even if the filtered translations list is empty.
    
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

## Stringtranslations
<details><summary><code>client.stringtranslations.<a href="src/fern/stringtranslations/client.py">gettranslations</a>(...) -> ApiIPagedResponseGlobalResourcesSharedModelsStringTranslation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.stringtranslations.gettranslations()

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

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**modified_after_timestamp:** `typing.Optional[str]` — Optional. Return only the StringDefinition objects that have a Timestamp value greater than that provided. This will be an encoded byte array.
    
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

<details><summary><code>client.stringtranslations.<a href="src/fern/stringtranslations/client.py">updatetranslations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, GlobalResourcesSharedModelsStringTranslation
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.stringtranslations.updatetranslations(
    request=[
        GlobalResourcesSharedModelsStringTranslation(
            string_value="StringValue",
        )
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

**request:** `typing.List[GlobalResourcesSharedModelsStringTranslation]` 
    
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

<details><summary><code>client.stringtranslations.<a href="src/fern/stringtranslations/client.py">gettranslation</a>(...) -> GlobalResourcesSharedModelsStringTranslation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.stringtranslations.gettranslation(
    string_id="stringId",
    language_id=1,
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

**string_id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**language_id:** `int` — 
    
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

<details><summary><code>client.stringtranslations.<a href="src/fern/stringtranslations/client.py">updatetranslation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.stringtranslations.updatetranslation(
    string_id_="stringId",
    language_id_=1,
    string_value="StringValue",
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

**string_id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**language_id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request:** `GlobalResourcesSharedModelsStringTranslation` 
    
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

## Translationkeys
<details><summary><code>client.translationkeys.<a href="src/fern/translationkeys/client.py">get</a>(...) -> ApiIPagedResponseOasSupportSharedModelsTranslationKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


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
    environment=FernApiEnvironment.DEFAULT,
)

client.translationkeys.get()

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

**limit:** `typing.Optional[int]` — 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — 
    
</dd>
</dl>

<dl>
<dd>

**key_names:** `typing.Optional[str]` — Can filter by keyNames, a comma deliminated list.
    
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

<details><summary><code>client.translationkeys.<a href="src/fern/translationkeys/client.py">createtranslationkey</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.translationkeys.createtranslationkey(
    key_name="KeyName",
    string_id="StringID",
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

**request:** `OasSupportSharedModelsTranslationKey` 
    
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

<details><summary><code>client.translationkeys.<a href="src/fern/translationkeys/client.py">gettranslationkey</a>(...) -> OasSupportSharedModelsTranslationKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.translationkeys.gettranslationkey(
    id=1,
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

**id:** `int` — 
    
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

<details><summary><code>client.translationkeys.<a href="src/fern/translationkeys/client.py">updatetranslationkey</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.translationkeys.updatetranslationkey(
    id_=1,
    key_name="KeyName",
    string_id="StringID",
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

**id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request:** `OasSupportSharedModelsTranslationKey` 
    
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

## Translationrequests
<details><summary><code>client.translationrequests.<a href="src/fern/translationrequests/client.py">gettranslationrequests</a>(...) -> ApiIPagedResponseGlobalResourcesSharedModelsTranslationRequest</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.translationrequests.gettranslationrequests()

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

**limit:** `typing.Optional[int]` — 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — 
    
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

<details><summary><code>client.translationrequests.<a href="src/fern/translationrequests/client.py">createtranslationrequest</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, GlobalResourcesSharedModelsTranslationRequestState
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.translationrequests.createtranslationrequest(
    cc_email_addresses=[
        "CCEmailAddresses"
    ],
    charge_to_account="ChargeToAccount",
    deadline=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    locale_ids=[
        1
    ],
    notes="Notes",
    state=GlobalResourcesSharedModelsTranslationRequestState.NOT_SUBMITTED,
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

**request:** `GlobalResourcesSharedModelsTranslationRequest` 
    
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

<details><summary><code>client.translationrequests.<a href="src/fern/translationrequests/client.py">gettranslationrequest</a>(...) -> GlobalResourcesSharedModelsTranslationRequest</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.translationrequests.gettranslationrequest(
    id=1,
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

**id:** `int` — 
    
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

<details><summary><code>client.translationrequests.<a href="src/fern/translationrequests/client.py">updatetranslationrequest</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, GlobalResourcesSharedModelsTranslationRequestState
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.translationrequests.updatetranslationrequest(
    id_=1,
    cc_email_addresses=[
        "CCEmailAddresses"
    ],
    charge_to_account="ChargeToAccount",
    deadline=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    locale_ids=[
        1
    ],
    notes="Notes",
    state=GlobalResourcesSharedModelsTranslationRequestState.NOT_SUBMITTED,
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

**id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request:** `GlobalResourcesSharedModelsTranslationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**do_resend_request:** `typing.Optional[bool]` — 
    
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

<details><summary><code>client.translationrequests.<a href="src/fern/translationrequests/client.py">updatetranslationrequeststrings</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.translationrequests.updatetranslationrequeststrings(
    id=1,
    request=[
        "string"
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

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[str]` 
    
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

## Translationsets
<details><summary><code>client.translationsets.<a href="src/fern/translationsets/client.py">updatetranslationsetattributes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, GlobalResourcesSharedModelsTranslationSetAttribute
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.translationsets.updatetranslationsetattributes(
    request=[
        GlobalResourcesSharedModelsTranslationSetAttribute(
            name="Name",
        )
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

**request:** `typing.List[GlobalResourcesSharedModelsTranslationSetAttribute]` 
    
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

<details><summary><code>client.translationsets.<a href="src/fern/translationsets/client.py">updatetranslationsetattribute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.translationsets.updatetranslationsetattribute(
    id_=1,
    name="Name",
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

**id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request:** `GlobalResourcesSharedModelsTranslationSetAttribute` 
    
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

<details><summary><code>client.translationsets.<a href="src/fern/translationsets/client.py">deletetranslationsetattribute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.translationsets.deletetranslationsetattribute(
    id=1,
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

**id:** `int` — 
    
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

<details><summary><code>client.translationsets.<a href="src/fern/translationsets/client.py">gettranslationsets</a>(...) -> ApiIPagedResponseGlobalResourcesSharedModelsTranslationSet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.translationsets.gettranslationsets()

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

**limit:** `typing.Optional[int]` — 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — 
    
</dd>
</dl>

<dl>
<dd>

**translation_request_id:** `typing.Optional[int]` — 
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[TranslationSetsGetTranslationSetsRequestState]` — 
    
</dd>
</dl>

<dl>
<dd>

**string_id:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**language_id:** `typing.Optional[int]` — 
    
</dd>
</dl>

<dl>
<dd>

**include_attributes:** `typing.Optional[str]` — Names of Attributes to include when retrieving this submission. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.
    
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

<details><summary><code>client.translationsets.<a href="src/fern/translationsets/client.py">gettranslationset</a>(...) -> GlobalResourcesSharedModelsTranslationSet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.translationsets.gettranslationset(
    id=1,
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

**id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**include_attributes:** `typing.Optional[str]` — Names of Attributes to include when retrieving this Translation set. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.
    
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

<details><summary><code>client.translationsets.<a href="src/fern/translationsets/client.py">updatetranslationset</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, GlobalResourcesSharedModelsTranslationSetState
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.translationsets.updatetranslationset(
    id_=1,
    file_i_ds=[
        "FileIDs"
    ],
    state=GlobalResourcesSharedModelsTranslationSetState.OUT_FOR_PROCESSING,
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

**id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request:** `GlobalResourcesSharedModelsTranslationSet` 
    
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

<details><summary><code>client.translationsets.<a href="src/fern/translationsets/client.py">gettranslationsetattributes</a>(...) -> ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.translationsets.gettranslationsetattributes(
    id=1,
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

**id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — 
    
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

<details><summary><code>client.translationsets.<a href="src/fern/translationsets/client.py">posttranslationsetattribute</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.translationsets.posttranslationsetattribute(
    id_=1,
    name="Name",
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

**id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**request:** `GlobalResourcesSharedModelsTranslationSetAttribute` 
    
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

<details><summary><code>client.translationsets.<a href="src/fern/translationsets/client.py">posttranslationsetattributes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, GlobalResourcesSharedModelsTranslationSetAttribute
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.translationsets.posttranslationsetattributes(
    id=1,
    request=[
        GlobalResourcesSharedModelsTranslationSetAttribute(
            name="Name",
        )
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

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[GlobalResourcesSharedModelsTranslationSetAttribute]` 
    
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

<details><summary><code>client.translationsets.<a href="src/fern/translationsets/client.py">getsourcestrings</a>(...) -> ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.translationsets.getsourcestrings(
    id=1,
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

**id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — 
    
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

<details><summary><code>client.translationsets.<a href="src/fern/translationsets/client.py">getstatistics</a>(...) -> GlobalResourcesSharedModelsTranslationSetStatistics</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.translationsets.getstatistics(
    id=1,
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

**id:** `int` — 
    
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

<details><summary><code>client.translationsets.<a href="src/fern/translationsets/client.py">gettranslationsetstrings</a>(...) -> ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetString</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.translationsets.gettranslationsetstrings(
    id=1,
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

**id:** `int` — 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — 
    
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

<details><summary><code>client.translationsets.<a href="src/fern/translationsets/client.py">updatetranslationsetstrings</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, GlobalResourcesSharedModelsTranslationSetString
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.translationsets.updatetranslationsetstrings(
    id=1,
    request=[
        GlobalResourcesSharedModelsTranslationSetString(
            language_id=1,
            string_id="StringID",
            translation_set_id=1,
        )
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

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[GlobalResourcesSharedModelsTranslationSetString]` 
    
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

## Updategroupclientrelationships
<details><summary><code>client.updategroupclientrelationships.<a href="src/fern/updategroupclientrelationships/client.py">getsubscriptions</a>(...) -> ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.updategroupclientrelationships.getsubscriptions()

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

**client_id:** `typing.Optional[str]` — Optional. Filter by Client ID
    
</dd>
</dl>

<dl>
<dd>

**update_group_id:** `typing.Optional[str]` — Optional. Filter by Update Group ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Optional. Filter by Active
    
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

<details><summary><code>client.updategroupclientrelationships.<a href="src/fern/updategroupclientrelationships/client.py">postsubscription</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.updategroupclientrelationships.postsubscription(
    client_id="ClientID",
    update_group_id="UpdateGroupID",
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

**request:** `UpdateSystemModelsUpdateGroupClientRelationship` 
    
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

<details><summary><code>client.updategroupclientrelationships.<a href="src/fern/updategroupclientrelationships/client.py">putsubscriptionbyclientidupdategroupid</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.updategroupclientrelationships.putsubscriptionbyclientidupdategroupid(
    client_id="ClientID",
    update_group_id="UpdateGroupID",
    active=True,
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

**client_id:** `str` — The Client ID.  This can be a client ID that has not been registered yet.
    
</dd>
</dl>

<dl>
<dd>

**update_group_id:** `str` — The Update Group ID
    
</dd>
</dl>

<dl>
<dd>

**active:** `bool` — Subscribe the client to the Update Group.
    
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

<details><summary><code>client.updategroupclientrelationships.<a href="src/fern/updategroupclientrelationships/client.py">getsubscription</a>(...) -> UpdateSystemModelsUpdateGroupClientRelationship</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.updategroupclientrelationships.getsubscription(
    relationship_id="RelationshipID",
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

**relationship_id:** `str` — The RelationshipID.
    
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

<details><summary><code>client.updategroupclientrelationships.<a href="src/fern/updategroupclientrelationships/client.py">putsubscription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.updategroupclientrelationships.putsubscription(
    relationship_id_="RelationshipID",
    client_id="ClientID",
    update_group_id="UpdateGroupID",
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

**relationship_id:** `str` — The relationship id of the UpdateGroupClientRelationship
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateSystemModelsUpdateGroupClientRelationship` 
    
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

## Updategroupsubscriptions
<details><summary><code>client.updategroupsubscriptions.<a href="src/fern/updategroupsubscriptions/client.py">getupdategroupsubscriptions</a>(...) -> ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.updategroupsubscriptions.getupdategroupsubscriptions()

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

**update_group_id:** `typing.Optional[str]` — Optional. Filter by Update Group ID.
    
</dd>
</dl>

<dl>
<dd>

**package_type_id:** `typing.Optional[str]` — Optional. Filter by Package Type ID.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — Optional. Filter by Client ID.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
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

<details><summary><code>client.updategroupsubscriptions.<a href="src/fern/updategroupsubscriptions/client.py">postupdategroupsubscription</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.updategroupsubscriptions.postupdategroupsubscription(
    client_id="ClientID",
    include=True,
    package_type_id="PackageTypeID",
    update_group_id="UpdateGroupID",
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

**request:** `UpdateSystemModelsUpdateGroupSubscription` 
    
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

<details><summary><code>client.updategroupsubscriptions.<a href="src/fern/updategroupsubscriptions/client.py">postupdategroupsubscriptions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, UpdateSystemModelsUpdateGroupSubscription
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.updategroupsubscriptions.postupdategroupsubscriptions(
    request=[
        UpdateSystemModelsUpdateGroupSubscription(
            client_id="ClientID",
            include=True,
            package_type_id="PackageTypeID",
            update_group_id="UpdateGroupID",
        )
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

**request:** `typing.List[UpdateSystemModelsUpdateGroupSubscription]` 
    
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

<details><summary><code>client.updategroupsubscriptions.<a href="src/fern/updategroupsubscriptions/client.py">putupdategroupsubscriptions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, UpdateSystemModelsUpdateGroupSubscription
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.updategroupsubscriptions.putupdategroupsubscriptions(
    request=[
        UpdateSystemModelsUpdateGroupSubscription(
            client_id="ClientID",
            include=True,
            package_type_id="PackageTypeID",
            update_group_id="UpdateGroupID",
        )
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

**request:** `typing.List[UpdateSystemModelsUpdateGroupSubscription]` 
    
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

<details><summary><code>client.updategroupsubscriptions.<a href="src/fern/updategroupsubscriptions/client.py">getupdategroupsubscription</a>(...) -> UpdateSystemModelsUpdateGroupSubscription</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.updategroupsubscriptions.getupdategroupsubscription(
    update_group_subscription_id=1,
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

**update_group_subscription_id:** `int` — The Update Group Subscription ID
    
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

<details><summary><code>client.updategroupsubscriptions.<a href="src/fern/updategroupsubscriptions/client.py">putupdategroupsubscription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.updategroupsubscriptions.putupdategroupsubscription(
    update_group_subscription_id_=1,
    client_id="ClientID",
    include=True,
    package_type_id="PackageTypeID",
    update_group_id="UpdateGroupID",
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

**update_group_subscription_id:** `int` — The Update Group Subscription ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateSystemModelsUpdateGroupSubscription` 
    
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

<details><summary><code>client.updategroupsubscriptions.<a href="src/fern/updategroupsubscriptions/client.py">deleteupdategroupsubscription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.updategroupsubscriptions.deleteupdategroupsubscription(
    update_group_subscription_id=1,
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

**update_group_subscription_id:** `int` — The Update Group Subscription ID to delete
    
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

## Updategroups
<details><summary><code>client.updategroups.<a href="src/fern/updategroups/client.py">get</a>(...) -> UpdateSystemModelsUpdateGroup</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.updategroups.get(
    id="ID",
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

**id:** `str` — The ID of the Update Group
    
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

<details><summary><code>client.updategroups.<a href="src/fern/updategroups/client.py">post</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.updategroups.post(
    description="Description",
    priority=1,
    update_type="UpdateType",
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

**request:** `UpdateSystemModelsUpdateGroup` 
    
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

<details><summary><code>client.updategroups.<a href="src/fern/updategroups/client.py">put</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.updategroups.put(
    id_="ID",
    description="Description",
    priority=1,
    update_type="UpdateType",
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

**id:** `str` — ID of the Update Group
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateSystemModelsUpdateGroup` 
    
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

<details><summary><code>client.updategroups.<a href="src/fern/updategroups/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.updategroups.delete(
    id="ID",
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

**id:** `str` — The ID of the Update Group to Delete
    
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

<details><summary><code>client.updategroups.<a href="src/fern/updategroups/client.py">getupdategroupbundles</a>(...) -> ApiPagedResponseUpdateSystemModelsBundle</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.updategroups.getupdategroupbundles(
    id="ID",
    include_inactive=True,
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

**id:** `str` — The UpdateGroupID
    
</dd>
</dl>

<dl>
<dd>

**include_inactive:** `bool` — Include Inactive Bundles (true|false)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
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

<details><summary><code>client.updategroups.<a href="src/fern/updategroups/client.py">addupdategroupuser</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.updategroups.addupdategroupuser(
    id="id",
    user_id=1,
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

**id:** `str` — The ID of the update group
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `int` — The userID to link to the update group
    
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

<details><summary><code>client.updategroups.<a href="src/fern/updategroups/client.py">removeupdategroupuser</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.updategroups.removeupdategroupuser(
    id="id",
    user_id=1,
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

**id:** `str` — The ID of the update group
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `int` — The userID to link to the update group
    
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

## Usercontentdefinitions
<details><summary><code>client.usercontentdefinitions.<a href="src/fern/usercontentdefinitions/client.py">getusercontentdefinitions</a>(...) -> ApiPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a collection of UserContentDefinitions. When successful, the response is a PagedResponse of UserContentDefinitions.
            If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.usercontentdefinitions.getusercontentdefinitions()

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

**limit:** `typing.Optional[int]` — Optional. The page limit.  If not specified, the default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset.  If not specified, the default page offset is 0.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[int]` — Optional. Filter by UserID.
    
</dd>
</dl>

<dl>
<dd>

**content_definition_id:** `typing.Optional[int]` — Optional. Filter by ContentDefinitionID
    
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

<details><summary><code>client.usercontentdefinitions.<a href="src/fern/usercontentdefinitions/client.py">postusercontentdefinition</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a UserContentDefinition.  The body of the POST is the UserContentDefinition to create.
            The UserContentDefinitionID will be assigned on creation of the Job.  When successful, the response
            is the UserContentDefinitionID.  If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.usercontentdefinitions.postusercontentdefinition()

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

**request:** `ContentSubmissionSharedBusinessEntitiesUserContentDefinition` 
    
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

<details><summary><code>client.usercontentdefinitions.<a href="src/fern/usercontentdefinitions/client.py">getusercontentdefinition</a>(...) -> ContentSubmissionSharedBusinessEntitiesUserContentDefinition</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a UserContentDefinition by ID. When successful, the response is the requested UserContentDefinition.
            If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.usercontentdefinitions.getusercontentdefinition(
    user_content_definition_id=1,
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

**user_content_definition_id:** `int` — The ID of the UserContentDefinition to get.
    
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

<details><summary><code>client.usercontentdefinitions.<a href="src/fern/usercontentdefinitions/client.py">deleteusercontentdefinition</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an UserContentDefinition. When successful, the response is empty.  If unsuccessful, an appropriate
            ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.usercontentdefinitions.deleteusercontentdefinition(
    user_content_definition_id=1,
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

**user_content_definition_id:** `int` — The ID of the UserContentDefinition to delete
    
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

## Users
<details><summary><code>client.users.<a href="src/fern/users/client.py">get</a>(...) -> ApiModelsUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.get(
    id=1,
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

**id:** `int` — The user ID
    
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

<details><summary><code>client.users.<a href="src/fern/users/client.py">post</a>(...) -> ApiModelsUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.post()

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

**request:** `ApiModelsUser` 
    
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

<details><summary><code>client.users.<a href="src/fern/users/client.py">getcurrentuser</a>() -> ApiModelsUser</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.getcurrentuser()

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

<details><summary><code>client.users.<a href="src/fern/users/client.py">putcurrentuser</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.putcurrentuser()

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

**request:** `ApiModelsUser` 
    
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

<details><summary><code>client.users.<a href="src/fern/users/client.py">put</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.put(
    id=1,
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

**id:** `int` — The user id
    
</dd>
</dl>

<dl>
<dd>

**request:** `ApiModelsUser` 
    
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

<details><summary><code>client.users.<a href="src/fern/users/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.delete(
    id=1,
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

**id:** `int` — The user id
    
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

## Voucherhistory
<details><summary><code>client.voucherhistory.<a href="src/fern/voucherhistory/client.py">getvoucherhistory</a>(...) -> ApiPagedResponseDealerDbModelsVoucherHistory</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.voucherhistory.getvoucherhistory()

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

**voucher_code:** `typing.Optional[str]` — Optional. Filter history data by Voucher Code.
    
</dd>
</dl>

<dl>
<dd>

**changed_before:** `typing.Optional[datetime.datetime]` — Optional. Filter history data where changes occured before provided date.
    
</dd>
</dl>

<dl>
<dd>

**changed_after:** `typing.Optional[datetime.datetime]` — Optional. Filter history data where changes occured after provided date.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
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

## Vouchers
<details><summary><code>client.vouchers.<a href="src/fern/vouchers/client.py">get</a>(...) -> DealerDbModelsVoucher</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.vouchers.get(
    voucher_code="VoucherCode",
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

**voucher_code:** `str` — The voucher code of the voucher to get.
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[VouchersGetRequestDeleted]` — Optional. Filter vouchers by Deleted state. By default only vouchers that are not deleted are returned.
    
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

<details><summary><code>client.vouchers.<a href="src/fern/vouchers/client.py">post</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.vouchers.post()

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

**request:** `DealerDbModelsVoucher` 
    
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

<details><summary><code>client.vouchers.<a href="src/fern/vouchers/client.py">put</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.vouchers.put(
    voucher_code_="VoucherCode",
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

**voucher_code:** `str` — The voucher code of the voucher to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `DealerDbModelsVoucher` 
    
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

<details><summary><code>client.vouchers.<a href="src/fern/vouchers/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.vouchers.delete(
    voucher_code="VoucherCode",
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

**voucher_code:** `str` — The voucher code of the voucher to delete.
    
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

<details><summary><code>client.vouchers.<a href="src/fern/vouchers/client.py">getvoucherhistory</a>(...) -> ApiPagedResponseDealerDbModelsVoucherHistory</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.vouchers.getvoucherhistory(
    voucher_code="VoucherCode",
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

**voucher_code:** `str` — The voucher code to get history for.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional. The page limit. The default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset. The default page offset is 0.
    
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

## Activities
<details><summary><code>client.activities.<a href="src/fern/activities/client.py">getactivities</a>(...) -> ApiPagedResponseBuildSystemSharedDtoActivity</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a collection of Activities. When successful, the response is a PagedResponse of Activities.  
            If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.activities.getactivities()

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

**limit:** `typing.Optional[int]` — Optional. The page limit.  If not specified, the default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset.  If not specified, the default page offset is 0.
    
</dd>
</dl>

<dl>
<dd>

**is_include_deleted:** `typing.Optional[bool]` — Does it include deleted activity, or not
    
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

<details><summary><code>client.activities.<a href="src/fern/activities/client.py">postactivity</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an Activity.  The body of the POST is the Activity to create.  The ActivityID will be assigned
            on creation of the Activity.  When successful, the response is the ActivityID.  If unsuccessful, an 
            appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.activities.postactivity()

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

**request:** `BuildSystemSharedDtoActivity` 
    
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

<details><summary><code>client.activities.<a href="src/fern/activities/client.py">getactivity</a>(...) -> BuildSystemSharedDtoActivity</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets an Activity by ID. When successful, the response is the requested Activity.  If unsuccessful,
            an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.activities.getactivity(
    activity_id=1,
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

**activity_id:** `int` — The ID of the Activity to get.
    
</dd>
</dl>

<dl>
<dd>

**is_include_deleted:** `typing.Optional[bool]` — Does it include deleted activity, or not
    
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

<details><summary><code>client.activities.<a href="src/fern/activities/client.py">putactivity</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an Activity.  The body of the PUT is the updated Activity.  When successful, the response is empty.
            If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.activities.putactivity(
    activity_id_=1,
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

**activity_id:** `int` — The id of the activity to update
    
</dd>
</dl>

<dl>
<dd>

**request:** `BuildSystemSharedDtoActivity` 
    
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

<details><summary><code>client.activities.<a href="src/fern/activities/client.py">deleteactivity</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an Activity. When successful, the response is empty.  If unsuccessful, an appropriate
            ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.activities.deleteactivity(
    activity_id=1,
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

**activity_id:** `int` — The id of the activity to delete
    
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

## Activityruns
<details><summary><code>client.activityruns.<a href="src/fern/activityruns/client.py">getactivityruns</a>(...) -> ApiPagedResponseBuildSystemSharedDtoActivityRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a collection of ActivityRuns. When successful, the response is a PagedResponse of ActivityRuns.  
            If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.activityruns.getactivityruns()

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

**limit:** `typing.Optional[int]` — Optional. The page limit.  If not specified, the default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset.  If not specified, the default page offset is 0.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ActivityRunsGetActivityRunsRequestStatus]` 

Optional. Filter activity runs by status.  Value should be a comma separated list of status to include.
            If not specified, the default status filter is “InProgress”.
    
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

<details><summary><code>client.activityruns.<a href="src/fern/activityruns/client.py">getactivityrun</a>(...) -> BuildSystemSharedDtoActivityRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets an ActivityRun by ID. When successful, the response is the requested ActivityRun.  If unsuccessful,
            an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.activityruns.getactivityrun(
    activity_run_id=1,
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

**activity_run_id:** `int` — The ID of the ActivityRun to get.
    
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

<details><summary><code>client.activityruns.<a href="src/fern/activityruns/client.py">putactivityrun</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the ActivityRunStatus of an ActivityRun.  The body of the PUT is the updated ActivityRunStatus.
            When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.
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
from fern import FernApi, BuildSystemSharedDtoActivityRunStatus
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.activityruns.putactivityrun(
    activity_run_id_=1,
    status=BuildSystemSharedDtoActivityRunStatus(),
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

**activity_run_id:** `int` — The ID of the ActivityRun to update ActivityRunStatus for.
    
</dd>
</dl>

<dl>
<dd>

**request:** `BuildSystemSharedDtoActivityRun` 
    
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

<details><summary><code>client.activityruns.<a href="src/fern/activityruns/client.py">getactivityrunstatus</a>(...) -> BuildSystemSharedDtoActivityRunStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the ActivityRunStatus of an ActivityRun.  When successful, the response is the requested ActivityRunStatus.
            If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.activityruns.getactivityrunstatus(
    activity_run_id=1,
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

**activity_run_id:** `int` — The ID of the ActivityRun to get ActivityRunStatus for.
    
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

<details><summary><code>client.activityruns.<a href="src/fern/activityruns/client.py">putactivityrunstatus</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the ActivityRunStatus of an ActivityRun.  The body of the PUT is the updated ActivityRunStatus.
            When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.activityruns.putactivityrunstatus(
    activity_run_id=1,
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

**activity_run_id:** `int` — The ID of the ActivityRun to update ActivityRunStatus for.
    
</dd>
</dl>

<dl>
<dd>

**request:** `BuildSystemSharedDtoActivityRunStatus` 
    
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

## Agents
<details><summary><code>client.agents.<a href="src/fern/agents/client.py">getagents</a>(...) -> ApiPagedResponseBuildSystemSharedDtoAgent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a collection of Agents. When successful, the response is a PagedResponse of Agents.  
            If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.agents.getagents()

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

**limit:** `typing.Optional[int]` — Optional. The page limit.  If not specified, the default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset.  If not specified, the default page offset is 0.
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">postagent</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an Agent.  The body of the POST is the Agent to create.  The AgentID will be assigned
            on creation of the Agent.  When successful, the response is the AgentID.  If unsuccessful, an
            appropriate ApiError is returned.
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
from fern import FernApi, BuildSystemSharedDtoAgentStatus
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.agents.postagent(
    keep_alive_interval=1,
    machine_name="MachineName",
    status=BuildSystemSharedDtoAgentStatus(
        online=True,
    ),
    user_id=1,
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

**request:** `BuildSystemSharedDtoAgent` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">getcurrentagentasync</a>() -> BuildSystemSharedDtoAgent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the Agent associated with the current user. When successful, the response is the requested Agent.  If unsuccessful,
            an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.agents.getcurrentagentasync()

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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">getcurrentagentactivityrun</a>() -> BuildSystemSharedDtoActivityRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the activity run assigned to an agent.  When successful, the response is the ActivityRun
            assigned to the Agent.  If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.agents.getcurrentagentactivityrun()

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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">getagentasync</a>(...) -> BuildSystemSharedDtoAgent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets an Agent by ID. When successful, the response is the requested Agent.  If unsuccessful,
            an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.agents.getagentasync(
    agent_id=1,
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

**agent_id:** `int` — The id of the Agent to get.
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">putagent</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an Agent.  The body of the PUT is the updated Agent.  When successful, the response is empty.
            If unsuccessful, an appropriate ApiError is returned.
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
from fern import FernApi, BuildSystemSharedDtoAgentStatus
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.agents.putagent(
    agent_id_=1,
    keep_alive_interval=1,
    machine_name="MachineName",
    status=BuildSystemSharedDtoAgentStatus(
        online=True,
    ),
    user_id=1,
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

**agent_id:** `int` — The id of the Agent to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `BuildSystemSharedDtoAgent` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">deleteagent</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an Agent. When successful, the response is empty.  If unsuccessful, an appropriate
            ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.agents.deleteagent(
    agent_id=1,
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

**agent_id:** `int` — The id of the Agent to delete.
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">getagentactivityrun</a>(...) -> BuildSystemSharedDtoActivityRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the activity run assigned to an agent.  When successful, the response is the ActivityRun
            assigned to the Agent.  If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.agents.getagentactivityrun(
    agent_id=1,
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

**agent_id:** `int` — The id of the Agent to get.
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">putagentactivityrun</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
from fern import FernApi, BuildSystemSharedDtoActivityRunStatus
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.agents.putagentactivityrun(
    agent_id=1,
    status=BuildSystemSharedDtoActivityRunStatus(),
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

**agent_id:** `int` — The id of the Agent to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `BuildSystemSharedDtoActivityRun` 
    
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

<details><summary><code>client.agents.<a href="src/fern/agents/client.py">putagentstatus</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the status of an Agent.The body of the PUT is the updated Agent status.  When successful,
            the response is empty.If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.agents.putagentstatus(
    agent_id=1,
    online=True,
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

**agent_id:** `int` — The id of the Agent to update.
    
</dd>
</dl>

<dl>
<dd>

**request:** `BuildSystemSharedDtoAgentStatus` 
    
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

## Jobruns
<details><summary><code>client.jobruns.<a href="src/fern/jobruns/client.py">getjobruns</a>(...) -> ApiPagedResponseBuildSystemSharedDtoJobRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a collection of JobRuns. When successful, the response is a PagedResponse of JobRuns.
            If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.jobruns.getjobruns()

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

**limit:** `typing.Optional[int]` — Optional. The page limit.  If not specified, the default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset.  If not specified, the default page offset is 0.
    
</dd>
</dl>

<dl>
<dd>

**include_activity_run_details:** `typing.Optional[bool]` — Optional. Indicates whether to include ActivityRun details.  Defaults to false.
    
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

<details><summary><code>client.jobruns.<a href="src/fern/jobruns/client.py">postjobrun</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a JobRun.  The body of the POST is the JobRun to create.  The JobRunID will be assigned on
            creation of the JobRun.  When successful, the response is the JobRunID.  If unsuccessful, an 
            appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.jobruns.postjobrun()

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

**request:** `BuildSystemSharedDtoJobRun` 
    
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

<details><summary><code>client.jobruns.<a href="src/fern/jobruns/client.py">getjobrun</a>(...) -> BuildSystemSharedDtoJobRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a JobRun by ID. When successful, the response is the requested JobRun.
            If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.jobruns.getjobrun(
    job_run_id=1,
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

**job_run_id:** `int` — The ID of the JobRun to get.
    
</dd>
</dl>

<dl>
<dd>

**include_activity_run_details:** `typing.Optional[bool]` — Optional. Indicates whether to include ActivityRun details.  Defaults to false.
    
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

<details><summary><code>client.jobruns.<a href="src/fern/jobruns/client.py">putjobrun</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

/// 
            Updates a JobRun.  The body of the PUT is the updated JobRun.
            When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.jobruns.putjobrun(
    job_run_id_=1,
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

**job_run_id:** `int` — The id of the JobRun to update
    
</dd>
</dl>

<dl>
<dd>

**request:** `BuildSystemSharedDtoJobRun` 
    
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

<details><summary><code>client.jobruns.<a href="src/fern/jobruns/client.py">deletejobrun</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a JobRun. When successful, the response is empty.  If unsuccessful, an appropriate
            ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.jobruns.deletejobrun(
    job_run_id=1,
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

**job_run_id:** `int` — The id of the JobRun to delete
    
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

## Jobs
<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">getjobs</a>(...) -> ApiPagedResponseBuildSystemSharedDtoJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a collection of Jobs. When successful, the response is a PagedResponse of Jobs.
            If unsuccessful, an appropriate ApiError is returned. 
            ///
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
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.getjobs()

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

**limit:** `typing.Optional[int]` — Optional. The page limit.  If not specified, the default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset.  If not specified, the default page offset is 0.
    
</dd>
</dl>

<dl>
<dd>

**is_include_deleted:** `typing.Optional[bool]` — Does it include deleted job, or not
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">postjob</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a Job.  The body of the POST is the Job to create.  The JobID will be assigned on
            creation of the Job.  When successful, the response is the JobID.  If unsuccessful, an 
            appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.postjob()

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

**request:** `BuildSystemSharedDtoJob` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">getjob</a>(...) -> BuildSystemSharedDtoJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a Job by ID. When successful, the response is the requested Job.
            If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.getjob(
    job_id=1,
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

**job_id:** `int` — The ID of the Job to get.
    
</dd>
</dl>

<dl>
<dd>

**is_include_deleted:** `typing.Optional[bool]` — Does it include deleted job, or not
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">putjob</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a Job.  The body of the PUT is the updated Job.  When successful, the response is empty.
            If unsuccessful, an appropriate ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.putjob(
    job_id_=1,
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

**job_id:** `int` — The id of the job to update
    
</dd>
</dl>

<dl>
<dd>

**request:** `BuildSystemSharedDtoJob` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">deletejob</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a Job. When successful, the response is empty.  If unsuccessful, an appropriate
            ApiError is returned.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.deletejob(
    job_id=1,
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

**job_id:** `int` — The id of the job to delete
    
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

## Steps
<details><summary><code>client.steps.<a href="src/fern/steps/client.py">getsteps</a>(...) -> ApiPagedResponseBuildSystemSharedDtoStep</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a collection of Steps. When successful, the response is a PagedResponse of Steps.
            If unsuccessful, an appropriate ApiError is returned.  Steps.Read permission is required.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.steps.getsteps()

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

**limit:** `typing.Optional[int]` — Optional. The page limit.  If not specified, the default page limit is 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Optional. The page offset.  If not specified, the default page offset is 0.
    
</dd>
</dl>

<dl>
<dd>

**include_deleted:** `typing.Optional[bool]` — Does it include deleted step, or not
    
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

<details><summary><code>client.steps.<a href="src/fern/steps/client.py">poststep</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.steps.poststep(
    config_required=True,
    implementation_id="ImplementationID",
    name="Name",
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

**request:** `BuildSystemSharedDtoStep` 
    
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

<details><summary><code>client.steps.<a href="src/fern/steps/client.py">getstep</a>(...) -> BuildSystemSharedDtoStep</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a Step by ID. When successful, the response is the requested Step.
            If unsuccessful, an appropriate ApiError is returned.  Steps.Read permission is required.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.steps.getstep(
    step_id=1,
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

**step_id:** `int` — The ID of the Step to get.
    
</dd>
</dl>

<dl>
<dd>

**is_include_deleted:** `typing.Optional[bool]` — Does it include deleted step, or not
    
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

<details><summary><code>client.steps.<a href="src/fern/steps/client.py">putstep</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

No Documentation Found.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.steps.putstep(
    step_id_=1,
    config_required=True,
    implementation_id="ImplementationID",
    name="Name",
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

**step_id:** `int` — The step ID of the step to update
    
</dd>
</dl>

<dl>
<dd>

**request:** `BuildSystemSharedDtoStep` 
    
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

