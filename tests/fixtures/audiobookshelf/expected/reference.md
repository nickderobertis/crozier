# Reference
## Authors
<details><summary><code>client.authors.<a href="src/fern/authors/client.py">get_author_by_id</a>(...) -> Author</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an author by ID. The author's books and series can be included in the response.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authors.get_author_by_id(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
    include="items,series",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `AuthorId` — Author ID
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[str]` — A comma separated list of what to include with the author. The options are `items` and `series`. `series` will only have an effect if `items` is included. For example, the value `items,series` will include both library items and series.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.authors.<a href="src/fern/authors/client.py">delete_author_by_id</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an author by ID. This will remove the author from all books.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authors.delete_author_by_id(
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

**id:** `AuthorId` — Author ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.authors.<a href="src/fern/authors/client.py">update_author_by_id</a>(...) -> UpdateAuthorByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an author by ID. The author's name and description can be updated. This endpoint will merge two authors if the new author name matches another author name in the database.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authors.update_author_by_id(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `AuthorId` — Author ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[AuthorName]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[AuthorDescription]` 
    
</dd>
</dl>

<dl>
<dd>

**image_path:** `typing.Optional[AuthorImagePath]` 
    
</dd>
</dl>

<dl>
<dd>

**asin:** `typing.Optional[AuthorAsin]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.authors.<a href="src/fern/authors/client.py">get_author_image_by_id</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an author image by author ID. The image will be returned in the requested format and size.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authors.get_author_image_by_id(
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

**id:** `AuthorId` — Author ID
    
</dd>
</dl>

<dl>
<dd>

**token:** `typing.Optional[str]` — API token
    
</dd>
</dl>

<dl>
<dd>

**ts:** `typing.Optional[int]` — Updated at value
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.authors.<a href="src/fern/authors/client.py">add_author_image_by_id</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add an author image to the server. The image will be downloaded from the provided URL and stored on the server.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authors.add_author_image_by_id(
    id="id",
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

**id:** `AuthorId` — Author ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `ImageUrl` 
    
</dd>
</dl>

<dl>
<dd>

**token:** `typing.Optional[str]` — API token
    
</dd>
</dl>

<dl>
<dd>

**ts:** `typing.Optional[int]` — Updated at value
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.authors.<a href="src/fern/authors/client.py">delete_author_image_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an author image by author ID. This will remove the image from the server and the database.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authors.delete_author_image_by_id(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `AuthorId` — Author ID
    
</dd>
</dl>

<dl>
<dd>

**token:** `typing.Optional[str]` — API token
    
</dd>
</dl>

<dl>
<dd>

**ts:** `typing.Optional[int]` — Updated at value
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.authors.<a href="src/fern/authors/client.py">update_author_image_by_id</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an author image by author ID. The image will be resized if the width, height, or format is provided.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authors.update_author_image_by_id(
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

**id:** `AuthorId` — Author ID
    
</dd>
</dl>

<dl>
<dd>

**token:** `typing.Optional[str]` — API token
    
</dd>
</dl>

<dl>
<dd>

**ts:** `typing.Optional[int]` — Updated at value
    
</dd>
</dl>

<dl>
<dd>

**width:** `typing.Optional[ImageWidth]` 
    
</dd>
</dl>

<dl>
<dd>

**height:** `typing.Optional[ImageHeight]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[ImageFormat]` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[ImageRaw]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.authors.<a href="src/fern/authors/client.py">match_author_by_id</a>(...) -> MatchAuthorByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Match the author against Audible using quick match. Quick match updates the author's description and image (if no image already existed) with information from audible. Either `asin` or `q` must be provided, with `asin` taking priority if both are provided.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.authors.match_author_by_id(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `AuthorId` — Author ID
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[AuthorSearchName]` 
    
</dd>
</dl>

<dl>
<dd>

**asin:** `typing.Optional[AuthorAsin]` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[Region]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Email
<details><summary><code>client.email.<a href="src/fern/email/client.py">get_email_settings</a>() -> EmailSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get email settings for sending e-books to e-readers.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.email.get_email_settings()

```
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

<details><summary><code>client.email.<a href="src/fern/email/client.py">update_email_settings</a>(...) -> EmailSettings</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, EreaderDeviceObject, EreaderDeviceObjectAvailabilityOption
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.email.update_email_settings(
    id="email-settings",
    port=465,
    secure=True,
    ereader_devices=[
        EreaderDeviceObject(
            name="name",
            email="email",
            availability_option=EreaderDeviceObjectAvailabilityOption.ADMIN_OR_UP,
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

**request:** `EmailSettings` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.email.<a href="src/fern/email/client.py">send_test_email</a>()</code></summary>
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

client.email.send_test_email()

```
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

<details><summary><code>client.email.<a href="src/fern/email/client.py">update_e_reader_devices</a>(...) -> UpdateEReaderDevicesResponse</code></summary>
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

client.email.update_e_reader_devices()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ereader_devices:** `typing.Optional[typing.List[EreaderDeviceObject]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.email.<a href="src/fern/email/client.py">send_e_book_to_device</a>(...)</code></summary>
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

client.email.send_e_book_to_device()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**library_item_id:** `typing.Optional[LibraryItemId]` 
    
</dd>
</dl>

<dl>
<dd>

**device_name:** `typing.Optional[EreaderName]` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.libraries.<a href="src/fern/libraries/client.py">get_libraries</a>() -> GetLibrariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all libraries on server.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
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

<details><summary><code>client.libraries.<a href="src/fern/libraries/client.py">create_library</a>(...) -> Library</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new library on server.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Folder
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.libraries.create_library(
    name="My Audiobooks",
    folders=[
        Folder()
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

**name:** `LibraryName` 
    
</dd>
</dl>

<dl>
<dd>

**folders:** `LibraryFolders` 
    
</dd>
</dl>

<dl>
<dd>

**display_order:** `typing.Optional[LibraryDisplayOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**icon:** `typing.Optional[LibraryIcon]` 
    
</dd>
</dl>

<dl>
<dd>

**media_type:** `typing.Optional[LibraryMediaType]` 
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[LibraryProvider]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[LibrarySettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.libraries.<a href="src/fern/libraries/client.py">get_library_by_id</a>(...) -> Library</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single library by ID on server.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.libraries.get_library_by_id(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
    minified=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `LibraryId` — The ID of the library.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**minified:** `typing.Optional[int]` — Return minified items if true
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.libraries.<a href="src/fern/libraries/client.py">delete_library_by_id</a>(...) -> Library</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a single library by ID on server and return the deleted object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.libraries.delete_library_by_id(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `LibraryId` — The ID of the library.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.libraries.<a href="src/fern/libraries/client.py">update_library_by_id</a>(...) -> Library</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a single library by ID on server.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.libraries.update_library_by_id(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `LibraryId` — The ID of the library.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[LibraryName]` 
    
</dd>
</dl>

<dl>
<dd>

**folders:** `typing.Optional[LibraryFolders]` 
    
</dd>
</dl>

<dl>
<dd>

**display_order:** `typing.Optional[LibraryDisplayOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**icon:** `typing.Optional[LibraryIcon]` 
    
</dd>
</dl>

<dl>
<dd>

**media_type:** `typing.Optional[LibraryMediaType]` 
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[LibraryProvider]` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[LibrarySettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.libraries.<a href="src/fern/libraries/client.py">get_library_authors</a>(...) -> GetLibraryAuthorsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all authors in a library by ID on server.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.libraries.get_library_authors(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `LibraryId` — The ID of the library.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.libraries.<a href="src/fern/libraries/client.py">get_library_items</a>(...) -> GetLibraryItemsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get items in a library by ID on server.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.libraries.get_library_items(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
    sort="numBooks",
    filter="media.metadata.title",
    include="rssfeed",
    minified=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `LibraryId` — The ID of the library.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items to return. This the size of a single page for the optional `page` query.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number (zero indexed) to return. If no limit is specified, then page will have no effect.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — The field to sort by from the request.
    
</dd>
</dl>

<dl>
<dd>

**desc:** `typing.Optional[int]` — Return items in reversed order if true.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — The filter for the library.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[str]` — The fields to include in the response. The only current option is `rssfeed`.
    
</dd>
</dl>

<dl>
<dd>

**minified:** `typing.Optional[int]` — Return minified items if true
    
</dd>
</dl>

<dl>
<dd>

**collapse_series:** `typing.Optional[int]` — Whether to collapse series into a single cover
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.libraries.<a href="src/fern/libraries/client.py">delete_library_issues</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete all items with issues in a library by library ID on the server. This only removes the items from the ABS database and does not delete media files.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.libraries.delete_library_issues(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `LibraryId` — The ID of the library.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.libraries.<a href="src/fern/libraries/client.py">get_library_series</a>(...) -> GetLibrarySeriesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get series in a library. Filtering and sorting can be applied.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.libraries.get_library_series(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
    filter="media.metadata.title",
    include="rssfeed",
    minified=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `LibraryId` — The ID of the library.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items to return. This the size of a single page for the optional `page` query.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number (zero indexed) to return. If no limit is specified, then page will have no effect.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetLibrarySeriesRequestSort]` — The field to sort by from the request.
    
</dd>
</dl>

<dl>
<dd>

**desc:** `typing.Optional[int]` — Return items in reversed order if true.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — The filter for the library.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[str]` — The fields to include in the response. The only current option is `rssfeed`.
    
</dd>
</dl>

<dl>
<dd>

**minified:** `typing.Optional[int]` — Return minified items if true
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.libraries.<a href="src/fern/libraries/client.py">get_library_series_by_id</a>(...) -> SeriesWithProgressAndRss</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single series in a library by ID on server. This endpoint is deprecated and `/api/series/{id}` should be used instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.libraries.get_library_series_by_id(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
    series_id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
    filter="media.metadata.title",
    minified=1,
    include="rssfeed",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `LibraryId` — The ID of the library.
    
</dd>
</dl>

<dl>
<dd>

**series_id:** `SeriesId` — The ID of the series.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items to return. This the size of a single page for the optional `page` query.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number (zero indexed) to return. If no limit is specified, then page will have no effect.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetLibrarySeriesByIdRequestSort]` — The field to sort by from the request.
    
</dd>
</dl>

<dl>
<dd>

**desc:** `typing.Optional[int]` — Return items in reversed order if true.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — The filter for the library.
    
</dd>
</dl>

<dl>
<dd>

**minified:** `typing.Optional[int]` — Return minified items if true
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[str]` — The fields to include in the response. The only current option is `rssfeed`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Notification
<details><summary><code>client.notification.<a href="src/fern/notification/client.py">get_notifications</a>() -> GetNotificationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all Apprise notification events and notification settings for server.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.notification.get_notifications()

```
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

<details><summary><code>client.notification.<a href="src/fern/notification/client.py">create_notification</a>(...) -> CreateNotificationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update Notification settings.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, NotificationEventName
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.notification.create_notification(
    event_name=NotificationEventName.ON_PODCAST_EPISODE_DOWNLOADED,
    urls=[
        "urls"
    ],
    title_template="New {{podcastTitle}} Episode!",
    body_template="{{episodeTitle}} has been added to {{libraryName}} library.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event_name:** `NotificationEventName` 
    
</dd>
</dl>

<dl>
<dd>

**urls:** `Urls` 
    
</dd>
</dl>

<dl>
<dd>

**title_template:** `TitleTemplate` 
    
</dd>
</dl>

<dl>
<dd>

**body_template:** `BodyTemplate` 
    
</dd>
</dl>

<dl>
<dd>

**library_id:** `typing.Optional[LibraryIdNullable]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[Enabled]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[NotificationType]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notification.<a href="src/fern/notification/client.py">configure_notification_settings</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the URL, max failed attempts, and maximum notifications that can be queued for Apprise.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.notification.configure_notification_settings()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**apprise_api_url:** `typing.Optional[AppriseApiUrl]` 
    
</dd>
</dl>

<dl>
<dd>

**max_failed_attempts:** `typing.Optional[MaxFailedAttempts]` 
    
</dd>
</dl>

<dl>
<dd>

**max_notification_queue:** `typing.Optional[MaxNotificationQueue]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notification.<a href="src/fern/notification/client.py">get_notification_event_data</a>() -> GetNotificationEventDataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all Apprise notification event data for the server.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.notification.get_notification_event_data()

```
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

<details><summary><code>client.notification.<a href="src/fern/notification/client.py">send_default_test_notification</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a test notification.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.notification.send_default_test_notification()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fail:** `typing.Optional[int]` — Whether to intentionally cause the notification to fail. `0` for false, `1` for true.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notification.<a href="src/fern/notification/client.py">delete_notification</a>(...) -> DeleteNotificationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the notification by ID and return the notification settings.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.notification.delete_notification(
    id="notification-settings",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `NotificationId` — The ID of the notification.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notification.<a href="src/fern/notification/client.py">update_notification</a>(...) -> UpdateNotificationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an individual Notification by ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.notification.update_notification(
    id="notification-settings",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `NotificationId` — The ID of the notification.
    
</dd>
</dl>

<dl>
<dd>

**library_id:** `typing.Optional[LibraryId]` 
    
</dd>
</dl>

<dl>
<dd>

**event_name:** `typing.Optional[NotificationEventName]` 
    
</dd>
</dl>

<dl>
<dd>

**urls:** `typing.Optional[Urls]` 
    
</dd>
</dl>

<dl>
<dd>

**title_template:** `typing.Optional[TitleTemplate]` 
    
</dd>
</dl>

<dl>
<dd>

**body_template:** `typing.Optional[BodyTemplate]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[Enabled]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[NotificationType]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notification.<a href="src/fern/notification/client.py">send_test_notification</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a test to the given notification by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.notification.send_test_notification(
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

**id:** `NotificationId` — The ID of the notification.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Podcasts
<details><summary><code>client.podcasts.<a href="src/fern/podcasts/client.py">create_podcast</a>(...) -> Podcast</code></summary>
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

client.podcasts.create_podcast()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Podcast` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.podcasts.<a href="src/fern/podcasts/client.py">get_podcast_feed</a>(...) -> GetPodcastFeedResponse</code></summary>
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

client.podcasts.get_podcast_feed()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rss_feed:** `typing.Optional[str]` — The RSS feed URL of the podcast
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.podcasts.<a href="src/fern/podcasts/client.py">get_feeds_from_opml_text</a>(...) -> GetFeedsFromOpmlTextResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Parse OPML text and return an array of feeds
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.podcasts.get_feeds_from_opml_text()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**opml_text:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.podcasts.<a href="src/fern/podcasts/client.py">bulk_create_podcasts_from_opml_feed_urls</a>(...)</code></summary>
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

client.podcasts.bulk_create_podcasts_from_opml_feed_urls()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**feeds:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**library_id:** `typing.Optional[LibraryId]` 
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[FolderId]` 
    
</dd>
</dl>

<dl>
<dd>

**auto_download_episodes:** `typing.Optional[AutoDownloadEpisodes]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.podcasts.<a href="src/fern/podcasts/client.py">check_new_episodes</a>(...) -> CheckNewEpisodesResponse</code></summary>
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

client.podcasts.check_new_episodes(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `PodcastId` — Podcast ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of episodes to download
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.podcasts.<a href="src/fern/podcasts/client.py">clear_episode_download_queue</a>(...)</code></summary>
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

client.podcasts.clear_episode_download_queue(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `PodcastId` — Podcast ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.podcasts.<a href="src/fern/podcasts/client.py">get_episode_downloads</a>(...) -> GetEpisodeDownloadsResponse</code></summary>
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

client.podcasts.get_episode_downloads(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `PodcastId` — Podcast ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.podcasts.<a href="src/fern/podcasts/client.py">find_episode</a>(...) -> FindEpisodeResponse</code></summary>
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

client.podcasts.find_episode(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
    title="title",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `PodcastId` — Podcast ID
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` — Title of the episode to search for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.podcasts.<a href="src/fern/podcasts/client.py">download_episodes</a>(...)</code></summary>
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

client.podcasts.download_episodes(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
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

**id:** `PodcastId` — Podcast ID
    
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

<details><summary><code>client.podcasts.<a href="src/fern/podcasts/client.py">quick_match_episodes</a>(...) -> QuickMatchEpisodesResponse</code></summary>
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

client.podcasts.quick_match_episodes(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `PodcastId` — Podcast ID
    
</dd>
</dl>

<dl>
<dd>

**override:** `typing.Optional[str]` — Override existing details if set to 1
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.podcasts.<a href="src/fern/podcasts/client.py">get_episode</a>(...) -> PodcastEpisode</code></summary>
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

client.podcasts.get_episode(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
    episode_id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `PodcastId` — Podcast ID
    
</dd>
</dl>

<dl>
<dd>

**episode_id:** `PodcastId` — Episode ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.podcasts.<a href="src/fern/podcasts/client.py">remove_episode</a>(...) -> Podcast</code></summary>
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

client.podcasts.remove_episode(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
    episode_id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `PodcastId` — Podcast ID
    
</dd>
</dl>

<dl>
<dd>

**episode_id:** `PodcastId` — Episode ID
    
</dd>
</dl>

<dl>
<dd>

**hard:** `typing.Optional[str]` — Hard delete the episode if set to 1
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.podcasts.<a href="src/fern/podcasts/client.py">update_episode</a>(...) -> Podcast</code></summary>
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

client.podcasts.update_episode(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
    episode_id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
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

**id:** `PodcastId` — Podcast ID
    
</dd>
</dl>

<dl>
<dd>

**episode_id:** `PodcastId` — Episode ID
    
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

## Series
<details><summary><code>client.series.<a href="src/fern/series/client.py">get_series</a>(...) -> SeriesWithProgressAndRss</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a series by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.series.get_series(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `SeriesId` — The ID of the series.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.series.<a href="src/fern/series/client.py">update_series</a>(...) -> Series</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a series by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.series.update_series(
    id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `SeriesId` — The ID of the series.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[SeriesName]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[SeriesDescription]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

