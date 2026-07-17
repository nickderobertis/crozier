# Reference
## Drive Groups
<details><summary><code>client.drive_groups.<a href="src/fern/drive_groups/client.py">all</a>(...) -> GetDriveGroupsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List DriveGroups
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.drive_groups.all_(
    fields="id,updated_at",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[DriveGroupsFilter]` — Apply filters
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drive_groups.<a href="src/fern/drive_groups/client.py">add</a>(...) -> CreateDriveGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create DriveGroup
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.drive_groups.add(
    name="accounting",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `DriveGroup` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drive_groups.<a href="src/fern/drive_groups/client.py">one</a>(...) -> GetDriveGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get DriveGroup
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.drive_groups.one(
    id="id",
    fields="id,updated_at",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drive_groups.<a href="src/fern/drive_groups/client.py">delete</a>(...) -> DeleteDriveGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete DriveGroup
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.drive_groups.delete(
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drive_groups.<a href="src/fern/drive_groups/client.py">update</a>(...) -> UpdateDriveGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update DriveGroup
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.drive_groups.update(
    id_="id",
    name="accounting",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**request:** `DriveGroup` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Drives
<details><summary><code>client.drives.<a href="src/fern/drives/client.py">all</a>(...) -> GetDrivesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Drives
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.drives.all_(
    fields="id,updated_at",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[DrivesFilter]` — Apply filters
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drives.<a href="src/fern/drives/client.py">add</a>(...) -> CreateDriveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Drive
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.drives.add(
    name="Project Resources",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Drive` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drives.<a href="src/fern/drives/client.py">one</a>(...) -> GetDriveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Drive
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.drives.one(
    id="id",
    fields="id,updated_at",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drives.<a href="src/fern/drives/client.py">delete</a>(...) -> DeleteDriveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Drive
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.drives.delete(
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drives.<a href="src/fern/drives/client.py">update</a>(...) -> UpdateDriveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Drive
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.drives.update(
    id_="id",
    name="Project Resources",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**request:** `Drive` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.files.<a href="src/fern/files/client.py">all</a>(...) -> GetFilesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Files
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.all_(
    fields="id,updated_at",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[FilesFilter]` — Apply filters
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[FilesSort]` — Apply sorting
    
</dd>
</dl>

<dl>
<dd>

**pass_through:** `typing.Optional[PassThroughQuery]` — Optional unmapped key/values that will be passed through to downstream as query parameters
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/fern/files/client.py">upload</a>(...) -> CreateFileResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload file (max 100MB). Please use the [Upload Sessions API](#operation/uploadSessionsStart) to upload bigger files. For more information on uploads, refer to the [file upload guide](/guides/file-upload).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.upload(
    apideck_metadata="x-apideck-metadata",
    request="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**apideck_metadata:** `str` — Metadata to attach to the file
    
</dd>
</dl>

<dl>
<dd>

**request:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/fern/files/client.py">search</a>(...) -> GetFilesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search Files
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.search(
    fields="id,updated_at",
    query="logo jpg",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — The query to search for. May match across multiple fields.
    
</dd>
</dl>

<dl>
<dd>

**pass_through:** `typing.Optional[PassThroughQuery]` — Optional unmapped key/values that will be passed through to downstream as query parameters
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
</dd>
</dl>

<dl>
<dd>

**drive_id:** `typing.Optional[str]` — ID of the drive to filter on
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/fern/files/client.py">one</a>(...) -> GetFileResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get File
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.one(
    id="id",
    fields="id,updated_at",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/fern/files/client.py">delete</a>(...) -> DeleteFileResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete File
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.delete(
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/fern/files/client.py">update</a>(...) -> UpdateFileResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rename or move File
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.update(
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the file.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the file.
    
</dd>
</dl>

<dl>
<dd>

**parent_folder_id:** `typing.Optional[ParentFolderId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/fern/files/client.py">download</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download File
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.files.download()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.folders.<a href="src/fern/folders/client.py">add</a>(...) -> CreateFolderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Folder
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.folders.add(
    fields="id,updated_at",
    name="Documents",
    parent_folder_id="1234",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the folder.
    
</dd>
</dl>

<dl>
<dd>

**parent_folder_id:** `ParentFolderId` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the folder.
    
</dd>
</dl>

<dl>
<dd>

**drive_id:** `typing.Optional[str]` — ID of the drive to create the folder in.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">one</a>(...) -> GetFolderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Folder
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.folders.one(
    id="id",
    fields="id,updated_at",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">delete</a>(...) -> DeleteFolderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Folder
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.folders.delete(
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">update</a>(...) -> UpdateFolderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rename or move Folder
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.folders.update(
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the folder.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the folder.
    
</dd>
</dl>

<dl>
<dd>

**parent_folder_id:** `typing.Optional[ParentFolderId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">copy</a>(...) -> UpdateFolderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Copy Folder
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.folders.copy(
    id="id",
    fields="id,updated_at",
    parent_folder_id="1234",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**parent_folder_id:** `ParentFolderId` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the folder.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Shared Links
<details><summary><code>client.shared_links.<a href="src/fern/shared_links/client.py">all</a>(...) -> GetSharedLinksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List SharedLinks
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shared_links.all_(
    fields="id,updated_at",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shared_links.<a href="src/fern/shared_links/client.py">add</a>(...) -> CreateSharedLinkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Shared Link
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shared_links.add(
    target_id="target_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `SharedLink` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shared_links.<a href="src/fern/shared_links/client.py">one</a>(...) -> GetSharedLinkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Shared Link
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shared_links.one(
    id="id",
    fields="id,updated_at",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shared_links.<a href="src/fern/shared_links/client.py">delete</a>(...) -> DeleteSharedLinkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Shared Link
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shared_links.delete(
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shared_links.<a href="src/fern/shared_links/client.py">update</a>(...) -> UpdateSharedLinkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Shared Link
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.shared_links.update(
    id="id",
    target_id="target_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**request:** `SharedLink` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Upload Sessions
<details><summary><code>client.upload_sessions.<a href="src/fern/upload_sessions/client.py">add</a>(...) -> CreateUploadSessionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start an Upload Session. Upload sessions are used to upload large files, use the [Upload File](#operation/filesUpload) endpoint to upload smaller files (up to 100MB). Note that the base URL is upload.apideck.com instead of unify.apideck.com. For more information on uploads, refer to the [file upload guide](/guides/file-upload).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.upload_sessions.add(
    name="Documents",
    parent_folder_id="1234",
    size=1810673,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the file.
    
</dd>
</dl>

<dl>
<dd>

**parent_folder_id:** `ParentFolderId` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `FileSize` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**drive_id:** `typing.Optional[str]` — ID of the drive to upload to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload_sessions.<a href="src/fern/upload_sessions/client.py">one</a>(...) -> GetUploadSessionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Upload Session. Use the `part_size` to split your file into parts. Upload the parts to the [Upload part of File](#operation/uploadSessionsUpload) endpoint. Note that the base URL is upload.apideck.com instead of unify.apideck.com. For more information on uploads, refer to the [file upload guide](/guides/file-upload).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.upload_sessions.one(
    id="id",
    fields="id,updated_at",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload_sessions.<a href="src/fern/upload_sessions/client.py">upload</a>(...) -> UpdateUploadSessionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload part of File to Upload Session (max 100MB). Get `part_size` from [Get Upload Session](#operation/uploadSessionsOne) first. Every File part (except the last one) uploaded to this endpoint should have Content-Length equal to `part_size`. Note that the base URL is upload.apideck.com instead of unify.apideck.com. For more information on uploads, refer to the [file upload guide](/guides/file-upload).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.upload_sessions.upload(
    id="id",
    part_number=0,
    digest="sha=fpRyg5eVQletdZqEKaFlqwBXJzM=",
    request="<binary string>",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**part_number:** `float` — Part number of the file part being uploaded.
    
</dd>
</dl>

<dl>
<dd>

**request:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**digest:** `typing.Optional[str]` — The RFC3230 message digest of the uploaded part. Only required for the Box connector. More information on the Box API docs [here](https://developer.box.com/reference/put-files-upload-sessions-id/#param-digest)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload_sessions.<a href="src/fern/upload_sessions/client.py">delete</a>(...) -> DeleteUploadSessionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Abort Upload Session. Note that the base URL is upload.apideck.com instead of unify.apideck.com. For more information on uploads, refer to the [file upload guide](/guides/file-upload).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.upload_sessions.delete(
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.upload_sessions.<a href="src/fern/upload_sessions/client.py">finish</a>(...) -> GetFileResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Finish Upload Session. Only call this endpoint after all File parts have been uploaded to [Upload part of File](#operation/uploadSessionsUpload). Note that the base URL is upload.apideck.com instead of unify.apideck.com. For more information on uploads, refer to the [file upload guide](/guides/file-upload).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.upload_sessions.finish(
    id="id",
    digest="sha=fpRyg5eVQletdZqEKaFlqwBXJzM=",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**digest:** `typing.Optional[str]` — The RFC3230 message digest of the uploaded part. Only required for the Box connector. More information on the Box API docs [here](https://developer.box.com/reference/put-files-upload-sessions-id/#param-digest)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

