# Reference
## projects
<details><summary><code>client.projects.<a href="src/fern/projects/client.py">servicebroker_projects_brokers_v2service_instances_get</a>(...) -> GoogleCloudServicebrokerV1Alpha1ServiceInstance</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the given service instance from the system.
This API is an extension and not part of the OSB spec.
Hence the path is a standard Google API URL.
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

client.projects.servicebroker_projects_brokers_v2service_instances_get(
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

**name:** `str` — The resource name of the instance to return.
    
</dd>
</dl>

<dl>
<dd>

**upload_protocol:** `typing.Optional[str]` — Upload protocol for media (e.g. "raw", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**quota_user:** `typing.Optional[str]` — Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**pretty_print:** `typing.Optional[bool]` — Returns response with indentations and line breaks.
    
</dd>
</dl>

<dl>
<dd>

**upload_type:** `typing.Optional[str]` — Legacy upload protocol for media (e.g. "media", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Selector specifying which fields to include in a partial response.
    
</dd>
</dl>

<dl>
<dd>

**callback:** `typing.Optional[str]` — JSONP
    
</dd>
</dl>

<dl>
<dd>

**oauth_token:** `typing.Optional[str]` — OAuth 2.0 token for the current user.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestAlt]` — Data format for response.
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` — API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">servicebroker_projects_brokers_instances_service_bindings_list</a>(...) -> GoogleCloudServicebrokerV1Alpha1ListBindingsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all the bindings in the instance
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

client.projects.servicebroker_projects_brokers_instances_service_bindings_list(
    parent="parent",
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

**parent:** `str` 

Parent must match
`projects/[PROJECT_ID]/brokers/[BROKER_ID]/instances/[INSTANCE_ID]`.
    
</dd>
</dl>

<dl>
<dd>

**upload_protocol:** `typing.Optional[str]` — Upload protocol for media (e.g. "raw", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**quota_user:** `typing.Optional[str]` — Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**pretty_print:** `typing.Optional[bool]` — Returns response with indentations and line breaks.
    
</dd>
</dl>

<dl>
<dd>

**upload_type:** `typing.Optional[str]` — Legacy upload protocol for media (e.g. "media", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Selector specifying which fields to include in a partial response.
    
</dd>
</dl>

<dl>
<dd>

**callback:** `typing.Optional[str]` — JSONP
    
</dd>
</dl>

<dl>
<dd>

**oauth_token:** `typing.Optional[str]` — OAuth 2.0 token for the current user.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestAlt]` — Data format for response.
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` — API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 

Specifies the number of results to return per page. If there are fewer
elements than the specified number, returns all elements.
Optional. If unset or 0, all the results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` 

Specifies a page token to use. Set `pageToken` to a `nextPageToken`
returned by a previous list request to get the next page of results.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">servicebroker_projects_brokers_service_instances_list</a>(...) -> GoogleCloudServicebrokerV1Alpha1ListServiceInstancesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all the instances in the brokers
This API is an extension and not part of the OSB spec.
Hence the path is a standard Google API URL.
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

client.projects.servicebroker_projects_brokers_service_instances_list(
    parent="parent",
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

**parent:** `str` — Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
    
</dd>
</dl>

<dl>
<dd>

**upload_protocol:** `typing.Optional[str]` — Upload protocol for media (e.g. "raw", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**quota_user:** `typing.Optional[str]` — Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**pretty_print:** `typing.Optional[bool]` — Returns response with indentations and line breaks.
    
</dd>
</dl>

<dl>
<dd>

**upload_type:** `typing.Optional[str]` — Legacy upload protocol for media (e.g. "media", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Selector specifying which fields to include in a partial response.
    
</dd>
</dl>

<dl>
<dd>

**callback:** `typing.Optional[str]` — JSONP
    
</dd>
</dl>

<dl>
<dd>

**oauth_token:** `typing.Optional[str]` — OAuth 2.0 token for the current user.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[ServicebrokerProjectsBrokersServiceInstancesListRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[ServicebrokerProjectsBrokersServiceInstancesListRequestAlt]` — Data format for response.
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` — API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 

Specifies the number of results to return per page. If there are fewer
elements than the specified number, returns all elements.
Optional. If unset or 0, all the results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` 

Specifies a page token to use. Set `pageToken` to a `nextPageToken`
returned by a previous list request to get the next page of results.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">servicebroker_projects_brokers_v2catalog_list</a>(...) -> GoogleCloudServicebrokerV1Alpha1ListCatalogResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all the Services registered with this broker for consumption for
given service registry broker, which contains an set of services.
Note, that Service producer API is separate from Broker API.
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

client.projects.servicebroker_projects_brokers_v2catalog_list(
    parent="parent",
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

**parent:** `str` — Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
    
</dd>
</dl>

<dl>
<dd>

**upload_protocol:** `typing.Optional[str]` — Upload protocol for media (e.g. "raw", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**quota_user:** `typing.Optional[str]` — Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**pretty_print:** `typing.Optional[bool]` — Returns response with indentations and line breaks.
    
</dd>
</dl>

<dl>
<dd>

**upload_type:** `typing.Optional[str]` — Legacy upload protocol for media (e.g. "media", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Selector specifying which fields to include in a partial response.
    
</dd>
</dl>

<dl>
<dd>

**callback:** `typing.Optional[str]` — JSONP
    
</dd>
</dl>

<dl>
<dd>

**oauth_token:** `typing.Optional[str]` — OAuth 2.0 token for the current user.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[ServicebrokerProjectsBrokersV2CatalogListRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[ServicebrokerProjectsBrokersV2CatalogListRequestAlt]` — Data format for response.
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` — API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 

Specifies the number of results to return per page. If there are fewer
elements than the specified number, returns all elements.
Optional. If unset or 0, all the results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` 

Specifies a page token to use. Set `pageToken` to a `nextPageToken`
returned by a previous list request to get the next page of results.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">servicebroker_projects_brokers_v2service_instances_delete</a>(...) -> GoogleCloudServicebrokerV1Alpha1DeleteServiceInstanceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprovisions a service instance.
For synchronous/asynchronous request details see CreateServiceInstance
method.
If service instance does not exist HTTP 410 status will be returned.
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

client.projects.servicebroker_projects_brokers_v2service_instances_delete(
    parent="parent",
    instance_id="instanceId",
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

**parent:** `str` — Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
    
</dd>
</dl>

<dl>
<dd>

**instance_id:** `str` — The instance id to deprovision.
    
</dd>
</dl>

<dl>
<dd>

**upload_protocol:** `typing.Optional[str]` — Upload protocol for media (e.g. "raw", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**quota_user:** `typing.Optional[str]` — Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**pretty_print:** `typing.Optional[bool]` — Returns response with indentations and line breaks.
    
</dd>
</dl>

<dl>
<dd>

**upload_type:** `typing.Optional[str]` — Legacy upload protocol for media (e.g. "media", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Selector specifying which fields to include in a partial response.
    
</dd>
</dl>

<dl>
<dd>

**callback:** `typing.Optional[str]` — JSONP
    
</dd>
</dl>

<dl>
<dd>

**oauth_token:** `typing.Optional[str]` — OAuth 2.0 token for the current user.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestAlt]` — Data format for response.
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` — API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**accepts_incomplete:** `typing.Optional[bool]` — See CreateServiceInstanceRequest for details.
    
</dd>
</dl>

<dl>
<dd>

**plan_id:** `typing.Optional[str]` — The plan id of the service instance.
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `typing.Optional[str]` — The service id of the service instance.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">servicebroker_projects_brokers_v2service_instances_get_last_operation</a>(...) -> GoogleCloudServicebrokerV1Alpha1Operation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the state of the last operation for the service instance.
Only last (or current) operation can be polled.
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

client.projects.servicebroker_projects_brokers_v2service_instances_get_last_operation(
    parent="parent",
    instance_id="instanceId",
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

**parent:** `str` — Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
    
</dd>
</dl>

<dl>
<dd>

**instance_id:** `str` — The instance id for which to return the last operation status.
    
</dd>
</dl>

<dl>
<dd>

**upload_protocol:** `typing.Optional[str]` — Upload protocol for media (e.g. "raw", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**quota_user:** `typing.Optional[str]` — Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**pretty_print:** `typing.Optional[bool]` — Returns response with indentations and line breaks.
    
</dd>
</dl>

<dl>
<dd>

**upload_type:** `typing.Optional[str]` — Legacy upload protocol for media (e.g. "media", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Selector specifying which fields to include in a partial response.
    
</dd>
</dl>

<dl>
<dd>

**callback:** `typing.Optional[str]` — JSONP
    
</dd>
</dl>

<dl>
<dd>

**oauth_token:** `typing.Optional[str]` — OAuth 2.0 token for the current user.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestAlt]` — Data format for response.
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` — API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**operation:** `typing.Optional[str]` 

If `operation` was returned during mutation operation, this field must be
populated with the provided value.
    
</dd>
</dl>

<dl>
<dd>

**plan_id:** `typing.Optional[str]` — Plan id.
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `typing.Optional[str]` — Service id.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">servicebroker_projects_brokers_v2service_instances_service_bindings_get</a>(...) -> GoogleCloudServicebrokerV1Alpha1GetBindingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

GetBinding returns the binding information.
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

client.projects.servicebroker_projects_brokers_v2service_instances_service_bindings_get(
    parent="parent",
    instance_id="instanceId",
    binding_id="bindingId",
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

**parent:** `str` — Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
    
</dd>
</dl>

<dl>
<dd>

**instance_id:** `str` — Instance id to which the binding is bound.
    
</dd>
</dl>

<dl>
<dd>

**binding_id:** `str` — The binding id.
    
</dd>
</dl>

<dl>
<dd>

**upload_protocol:** `typing.Optional[str]` — Upload protocol for media (e.g. "raw", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**quota_user:** `typing.Optional[str]` — Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**pretty_print:** `typing.Optional[bool]` — Returns response with indentations and line breaks.
    
</dd>
</dl>

<dl>
<dd>

**upload_type:** `typing.Optional[str]` — Legacy upload protocol for media (e.g. "media", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Selector specifying which fields to include in a partial response.
    
</dd>
</dl>

<dl>
<dd>

**callback:** `typing.Optional[str]` — JSONP
    
</dd>
</dl>

<dl>
<dd>

**oauth_token:** `typing.Optional[str]` — OAuth 2.0 token for the current user.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestAlt]` — Data format for response.
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` — API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**plan_id:** `typing.Optional[str]` — Plan id.
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `typing.Optional[str]` — Service id.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">servicebroker_projects_brokers_v2service_instances_service_bindings_get_last_operation</a>(...) -> GoogleCloudServicebrokerV1Alpha1Operation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the state of the last operation for the binding.
Only last (or current) operation can be polled.
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

client.projects.servicebroker_projects_brokers_v2service_instances_service_bindings_get_last_operation(
    parent="parent",
    instance_id="instanceId",
    binding_id="bindingId",
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

**parent:** `str` — Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
    
</dd>
</dl>

<dl>
<dd>

**instance_id:** `str` — The instance id that the binding is bound to.
    
</dd>
</dl>

<dl>
<dd>

**binding_id:** `str` — The binding id for which to return the last operation
    
</dd>
</dl>

<dl>
<dd>

**upload_protocol:** `typing.Optional[str]` — Upload protocol for media (e.g. "raw", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**quota_user:** `typing.Optional[str]` — Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**pretty_print:** `typing.Optional[bool]` — Returns response with indentations and line breaks.
    
</dd>
</dl>

<dl>
<dd>

**upload_type:** `typing.Optional[str]` — Legacy upload protocol for media (e.g. "media", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Selector specifying which fields to include in a partial response.
    
</dd>
</dl>

<dl>
<dd>

**callback:** `typing.Optional[str]` — JSONP
    
</dd>
</dl>

<dl>
<dd>

**oauth_token:** `typing.Optional[str]` — OAuth 2.0 token for the current user.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestAlt]` — Data format for response.
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` — API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**operation:** `typing.Optional[str]` 

If `operation` was returned during mutation operation, this field must be
populated with the provided value.
    
</dd>
</dl>

<dl>
<dd>

**plan_id:** `typing.Optional[str]` — Plan id.
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `typing.Optional[str]` — Service id.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">servicebroker_projects_brokers_v2service_instances_service_bindings_create</a>(...) -> GoogleCloudServicebrokerV1Alpha1CreateBindingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

CreateBinding generates a service binding to an existing service instance.
See ProviServiceInstance for async operation details.
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

client.projects.servicebroker_projects_brokers_v2service_instances_service_bindings_create(
    parent="parent",
    instance_id="instanceId",
    binding_id_="binding_id",
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

**parent:** `str` 

The GCP container.
Must match
`projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
    
</dd>
</dl>

<dl>
<dd>

**instance_id:** `str` — The service instance to which to bind.
    
</dd>
</dl>

<dl>
<dd>

**binding_id:** `str` 

The id of the binding. Must be unique within GCP project.
Maximum length is 64, GUID recommended.
Required.
    
</dd>
</dl>

<dl>
<dd>

**request:** `GoogleCloudServicebrokerV1Alpha1Binding` 
    
</dd>
</dl>

<dl>
<dd>

**upload_protocol:** `typing.Optional[str]` — Upload protocol for media (e.g. "raw", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**quota_user:** `typing.Optional[str]` — Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**pretty_print:** `typing.Optional[bool]` — Returns response with indentations and line breaks.
    
</dd>
</dl>

<dl>
<dd>

**upload_type:** `typing.Optional[str]` — Legacy upload protocol for media (e.g. "media", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Selector specifying which fields to include in a partial response.
    
</dd>
</dl>

<dl>
<dd>

**callback:** `typing.Optional[str]` — JSONP
    
</dd>
</dl>

<dl>
<dd>

**oauth_token:** `typing.Optional[str]` — OAuth 2.0 token for the current user.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestAlt]` — Data format for response.
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` — API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**accepts_incomplete:** `typing.Optional[bool]` — See CreateServiceInstanceRequest for details.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">servicebroker_projects_brokers_v2service_instances_create</a>(...) -> GoogleCloudServicebrokerV1Alpha1CreateServiceInstanceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provisions a service instance.
If `request.accepts_incomplete` is false and Broker cannot execute request
synchronously HTTP 422 error will be returned along with
FAILED_PRECONDITION status.
If `request.accepts_incomplete` is true and the Broker decides to execute
resource asynchronously then HTTP 202 response code will be returned and a
valid polling operation in the response will be included.
If Broker executes the request synchronously and it succeeds HTTP 201
response will be furnished.
If identical instance exists, then HTTP 200 response will be returned.
If an instance with identical ID but mismatching parameters exists, then
HTTP 409 status code will be returned.
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

client.projects.servicebroker_projects_brokers_v2service_instances_create(
    parent="parent",
    instance_id_="instance_id",
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

**parent:** `str` — Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
    
</dd>
</dl>

<dl>
<dd>

**instance_id:** `str` 

The id of the service instance. Must be unique within GCP project.
Maximum length is 64, GUID recommended.
Required.
    
</dd>
</dl>

<dl>
<dd>

**request:** `GoogleCloudServicebrokerV1Alpha1ServiceInstance` 
    
</dd>
</dl>

<dl>
<dd>

**upload_protocol:** `typing.Optional[str]` — Upload protocol for media (e.g. "raw", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**quota_user:** `typing.Optional[str]` — Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**pretty_print:** `typing.Optional[bool]` — Returns response with indentations and line breaks.
    
</dd>
</dl>

<dl>
<dd>

**upload_type:** `typing.Optional[str]` — Legacy upload protocol for media (e.g. "media", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Selector specifying which fields to include in a partial response.
    
</dd>
</dl>

<dl>
<dd>

**callback:** `typing.Optional[str]` — JSONP
    
</dd>
</dl>

<dl>
<dd>

**oauth_token:** `typing.Optional[str]` — OAuth 2.0 token for the current user.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestAlt]` — Data format for response.
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` — API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**accepts_incomplete:** `typing.Optional[bool]` 

Value indicating that API client supports asynchronous operations. If
Broker cannot execute the request synchronously HTTP 422 code will be
returned to HTTP clients along with FAILED_PRECONDITION error.
If true and broker will execute request asynchronously 202 HTTP code will
be returned.
This broker always requires this to be true as all mutator operations are
asynchronous.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">servicebroker_projects_brokers_v2service_instances_patch</a>(...) -> GoogleCloudServicebrokerV1Alpha1UpdateServiceInstanceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing service instance.
See CreateServiceInstance for possible response codes.
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

client.projects.servicebroker_projects_brokers_v2service_instances_patch(
    parent="parent",
    instance_id_="instance_id",
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

**parent:** `str` — Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
    
</dd>
</dl>

<dl>
<dd>

**instance_id:** `str` 

The id of the service instance. Must be unique within GCP project.
Maximum length is 64, GUID recommended.
Required.
    
</dd>
</dl>

<dl>
<dd>

**request:** `GoogleCloudServicebrokerV1Alpha1ServiceInstance` 
    
</dd>
</dl>

<dl>
<dd>

**upload_protocol:** `typing.Optional[str]` — Upload protocol for media (e.g. "raw", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**quota_user:** `typing.Optional[str]` — Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**pretty_print:** `typing.Optional[bool]` — Returns response with indentations and line breaks.
    
</dd>
</dl>

<dl>
<dd>

**upload_type:** `typing.Optional[str]` — Legacy upload protocol for media (e.g. "media", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Selector specifying which fields to include in a partial response.
    
</dd>
</dl>

<dl>
<dd>

**callback:** `typing.Optional[str]` — JSONP
    
</dd>
</dl>

<dl>
<dd>

**oauth_token:** `typing.Optional[str]` — OAuth 2.0 token for the current user.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestAlt]` — Data format for response.
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` — API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**accepts_incomplete:** `typing.Optional[bool]` — See CreateServiceInstanceRequest for details.
    
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

## v1alpha1
<details><summary><code>client.v1alpha1.<a href="src/fern/v1alpha1/client.py">servicebroker_get_iam_policy</a>(...) -> GoogleIamV1Policy</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the access control policy for a resource.
Returns an empty policy if the resource exists and does not have a policy
set.
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

client.v1alpha1.servicebroker_get_iam_policy(
    resource="resource",
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

**resource:** `str` 

REQUIRED: The resource for which the policy is being requested.
See the operation documentation for the appropriate value for this field.
    
</dd>
</dl>

<dl>
<dd>

**upload_protocol:** `typing.Optional[str]` — Upload protocol for media (e.g. "raw", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**quota_user:** `typing.Optional[str]` — Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**pretty_print:** `typing.Optional[bool]` — Returns response with indentations and line breaks.
    
</dd>
</dl>

<dl>
<dd>

**upload_type:** `typing.Optional[str]` — Legacy upload protocol for media (e.g. "media", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Selector specifying which fields to include in a partial response.
    
</dd>
</dl>

<dl>
<dd>

**callback:** `typing.Optional[str]` — JSONP
    
</dd>
</dl>

<dl>
<dd>

**oauth_token:** `typing.Optional[str]` — OAuth 2.0 token for the current user.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[ServicebrokerGetIamPolicyRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[ServicebrokerGetIamPolicyRequestAlt]` — Data format for response.
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` — API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**options_requested_policy_version:** `typing.Optional[int]` 

Optional. The policy format version to be returned.

Valid values are 0, 1, and 3. Requests specifying an invalid value will be
rejected.

Requests for policies with any conditional bindings must specify version 3.
Policies without any conditional bindings may specify any valid value or
leave the field unset.
    
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

<details><summary><code>client.v1alpha1.<a href="src/fern/v1alpha1/client.py">servicebroker_set_iam_policy</a>(...) -> GoogleIamV1Policy</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets the access control policy on the specified resource. Replaces any
existing policy.

Can return Public Errors: NOT_FOUND, INVALID_ARGUMENT and PERMISSION_DENIED
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

client.v1alpha1.servicebroker_set_iam_policy(
    resource="resource",
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

**resource:** `str` 

REQUIRED: The resource for which the policy is being specified.
See the operation documentation for the appropriate value for this field.
    
</dd>
</dl>

<dl>
<dd>

**upload_protocol:** `typing.Optional[str]` — Upload protocol for media (e.g. "raw", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**quota_user:** `typing.Optional[str]` — Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**pretty_print:** `typing.Optional[bool]` — Returns response with indentations and line breaks.
    
</dd>
</dl>

<dl>
<dd>

**upload_type:** `typing.Optional[str]` — Legacy upload protocol for media (e.g. "media", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Selector specifying which fields to include in a partial response.
    
</dd>
</dl>

<dl>
<dd>

**callback:** `typing.Optional[str]` — JSONP
    
</dd>
</dl>

<dl>
<dd>

**oauth_token:** `typing.Optional[str]` — OAuth 2.0 token for the current user.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[ServicebrokerSetIamPolicyRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[ServicebrokerSetIamPolicyRequestAlt]` — Data format for response.
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` — API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**policy:** `typing.Optional[GoogleIamV1Policy]` 

REQUIRED: The complete policy to be applied to the `resource`. The size of
the policy is limited to a few 10s of KB. An empty policy is a
valid policy but certain Cloud Platform services (such as Projects)
might reject them.
    
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

<details><summary><code>client.v1alpha1.<a href="src/fern/v1alpha1/client.py">servicebroker_test_iam_permissions</a>(...) -> GoogleIamV1TestIamPermissionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns permissions that a caller has on the specified resource.
If the resource does not exist, this will return an empty set of
permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware
UIs and command-line tools, not for authorization checking. This operation
may "fail open" without warning.
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

client.v1alpha1.servicebroker_test_iam_permissions(
    resource="resource",
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

**resource:** `str` 

REQUIRED: The resource for which the policy detail is being requested.
See the operation documentation for the appropriate value for this field.
    
</dd>
</dl>

<dl>
<dd>

**upload_protocol:** `typing.Optional[str]` — Upload protocol for media (e.g. "raw", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**quota_user:** `typing.Optional[str]` — Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**pretty_print:** `typing.Optional[bool]` — Returns response with indentations and line breaks.
    
</dd>
</dl>

<dl>
<dd>

**upload_type:** `typing.Optional[str]` — Legacy upload protocol for media (e.g. "media", "multipart").
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Selector specifying which fields to include in a partial response.
    
</dd>
</dl>

<dl>
<dd>

**callback:** `typing.Optional[str]` — JSONP
    
</dd>
</dl>

<dl>
<dd>

**oauth_token:** `typing.Optional[str]` — OAuth 2.0 token for the current user.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[ServicebrokerTestIamPermissionsRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[ServicebrokerTestIamPermissionsRequestAlt]` — Data format for response.
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` — API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.Optional[typing.List[str]]` 

The set of permissions to check for the `resource`. Permissions with
wildcards (such as '*' or 'storage.*') are not allowed. For more
information see
[IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).
    
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

