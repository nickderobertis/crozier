# Reference
<details><summary><code>client.<a href="src/fern/client.py">send_lower</a>(...) -> Parcel</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.send_lower(
    forwarded_proto="v2",
    forwarded_host="v3",
    forwarded_port="v4",
    forwarded="v5",
    real_ip="v6",
    host="v7",
    connection="v8",
    transfer_encoding="v9",
    te="v10",
    trailer="v11",
    upgrade="v12",
    via="v13",
    keep_alive="v14",
    expect="v15",
    date="v16",
    accept="v17",
    accept_encoding="v18",
    accept_charset="v19",
    accept_language="v20",
    referer="v21",
    content_encoding="v22",
    content_md5="v23",
    content_language="v24",
    cache_control="v25",
    pragma="v26",
    proxy_authorization="v27",
    dnt="v28",
    sec_fetch_mode="v29",
    request_id="v30",
    if_match="v31",
    range="v32",
    authorization="v33",
    csrf_token="v34",
    http_method_override="v35",
    set_cookie="v40",
    forwarded_server="v41",
    client_ip="v42",
    true_client_ip="v43",
    original_forwarded_for="v44",
    content_range="v45",
    idempotency_key="v47",
    label="crate",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**forwarded_proto:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**forwarded_host:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**forwarded_port:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**forwarded:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**real_ip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**host:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**transfer_encoding:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**te:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**trailer:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**upgrade:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**via:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**keep_alive:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expect:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**date:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**accept:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**accept_encoding:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**accept_charset:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**accept_language:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**referer:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**content_encoding:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**content_md5:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**content_language:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cache_control:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**pragma:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**proxy_authorization:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**dnt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sec_fetch_mode:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**if_match:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**range:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**csrf_token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**http_method_override:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**set_cookie:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**forwarded_server:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_ip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**true_client_ip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**original_forwarded_for:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**content_range:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `Parcel` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">send_canonical</a>(...) -> Parcel</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.send_canonical(
    forwarded_proto="c2",
    forwarded_host="c3",
    forwarded_port="c4",
    forwarded="c5",
    real_ip="c6",
    host="c7",
    connection="c8",
    transfer_encoding="c9",
    te="c10",
    trailer="c11",
    upgrade="c12",
    via="c13",
    keep_alive="c14",
    expect="c15",
    date="c16",
    accept="c17",
    accept_encoding="c18",
    accept_charset="c19",
    accept_language="c20",
    referer="c21",
    content_encoding="c22",
    content_md5="c23",
    content_language="c24",
    cache_control="c25",
    pragma="c26",
    proxy_authorization="c27",
    dnt="c28",
    sec_fetch_mode="c29",
    request_id="c30",
    if_match="c31",
    range="c32",
    authorization="c33",
    csrf_token="c34",
    http_method_override="c35",
    set_cookie="c40",
    forwarded_server="c41",
    client_ip="c42",
    true_client_ip="c43",
    original_forwarded_for="c44",
    content_range="c45",
    idempotency_key="c47",
    label="crate",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**forwarded_proto:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**forwarded_host:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**forwarded_port:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**forwarded:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**real_ip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**host:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**transfer_encoding:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**te:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**trailer:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**upgrade:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**via:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**keep_alive:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expect:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**date:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**accept:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**accept_encoding:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**accept_charset:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**accept_language:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**referer:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**content_encoding:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**content_md5:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**content_language:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cache_control:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**pragma:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**proxy_authorization:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**dnt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sec_fetch_mode:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**if_match:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**range:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**csrf_token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**http_method_override:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**set_cookie:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**forwarded_server:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_ip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**true_client_ip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**original_forwarded_for:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**content_range:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `Parcel` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">send_optional</a>(...) -> Parcel</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.send_optional(
    forwarded_proto="o2",
    host="o3",
    transfer_encoding="o4",
    label="crate",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Parcel` 
    
</dd>
</dl>

<dl>
<dd>

**forwarded_proto:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**host:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**transfer_encoding:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">list_relays</a>() -> typing.List[Parcel]</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.list_relays()

```
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

