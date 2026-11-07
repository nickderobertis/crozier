# Reference
<details><summary><code>client.<a href="src/fern/client.py">fetch_bootstrap_script_url_for_a_cluster</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is used to fetch the URL to a script to use to bootstrap the edge cluster. The URL returned may contain authentication and may only be valid for a certain length of time. The script needs to be fetched from the returned URL using GET and run using a Bourne shell, with `kubectl` in the PATH and configured to access the edge cluster.
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.fetch_bootstrap_script_url_for_a_cluster(
    cluster="cluster",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cluster:** `typing.Optional[str]` — Cluster UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">fetch_cluster_setup_status</a>(...) -> GetClusterClusterStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The _Edge cluster setup status_ Config Store entries should not normally be accessible except to the Cluster Manager itself. This endpoint is suitable for polling to find out when a cluster is ready to be bootstrapped. Do not rely on any fields other than those documented in the response.
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.fetch_cluster_setup_status(
    cluster="cluster",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cluster:** `typing.Optional[str]` — Cluster UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">update_a_secret_value_on_an_edge_cluster</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint accepts secret information, as a binary blob, and arranges to securely make it available as a Kubernetes Secret on the edge cluster. Once encrypted there is no way to retrieve the information without access to the private key on the edge cluster.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.update_a_secret_value_on_an_edge_cluster(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — The secret information to encrypt, as a binary blob.
    
</dd>
</dl>

<dl>
<dd>

**cluster:** `typing.Optional[str]` — Cluster UUID
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `typing.Optional[str]` — Kubernetes namespace of Secret to modify
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Kubernetes name of Secret to modify
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">delete_a_secret_value_from_an_edge_cluster</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The requested key will be removed from the Secret. If the Secret is now empty, the entire Secret will be removed. A successful response from this endpoint does not indicate that the key has actually been removed on the edge cluster yet.
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.delete_a_secret_value_from_an_edge_cluster(
    cluster="cluster",
    namespace="namespace",
    name="name",
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

**key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cluster:** `typing.Optional[str]` — Cluster UUID
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `typing.Optional[str]` — Kubernetes namespace of Secret to modify
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Kubernetes name of Secret to modify
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

