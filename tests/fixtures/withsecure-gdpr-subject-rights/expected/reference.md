# Reference
## Flags
<details><summary><code>client.flags.<a href="src/fern/flags/client.py">get_personal_data_contexts</a>(...) -> ContextsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The API exposes actions against contexts (logical groups) of personal data in the given system. The grouping should be based on usage, e.g., personal data used for marketing, personal data collected for usage analysis, or personal data processed for technical realisation of the service. The same personal data type (e.g., an email address) may be in several contexts; this does not imply it would be actually duplicated in the system, but it could be used in different contexts. Typically, a single context should not contain data that is processed under different basis of processing.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.flags.get_personal_data_contexts(
    accept_language="fi_FI",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**accept_language:** `typing.Optional[str]` — A list of accepted languages.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Export
<details><summary><code>client.export.<a href="src/fern/export/client.py">export_personal_data</a>(...) -> ExportRequestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an export request to export all personal data stored within a particular personal data context. This will only schedule an export. The status and result must be polled for separately.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.export.export_personal_data(
    context_uuid="1234",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**context_uuid:** `ContextUuid` — The personal data context (data category) to export.
    
</dd>
</dl>

<dl>
<dd>

**authenticated_identifiers:** `typing.Optional[SuppliedAuth]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.export.<a href="src/fern/export/client.py">query_the_status_of_an_export_request</a>(...) -> ExportReadyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query the status of an export request. The status should be polled for until completed. The location of the exported content is communicated once the export request is completed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.export.query_the_status_of_an_export_request(
    accept_language="fi_FI",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ExportRequestResponse` 
    
</dd>
</dl>

<dl>
<dd>

**accept_language:** `typing.Optional[str]` — A list of accepted languages.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Deletion
<details><summary><code>client.deletion.<a href="src/fern/deletion/client.py">delete_personal_data</a>(...) -> DeletionRequestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a deletion request to delete all personal data stored within a particular personal data context. This will only schedule a deletion. The status and result must be polled for separately.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.deletion.delete_personal_data(
    context_uuid="1234",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**context_uuid:** `ContextUuid` — The personal data context (data category) to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_grounds:** `typing.Optional[DeletionRequestGrounds]` 
    
</dd>
</dl>

<dl>
<dd>

**authenticated_identifiers:** `typing.Optional[SuppliedAuth]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deletion.<a href="src/fern/deletion/client.py">query_the_status_of_a_deletion_request</a>(...) -> DeletionReadyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query the status of a deletion request. The status should be polled for until completed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.deletion.query_the_status_of_a_deletion_request(
    accept_language="fi_FI",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `DeletionRequestResponse` 
    
</dd>
</dl>

<dl>
<dd>

**accept_language:** `typing.Optional[str]` — A list of accepted languages
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

