# Reference
## Management
<details><summary><code>client.management.<a href="src/fern/management/client.py#L25-L51">get_actuator_info</a>() -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.management.get_actuator_info()

```
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

## User session
<details><summary><code>client.user_session.<a href="src/fern/user_session/client.py#L25-L48">post_logout</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invalidates the current session and clean up any remember-me authentication.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.user_session.post_logout()

```
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

<details><summary><code>client.user_session.<a href="src/fern/user_session/client.py#L50-L73">post_logout1</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invalidates the current session and clean up any remember-me authentication.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.user_session.post_logout1()

```
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

<details><summary><code>client.user_session.<a href="src/fern/user_session/client.py#L75-L98">convert_header_session_to_cookie</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Forcefully return Set-Cookie header, even if the session is contained in the X-Auth-Token header.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.user_session.convert_header_session_to_cookie()

```
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

## Deprecated
<details><summary><code>client.deprecated.<a href="src/fern/deprecated/client.py#L31-L67">get_age_ratings1</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use GET /v2/age-ratings instead. Deprecated since 1.26.0
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.deprecated.get_age_ratings1()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deprecated.<a href="src/fern/deprecated/client.py#L69-L115">get_authors_deprecated</a>(...) -> typing.List[AuthorDto]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use GET /api/v2/authors instead. Deprecated since 1.20.0.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.deprecated.get_authors_deprecated()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**library_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**series_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deprecated.<a href="src/fern/deprecated/client.py#L117-L145">get_authors_names1</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use GET /v2/authors/names instead. Deprecated since 1.26.0
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.deprecated.get_authors_names1()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deprecated.<a href="src/fern/deprecated/client.py#L147-L171">get_authors_roles1</a>() -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use GET /v2/authors/roles instead. Deprecated since 1.26.0
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.deprecated.get_authors_roles1()

```
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

<details><summary><code>client.deprecated.<a href="src/fern/deprecated/client.py#L173-L209">get_genres1</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use GET /v2/genres instead. Deprecated since 1.26.0
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.deprecated.get_genres1()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deprecated.<a href="src/fern/deprecated/client.py#L211-L247">get_languages1</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use GET /v2/languages instead. Deprecated since 1.26.0
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.deprecated.get_languages1()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deprecated.<a href="src/fern/deprecated/client.py#L249-L398">update_library_by_id_deprecated</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use PATCH /api/v1/libraries/{libraryId} instead. Deprecated since 1.3.0.

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.deprecated.update_library_by_id_deprecated(
    library_id="libraryId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LibraryUpdateDto` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deprecated.<a href="src/fern/deprecated/client.py#L400-L436">get_publishers1</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use GET /v2/publishers instead. Deprecated since 1.26.0
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.deprecated.get_publishers1()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deprecated.<a href="src/fern/deprecated/client.py#L438-L474">get_series_release_dates</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use GET /v2/series/release-years instead. Deprecated since 1.26.0
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.deprecated.get_series_release_dates()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deprecated.<a href="src/fern/deprecated/client.py#L476-L512">get_sharing_labels1</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use GET /v2/sharing-labels instead. Deprecated since 1.26.0
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.deprecated.get_sharing_labels1()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deprecated.<a href="src/fern/deprecated/client.py#L514-L550">get_tags1</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use GET /v2/tags instead. Deprecated since 1.26.0
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.deprecated.get_tags1()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deprecated.<a href="src/fern/deprecated/client.py#L552-L591">get_book_tags</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use GET /v2/tags instead. Deprecated since 1.26.0
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.deprecated.get_book_tags()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**series_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**readlist_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deprecated.<a href="src/fern/deprecated/client.py#L593-L629">get_series_tags</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use GET /v2/tags instead. Deprecated since 1.26.0
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.deprecated.get_series_tags()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Announcements
<details><summary><code>client.announcements.<a href="src/fern/announcements/client.py#L29-L53">get_announcements</a>() -> JsonFeedDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.announcements.get_announcements()

```
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

<details><summary><code>client.announcements.<a href="src/fern/announcements/client.py#L55-L84">mark_announcements_read</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.announcements.mark_announcements_read(
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

## Books
<details><summary><code>client.books.<a href="src/fern/books/client.py#L39-L121">get_all_books_deprecated</a>(...) -> PageBookDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use POST /api/v1/books/list instead. Deprecated since 1.19.0.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.books.get_all_books_deprecated()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**media_status:** `typing.Optional[typing.Union[GetAllBooksDeprecatedRequestMediaStatusItem, typing.Sequence[GetAllBooksDeprecatedRequestMediaStatusItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**read_status:** `typing.Optional[typing.Union[GetAllBooksDeprecatedRequestReadStatusItem, typing.Sequence[GetAllBooksDeprecatedRequestReadStatusItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**released_after:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.books.<a href="src/fern/books/client.py#L123-L170">get_books_duplicates</a>(...) -> PageBookDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return books that have the same file hash.

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.books.get_books_duplicates()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.books.<a href="src/fern/books/client.py#L172-L213">get_books_latest</a>(...) -> PageBookDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return newly added or updated books.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.books.get_books_latest()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.books.<a href="src/fern/books/client.py#L215-L270">get_books</a>(...) -> PageBookDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.books.get_books()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**condition:** `typing.Optional[SearchConditionBook]` 
    
</dd>
</dl>

<dl>
<dd>

**full_text_search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.books.<a href="src/fern/books/client.py#L272-L306">update_book_metadata_by_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set a field to null to unset the metadata. You can omit fields you don't want to update.

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, BookMetadataUpdateDto
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.books.update_book_metadata_by_batch(
    request={
        "key": BookMetadataUpdateDto()
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

**request:** `typing.Dict[str, BookMetadataUpdateDto]` — A map of book IDs which values are the metadata fields to update. Set a field to null to unset the metadata. You can omit fields you don't want to update.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.books.<a href="src/fern/books/client.py#L308-L349">get_books_on_deck</a>(...) -> PageBookDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return first unread book of series with at least one book read and no books in progress.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.books.get_books_on_deck()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.books.<a href="src/fern/books/client.py#L351-L377">get_book_by_id</a>(...) -> BookDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.books.get_book_by_id(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.books.<a href="src/fern/books/client.py#L379-L406">book_analyze</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.books.book_analyze(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.books.<a href="src/fern/books/client.py#L408-L440">download_book_file</a>(...) -> StreamingResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download the book file.

Required role: **FILE_DOWNLOAD**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.books.download_book_file(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.books.<a href="src/fern/books/client.py#L442-L469">delete_book_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.books.delete_book_file(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.books.<a href="src/fern/books/client.py#L471-L503">download_book_file1</a>(...) -> StreamingResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download the book file.

Required role: **FILE_DOWNLOAD**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.books.download_book_file1(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.books.<a href="src/fern/books/client.py#L505-L614">update_book_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set a field to null to unset the metadata. You can omit fields you don't want to update.

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.books.update_book_metadata(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `BookMetadataUpdateDto` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.books.<a href="src/fern/books/client.py#L616-L643">book_refresh_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.books.book_refresh_metadata(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.books.<a href="src/fern/books/client.py#L645-L673">get_book_sibling_next</a>(...) -> BookDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.books.get_book_sibling_next(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.books.<a href="src/fern/books/client.py#L675-L703">get_book_sibling_previous</a>(...) -> BookDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.books.get_book_sibling_previous(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.books.<a href="src/fern/books/client.py#L705-L734">delete_book_read_progress</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mark book as unread
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.books.delete_book_read_progress(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.books.<a href="src/fern/books/client.py#L736-L776">mark_book_read_progress</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mark book as read and/or change page progress.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.books.mark_book_read_progress(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**completed:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.books.<a href="src/fern/books/client.py#L778-L806">get_read_lists_by_book_id</a>(...) -> typing.List[ReadListDto]</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.books.get_read_lists_by_book_id(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Import
<details><summary><code>client.import_.<a href="src/fern/import_/client.py#L31-L74">books</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, BookImportDto
from fern.environment import FernApiEnvironment
from fern.import_ import BookImportBatchDtoCopyMode

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.import_.books(
    books=[
        BookImportDto(
            series_id="seriesId",
            source_file="sourceFile",
        )
    ],
    copy_mode=BookImportBatchDtoCopyMode.MOVE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**books:** `typing.List[BookImportDto]` 
    
</dd>
</dl>

<dl>
<dd>

**copy_mode:** `BookImportBatchDtoCopyMode` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.import_.<a href="src/fern/import_/client.py#L76-L108">scan_transient_books</a>(...) -> typing.List[TransientBookDto]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scan provided folder for transient books.

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.import_.scan_transient_books(
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

**path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.import_.<a href="src/fern/import_/client.py#L110-L140">analyze_transient_book</a>(...) -> TransientBookDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.import_.analyze_transient_book(
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

<details><summary><code>client.import_.<a href="src/fern/import_/client.py#L142-L175">get_page_by_transient_book_id</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.import_.get_page_by_transient_book_id(
    id="id",
    page_number=1,
)

```
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

**page_number:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Book Poster
<details><summary><code>client.book_poster.<a href="src/fern/book_poster/client.py#L30-L62">books_regenerate_thumbnails</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.book_poster.books_regenerate_thumbnails()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**for_bigger_result_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.book_poster.<a href="src/fern/book_poster/client.py#L64-L92">get_book_thumbnail</a>(...) -> typing.Iterator[bytes]</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.book_poster.get_book_thumbnail(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.book_poster.<a href="src/fern/book_poster/client.py#L94-L122">get_book_thumbnails</a>(...) -> typing.List[ThumbnailBookDto]</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.book_poster.get_book_thumbnails(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.book_poster.<a href="src/fern/book_poster/client.py#L124-L166">add_user_uploaded_book_thumbnail</a>(...) -> ThumbnailBookDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.book_poster.add_user_uploaded_book_thumbnail(
    book_id="bookId",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**selected:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.book_poster.<a href="src/fern/book_poster/client.py#L168-L199">get_book_thumbnail_by_id</a>(...) -> typing.Iterator[bytes]</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.book_poster.get_book_thumbnail_by_id(
    book_id="bookId",
    thumbnail_id="thumbnailId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**thumbnail_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.book_poster.<a href="src/fern/book_poster/client.py#L201-L237">delete_user_uploaded_book_thumbnail</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Only uploaded posters can be deleted.

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.book_poster.delete_user_uploaded_book_thumbnail(
    book_id="bookId",
    thumbnail_id="thumbnailId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**thumbnail_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.book_poster.<a href="src/fern/book_poster/client.py#L239-L273">mark_book_thumbnail_selected</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.book_poster.mark_book_thumbnail_selected(
    book_id="bookId",
    thumbnail_id="thumbnailId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**thumbnail_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## WebPub Manifest
<details><summary><code>client.web_pub_manifest.<a href="src/fern/web_pub_manifest/client.py#L34-L62">get_book_web_pub_manifest</a>(...) -> WpPublicationDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.web_pub_manifest.get_book_web_pub_manifest(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.web_pub_manifest.<a href="src/fern/web_pub_manifest/client.py#L64-L92">get_book_web_pub_manifest_divina</a>(...) -> WpPublicationDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.web_pub_manifest.get_book_web_pub_manifest_divina(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.web_pub_manifest.<a href="src/fern/web_pub_manifest/client.py#L94-L122">get_book_web_pub_manifest_epub</a>(...) -> WpPublicationDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.web_pub_manifest.get_book_web_pub_manifest_epub(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.web_pub_manifest.<a href="src/fern/web_pub_manifest/client.py#L124-L152">get_book_web_pub_manifest_pdf</a>(...) -> WpPublicationDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.web_pub_manifest.get_book_web_pub_manifest_pdf(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.web_pub_manifest.<a href="src/fern/web_pub_manifest/client.py#L154-L184">get_book_positions</a>(...) -> R2Positions</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Positions API is a proposed standard for OPDS 2 and Readium. It is used by the Epub Reader.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.web_pub_manifest.get_book_positions(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.web_pub_manifest.<a href="src/fern/web_pub_manifest/client.py#L186-L216">get_book_progression</a>(...) -> R2Progression</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Progression API is a proposed standard for OPDS 2 and Readium. It is used by the Epub Reader.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.web_pub_manifest.get_book_progression(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.web_pub_manifest.<a href="src/fern/web_pub_manifest/client.py#L218-L274">update_book_progression</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Progression API is a proposed standard for OPDS 2 and Readium. It is used by the Epub Reader.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, R2Device, R2Locator
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.web_pub_manifest.update_book_progression(
    book_id="bookId",
    device=R2Device(
        id="id",
        name="name",
    ),
    locator=R2Locator(
        href="href",
        type="type",
    ),
    modified=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `R2Progression` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.web_pub_manifest.<a href="src/fern/web_pub_manifest/client.py#L276-L309">get_book_epub_resource</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return a resource from within an Epub book.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.web_pub_manifest.get_book_epub_resource(
    book_id="bookId",
    resource="resource",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Book Pages
<details><summary><code>client.book_pages.<a href="src/fern/book_pages/client.py#L28-L56">get_book_pages</a>(...) -> typing.List[PageDto]</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.book_pages.get_book_pages(
    book_id="bookId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.book_pages.<a href="src/fern/book_pages/client.py#L58-L118">get_book_page_by_number</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **PAGE_STREAMING**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.book_pages.get_book_page_by_number(
    book_id="bookId",
    page_number=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**convert:** `typing.Optional[GetBookPageByNumberRequestConvert]` — Convert the image to the provided format.
    
</dd>
</dl>

<dl>
<dd>

**zero_based:** `typing.Optional[bool]` — If set to true, pages will start at index 0. If set to false, pages will start at index 1.
    
</dd>
</dl>

<dl>
<dd>

**content_negotiation:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**accept:** `typing.Optional[typing.List[MediaType]]` — Some very limited server driven content negotiation is handled. If a book is a PDF book, and the Accept header contains 'application/pdf' as a more specific type than other 'image/' types, a raw PDF page will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.book_pages.<a href="src/fern/book_pages/client.py#L120-L155">get_book_page_raw_by_number</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the book page in raw format, without content negotiation.

Required role: **PAGE_STREAMING**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.book_pages.get_book_page_raw_by_number(
    book_id="bookId",
    page_number=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.book_pages.<a href="src/fern/book_pages/client.py#L157-L192">get_book_page_thumbnail_by_number</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The image is resized to 300px on the largest dimension.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.book_pages.get_book_page_thumbnail_by_number(
    book_id="bookId",
    page_number=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Claim
<details><summary><code>client.claim.<a href="src/fern/claim/client.py#L27-L51">get_claim_status</a>() -> ClaimStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check whether this server has already been claimed.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.claim.get_claim_status()

```
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

<details><summary><code>client.claim.<a href="src/fern/claim/client.py#L53-L88">server</a>(...) -> UserDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an admin user with the provided credentials.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.claim.server(
    komga_email="X-Komga-Email",
    komga_password="X-Komga-Password",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**komga_email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**komga_password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Client settings
<details><summary><code>client.client_settings.<a href="src/fern/client_settings/client.py#L31-L62">delete_global_settings</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Setting key should be a valid lowercase namespace string like 'application.domain.key'

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.client_settings.delete_global_settings(
    request=[
        "application.key1",
        "application.key2"
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

<details><summary><code>client.client_settings.<a href="src/fern/client_settings/client.py#L64-L107">save_global_setting</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Setting key should be a valid lowercase namespace string like 'application.domain.key'

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ClientSettingGlobalUpdateDto
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.client_settings.save_global_setting(
    request={
        "application.key1": ClientSettingGlobalUpdateDto(
            allow_unauthorized=True,
            value="a string value",
        ),
        "application.key2": ClientSettingGlobalUpdateDto(
            allow_unauthorized=False,
            value="{\"json\":\"object\"}",
        )
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

**request:** `typing.Dict[str, ClientSettingGlobalUpdateDto]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.client_settings.<a href="src/fern/client_settings/client.py#L109-L135">get_global_settings</a>() -> typing.Dict[str, ClientSettingDto]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

For unauthenticated users, only settings with 'allowUnauthorized=true' will be returned.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.client_settings.get_global_settings()

```
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

<details><summary><code>client.client_settings.<a href="src/fern/client_settings/client.py#L137-L166">delete_user_settings</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Setting key should be a valid lowercase namespace string like 'application.domain.key'
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.client_settings.delete_user_settings(
    request=[
        "application.key1",
        "application.key2"
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

<details><summary><code>client.client_settings.<a href="src/fern/client_settings/client.py#L168-L207">save_user_setting</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Setting key should be a valid lowercase namespace string like 'application.domain.key'
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ClientSettingUserUpdateDto
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.client_settings.save_user_setting(
    request={
        "application.key1": ClientSettingUserUpdateDto(
            value="a string value",
        ),
        "application.key2": ClientSettingUserUpdateDto(
            value="{\"json\":\"object\"}",
        )
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

**request:** `typing.Dict[str, ClientSettingUserUpdateDto]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.client_settings.<a href="src/fern/client_settings/client.py#L209-L233">get_user_settings</a>() -> typing.Dict[str, ClientSettingDto]</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.client_settings.get_user_settings()

```
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

## Collections
<details><summary><code>client.collections.<a href="src/fern/collections/client.py#L30-L75">get_collections</a>(...) -> PageCollectionDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.get_collections()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py#L77-L120">create_collection</a>(...) -> CollectionDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.create_collection(
    name="name",
    ordered=True,
    series_ids=[
        "seriesIds"
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**ordered:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**series_ids:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py#L122-L150">get_collection_by_id</a>(...) -> CollectionDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.get_collection_by_id(
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

<details><summary><code>client.collections.<a href="src/fern/collections/client.py#L152-L179">delete_collection_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.delete_collection_by_id(
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

<details><summary><code>client.collections.<a href="src/fern/collections/client.py#L181-L224">update_collection_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.update_collection_by_id(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ordered:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**series_ids:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Collection Series
<details><summary><code>client.collection_series.<a href="src/fern/collection_series/client.py#L28-L134">get_series_by_collection_id</a>(...) -> PageSeriesDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.collection_series.get_series_by_collection_id(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[GetSeriesByCollectionIdRequestStatusItem, typing.Sequence[GetSeriesByCollectionIdRequestStatusItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**read_status:** `typing.Optional[typing.Union[GetSeriesByCollectionIdRequestReadStatusItem, typing.Sequence[GetSeriesByCollectionIdRequestReadStatusItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**publisher:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**genre:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**age_rating:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**release_year:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**complete:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**author:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Author criteria in the format: name,role. Multiple author criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Collection Poster
<details><summary><code>client.collection_poster.<a href="src/fern/collection_poster/client.py#L30-L58">get_collection_thumbnail</a>(...) -> typing.Iterator[bytes]</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.collection_poster.get_collection_thumbnail(
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

<details><summary><code>client.collection_poster.<a href="src/fern/collection_poster/client.py#L60-L88">get_collection_thumbnails</a>(...) -> typing.List[ThumbnailSeriesCollectionDto]</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.collection_poster.get_collection_thumbnails(
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

<details><summary><code>client.collection_poster.<a href="src/fern/collection_poster/client.py#L90-L132">add_user_uploaded_collection_thumbnail</a>(...) -> ThumbnailSeriesCollectionDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.collection_poster.add_user_uploaded_collection_thumbnail(
    id="id",
    file="example_file",
)

```
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

**file:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**selected:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collection_poster.<a href="src/fern/collection_poster/client.py#L134-L165">get_collection_thumbnail_by_id</a>(...) -> typing.Iterator[bytes]</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.collection_poster.get_collection_thumbnail_by_id(
    id="id",
    thumbnail_id="thumbnailId",
)

```
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

**thumbnail_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collection_poster.<a href="src/fern/collection_poster/client.py#L167-L201">delete_user_uploaded_collection_thumbnail</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.collection_poster.delete_user_uploaded_collection_thumbnail(
    id="id",
    thumbnail_id="thumbnailId",
)

```
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

**thumbnail_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collection_poster.<a href="src/fern/collection_poster/client.py#L203-L237">mark_collection_thumbnail_selected</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.collection_poster.mark_collection_thumbnail_selected(
    id="id",
    thumbnail_id="thumbnailId",
)

```
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

**thumbnail_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## File system
<details><summary><code>client.file_system.<a href="src/fern/file_system/client.py#L29-L66">get_directory_listing</a>(...) -> DirectoryListingDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List folders and files from the host server's file system. If no request body is passed then the root directories are returned.

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.file_system.get_directory_listing(
    path="path",
    show_files=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**show_files:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Fonts
<details><summary><code>client.fonts.<a href="src/fern/fonts/client.py#L25-L49">get_fonts</a>() -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all available font families.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.fonts.get_fonts()

```
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

<details><summary><code>client.fonts.<a href="src/fern/fonts/client.py#L51-L81">get_font_family_as_css</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download a CSS file with the @font-face block for the font family. This is used by the Epub Reader to change fonts.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.fonts.get_font_family_as_css(
    font_family="fontFamily",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**font_family:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fonts.<a href="src/fern/fonts/client.py#L83-L114">get_font_file</a>(...) -> typing.Iterator[bytes]</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.fonts.get_font_file(
    font_family="fontFamily",
    font_file="fontFile",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**font_family:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**font_file:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## History
<details><summary><code>client.history.<a href="src/fern/history/client.py#L26-L68">get_historical_events</a>(...) -> PageHistoricalEventDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.history.get_historical_events()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Libraries
<details><summary><code>client.libraries.<a href="src/fern/libraries/client.py#L33-L57">get_libraries</a>() -> typing.List[LibraryDto]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The libraries are filtered based on the current user's permissions
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.libraries.get_libraries()

```
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

<details><summary><code>client.libraries.<a href="src/fern/libraries/client.py#L59-L234">add_library</a>(...) -> LibraryDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.libraries import LibraryCreationDtoScanInterval, LibraryCreationDtoSeriesCover

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.libraries.add_library(
    analyze_dimensions=True,
    convert_to_cbz=True,
    empty_trash_after_scan=True,
    hash_files=True,
    hash_koreader=True,
    hash_pages=True,
    import_barcode_isbn=True,
    import_comic_info_book=True,
    import_comic_info_collection=True,
    import_comic_info_read_list=True,
    import_comic_info_series=True,
    import_comic_info_series_append_volume=True,
    import_epub_book=True,
    import_epub_series=True,
    import_local_artwork=True,
    import_mylar_series=True,
    name="name",
    repair_extensions=True,
    root="root",
    scan_cbx=True,
    scan_directory_exclusions=[
        "scanDirectoryExclusions"
    ],
    scan_epub=True,
    scan_force_modified_time=True,
    scan_interval=LibraryCreationDtoScanInterval.DISABLED,
    scan_on_startup=True,
    scan_pdf=True,
    series_cover=LibraryCreationDtoSeriesCover.FIRST,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**analyze_dimensions:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**convert_to_cbz:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**empty_trash_after_scan:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**hash_files:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**hash_koreader:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**hash_pages:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**import_barcode_isbn:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**import_comic_info_book:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**import_comic_info_collection:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**import_comic_info_read_list:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**import_comic_info_series:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**import_comic_info_series_append_volume:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**import_epub_book:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**import_epub_series:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**import_local_artwork:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**import_mylar_series:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**repair_extensions:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**root:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scan_cbx:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**scan_directory_exclusions:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**scan_epub:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**scan_force_modified_time:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**scan_interval:** `LibraryCreationDtoScanInterval` 
    
</dd>
</dl>

<dl>
<dd>

**scan_on_startup:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**scan_pdf:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**series_cover:** `LibraryCreationDtoSeriesCover` 
    
</dd>
</dl>

<dl>
<dd>

**oneshots_directory:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.libraries.<a href="src/fern/libraries/client.py#L236-L264">get_library_by_id</a>(...) -> LibraryDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.libraries.get_library_by_id(
    library_id="libraryId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.libraries.<a href="src/fern/libraries/client.py#L266-L293">delete_library_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.libraries.delete_library_by_id(
    library_id="libraryId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.libraries.<a href="src/fern/libraries/client.py#L295-L444">update_library_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can omit fields you don't want to update

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.libraries.update_library_by_id(
    library_id="libraryId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LibraryUpdateDto` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.libraries.<a href="src/fern/libraries/client.py#L446-L473">library_analyze</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.libraries.library_analyze(
    library_id="libraryId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.libraries.<a href="src/fern/libraries/client.py#L475-L502">library_empty_trash</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.libraries.library_empty_trash(
    library_id="libraryId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.libraries.<a href="src/fern/libraries/client.py#L504-L533">library_refresh_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.libraries.library_refresh_metadata(
    library_id="libraryId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.libraries.<a href="src/fern/libraries/client.py#L535-L570">library_scan</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.libraries.library_scan(
    library_id="libraryId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**deep:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## OAuth2
<details><summary><code>client.o_auth2.<a href="src/fern/o_auth2/client.py#L26-L50">get_o_auth2providers</a>() -> typing.List[OAuth2ClientDto]</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth2.get_o_auth2providers()

```
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

## Duplicate Pages
<details><summary><code>client.duplicate_pages.<a href="src/fern/duplicate_pages/client.py#L33-L80">get_known_page_hashes</a>(...) -> PagePageHashKnownDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.duplicate_pages.get_known_page_hashes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `typing.Optional[typing.Union[GetKnownPageHashesRequestActionItem, typing.Sequence[GetKnownPageHashesRequestActionItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.duplicate_pages.<a href="src/fern/duplicate_pages/client.py#L82-L125">create_or_update_known_page_hash</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.duplicate_pages import PageHashCreationDtoAction

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.duplicate_pages.create_or_update_known_page_hash(
    action=PageHashCreationDtoAction.DELETE_AUTO,
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

**action:** `PageHashCreationDtoAction` 
    
</dd>
</dl>

<dl>
<dd>

**hash:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.duplicate_pages.<a href="src/fern/duplicate_pages/client.py#L127-L169">get_unknown_page_hashes</a>(...) -> PagePageHashUnknownDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.duplicate_pages.get_unknown_page_hashes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.duplicate_pages.<a href="src/fern/duplicate_pages/client.py#L171-L209">get_unknown_page_hash_thumbnail</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.duplicate_pages.get_unknown_page_hash_thumbnail(
    page_hash="pageHash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_hash:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resize:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.duplicate_pages.<a href="src/fern/duplicate_pages/client.py#L211-L258">get_page_hash_matches</a>(...) -> PagePageHashMatchDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.duplicate_pages.get_page_hash_matches(
    page_hash="pageHash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_hash:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.duplicate_pages.<a href="src/fern/duplicate_pages/client.py#L260-L289">delete_duplicate_pages_by_page_hash</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.duplicate_pages.delete_duplicate_pages_by_page_hash(
    page_hash="pageHash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_hash:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.duplicate_pages.<a href="src/fern/duplicate_pages/client.py#L291-L356">delete_single_match_by_page_hash</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.duplicate_pages.delete_single_match_by_page_hash(
    page_hash="pageHash",
    book_id="bookId",
    file_name="fileName",
    file_size=1000000,
    media_type="mediaType",
    page_number=1,
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_hash:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PageHashMatchDto` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.duplicate_pages.<a href="src/fern/duplicate_pages/client.py#L358-L388">get_known_page_hash_thumbnail</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.duplicate_pages.get_known_page_hash_thumbnail(
    page_hash="pageHash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_hash:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Readlists
<details><summary><code>client.readlists.<a href="src/fern/readlists/client.py#L31-L76">get_read_lists</a>(...) -> PageReadListDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.readlists.get_read_lists()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.readlists.<a href="src/fern/readlists/client.py#L78-L125">create_read_list</a>(...) -> ReadListDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.readlists.create_read_list(
    book_ids=[
        "bookIds"
    ],
    name="name",
    ordered=True,
    summary="summary",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**book_ids:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**ordered:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**summary:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.readlists.<a href="src/fern/readlists/client.py#L127-L153">get_read_list_by_id</a>(...) -> ReadListDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.readlists.get_read_list_by_id(
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

<details><summary><code>client.readlists.<a href="src/fern/readlists/client.py#L155-L182">delete_read_list_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.readlists.delete_read_list_by_id(
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

<details><summary><code>client.readlists.<a href="src/fern/readlists/client.py#L184-L230">update_read_list_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.readlists.update_read_list_by_id(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**book_ids:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ordered:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**summary:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.readlists.<a href="src/fern/readlists/client.py#L232-L264">download_read_list_as_zip</a>(...) -> StreamingResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download the whole readlist as a ZIP file.

Required role: **FILE_DOWNLOAD**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.readlists.download_read_list_as_zip(
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

## ComicRack
<details><summary><code>client.comic_rack.<a href="src/fern/comic_rack/client.py#L30-L59">match_comic_rack_list</a>(...) -> ReadListRequestMatchDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.comic_rack.match_comic_rack_list(
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Readlist Books
<details><summary><code>client.readlist_books.<a href="src/fern/readlist_books/client.py#L29-L110">get_books_by_read_list_id</a>(...) -> PageBookDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.readlist_books.get_books_by_read_list_id(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**read_status:** `typing.Optional[typing.Union[GetBooksByReadListIdRequestReadStatusItem, typing.Sequence[GetBooksByReadListIdRequestReadStatusItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**media_status:** `typing.Optional[typing.Union[GetBooksByReadListIdRequestMediaStatusItem, typing.Sequence[GetBooksByReadListIdRequestMediaStatusItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**author:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Author criteria in the format: name,role. Multiple author criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.readlist_books.<a href="src/fern/readlist_books/client.py#L112-L143">get_book_sibling_next_in_read_list</a>(...) -> BookDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.readlist_books.get_book_sibling_next_in_read_list(
    id="id",
    book_id="bookId",
)

```
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

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.readlist_books.<a href="src/fern/readlist_books/client.py#L145-L178">get_book_sibling_previous_in_read_list</a>(...) -> BookDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.readlist_books.get_book_sibling_previous_in_read_list(
    id="id",
    book_id="bookId",
)

```
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

**book_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Mihon
<details><summary><code>client.mihon.<a href="src/fern/mihon/client.py#L30-L60">get_mihon_read_progress_by_read_list_id</a>(...) -> TachiyomiReadProgressDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mihon specific, due to how read progress is handled in Mihon.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.mihon.get_mihon_read_progress_by_read_list_id(
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

<details><summary><code>client.mihon.<a href="src/fern/mihon/client.py#L62-L96">update_mihon_read_progress_by_read_list_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mihon specific, due to how read progress is handled in Mihon.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.mihon.update_mihon_read_progress_by_read_list_id(
    id="id",
    last_book_read=1,
)

```
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

**last_book_read:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mihon.<a href="src/fern/mihon/client.py#L98-L128">get_mihon_read_progress_by_series_id</a>(...) -> TachiyomiReadProgressV2Dto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mihon specific, due to how read progress is handled in Mihon.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.mihon.get_mihon_read_progress_by_series_id(
    series_id="seriesId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**series_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mihon.<a href="src/fern/mihon/client.py#L130-L168">update_mihon_read_progress_by_series_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mihon specific, due to how read progress is handled in Mihon.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.mihon.update_mihon_read_progress_by_series_id(
    series_id="seriesId",
    last_book_number_sort_read=1.1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**series_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**last_book_number_sort_read:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Readlist Poster
<details><summary><code>client.readlist_poster.<a href="src/fern/readlist_poster/client.py#L30-L58">get_read_list_thumbnail</a>(...) -> typing.Iterator[bytes]</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.readlist_poster.get_read_list_thumbnail(
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

<details><summary><code>client.readlist_poster.<a href="src/fern/readlist_poster/client.py#L60-L88">get_read_list_thumbnails</a>(...) -> typing.List[ThumbnailReadListDto]</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.readlist_poster.get_read_list_thumbnails(
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

<details><summary><code>client.readlist_poster.<a href="src/fern/readlist_poster/client.py#L90-L132">add_user_uploaded_read_list_thumbnail</a>(...) -> ThumbnailReadListDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.readlist_poster.add_user_uploaded_read_list_thumbnail(
    id="id",
    file="example_file",
)

```
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

**file:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**selected:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.readlist_poster.<a href="src/fern/readlist_poster/client.py#L134-L165">get_read_list_thumbnail_by_id</a>(...) -> typing.Iterator[bytes]</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.readlist_poster.get_read_list_thumbnail_by_id(
    id="id",
    thumbnail_id="thumbnailId",
)

```
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

**thumbnail_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.readlist_poster.<a href="src/fern/readlist_poster/client.py#L167-L201">delete_user_uploaded_read_list_thumbnail</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.readlist_poster.delete_user_uploaded_read_list_thumbnail(
    id="id",
    thumbnail_id="thumbnailId",
)

```
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

**thumbnail_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.readlist_poster.<a href="src/fern/readlist_poster/client.py#L203-L237">mark_read_list_thumbnail_selected</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.readlist_poster.mark_read_list_thumbnail_selected(
    id="id",
    thumbnail_id="thumbnailId",
)

```
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

**thumbnail_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Releases
<details><summary><code>client.releases.<a href="src/fern/releases/client.py#L26-L50">get_releases</a>() -> typing.List[ReleaseDto]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.releases.get_releases()

```
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

## Series
<details><summary><code>client.series.<a href="src/fern/series/client.py#L49-L174">get_series_deprecated</a>(...) -> PageSeriesDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use POST /api/v1/series/list instead. Deprecated since 1.19.0.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.series.get_series_deprecated()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[GetSeriesDeprecatedRequestStatusItem, typing.Sequence[GetSeriesDeprecatedRequestStatusItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**read_status:** `typing.Optional[typing.Union[GetSeriesDeprecatedRequestReadStatusItem, typing.Sequence[GetSeriesDeprecatedRequestReadStatusItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**publisher:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**genre:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**age_rating:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**release_year:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**sharing_label:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**complete:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**oneshot:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**search_regex:** `typing.Optional[str]` — Search by regex criteria, in the form: regex,field. Supported fields are TITLE and TITLE_SORT.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**author:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Author criteria in the format: name,role. Multiple author criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series.<a href="src/fern/series/client.py#L176-L286">get_series_alphabetical_groups_deprecated</a>(...) -> typing.List[GroupCountDto]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use POST /api/v1/series/list/alphabetical-groups instead. Deprecated since 1.19.0.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.series.get_series_alphabetical_groups_deprecated()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[GetSeriesAlphabeticalGroupsDeprecatedRequestStatusItem, typing.Sequence[GetSeriesAlphabeticalGroupsDeprecatedRequestStatusItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**read_status:** `typing.Optional[typing.Union[GetSeriesAlphabeticalGroupsDeprecatedRequestReadStatusItem, typing.Sequence[GetSeriesAlphabeticalGroupsDeprecatedRequestReadStatusItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**publisher:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**genre:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**age_rating:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**release_year:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**sharing_label:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**complete:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**oneshot:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**search_regex:** `typing.Optional[str]` — Search by regex criteria, in the form: regex,field. Supported fields are TITLE and TITLE_SORT.
    
</dd>
</dl>

<dl>
<dd>

**author:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Author criteria in the format: name,role. Multiple author criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series.<a href="src/fern/series/client.py#L288-L344">get_series_latest</a>(...) -> PageSeriesDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return recently added or updated series.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.series.get_series_latest()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**oneshot:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series.<a href="src/fern/series/client.py#L346-L401">get_series</a>(...) -> PageSeriesDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.series.get_series()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `SeriesSearch` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series.<a href="src/fern/series/client.py#L403-L439">get_series_alphabetical_groups</a>(...) -> typing.List[GroupCountDto]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List series grouped by the first character of their sort title.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.series.get_series_alphabetical_groups()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `SeriesSearch` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series.<a href="src/fern/series/client.py#L441-L497">get_series_new</a>(...) -> PageSeriesDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return newly added series.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.series.get_series_new()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**oneshot:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series.<a href="src/fern/series/client.py#L499-L555">get_series_updated</a>(...) -> PageSeriesDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return recently updated series, but not newly added ones.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.series.get_series_updated()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**oneshot:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series.<a href="src/fern/series/client.py#L557-L583">get_series_by_id</a>(...) -> SeriesDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.series.get_series_by_id(
    series_id="seriesId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**series_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series.<a href="src/fern/series/client.py#L585-L612">analyze</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.series.analyze(
    series_id="seriesId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**series_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series.<a href="src/fern/series/client.py#L614-L698">get_books_by_series_id</a>(...) -> PageBookDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use POST /api/v1/books/list instead. Deprecated since 1.19.0.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.series.get_books_by_series_id(
    series_id="seriesId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**series_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**media_status:** `typing.Optional[typing.Union[GetBooksBySeriesIdRequestMediaStatusItem, typing.Sequence[GetBooksBySeriesIdRequestMediaStatusItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**read_status:** `typing.Optional[typing.Union[GetBooksBySeriesIdRequestReadStatusItem, typing.Sequence[GetBooksBySeriesIdRequestReadStatusItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**author:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Author criteria in the format: name,role. Multiple author criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series.<a href="src/fern/series/client.py#L700-L728">get_collections_by_series_id</a>(...) -> typing.List[CollectionDto]</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.series.get_collections_by_series_id(
    series_id="seriesId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**series_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series.<a href="src/fern/series/client.py#L730-L762">download_series_as_zip</a>(...) -> StreamingResponseBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download the whole series as a ZIP file.

Required role: **FILE_DOWNLOAD**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.series.download_series_as_zip(
    series_id="seriesId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**series_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series.<a href="src/fern/series/client.py#L764-L793">delete_series_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete all of the series' books files on disk.

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.series.delete_series_file(
    series_id="seriesId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**series_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series.<a href="src/fern/series/client.py#L795-L942">update_series_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.series.update_series_metadata(
    series_id="seriesId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**series_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**age_rating:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**age_rating_lock:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**alternate_titles:** `typing.Optional[typing.List[AlternateTitleUpdateDto]]` 
    
</dd>
</dl>

<dl>
<dd>

**alternate_titles_lock:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**genres:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**genres_lock:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**language_lock:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**links:** `typing.Optional[typing.List[WebLinkUpdateDto]]` 
    
</dd>
</dl>

<dl>
<dd>

**links_lock:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**publisher:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**publisher_lock:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**reading_direction:** `typing.Optional[SeriesMetadataUpdateDtoReadingDirection]` 
    
</dd>
</dl>

<dl>
<dd>

**reading_direction_lock:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**sharing_labels:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**sharing_labels_lock:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[SeriesMetadataUpdateDtoStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**status_lock:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**summary:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**summary_lock:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**tags_lock:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title_lock:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sort:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title_sort_lock:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**total_book_count:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**total_book_count_lock:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series.<a href="src/fern/series/client.py#L944-L971">refresh_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.series.refresh_metadata(
    series_id="seriesId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**series_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series.<a href="src/fern/series/client.py#L973-L1000">mark_series_as_read</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mark all book for series as read
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.series.mark_series_as_read(
    series_id="seriesId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**series_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series.<a href="src/fern/series/client.py#L1002-L1029">mark_series_as_unread</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mark all book for series as unread
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.series.mark_series_as_unread(
    series_id="seriesId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**series_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Series Poster
<details><summary><code>client.series_poster.<a href="src/fern/series_poster/client.py#L30-L58">get_series_thumbnail</a>(...) -> typing.Iterator[bytes]</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.series_poster.get_series_thumbnail(
    series_id="seriesId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**series_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series_poster.<a href="src/fern/series_poster/client.py#L60-L88">get_series_thumbnails</a>(...) -> typing.List[ThumbnailSeriesDto]</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.series_poster.get_series_thumbnails(
    series_id="seriesId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**series_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series_poster.<a href="src/fern/series_poster/client.py#L90-L132">add_user_uploaded_series_thumbnail</a>(...) -> ThumbnailSeriesDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.series_poster.add_user_uploaded_series_thumbnail(
    series_id="seriesId",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**series_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**selected:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series_poster.<a href="src/fern/series_poster/client.py#L134-L165">get_series_thumbnail_by_id</a>(...) -> typing.Iterator[bytes]</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.series_poster.get_series_thumbnail_by_id(
    series_id="seriesId",
    thumbnail_id="thumbnailId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**series_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**thumbnail_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series_poster.<a href="src/fern/series_poster/client.py#L167-L201">delete_user_uploaded_series_thumbnail</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.series_poster.delete_user_uploaded_series_thumbnail(
    series_id="seriesId",
    thumbnail_id="thumbnailId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**series_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**thumbnail_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series_poster.<a href="src/fern/series_poster/client.py#L203-L237">mark_series_thumbnail_selected</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.series_poster.mark_series_thumbnail_selected(
    series_id="seriesId",
    thumbnail_id="thumbnailId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**series_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**thumbnail_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Server settings
<details><summary><code>client.server_settings.<a href="src/fern/server_settings/client.py#L30-L54">get_server_settings</a>() -> SettingsDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.server_settings.get_server_settings()

```
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

<details><summary><code>client.server_settings.<a href="src/fern/server_settings/client.py#L56-L132">update_server_settings</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can omit fields you don't want to update

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.server_settings.update_server_settings()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**delete_empty_collections:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**delete_empty_read_lists:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**kepubify_path:** `typing.Optional[str]` — Will be removed in a future version
    
</dd>
</dl>

<dl>
<dd>

**kobo_port:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**kobo_proxy:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**remember_me_duration_days:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**renew_remember_me_key:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**server_context_path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**server_port:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**task_pool_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**thumbnail_size:** `typing.Optional[SettingsUpdateDtoThumbnailSize]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sync points
<details><summary><code>client.sync_points.<a href="src/fern/sync_points/client.py#L25-L55">delete_sync_points_for_current_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

If an API Key ID is passed, deletes only the sync points associated with that API Key. Deleting sync points will allow a Kobo to sync from scratch upon the next sync.
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.sync_points.delete_sync_points_for_current_user()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tasks
<details><summary><code>client.tasks.<a href="src/fern/tasks/client.py#L25-L51">empty_task_queue</a>() -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel all tasks queued

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.tasks.empty_task_queue()

```
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

## Referential metadata
<details><summary><code>client.referential_metadata.<a href="src/fern/referential_metadata/client.py#L29-L81">get_age_ratings</a>(...) -> PageInteger</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Can be filtered by various criteria
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.referential_metadata.get_age_ratings()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.referential_metadata.<a href="src/fern/referential_metadata/client.py#L83-L151">get_authors</a>(...) -> PageAuthorDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Can be filtered by various criteria
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.referential_metadata.get_authors()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**series_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**readlist_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.referential_metadata.<a href="src/fern/referential_metadata/client.py#L153-L221">get_authors_names</a>(...) -> PageString</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Can be filtered by various criteria
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.referential_metadata.get_authors_names()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**series_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**readlist_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.referential_metadata.<a href="src/fern/referential_metadata/client.py#L223-L283">get_authors_roles</a>(...) -> PageString</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Can be filtered by various criteria
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.referential_metadata.get_authors_roles()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**series_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**readlist_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.referential_metadata.<a href="src/fern/referential_metadata/client.py#L285-L341">get_genres</a>(...) -> PageString</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Can be filtered by various criteria
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.referential_metadata.get_genres()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.referential_metadata.<a href="src/fern/referential_metadata/client.py#L343-L399">get_languages</a>(...) -> PageString</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Can be filtered by various criteria
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.referential_metadata.get_languages()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.referential_metadata.<a href="src/fern/referential_metadata/client.py#L401-L457">get_publishers</a>(...) -> PageString</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Can be filtered by various criteria
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.referential_metadata.get_publishers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.referential_metadata.<a href="src/fern/referential_metadata/client.py#L459-L511">get_series_release_years</a>(...) -> PageString</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Can be filtered by various criteria
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.referential_metadata.get_series_release_years()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.referential_metadata.<a href="src/fern/referential_metadata/client.py#L513-L569">get_sharing_labels</a>(...) -> PageString</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Can be filtered by various criteria
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.referential_metadata.get_sharing_labels()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.referential_metadata.<a href="src/fern/referential_metadata/client.py#L571-L639">get_tags</a>(...) -> PageString</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Can be filtered by various criteria
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.referential_metadata.get_tags()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**library_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**series_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**readlist_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[GetTagsRequestInclude]` 
    
</dd>
</dl>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.users.<a href="src/fern/users/client.py#L33-L57">get_users</a>() -> typing.List[UserDto]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.get_users()

```
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

<details><summary><code>client.users.<a href="src/fern/users/client.py#L59-L121">add_user</a>(...) -> UserDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.add_user(
    email="email",
    password="password",
    roles=[
        "roles"
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

**email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**age_restriction:** `typing.Optional[AgeRestrictionUpdateDto]` 
    
</dd>
</dl>

<dl>
<dd>

**labels_allow:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**labels_exclude:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**shared_libraries:** `typing.Optional[SharedLibrariesUpdateDto]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py#L123-L168">get_authentication_activity</a>(...) -> PageAuthenticationActivityDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.get_authentication_activity()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py#L170-L197">delete_user_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.delete_user_by_id(
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

<details><summary><code>client.users.<a href="src/fern/users/client.py#L199-L254">update_user_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.update_user_by_id(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**age_restriction:** `typing.Optional[AgeRestrictionUpdateDto]` 
    
</dd>
</dl>

<dl>
<dd>

**labels_allow:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**labels_exclude:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**shared_libraries:** `typing.Optional[SharedLibrariesUpdateDto]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py#L256-L294">get_latest_authentication_activity_by_user_id</a>(...) -> AuthenticationActivityDto</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.get_latest_authentication_activity_by_user_id(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**apikey_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py#L296-L328">update_password_by_user_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Required role: **ADMIN**
</dd>
</dl>
</dd>
</dl>

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
    environment=FernApiEnvironment.DEFAULT,
)

client.users.update_password_by_user_id(
    id="id",
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PasswordUpdateDto` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Current user
<details><summary><code>client.current_user.<a href="src/fern/current_user/client.py#L30-L56">get_current_user</a>(...) -> UserDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.current_user.get_current_user()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**remember_me:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.current_user.<a href="src/fern/current_user/client.py#L58-L101">get_authentication_activity_for_current_user</a>(...) -> PageAuthenticationActivityDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.current_user.get_authentication_activity_for_current_user()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**unpaged:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index (0..N)
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to be returned
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.current_user.<a href="src/fern/current_user/client.py#L103-L132">update_password_for_current_user</a>(...)</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.current_user.update_password_for_current_user(
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

**request:** `PasswordUpdateDto` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py#L29-L53">get_api_keys_for_current_user</a>() -> typing.List[ApiKeyDto]</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.get_api_keys_for_current_user()

```
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

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py#L55-L83">create_api_key_for_current_user</a>(...) -> ApiKeyDto</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.create_api_key_for_current_user(
    comment="comment",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**comment:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py#L85-L110">delete_api_key_by_key_id</a>(...)</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.delete_api_key_by_key_id(
    key_id="keyId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

