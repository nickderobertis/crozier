# Reference
## Connections
<details><summary><code>client.connections.<a href="src/fern/connections/client.py">authorize</a>(...) -> UnexpectedErrorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

__In most cases the authorize link is provided in the ``/connections`` endpoint. Normally you don't need to manually generate these links.__

Use this endpoint to authenticate a user with a connector. It will return a 301 redirect to the downstream connector endpoints.

Auth links will have a state parameter included to verify the validity of the request. This is the url your users will use to activate OAuth supported integration providers.

Vault handles the complete Authorization Code Grant Type Flow for you and will redirect you to the dynamic redirect uri you have appended to the url in case this is missing the default redirect uri you have configured for your Unify application.
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
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connections.authorize(
    service_id="pipedrive",
    application_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    state="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb25zdW1lcl9pZCI6InRlc3RfdXNlcl9pZCIsInVuaWZpZWRfYXBpIjoiZGVmYXVsdCIsInNlcnZpY2VfaWQiOiJ0ZWFtbGVhZGVyIiwiYXBwbGljYXRpb25faWQiOiIxMTExIiwiaWF0IjoxNjIyMTI2Nzg3fQ.97_pn1UAXc7mctXBdr15czUNO1jjdQ9sJUOIE_Myzbk",
    redirect_uri="http://example.com/integrations",
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

**service_id:** `str` — Service ID of the resource to return
    
</dd>
</dl>

<dl>
<dd>

**application_id:** `str` — Application ID of the resource to return
    
</dd>
</dl>

<dl>
<dd>

**state:** `str` — An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks.
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `str` — URL to redirect back to after authorization. When left empty the default configured redirect uri will be used.
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — One or more OAuth scopes to request from the connector. OAuth scopes control the set of resources and operations that are allowed after authorization. Refer to the connector's documentation for the available scopes.
    
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">callback</a>(...) -> UnexpectedErrorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint gets called after the triggering the authorize flow.

Callback links need a state and code parameter to verify the validity of the request.
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
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connections.callback(
    state="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb25zdW1lcl9pZCI6InRlc3RfdXNlcl9pZCIsInVuaWZpZWRfYXBpIjoiZGVmYXVsdCIsInNlcnZpY2VfaWQiOiJ0ZWFtbGVhZGVyIiwiYXBwbGljYXRpb25faWQiOiIxMTExIiwiaWF0IjoxNjIyMTI2Nzg3fQ.97_pn1UAXc7mctXBdr15czUNO1jjdQ9sJUOIE_Myzbk",
    code="g0ZGZmNjVmOWI",
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

**state:** `str` — An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks.
    
</dd>
</dl>

<dl>
<dd>

**code:** `str` — An authorization code from the connector which Apideck Vault will later exchange for an access token.
    
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">all</a>(...) -> GetConnectionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint includes all the configured integrations and contains the required assets
to build an integrations page where your users can install integrations.
OAuth2 supported integrations will contain authorize and revoke links to handle the authentication flows.
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
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connections.all_(
    api="crm",
    apideck_consumer_id="x-apideck-consumer-id",
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

**apideck_consumer_id:** `str` — ID of the consumer which you want to get or push data from
    
</dd>
</dl>

<dl>
<dd>

**api:** `typing.Optional[str]` — Scope results to Unified API
    
</dd>
</dl>

<dl>
<dd>

**configured:** `typing.Optional[bool]` — Scopes results to connections that have been configured or not
    
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">one</a>(...) -> GetConnectionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a connection
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
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connections.one(
    unified_api="crm",
    service_id="pipedrive",
    apideck_consumer_id="x-apideck-consumer-id",
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

**unified_api:** `str` — Unified API
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `str` — Service ID of the resource to return
    
</dd>
</dl>

<dl>
<dd>

**apideck_consumer_id:** `str` — ID of the consumer which you want to get or push data from
    
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">add</a>(...) -> CreateConnectionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an authorized connection
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
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connections.add(
    unified_api_="crm",
    service_id_="pipedrive",
    apideck_consumer_id="x-apideck-consumer-id",
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

**unified_api:** `str` — Unified API
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `str` — Service ID of the resource to return
    
</dd>
</dl>

<dl>
<dd>

**apideck_consumer_id:** `str` — ID of the consumer which you want to get or push data from
    
</dd>
</dl>

<dl>
<dd>

**request:** `Connection` 
    
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a connection
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
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connections.delete(
    unified_api="crm",
    service_id="pipedrive",
    apideck_consumer_id="x-apideck-consumer-id",
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

**unified_api:** `str` — Unified API
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `str` — Service ID of the resource to return
    
</dd>
</dl>

<dl>
<dd>

**apideck_consumer_id:** `str` — ID of the consumer which you want to get or push data from
    
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">update</a>(...) -> UpdateConnectionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a connection
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
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connections.update(
    unified_api_="crm",
    service_id_="pipedrive",
    apideck_consumer_id="x-apideck-consumer-id",
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

**unified_api:** `str` — Unified API
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `str` — Service ID of the resource to return
    
</dd>
</dl>

<dl>
<dd>

**apideck_consumer_id:** `str` — ID of the consumer which you want to get or push data from
    
</dd>
</dl>

<dl>
<dd>

**request:** `Connection` 
    
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">import</a>(...) -> CreateConnectionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import an authorized connection.
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
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connections.import_(
    unified_api="crm",
    service_id="pipedrive",
    apideck_consumer_id="x-apideck-consumer-id",
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

**unified_api:** `str` — Unified API
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `str` — Service ID of the resource to return
    
</dd>
</dl>

<dl>
<dd>

**apideck_consumer_id:** `str` — ID of the consumer which you want to get or push data from
    
</dd>
</dl>

<dl>
<dd>

**credentials:** `typing.Optional[ConnectionImportDataCredentials]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Attach your own consumer specific metadata
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[typing.Dict[str, typing.Any]]` — Connection settings. Values will persist to `form_fields` with corresponding id
    
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">token</a>(...) -> GetConnectionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an access token for a connection and store it in Vault. Currently only supported for connections with the client_credentials OAuth grant type.

Note that the access token will not be returned in the response. A 200 response code indicates a valid access token was stored on the connection.
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
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connections.token(
    unified_api="crm",
    service_id="pipedrive",
    apideck_consumer_id="x-apideck-consumer-id",
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

**unified_api:** `str` — Unified API
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `str` — Service ID of the resource to return
    
</dd>
</dl>

<dl>
<dd>

**apideck_consumer_id:** `str` — ID of the consumer which you want to get or push data from
    
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">connection_settings_all</a>(...) -> GetConnectionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint returns custom settings and their defaults required by connection for a given resource.
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
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connections.connection_settings_all(
    unified_api="crm",
    service_id="pipedrive",
    resource="leads",
    apideck_consumer_id="x-apideck-consumer-id",
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

**unified_api:** `str` — Unified API
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `str` — Service ID of the resource to return
    
</dd>
</dl>

<dl>
<dd>

**resource:** `str` — Resource Name
    
</dd>
</dl>

<dl>
<dd>

**apideck_consumer_id:** `str` — ID of the consumer which you want to get or push data from
    
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">connection_settings_update</a>(...) -> UpdateConnectionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update default values for a connection's resource settings
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
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connections.connection_settings_update(
    unified_api_="crm",
    service_id_="pipedrive",
    resource="leads",
    apideck_consumer_id="x-apideck-consumer-id",
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

**unified_api:** `str` — Unified API
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `str` — Service ID of the resource to return
    
</dd>
</dl>

<dl>
<dd>

**resource:** `str` — Resource Name
    
</dd>
</dl>

<dl>
<dd>

**apideck_consumer_id:** `str` — ID of the consumer which you want to get or push data from
    
</dd>
</dl>

<dl>
<dd>

**request:** `Connection` 
    
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">revoke</a>(...) -> UnexpectedErrorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

__In most cases the authorize link is provided in the ``/connections`` endpoint. Normally you don't need to manually generate these links.__

Use this endpoint to revoke an existing OAuth connector.

Auth links will have a state parameter included to verify the validity of the request. This is the url your users will use to activate OAuth supported integration providers.

Vault handles the complete revoke flow for you and will redirect you to the dynamic redirect uri you have appended to the url in case this is missing the default redirect uri you have configured for your Unify application.
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
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connections.revoke(
    service_id="pipedrive",
    application_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
    state="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb25zdW1lcl9pZCI6InRlc3RfdXNlcl9pZCIsInVuaWZpZWRfYXBpIjoiZGVmYXVsdCIsInNlcnZpY2VfaWQiOiJ0ZWFtbGVhZGVyIiwiYXBwbGljYXRpb25faWQiOiIxMTExIiwiaWF0IjoxNjIyMTI2Nzg3fQ.97_pn1UAXc7mctXBdr15czUNO1jjdQ9sJUOIE_Myzbk",
    redirect_uri="http://example.com/integrations",
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

**service_id:** `str` — Service ID of the resource to return
    
</dd>
</dl>

<dl>
<dd>

**application_id:** `str` — Application ID of the resource to return
    
</dd>
</dl>

<dl>
<dd>

**state:** `str` — An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks.
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `str` — URL to redirect back to after authorization. When left empty the default configured redirect uri will be used.
    
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

## Consumers
<details><summary><code>client.consumers.<a href="src/fern/consumers/client.py">all</a>(...) -> GetConsumersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint includes all application consumers, along with an aggregated count of requests made.
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
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.consumers.all_()

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

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
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

<details><summary><code>client.consumers.<a href="src/fern/consumers/client.py">add</a>(...) -> CreateConsumerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a consumer
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
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.consumers.add(
    consumer_id="test_consumer_id",
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

**request:** `Consumer` 
    
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

<details><summary><code>client.consumers.<a href="src/fern/consumers/client.py">one</a>(...) -> GetConsumerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Consumer detail including their aggregated counts with the connections they have authorized.
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
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.consumers.one(
    consumer_id="test_user_id",
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

**consumer_id:** `str` — ID of the consumer to return
    
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

<details><summary><code>client.consumers.<a href="src/fern/consumers/client.py">delete</a>(...) -> DeleteConsumerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete consumer and all their connections, including credentials.
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
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.consumers.delete(
    consumer_id="test_user_id",
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

**consumer_id:** `str` — ID of the consumer to return
    
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

<details><summary><code>client.consumers.<a href="src/fern/consumers/client.py">update</a>(...) -> UpdateConsumerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update consumer metadata such as name and email.
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
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.consumers.update(
    consumer_id="test_user_id",
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

**consumer_id:** `str` — ID of the consumer to return
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[ConsumerMetadata]` 
    
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

<details><summary><code>client.consumers.<a href="src/fern/consumers/client.py">consumer_request_counts_all</a>(...) -> ConsumerRequestCountsInDateRangeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get consumer request counts within a given datetime range.
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
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.consumers.consumer_request_counts_all(
    consumer_id="test_user_id",
    start_datetime="2021-05-01T12:00:00.000Z",
    end_datetime="2021-05-30T12:00:00.000Z",
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

**consumer_id:** `str` — ID of the consumer to return
    
</dd>
</dl>

<dl>
<dd>

**start_datetime:** `str` — Scopes results to requests that happened after datetime
    
</dd>
</dl>

<dl>
<dd>

**end_datetime:** `str` — Scopes results to requests that happened before datetime
    
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

## Logs
<details><summary><code>client.logs.<a href="src/fern/logs/client.py">all</a>(...) -> GetLogsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint includes all consumer request logs.
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
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.logs.all_(
    apideck_consumer_id="x-apideck-consumer-id",
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

**apideck_consumer_id:** `str` — ID of the consumer which you want to get or push data from
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[LogsFilter]` — Filter results
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
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

## Sessions
<details><summary><code>client.sessions.<a href="src/fern/sessions/client.py">create</a>(...) -> CreateSessionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Making a POST request to this endpoint will initiate a Hosted Vault session. Redirect the consumer to the returned
URL to allow temporary access to manage their integrations and settings.

Note: This is a short lived token that will expire after 1 hour (TTL: 3600).
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
    apideck_app_id="<x-apideck-app-id>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sessions.create(
    apideck_consumer_id="x-apideck-consumer-id",
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

**apideck_consumer_id:** `str` — ID of the consumer which you want to get or push data from
    
</dd>
</dl>

<dl>
<dd>

**consumer_metadata:** `typing.Optional[ConsumerMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_consumer_settings:** `typing.Optional[typing.Dict[str, typing.Any]]` — Custom consumer settings that are passed as part of the session.
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `typing.Optional[str]` — The URL to redirect the user to after the session has been configured.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[SessionSettings]` — Settings to change the way the Vault is displayed.
    
</dd>
</dl>

<dl>
<dd>

**theme:** `typing.Optional[SessionTheme]` — Theming options to change the look and feel of Vault.
    
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

