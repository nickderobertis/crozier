# Reference
## alias
<details><summary><code>client.alias.<a href="src/fern/alias/client.py">username</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get basic details about a user, given their username
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.alias.username(
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

**username:** `str` — Username of the user who you are looking for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.alias.<a href="src/fern/alias/client.py">alias_val2</a>(...) -> Val</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a val
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.alias.alias_val2(
    username="username",
    val_name="val_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `str` — Username of the user whose val you are looking for
    
</dd>
</dl>

<dl>
<dd>

**val_name:** `str` — Name of the val you're looking for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## me
<details><summary><code>client.me.<a href="src/fern/me/client.py">get</a>() -> MeGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get profile information for the current user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.me.get()

```
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

<details><summary><code>client.me.<a href="src/fern/me/client.py">me_vals2</a>(...) -> MeVals2Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] List all of a user's vals for authenticated users
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.me.me_vals2(
    offset=1,
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**offset:** `int` — Number of items to skip in order to deliver paginated results
    
</dd>
</dl>

<dl>
<dd>

**limit:** `int` — Maximum items to return in each paginated response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## blobs
<details><summary><code>client.blobs.<a href="src/fern/blobs/client.py">v1blobs_list</a>(...) -> typing.List[V1BlobsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List blobs in your account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.blobs.v1blobs_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prefix:** `typing.Optional[str]` — If specified, only include blobs that start with this string
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.blobs.<a href="src/fern/blobs/client.py">v1blobs_get</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a blob’s contents.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.blobs.v1blobs_get(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — Key that uniquely identifies this blob
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.blobs.<a href="src/fern/blobs/client.py">v1blobs_store</a>(...) -> V1BlobsStoreResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Store data in blob storage
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.blobs.v1blobs_store(
    key="key",
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

**key:** `str` — Key that uniquely identifies this blob
    
</dd>
</dl>

<dl>
<dd>

**request:** `bytes` — Binary input data
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.blobs.<a href="src/fern/blobs/client.py">v1blobs_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a blob
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.blobs.v1blobs_delete(
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

**key:** `str` — Key that uniquely identifies this blob
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.blobs.<a href="src/fern/blobs/client.py">v2blobs_list</a>(...) -> typing.List[V2BlobsListResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List blobs in your account
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.blobs.v2blobs_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prefix:** `typing.Optional[str]` — If specified, only include blobs that start with this string
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.blobs.<a href="src/fern/blobs/client.py">v2blobs_get</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a blob’s contents.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.blobs.v2blobs_get(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — Key that uniquely identifies this blob
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.blobs.<a href="src/fern/blobs/client.py">v2blobs_store</a>(...) -> V2BlobsStoreResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Store data in blob storage
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.blobs.v2blobs_store(
    key="key",
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

**key:** `str` — Key that uniquely identifies this blob
    
</dd>
</dl>

<dl>
<dd>

**request:** `bytes` — Binary input data
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.blobs.<a href="src/fern/blobs/client.py">v2blobs_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a blob
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.blobs.v2blobs_delete(
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

**key:** `str` — Key that uniquely identifies this blob
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## users
<details><summary><code>client.users.<a href="src/fern/users/client.py">get</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get basic information about a user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.users.get(
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

**user_id:** `str` — User Id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## sqlite
<details><summary><code>client.sqlite.<a href="src/fern/sqlite/client.py">execute</a>(...) -> ResultSet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a single SQLite statement and return results
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.sqlite.execute(
    statement="SELECT 1;",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**statement:** `SqliteExecuteRequestStatement` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sqlite.<a href="src/fern/sqlite/client.py">batch</a>(...) -> typing.List[ResultSet]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a batch of SQLite statements and return results for all of them
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.sqlite import SqliteBatchRequestMode

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.sqlite.batch(
    statements=[
        "SELECT 1;"
    ],
    mode=SqliteBatchRequestMode.READ,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**statements:** `typing.List[SqliteBatchRequestStatementsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[SqliteBatchRequestMode]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## emails
<details><summary><code>client.emails.<a href="src/fern/emails/client.py">send</a>(...) -> EmailsSendResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send emails
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.emails.send(
    subject="An important message",
    text="Hello world",
    html="Hello <strong>world</strong>",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subject:** `typing.Optional[str]` — The subject line of the email
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[EmailsSendRequestFrom]` 
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[typing.Dict[str, str]]` — A set of headers to include the email that you send
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[EmailsSendRequestTo]` — A single email or list of emails for one of the address fields
    
</dd>
</dl>

<dl>
<dd>

**cc:** `typing.Optional[EmailsSendRequestCc]` — A single email or list of emails for one of the address fields
    
</dd>
</dl>

<dl>
<dd>

**bcc:** `typing.Optional[EmailsSendRequestBcc]` — A single email or list of emails for one of the address fields
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[str]` — Text content of the email, for email clients that may not support HTML
    
</dd>
</dl>

<dl>
<dd>

**html:** `typing.Optional[str]` — HTML content of the email. Can be specified alongside text
    
</dd>
</dl>

<dl>
<dd>

**attachments:** `typing.Optional[typing.List[EmailsSendRequestAttachmentsItem]]` — A list of attachments to add to the email
    
</dd>
</dl>

<dl>
<dd>

**reply_to_list:** `typing.Optional[EmailsSendRequestReplyToList]` — A reply-to list of email addresses
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Telemetry
<details><summary><code>client.telemetry.<a href="src/fern/telemetry/client.py">trace_list</a>(...) -> TraceListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get OpenTelemetry traces within a specified time window with flexible pagination options: Pass in only the end time to paginate backwards from there. Pass in a start time to paginate backwards from now until the start time. Pass in both to get resources within the time window. Choose to return in end_time order instead to view traces that completed in a window or since a time. Filter additionally by branch_ids or file_id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.telemetry import TraceListRequestDirection

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.telemetry.trace_list(
    direction=TraceListRequestDirection.ASC,
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**direction:** `TraceListRequestDirection` — Sort direction for the traces. Defaults to descending order of timestamp.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `int` — Maximum items to return in each paginated response
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[str]` — Include only resources from a given file identified by its ID
    
</dd>
</dl>

<dl>
<dd>

**branch_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Branch IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[datetime.datetime]` — Start date of the time window (earliest time)
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[datetime.datetime]` — End date of the time window (latest time)
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[TraceListRequestOrderBy]` — When set to end_time, traces are sorted by their end time, and pending traces are omitted. When set to start_time, all traces are included, with pending traces given "0" for their end time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.telemetry.<a href="src/fern/telemetry/client.py">log_list</a>(...) -> LogListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get OpenTelemetry logs within a specified time window with flexible pagination options: Pass in only the end time to paginate backwards from there. Pass in a start time to paginate backwards from now until the start time. Pass in both to get resources within the time window. Filter additionally by branch_ids or file_id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.telemetry import LogListRequestDirection

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.telemetry.log_list(
    direction=LogListRequestDirection.ASC,
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**direction:** `LogListRequestDirection` — Sort direction for the traces. Defaults to descending order of timestamp.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `int` — Maximum items to return in each paginated response
    
</dd>
</dl>

<dl>
<dd>

**trace_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[str]` — Include only resources from a given file identified by its ID
    
</dd>
</dl>

<dl>
<dd>

**branch_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Branch IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[datetime.datetime]` — Start date of the time window (earliest time)
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[datetime.datetime]` — End date of the time window (latest time)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## vals
<details><summary><code>client.vals.<a href="src/fern/vals/client.py">val_environment_variables_list</a>(...) -> ValEnvironmentVariablesListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List environment variables defined in this project. This only includes names, not values.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.vals.val_environment_variables_list(
    val_id="val_id",
    offset=1,
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**val_id:** `str` — Id of a val
    
</dd>
</dl>

<dl>
<dd>

**offset:** `int` — Number of items to skip in order to deliver paginated results
    
</dd>
</dl>

<dl>
<dd>

**limit:** `int` — Maximum items to return in each paginated response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vals.<a href="src/fern/vals/client.py">val_environment_variables_create</a>(...) -> TEnvironmentVariable</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new environment variable scoped to this project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.vals.val_environment_variables_create(
    val_id="val_id",
    value="value",
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

**val_id:** `str` — Id of a val
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — Value of the environment variable.
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Name or key of the environment variable, accessible via Deno.env or process.env
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the environment variable. Send null to clear an existing description; omit it to leave the description unchanged.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vals.<a href="src/fern/vals/client.py">val_environment_variables_update</a>(...) -> TEnvironmentVariable</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a environment variable scoped to this project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.vals.val_environment_variables_update(
    val_id="val_id",
    key="key",
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

**val_id:** `str` — Id of a val
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — Value of the environment variable.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the environment variable. Send null to clear an existing description; omit it to leave the description unchanged.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vals.<a href="src/fern/vals/client.py">val_environment_variables_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a environment variable scoped to this project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.vals.val_environment_variables_delete(
    val_id="val_id",
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

**val_id:** `str` — Id of a val
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vals.<a href="src/fern/vals/client.py">val_environment_variable_groups_list</a>(...) -> ValEnvironmentVariableGroupsListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the environment variable groups attached to this val. This only includes the groups, not the variables in them.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.vals.val_environment_variable_groups_list(
    val_id="val_id",
    offset=1,
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**val_id:** `str` — Id of a val
    
</dd>
</dl>

<dl>
<dd>

**offset:** `int` — Number of items to skip in order to deliver paginated results
    
</dd>
</dl>

<dl>
<dd>

**limit:** `int` — Maximum items to return in each paginated response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vals.<a href="src/fern/vals/client.py">val_environment_variable_groups_attach</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach an environment variable group to this val. Every variable in the group is injected into the val's environment. Variables defined on the val itself take precedence over variables with the same key in a group. Attaching a group that is already attached succeeds without doing anything.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.vals.val_environment_variable_groups_attach(
    val_id="val_id",
    group_id="group_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**val_id:** `str` — Id of a val
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `str` — Id of an environment variable group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vals.<a href="src/fern/vals/client.py">val_environment_variable_groups_detach</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detach an environment variable group from this val. The group itself, and the variables in it, are left alone.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.vals.val_environment_variable_groups_detach(
    val_id="val_id",
    group_id="group_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**val_id:** `str` — Id of a val
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `str` — Id of an environment variable group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vals.<a href="src/fern/vals/client.py">vals_get2</a>(...) -> Val</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a val by id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.vals.vals_get2(
    val_id="val_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**val_id:** `str` — Id of a val
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vals.<a href="src/fern/vals/client.py">projects_delete2</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a project
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.vals.projects_delete2(
    val_id="val_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**val_id:** `str` — Id of a val
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vals.<a href="src/fern/vals/client.py">vals_list2</a>(...) -> ValsList2Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all vals including all public vals and your unlisted and private vals
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.vals.vals_list2(
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `int` — Maximum items to return in each paginated response
    
</dd>
</dl>

<dl>
<dd>

**privacy:** `typing.Optional[ValsList2RequestPrivacy]` — This resource's privacy setting. Unlisted resources do not appear on profile pages or elsewhere, but you can link to them.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — User ID to filter by
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[datetime.datetime]` — Cursor to start the pagination from
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vals.<a href="src/fern/vals/client.py">vals_create2</a>(...) -> Val</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new val
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.vals import ValsCreate2RequestPrivacy

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.vals.vals_create2(
    name="myVal",
    description="My val",
    privacy=ValsCreate2RequestPrivacy.PUBLIC,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**privacy:** `ValsCreate2RequestPrivacy` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `typing.Optional[str]` — ID of the org to create the val in
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vals.<a href="src/fern/vals/client.py">branches_get2</a>(...) -> Branch</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a branch by id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.vals.branches_get2(
    val_id="val_id",
    branch_id="branch_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**val_id:** `str` — Id of a val
    
</dd>
</dl>

<dl>
<dd>

**branch_id:** `str` — Id of a branch
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vals.<a href="src/fern/vals/client.py">branches_delete2</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a branch
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.vals.branches_delete2(
    val_id="val_id",
    branch_id="branch_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**val_id:** `str` — Id of a val
    
</dd>
</dl>

<dl>
<dd>

**branch_id:** `str` — Id of a branch
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vals.<a href="src/fern/vals/client.py">branches_list2</a>(...) -> BranchesList2Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all branches for a val
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.vals.branches_list2(
    val_id="val_id",
    offset=1,
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**val_id:** `str` — Id of a val
    
</dd>
</dl>

<dl>
<dd>

**offset:** `int` — Number of items to skip in order to deliver paginated results
    
</dd>
</dl>

<dl>
<dd>

**limit:** `int` — Maximum items to return in each paginated response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vals.<a href="src/fern/vals/client.py">branches_create2</a>(...) -> Branch</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new branch
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.vals.branches_create2(
    val_id="val_id",
    name="my-branch",
    branch_id="00000000-0000-0000-0000-000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**val_id:** `str` — Id of a val
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**branch_id:** `typing.Optional[str]` — The branch ID to fork from. If this is not specified, the new branch will be forked from main.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vals.<a href="src/fern/vals/client.py">val_files_get2</a>(...) -> ValFilesGet2Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get metadata for files and directories in a val. If path is an empty string, returns files at the root directory.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.vals.val_files_get2(
    val_id="val_id",
    path="path",
    recursive=True,
    offset=1,
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**val_id:** `str` — Id of a val
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.
    
</dd>
</dl>

<dl>
<dd>

**recursive:** `bool` — Whether to recursively act on all files in the project
    
</dd>
</dl>

<dl>
<dd>

**offset:** `int` — Number of items to skip in order to deliver paginated results
    
</dd>
</dl>

<dl>
<dd>

**limit:** `int` — Maximum items to return in each paginated response
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` — Specific branch version to query
    
</dd>
</dl>

<dl>
<dd>

**branch_id:** `typing.Optional[str]` — Id to query
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vals.<a href="src/fern/vals/client.py">files_create2</a>(...) -> FileRevisionMetadataV2</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new file, project val or directory
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.vals import FilesCreate2RequestBodyZero, FilesCreate2RequestBodyZeroType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.vals.files_create2(
    val_id="val_id",
    path="path",
    request=FilesCreate2RequestBodyZero(
        type=FilesCreate2RequestBodyZeroType.DIRECTORY,
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

**val_id:** `str` — Id of a val
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.
    
</dd>
</dl>

<dl>
<dd>

**request:** `FilesCreate2RequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**branch_id:** `typing.Optional[str]` — The specified branch of the resource. Defaults to main if not provided.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vals.<a href="src/fern/vals/client.py">file_content_update2</a>(...) -> FileRevisionMetadataV2</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a file's content
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.vals.file_content_update2(
    val_id="val_id",
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**val_id:** `str` — Id of a val
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.
    
</dd>
</dl>

<dl>
<dd>

**branch_id:** `typing.Optional[str]` — The specified branch of the resource. Defaults to main if not provided.
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — File and val content. An empty string will create an empty file. When creating a directory, the content should be null or undefined.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[FileContentUpdate2RequestType]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_path:** `typing.Optional[str]` — Path to the directory you'd like to move this file to (e.g. 'folder1/folder2')
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vals.<a href="src/fern/vals/client.py">files_delete2</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a file or a directory. To delete a directory and all of its children, use the recursive flag. To delete all files, pass in an empty path and the recursive flag.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.vals.files_delete2(
    val_id="val_id",
    path="path",
    recursive=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**val_id:** `str` — Id of a val
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.
    
</dd>
</dl>

<dl>
<dd>

**recursive:** `bool` — Whether to recursively act on all files in the project
    
</dd>
</dl>

<dl>
<dd>

**branch_id:** `typing.Optional[str]` — The specified branch of the resource. Defaults to main if not provided.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vals.<a href="src/fern/vals/client.py">files_content_get2</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download file content
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.vals.files_content_get2(
    val_id="val_id",
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**val_id:** `str` — Id of a val
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` — Specific branch version to query
    
</dd>
</dl>

<dl>
<dd>

**branch_id:** `typing.Optional[str]` — Id to query
    
</dd>
</dl>

<dl>
<dd>

**if_match:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**if_unmodified_since:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**if_none_match:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**if_modified_since:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cache_control:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.files.<a href="src/fern/files/client.py">query_val_file_by_id</a>(...) -> FileRevisionMetadataV2</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get file metadata by file ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.files.query_val_file_by_id(
    file_id="file_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — ID of a file in a val
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Orgs
<details><summary><code>client.orgs.<a href="src/fern/orgs/client.py">list</a>(...) -> OrgsListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all orgs you are a member of
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.orgs.list(
    offset=1,
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**offset:** `int` — Number of items to skip in order to deliver paginated results
    
</dd>
</dl>

<dl>
<dd>

**limit:** `int` — Maximum items to return in each paginated response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orgs.<a href="src/fern/orgs/client.py">memberships_list</a>(...) -> typing.List[Membership]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all memberships of an org
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.orgs.memberships_list(
    org_id="org_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Id of an org
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Connections
<details><summary><code>client.connections.<a href="src/fern/connections/client.py">post_v3connections_slack_token</a>(...) -> PostV3ConnectionsSlackTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a valid Slack access token for a connected workspace. Automatically refreshes the token if expired.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.connections.post_v3connections_slack_token(
    team_id="team_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The Slack team/workspace ID (e.g., 'T9TK3CUKW')
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">post_v3connections_google_docs_token</a>(...) -> PostV3ConnectionsGoogleDocsTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a valid Google access token for a connected Google account. Automatically refreshes the token if expired.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.connections.post_v3connections_google_docs_token(
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

**email:** `str` — The Google account email
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Val
<details><summary><code>client.val.<a href="src/fern/val/client.py">get_v3val_viewer</a>(...) -> GetV3ValViewerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Look up the identity of the viewer of an app-authenticated (intranet) val, given the X-Val-Town-User header value that Fastify forwarded to the val. Authenticated with the val's own API token (bearer auth). The projectId inside the signed header must match the caller's own project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.val.get_v3val_viewer(
    val_town_user="x-val-town-user",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**val_town_user:** `str` — The signed X-Val-Town-User header value Fastify forwarded to the val.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EnvVarGroups
<details><summary><code>client.env_var_groups.<a href="src/fern/env_var_groups/client.py">environment_variable_groups_list</a>(...) -> EnvironmentVariableGroupsListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List environment variable groups
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.env_var_groups.environment_variable_groups_list(
    offset=1,
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**offset:** `int` — Number of items to skip in order to deliver paginated results
    
</dd>
</dl>

<dl>
<dd>

**limit:** `int` — Maximum items to return in each paginated response
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `typing.Optional[str]` — Organization to act in. Defaults to the organization that owns the API token. List the organizations you belong to with GET /v2/orgs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.env_var_groups.<a href="src/fern/env_var_groups/client.py">environment_variable_groups_create</a>(...) -> EnvironmentVariableGroupsCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new environment variable group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.env_var_groups.environment_variable_groups_create(
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `typing.Optional[str]` — Organization to act in. Defaults to the organization that owns the API token. List the organizations you belong to with GET /v2/orgs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.env_var_groups.<a href="src/fern/env_var_groups/client.py">environment_variable_groups_rename</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rename an environment variable group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.env_var_groups.environment_variable_groups_rename(
    id="id",
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

**id:** `str` — Environment variable group ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — New name for group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.env_var_groups.<a href="src/fern/env_var_groups/client.py">environment_variable_groups_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an environment variable group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.env_var_groups.environment_variable_groups_delete(
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

**id:** `str` — Environment variable group ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.env_var_groups.<a href="src/fern/env_var_groups/client.py">environment_variable_groups_get</a>(...) -> typing.List[TEnvironmentVariable]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List variables in an environment variable group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.env_var_groups.environment_variable_groups_get(
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

**id:** `str` — Environment variable group ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.env_var_groups.<a href="src/fern/env_var_groups/client.py">environment_variable_groups_create_variable</a>(...) -> TEnvironmentVariable</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an environment variable in a group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.env_var_groups.environment_variable_groups_create_variable(
    id="id",
    value="value",
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

**id:** `str` — Environment variable group ID
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — Value of the environment variable.
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Name or key of the environment variable, accessible via Deno.env or process.env
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the environment variable. Send null to clear an existing description; omit it to leave the description unchanged.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.env_var_groups.<a href="src/fern/env_var_groups/client.py">environment_variable_groups_upsert_variable</a>(...) -> TEnvironmentVariable</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update an environment variable in a group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.env_var_groups.environment_variable_groups_upsert_variable(
    id="id",
    key="key",
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

**id:** `str` — Environment variable group ID
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Environment variable key
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — Value of the environment variable.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the environment variable. Send null to clear an existing description; omit it to leave the description unchanged.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.env_var_groups.<a href="src/fern/env_var_groups/client.py">environment_variable_groups_variable_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an environment variable in a group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.env_var_groups.environment_variable_groups_variable_delete(
    id="id",
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

**id:** `str` — Environment variable group ID
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Environment variable key
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

