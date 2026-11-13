# Reference
## Health
<details><summary><code>client.health.<a href="src/fern/health/client.py#L26-L50">health_check</a>() -> GetApiHealthResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check if the API is running and connected to dependencies
</dd>
</dl>
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

client.health.health_check()

```
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

## Shards
<details><summary><code>client.shards.<a href="src/fern/shards/client.py#L33-L75">list_all_shards</a>(...) -> GetApiShardsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a paginated list of all Crystal shards
</dd>
</dl>
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

client.shards.list_all_shards()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of items per page
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Search query to filter shards by name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shards.<a href="src/fern/shards/client.py#L77-L139">create_a_new_shard</a>(...) -> PostApiShardsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publish a new Crystal shard to the registry
</dd>
</dl>
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

client.shards.create_a_new_shard(
    name="my-shard",
    repository_url="https://github.com/user/my-shard",
    version="1.0.0",
)

```
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

**repository_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**homepage_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**documentation_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**license:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shards.<a href="src/fern/shards/client.py#L141-L225">upload_shard_package</a>(...) -> PostApiShardsUploadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a Crystal shard package via multipart form data.
This endpoint accepts a .tar.gz file along with shard metadata.
The package is uploaded directly to MinIO storage and a ShardVersion is created.

**Authentication required:** Include auth_token in Authorization header or as query parameter.
**Size limit:** Maximum 50 MB per package.
</dd>
</dl>
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

client.shards.upload_shard_package(
    package="example_package",
    name="name",
    version="version",
    repository_url="repository_url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Unique shard name (lowercase, alphanumeric with hyphens)
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` — Semantic version number
    
</dd>
</dl>

<dl>
<dd>

**repository_url:** `str` — Git repository URL
    
</dd>
</dl>

<dl>
<dd>

**package:** `core.File` — Package archive file (.tar.gz, max 50 MB)
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Brief description of the shard
    
</dd>
</dl>

<dl>
<dd>

**homepage_url:** `typing.Optional[str]` — Project homepage URL
    
</dd>
</dl>

<dl>
<dd>

**documentation_url:** `typing.Optional[str]` — Documentation URL
    
</dd>
</dl>

<dl>
<dd>

**license:** `typing.Optional[str]` — SPDX license identifier
    
</dd>
</dl>

<dl>
<dd>

**checksum:** `typing.Optional[str]` — Optional SHA256 checksum for verification (computed if not provided)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shards.<a href="src/fern/shards/client.py#L227-L263">get_shard_details_by_name_deprecated</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Superseded by /api/shards/{host}/{owner}/{repo}. A shard is identified by
the repository it comes from, because two shards may share a name on
different hosts.

When exactly one shard carries the name, this responds 301 with the
canonical path in Location. When more than one does, it responds 409
with the candidate paths rather than guessing which was meant.
</dd>
</dl>
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

client.shards.get_shard_details_by_name_deprecated(
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

**name:** `str` — Shard display name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shards.<a href="src/fern/shards/client.py#L265-L308">get_shard_details</a>(...) -> ShardDetail</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a shard by the repository that identifies it, for example
/api/shards/github.com/kemalcr/kemal.

Nested namespace paths (host/group/subgroup/repo) are not addressable:
identity is host/owner/repo.
</dd>
</dl>
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

client.shards.get_shard_details(
    host="github.com",
    owner="kemalcr",
    repo="kemal",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**host:** `str` — Repository host
    
</dd>
</dl>

<dl>
<dd>

**owner:** `str` — Owner or organisation on that host
    
</dd>
</dl>

<dl>
<dd>

**repo:** `str` — Repository name on that host
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Versions
<details><summary><code>client.versions.<a href="src/fern/versions/client.py#L27-L66">list_shard_versions</a>(...) -> GetApiShardsHostOwnerRepoVersionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all versions of a specific shard
</dd>
</dl>
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

client.versions.list_shard_versions(
    host="github.com",
    owner="kemalcr",
    repo="kemal",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**host:** `str` — Repository host
    
</dd>
</dl>

<dl>
<dd>

**owner:** `str` — Owner or organisation on that host
    
</dd>
</dl>

<dl>
<dd>

**repo:** `str` — Repository name on that host
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.versions.<a href="src/fern/versions/client.py#L68-L111">get_specific_version</a>(...) -> GetApiShardsHostOwnerRepoVersionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get detailed information about a specific version of a shard
</dd>
</dl>
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

client.versions.get_specific_version(
    host="github.com",
    owner="kemalcr",
    repo="kemal",
    version="version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**host:** `str` — Repository host
    
</dd>
</dl>

<dl>
<dd>

**owner:** `str` — Owner or organisation on that host
    
</dd>
</dl>

<dl>
<dd>

**repo:** `str` — Repository name on that host
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` — Version string (e.g., 1.0.0)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Downloads
<details><summary><code>client.downloads.<a href="src/fern/downloads/client.py#L28-L73">track_download</a>(...) -> PostApiShardsHostOwnerRepoVersionDownloadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Record a download of a specific shard version. Downloads are attributed
to the repository, never to a name, so this endpoint takes the identity
only.
</dd>
</dl>
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

client.downloads.track_download(
    host="github.com",
    owner="kemalcr",
    repo="kemal",
    version="version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**host:** `str` — Repository host
    
</dd>
</dl>

<dl>
<dd>

**owner:** `str` — Owner or organisation on that host
    
</dd>
</dl>

<dl>
<dd>

**repo:** `str` — Repository name on that host
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` — Version string (e.g., 1.0.0)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

