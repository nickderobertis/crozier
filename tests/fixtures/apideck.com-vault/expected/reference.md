# Reference
## Connections
<details><summary><code>client.connections.<a href="src/fern/connections/client.py">authorize</a>(...)</code></summary>
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

client = FernApi(
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">callback</a>(...)</code></summary>
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

client = FernApi(
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">all_</a>(...)</code></summary>
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

client = FernApi(
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
)
client.connections.all_(
    apideck_consumer_id="x-apideck-consumer-id",
    api="crm",
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">one</a>(...)</code></summary>
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

client = FernApi(
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">add</a>(...)</code></summary>
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

client = FernApi(
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
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

**unified_api_:** `str` — Unified API
    
</dd>
</dl>

<dl>
<dd>

**service_id_:** `str` — Service ID of the resource to return
    
</dd>
</dl>

<dl>
<dd>

**apideck_consumer_id:** `str` — ID of the consumer which you want to get or push data from
    
</dd>
</dl>

<dl>
<dd>

**auth_type:** `typing.Optional[AuthType]` 
    
</dd>
</dl>

<dl>
<dd>

**authorize_url:** `typing.Optional[str]` — The OAuth redirect URI. Redirect your users to this URI to let them authorize your app in the connector's UI. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.
    
</dd>
</dl>

<dl>
<dd>

**configurable_resources:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[typing.Sequence[ConnectionConfigurationItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the connection is enabled or not. You can enable or disable a connection using the Update Connection API.
    
</dd>
</dl>

<dl>
<dd>

**form_fields:** `typing.Optional[typing.Sequence[FormField]]` — The settings that are wanted to create a connection.
    
</dd>
</dl>

<dl>
<dd>

**has_guide:** `typing.Optional[bool]` — Whether the connector has a guide available in the developer docs or not (https://docs.apideck.com/connectors/{service_id}/docs/consumer+connection).
    
</dd>
</dl>

<dl>
<dd>

**icon:** `typing.Optional[str]` — A visual icon of the connection, that will be shown in the Vault
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — The unique identifier of the connection.
    
</dd>
</dl>

<dl>
<dd>

**integration_state:** `typing.Optional[IntegrationState]` 
    
</dd>
</dl>

<dl>
<dd>

**logo:** `typing.Optional[str]` — The logo of the connection, that will be shown in the Vault
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Attach your own consumer specific metadata
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the connection
    
</dd>
</dl>

<dl>
<dd>

**oauth_grant_type:** `typing.Optional[OAuthGrantType]` 
    
</dd>
</dl>

<dl>
<dd>

**resource_schema_support:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**resource_settings_support:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**revoke_url:** `typing.Optional[str]` — The OAuth revoke URI. Redirect your users to this URI to revoke this connection. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `typing.Optional[str]` — The ID of the service this connection belongs to.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Connection settings. Values will persist to `form_fields` with corresponding id
    
</dd>
</dl>

<dl>
<dd>

**settings_required_for_authorization:** `typing.Optional[typing.Sequence[str]]` — List of settings that are required to be configured on integration before authorization can occur
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[ConnectionState]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ConnectionStatus]` — Status of the connection.
    
</dd>
</dl>

<dl>
<dd>

**subscriptions:** `typing.Optional[typing.Sequence[WebhookSubscription]]` 
    
</dd>
</dl>

<dl>
<dd>

**tag_line:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**unified_api:** `typing.Optional[str]` — The unified API category where the connection belongs to.
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**validation_support:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` — The website URL of the connection
    
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

client = FernApi(
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">update</a>(...)</code></summary>
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

client = FernApi(
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
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

**unified_api_:** `str` — Unified API
    
</dd>
</dl>

<dl>
<dd>

**service_id_:** `str` — Service ID of the resource to return
    
</dd>
</dl>

<dl>
<dd>

**apideck_consumer_id:** `str` — ID of the consumer which you want to get or push data from
    
</dd>
</dl>

<dl>
<dd>

**auth_type:** `typing.Optional[AuthType]` 
    
</dd>
</dl>

<dl>
<dd>

**authorize_url:** `typing.Optional[str]` — The OAuth redirect URI. Redirect your users to this URI to let them authorize your app in the connector's UI. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.
    
</dd>
</dl>

<dl>
<dd>

**configurable_resources:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[typing.Sequence[ConnectionConfigurationItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the connection is enabled or not. You can enable or disable a connection using the Update Connection API.
    
</dd>
</dl>

<dl>
<dd>

**form_fields:** `typing.Optional[typing.Sequence[FormField]]` — The settings that are wanted to create a connection.
    
</dd>
</dl>

<dl>
<dd>

**has_guide:** `typing.Optional[bool]` — Whether the connector has a guide available in the developer docs or not (https://docs.apideck.com/connectors/{service_id}/docs/consumer+connection).
    
</dd>
</dl>

<dl>
<dd>

**icon:** `typing.Optional[str]` — A visual icon of the connection, that will be shown in the Vault
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — The unique identifier of the connection.
    
</dd>
</dl>

<dl>
<dd>

**integration_state:** `typing.Optional[IntegrationState]` 
    
</dd>
</dl>

<dl>
<dd>

**logo:** `typing.Optional[str]` — The logo of the connection, that will be shown in the Vault
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Attach your own consumer specific metadata
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the connection
    
</dd>
</dl>

<dl>
<dd>

**oauth_grant_type:** `typing.Optional[OAuthGrantType]` 
    
</dd>
</dl>

<dl>
<dd>

**resource_schema_support:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**resource_settings_support:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**revoke_url:** `typing.Optional[str]` — The OAuth revoke URI. Redirect your users to this URI to revoke this connection. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `typing.Optional[str]` — The ID of the service this connection belongs to.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Connection settings. Values will persist to `form_fields` with corresponding id
    
</dd>
</dl>

<dl>
<dd>

**settings_required_for_authorization:** `typing.Optional[typing.Sequence[str]]` — List of settings that are required to be configured on integration before authorization can occur
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[ConnectionState]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ConnectionStatus]` — Status of the connection.
    
</dd>
</dl>

<dl>
<dd>

**subscriptions:** `typing.Optional[typing.Sequence[WebhookSubscription]]` 
    
</dd>
</dl>

<dl>
<dd>

**tag_line:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**unified_api:** `typing.Optional[str]` — The unified API category where the connection belongs to.
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**validation_support:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` — The website URL of the connection
    
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">import_</a>(...)</code></summary>
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

client = FernApi(
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
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

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Attach your own consumer specific metadata
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Connection settings. Values will persist to `form_fields` with corresponding id
    
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">token</a>(...)</code></summary>
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

client = FernApi(
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">connection_settings_all</a>(...)</code></summary>
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

client = FernApi(
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">connection_settings_update</a>(...)</code></summary>
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

client = FernApi(
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
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

**unified_api_:** `str` — Unified API
    
</dd>
</dl>

<dl>
<dd>

**service_id_:** `str` — Service ID of the resource to return
    
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

**auth_type:** `typing.Optional[AuthType]` 
    
</dd>
</dl>

<dl>
<dd>

**authorize_url:** `typing.Optional[str]` — The OAuth redirect URI. Redirect your users to this URI to let them authorize your app in the connector's UI. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.
    
</dd>
</dl>

<dl>
<dd>

**configurable_resources:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[typing.Sequence[ConnectionConfigurationItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the connection is enabled or not. You can enable or disable a connection using the Update Connection API.
    
</dd>
</dl>

<dl>
<dd>

**form_fields:** `typing.Optional[typing.Sequence[FormField]]` — The settings that are wanted to create a connection.
    
</dd>
</dl>

<dl>
<dd>

**has_guide:** `typing.Optional[bool]` — Whether the connector has a guide available in the developer docs or not (https://docs.apideck.com/connectors/{service_id}/docs/consumer+connection).
    
</dd>
</dl>

<dl>
<dd>

**icon:** `typing.Optional[str]` — A visual icon of the connection, that will be shown in the Vault
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — The unique identifier of the connection.
    
</dd>
</dl>

<dl>
<dd>

**integration_state:** `typing.Optional[IntegrationState]` 
    
</dd>
</dl>

<dl>
<dd>

**logo:** `typing.Optional[str]` — The logo of the connection, that will be shown in the Vault
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Attach your own consumer specific metadata
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the connection
    
</dd>
</dl>

<dl>
<dd>

**oauth_grant_type:** `typing.Optional[OAuthGrantType]` 
    
</dd>
</dl>

<dl>
<dd>

**resource_schema_support:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**resource_settings_support:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**revoke_url:** `typing.Optional[str]` — The OAuth revoke URI. Redirect your users to this URI to revoke this connection. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `typing.Optional[str]` — The ID of the service this connection belongs to.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Connection settings. Values will persist to `form_fields` with corresponding id
    
</dd>
</dl>

<dl>
<dd>

**settings_required_for_authorization:** `typing.Optional[typing.Sequence[str]]` — List of settings that are required to be configured on integration before authorization can occur
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[ConnectionState]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ConnectionStatus]` — Status of the connection.
    
</dd>
</dl>

<dl>
<dd>

**subscriptions:** `typing.Optional[typing.Sequence[WebhookSubscription]]` 
    
</dd>
</dl>

<dl>
<dd>

**tag_line:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**unified_api:** `typing.Optional[str]` — The unified API category where the connection belongs to.
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**validation_support:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` — The website URL of the connection
    
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">revoke</a>(...)</code></summary>
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

client = FernApi(
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
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
<details><summary><code>client.consumers.<a href="src/fern/consumers/client.py">all_</a>(...)</code></summary>
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

client = FernApi(
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.consumers.<a href="src/fern/consumers/client.py">add</a>(...)</code></summary>
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

client = FernApi(
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
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

**consumer_id:** `ConsumerId` 
    
</dd>
</dl>

<dl>
<dd>

**aggregated_request_count:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**application_id:** `typing.Optional[str]` — ID of your Apideck Application
    
</dd>
</dl>

<dl>
<dd>

**connections:** `typing.Optional[typing.Sequence[ConsumerConnection]]` 
    
</dd>
</dl>

<dl>
<dd>

**created:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[ConsumerMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**modified:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_count_updated:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_counts:** `typing.Optional[RequestCountAllocation]` 
    
</dd>
</dl>

<dl>
<dd>

**services:** `typing.Optional[typing.Sequence[str]]` 
    
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

<details><summary><code>client.consumers.<a href="src/fern/consumers/client.py">one</a>(...)</code></summary>
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

client = FernApi(
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.consumers.<a href="src/fern/consumers/client.py">delete</a>(...)</code></summary>
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

client = FernApi(
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.consumers.<a href="src/fern/consumers/client.py">update</a>(...)</code></summary>
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

client = FernApi(
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.consumers.<a href="src/fern/consumers/client.py">consumer_request_counts_all</a>(...)</code></summary>
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

client = FernApi(
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
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
<details><summary><code>client.logs.<a href="src/fern/logs/client.py">all_</a>(...)</code></summary>
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

client = FernApi(
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
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
<details><summary><code>client.sessions.<a href="src/fern/sessions/client.py">create</a>(...)</code></summary>
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

client = FernApi(
    apideck_app_id="YOUR_APIDECK_APP_ID",
    api_key="YOUR_API_KEY",
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

**custom_consumer_settings:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Custom consumer settings that are passed as part of the session.
    
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

