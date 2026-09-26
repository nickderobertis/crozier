# Reference
## Deployment
<details><summary><code>client.deployment.<a href="src/fern/deployment/client.py">license_status</a>() -> DeploymentLicenseStatusResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.deployment.license_status()

```
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

## Doc
<details><summary><code>client.doc.<a href="src/fern/doc/client.py">head</a>(...) -> DocHead200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.head(
    doc_id="docId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.<a href="src/fern/doc/client.py">download</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.download(
    doc_id="docId",
    layer_name="layerName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.<a href="src/fern/doc/client.py">manifest</a>(...) -> DocManifest200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.manifest(
    doc_id="docId",
    layer_name="layerName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.<a href="src/fern/doc/client.py">render</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Render parameters (viewport, format) pass as flat dotted query keys, e.g. `?viewport.kind=width&viewport.width=800`; the full grammar is documented with the viewer.
</dd>
</dl>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.render(
    doc_id="docId",
    layer_name="layerName",
    page_key="pageKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.<a href="src/fern/doc/client.py">text</a>(...) -> DocText200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.text(
    doc_id="docId",
    layer_name="layerName",
    page_key="pageKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Shares
<details><summary><code>client.shares.<a href="src/fern/shares/client.py">exchange</a>(...) -> SharesExchange200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unauthenticated, but requires a browser Origin header, checked against the grant allowlist. Unknown, revoked, and disabled tokens are indistinguishable (404). Passphrase-protected grants return 422 SharePasswordRequired until `password` is supplied. Mounted only when the deployment can sign (HS256 mode).
</dd>
</dl>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.shares.exchange(
    share_token="shareToken",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**share_token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shares.<a href="src/fern/shares/client.py">list</a>(...) -> SharesList200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.shares.list(
    tenant_id="tenantId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**doc_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shares.<a href="src/fern/shares/client.py">create</a>(...) -> SharesCreate200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The returned share id IS the public share token. Mounted only when the deployment can sign (HS256 mode) — exchange mints session JWTs, so grants exist only where minting does.
</dd>
</dl>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.shares.create(
    tenant_id="tenantId",
    doc_id="docId",
    scope=[
        "scope"
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

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**origins:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**session_ttl_seconds:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shares.<a href="src/fern/shares/client.py">get</a>(...) -> SharesGet200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.shares.get(
    tenant_id="tenantId",
    share_id="shareId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**share_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shares.<a href="src/fern/shares/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.shares.delete(
    tenant_id="tenantId",
    share_id="shareId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**share_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shares.<a href="src/fern/shares/client.py">update</a>(...) -> SharesUpdate200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.shares.update(
    tenant_id="tenantId",
    share_id="shareId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**share_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**origins:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**session_ttl_seconds:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**disabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tenants
<details><summary><code>client.tenants.<a href="src/fern/tenants/client.py">list</a>(...) -> TenantsList200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.tenants.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.<a href="src/fern/tenants/client.py">create</a>(...) -> TenantsCreate200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.tenants.create(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.<a href="src/fern/tenants/client.py">get</a>(...) -> TenantsGet200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.tenants.get(
    tenant_id="tenantId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.<a href="src/fern/tenants/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Destroys the tenant and everything in its namespace — documents, layers, stored bytes, audit history. Irreversible.
</dd>
</dl>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.tenants.delete(
    tenant_id="tenantId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.<a href="src/fern/tenants/client.py">resume</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.tenants.resume(
    tenant_id="tenantId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.<a href="src/fern/tenants/client.py">suspend</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Instantly reversible with resume. The API token is exempt, so a suspended tenant can still be inspected, exported, resumed, or deleted.
</dd>
</dl>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.tenants.suspend(
    tenant_id="tenantId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenants.<a href="src/fern/tenants/client.py">usage</a>(...) -> TenantsUsage200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Facts only — no limits or billing state. Views count share exchanges plus authorized /v1/access grants, deduplicated across the two.
</dd>
</dl>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.tenants.usage(
    tenant_id="tenantId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Documents
<details><summary><code>client.documents.<a href="src/fern/documents/client.py">list</a>(...) -> DocumentsList200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.documents.list(
    tenant_id="tenantId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[ListDocumentsRequestState]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/fern/documents/client.py">get</a>(...) -> DocumentsGet200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.documents.get(
    tenant_id="tenantId",
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

**tenant_id:** `str` 
    
</dd>
</dl>

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

<details><summary><code>client.documents.<a href="src/fern/documents/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.documents.delete(
    tenant_id="tenantId",
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

**tenant_id:** `str` 
    
</dd>
</dl>

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

<details><summary><code>client.documents.<a href="src/fern/documents/client.py">commit</a>(...) -> DocumentsCommit200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.documents.commit(
    tenant_id="tenantId",
    id="id",
    sha256="sha256",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sha256:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/fern/documents/client.py">download</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.documents.download(
    tenant_id="tenantId",
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

**tenant_id:** `str` 
    
</dd>
</dl>

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

<details><summary><code>client.documents.<a href="src/fern/documents/client.py">thumbnail</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.documents.thumbnail(
    tenant_id="tenantId",
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

**tenant_id:** `str` 
    
</dd>
</dl>

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

<details><summary><code>client.documents.<a href="src/fern/documents/client.py">upload_proxy</a>(...) -> DocumentsUploadProxy200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This bounded origin-mediated fallback must only be used after documents.init returns upload.kind=proxy. Auto mode prefers a presigned object-store PUT whenever available.
</dd>
</dl>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.documents.upload_proxy(
    tenant_id="tenantId",
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

**tenant_id:** `str` 
    
</dd>
</dl>

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/fern/documents/client.py">import_from</a>(...) -> DocumentsImportFrom200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Default mode is synchronous and bounded: the response returns only after the transfer verified and committed (or failed). mode=async (connection sources only) answers 202 immediately and an in-process worker performs the transfer with leased, fenced retries; poll the document until ready/failed. The deployment import policy gates scheme, network range, and size; sources must declare a length. CloudPDF copies and owns the bytes — the source is never referenced in place. A 502 marks a retryable upstream failure: retry with the same idempotencyKey to resume the same document. URL sources are capabilities and never echoed back. Connection sources name operator-registered storage (bucket/prefix scope, allowed credential classes, and tenant bindings are deployment configuration); `revision` is provider-interpreted (S3 VersionId, GCS generation, Azure version id).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.documents import DocumentsImportFromRequestSource_Url

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.documents.import_from(
    tenant_id="tenantId",
    source=DocumentsImportFromRequestSource_Url(
        url="url",
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

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `DocumentsImportFromRequestSource` — Where CloudPDF pulls the bytes from. The two shapes differ in WHO supplies the authority to read, not in which storage vendor holds the file.
    
</dd>
</dl>

<dl>
<dd>

**expected:** `typing.Optional[DocumentsImportFromRequestExpected]` — Integrity pins, enforced when present. When absent, the server-observed values become authoritative.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Retrying with the same key resumes the same document rather than importing a second copy — including after a 502.
    
</dd>
</dl>

<dl>
<dd>

**dedup_mode:** `typing.Optional[DocumentsImportFromRequestDedupMode]` — always-create (default) creates a new document every time. reuse-existing returns a document that already holds the same content instead of storing it twice.
    
</dd>
</dl>

<dl>
<dd>

**doc_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[DocumentsImportFromRequestMode]` — sync (default) holds the response open for the whole transfer. async answers 202 with the document pending and transfers in the background; it requires a connection source, and filesystem connections additionally require expected.sha256.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/fern/documents/client.py">init</a>(...) -> DocumentsInit200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.documents.init(
    tenant_id="tenantId",
    content_length=1.1,
    content_sha256="contentSha256",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**content_length:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**content_sha256:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**dedup_mode:** `typing.Optional[DocumentsInitRequestDedupMode]` — always-create (default) creates a new document every time. reuse-existing returns a document that already holds the same content instead of storing it twice.
    
</dd>
</dl>

<dl>
<dd>

**doc_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**upload_ttl_sec:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**upload_preference:** `typing.Optional[DocumentsInitRequestUploadPreference]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tokens
<details><summary><code>client.tokens.<a href="src/fern/tokens/client.py">issue</a>(...) -> TokensIssue200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

kind "tenant" requires the API token — authority mints only downward. Mounted only when the deployment can sign (HS256 mode); asymmetric deployments mint with their own private key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TokensIssueRequest_Doc

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.tokens.issue(
    tenant_id="tenantId",
    request=TokensIssueRequest_Doc(
        sub="sub",
        doc_id="docId",
        scope=[
            "scope"
        ],
        expires_in=1,
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

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `TokensIssueRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tokens.<a href="src/fern/tokens/client.py">revoke</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mounted only when the deployment enables token revocation.
</dd>
</dl>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.tokens.revoke(
    tenant_id="tenantId",
    jti="jti",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenant_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**jti:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**expires_at_seconds:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Doc Annotations
<details><summary><code>client.doc.annotations.<a href="src/fern/doc/annotations/client.py">list_all</a>(...) -> DocAnnotationsListAll200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one entry per page plus the audit-log cursor for reconciling subsequent document events. Page order is unspecified; join by `pageState.pageObjectNumber` when display order matters.
</dd>
</dl>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.annotations.list_all(
    doc_id="docId",
    layer_name="layerName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.annotations.<a href="src/fern/doc/annotations/client.py">list</a>(...) -> DocAnnotationsList200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.annotations.list(
    doc_id="docId",
    layer_name="layerName",
    page_key="pageKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.annotations.<a href="src/fern/doc/annotations/client.py">create</a>(...) -> DocAnnotationsCreate200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Doc JWTs may instead carry collab scopes (annotations:create:self, …) that refine per-annotation authorship rules; the API token is exempt from both.
</dd>
</dl>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.annotations.create(
    doc_id="docId",
    layer_name="layerName",
    page_key="pageKey",
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

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DocAnnotationsCreateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.annotations.<a href="src/fern/doc/annotations/client.py">delete</a>(...) -> DocAnnotationsDelete200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.annotations.delete(
    doc_id="docId",
    layer_name="layerName",
    page_key="pageKey",
    annot_key="annotKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**annot_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.annotations.<a href="src/fern/doc/annotations/client.py">update</a>(...) -> DocAnnotationsUpdate200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.annotations.update(
    doc_id="docId",
    layer_name="layerName",
    page_key="pageKey",
    annot_key="annotKey",
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

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**annot_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DocAnnotationsUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.annotations.<a href="src/fern/doc/annotations/client.py">export_appearance</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.annotations.export_appearance(
    doc_id="docId",
    layer_name="layerName",
    page_key="pageKey",
    request={
        "string": {"key": "value"}
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

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DocAnnotationsExportAppearanceRequest` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.annotations.<a href="src/fern/doc/annotations/client.py">flatten</a>(...) -> DocAnnotationsFlatten200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.annotations.flatten(
    doc_id="docId",
    layer_name="layerName",
    page_key="pageKey",
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

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DocAnnotationsFlattenRequest` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Doc Forms
<details><summary><code>client.doc.forms.<a href="src/fern/doc/forms/client.py">get</a>(...) -> DocFormsGet200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.forms.get(
    doc_id="docId",
    layer_name="layerName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.forms.<a href="src/fern/doc/forms/client.py">export_data</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.forms.export_data(
    doc_id="docId",
    layer_name="layerName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[ExportDataFormsRequestFormat]` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.forms.<a href="src/fern/doc/forms/client.py">import_data</a>(...) -> DocFormsImportData200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.forms.import_data(
    doc_id="docId",
    layer_name="layerName",
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

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DocFormsImportDataRequest` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.forms.<a href="src/fern/doc/forms/client.py">reset</a>(...) -> DocFormsReset200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.forms.reset(
    doc_id="docId",
    layer_name="layerName",
    field_key="fieldKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**field_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.forms.<a href="src/fern/doc/forms/client.py">set_value</a>(...) -> DocFormsSetValue200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.forms.set_value(
    doc_id="docId",
    layer_name="layerName",
    field_key="fieldKey",
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

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**field_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DocFormsSetValueRequest` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Doc Metadata
<details><summary><code>client.doc.metadata.<a href="src/fern/doc/metadata/client.py">get</a>(...) -> DocMetadataGet200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.metadata.get(
    doc_id="docId",
    layer_name="layerName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Doc Pages
<details><summary><code>client.doc.pages.<a href="src/fern/doc/pages/client.py">set_scale</a>(...) -> DocPagesSetScale200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.pages.set_scale(
    doc_id="docId",
    layer_name="layerName",
    page_key="pageKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**measure:** `typing.Optional[DocPagesSetScaleRequestMeasure]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.pages.<a href="src/fern/doc/pages/client.py">viewports</a>(...) -> DocPagesViewports200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.pages.viewports(
    doc_id="docId",
    layer_name="layerName",
    page_key="pageKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.pages.<a href="src/fern/doc/pages/client.py">delete</a>(...) -> DocPagesDelete200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.pages.delete(
    doc_id="docId",
    layer_name="layerName",
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

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DocPagesDeleteRequest` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.pages.<a href="src/fern/doc/pages/client.py">extract</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A read, not a mutation: the source document is untouched and no event is published. Body is `{"pageObjectNumbers": number[]}`; the response body is the new PDF.
</dd>
</dl>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.pages.extract(
    doc_id="docId",
    layer_name="layerName",
    request={
        "string": {"key": "value"}
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

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DocPagesExtractRequest` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.pages.<a href="src/fern/doc/pages/client.py">flatten</a>(...) -> DocPagesFlatten200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.pages.flatten(
    doc_id="docId",
    layer_name="layerName",
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

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DocPagesFlattenRequest` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.pages.<a href="src/fern/doc/pages/client.py">insert</a>(...) -> DocPagesInsert200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Multipart mutation envelope: a `body` field holding `{"destIndex"?: number}` (omitted → append) plus a `resource:source` file part carrying the standalone PDF whose pages are copied in. The inserted copies get fresh page object numbers, returned in insertion order.
</dd>
</dl>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.pages.insert(
    doc_id="docId",
    layer_name="layerName",
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

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.pages.<a href="src/fern/doc/pages/client.py">insert_blank</a>(...) -> DocPagesInsertBlank200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Body is `{"size": {"width", "height"}, "count"?, "destIndex"?}` — size in PDF points, count in [1, 100], destIndex omitted → append.
</dd>
</dl>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.pages.insert_blank(
    doc_id="docId",
    layer_name="layerName",
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

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DocPagesInsertBlankRequest` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.pages.<a href="src/fern/doc/pages/client.py">move</a>(...) -> DocPagesMove200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.pages.move(
    doc_id="docId",
    layer_name="layerName",
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

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DocPagesMoveRequest` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.pages.<a href="src/fern/doc/pages/client.py">set_name</a>(...) -> DocPagesSetName200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.pages.set_name(
    doc_id="docId",
    layer_name="layerName",
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

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DocPagesSetNameRequest` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.pages.<a href="src/fern/doc/pages/client.py">remove_name</a>(...) -> DocPagesRemoveName200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.pages.remove_name(
    doc_id="docId",
    layer_name="layerName",
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

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DocPagesRemoveNameRequest` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.pages.<a href="src/fern/doc/pages/client.py">rotate</a>(...) -> DocPagesRotate200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.pages.rotate(
    doc_id="docId",
    layer_name="layerName",
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

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DocPagesRotateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Doc Redactions
<details><summary><code>client.doc.redactions.<a href="src/fern/doc/redactions/client.py">apply</a>(...) -> DocRedactionsApply200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.redactions.apply(
    doc_id="docId",
    layer_name="layerName",
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

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DocRedactionsApplyRequest` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Doc Signatures
<details><summary><code>client.doc.signatures.<a href="src/fern/doc/signatures/client.py">list</a>(...) -> DocSignaturesList200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Describes the bytes the layer is over: the base version's signatures plus the layer's own edits as the last revision. Signed bytes (contents, digests, revision prefixes) are served per base version under /versions.
</dd>
</dl>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.signatures.list(
    doc_id="docId",
    layer_name="layerName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.signatures.<a href="src/fern/doc/signatures/client.py">abort</a>(...) -> DocSignaturesAbort200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.signatures.abort(
    doc_id="docId",
    layer_name="layerName",
    signing_id="signingId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**signing_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.signatures.<a href="src/fern/doc/signatures/client.py">complete</a>(...) -> DocSignaturesComplete200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`cms` is the detached CMS over the prepared digest, base64. `expectedVersion` must be what prepare returned. Idempotent by signing id: the same CMS again answers `already-completed`. Every layer of the document then sits over the new version; refetch the manifest after a completion.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.doc.signatures import DocSignaturesCompleteRequestExpectedVersion

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.signatures.complete(
    doc_id="docId",
    layer_name="layerName",
    signing_id="signingId",
    cms="cms",
    expected_version=DocSignaturesCompleteRequestExpectedVersion(
        base_sha256="baseSha256",
        edits_version=1,
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

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**signing_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cms:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expected_version:** `DocSignaturesCompleteRequestExpectedVersion` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.signatures.<a href="src/fern/doc/signatures/client.py">analysis</a>(...) -> DocSignaturesAnalysis200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exactly one of `since.signature=<index>` or `since.revision=<index>`; the layer's pending edits are the end. `level=fill|annotate|lta|none` evaluates exploratorily and never becomes a verdict. For history between two base revisions use the version analysis.
</dd>
</dl>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.signatures.analysis(
    doc_id="docId",
    layer_name="layerName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**since_signature:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**since_revision:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**level:** `typing.Optional[AnalysisSignaturesRequestLevel]` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.signatures.<a href="src/fern/doc/signatures/client.py">prepare</a>(...) -> DocSignaturesPrepare200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The multipart envelope: a JSON `body` part (field, subFilter, digest, contentsSize, signer, certify, lock, appearance) and an optional `resource:<key>` PDF part the body's `appearance.resource` names. A certification (`certify.permission`) additionally requires `doc.sign.certify`. The layer is read-only until the signing completes, is aborted, or expires (15 minutes). A layer behind the document head cannot sign (StaleBase).
</dd>
</dl>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.signatures.prepare(
    doc_id="docId",
    layer_name="layerName",
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

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layer_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Doc Versions
<details><summary><code>client.doc.versions.<a href="src/fern/doc/versions/client.py">list</a>(...) -> DocVersionsList200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Every completed signature publishes a new version. Never cached: the list grows.
</dd>
</dl>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.versions.list(
    doc_id="docId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.versions.<a href="src/fern/doc/versions/client.py">analysis</a>(...) -> DocVersionsAnalysis200Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exactly one of `since.signature` / `since.revision`; `until=<revision>` defaults to the last. The same answer for every layer and every caller.
</dd>
</dl>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.versions.analysis(
    doc_id="docId",
    sha="sha",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sha:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**since_signature:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**since_revision:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**level:** `typing.Optional[AnalysisVersionsRequestLevel]` 
    
</dd>
</dl>

<dl>
<dd>

**until:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**policy:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.versions.<a href="src/fern/doc/versions/client.py">download</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.versions.download(
    doc_id="docId",
    sha="sha",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sha:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.versions.<a href="src/fern/doc/versions/client.py">revision</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.versions.revision(
    doc_id="docId",
    sha="sha",
    index=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sha:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**index:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.versions.<a href="src/fern/doc/versions/client.py">signatures</a>(...) -> DocVersionsSignatures200Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.versions.signatures(
    doc_id="docId",
    sha="sha",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sha:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.versions.<a href="src/fern/doc/versions/client.py">signature_contents</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`fieldKey` is the field's fully qualified name, token-text encoded (the same encoding attachment keys use).
</dd>
</dl>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.versions.signature_contents(
    doc_id="docId",
    sha="sha",
    field_key="fieldKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sha:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**field_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.doc.versions.<a href="src/fern/doc/versions/client.py">signature_digest</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

What a CMS verifier compares its message digest to.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.doc.versions import SignatureDigestVersionsRequestAlgorithm

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.doc.versions.signature_digest(
    doc_id="docId",
    sha="sha",
    field_key="fieldKey",
    algorithm=SignatureDigestVersionsRequestAlgorithm.SHA1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sha:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**field_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**algorithm:** `SignatureDigestVersionsRequestAlgorithm` 
    
</dd>
</dl>

<dl>
<dd>

**document_password:** `typing.Optional[str]` — Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

