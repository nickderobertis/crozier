# Reference
## Execute
<details><summary><code>client.execute.<a href="src/fern/execute/client.py">get_proxy</a>() -> typing.Any</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_service_id="<x-apideck-service-id>",
    apideck_downstream_url="<x-apideck-downstream-url>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.execute.<a href="src/fern/execute/client.py">post_proxy</a>(...) -> typing.Any</code></summary>
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
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.execute import PostProxyRequestBodyZero

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_service_id="<x-apideck-service-id>",
    apideck_downstream_url="<x-apideck-downstream-url>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.execute.<a href="src/fern/execute/client.py">put_proxy</a>(...) -> typing.Any</code></summary>
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
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.execute import PutProxyRequestBodyZero

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_service_id="<x-apideck-service-id>",
    apideck_downstream_url="<x-apideck-downstream-url>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.execute.<a href="src/fern/execute/client.py">delete_proxy</a>() -> typing.Any</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_service_id="<x-apideck-service-id>",
    apideck_downstream_url="<x-apideck-downstream-url>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
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

<details><summary><code>client.execute.<a href="src/fern/execute/client.py">patch_proxy</a>(...) -> typing.Any</code></summary>
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
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.execute import PatchProxyRequestBodyZero

client = FernApi(
    api_key="<value>",
    apideck_consumer_id="<x-apideck-consumer-id>",
    apideck_service_id="<x-apideck-service-id>",
    apideck_downstream_url="<x-apideck-downstream-url>",
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
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

