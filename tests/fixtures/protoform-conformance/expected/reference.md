# Reference
## Library RPC
<details><summary><code>client.library_rpc.<a href="src/fern/library_rpc/client.py">protoform_conformance_v1library_service_list_books</a>(...) -> ProtoformConformanceV1ListBooksResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.library_rpc.protoform_conformance_v1library_service_list_books(
    parent="publishers/demo-library",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**parent:** `PublisherName` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — Case-insensitive title or ISBN substring.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.library_rpc.<a href="src/fern/library_rpc/client.py">protoform_conformance_v1library_service_get_book</a>(...) -> ProtoformConformanceV1Book</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.library_rpc.protoform_conformance_v1library_service_get_book(
    name="publishers/demo-library/books/protoform-guide",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `BookName` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.library_rpc.<a href="src/fern/library_rpc/client.py">protoform_conformance_v1library_service_create_book</a>(...) -> ProtoformConformanceV1Book</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ProtoformConformanceV1Book
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.library_rpc.protoform_conformance_v1library_service_create_book(
    parent="publishers/demo-library",
    book=ProtoformConformanceV1Book(
        display_name="The Protoform Guide",
        isbn="9783161484100",
    ),
    book_id="protoform-guide",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**parent:** `PublisherName` 
    
</dd>
</dl>

<dl>
<dd>

**book:** `ProtoformConformanceV1Book` 
    
</dd>
</dl>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**validate_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.library_rpc.<a href="src/fern/library_rpc/client.py">protoform_conformance_v1library_service_update_book</a>(...) -> ProtoformConformanceV1Book</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ProtoformConformanceV1Book
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.library_rpc.protoform_conformance_v1library_service_update_book(
    book=ProtoformConformanceV1Book(
        display_name="The Protoform Guide",
        isbn="9783161484100",
    ),
    update_mask="displayName,note",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book:** `ProtoformConformanceV1Book` 
    
</dd>
</dl>

<dl>
<dd>

**update_mask:** `str` — Protobuf JSON FieldMask, such as displayName,note.
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**validate_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**allow_missing:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.library_rpc.<a href="src/fern/library_rpc/client.py">protoform_conformance_v1library_service_delete_book</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a book by resource name and etag. The server validates optimistic concurrency, returns a structured Connect error when the version is stale, and responds with an empty protobuf message after successful deletion.
</dd>
</dl>
</dd>
</dl>

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

client.library_rpc.protoform_conformance_v1library_service_delete_book(
    name="publishers/demo-library/books/protoform-guide",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `BookName` 
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**etag:** `typing.Optional[str]` — Last observed book etag.
    
</dd>
</dl>

<dl>
<dd>

**validate_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

