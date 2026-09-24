# Reference
<details><summary><code>client.<a href="src/fern/client.py">token_legacy</a>(...) -> TokenResponseLegacy</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated. Will be removed in a future release. Please use /token/sign instead. Returns a signed, non-expiring legacy access token.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SignTokenPayloadPayload

client = FernApi(
    okapi_tenant="<X-Okapi-Tenant>",
    okapi_url="<X-Okapi-Url>",
    base_url="https://yourhost.com/path/to/api",
)

client.token_legacy(
    payload=SignTokenPayloadPayload(
        sub="sub",
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

**request:** `SignTokenPayload` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">token_sign_legacy</a>(...) -> Token</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a signed, expiring refresh token. This is a legacy endpoint and should not be
called by new code and will soon be fully depreciated.
</dd>
</dl>
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
    okapi_tenant="<X-Okapi-Tenant>",
    okapi_url="<X-Okapi-Url>",
    base_url="https://yourhost.com/path/to/api",
)

client.token_sign_legacy(
    user_id="userId",
    sub="sub",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The user id of the request
    
</dd>
</dl>

<dl>
<dd>

**sub:** `str` — The subject (user id) of the request
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">token_sign</a>(...) -> TokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a signed, expiring access token and refresh token. Also returns the expiration
of each token in the body of the response. The access token time to live is 10 minutes and
the refresh token is one week.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SignTokenPayloadPayload

client = FernApi(
    okapi_tenant="<X-Okapi-Tenant>",
    okapi_url="<X-Okapi-Url>",
    base_url="https://yourhost.com/path/to/api",
)

client.token_sign(
    payload=SignTokenPayloadPayload(
        sub="sub",
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

**request:** `SignTokenPayload` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">token_refresh</a>(...) -> TokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a new refresh token and a new access token. Also returns the expiration of each token
in the body of the response. Time to live is 10 minutes for the access token and one week for
the refresh token.
</dd>
</dl>
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
    okapi_tenant="<X-Okapi-Tenant>",
    okapi_url="<X-Okapi-Url>",
    base_url="https://yourhost.com/path/to/api",
)

client.token_refresh(
    refresh_token="refreshToken",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `RefreshToken` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">token_invalidate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invalidate a single refresh token. An access token cannot be invalidated and remains valid until its expiration time; this is by design because the access token is stateless.
</dd>
</dl>
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
    okapi_tenant="<X-Okapi-Tenant>",
    okapi_url="<X-Okapi-Url>",
    base_url="https://yourhost.com/path/to/api",
)

client.token_invalidate(
    refresh_token="refreshToken",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `RefreshToken` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">token_invalidate_all</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invalidate all refresh tokens for a user. An access token cannot be invalidated and remains valid until its expiration time; this is by design because the access token is stateless.
</dd>
</dl>
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
    okapi_tenant="<X-Okapi-Tenant>",
    okapi_url="<X-Okapi-Url>",
    base_url="https://yourhost.com/path/to/api",
)

client.token_invalidate_all()

```
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

