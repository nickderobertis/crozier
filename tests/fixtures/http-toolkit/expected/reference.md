# Reference
## Base Routes
<details><summary><code>client.base_routes.<a href="src/fern/base_routes/client.py#L26-L52">base_ok</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a simple OK response
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.base_routes.base_ok()

```
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

<details><summary><code>client.base_routes.<a href="src/fern/base_routes/client.py#L54-L80">base_health</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check the health of the service, always returns 200 OK, /healthz is also available
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.base_routes.base_health()

```
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

<details><summary><code>client.base_routes.<a href="src/fern/base_routes/client.py#L82-L108">base_info</a>() -> SystemInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get system information
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.base_routes.base_info()

```
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

## Wildcard Inspection Routes
<details><summary><code>client.wildcard_inspection_routes.<a href="src/fern/wildcard_inspection_routes/client.py#L26-L58">wildcard_inspect_anything</a>(...) -> RequestInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.wildcard_inspection_routes.wildcard_inspect_anything(
    extra_path="extraPath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**extra_path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.wildcard_inspection_routes.<a href="src/fern/wildcard_inspection_routes/client.py#L60-L92">wildcard_inspect_anything_post</a>(...) -> RequestInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.wildcard_inspection_routes.wildcard_inspect_anything_post(
    extra_path="extraPath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**extra_path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.wildcard_inspection_routes.<a href="src/fern/wildcard_inspection_routes/client.py#L94-L126">wildcard_inspect_anything_put</a>(...) -> RequestInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.wildcard_inspection_routes.wildcard_inspect_anything_put(
    extra_path="extraPath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**extra_path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.wildcard_inspection_routes.<a href="src/fern/wildcard_inspection_routes/client.py#L128-L160">wildcard_inspect_anything_delete</a>(...) -> RequestInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.wildcard_inspection_routes.wildcard_inspect_anything_delete(
    extra_path="extraPath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**extra_path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.wildcard_inspection_routes.<a href="src/fern/wildcard_inspection_routes/client.py#L162-L194">wildcard_inspect_anything_patch</a>(...) -> RequestInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.wildcard_inspection_routes.wildcard_inspect_anything_patch(
    extra_path="extraPath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**extra_path:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Authenticated Routes
<details><summary><code>client.authenticated_routes.<a href="src/fern/authenticated_routes/client.py#L25-L51">auth_basic_auth</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Route is protected by basic auth, see docs for the credentials
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.authenticated_routes.auth_basic_auth()

```
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

<details><summary><code>client.authenticated_routes.<a href="src/fern/authenticated_routes/client.py#L53-L79">auth_basic_auth_post</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Route is protected by basic auth, see docs for the credentials
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.authenticated_routes.auth_basic_auth_post()

```
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

<details><summary><code>client.authenticated_routes.<a href="src/fern/authenticated_routes/client.py#L81-L107">auth_jwt_auth</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Route is protected by SHA256 JWT auth, see docs for obtaining the token
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.authenticated_routes.auth_jwt_auth()

```
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

<details><summary><code>client.authenticated_routes.<a href="src/fern/authenticated_routes/client.py#L109-L135">auth_jwt_auth_post</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Route is protected by basic auth, see docs for the credentials
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.authenticated_routes.auth_jwt_auth_post()

```
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

## Utility Routes
<details><summary><code>client.utility_routes.<a href="src/fern/utility_routes/client.py#L25-L51">utils_delay_random</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delay the response by 1 to 10 seconds randomly
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.utility_routes.utils_delay_random()

```
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

<details><summary><code>client.utility_routes.<a href="src/fern/utility_routes/client.py#L53-L83">utils_delay</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delay the response by the specified number of seconds
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.utility_routes.utils_delay(
    seconds=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**seconds:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.utility_routes.<a href="src/fern/utility_routes/client.py#L85-L111">utils_number</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a random number
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.utility_routes.utils_number()

```
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

<details><summary><code>client.utility_routes.<a href="src/fern/utility_routes/client.py#L113-L143">utils_number_max</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a random number up to the specified maximum
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.utility_routes.utils_number_max(
    max=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**max:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.utility_routes.<a href="src/fern/utility_routes/client.py#L145-L175">utils_status</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a response with the specified status code
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.utility_routes.utils_status(
    code=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**code:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.utility_routes.<a href="src/fern/utility_routes/client.py#L177-L203">utils_uuid</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a random UUID
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.utility_routes.utils_uuid()

```
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

<details><summary><code>client.utility_routes.<a href="src/fern/utility_routes/client.py#L205-L235">utils_uuid_from</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a UUID generated from the input string
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.utility_routes.utils_uuid_from(
    input="input",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.utility_routes.<a href="src/fern/utility_routes/client.py#L237-L263">utils_word</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a random word
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.utility_routes.utils_word()

```
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

<details><summary><code>client.utility_routes.<a href="src/fern/utility_routes/client.py#L265-L295">utils_words</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a number of random words
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.utility_routes.utils_words(
    count=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**count:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Inspect Routes
<details><summary><code>client.inspect_routes.<a href="src/fern/inspect_routes/client.py#L26-L52">inspect_inspect</a>() -> RequestInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Inspect the incoming HTTP request and return the details
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.inspect_routes.inspect_inspect()

```
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

<details><summary><code>client.inspect_routes.<a href="src/fern/inspect_routes/client.py#L54-L80">inspect_inspect_post</a>() -> RequestInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Inspect the incoming HTTP request and return the details
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.inspect_routes.inspect_inspect_post()

```
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

<details><summary><code>client.inspect_routes.<a href="src/fern/inspect_routes/client.py#L82-L108">inspect_inspect_put</a>() -> RequestInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Inspect the incoming HTTP request and return the details
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.inspect_routes.inspect_inspect_put()

```
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

<details><summary><code>client.inspect_routes.<a href="src/fern/inspect_routes/client.py#L110-L136">inspect_inspect_delete</a>() -> RequestInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Inspect the incoming HTTP request and return the details
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.inspect_routes.inspect_inspect_delete()

```
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

<details><summary><code>client.inspect_routes.<a href="src/fern/inspect_routes/client.py#L138-L164">inspect_inspect_patch</a>() -> RequestInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Inspect the incoming HTTP request and return the details
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    base_url="https://yourhost.com/path/to/api",
)

client.inspect_routes.inspect_inspect_patch()

```
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

