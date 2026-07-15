# Reference
## Execute
<details><summary><code>client.execute.<a href="src/fern/execute/client.py">get_proxy</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Proxies a downstream GET request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
**Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_downstream_url="YOUR_APIDECK_DOWNSTREAM_URL",
    apideck_downstream_authorization="YOUR_APIDECK_DOWNSTREAM_AUTHORIZATION",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
)
client.execute.get_proxy()

```
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

<details><summary><code>client.execute.<a href="src/fern/execute/client.py">post_proxy</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Proxies a downstream POST request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
**Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.
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
from fern.execute import PostProxyRequestBodyZero

from fern import FernApi

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_downstream_url="YOUR_APIDECK_DOWNSTREAM_URL",
    apideck_downstream_authorization="YOUR_APIDECK_DOWNSTREAM_AUTHORIZATION",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
)
client.execute.post_proxy(
    request=PostProxyRequestBodyZero(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PostProxyRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.execute.<a href="src/fern/execute/client.py">put_proxy</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Proxies a downstream PUT request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
**Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.
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
from fern.execute import PutProxyRequestBodyZero

from fern import FernApi

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_downstream_url="YOUR_APIDECK_DOWNSTREAM_URL",
    apideck_downstream_authorization="YOUR_APIDECK_DOWNSTREAM_AUTHORIZATION",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
)
client.execute.put_proxy(
    request=PutProxyRequestBodyZero(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PutProxyRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.execute.<a href="src/fern/execute/client.py">delete_proxy</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Proxies a downstream DELETE request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
**Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_downstream_url="YOUR_APIDECK_DOWNSTREAM_URL",
    apideck_downstream_authorization="YOUR_APIDECK_DOWNSTREAM_AUTHORIZATION",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
)
client.execute.delete_proxy()

```
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

<details><summary><code>client.execute.<a href="src/fern/execute/client.py">patch_proxy</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Proxies a downstream PATCH request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
**Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.
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
from fern.execute import PatchProxyRequestBodyZero

from fern import FernApi

client = FernApi(
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_downstream_url="YOUR_APIDECK_DOWNSTREAM_URL",
    apideck_downstream_authorization="YOUR_APIDECK_DOWNSTREAM_AUTHORIZATION",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
)
client.execute.patch_proxy(
    request=PatchProxyRequestBodyZero(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PatchProxyRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

