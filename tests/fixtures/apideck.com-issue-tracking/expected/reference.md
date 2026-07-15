# Reference
## Collections
<details><summary><code>client.collections.<a href="src/fern/collections/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Collections
</dd>
</dl>
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.collections.all_(
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

**sort:** `typing.Optional[CollectionsSort]` — Apply sorting
    
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

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Collection
</dd>
</dl>
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.collections.one(
    collection_id="apideck-io",
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

**collection_id:** `str` — The collection ID
    
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

## Tags
<details><summary><code>client.tags.<a href="src/fern/tags/client.py">collection_tags_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Tags
</dd>
</dl>
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.tags.collection_tags_all(
    collection_id="apideck-io",
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

**collection_id:** `str` — The collection ID
    
</dd>
</dl>

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

## Tickets
<details><summary><code>client.tickets.<a href="src/fern/tickets/client.py">collection_tickets_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Tickets
</dd>
</dl>
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.tickets.collection_tickets_all(
    collection_id="apideck-io",
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

**collection_id:** `str` — The collection ID
    
</dd>
</dl>

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

**sort:** `typing.Optional[TicketsSort]` — Apply sorting
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[IssuesFilter]` — Apply filters
    
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

<details><summary><code>client.tickets.<a href="src/fern/tickets/client.py">collection_tickets_add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Ticket
</dd>
</dl>
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.tickets.collection_tickets_add(
    collection_id_="apideck-io",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id_:** `str` — The collection ID
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**assignees:** `typing.Optional[typing.Sequence[Assignee]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[str]` — The ticket's collection ID
    
</dd>
</dl>

<dl>
<dd>

**completed_at:** `typing.Optional[dt.datetime]` — When the ticket was completed
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The ticket's description. HTML version of description is mapped if supported by the third-party platform
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[dt.datetime]` — Due date of the ticket
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` — The ticket's parent ID
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[TicketPriority]` — Priority of the ticket
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The current status of the ticket. Possible values include: open, in_progress, closed, or - in cases where there is no clear mapping - the original value passed through.
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[str]` — Subject of the ticket
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[CollectionTag]]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — The ticket's type
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tickets.<a href="src/fern/tickets/client.py">collection_tickets_one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Ticket
</dd>
</dl>
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.tickets.collection_tickets_one(
    collection_id="apideck-io",
    ticket_id="ticket_id",
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

**collection_id:** `str` — The collection ID
    
</dd>
</dl>

<dl>
<dd>

**ticket_id:** `str` — ID of the ticket you are acting upon.
    
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

<details><summary><code>client.tickets.<a href="src/fern/tickets/client.py">collection_tickets_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Ticket
</dd>
</dl>
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.tickets.collection_tickets_delete(
    collection_id="apideck-io",
    ticket_id="ticket_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — The collection ID
    
</dd>
</dl>

<dl>
<dd>

**ticket_id:** `str` — ID of the ticket you are acting upon.
    
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

<details><summary><code>client.tickets.<a href="src/fern/tickets/client.py">collection_tickets_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Ticket
</dd>
</dl>
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.tickets.collection_tickets_update(
    collection_id_="apideck-io",
    ticket_id="ticket_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id_:** `str` — The collection ID
    
</dd>
</dl>

<dl>
<dd>

**ticket_id:** `str` — ID of the ticket you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**assignees:** `typing.Optional[typing.Sequence[Assignee]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[str]` — The ticket's collection ID
    
</dd>
</dl>

<dl>
<dd>

**completed_at:** `typing.Optional[dt.datetime]` — When the ticket was completed
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The ticket's description. HTML version of description is mapped if supported by the third-party platform
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[dt.datetime]` — Due date of the ticket
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` — The ticket's parent ID
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[TicketPriority]` — Priority of the ticket
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The current status of the ticket. Possible values include: open, in_progress, closed, or - in cases where there is no clear mapping - the original value passed through.
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[str]` — Subject of the ticket
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[CollectionTag]]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — The ticket's type
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Comments
<details><summary><code>client.comments.<a href="src/fern/comments/client.py">collection_ticket_comments_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Comments
</dd>
</dl>
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.comments.collection_ticket_comments_all(
    collection_id="apideck-io",
    ticket_id="ticket_id",
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

**collection_id:** `str` — The collection ID
    
</dd>
</dl>

<dl>
<dd>

**ticket_id:** `str` — ID of the ticket you are acting upon.
    
</dd>
</dl>

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

**sort:** `typing.Optional[CommentsSort]` — Apply sorting
    
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

<details><summary><code>client.comments.<a href="src/fern/comments/client.py">collection_ticket_comments_add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Comment
</dd>
</dl>
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.comments.collection_ticket_comments_add(
    collection_id="apideck-io",
    ticket_id="ticket_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — The collection ID
    
</dd>
</dl>

<dl>
<dd>

**ticket_id:** `str` — ID of the ticket you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[str]` — Body of the comment
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.comments.<a href="src/fern/comments/client.py">collection_ticket_comments_one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Comment
</dd>
</dl>
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.comments.collection_ticket_comments_one(
    collection_id="apideck-io",
    ticket_id="ticket_id",
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

**collection_id:** `str` — The collection ID
    
</dd>
</dl>

<dl>
<dd>

**ticket_id:** `str` — ID of the ticket you are acting upon.
    
</dd>
</dl>

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

<details><summary><code>client.comments.<a href="src/fern/comments/client.py">collection_ticket_comments_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Comment
</dd>
</dl>
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.comments.collection_ticket_comments_delete(
    collection_id="apideck-io",
    ticket_id="ticket_id",
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

**collection_id:** `str` — The collection ID
    
</dd>
</dl>

<dl>
<dd>

**ticket_id:** `str` — ID of the ticket you are acting upon.
    
</dd>
</dl>

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

<details><summary><code>client.comments.<a href="src/fern/comments/client.py">collection_ticket_comments_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Comment
</dd>
</dl>
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.comments.collection_ticket_comments_update(
    collection_id="apideck-io",
    ticket_id="ticket_id",
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

**collection_id:** `str` — The collection ID
    
</dd>
</dl>

<dl>
<dd>

**ticket_id:** `str` — ID of the ticket you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**id_:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[str]` — Body of the comment
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.users.<a href="src/fern/users/client.py">collection_users_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Users
</dd>
</dl>
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.users.collection_users_all(
    collection_id="apideck-io",
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

**collection_id:** `str` — The collection ID
    
</dd>
</dl>

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

<details><summary><code>client.users.<a href="src/fern/users/client.py">collection_users_one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get user
</dd>
</dl>
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.users.collection_users_one(
    collection_id="apideck-io",
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

**collection_id:** `str` — The collection ID
    
</dd>
</dl>

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

