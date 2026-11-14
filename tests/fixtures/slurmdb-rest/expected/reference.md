# Reference
## slurm
<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L47-L79">slurmdbd_get_job</a>(...) -> Dbv0037JobInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.
</dd>
</dl>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_get_job(
    job_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `int` — Slurm Job ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L81-L104">slurmdbd_get_db_config</a>() -> Dbv0037ConfigInfo</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_get_db_config()

```
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

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L106-L131">slurmdbd_set_db_config</a>() -> Dbv0037ConfigResponse</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_set_db_config()

```
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

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L133-L156">slurmdbd_get_tres</a>() -> Dbv0037TresInfo</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_get_tres()

```
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

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L158-L181">slurmdbd_update_tres</a>() -> Dbv0037ResponseTres</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_update_tres()

```
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

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L183-L213">slurmdbd_get_single_qos</a>(...) -> Dbv0037QosInfo</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_get_single_qos(
    qos_name="qos_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**qos_name:** `str` — Slurm QOS Name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L215-L245">slurmdbd_delete_qos</a>(...) -> Dbv0037ResponseQosDelete</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_delete_qos(
    qos_name="qos_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**qos_name:** `str` — Slurm QOS Name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L247-L270">slurmdbd_get_qos</a>() -> Dbv0037QosInfo</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_get_qos()

```
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

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L272-L297">slurmdbd_get_associations</a>() -> Dbv0037AssociationsInfo</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_get_associations()

```
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

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L299-L344">slurmdbd_get_association</a>(...) -> Dbv0037AssociationsInfo</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_get_association()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cluster:** `typing.Optional[str]` — Cluster name
    
</dd>
</dl>

<dl>
<dd>

**account:** `typing.Optional[str]` — Account name
    
</dd>
</dl>

<dl>
<dd>

**user:** `typing.Optional[str]` — User name
    
</dd>
</dl>

<dl>
<dd>

**partition:** `typing.Optional[str]` — Partition Name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L346-L394">slurmdbd_delete_association</a>(...) -> Dbv0037ResponseAssociationDelete</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_delete_association(
    account="account",
    user="user",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account:** `str` — Account name
    
</dd>
</dl>

<dl>
<dd>

**user:** `str` — User name
    
</dd>
</dl>

<dl>
<dd>

**cluster:** `typing.Optional[str]` — Cluster name
    
</dd>
</dl>

<dl>
<dd>

**partition:** `typing.Optional[str]` — Partition Name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L396-L426">slurmdbd_get_user</a>(...) -> Dbv0037UserInfo</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_get_user(
    user_name="user_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_name:** `str` — Slurm User Name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L428-L458">slurmdbd_delete_user</a>(...) -> Dbv0037ResponseUserDelete</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_delete_user(
    user_name="user_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_name:** `str` — Slurm User Name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L460-L483">slurmdbd_get_users</a>() -> Dbv0037UserInfo</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_get_users()

```
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

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L485-L510">slurmdbd_update_users</a>() -> Dbv0037ResponseUserUpdate</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_update_users()

```
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

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L512-L542">slurmdbd_get_cluster</a>(...) -> Dbv0037ClusterInfo</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_get_cluster(
    cluster_name="cluster_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cluster_name:** `str` — Slurm cluster name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L544-L574">slurmdbd_delete_cluster</a>(...) -> Dbv0037ResponseClusterDelete</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_delete_cluster(
    cluster_name="cluster_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cluster_name:** `str` — Slurm cluster name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L576-L599">slurmdbd_get_clusters</a>() -> Dbv0037ClusterInfo</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_get_clusters()

```
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

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L601-L626">slurmdbd_add_clusters</a>() -> Dbv0037ResponseClusterAdd</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_add_clusters()

```
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

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L628-L658">slurmdbd_get_wckey</a>(...) -> Dbv0037WckeyInfo</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_get_wckey(
    wckey="wckey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**wckey:** `str` — Slurm wckey name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L660-L690">slurmdbd_delete_wckey</a>(...) -> Dbv0037ResponseWckeyDelete</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_delete_wckey(
    wckey="wckey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**wckey:** `str` — Slurm wckey name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L692-L715">slurmdbd_get_wckeys</a>() -> Dbv0037WckeyInfo</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_get_wckeys()

```
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

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L717-L742">slurmdbd_add_wckeys</a>() -> Dbv0037ResponseWckeyAdd</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_add_wckeys()

```
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

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L744-L774">slurmdbd_get_account</a>(...) -> Dbv0037AccountInfo</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_get_account(
    account_name="account_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_name:** `str` — Slurm Account Name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L776-L806">slurmdbd_delete_account</a>(...) -> Dbv0037ResponseAccountDelete</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_delete_account(
    account_name="account_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_name:** `str` — Slurm Account Name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L808-L831">slurmdbd_get_accounts</a>() -> Dbv0037AccountInfo</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_get_accounts()

```
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

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L833-L858">slurmdbd_update_account</a>() -> Dbv0037AccountResponse</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_update_account()

```
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

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L860-L1029">slurmdbd_get_jobs</a>(...) -> Dbv0037JobInfo</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_get_jobs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**submit_time:** `typing.Optional[str]` 

Filter by submission time
 Accepted formats:
 HH:MM[:SS] [AM|PM]
MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]
MM/DD[/YY]-HH:MM[:SS]
YYYY-MM-DD[THH:MM[:SS]]
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` 

Filter by start time
 Accepted formats:
 HH:MM[:SS] [AM|PM]
MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]
MM/DD[/YY]-HH:MM[:SS]
YYYY-MM-DD[THH:MM[:SS]]
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` 

Filter by end time
 Accepted formats:
 HH:MM[:SS] [AM|PM]
MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]
MM/DD[/YY]-HH:MM[:SS]
YYYY-MM-DD[THH:MM[:SS]]
    
</dd>
</dl>

<dl>
<dd>

**account:** `typing.Optional[str]` — Comma delimited list of accounts to match
    
</dd>
</dl>

<dl>
<dd>

**association:** `typing.Optional[str]` — Comma delimited list of associations to match
    
</dd>
</dl>

<dl>
<dd>

**cluster:** `typing.Optional[str]` — Comma delimited list of cluster to match
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[str]` — Comma delimited list of constraints to match
    
</dd>
</dl>

<dl>
<dd>

**cpus_max:** `typing.Optional[str]` — Number of CPUs high range
    
</dd>
</dl>

<dl>
<dd>

**cpus_min:** `typing.Optional[str]` — Number of CPUs low range
    
</dd>
</dl>

<dl>
<dd>

**skip_steps:** `typing.Optional[bool]` — Report job step information
    
</dd>
</dl>

<dl>
<dd>

**disable_wait_for_result:** `typing.Optional[bool]` — Disable waiting for result from slurmdbd
    
</dd>
</dl>

<dl>
<dd>

**exit_code:** `typing.Optional[str]` — Exit code of job
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — Comma delimited list of formats to match
    
</dd>
</dl>

<dl>
<dd>

**group:** `typing.Optional[str]` — Comma delimited list of groups to match
    
</dd>
</dl>

<dl>
<dd>

**job_name:** `typing.Optional[str]` — Comma delimited list of job names to match
    
</dd>
</dl>

<dl>
<dd>

**nodes_max:** `typing.Optional[str]` — Number of nodes high range
    
</dd>
</dl>

<dl>
<dd>

**nodes_min:** `typing.Optional[str]` — Number of nodes low range
    
</dd>
</dl>

<dl>
<dd>

**partition:** `typing.Optional[str]` — Comma delimited list of partitions to match
    
</dd>
</dl>

<dl>
<dd>

**qos:** `typing.Optional[str]` — Comma delimited list of QOS to match
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` — Comma delimited list of job reasons to match
    
</dd>
</dl>

<dl>
<dd>

**reservation:** `typing.Optional[str]` — Comma delimited list of reservations to match
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` — Comma delimited list of states to match
    
</dd>
</dl>

<dl>
<dd>

**step:** `typing.Optional[str]` — Comma delimited list of job steps to match
    
</dd>
</dl>

<dl>
<dd>

**node:** `typing.Optional[str]` — Comma delimited list of used nodes to match
    
</dd>
</dl>

<dl>
<dd>

**wckey:** `typing.Optional[str]` — Comma delimited list of wckeys to match
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.slurm.<a href="src/fern/slurm/client.py#L1031-L1054">slurmdbd_diag</a>() -> Dbv0037Diag</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.slurm.slurmdbd_diag()

```
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

## Openapi
<details><summary><code>client.openapi.<a href="src/fern/openapi/client.py#L25-L47">retrieve_open_api_specification</a>()</code></summary>
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
    slurm_user_token="<X-SLURM-USER-TOKEN>",
    environment=FernApiEnvironment.DEFAULT,
)

client.openapi.retrieve_open_api_specification()

```
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

