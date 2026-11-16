# Reference
## AppV1
<details><summary><code>client.app_v1.<a href="src/fern/app_v1/client.py#L33-L59">get_apps</a>() -> typing.List[ApplicationWithLatestDeploymentAndBuild]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an unsorted list of your organization’s [applications](https://hathora.dev/docs/concepts/hathora-entities#application). An application is uniquely identified by an `appId`.
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

client.app_v1.get_apps()

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

<details><summary><code>client.app_v1.<a href="src/fern/app_v1/client.py#L61-L100">create_app</a>(...) -> Application</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new [application](https://hathora.dev/docs/concepts/hathora-entities#application).
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
from fern import FernApi, AuthConfiguration
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.app_v1.create_app(
    auth_configuration=AuthConfiguration(),
    app_name="minecraft",
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

**request:** `AppConfig` 
    
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

<details><summary><code>client.app_v1.<a href="src/fern/app_v1/client.py#L102-L145">update_app</a>(...) -> Application</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update data for an existing [application](https://hathora.dev/docs/concepts/hathora-entities#application) using `appId`.
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
from fern import FernApi, AuthConfiguration
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.app_v1.update_app(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    auth_configuration=AuthConfiguration(),
    app_name="minecraft",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `AppConfig` 
    
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

<details><summary><code>client.app_v1.<a href="src/fern/app_v1/client.py#L147-L175">get_app_info</a>(...) -> Application</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details for an [application](https://hathora.dev/docs/concepts/hathora-entities#application) using `appId`.
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

client.app_v1.get_app_info(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
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

**app_id:** `AppId` 
    
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

<details><summary><code>client.app_v1.<a href="src/fern/app_v1/client.py#L177-L204">delete_app</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an [application](https://hathora.dev/docs/concepts/hathora-entities#application) using `appId`. Your organization will lose access to this application.
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

client.app_v1.delete_app(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
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

**app_id:** `AppId` 
    
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

## AuthV1
<details><summary><code>client.auth_v1.<a href="src/fern/auth_v1/client.py#L30-L60">login_anonymous</a>(...) -> LoginResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a unique player token for an anonymous user.
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

client.auth_v1.login_anonymous(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
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

**app_id:** `AppId` 
    
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

<details><summary><code>client.auth_v1.<a href="src/fern/auth_v1/client.py#L62-L96">login_nickname</a>(...) -> LoginResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a unique player token with a specified nickname for a user.
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

client.auth_v1.login_nickname(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    nickname="squiddytwoshoes",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**nickname:** `str` — An alias to represent a player.
    
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

<details><summary><code>client.auth_v1.<a href="src/fern/auth_v1/client.py#L98-L132">login_google</a>(...) -> LoginResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a unique player token using a Google-signed OIDC `idToken`.
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

client.auth_v1.login_google(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    id_token="eyJhbGciOiJSUzI1NiIsImtpZCI6ImZkNDhhNzUxMzhkOWQ0OGYwYWE2MzVlZjU2OWM0ZTE5NmY3YWU4ZDYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiODQ4NDEyODI2Nzg4LW00bXNyYjZxNDRkbTJ1ZTNrZ3Z1aTBmcTdrZGE1NWxzLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiODQ4NDEyODI2Nzg4LW00bXNyYjZxNDRkbTJ1ZTNrZ3Z1aTBmcTdrZGE1NWxzLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTE0NTQyMzMwNzI3MTU2MTMzNzc2IiwiZW1haWwiOiJocGFdkeivmeuzQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhdF9oYXNoIjoidno1NGhhdTNxbnVR",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**id_token:** `str` — A Google-signed OIDC ID token representing a player's authenticated identity. Learn how to get an `idToken` [here](https://cloud.google.com/docs/authentication/get-id-token).
    
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

## BillingV1
<details><summary><code>client.billing_v1.<a href="src/fern/billing_v1/client.py#L30-L52">get_balance</a>() -> float</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.billing_v1.get_balance()

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

<details><summary><code>client.billing_v1.<a href="src/fern/billing_v1/client.py#L54-L76">get_payment_method</a>() -> PaymentMethod</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.billing_v1.get_payment_method()

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

<details><summary><code>client.billing_v1.<a href="src/fern/billing_v1/client.py#L78-L108">init_stripe_customer_portal_url</a>(...) -> str</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.billing_v1.init_stripe_customer_portal_url(
    return_url="returnUrl",
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

**return_url:** `str` 
    
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

<details><summary><code>client.billing_v1.<a href="src/fern/billing_v1/client.py#L110-L132">get_invoices</a>() -> typing.List[Invoice]</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.billing_v1.get_invoices()

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

## BuildV1
<details><summary><code>client.build_v1.<a href="src/fern/build_v1/client.py#L33-L63">get_builds</a>(...) -> typing.List[Build]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of [builds](https://hathora.dev/docs/concepts/hathora-entities#build) for an [application](https://hathora.dev/docs/concepts/hathora-entities#application).
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

client.build_v1.get_builds(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
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

**app_id:** `AppId` 
    
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

<details><summary><code>client.build_v1.<a href="src/fern/build_v1/client.py#L65-L98">get_build_info</a>(...) -> Build</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details for a [build](https://hathora.dev/docs/concepts/hathora-entities#build).
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

client.build_v1.get_build_info(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    build_id=1,
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**build_id:** `BuildId` 
    
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

<details><summary><code>client.build_v1.<a href="src/fern/build_v1/client.py#L100-L136">create_build</a>(...) -> Build</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new [build](https://hathora.dev/docs/concepts/hathora-entities#build). Responds with a `buildId` that you must pass to [`RunBuild()`](https://hathora.dev/api#tag/BuildV1/operation/RunBuild) to build the game server artifact. You can optionally pass in a `buildTag` to associate an external version with a build.
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

client.build_v1.create_build(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**build_tag:** `typing.Optional[BuildTag]` 
    
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

<details><summary><code>client.build_v1.<a href="src/fern/build_v1/client.py#L138-L167">run_build</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Builds a game server artifact from a tarball you provide. Pass in the `buildId` generated from [`CreateBuild()`](https://hathora.dev/api#tag/BuildV1/operation/CreateBuild).
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
client.build_v1.run_build(...)
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**build_id:** `BuildId` 
    
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

<details><summary><code>client.build_v1.<a href="src/fern/build_v1/client.py#L169-L201">delete_build</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a [build](https://hathora.dev/docs/concepts/hathora-entities#build). All associated metadata is deleted.
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

client.build_v1.delete_build(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    build_id=1,
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**build_id:** `BuildId` 
    
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

## DeploymentV1
<details><summary><code>client.deployment_v1.<a href="src/fern/deployment_v1/client.py#L37-L67">get_deployments_deprecated</a>(...) -> typing.List[Deployment]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of [deployments](https://hathora.dev/docs/concepts/hathora-entities#deployment) for an [application](https://hathora.dev/docs/concepts/hathora-entities#application).
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

client.deployment_v1.get_deployments_deprecated(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
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

**app_id:** `AppId` 
    
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

<details><summary><code>client.deployment_v1.<a href="src/fern/deployment_v1/client.py#L69-L99">get_latest_deployment_deprecated</a>(...) -> Deployment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the latest [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment) for an [application](https://hathora.dev/docs/concepts/hathora-entities#application).
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

client.deployment_v1.get_latest_deployment_deprecated(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
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

**app_id:** `AppId` 
    
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

<details><summary><code>client.deployment_v1.<a href="src/fern/deployment_v1/client.py#L101-L136">get_deployment_info_deprecated</a>(...) -> Deployment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details for a [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment).
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

client.deployment_v1.get_deployment_info_deprecated(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    deployment_id=1,
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `DeploymentId` 
    
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

<details><summary><code>client.deployment_v1.<a href="src/fern/deployment_v1/client.py#L138-L224">create_deployment_deprecated</a>(...) -> Deployment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment). Creating a new deployment means all new rooms created will use the latest deployment configuration, but existing games in progress will not be affected.
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
from fern import FernApi, PlanName, TransportType
from fern.environment import FernApiEnvironment
from fern.deployment_v1 import DeploymentConfigEnvItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.deployment_v1.create_deployment_deprecated(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    build_id=1,
    env=[
        DeploymentConfigEnvItem(
            value="TRUE",
            name="EULA",
        )
    ],
    rooms_per_process=3,
    plan_name=PlanName.TINY,
    transport_type=TransportType.TCP,
    container_port=4000,
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**build_id:** `BuildId` 
    
</dd>
</dl>

<dl>
<dd>

**env:** `typing.List[DeploymentConfigEnvItem]` — The environment variable that our process will have access to at runtime.
    
</dd>
</dl>

<dl>
<dd>

**rooms_per_process:** `NumRoomsPerProcess` 
    
</dd>
</dl>

<dl>
<dd>

**plan_name:** `PlanName` 
    
</dd>
</dl>

<dl>
<dd>

**transport_type:** `TransportType` 
    
</dd>
</dl>

<dl>
<dd>

**container_port:** `int` — Default port the server listens on.
    
</dd>
</dl>

<dl>
<dd>

**idle_timeout_enabled:** `typing.Optional[bool]` 

Option to shut down processes that have had no new connections or rooms
for five minutes.
    
</dd>
</dl>

<dl>
<dd>

**additional_container_ports:** `typing.Optional[typing.List[ContainerPort]]` — Additional ports your server listens on.
    
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

## DeploymentV2
<details><summary><code>client.deployment_v2.<a href="src/fern/deployment_v2/client.py#L36-L66">get_deployments</a>(...) -> typing.List[DeploymentV2]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of [deployments](https://hathora.dev/docs/concepts/hathora-entities#deployment) for an [application](https://hathora.dev/docs/concepts/hathora-entities#application).
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

client.deployment_v2.get_deployments(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
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

**app_id:** `AppId` 
    
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

<details><summary><code>client.deployment_v2.<a href="src/fern/deployment_v2/client.py#L68-L98">get_latest_deployment</a>(...) -> DeploymentV2</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the latest [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment) for an [application](https://hathora.dev/docs/concepts/hathora-entities#application).
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

client.deployment_v2.get_latest_deployment(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
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

**app_id:** `AppId` 
    
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

<details><summary><code>client.deployment_v2.<a href="src/fern/deployment_v2/client.py#L100-L133">get_deployment_info</a>(...) -> DeploymentV2</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details for a [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment).
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

client.deployment_v2.get_deployment_info(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    deployment_id=1,
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `DeploymentId` 
    
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

<details><summary><code>client.deployment_v2.<a href="src/fern/deployment_v2/client.py#L135-L229">create_deployment</a>(...) -> DeploymentV2</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment). Creating a new deployment means all new rooms created will use the latest deployment configuration, but existing games in progress will not be affected.
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
from fern import FernApi, TransportType
from fern.environment import FernApiEnvironment
from fern.deployment_v2 import DeploymentConfigV2EnvItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.deployment_v2.create_deployment(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    build_id=1,
    idle_timeout_enabled=True,
    env=[
        DeploymentConfigV2EnvItem(
            value="TRUE",
            name="EULA",
        )
    ],
    rooms_per_process=3,
    transport_type=TransportType.TCP,
    container_port=4000,
    requested_memory_mb=1024,
    requested_cpu=0.5,
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**build_id:** `BuildId` 
    
</dd>
</dl>

<dl>
<dd>

**idle_timeout_enabled:** `bool` 

Option to shut down processes that have had no new connections or rooms
for five minutes.
    
</dd>
</dl>

<dl>
<dd>

**env:** `typing.List[DeploymentConfigV2EnvItem]` — The environment variable that our process will have access to at runtime.
    
</dd>
</dl>

<dl>
<dd>

**rooms_per_process:** `NumRoomsPerProcess` 
    
</dd>
</dl>

<dl>
<dd>

**transport_type:** `TransportType` 
    
</dd>
</dl>

<dl>
<dd>

**container_port:** `int` — Default port the server listens on.
    
</dd>
</dl>

<dl>
<dd>

**requested_memory_mb:** `float` — The amount of memory allocated to your process.
    
</dd>
</dl>

<dl>
<dd>

**requested_cpu:** `float` — The number of cores allocated to your process.
    
</dd>
</dl>

<dl>
<dd>

**additional_container_ports:** `typing.Optional[typing.List[ContainerPort]]` — Additional ports your server listens on.
    
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

## DiscoveryV1
<details><summary><code>client.discovery_v1.<a href="src/fern/discovery_v1/client.py#L26-L52">get_ping_service_endpoints</a>() -> DiscoveryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of all regions with a host and port that a client can directly ping. Open a websocket connection to `wss://<host>:<port>/ws` and send a packet. To calculate ping, measure the time it takes to get an echo packet back.
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

client.discovery_v1.get_ping_service_endpoints()

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

## LobbyV1
<details><summary><code>client.lobby_v1.<a href="src/fern/lobby_v1/client.py#L29-L68">create_private_lobby_deprecated</a>(...) -> RoomId</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.lobby_v1.create_private_lobby_deprecated(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[Region]` 
    
</dd>
</dl>

<dl>
<dd>

**local:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.lobby_v1.<a href="src/fern/lobby_v1/client.py#L70-L109">create_public_lobby_deprecated</a>(...) -> RoomId</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.lobby_v1.create_public_lobby_deprecated(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[Region]` 
    
</dd>
</dl>

<dl>
<dd>

**local:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.lobby_v1.<a href="src/fern/lobby_v1/client.py#L111-L150">list_active_public_lobbies_deprecated_v1</a>(...) -> typing.List[Lobby]</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.lobby_v1.list_active_public_lobbies_deprecated_v1(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**local:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[Region]` 
    
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

## LobbyV2
<details><summary><code>client.lobby_v2.<a href="src/fern/lobby_v2/client.py#L34-L79">create_private_lobby</a>(...) -> Lobby</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Region
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.lobby_v2.create_private_lobby(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    room_id="2swovpy1fnunu",
    initial_config={
        "key": "value"
    },
    region=Region.SEATTLE,
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**initial_config:** `LobbyInitialConfig` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `Region` 
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `typing.Optional[RoomId]` 
    
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

<details><summary><code>client.lobby_v2.<a href="src/fern/lobby_v2/client.py#L81-L126">create_public_lobby</a>(...) -> Lobby</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Region
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.lobby_v2.create_public_lobby(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    room_id="2swovpy1fnunu",
    initial_config={
        "key": "value"
    },
    region=Region.SEATTLE,
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**initial_config:** `LobbyInitialConfig` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `Region` 
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `typing.Optional[RoomId]` 
    
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

<details><summary><code>client.lobby_v2.<a href="src/fern/lobby_v2/client.py#L128-L173">create_local_lobby</a>(...) -> Lobby</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Region
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.lobby_v2.create_local_lobby(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    room_id="2swovpy1fnunu",
    initial_config={
        "key": "value"
    },
    region=Region.SEATTLE,
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**initial_config:** `LobbyInitialConfig` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `Region` 
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `typing.Optional[RoomId]` 
    
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

<details><summary><code>client.lobby_v2.<a href="src/fern/lobby_v2/client.py#L175-L231">create_lobby_deprecated</a>(...) -> Lobby</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new lobby for an [application](https://hathora.dev/docs/concepts/hathora-entities#application). A lobby object is a wrapper around a [room](https://hathora.dev/docs/concepts/hathora-entities#room) object. With a lobby, you get additional functionality like configuring the visibility of the room, managing the state of a match, and retrieving a list of public lobbies to display to players.
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
from fern import FernApi, LobbyVisibility, Region
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.lobby_v2.create_lobby_deprecated(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    room_id="2swovpy1fnunu",
    visibility=LobbyVisibility.PRIVATE,
    initial_config={
        "key": "value"
    },
    region=Region.SEATTLE,
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**visibility:** `LobbyVisibility` 
    
</dd>
</dl>

<dl>
<dd>

**initial_config:** `LobbyInitialConfig` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `Region` 
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `typing.Optional[RoomId]` 
    
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

<details><summary><code>client.lobby_v2.<a href="src/fern/lobby_v2/client.py#L233-L272">list_active_public_lobbies_deprecated_v2</a>(...) -> typing.List[Lobby]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all active lobbies for a an [application](https://hathora.dev/docs/concepts/hathora-entities#application). Filter by optionally passing in a `region`. Use this endpoint to display all public lobbies that a player can join in the game client.
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

client.lobby_v2.list_active_public_lobbies_deprecated_v2(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[Region]` — Region to filter by. If omitted, active public lobbies in all regions will be returned.
    
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

<details><summary><code>client.lobby_v2.<a href="src/fern/lobby_v2/client.py#L274-L307">get_lobby_info</a>(...) -> Lobby</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details for a lobby.
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

client.lobby_v2.get_lobby_info(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    room_id="2swovpy1fnunu",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `RoomId` 
    
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

<details><summary><code>client.lobby_v2.<a href="src/fern/lobby_v2/client.py#L309-L351">set_lobby_state</a>(...) -> Lobby</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the state of a lobby. State is intended to be set by the server and must be smaller than 1MB. Use this endpoint to store match data like live player count to enforce max number of clients or persist end-game data (i.e. winner or final scores).
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

client.lobby_v2.set_lobby_state(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    room_id="2swovpy1fnunu",
    state={
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `RoomId` 
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Dict[str, typing.Any]` — JSON blob to store metadata for a room. Must be smaller than 1MB.
    
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

## LobbyV3
<details><summary><code>client.lobby_v3.<a href="src/fern/lobby_v3/client.py#L35-L95">create_lobby</a>(...) -> LobbyV3</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new lobby for an [application](https://hathora.dev/docs/concepts/hathora-entities#application). A lobby object is a wrapper around a [room](https://hathora.dev/docs/concepts/hathora-entities#room) object. With a lobby, you get additional functionality like configuring the visibility of the room, managing the state of a match, and retrieving a list of public lobbies to display to players.
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
from fern import FernApi, LobbyVisibility, Region
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.lobby_v3.create_lobby(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    short_code="LFG4",
    room_id="2swovpy1fnunu",
    visibility=LobbyVisibility.PRIVATE,
    region=Region.SEATTLE,
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**visibility:** `LobbyVisibility` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `Region` 
    
</dd>
</dl>

<dl>
<dd>

**short_code:** `typing.Optional[ShortCode]` 
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `typing.Optional[RoomId]` 
    
</dd>
</dl>

<dl>
<dd>

**room_config:** `typing.Optional[RoomConfig]` 
    
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

<details><summary><code>client.lobby_v3.<a href="src/fern/lobby_v3/client.py#L97-L134">list_active_public_lobbies</a>(...) -> typing.List[LobbyV3]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all active lobbies for a given [application](https://hathora.dev/docs/concepts/hathora-entities#application). Filter the array by optionally passing in a `region`. Use this endpoint to display all public lobbies that a player can join in the game client.
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

client.lobby_v3.list_active_public_lobbies(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[Region]` — If omitted, active public lobbies in all regions will be returned.
    
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

<details><summary><code>client.lobby_v3.<a href="src/fern/lobby_v3/client.py#L136-L169">get_lobby_info_by_room_id</a>(...) -> LobbyV3</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details for a lobby.
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

client.lobby_v3.get_lobby_info_by_room_id(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    room_id="2swovpy1fnunu",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `RoomId` 
    
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

<details><summary><code>client.lobby_v3.<a href="src/fern/lobby_v3/client.py#L171-L204">get_lobby_info_by_short_code</a>(...) -> LobbyV3</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details for a lobby. If 2 or more lobbies have the same `shortCode`, then the most recently created lobby will be returned.
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

client.lobby_v3.get_lobby_info_by_short_code(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    short_code="LFG4",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**short_code:** `ShortCode` 
    
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

## LogV1
<details><summary><code>client.log_v1.<a href="src/fern/log_v1/client.py#L31-L75">get_logs_for_app</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a stream of logs for an [application](https://hathora.dev/docs/concepts/hathora-entities#application) using `appId`.
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

client.log_v1.get_logs_for_app(
    app_id="appId",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**follow:** `typing.Optional[LogsFollow]` 
    
</dd>
</dl>

<dl>
<dd>

**tail_lines:** `typing.Optional[TailLines]` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[Region]` 
    
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

<details><summary><code>client.log_v1.<a href="src/fern/log_v1/client.py#L77-L122">get_logs_for_process</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a stream of logs for a [process](https://hathora.dev/docs/concepts/hathora-entities#process) using `appId` and `processId`.
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

client.log_v1.get_logs_for_process(
    app_id="appId",
    process_id="processId",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `ProcessId` 
    
</dd>
</dl>

<dl>
<dd>

**follow:** `typing.Optional[LogsFollow]` 
    
</dd>
</dl>

<dl>
<dd>

**tail_lines:** `typing.Optional[TailLines]` 
    
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

<details><summary><code>client.log_v1.<a href="src/fern/log_v1/client.py#L124-L157">download_log_for_process</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download entire log file for a stopped process.
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

client.log_v1.download_log_for_process(
    app_id="appId",
    process_id="processId",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `ProcessId` 
    
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

<details><summary><code>client.log_v1.<a href="src/fern/log_v1/client.py#L159-L204">get_logs_for_deployment</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a stream of logs for a [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment) using `appId` and `deploymentId`.
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

client.log_v1.get_logs_for_deployment(
    app_id="appId",
    deployment_id=1,
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `DeploymentId` 
    
</dd>
</dl>

<dl>
<dd>

**follow:** `typing.Optional[LogsFollow]` 
    
</dd>
</dl>

<dl>
<dd>

**tail_lines:** `typing.Optional[TailLines]` 
    
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

## ManagementV1
<details><summary><code>client.management_v1.<a href="src/fern/management_v1/client.py#L29-L57">send_verification_email</a>(...) -> VerificationEmailResponse</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.management_v1.send_verification_email(
    user_id="userId",
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

**user_id:** `str` 
    
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

## MetricsV1
<details><summary><code>client.metrics_v1.<a href="src/fern/metrics_v1/client.py#L30-L84">get_metrics</a>(...) -> MetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get metrics for a [process](https://hathora.dev/docs/concepts/hathora-entities#process) using `appId` and `processId`.
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

client.metrics_v1.get_metrics(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `ProcessId` 
    
</dd>
</dl>

<dl>
<dd>

**metrics:** `typing.Optional[typing.Union[MetricName, typing.Sequence[MetricName]]]` — Available metrics to query over time.
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[float]` — Unix timestamp. Default is current time.
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[float]` — Unix timestamp. Default is -1 hour from `end`.
    
</dd>
</dl>

<dl>
<dd>

**step:** `typing.Optional[MetricsStep]` 
    
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

## ProcessesV1
<details><summary><code>client.processes_v1.<a href="src/fern/processes_v1/client.py#L30-L66">get_running_processes</a>(...) -> typing.List[ProcessWithRooms]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve 10 most recently started [process](https://hathora.dev/docs/concepts/hathora-entities#process) objects for an [application](https://hathora.dev/docs/concepts/hathora-entities#application). Filter the array by optionally passing in a `region`.
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

client.processes_v1.get_running_processes(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[Region]` 
    
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

<details><summary><code>client.processes_v1.<a href="src/fern/processes_v1/client.py#L68-L104">get_stopped_processes</a>(...) -> typing.List[Process]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve 10 most recently stopped [process](https://hathora.dev/docs/concepts/hathora-entities#process) objects for an [application](https://hathora.dev/docs/concepts/hathora-entities#application). Filter the array by optionally passing in a `region`.
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

client.processes_v1.get_stopped_processes(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[Region]` 
    
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

<details><summary><code>client.processes_v1.<a href="src/fern/processes_v1/client.py#L106-L139">get_process_info_deprecated</a>(...) -> Process</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details for a [process](https://hathora.dev/docs/concepts/hathora-entities#process).
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

client.processes_v1.get_process_info_deprecated(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `ProcessId` 
    
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

## ProcessesV2
<details><summary><code>client.processes_v2.<a href="src/fern/processes_v2/client.py#L30-L63">get_process_info</a>(...) -> ProcessV2</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details for a [process](https://hathora.dev/docs/concepts/hathora-entities#process).
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

client.processes_v2.get_process_info(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `ProcessId` 
    
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

<details><summary><code>client.processes_v2.<a href="src/fern/processes_v2/client.py#L65-L106">get_latest_processes</a>(...) -> typing.List[ProcessV2]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the 10 most recent [processes](https://hathora.dev/docs/concepts/hathora-entities#process) objects for an [application](https://hathora.dev/docs/concepts/hathora-entities#application). Filter the array by optionally passing in a `status` or `region`.
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

client.processes_v2.get_latest_processes(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[ProcessStatus, typing.Sequence[ProcessStatus]]]` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[typing.Union[Region, typing.Sequence[Region]]]` 
    
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

<details><summary><code>client.processes_v2.<a href="src/fern/processes_v2/client.py#L108-L140">stop_process</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stops a [process](https://hathora.dev/docs/concepts/hathora-entities#process) immediately.
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

client.processes_v2.stop_process(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `ProcessId` 
    
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

<details><summary><code>client.processes_v2.<a href="src/fern/processes_v2/client.py#L142-L175">create_process</a>(...) -> ProcessV2</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a [process](https://hathora.dev/docs/concepts/hathora-entities#process) without a room. Use this to pre-allocate processes ahead of time so that subsequent room assignment via [CreateRoom()](https://hathora.dev/api#tag/RoomV2/operation/CreateRoom) can be instant.
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
from fern import FernApi, Region
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.processes_v2.create_process(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    region=Region.SEATTLE,
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `Region` 
    
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

## RoomV1
<details><summary><code>client.room_v1.<a href="src/fern/room_v1/client.py#L36-L80">create_room_deprecated</a>(...) -> RoomId</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Region
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.room_v1.create_room_deprecated(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    room_id="2swovpy1fnunu",
    region=Region.SEATTLE,
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateRoomParams` 
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `typing.Optional[RoomId]` 
    
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

<details><summary><code>client.room_v1.<a href="src/fern/room_v1/client.py#L82-L113">get_room_info_deprecated</a>(...) -> Room</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.room_v1.get_room_info_deprecated(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    room_id="2swovpy1fnunu",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `RoomId` 
    
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

<details><summary><code>client.room_v1.<a href="src/fern/room_v1/client.py#L115-L148">get_active_rooms_for_process_deprecated</a>(...) -> typing.List[RoomWithoutAllocations]</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.room_v1.get_active_rooms_for_process_deprecated(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `ProcessId` 
    
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

<details><summary><code>client.room_v1.<a href="src/fern/room_v1/client.py#L150-L183">get_inactive_rooms_for_process_deprecated</a>(...) -> typing.List[RoomWithoutAllocations]</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.room_v1.get_inactive_rooms_for_process_deprecated(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `ProcessId` 
    
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

<details><summary><code>client.room_v1.<a href="src/fern/room_v1/client.py#L185-L215">destroy_room_deprecated</a>(...)</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.room_v1.destroy_room_deprecated(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    room_id="2swovpy1fnunu",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `RoomId` 
    
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

<details><summary><code>client.room_v1.<a href="src/fern/room_v1/client.py#L217-L247">suspend_room_deprecated</a>(...)</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.room_v1.suspend_room_deprecated(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    room_id="2swovpy1fnunu",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `RoomId` 
    
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

<details><summary><code>client.room_v1.<a href="src/fern/room_v1/client.py#L249-L280">get_connection_info_deprecated</a>(...) -> ConnectionInfo</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.room_v1.get_connection_info_deprecated(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    room_id="2swovpy1fnunu",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `RoomId` 
    
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

## RoomV2
<details><summary><code>client.room_v2.<a href="src/fern/room_v2/client.py#L37-L83">create_room</a>(...) -> CreateRoomResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new [room](https://hathora.dev/docs/concepts/hathora-entities#room) for an existing [application](https://hathora.dev/docs/concepts/hathora-entities#application). Poll the [`GetConnectionInfo()`](https://hathora.dev/api#tag/RoomV2/operation/GetConnectionInfo) endpoint to get connection details for an active room.
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
from fern import FernApi, Region
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.room_v2.create_room(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    room_id="2swovpy1fnunu",
    region=Region.SEATTLE,
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateRoomParams` 
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `typing.Optional[RoomId]` 
    
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

<details><summary><code>client.room_v2.<a href="src/fern/room_v2/client.py#L85-L118">get_room_info</a>(...) -> Room</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retreive current and historical allocation data for a [room](https://hathora.dev/docs/concepts/hathora-entities#room).
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

client.room_v2.get_room_info(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    room_id="2swovpy1fnunu",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `RoomId` 
    
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

<details><summary><code>client.room_v2.<a href="src/fern/room_v2/client.py#L120-L153">get_active_rooms_for_process</a>(...) -> typing.List[RoomWithoutAllocations]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all active [rooms](https://hathora.dev/docs/concepts/hathora-entities#room) for a given [process](https://hathora.dev/docs/concepts/hathora-entities#process).
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

client.room_v2.get_active_rooms_for_process(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `ProcessId` 
    
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

<details><summary><code>client.room_v2.<a href="src/fern/room_v2/client.py#L155-L188">get_inactive_rooms_for_process</a>(...) -> typing.List[RoomWithoutAllocations]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all inactive [rooms](https://hathora.dev/docs/concepts/hathora-entities#room) for a given [process](https://hathora.dev/docs/concepts/hathora-entities#process).
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

client.room_v2.get_inactive_rooms_for_process(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `ProcessId` 
    
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

<details><summary><code>client.room_v2.<a href="src/fern/room_v2/client.py#L190-L222">destroy_room</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Destroy a [room](https://hathora.dev/docs/concepts/hathora-entities#room). All associated metadata is deleted.
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

client.room_v2.destroy_room(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    room_id="2swovpy1fnunu",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `RoomId` 
    
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

<details><summary><code>client.room_v2.<a href="src/fern/room_v2/client.py#L224-L256">suspend_room</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Suspend a [room](https://hathora.dev/docs/concepts/hathora-entities#room). The room is unallocated from the process but can be rescheduled later using the same `roomId`.
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

client.room_v2.suspend_room(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    room_id="2swovpy1fnunu",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `RoomId` 
    
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

<details><summary><code>client.room_v2.<a href="src/fern/room_v2/client.py#L258-L291">get_connection_info</a>(...) -> ConnectionInfoV2</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Poll this endpoint to get connection details to a [room](https://hathora.dev/docs/concepts/hathora-entities#room). Clients can call this endpoint without authentication.
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

client.room_v2.get_connection_info(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    room_id="2swovpy1fnunu",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `RoomId` 
    
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

<details><summary><code>client.room_v2.<a href="src/fern/room_v2/client.py#L293-L333">update_room_config</a>(...)</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.room_v2.update_room_config(
    app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
    room_id="2swovpy1fnunu",
    room_config="{\"name\":\"my-room\"}",
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

**app_id:** `AppId` 
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `RoomId` 
    
</dd>
</dl>

<dl>
<dd>

**room_config:** `RoomConfig` 
    
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

## OrgTokensV1
<details><summary><code>client.org_tokens_v1.<a href="src/fern/org_tokens_v1/client.py#L32-L62">get_org_tokens</a>(...) -> ListOrgTokens</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all organization tokens for a given org.
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

client.org_tokens_v1.get_org_tokens(
    org_id="org-6f706e83-0ec1-437a-9a46-7d4281eb2f39",
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

**org_id:** `OrgId` 
    
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

<details><summary><code>client.org_tokens_v1.<a href="src/fern/org_tokens_v1/client.py#L64-L97">create_org_token</a>(...) -> CreatedOrgToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new organization token.
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

client.org_tokens_v1.create_org_token(
    org_id="org-6f706e83-0ec1-437a-9a46-7d4281eb2f39",
    name="ci-token",
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

**org_id:** `OrgId` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `OrgTokenName` 
    
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

<details><summary><code>client.org_tokens_v1.<a href="src/fern/org_tokens_v1/client.py#L99-L132">revoke_org_token</a>(...) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke an organization token.
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

client.org_tokens_v1.revoke_org_token(
    org_id="org-6f706e83-0ec1-437a-9a46-7d4281eb2f39",
    org_token_id="org-6f706e83-0ec1-437a-9a46-7d4281eb2f39",
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

**org_id:** `OrgId` 
    
</dd>
</dl>

<dl>
<dd>

**org_token_id:** `OrgId` 
    
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

