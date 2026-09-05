# Reference
## page-metadata
<details><summary><code>client.page_metadata.<a href="src/fern/page_metadata/client.py">list_page_metadata</a>(...) -> PageMetadataListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List entries of the Jentic instance's `page-metadata` collection. This is the collection-type list endpoint (`GET /{pluralApiId}`) with `pluralApiId = page-metadatas`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.page_metadata.list_page_metadata()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sort the response. Single field `sort=field:asc`, or multiple via `sort[0]=field:asc&sort[1]=other:desc`. Direction is `:asc` (default) or `:desc`.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select only specific fields to return, e.g. `fields[0]=title&fields[1]=description`. Does not apply to relational/media/component/dynamic-zone fields.
    
</dd>
</dl>

<dl>
<dd>

**populate:** `typing.Optional[ListPageMetadataRequestPopulate]` — Populate relations, media, components, and dynamic zones (excluded by default). `populate=*` for all one level deep, or bracket syntax for specific/nested relations.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListPageMetadataRequestStatus]` — Select the Draft & Publish status on reads.
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — Select a locale (i18n plugin).
    
</dd>
</dl>

<dl>
<dd>

**publication_filter:** `typing.Optional[str]` — Select documents by how their draft and published versions relate.
    
</dd>
</dl>

<dl>
<dd>

**pagination_page:** `typing.Optional[int]` — Page-based pagination: page number. Cannot be combined with start/limit.
    
</dd>
</dl>

<dl>
<dd>

**pagination_page_size:** `typing.Optional[int]` — Page-based pagination: entries per page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_start:** `typing.Optional[int]` — Offset-based pagination: index of the first entry. Cannot be combined with page/pageSize.
    
</dd>
</dl>

<dl>
<dd>

**pagination_limit:** `typing.Optional[int]` — Offset-based pagination: number of entries to return. Maximum is configurable per instance.
    
</dd>
</dl>

<dl>
<dd>

**pagination_with_count:** `typing.Optional[bool]` — Include the total count / page count in the pagination metadata.
    
</dd>
</dl>

<dl>
<dd>

**filters_page_path_eq:** `typing.Optional[str]` — Filter by exact page path.
    
</dd>
</dl>

<dl>
<dd>

**filters_robots_index_eq:** `typing.Optional[bool]` — Filter by robotsIndex flag.
    
</dd>
</dl>

<dl>
<dd>

**filters_robots_follow_eq:** `typing.Optional[bool]` — Filter by robotsFollow flag.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.page_metadata.<a href="src/fern/page_metadata/client.py">create_page_metadata</a>(...) -> PageMetadataSingleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a `page-metadata` entry (`POST /{pluralApiId}`). Note: over REST the created entry is published even when `status=draft` is supplied; verify `publishedAt` on the response.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PageMetadataAttributes
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.page_metadata.create_page_metadata(
    data=PageMetadataAttributes(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PageMetadataWriteRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.page_metadata.<a href="src/fern/page_metadata/client.py">get_page_metadata</a>(...) -> PageMetadataSingleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a single `page-metadata` entry by documentId (`GET /{pluralApiId}/{documentId}`).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.page_metadata.get_page_metadata(
    document_id="documentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_id:** `str` — Strapi 5 document identifier (string), stable across locales and draft/published versions.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select only specific fields to return, e.g. `fields[0]=title&fields[1]=description`. Does not apply to relational/media/component/dynamic-zone fields.
    
</dd>
</dl>

<dl>
<dd>

**populate:** `typing.Optional[GetPageMetadataRequestPopulate]` — Populate relations, media, components, and dynamic zones (excluded by default). `populate=*` for all one level deep, or bracket syntax for specific/nested relations.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[GetPageMetadataRequestStatus]` — Select the Draft & Publish status on reads.
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — Select a locale (i18n plugin).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.page_metadata.<a href="src/fern/page_metadata/client.py">update_page_metadata</a>(...) -> PageMetadataSingleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update a `page-metadata` entry by documentId (`PUT /{pluralApiId}/{documentId}`). Used to flip `robotsIndex` / `robotsFollow`. Note: updating over REST publishes the entry; there is no REST route to unpublish. Verify `publishedAt` on the response.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PageMetadataAttributes
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.page_metadata.update_page_metadata(
    document_id="documentId",
    data=PageMetadataAttributes(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_id:** `str` — Strapi 5 document identifier (string), stable across locales and draft/published versions.
    
</dd>
</dl>

<dl>
<dd>

**request:** `PageMetadataWriteRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.page_metadata.<a href="src/fern/page_metadata/client.py">delete_page_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a `page-metadata` entry by documentId (`DELETE /{pluralApiId}/{documentId}`).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.page_metadata.delete_page_metadata(
    document_id="documentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_id:** `str` — Strapi 5 document identifier (string), stable across locales and draft/published versions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## collection-type
<details><summary><code>client.collection_type.<a href="src/fern/collection_type/client.py">list_entries</a>(...) -> EntryListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

For a collection type (`apiId` = plural API ID, e.g. `articles`, `page-metadatas`) this lists entries with filtering, sorting, field selection, population, pagination, and status. For a single type (`apiId` = singular API ID, e.g. `homepage`) this returns the one global entry; the list query parameters do not apply. Collection and single types share this path position, so they are described by one templated path.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.collection_type.list_entries(
    api_id="apiId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_id:** `str` — The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sort the response. Single field `sort=field:asc`, or multiple via `sort[0]=field:asc&sort[1]=other:desc`. Direction is `:asc` (default) or `:desc`.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select only specific fields to return, e.g. `fields[0]=title&fields[1]=description`. Does not apply to relational/media/component/dynamic-zone fields.
    
</dd>
</dl>

<dl>
<dd>

**populate:** `typing.Optional[ListEntriesRequestPopulate]` — Populate relations, media, components, and dynamic zones (excluded by default). `populate=*` for all one level deep, or bracket syntax for specific/nested relations.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListEntriesRequestStatus]` — Select the Draft & Publish status on reads.
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — Select a locale (i18n plugin).
    
</dd>
</dl>

<dl>
<dd>

**publication_filter:** `typing.Optional[str]` — Select documents by how their draft and published versions relate.
    
</dd>
</dl>

<dl>
<dd>

**pagination_page:** `typing.Optional[int]` — Page-based pagination: page number. Cannot be combined with start/limit.
    
</dd>
</dl>

<dl>
<dd>

**pagination_page_size:** `typing.Optional[int]` — Page-based pagination: entries per page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_start:** `typing.Optional[int]` — Offset-based pagination: index of the first entry. Cannot be combined with page/pageSize.
    
</dd>
</dl>

<dl>
<dd>

**pagination_limit:** `typing.Optional[int]` — Offset-based pagination: number of entries to return. Maximum is configurable per instance.
    
</dd>
</dl>

<dl>
<dd>

**pagination_with_count:** `typing.Optional[bool]` — Include the total count / page count in the pagination metadata.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Dict[str, typing.Any]]` — Filter the response. Use bracket syntax `filters[field][$operator]=value`. Operators: $eq, $eqi, $ne, $nei, $lt, $lte, $gt, $gte, $in, $notIn, $contains, $notContains, $containsi, $notContainsi, $startsWith, $startsWithi, $endsWith, $endsWithi, $null, $notNull, $between, $or, $and, $not.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collection_type.<a href="src/fern/collection_type/client.py">create_entry</a>(...) -> EntrySingleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an entry of a collection type. The request body wraps attributes under a `data` key. Not applicable to single types (use PUT). Note: over REST the entry is auto-published even with `status=draft`; verify `publishedAt` on the response.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.collection_type.create_entry(
    api_id="apiId",
    data={
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

**api_id:** `str` — The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntryWriteRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collection_type.<a href="src/fern/collection_type/client.py">get_entry</a>(...) -> EntrySingleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a single collection-type entry by its `documentId`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.collection_type.get_entry(
    api_id="apiId",
    document_id="documentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_id:** `str` — The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` — Strapi 5 document identifier (string), stable across locales and draft/published versions.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Select only specific fields to return, e.g. `fields[0]=title&fields[1]=description`. Does not apply to relational/media/component/dynamic-zone fields.
    
</dd>
</dl>

<dl>
<dd>

**populate:** `typing.Optional[GetEntryRequestPopulate]` — Populate relations, media, components, and dynamic zones (excluded by default). `populate=*` for all one level deep, or bracket syntax for specific/nested relations.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[GetEntryRequestStatus]` — Select the Draft & Publish status on reads.
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — Select a locale (i18n plugin).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collection_type.<a href="src/fern/collection_type/client.py">update_entry</a>(...) -> EntrySingleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update a collection-type entry by `documentId`. Note: updating over REST publishes the entry; there is no REST route to unpublish.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.collection_type.update_entry(
    api_id="apiId",
    document_id="documentId",
    data={
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

**api_id:** `str` — The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` — Strapi 5 document identifier (string), stable across locales and draft/published versions.
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntryWriteRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collection_type.<a href="src/fern/collection_type/client.py">delete_entry</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a collection-type entry by `documentId`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.collection_type.delete_entry(
    api_id="apiId",
    document_id="documentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_id:** `str` — The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` — Strapi 5 document identifier (string), stable across locales and draft/published versions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## single-type
<details><summary><code>client.single_type.<a href="src/fern/single_type/client.py">update_single_type</a>(...) -> EntrySingleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

For a single type (`apiId` = singular API ID), update the one global entry, creating it if absent. Collection-type entries are updated at `/{apiId}/{documentId}` instead. Note: updating over REST publishes the entry; there is no REST route to unpublish.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.single_type.update_single_type(
    api_id="apiId",
    data={
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

**api_id:** `str` — The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntryWriteRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.single_type.<a href="src/fern/single_type/client.py">delete_single_type</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

For a single type (`apiId` = singular API ID), delete the one global entry. Collection-type entries are deleted at `/{apiId}/{documentId}` instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.single_type.delete_single_type(
    api_id="apiId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_id:** `str` — The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

