# Reference
## projects
<details><summary><code>client.projects.<a href="src/fern/projects/client.py">speech_projects_locations_operations_get</a>(...) -> Operation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.
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

client.projects.speech_projects_locations_operations_get(
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

**name:** `str` — The name of the operation resource.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[SpeechProjectsLocationsOperationsGetRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[SpeechProjectsLocationsOperationsGetRequestAlt]` — Data format for response.
    
</dd>
</dl>

<dl>
<dd>

**callback:** `typing.Optional[str]` — JSONP
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Selector specifying which fields to include in a partial response.
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` — API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    
</dd>
</dl>

<dl>
<dd>

**oauth_token:** `typing.Optional[str]` — OAuth 2.0 token for the current user.
    
</dd>
</dl>

<dl>
<dd>

**pretty_print:** `typing.Optional[bool]` — Returns response with indentations and line breaks.
    
</dd>
</dl>

<dl>
<dd>

**quota_user:** `typing.Optional[str]` — Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**upload_protocol:** `typing.Optional[str]` — Upload protocol for media (e.g. "raw", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**upload_type:** `typing.Optional[str]` — Legacy upload protocol for media (e.g. "media", "multipart").
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">speech_projects_locations_operations_list</a>(...) -> ListOperationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. NOTE: the `name` binding allows API services to override the binding to use different resource name schemes, such as `users/* /operations`. To override the binding, API services can add a binding such as `"/v1/{name=users/*}/operations"` to their service configuration. For backwards compatibility, the default name includes the operations collection id, however overriding users must ensure the name binding is the parent resource, without the operations collection id.
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

client.projects.speech_projects_locations_operations_list(
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

**name:** `str` — The name of the operation's parent resource.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[SpeechProjectsLocationsOperationsListRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[SpeechProjectsLocationsOperationsListRequestAlt]` — Data format for response.
    
</dd>
</dl>

<dl>
<dd>

**callback:** `typing.Optional[str]` — JSONP
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Selector specifying which fields to include in a partial response.
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` — API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    
</dd>
</dl>

<dl>
<dd>

**oauth_token:** `typing.Optional[str]` — OAuth 2.0 token for the current user.
    
</dd>
</dl>

<dl>
<dd>

**pretty_print:** `typing.Optional[bool]` — Returns response with indentations and line breaks.
    
</dd>
</dl>

<dl>
<dd>

**quota_user:** `typing.Optional[str]` — Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**upload_protocol:** `typing.Optional[str]` — Upload protocol for media (e.g. "raw", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**upload_type:** `typing.Optional[str]` — Legacy upload protocol for media (e.g. "media", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — The standard list filter.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The standard list page size.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — The standard list page token.
    
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

