# Reference
## locations
<details><summary><code>client.locations.<a href="src/fern/locations/client.py">monitoring_locations_global_metrics_scopes_list_metrics_scopes_by_monitored_project</a>(...) -> ListMetricsScopesByMonitoredProjectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of every Metrics Scope that a specific MonitoredProject has been added to. The metrics scope representing the specified monitored project will always be the first entry in the response.
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

client.locations.monitoring_locations_global_metrics_scopes_list_metrics_scopes_by_monitored_project()

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

**xgafv:** `typing.Optional[MonitoringLocationsGlobalMetricsScopesListMetricsScopesByMonitoredProjectRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[MonitoringLocationsGlobalMetricsScopesListMetricsScopesByMonitoredProjectRequestAlt]` — Data format for response.
    
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

**monitored_resource_container:** `typing.Optional[str]` — Required. The resource name of the Monitored Project being requested. Example: projects/{MONITORED_PROJECT_ID_OR_NUMBER}
    
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

<details><summary><code>client.locations.<a href="src/fern/locations/client.py">monitoring_locations_global_metrics_scopes_projects_create</a>(...) -> Operation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a MonitoredProject with the given project ID to the specified Metrics Scope.
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

client.locations.monitoring_locations_global_metrics_scopes_projects_create(
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

**parent:** `str` — Required. The resource name of the existing Metrics Scope that will monitor this project. Example: locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}
    
</dd>
</dl>

<dl>
<dd>

**request:** `MonitoredProject` 
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[MonitoringLocationsGlobalMetricsScopesProjectsCreateRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[MonitoringLocationsGlobalMetricsScopesProjectsCreateRequestAlt]` — Data format for response.
    
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

## projects
<details><summary><code>client.projects.<a href="src/fern/projects/client.py">monitoring_projects_dashboards_get</a>(...) -> Dashboard</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches a specific dashboard.This method requires the monitoring.dashboards.get permission on the specified dashboard. For more information, see Cloud Identity and Access Management (https://cloud.google.com/iam).
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

client.projects.monitoring_projects_dashboards_get(
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

**name:** `str` — Required. The resource name of the Dashboard. The format is one of: dashboards/[DASHBOARD_ID] (for system dashboards) projects/[PROJECT_ID_OR_NUMBER]/dashboards/[DASHBOARD_ID] (for custom dashboards).
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[MonitoringProjectsDashboardsGetRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[MonitoringProjectsDashboardsGetRequestAlt]` — Data format for response.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">monitoring_projects_dashboards_delete</a>(...) -> Empty</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing custom dashboard.This method requires the monitoring.dashboards.delete permission on the specified dashboard. For more information, see Cloud Identity and Access Management (https://cloud.google.com/iam).
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

client.projects.monitoring_projects_dashboards_delete(
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

**name:** `str` — Required. The resource name of the Dashboard. The format is: projects/[PROJECT_ID_OR_NUMBER]/dashboards/[DASHBOARD_ID] 
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[MonitoringProjectsDashboardsDeleteRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[MonitoringProjectsDashboardsDeleteRequestAlt]` — Data format for response.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">monitoring_projects_dashboards_patch</a>(...) -> Dashboard</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replaces an existing custom dashboard with a new definition.This method requires the monitoring.dashboards.update permission on the specified dashboard. For more information, see Cloud Identity and Access Management (https://cloud.google.com/iam).
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

client.projects.monitoring_projects_dashboards_patch(
    name_="name",
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

**name:** `str` — Identifier. The resource name of the dashboard.
    
</dd>
</dl>

<dl>
<dd>

**request:** `Dashboard` 
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[MonitoringProjectsDashboardsPatchRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[MonitoringProjectsDashboardsPatchRequestAlt]` — Data format for response.
    
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

**validate_only:** `typing.Optional[bool]` — If set, validate the request and preview the review, but do not actually save it.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">monitoring_projects_location_prometheus_api_v1label_values</a>(...) -> HttpBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists possible values for a given label name.
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

client.projects.monitoring_projects_location_prometheus_api_v1label_values(
    name="name",
    location="location",
    label="label",
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

**name:** `str` — The workspace on which to execute the request. It is not part of the open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine. The format is: projects/PROJECT_ID_OR_NUMBER.
    
</dd>
</dl>

<dl>
<dd>

**location:** `str` — Location of the resource information. Has to be "global" now.
    
</dd>
</dl>

<dl>
<dd>

**label:** `str` — The label name for which values are queried.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestAlt]` — Data format for response.
    
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

**end:** `typing.Optional[str]` — The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.
    
</dd>
</dl>

<dl>
<dd>

**match:** `typing.Optional[str]` — A list of matchers encoded in the Prometheus label matcher format to constrain the values to series that satisfy them.
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[str]` — The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">monitoring_projects_location_prometheus_api_v1labels</a>(...) -> HttpBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists labels for metrics.
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

client.projects.monitoring_projects_location_prometheus_api_v1labels(
    name="name",
    location="location",
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

**name:** `str` — The workspace on which to execute the request. It is not part of the open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine. The format is: projects/PROJECT_ID_OR_NUMBER.
    
</dd>
</dl>

<dl>
<dd>

**location:** `str` — Location of the resource information. Has to be "global" now.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[MonitoringProjectsLocationPrometheusApiV1LabelsRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[MonitoringProjectsLocationPrometheusApiV1LabelsRequestAlt]` — Data format for response.
    
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

**end:** `typing.Optional[str]` — The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.
    
</dd>
</dl>

<dl>
<dd>

**match:** `typing.Optional[str]` — A list of matchers encoded in the Prometheus label matcher format to constrain the values to series that satisfy them.
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[str]` — The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">monitoring_projects_location_prometheus_api_v1metadata_list</a>(...) -> HttpBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists metadata for metrics.
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

client.projects.monitoring_projects_location_prometheus_api_v1metadata_list(
    name="name",
    location="location",
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

**name:** `str` — Required. The workspace on which to execute the request. It is not part of the open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine. The format is: projects/PROJECT_ID_OR_NUMBER.
    
</dd>
</dl>

<dl>
<dd>

**location:** `str` — Location of the resource information. Has to be "global" for now.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[MonitoringProjectsLocationPrometheusApiV1MetadataListRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[MonitoringProjectsLocationPrometheusApiV1MetadataListRequestAlt]` — Data format for response.
    
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

**limit:** `typing.Optional[str]` — Maximum number of metrics to return.
    
</dd>
</dl>

<dl>
<dd>

**metric:** `typing.Optional[str]` — The metric name for which to query metadata. If unset, all metric metadata is returned.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">monitoring_projects_location_prometheus_api_v1query</a>(...) -> HttpBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Evaluate a PromQL query at a single point in time.
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

client.projects.monitoring_projects_location_prometheus_api_v1query(
    name="name",
    location="location",
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

**name:** `str` — The project on which to execute the request. Data associcated with the project's workspace stored under the The format is: projects/PROJECT_ID_OR_NUMBER. Open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine.
    
</dd>
</dl>

<dl>
<dd>

**location:** `str` — Location of the resource information. Has to be "global" now.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryRequestAlt]` — Data format for response.
    
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

**query:** `typing.Optional[str]` — A PromQL query string. Query lanauge documentation: https://prometheus.io/docs/prometheus/latest/querying/basics/.
    
</dd>
</dl>

<dl>
<dd>

**time:** `typing.Optional[str]` — The single point in time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[str]` — An upper bound timeout for the query. Either a Prometheus duration string (https://prometheus.io/docs/prometheus/latest/querying/basics/#time-durations) or floating point seconds. This non-standard encoding must be used for compatibility with the open source API. Clients may still implement timeouts at the connection level while ignoring this field.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">monitoring_projects_location_prometheus_api_v1query_exemplars</a>(...) -> HttpBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists exemplars relevant to a given PromQL query,
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

client.projects.monitoring_projects_location_prometheus_api_v1query_exemplars(
    name="name",
    location="location",
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

**name:** `str` — The project on which to execute the request. Data associcated with the project's workspace stored under the The format is: projects/PROJECT_ID_OR_NUMBER. Open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine.
    
</dd>
</dl>

<dl>
<dd>

**location:** `str` — Location of the resource information. Has to be "global" now.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestAlt]` — Data format for response.
    
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

**end:** `typing.Optional[str]` — The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — A PromQL query string. Query lanauge documentation: https://prometheus.io/docs/prometheus/latest/querying/basics/.
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[str]` — The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">monitoring_projects_location_prometheus_api_v1query_range</a>(...) -> HttpBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Evaluate a PromQL query with start, end time range.
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

client.projects.monitoring_projects_location_prometheus_api_v1query_range(
    name="name",
    location="location",
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

**name:** `str` — The project on which to execute the request. Data associcated with the project's workspace stored under the The format is: projects/PROJECT_ID_OR_NUMBER. Open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine.
    
</dd>
</dl>

<dl>
<dd>

**location:** `str` — Location of the resource information. Has to be "global" now.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestAlt]` — Data format for response.
    
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

**end:** `typing.Optional[str]` — The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — A PromQL query string. Query lanauge documentation: https://prometheus.io/docs/prometheus/latest/querying/basics/.
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[str]` — The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.
    
</dd>
</dl>

<dl>
<dd>

**step:** `typing.Optional[str]` — The resolution of query result. Either a Prometheus duration string (https://prometheus.io/docs/prometheus/latest/querying/basics/#time-durations) or floating point seconds. This non-standard encoding must be used for compatibility with the open source API. Clients may still implement timeouts at the connection level while ignoring this field.
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[str]` — An upper bound timeout for the query. Either a Prometheus duration string (https://prometheus.io/docs/prometheus/latest/querying/basics/#time-durations) or floating point seconds. This non-standard encoding must be used for compatibility with the open source API. Clients may still implement timeouts at the connection level while ignoring this field.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">monitoring_projects_location_prometheus_api_v1series</a>(...) -> HttpBody</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists metadata for metrics.
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

client.projects.monitoring_projects_location_prometheus_api_v1series(
    name="name",
    location="location",
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

**name:** `str` — Required. The workspace on which to execute the request. It is not part of the open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine. The format is: projects/PROJECT_ID_OR_NUMBER.
    
</dd>
</dl>

<dl>
<dd>

**location:** `str` — Location of the resource information. Has to be "global" for now.
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[MonitoringProjectsLocationPrometheusApiV1SeriesRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[MonitoringProjectsLocationPrometheusApiV1SeriesRequestAlt]` — Data format for response.
    
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

**end:** `typing.Optional[str]` — The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[str]` — The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">monitoring_projects_dashboards_list</a>(...) -> ListDashboardsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the existing dashboards.This method requires the monitoring.dashboards.list permission on the specified project. For more information, see Cloud Identity and Access Management (https://cloud.google.com/iam).
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

client.projects.monitoring_projects_dashboards_list(
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

**parent:** `str` — Required. The scope of the dashboards to list. The format is: projects/[PROJECT_ID_OR_NUMBER] 
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[MonitoringProjectsDashboardsListRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[MonitoringProjectsDashboardsListRequestAlt]` — Data format for response.
    
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

**page_size:** `typing.Optional[int]` — A positive number that is the maximum number of results to return. If unspecified, a default of 1000 is used.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Optional. If this field is not empty then it must contain the nextPageToken value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.
    
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

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">monitoring_projects_dashboards_create</a>(...) -> Dashboard</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new custom dashboard. For examples on how you can use this API to create dashboards, see Managing dashboards by API (https://cloud.google.com/monitoring/dashboards/api-dashboard). This method requires the monitoring.dashboards.create permission on the specified project. For more information about permissions, see Cloud Identity and Access Management (https://cloud.google.com/iam).
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

client.projects.monitoring_projects_dashboards_create(
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

**parent:** `str` — Required. The project on which to execute the request. The format is: projects/[PROJECT_ID_OR_NUMBER] The [PROJECT_ID_OR_NUMBER] must match the dashboard resource name.
    
</dd>
</dl>

<dl>
<dd>

**request:** `Dashboard` 
    
</dd>
</dl>

<dl>
<dd>

**xgafv:** `typing.Optional[MonitoringProjectsDashboardsCreateRequestXgafv]` — V1 error format.
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**alt:** `typing.Optional[MonitoringProjectsDashboardsCreateRequestAlt]` — Data format for response.
    
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

**validate_only:** `typing.Optional[bool]` — If set, validate the request and preview the review, but do not actually save it.
    
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

