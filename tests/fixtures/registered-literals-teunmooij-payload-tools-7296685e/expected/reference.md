# Reference
## Pages
<details><summary><code>client.pages.<a href="src/fern/pages/client.py#L35-L100">find_paginated_pages</a>(...) -> Pagess</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Find paginated Pages
</dd>
</dl>
</dd>
</dl>

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

client.pages.find_paginated_pages()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**depth:** `typing.Optional[float]` — number of levels to automatically populate relationships and uploads
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — retrieves document(s) in a specific locale
    
</dd>
</dl>

<dl>
<dd>

**fallback_locale:** `typing.Optional[str]` — specifies a fallback locale if no locale value exists
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — sort by field
    
</dd>
</dl>

<dl>
<dd>

**where:** `typing.Optional[Where]` — pass a where query to constrain returned documents (complex type, see documentation)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — limit the returned documents to a certain number
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — get a specific page of documents
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pages.<a href="src/fern/pages/client.py#L102-L171">create_a_new_page</a>(...) -> PagesUpsertConfirmation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Page
</dd>
</dl>
</dd>
</dl>

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

client.pages.create_a_new_page(
    id="id",
    updated_at="updatedAt",
    created_at="createdAt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Pages` 
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[float]` — number of levels to automatically populate relationships and uploads
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — retrieves document(s) in a specific locale
    
</dd>
</dl>

<dl>
<dd>

**fallback_locale:** `typing.Optional[str]` — specifies a fallback locale if no locale value exists
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pages.<a href="src/fern/pages/client.py#L173-L240">delete_multiple_pages</a>(...) -> DeletePagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete all Pages matching the where query
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Where
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pages.delete_multiple_pages(
    where=Where(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**where:** `Where` — pass a where query to constrain returned documents (complex type, see documentation)
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — sort by field
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — limit the returned documents to a certain number
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — get a specific page of documents
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[float]` — number of levels to automatically populate relationships and uploads
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — retrieves document(s) in a specific locale
    
</dd>
</dl>

<dl>
<dd>

**fallback_locale:** `typing.Optional[str]` — specifies a fallback locale if no locale value exists
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pages.<a href="src/fern/pages/client.py#L242-L332">update_multiple_pages</a>(...) -> PatchPagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update all Pages matching the where query
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Where
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pages.update_multiple_pages(
    where=Where(),
    id="id",
    updated_at="updatedAt",
    created_at="createdAt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**where:** `Where` — pass a where query to constrain returned documents (complex type, see documentation)
    
</dd>
</dl>

<dl>
<dd>

**request:** `Pages` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — sort by field
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — limit the returned documents to a certain number
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — get a specific page of documents
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[float]` — number of levels to automatically populate relationships and uploads
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — retrieves document(s) in a specific locale
    
</dd>
</dl>

<dl>
<dd>

**fallback_locale:** `typing.Optional[str]` — specifies a fallback locale if no locale value exists
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pages.<a href="src/fern/pages/client.py#L334-L406">get_a_single_page_by_its_id</a>(...) -> Pages</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single Page by its id
</dd>
</dl>
</dd>
</dl>

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

client.pages.get_a_single_page_by_its_id(
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

**id:** `str` — id of the Page
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[float]` — number of levels to automatically populate relationships and uploads
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — retrieves document(s) in a specific locale
    
</dd>
</dl>

<dl>
<dd>

**fallback_locale:** `typing.Optional[str]` — specifies a fallback locale if no locale value exists
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — sort by field
    
</dd>
</dl>

<dl>
<dd>

**where:** `typing.Optional[Where]` — pass a where query to constrain returned documents (complex type, see documentation)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — limit the returned documents to a certain number
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — get a specific page of documents
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pages.<a href="src/fern/pages/client.py#L408-L456">deletes_an_existing_page</a>(...) -> PagesUpsertConfirmation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing Page
</dd>
</dl>
</dd>
</dl>

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

client.pages.deletes_an_existing_page(
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

**id:** `str` — id of the Page
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[float]` — number of levels to automatically populate relationships and uploads
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — retrieves document(s) in a specific locale
    
</dd>
</dl>

<dl>
<dd>

**fallback_locale:** `typing.Optional[str]` — specifies a fallback locale if no locale value exists
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pages.<a href="src/fern/pages/client.py#L458-L533">updates_a_page</a>(...) -> PagesUpsertConfirmation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a Page
</dd>
</dl>
</dd>
</dl>

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

client.pages.updates_a_page(
    id_="id",
    id="id",
    updated_at="updatedAt",
    created_at="createdAt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — id of the Page
    
</dd>
</dl>

<dl>
<dd>

**request:** `Pages` 
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[float]` — number of levels to automatically populate relationships and uploads
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — retrieves document(s) in a specific locale
    
</dd>
</dl>

<dl>
<dd>

**fallback_locale:** `typing.Optional[str]` — specifies a fallback locale if no locale value exists
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.users.<a href="src/fern/users/client.py#L34-L99">find_paginated_users</a>(...) -> Userss</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Find paginated Users
</dd>
</dl>
</dd>
</dl>

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

client.users.find_paginated_users()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**depth:** `typing.Optional[float]` — number of levels to automatically populate relationships and uploads
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — retrieves document(s) in a specific locale
    
</dd>
</dl>

<dl>
<dd>

**fallback_locale:** `typing.Optional[str]` — specifies a fallback locale if no locale value exists
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — sort by field
    
</dd>
</dl>

<dl>
<dd>

**where:** `typing.Optional[Where]` — pass a where query to constrain returned documents (complex type, see documentation)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — limit the returned documents to a certain number
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — get a specific page of documents
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py#L101-L194">create_a_new_user</a>(...) -> UsersUpsertConfirmation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new User
</dd>
</dl>
</dd>
</dl>

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

client.users.create_a_new_user(
    id="id",
    updated_at="updatedAt",
    created_at="createdAt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Users` 
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[float]` — number of levels to automatically populate relationships and uploads
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — retrieves document(s) in a specific locale
    
</dd>
</dl>

<dl>
<dd>

**fallback_locale:** `typing.Optional[str]` — specifies a fallback locale if no locale value exists
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py#L196-L263">delete_multiple_users</a>(...) -> DeleteUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete all Users matching the where query
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Where
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.users.delete_multiple_users(
    where=Where(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**where:** `Where` — pass a where query to constrain returned documents (complex type, see documentation)
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — sort by field
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — limit the returned documents to a certain number
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — get a specific page of documents
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[float]` — number of levels to automatically populate relationships and uploads
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — retrieves document(s) in a specific locale
    
</dd>
</dl>

<dl>
<dd>

**fallback_locale:** `typing.Optional[str]` — specifies a fallback locale if no locale value exists
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py#L265-L379">update_multiple_users</a>(...) -> PatchUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update all Users matching the where query
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Where
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.users.update_multiple_users(
    where=Where(),
    id="id",
    updated_at="updatedAt",
    created_at="createdAt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**where:** `Where` — pass a where query to constrain returned documents (complex type, see documentation)
    
</dd>
</dl>

<dl>
<dd>

**request:** `Users` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — sort by field
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — limit the returned documents to a certain number
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — get a specific page of documents
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[float]` — number of levels to automatically populate relationships and uploads
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — retrieves document(s) in a specific locale
    
</dd>
</dl>

<dl>
<dd>

**fallback_locale:** `typing.Optional[str]` — specifies a fallback locale if no locale value exists
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py#L381-L453">get_a_single_user_by_its_id</a>(...) -> Users</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single User by its id
</dd>
</dl>
</dd>
</dl>

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

client.users.get_a_single_user_by_its_id(
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

**id:** `str` — id of the User
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[float]` — number of levels to automatically populate relationships and uploads
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — retrieves document(s) in a specific locale
    
</dd>
</dl>

<dl>
<dd>

**fallback_locale:** `typing.Optional[str]` — specifies a fallback locale if no locale value exists
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — sort by field
    
</dd>
</dl>

<dl>
<dd>

**where:** `typing.Optional[Where]` — pass a where query to constrain returned documents (complex type, see documentation)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — limit the returned documents to a certain number
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — get a specific page of documents
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py#L455-L503">deletes_an_existing_user</a>(...) -> UsersUpsertConfirmation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing User
</dd>
</dl>
</dd>
</dl>

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

client.users.deletes_an_existing_user(
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

**id:** `str` — id of the User
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[float]` — number of levels to automatically populate relationships and uploads
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — retrieves document(s) in a specific locale
    
</dd>
</dl>

<dl>
<dd>

**fallback_locale:** `typing.Optional[str]` — specifies a fallback locale if no locale value exists
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py#L505-L604">updates_a_user</a>(...) -> UsersUpsertConfirmation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a User
</dd>
</dl>
</dd>
</dl>

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

client.users.updates_a_user(
    id_="id",
    id="id",
    updated_at="updatedAt",
    created_at="createdAt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — id of the User
    
</dd>
</dl>

<dl>
<dd>

**request:** `Users` 
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[float]` — number of levels to automatically populate relationships and uploads
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — retrieves document(s) in a specific locale
    
</dd>
</dl>

<dl>
<dd>

**fallback_locale:** `typing.Optional[str]` — specifies a fallback locale if no locale value exists
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Auth
<details><summary><code>client.auth.<a href="src/fern/auth/client.py#L31-L55">current_user_data</a>() -> UsersMe</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Data about the current user
</dd>
</dl>
</dd>
</dl>

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

client.auth.current_user_data()

```
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py#L57-L88">login</a>(...) -> UsersMe</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Login
</dd>
</dl>
</dd>
</dl>

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

client.auth.login(
    email="email",
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.auth.<a href="src/fern/auth/client.py#L90-L114">logout</a>() -> Confirmation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Logout
</dd>
</dl>
</dd>
</dl>

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

client.auth.logout()

```
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py#L116-L140">refresh_jwt</a>() -> UsersMe</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Refresh the JWT token
</dd>
</dl>
</dd>
</dl>

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

client.auth.refresh_jwt()

```
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

<details><summary><code>client.auth.<a href="src/fern/auth/client.py#L142-L170">unlock_account</a>(...) -> Confirmation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unlock account
</dd>
</dl>
</dd>
</dl>

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

client.auth.unlock_account(
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

**email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.auth.<a href="src/fern/auth/client.py#L172-L196">current_users_resource_access</a>() -> Access</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the user's access per resource
</dd>
</dl>
</dd>
</dl>

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

client.auth.current_users_resource_access()

```
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

## GlobalMyGlobal
<details><summary><code>client.global_my_global.<a href="src/fern/global_my_global/client.py#L31-L73">get_the_my_global</a>(...) -> MyGlobal</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the My Global
</dd>
</dl>
</dd>
</dl>

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

client.global_my_global.get_the_my_global()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**depth:** `typing.Optional[float]` — number of levels to automatically populate relationships and uploads
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — retrieves document(s) in a specific locale
    
</dd>
</dl>

<dl>
<dd>

**fallback_locale:** `typing.Optional[str]` — specifies a fallback locale if no locale value exists
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.global_my_global.<a href="src/fern/global_my_global/client.py#L75-L142">updates_the_my_global</a>(...) -> MyGlobalUpsertConfirmation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the My Global
</dd>
</dl>
</dd>
</dl>

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

client.global_my_global.updates_the_my_global(
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

**request:** `MyGlobal` 
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[float]` — number of levels to automatically populate relationships and uploads
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — retrieves document(s) in a specific locale
    
</dd>
</dl>

<dl>
<dd>

**fallback_locale:** `typing.Optional[str]` — specifies a fallback locale if no locale value exists
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

