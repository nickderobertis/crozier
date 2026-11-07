# Reference
## auth
<details><summary><code>client.auth.<a href="src/fern/auth/client.py">create_token</a>(...) -> CreateTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a new token to access REST API
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TokenRequestTokenScope
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.auth.create_token(
    token_name="token_name",
    token_scope=TokenRequestTokenScope.READ,
    token_expire=datetime.date.fromisoformat("2023-01-15"),
    username="username",
    password="password",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token_name:** `str` — Friendly name of the token
    
</dd>
</dl>

<dl>
<dd>

**token_scope:** `TokenRequestTokenScope` — The scope of the token.
    
</dd>
</dl>

<dl>
<dd>

**token_expire:** `datetime.date` — Date when the token must expire (default max 30 days).
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` — Username of the login user.
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — Password of the user trying to login.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## info
<details><summary><code>client.info.<a href="src/fern/info/client.py">get_info</a>() -> ApiInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the current API version, supported authentication methods and description
</dd>
</dl>
</dd>
</dl>

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

client.info.get_info()

```
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

<details><summary><code>client.info.<a href="src/fern/info/client.py">get_open_api</a>() -> ApIinfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the current API documentation as a response with content negotiation.
</dd>
</dl>
</dd>
</dl>

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

client.info.get_open_api()

```
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

<details><summary><code>client.info.<a href="src/fern/info/client.py">get_health</a>() -> HealthInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check if API is ready to accept requests or not
</dd>
</dl>
</dd>
</dl>

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

client.info.get_health()

```
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

<details><summary><code>client.info.<a href="src/fern/info/client.py">get_banner_message</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Banner message from the server
</dd>
</dl>
</dd>
</dl>

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

client.info.get_banner_message()

```
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

## Maintenance
<details><summary><code>client.maintenance.<a href="src/fern/maintenance/client.py">initiate_maintenance</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Perform maintenance operations corresponding to the user options.
</dd>
</dl>
</dd>
</dl>

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

client.maintenance.initiate_maintenance()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**options:** `typing.Optional[typing.List[CreateMaintenanceOptionsItem]]` — options list
    
</dd>
</dl>

<dl>
<dd>

**logs_date:** `typing.Optional[str]` — Date from which to remove older gold files from repository.
    
</dd>
</dl>

<dl>
<dd>

**gold_date:** `typing.Optional[str]` — Date from which to remove older log files from repository.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Admin
<details><summary><code>client.admin.<a href="src/fern/admin/client.py">get_obligations_list</a>() -> ObligationsList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the list of obligations in the server.
</dd>
</dl>
</dd>
</dl>

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

client.admin.get_obligations_list()

```
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

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">get_obligations_data</a>(...) -> ObligationExtended</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the details of a particular obligation from the server.
</dd>
</dl>
</dd>
</dl>

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

client.admin.get_obligations_data(
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

**id:** `int` — Id of the obligation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">delete_obligations_data</a>(...) -> typing.List[Info]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a particular obligation from the server.
</dd>
</dl>
</dd>
</dl>

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

client.admin.delete_obligations_data(
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

**id:** `int` — Id of the obligation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">get_all_obligations_data</a>() -> typing.List[ObligationExtended]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the details of all obligations from the server.
</dd>
</dl>
</dd>
</dl>

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

client.admin.get_all_obligations_data()

```
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

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">get_customise_data</a>() -> typing.List[Customise]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the admin configuration data from the server
</dd>
</dl>
</dd>
</dl>

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

client.admin.get_customise_data()

```
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

<details><summary><code>client.admin.<a href="src/fern/admin/client.py">update_customise_data</a>(...) -> typing.List[Info]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the admin configuration data.
</dd>
</dl>
</dd>
</dl>

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

client.admin.update_customise_data()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `typing.Optional[str]` — Key of the field to be updated
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` — Value of the field to be updated
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## License
<details><summary><code>client.license.<a href="src/fern/license/client.py">import_obligation_csv</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import an obligation csv file
</dd>
</dl>
</dd>
</dl>

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

client.license.import_obligation_csv(
    file_input="example_file_input",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_input:** `core.File` — CSV to be imported
    
</dd>
</dl>

<dl>
<dd>

**enclosure:** `typing.Optional[str]` — Enclosure for string in CSV
    
</dd>
</dl>

<dl>
<dd>

**delimiter:** `typing.Optional[str]` — Delimiters for fields in CSV
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.license.<a href="src/fern/license/client.py">export_license_obligations</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Export a csv license obligation list
</dd>
</dl>
</dd>
</dl>

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

client.license.export_license_obligations()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[int]` — Obligation id to export, 0 for all
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.license.<a href="src/fern/license/client.py">import_obligations_from_json</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import an obligation json file
</dd>
</dl>
</dd>
</dl>

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

client.license.import_obligations_from_json(
    file_input="example_fileInput",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_input:** `core.File` — JSON to be imported
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.license.<a href="src/fern/license/client.py">export_obligations_to_json</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Export a json license obligation list
</dd>
</dl>
</dd>
</dl>

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

client.license.export_obligations_to_json()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[int]` — Obligation id to export, 0 for all
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.license.<a href="src/fern/license/client.py">get_licenses</a>(...) -> typing.List[GetLicensesResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of available licenses (filtered by kind or status)
</dd>
</dl>
</dd>
</dl>

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

client.license.get_licenses()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**kind:** `typing.Optional[GetLicensesRequestKind]` — Which kind of licenses to get.
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number to fetch
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits of responses per request
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Get only active licenses
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.license.<a href="src/fern/license/client.py">create_license</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new license to the database
</dd>
</dl>
</dd>
</dl>

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

client.license.create_license(
    short_name="MIT",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**short_name:** `str` — Short name
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose
    
</dd>
</dl>

<dl>
<dd>

**merge_request:** `typing.Optional[bool]` — Open a merge request for candidate license?
    
</dd>
</dl>

<dl>
<dd>

**full_name:** `typing.Optional[str]` — Full name
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[str]` — License text
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — URL of the license text
    
</dd>
</dl>

<dl>
<dd>

**risk:** `typing.Optional[int]` — Risk level
    
</dd>
</dl>

<dl>
<dd>

**is_candidate:** `typing.Optional[bool]` — Is the license a candidate?
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.license.<a href="src/fern/license/client.py">import_license</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import a csv license to the database
</dd>
</dl>
</dd>
</dl>

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

client.license.import_license(
    file_input="example_file_input",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_input:** `core.File` — CSV to be imported
    
</dd>
</dl>

<dl>
<dd>

**enclosure:** `typing.Optional[str]` — Enclosure for string in CSV
    
</dd>
</dl>

<dl>
<dd>

**delimiter:** `typing.Optional[str]` — Delimiters for fields in CSV
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.license.<a href="src/fern/license/client.py">export_license</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Export a csv license
</dd>
</dl>
</dd>
</dl>

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

client.license.export_license()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[int]` — License id to export, 0 for all
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.license.<a href="src/fern/license/client.py">handle_import_license</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import a json license to the database
</dd>
</dl>
</dd>
</dl>

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

client.license.handle_import_license(
    file_input="example_fileInput",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_input:** `core.File` — JSON to be imported
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.license.<a href="src/fern/license/client.py">export_admin_license_to_json</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Export a json license
</dd>
</dl>
</dd>
</dl>

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

client.license.export_admin_license_to_json()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[int]` — License id to export, 0 for all
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.license.<a href="src/fern/license/client.py">get_license_by_shortname</a>(...) -> GetLicenseByShortnameResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific license
</dd>
</dl>
</dd>
</dl>

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

client.license.get_license_by_shortname(
    shortname="shortname",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**shortname:** `str` — Shortname of the license
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.license.<a href="src/fern/license/client.py">update_license_by_shortname</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update information about a given license
</dd>
</dl>
</dd>
</dl>

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

client.license.update_license_by_shortname(
    shortname="shortname",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**shortname:** `str` — Shortname of the license
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose
    
</dd>
</dl>

<dl>
<dd>

**full_name:** `typing.Optional[str]` — New fullname
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[str]` — New license text
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — New URL for license
    
</dd>
</dl>

<dl>
<dd>

**risk:** `typing.Optional[int]` — New risk value
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.license.<a href="src/fern/license/client.py">get_admin_license_candidates</a>() -> typing.List[LicenseCandidate]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of license candidates from the database.
</dd>
</dl>
</dd>
</dl>

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

client.license.get_admin_license_candidates()

```
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

<details><summary><code>client.license.<a href="src/fern/license/client.py">delete_by_license_candidate_id</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a single admin-license-candidate by the given id.
</dd>
</dl>
</dd>
</dl>

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

client.license.delete_by_license_candidate_id(
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

**id:** `int` — Id of the license-candidate
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.license.<a href="src/fern/license/client.py">get_admin_license_acknowledgements</a>() -> typing.List[AdminLicenseAcknowledgement]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of the admin license acknowledgements
</dd>
</dl>
</dd>
</dl>

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

client.license.get_admin_license_acknowledgements()

```
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

<details><summary><code>client.license.<a href="src/fern/license/client.py">mutate_admin_license_acknowledgement</a>(...) -> typing.List[Info]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add, edit and toggle admin-license acknowledgement
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, MutateAdminAcknowledgement
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.license.mutate_admin_license_acknowledgement(
    request=[
        MutateAdminAcknowledgement()
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

**request:** `typing.List[MutateAdminAcknowledgement]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.license.<a href="src/fern/license/client.py">get_all_standard_license_comments</a>() -> typing.List[StandardComment]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all standard license comments.
</dd>
</dl>
</dd>
</dl>

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

client.license.get_all_standard_license_comments()

```
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

<details><summary><code>client.license.<a href="src/fern/license/client.py">mutate_std_comments</a>(...) -> typing.List[Info]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add, edit and toggle standard comments
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, MutateStdComment
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.license.mutate_std_comments(
    request=[
        MutateStdComment()
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

**request:** `typing.List[MutateStdComment]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.license.<a href="src/fern/license/client.py">verify_license</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verify a license as new or variant of another license
</dd>
</dl>
</dd>
</dl>

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

client.license.verify_license(
    shortname="shortname",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**shortname:** `str` — Shortname of the license to be verified
    
</dd>
</dl>

<dl>
<dd>

**parent_shortname:** `typing.Optional[str]` — Shortname of the parent license
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.license.<a href="src/fern/license/client.py">merge_license</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Merge a license to another existing license
</dd>
</dl>
</dd>
</dl>

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

client.license.merge_license(
    shortname="shortname",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**shortname:** `str` — Shortname of the license to be merged
    
</dd>
</dl>

<dl>
<dd>

**parent_shortname:** `typing.Optional[str]` — Shortname of the parent license
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.license.<a href="src/fern/license/client.py">get_suggested_license</a>(...) -> GetSuggestedLicense</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single suggested license by the given reference text.
</dd>
</dl>
</dd>
</dl>

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

client.license.get_suggested_license()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**reference_text:** `typing.Optional[str]` — Reference text to get suggested license
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Upload
<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_upload_by_id</a>(...) -> Upload</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single upload
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_upload_by_id(
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

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while accessing the package
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">move_upload_by_id</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Copy or move an upload by id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.upload import MoveUploadByIdRequestAction

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.upload.move_upload_by_id(
    id=1,
    folder_id=1,
    action=MoveUploadByIdRequestAction.COPY,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `int` — Folder Id, where upload should be copied to
    
</dd>
</dl>

<dl>
<dd>

**action:** `MoveUploadByIdRequestAction` — Action to be performed
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while accessing the package
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">delete_upload_by_id</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a single upload by id
</dd>
</dl>
</dd>
</dl>

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

client.upload.delete_upload_by_id(
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

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while accessing the package
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">update_upload_by_id</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an upload information
</dd>
</dl>
</dd>
</dl>

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

client.upload.update_upload_by_id(
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

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[UpdateUploadByIdRequestStatus]` — New status of the upload
    
</dd>
</dl>

<dl>
<dd>

**assignee:** `typing.Optional[int]` — New assignee for the project
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while accessing the package
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_uploads</a>(...) -> typing.List[Upload]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The uploads endpoint returns all uploads
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_uploads()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `typing.Optional[int]` — Folder ID to limit the uploads to
    
</dd>
</dl>

<dl>
<dd>

**recursive:** `typing.Optional[bool]` — Load uploads from child folders as well
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter pattern for name and description
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[GetUploadsRequestStatus]` — Status of uploads
    
</dd>
</dl>

<dl>
<dd>

**assignee:** `typing.Optional[str]` — User name to which uploads are assigned to or -me- or -unassigned-
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[str]` — Uploads since given date in YYYY-MM-DD format
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while accessing the package
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number to fetch
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits of responses per request
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">create_upload</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint to create a new upload in FOSSology
</dd>
</dl>
</dd>
</dl>

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

client.upload.create_upload(
    folder_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `int` — Folder Id, where upload should be created
    
</dd>
</dl>

<dl>
<dd>

**public:** `typing.Literal` — The access level to the upload
    
</dd>
</dl>

<dl>
<dd>

**upload_type:** `typing.Literal` — Type of upload done. Choose `file` if uploading a file.
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while accessing the package
    
</dd>
</dl>

<dl>
<dd>

**upload_description:** `typing.Optional[str]` — Visible description of the file
    
</dd>
</dl>

<dl>
<dd>

**apply_global:** `typing.Optional[bool]` — Apply global decisions for current upload
    
</dd>
</dl>

<dl>
<dd>

**ignore_scm:** `typing.Optional[bool]` — Ignore SCM files (Git, SVN, TFS) and files with particular Mimetype
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[CreateUploadRequestLocation]` 
    
</dd>
</dl>

<dl>
<dd>

**scan_options:** `typing.Optional[ScanOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**main_license:** `typing.Optional[str]` — Main license shortname for the upload.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_upload_file_by_id</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a file by upload id
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_upload_file_by_id(
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

**id:** `int` — Download file using Upload ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_summary_by_upload_id</a>(...) -> UploadSummary</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns summary for single upload
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_summary_by_upload_id(
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

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[int]` — Id of the agent
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while accessing the package
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_item_info</a>(...) -> Fileinfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns info for single file
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_item_info(
    id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree Id of the file
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_licenses_by_upload_id</a>(...) -> UploadLicenses</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of licenses found by requested agent
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.upload import GetLicensesByUploadIdRequestAgentItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.upload.get_licenses_by_upload_id(
    id=1,
    agent=[
        GetLicensesByUploadIdRequestAgentItem.NOMOS
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

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**agent:** `typing.Optional[typing.Union[GetLicensesByUploadIdRequestAgentItem, typing.Sequence[GetLicensesByUploadIdRequestAgentItem]]]` — Name of the agent
    
</dd>
</dl>

<dl>
<dd>

**containers:** `typing.Optional[bool]` — Show directories and containers
    
</dd>
</dl>

<dl>
<dd>

**license:** `typing.Optional[bool]` — Show license in response
    
</dd>
</dl>

<dl>
<dd>

**copyright:** `typing.Optional[bool]` — Show copyrights in response
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number (starts from 1)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits of responses per request
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while accessing the package
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_copyrights_by_upload_id</a>(...) -> UploadCopyrights</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of copyrights found on the requested upload.
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_copyrights_by_upload_id(
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

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">set_upload_permissions</a>(...) -> typing.List[Info]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set permissions for a upload in a folder for different groups
</dd>
</dl>
</dd>
</dl>

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

client.upload.set_upload_permissions(
    id=1,
    all_uploads_permission=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Enter any upload id
    
</dd>
</dl>

<dl>
<dd>

**all_uploads_permission:** `bool` — Apply same permissions to all uploads in this folder
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[int]` — Enter a folder id
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `typing.Optional[int]` — Enter the id of the group you want to add or edit permission for this upload
    
</dd>
</dl>

<dl>
<dd>

**new_permission:** `typing.Optional[SetUploadPermissionsRequestNewPermission]` — Select the permission for selected group
    
</dd>
</dl>

<dl>
<dd>

**public_permission:** `typing.Optional[SetUploadPermissionsRequestPublicPermission]` — Select the public permission for this upload
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_groups_with_permissions</a>(...) -> UploadPermGroups</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of all the groups with their respective permissions for a upload
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_groups_with_permissions(
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

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_highlight_entries</a>(...) -> typing.List[HighlightInfo]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get highlight entries of the content for the given upload and item id.
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_highlight_entries(
    id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Id of the item
    
</dd>
</dl>

<dl>
<dd>

**clearing_id:** `typing.Optional[int]` — Id of the clearing event
    
</dd>
</dl>

<dl>
<dd>

**license_id:** `typing.Optional[int]` — Id of the license
    
</dd>
</dl>

<dl>
<dd>

**highlight_id:** `typing.Optional[int]` — Id of the highlight
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[int]` — Id of the agent
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">view_the_content_of_the_file</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the contents of a specific file
</dd>
</dl>
</dd>
</dl>

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

client.upload.view_the_content_of_the_file(
    id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Id of the item
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">set_clearing_decision</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the clearing decision for a particular upload tree item.
</dd>
</dl>
</dd>
</dl>

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

client.upload.set_clearing_decision(
    id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Id of the itemId
    
</dd>
</dl>

<dl>
<dd>

**decision_type:** `typing.Optional[int]` 

Type of decision.
0: WIP
3: To be discussed
4: Irrelevant
5: Identified
6: Do not use
7: Non functional
    
</dd>
</dl>

<dl>
<dd>

**global_decision:** `typing.Optional[bool]` 

Is the decision global?
If true, the decision is applied to all occurrence of the file on the server!
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">schedule_bulk_scan</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schedule the bulk scan for the item
</dd>
</dl>
</dd>
</dl>

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

client.upload.schedule_bulk_scan(
    id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Id of the itemId
    
</dd>
</dl>

<dl>
<dd>

**bulk_actions:** `typing.Optional[typing.List[ScheduleBulkScanBulkActionsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**ref_text:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**bulk_scope:** `typing.Optional[ScheduleBulkScanBulkScope]` 
    
</dd>
</dl>

<dl>
<dd>

**force_decision:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**ignore_irre:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**delimiters:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**scan_only_findings:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_bulk_history</a>(...) -> typing.List[GetBulkHistory]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the bulk history for a specific upload item
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_bulk_history(
    id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Id of the itemId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_license_decisions</a>(...) -> typing.List[LicenseDecision]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the license decisions list for the given upload and item id
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_license_decisions(
    id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Id of the itemId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">add_edit_delete_license_decision</a>(...) -> AddEditDeleteLicenseDecisionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add, update or delete a license decision for a particular upload tree item.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AddEditDeleteLicenseDecision
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.upload.add_edit_delete_license_decision(
    id=1,
    item_id=1,
    request=[
        AddEditDeleteLicenseDecision()
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

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Id of the itemId
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[AddEditDeleteLicenseDecision]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_main_licenses</a>(...) -> typing.List[License]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get main licenses assigned on a particular upload
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_main_licenses(
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

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">set_main_license</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the main license for a particular upload.
</dd>
</dl>
</dd>
</dl>

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

client.upload.set_main_license(
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

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**short_name:** `typing.Optional[str]` — short name of the license
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">delete_main_license</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a main license from an upload.
</dd>
</dl>
</dd>
</dl>

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

client.upload.delete_main_license(
    id=1,
    short_name="shortName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**short_name:** `str` — shortName of the main license to be deleted
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_previous_and_next_item</a>(...) -> GetPrevNextItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the index of the previous and the next time for an upload
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_previous_and_next_item(
    id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Id of the itemId
    
</dd>
</dl>

<dl>
<dd>

**selection:** `typing.Optional[GetPreviousAndNextItemRequestSelection]` — Return jobs for the given upload id only
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_clearing_history</a>(...) -> GetClearingHistory</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the clearing history for a specific upload item
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_clearing_history(
    id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Id of the itemId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_clearing_progress_info</a>(...) -> ClearingProgressInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the clearing progress information for an upload
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_clearing_progress_info(
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

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_licenses_histogram</a>(...) -> typing.List[LicenseHistogram]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the licenses histogram for a specific upload
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_licenses_histogram(
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

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[int]` — Id of the agent
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_agents_by_upload_id</a>(...) -> typing.List[AgentOfUpload]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of agents for a upload.
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_agents_by_upload_id(
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

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_all_edited_licenses</a>(...) -> typing.List[EditedLicense]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the edited licenses list for a specific upload
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_all_edited_licenses(
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

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_all_scanned_licenses</a>(...) -> typing.List[ScannedLicense]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the scanned licenses list for a specific upload
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_all_scanned_licenses(
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

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[int]` — Id of the agent
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_item_tree_view</a>(...) -> typing.List[TreeViewModel]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the tree view for the given upload and item id
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_item_tree_view(
    id=1,
    item_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Id of the itemId
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[int]` — Id of the agent
    
</dd>
</dl>

<dl>
<dd>

**tag_id:** `typing.Optional[int]` — Id of the tag
    
</dd>
</dl>

<dl>
<dd>

**scan_license_filter:** `typing.Optional[int]` — ShortName of the selected scan license filter
    
</dd>
</dl>

<dl>
<dd>

**edited_license_filter:** `typing.Optional[int]` — ShortName of the selected edited license filter
    
</dd>
</dl>

<dl>
<dd>

**flatten:** `typing.Optional[bool]` — Flatten the tree
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetItemTreeViewRequestSort]` — Sort the tree
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Filter the list according to the search string
    
</dd>
</dl>

<dl>
<dd>

**show_quick:** `typing.Optional[bool]` — Show all the items of the current container
    
</dd>
</dl>

<dl>
<dd>

**filter_open:** `typing.Optional[bool]` — openCBox Filter is checked
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number (starts from 1)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits of responses per request
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_top_item_id</a>(...) -> typing.List[Info]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the item id for the top level item in a given upload.
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_top_item_id(
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

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_licenses_reuse_summary</a>(...) -> GetReuseReportSummary</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the overall licenses reuse summary for an upload
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_licenses_reuse_summary(
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

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_revisions_for_agents</a>(...) -> typing.List[AgentsRevision]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of revisions for the successful agents for the upload
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_revisions_for_agents(
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

**id:** `int` — Id of the upload
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">run_one_shot_nomos</a>(...) -> OneShotInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run one-shot nomos analysis on the upload without storing the results.
</dd>
</dl>
</dd>
</dl>

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

client.upload.run_one_shot_nomos(
    file_input="example_fileInput",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_input:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">run_one_shot_monk</a>(...) -> OneShotInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run one-shot monk analysis on the upload without storing the results.
</dd>
</dl>
</dd>
</dl>

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

client.upload.run_one_shot_monk(
    file_input="example_fileInput",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_input:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">run_one_shot_ceu</a>(...) -> OneShotInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run one-shot Copyright/Email/URL analysis on the upload without storing the results.
</dd>
</dl>
</dd>
</dl>

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

client.upload.run_one_shot_ceu(
    file_input="example_fileInput",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_input:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_files</a>(...) -> typing.List[File]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of files by hashes
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Hash
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.upload.get_files(
    request=[
        Hash()
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

**request:** `typing.List[Hash]` 
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while downloading specific report
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">get_conf_info</a>(...) -> typing.List[ConfResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get conf information
</dd>
</dl>
</dd>
</dl>

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

client.upload.get_conf_info(
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

**id:** `int` — Upload Id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload.<a href="src/fern/upload/client.py">update_conf_data</a>(...) -> typing.List[Info]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the conf page data from the server
</dd>
</dl>
</dd>
</dl>

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

client.upload.update_conf_data(
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

**id:** `int` — Upload Id
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` — Key of the field to be updated
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` 

Value of the field to be updated. If value is a JSON, it should be
sent as an encoded string.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Search
<details><summary><code>client.search.<a href="src/fern/search/client.py">file</a>(...) -> typing.List[SearchResults]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search the FOSSology for a specific file
</dd>
</dl>
</dd>
</dl>

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

client.search.file()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search_type:** `typing.Literal` — Limit search to
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while performing search
    
</dd>
</dl>

<dl>
<dd>

**upload_id:** `typing.Optional[int]` — Id of the upload to search files into
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` — Filename to find, can contain % as wild-card
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` — Tag to find
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number (starts from 1)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits of responses per request
    
</dd>
</dl>

<dl>
<dd>

**filesizemin:** `typing.Optional[int]` — Min filesize in bytes
    
</dd>
</dl>

<dl>
<dd>

**filesizemax:** `typing.Optional[int]` — Max filesize in bytes
    
</dd>
</dl>

<dl>
<dd>

**license:** `typing.Optional[str]` — License search filter
    
</dd>
</dl>

<dl>
<dd>

**copyright:** `typing.Optional[str]` — Copyright search filter
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## User
<details><summary><code>client.user.<a href="src/fern/user/client.py">get_users</a>() -> typing.List[User]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the registered users
</dd>
</dl>
</dd>
</dl>

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

client.user.get_users()

```
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

<details><summary><code>client.user.<a href="src/fern/user/client.py">create_user</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new user
</dd>
</dl>
</dd>
</dl>

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

client.user.create_user(
    name="name",
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

**name:** `str` — Unique username
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**user_pass:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**default_visibility:** `typing.Optional[CreateUserRequestDefaultVisibility]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the user
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Email of the user, needs to be unique and is required
    
</dd>
</dl>

<dl>
<dd>

**access_level:** `typing.Optional[UserAccessLevel]` 
    
</dd>
</dl>

<dl>
<dd>

**root_folder_id:** `typing.Optional[float]` — root folder id of the user
    
</dd>
</dl>

<dl>
<dd>

**email_notification:** `typing.Optional[bool]` — enable email notification when upload scan completes
    
</dd>
</dl>

<dl>
<dd>

**default_group:** `typing.Optional[int]` — Default group id of the user
    
</dd>
</dl>

<dl>
<dd>

**agents:** `typing.Optional[Analysis]` 
    
</dd>
</dl>

<dl>
<dd>

**default_bucketpool:** `typing.Optional[int]` — Default bucket pool id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/fern/user/client.py">get_user_by_id</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one single user by id
</dd>
</dl>
</dd>
</dl>

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

client.user.get_user_by_id(
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

<details><summary><code>client.user.<a href="src/fern/user/client.py">modify_user_by_id</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edit user details by id
</dd>
</dl>
</dd>
</dl>

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

client.user.modify_user_by_id(
    id_path_param=1,
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

**id_path_param:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — ID of the user
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Unique username
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the user
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Email of the user, needs to be unique and is required
    
</dd>
</dl>

<dl>
<dd>

**access_level:** `typing.Optional[UserAccessLevel]` 
    
</dd>
</dl>

<dl>
<dd>

**root_folder_id:** `typing.Optional[float]` — root folder id of the user
    
</dd>
</dl>

<dl>
<dd>

**email_notification:** `typing.Optional[bool]` — enable email notification when upload scan completes
    
</dd>
</dl>

<dl>
<dd>

**default_group:** `typing.Optional[int]` — Default group id of the user
    
</dd>
</dl>

<dl>
<dd>

**agents:** `typing.Optional[Analysis]` 
    
</dd>
</dl>

<dl>
<dd>

**default_bucketpool:** `typing.Optional[int]` — Default bucket pool id
    
</dd>
</dl>

<dl>
<dd>

**user_pass:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**default_folder_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**default_visibility:** `typing.Optional[ModifyUserByIdRequestDefaultVisibility]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/fern/user/client.py">delete_user_by_id</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a single user by id
</dd>
</dl>
</dd>
</dl>

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

client.user.delete_user_by_id(
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

<details><summary><code>client.user.<a href="src/fern/user/client.py">get_self</a>() -> GetSelfResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the information about logged in user
</dd>
</dl>
</dd>
</dl>

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

client.user.get_self()

```
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

<details><summary><code>client.user.<a href="src/fern/user/client.py">create_rest_api_token</a>(...) -> CreateRestApiTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new REST API Token
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TokenRequestTokenScope
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user.create_rest_api_token(
    token_name="token_name",
    token_scope=TokenRequestTokenScope.READ,
    token_expire=datetime.date.fromisoformat("2023-01-15"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `TokenRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/fern/user/client.py">get_tokens_by_type</a>(...) -> GetTokensByTypeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all the REST API tokens (active | expired)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.user import GetTokensByTypeRequestType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user.get_tokens_by_type(
    type=GetTokensByTypeRequestType.ACTIVE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `GetTokensByTypeRequestType` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/fern/user/client.py">update_permission_by_group_id_and_user_id</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update User's permission in group.
</dd>
</dl>
</dd>
</dl>

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

client.user.update_permission_by_group_id_and_user_id(
    id=1,
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

**id:** `int` — Id of the group
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `int` — user id of the member
    
</dd>
</dl>

<dl>
<dd>

**perm:** `typing.Optional[int]` 

New user permission in the group.
0: User
1: Admin
2: Advisor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Copyrights
<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">get_file_copyrights</a>(...) -> typing.List[GetFileCopyrights]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of copyrights associated with the file
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.copyrights import GetFileCopyrightsRequestStatus

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.copyrights.get_file_copyrights(
    id=1,
    item_id=1,
    status=GetFileCopyrightsRequestStatus.ACTIVE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload Id
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)
    
</dd>
</dl>

<dl>
<dd>

**status:** `GetFileCopyrightsRequestStatus` — Status of the CX
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits of responses per request
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for responses
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">update_file_copyrights</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a copyright statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.update_file_copyrights(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request:** `SetCopyrightInfo` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">delete_file_copyrights</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a copyright statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.delete_file_copyrights(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">restore_file_copyrights</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restores a copyright statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.restore_file_copyrights(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">get_file_user_copyrights</a>(...) -> typing.List[GetFileCopyrights]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of user copyright findings associated with the file
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.copyrights import GetFileUserCopyrightsRequestStatus

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.copyrights.get_file_user_copyrights(
    id=1,
    item_id=1,
    status=GetFileUserCopyrightsRequestStatus.ACTIVE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload Id
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)
    
</dd>
</dl>

<dl>
<dd>

**status:** `GetFileUserCopyrightsRequestStatus` — Status of the CX
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits of responses per request
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for responses
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">update_file_user_copyright</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates user copyright statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.update_file_user_copyright(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request:** `SetCopyrightInfo` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">delete_file_user_copyright</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes user copyright statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.delete_file_user_copyright(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">restore_file_user_copyright</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restores user copyright statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.restore_file_user_copyright(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">get_file_scan_code_copyrights</a>(...) -> typing.List[GetFileCopyrights]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of scancode copyright findings associated with the file
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.copyrights import GetFileScanCodeCopyrightsRequestStatus

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.copyrights.get_file_scan_code_copyrights(
    id=1,
    item_id=1,
    status=GetFileScanCodeCopyrightsRequestStatus.ACTIVE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload Id
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)
    
</dd>
</dl>

<dl>
<dd>

**status:** `GetFileScanCodeCopyrightsRequestStatus` — Status of the CX
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits of responses per request
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for responses
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">update_file_scan_code_copyright</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates scancode copyright statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.update_file_scan_code_copyright(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request:** `SetCopyrightInfo` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">delete_file_scan_code_copyright</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes scancode copyright statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.delete_file_scan_code_copyright(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">restore_file_scan_code_copyright</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restores scancode copyright statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.restore_file_scan_code_copyright(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">get_file_emails</a>(...) -> typing.List[GetFileCopyrights]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of emails associated with the file
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.copyrights import GetFileEmailsRequestStatus

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.copyrights.get_file_emails(
    id=1,
    item_id=1,
    status=GetFileEmailsRequestStatus.ACTIVE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload Id
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)
    
</dd>
</dl>

<dl>
<dd>

**status:** `GetFileEmailsRequestStatus` — Status of the CX
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits of responses per request
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for responses
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">update_file_email</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an email statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.update_file_email(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request:** `SetCopyrightInfo` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">delete_file_emails</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an email statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.delete_file_emails(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">restore_file_email</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restores an email statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.restore_file_email(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">get_file_scan_code_email</a>(...) -> typing.List[GetFileCopyrights]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of scancode email findings associated with the file
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.copyrights import GetFileScanCodeEmailRequestStatus

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.copyrights.get_file_scan_code_email(
    id=1,
    item_id=1,
    status=GetFileScanCodeEmailRequestStatus.ACTIVE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload Id
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)
    
</dd>
</dl>

<dl>
<dd>

**status:** `GetFileScanCodeEmailRequestStatus` — Status of the CX
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits of responses per request
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for responses
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">update_file_scan_code_email</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates scancode email finding for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.update_file_scan_code_email(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request:** `SetCopyrightInfo` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">delete_file_scan_code_email</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes scancode email finding for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.delete_file_scan_code_email(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">restore_file_scan_code_email</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restores scancode email finding for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.restore_file_scan_code_email(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">get_file_urls</a>(...) -> typing.List[GetFileCopyrights]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of URLs associated with the file
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.copyrights import GetFileUrlsRequestStatus

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.copyrights.get_file_urls(
    id=1,
    item_id=1,
    status=GetFileUrlsRequestStatus.ACTIVE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload Id
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)
    
</dd>
</dl>

<dl>
<dd>

**status:** `GetFileUrlsRequestStatus` — Status of the CX
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits of responses per request
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for responses
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">update_file_url</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an URL statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.update_file_url(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request:** `SetCopyrightInfo` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">delete_file_url</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an URL statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.delete_file_url(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">restore_file_url</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restores an URL statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.restore_file_url(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">get_file_scan_code_url</a>(...) -> typing.List[GetFileCopyrights]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of scancode url findings associated with the file
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.copyrights import GetFileScanCodeUrlRequestStatus

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.copyrights.get_file_scan_code_url(
    id=1,
    item_id=1,
    status=GetFileScanCodeUrlRequestStatus.ACTIVE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload Id
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)
    
</dd>
</dl>

<dl>
<dd>

**status:** `GetFileScanCodeUrlRequestStatus` — Status of the CX
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits of responses per request
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for responses
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">update_file_scan_code_url</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates scancode url finding for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.update_file_scan_code_url(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request:** `SetCopyrightInfo` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">delete_file_scan_code_url</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes scancode url finding for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.delete_file_scan_code_url(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">restore_file_scan_code_url</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restores scancode url finding for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.restore_file_scan_code_url(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">get_file_authors</a>(...) -> typing.List[GetFileCopyrights]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of authors associated with the file
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.copyrights import GetFileAuthorsRequestStatus

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.copyrights.get_file_authors(
    id=1,
    item_id=1,
    status=GetFileAuthorsRequestStatus.ACTIVE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload Id
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)
    
</dd>
</dl>

<dl>
<dd>

**status:** `GetFileAuthorsRequestStatus` — Status of the CX
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits of responses per request
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for responses
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">update_file_author</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an author statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.update_file_author(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request:** `SetCopyrightInfo` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">delete_file_author</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an author statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.delete_file_author(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">restore_file_author</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restores an author statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.restore_file_author(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">get_file_scan_code_author</a>(...) -> typing.List[GetFileCopyrights]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of scancode author findings associated with the file
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.copyrights import GetFileScanCodeAuthorRequestStatus

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.copyrights.get_file_scan_code_author(
    id=1,
    item_id=1,
    status=GetFileScanCodeAuthorRequestStatus.ACTIVE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload Id
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)
    
</dd>
</dl>

<dl>
<dd>

**status:** `GetFileScanCodeAuthorRequestStatus` — Status of the CX
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits of responses per request
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for responses
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">update_file_scan_code_author</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates scancode author finding for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.update_file_scan_code_author(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request:** `SetCopyrightInfo` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">delete_file_scan_code_author</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes scancode author finding for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.delete_file_scan_code_author(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">restore_file_scan_code_author</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restores scancode author finding for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.restore_file_scan_code_author(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">get_file_eccs</a>(...) -> typing.List[GetFileCopyrights]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of ECCs associated with the file
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.copyrights import GetFileEccsRequestStatus

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.copyrights.get_file_eccs(
    id=1,
    item_id=1,
    status=GetFileEccsRequestStatus.ACTIVE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload Id
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)
    
</dd>
</dl>

<dl>
<dd>

**status:** `GetFileEccsRequestStatus` — Status of the CX
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits of responses per request
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for responses
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">update_file_ecc</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an ECC statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.update_file_ecc(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request:** `SetCopyrightInfo` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">delete_file_ecc</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an ECC statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.delete_file_ecc(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">restore_file_ecc</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restores an ECC statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.restore_file_ecc(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">get_file_keywords</a>(...) -> typing.List[GetFileCopyrights]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of keywords associated with the file
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.copyrights import GetFileKeywordsRequestStatus

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.copyrights.get_file_keywords(
    id=1,
    item_id=1,
    status=GetFileKeywordsRequestStatus.ACTIVE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload Id
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)
    
</dd>
</dl>

<dl>
<dd>

**status:** `GetFileKeywordsRequestStatus` — Status of the CX
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits of responses per request
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for responses
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">update_file_keyword</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a keyword statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.update_file_keyword(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request:** `SetCopyrightInfo` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">delete_file_keyword</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a keyword statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.delete_file_keyword(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">restore_file_keyword</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restores a keyword statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.restore_file_keyword(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">get_file_ipras</a>(...) -> typing.List[GetFileCopyrights]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of IPRAs associated with the file
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.copyrights import GetFileIprasRequestStatus

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.copyrights.get_file_ipras(
    id=1,
    item_id=1,
    status=GetFileIprasRequestStatus.ACTIVE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload Id
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)
    
</dd>
</dl>

<dl>
<dd>

**status:** `GetFileIprasRequestStatus` — Status of the CX
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits of responses per request
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for responses
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">update_file_ipra</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an IPRA statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.update_file_ipra(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request:** `SetCopyrightInfo` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">delete_file_ipra</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an IPRA statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.delete_file_ipra(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">restore_file_ipra</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restores an IPRA statement for a particular file
</dd>
</dl>
</dd>
</dl>

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

client.copyrights.restore_file_ipra(
    id=1,
    item_id=1,
    hash="hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload tree ID
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` — CX hash
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">get_total_file_copyrights</a>(...) -> typing.List[GetTotalFileCopyrightsResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the total number of copyrights associated with the file
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.copyrights import GetTotalFileCopyrightsRequestStatus

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.copyrights.get_total_file_copyrights(
    id=1,
    item_id=1,
    status=GetTotalFileCopyrightsRequestStatus.ACTIVE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload Id
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload Tree ID
    
</dd>
</dl>

<dl>
<dd>

**status:** `GetTotalFileCopyrightsRequestStatus` — status of the copyright
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copyrights.<a href="src/fern/copyrights/client.py">get_total_file_user_copyrights</a>(...) -> typing.List[GetTotalFileUserCopyrightsResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the total number of user copyright findings associated with the file
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.copyrights import GetTotalFileUserCopyrightsRequestStatus

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.copyrights.get_total_file_user_copyrights(
    id=1,
    item_id=1,
    status=GetTotalFileUserCopyrightsRequestStatus.ACTIVE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Upload Id
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `int` — Upload Tree ID
    
</dd>
</dl>

<dl>
<dd>

**status:** `GetTotalFileUserCopyrightsRequestStatus` — status of the copyright
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Job
<details><summary><code>client.job.<a href="src/fern/job/client.py">get_jobs</a>(...) -> typing.List[Job]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all jobs with their status created by the logged in user
</dd>
</dl>
</dd>
</dl>

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

client.job.get_jobs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sort:** `typing.Optional[GetJobsRequestSort]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[GetJobsRequestStatus]` — Returns only jobs with the selected status.
    
</dd>
</dl>

<dl>
<dd>

**upload:** `typing.Optional[int]` — Return jobs for the given upload id only
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while accessing jobs
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.job.<a href="src/fern/job/client.py">start_jobs</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schedule an Analysis of an existing upload
</dd>
</dl>
</dd>
</dl>

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

client.job.start_jobs(
    folder_id=1,
    upload_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**upload_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ScanOptions` 
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while accessing jobs
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.job.<a href="src/fern/job/client.py">get_all_jobs</a>(...) -> typing.List[Job]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all jobs with their status created by every user. This API returns a response only if the requesting user is an Admin.
</dd>
</dl>
</dd>
</dl>

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

client.job.get_all_jobs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**status:** `typing.Optional[GetAllJobsRequestStatus]` — Returns only jobs with the selected status.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetAllJobsRequestSort]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.job.<a href="src/fern/job/client.py">get_scheduler_options_by_operation</a>(...) -> GetSchedulerOption</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the scheduler options for a specific operation
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.job import GetSchedulerOptionsByOperationRequestOperationName

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.job.get_scheduler_options_by_operation(
    operation_name=GetSchedulerOptionsByOperationRequestOperationName.STATUS,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**operation_name:** `GetSchedulerOptionsByOperationRequestOperationName` — Name of the operation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.job.<a href="src/fern/job/client.py">handle_scheduler_run</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Run the scheduler with the selected options from a specific operation
</dd>
</dl>
</dd>
</dl>

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

client.job.handle_scheduler_run()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job:** `typing.Optional[str]` — Name of the selected job
    
</dd>
</dl>

<dl>
<dd>

**level:** `typing.Optional[str]` — Level of the selected verbose
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — Priority option selected
    
</dd>
</dl>

<dl>
<dd>

**operation:** `typing.Optional[HandleSchedulerRunRequestOperation]` — Operation to be run by the scheduler
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.job.<a href="src/fern/job/client.py">get_job_by_id</a>(...) -> Job</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns job with the status
</dd>
</dl>
</dd>
</dl>

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

client.job.get_job_by_id(
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

**id:** `int` — Id of the job
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.job.<a href="src/fern/job/client.py">get_jobs_history_per_upload</a>(...) -> typing.List[ShowJob]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the history of all the jobs queued based on an upload
</dd>
</dl>
</dd>
</dl>

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

client.job.get_jobs_history_per_upload(
    upload=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**upload:** `int` — Return jobs for the given upload id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.job.<a href="src/fern/job/client.py">get_job_statistics</a>() -> typing.List[GetJobStatistics]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the statistics of all the jobs for the Admin Dashboard
</dd>
</dl>
</dd>
</dl>

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

client.job.get_job_statistics()

```
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

<details><summary><code>client.job.<a href="src/fern/job/client.py">get_all_server_jobs</a>() -> AllServerJobs</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all jobs with the scheduler status for the Admin Dashboard. This API returns a response only if the requesting user is an Admin.
</dd>
</dl>
</dd>
</dl>

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

client.job.get_all_server_jobs()

```
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

<details><summary><code>client.job.<a href="src/fern/job/client.py">delete_job</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a job queue and all the other job queues depending on it
</dd>
</dl>
</dd>
</dl>

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

client.job.delete_job(
    id=1,
    queue=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Id of the Job
    
</dd>
</dl>

<dl>
<dd>

**queue:** `int` — Id of the job queue to be deleted
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.job.<a href="src/fern/job/client.py">get_reports_by_upload</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all reports available for a given upload
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.job import GetReportsByUploadRequestReportFormat

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.job.get_reports_by_upload(
    upload_id=1,
    report_format=GetReportsByUploadRequestReportFormat.DEP5,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**upload_id:** `int` — Id of the upload to generate the report for
    
</dd>
</dl>

<dl>
<dd>

**report_format:** `GetReportsByUploadRequestReportFormat` — Which report to be genereated
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while generating a report
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.job.<a href="src/fern/job/client.py">get_report_by_id</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a report by id
</dd>
</dl>
</dd>
</dl>

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

client.job.get_report_by_id(
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

**id:** `int` — Id the report to download
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while downloading specific report
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Folders
<details><summary><code>client.folders.<a href="src/fern/folders/client.py">get_folders</a>(...) -> typing.List[Folder]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all folders or from a specific group
</dd>
</dl>
</dd>
</dl>

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

client.folders.get_folders()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while accessing folders
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">get_folder_by_id</a>(...) -> Folder</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single folder by id
</dd>
</dl>
</dd>
</dl>

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

client.folders.get_folder_by_id(
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

**id:** `int` — ID of the folder
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while accessing the folder
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">unlink_content</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unlink a content from a folder
</dd>
</dl>
</dd>
</dl>

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

client.folders.unlink_content(
    content_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**content_id:** `int` — ID of the content
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">get_all_folder_contents</a>(...) -> typing.List[GetFolderContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all contents of a folder by id
</dd>
</dl>
</dd>
</dl>

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

client.folders.get_all_folder_contents(
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

**id:** `int` — ID of the folder
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">get_unlinkable_contents</a>(...) -> GetFolderContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get unlinkable contents of a folder by id. These contents are copied.
</dd>
</dl>
</dd>
</dl>

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

client.folders.get_unlinkable_contents(
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

**id:** `int` — ID of the folder
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organize
<details><summary><code>client.organize.<a href="src/fern/organize/client.py">create_folder</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new child folder with optional description
</dd>
</dl>
</dd>
</dl>

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

client.organize.create_folder(
    parent_folder=1,
    folder_name="folderName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**parent_folder:** `int` — Parent folder for the new folder
    
</dd>
</dl>

<dl>
<dd>

**folder_name:** `str` — Name of the new folder
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while accessing folders
    
</dd>
</dl>

<dl>
<dd>

**folder_description:** `typing.Optional[str]` — Description of the new folder
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organize.<a href="src/fern/organize/client.py">move_folder_by_id</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Copy or move a folder by id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.organize import MoveFolderByIdRequestAction

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organize.move_folder_by_id(
    id=1,
    parent=1,
    action=MoveFolderByIdRequestAction.COPY,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — ID of the folder
    
</dd>
</dl>

<dl>
<dd>

**parent:** `int` — New parent folder id
    
</dd>
</dl>

<dl>
<dd>

**action:** `MoveFolderByIdRequestAction` — Action to be performed
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while accessing the folder
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organize.<a href="src/fern/organize/client.py">delete_folder_by_id</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schedule a folder deletion
</dd>
</dl>
</dd>
</dl>

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

client.organize.delete_folder_by_id(
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

**id:** `int` — ID of the folder
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while accessing the folder
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organize.<a href="src/fern/organize/client.py">patch_folder_by_id</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change a folder's name and/or description
</dd>
</dl>
</dd>
</dl>

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

client.organize.patch_folder_by_id(
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

**id:** `int` — ID of the folder
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while accessing the folder
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — New name of the folder
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — New description of the folder
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organize.<a href="src/fern/organize/client.py">create_group</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new user group
</dd>
</dl>
</dd>
</dl>

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

client.organize.create_group(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of the new group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Groups
<details><summary><code>client.groups.<a href="src/fern/groups/client.py">get_groups</a>() -> typing.List[Group]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns accessible groups for a user, all groups for an admin
</dd>
</dl>
</dd>
</dl>

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

client.groups.get_groups()

```
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

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">delete_group_by_id</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a single group by id.
</dd>
</dl>
</dd>
</dl>

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

client.groups.delete_group_by_id(
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

**id:** `int` — Id of the group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">add_member</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

add a new user to group
</dd>
</dl>
</dd>
</dl>

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

client.groups.add_member(
    id=1,
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

**id:** `int` — Id of the group
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `int` — user id of the member
    
</dd>
</dl>

<dl>
<dd>

**perm:** `typing.Optional[int]` — Default permission of the new member.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">delete_group_member_by_group_id_and_user_id</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a single group member by groupId and userId
</dd>
</dl>
</dd>
</dl>

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

client.groups.delete_group_member_by_group_id_and_user_id(
    id=1,
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

**id:** `int` — Id of the group
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `int` — user id of the member
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">deletable_groups</a>() -> typing.List[Group]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return a list of the groups which it is possible to delete.
</dd>
</dl>
</dd>
</dl>

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

client.groups.deletable_groups()

```
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

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">get_group_users_with_roles</a>(...) -> typing.List[UserGroupMember]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns accessible objects of users with roles from the group
</dd>
</dl>
</dd>
</dl>

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

client.groups.get_group_users_with_roles(
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

**id:** `int` — ID of the group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Report
<details><summary><code>client.report.<a href="src/fern/report/client.py">upload_report</a>(...) -> Info</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import a report to an existing upload
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.report import UploadReportRequestReportFormat

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.report.upload_report(
    upload=1,
    report_format=UploadReportRequestReportFormat.DECISIONIMPORTER,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**upload:** `int` — Upload ID
    
</dd>
</dl>

<dl>
<dd>

**report_format:** `UploadReportRequestReportFormat` — Type of report being uploaded
    
</dd>
</dl>

<dl>
<dd>

**group_name:** `typing.Optional[str]` — The group name to chose while uploading report
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Overview
<details><summary><code>client.overview.<a href="src/fern/overview/client.py">get_database_contents</a>() -> typing.List[GetDatabaseContent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get database contents for the dashboard display.
</dd>
</dl>
</dd>
</dl>

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

client.overview.get_database_contents()

```
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

<details><summary><code>client.overview.<a href="src/fern/overview/client.py">get_php_info</a>() -> GetPhpInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get PHP info
</dd>
</dl>
</dd>
</dl>

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

client.overview.get_php_info()

```
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

<details><summary><code>client.overview.<a href="src/fern/overview/client.py">get_disk_usage</a>() -> typing.List[DiskUsage]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get disk usage
</dd>
</dl>
</dd>
</dl>

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

client.overview.get_disk_usage()

```
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

<details><summary><code>client.overview.<a href="src/fern/overview/client.py">get_database_metrics</a>() -> typing.List[GetDatabaseMetric]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get database metrics for the dashboard display.
</dd>
</dl>
</dd>
</dl>

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

client.overview.get_database_metrics()

```
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

<details><summary><code>client.overview.<a href="src/fern/overview/client.py">get_active_queries</a>() -> typing.List[GetActiveQuery]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of active queries from the database.
</dd>
</dl>
</dd>
</dl>

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

client.overview.get_active_queries()

```
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

