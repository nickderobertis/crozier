# Reference
## Alerts
<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">get_alert_filter_and_options</a>() -> AlertFilterSuggestion</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an object whose keys are the available policy filters. The corresponding values are default or recently set filter options
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
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.get_alert_filter_and_options()

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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">get_alert_filter_options</a>(...) -> ParsedTableFilter</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns available options for an alert filter key. Supports fuzzy autocomplete search. If you specify a **query** value in the request body parameters, the response includes only items that contain the **query** string.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.get_alert_filter_options(
    filter_name="filterName",
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

**filter_name:** `str` — Filter name
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Case-insensitive fuzzy search autocomplete filter. Includes only items that contain the query as a substring.
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">get_alerts</a>(...) -> typing.List[AlertModel]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of alerts that match the constraints specified in the query parameters. Max 10k results. To get more, use **List Alerts V2 - GET**.  

Data in the response object does not include alert rules.

Also, in the response object:

* Property **riskDetail** is deprecated.
* Property **resource.cloudServiceName** is populated only for alerts whose resources belong to a cloud service.

When `detailed` flag is set to **true**, following fields will be returned within the policy response object:

- `complianceMetadata`
- `name`
- `description`
- `labels`
- `deleted`
- `recommendation`
- `lastModifiedBy`
- `lastModifiedOn`
- `severity`

#### Rate Limits ####

The following rate limits apply:
* Request rate limit: 2/sec 
* Burst limit: 10/sec        
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
from fern.alerts import GetAlertsRequestTimeType, GetAlertsRequestTimeUnit

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.get_alerts(
    time_type=GetAlertsRequestTimeType.RELATIVE,
    time_amount="timeAmount",
    time_unit=GetAlertsRequestTimeUnit.MINUTE,
    detailed=True,
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

**time_type:** `GetAlertsRequestTimeType` — Time Type
    
</dd>
</dl>

<dl>
<dd>

**time_amount:** `str` — Number of **timeUnits**
    
</dd>
</dl>

<dl>
<dd>

**time_unit:** `GetAlertsRequestTimeUnit` — Time Unit
    
</dd>
</dl>

<dl>
<dd>

**detailed:** `bool` — true = Return detailed alert data.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of specific fields to retrieve. Allowed values: alert.id, alert.status, alert.time, cloud.accountId, cloud.account, cloud.region, resource.id, resource.name, policy.name, policy.type, policy.severity
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — The maximum number of items that will be returned in one response. The maximum cannot exceed 10,000. The default is 10,000.
    
</dd>
</dl>

<dl>
<dd>

**alert_id:** `typing.Optional[str]` — Alert ID
    
</dd>
</dl>

<dl>
<dd>

**alert_status:** `typing.Optional[GetAlertsRequestAlertStatus]` — Alert status
    
</dd>
</dl>

<dl>
<dd>

**cloud_account:** `typing.Optional[str]` — Cloud account
    
</dd>
</dl>

<dl>
<dd>

**cloud_account_id:** `typing.Optional[str]` — Cloud account Id
    
</dd>
</dl>

<dl>
<dd>

**account_group:** `typing.Optional[str]` — Account group
    
</dd>
</dl>

<dl>
<dd>

**cloud_type:** `typing.Optional[str]` — Cloud type
    
</dd>
</dl>

<dl>
<dd>

**cloud_region:** `typing.Optional[str]` — Cloud region
    
</dd>
</dl>

<dl>
<dd>

**cloud_service:** `typing.Optional[str]` — Cloud service
    
</dd>
</dl>

<dl>
<dd>

**policy_id:** `typing.Optional[str]` — Policy ID
    
</dd>
</dl>

<dl>
<dd>

**policy_name:** `typing.Optional[str]` — Policy name
    
</dd>
</dl>

<dl>
<dd>

**policy_severity:** `typing.Optional[GetAlertsRequestPolicySeverity]` — Policy severity
    
</dd>
</dl>

<dl>
<dd>

**policy_label:** `typing.Optional[str]` — Policy label
    
</dd>
</dl>

<dl>
<dd>

**policy_type:** `typing.Optional[GetAlertsRequestPolicyType]` — Policy type
    
</dd>
</dl>

<dl>
<dd>

**policy_compliance_standard:** `typing.Optional[str]` — Policy compliance standard name
    
</dd>
</dl>

<dl>
<dd>

**policy_compliance_requirement:** `typing.Optional[str]` — Policy compliance requirement name
    
</dd>
</dl>

<dl>
<dd>

**policy_compliance_section:** `typing.Optional[str]` — Policy compliance section ID
    
</dd>
</dl>

<dl>
<dd>

**policy_remediable:** `typing.Optional[GetAlertsRequestPolicyRemediable]` — Policy is remediable
    
</dd>
</dl>

<dl>
<dd>

**alert_rule_name:** `typing.Optional[str]` — Alert rule name
    
</dd>
</dl>

<dl>
<dd>

**resource_id:** `typing.Optional[str]` — Resource ID
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `typing.Optional[str]` — Resource name
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `typing.Optional[str]` — Resource TYPE
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">post_alerts</a>(...) -> typing.List[AlertModel]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of alerts that matches the constraints specified in the body parameters. Max 10k results. To get more, use **List Alerts V2 - POST**.  

The **fields** body parameter allows you to request specific fields from the alert payload. These fields
are separate from the filters you specify. The following are valid **fields** items.

* alert.id
* alert.status
* alert.time
* cloud.account
* cloud.accountId
* cloud.region
* resource.id
* resource.name
* policy.name
* policy.type
* policy.severity

The **filters** body parameter enables you to narrow your request for alerts. See 
[List Alert Filters](/prisma-cloud/api/cspm/get-alert-filter-and-options) 
for an API request to list all the valid filters.

Data in the response object does not include alert rules.

Also, in the response object:

* Property **riskDetail** is deprecated.
* Property **resource.cloudServiceName** is populated only for alerts whose resources belong to a cloud service.

When `detailed` flag is set to **true**, following fields will be returned within the policy response object:

- `complianceMetadata`
- `name`
- `description`
- `labels`
- `deleted`
- `recommendation`
- `lastModifiedBy`
- `lastModifiedOn`
- `severity`

#### Rate Limits ####

The following rate limits apply:
* Request rate limit: 2/sec 
* Burst limit: 10/sec        
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
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.post_alerts()

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

**request:** `FilterModel` 
    
</dd>
</dl>

<dl>
<dd>

**detailed:** `typing.Optional[bool]` — true = Return detailed alert data. Default is false. Overrides **detailed** in body param.
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">get_alerts_v2</a>(...) -> PagedResultsAlertModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of alerts from the Prisma Cloud platform.  

Data in the response object does not include alert rules.

Also, in the response object:

* Property **riskDetail** is deprecated.
* Property **items[].resource.cloudServiceName** is populated only for alerts whose resources belong to a cloud service.

When `detailed` flag is set to **true**, following fields will be returned within the policy response object:

- `complianceMetadata`
- `name`
- `description`
- `labels`
- `deleted`
- `recommendation`
- `lastModifiedBy`
- `lastModifiedOn`
- `severity`

#### Rate Limits ####

The following rate limits apply:
* Request rate limit: 2/sec 
* Burst limit: 10/sec      
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
from fern.alerts import GetAlertsV2RequestTimeType, GetAlertsV2RequestTimeUnit

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.get_alerts_v2(
    time_type=GetAlertsV2RequestTimeType.RELATIVE,
    time_amount="timeAmount",
    time_unit=GetAlertsV2RequestTimeUnit.MINUTE,
    detailed=True,
    sort_by="sortBy=id:desc&sortBy=firstseen:asc,lastseen:desc",
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

**time_type:** `GetAlertsV2RequestTimeType` — Time Type
    
</dd>
</dl>

<dl>
<dd>

**time_amount:** `str` — Number of **timeUnits**
    
</dd>
</dl>

<dl>
<dd>

**time_unit:** `GetAlertsV2RequestTimeUnit` — Time Unit
    
</dd>
</dl>

<dl>
<dd>

**detailed:** `bool` — true = Return detailed alert data.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Array of specific fields to return. Allowed fields: alert.id, alert.status, alert.time, cloud.accountId, cloud.account, cloud.region, resource.id, resource.name, policy.name, policy.type, policy.severity
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — Response object property by which to sort response list. The valid values are in the response object attribute **sortAllowedColumns**. The format is **property:asc** for ascending and **property:desc** for descending sort 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — The maximum number of items that will be returned in one response. The maximum cannot exceed 10,000. The default is 10,000.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Token that identifies the required page of data. When there are multiple pages of data in the response, set **pageToken** to the **nextPageToken** value from the previous API response to retrieve the next page of data.
    
</dd>
</dl>

<dl>
<dd>

**alert_id:** `typing.Optional[str]` — Alert ID
    
</dd>
</dl>

<dl>
<dd>

**alert_status:** `typing.Optional[GetAlertsV2RequestAlertStatus]` — Alert status
    
</dd>
</dl>

<dl>
<dd>

**cloud_account:** `typing.Optional[str]` — Cloud account
    
</dd>
</dl>

<dl>
<dd>

**cloud_account_id:** `typing.Optional[str]` — Cloud account Id
    
</dd>
</dl>

<dl>
<dd>

**account_group:** `typing.Optional[str]` — Account group
    
</dd>
</dl>

<dl>
<dd>

**cloud_type:** `typing.Optional[str]` — Cloud type
    
</dd>
</dl>

<dl>
<dd>

**cloud_region:** `typing.Optional[str]` — Cloud region
    
</dd>
</dl>

<dl>
<dd>

**cloud_service:** `typing.Optional[str]` — Cloud service
    
</dd>
</dl>

<dl>
<dd>

**policy_id:** `typing.Optional[str]` — Policy ID
    
</dd>
</dl>

<dl>
<dd>

**policy_name:** `typing.Optional[str]` — Policy name
    
</dd>
</dl>

<dl>
<dd>

**policy_severity:** `typing.Optional[GetAlertsV2RequestPolicySeverity]` — Policy severity
    
</dd>
</dl>

<dl>
<dd>

**policy_label:** `typing.Optional[str]` — Policy label
    
</dd>
</dl>

<dl>
<dd>

**policy_type:** `typing.Optional[GetAlertsV2RequestPolicyType]` — Policy type
    
</dd>
</dl>

<dl>
<dd>

**policy_compliance_standard:** `typing.Optional[str]` — Policy compliance standard name
    
</dd>
</dl>

<dl>
<dd>

**policy_compliance_requirement:** `typing.Optional[str]` — Policy compliance requirement name
    
</dd>
</dl>

<dl>
<dd>

**policy_compliance_section:** `typing.Optional[str]` — Policy compliance section ID
    
</dd>
</dl>

<dl>
<dd>

**policy_remediable:** `typing.Optional[GetAlertsV2RequestPolicyRemediable]` — Policy is remediable
    
</dd>
</dl>

<dl>
<dd>

**alert_rule_name:** `typing.Optional[str]` — Alert rule name
    
</dd>
</dl>

<dl>
<dd>

**resource_id:** `typing.Optional[str]` — Resource ID
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `typing.Optional[str]` — Resource name
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `typing.Optional[str]` — Resource TYPE
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">post_alerts_v2</a>(...) -> PagedResultsAlertModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of alerts that matches the constraints specified in the body parameters.  

The **fields** request body parameter allows you to request specific fields from the alert payload. 
These fields are separate from the filters you specify. The following are valid **fields** items.

* alert.id
* alert.status
* alert.time
* cloud.account
* cloud.accountId
* cloud.region
* resource.id
* resource.name
* policy.name
* policy.type
* policy.severity

The **filters** request body parameter enables you to narrow your request for alerts. See 
[List Alert Filters](/prisma-cloud/api/cspm/get-alert-filter-and-options) 
for an API request to list all the valid filters.

You can find the valid values for the **sortBy** request body parameter in the response 
object attribute **sortAllowedColumns**.

Data in the response object does not include alert rules.

Also, in the response object:

* Property **riskDetail** is deprecated.
* Property **items[].resource.cloudServiceName** is populated only for alerts whose resources belong to a cloud service.

When `detailed` flag is set to **true**, following fields will be returned within the policy response object:

- `complianceMetadata`
- `name`
- `description`
- `labels`
- `deleted`
- `recommendation`
- `lastModifiedBy`
- `lastModifiedOn`
- `severity`

#### Rate Limits ####

The following rate limits apply:
* Request rate limit: 2/sec 
* Burst limit: 10/sec 
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
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.post_alerts_v2()

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

**request:** `FilterModel` 
    
</dd>
</dl>

<dl>
<dd>

**detailed:** `typing.Optional[bool]` — true = Return detailed alert data. Default is false. Overrides **detailed** in body param.
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">get_alerts_grouped</a>(...) -> typing.List[AlertModel]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns alert counts grouped by policy. You can use query parameters to narrow the response.  

In the response object:

* Property **alertRules** is not populated.         
* Property **riskDetail** is deprecated.
* Property **resource.cloudServiceName** is not populated.

#### Rate Limits ####

The following rate limits apply:
* Request rate limit: 1/sec 
* Burst limit: 5/sec        
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
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.get_alerts_grouped()

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

**alert_id:** `typing.Optional[str]` — Alert ID
    
</dd>
</dl>

<dl>
<dd>

**alert_status:** `typing.Optional[GetAlertsGroupedRequestAlertStatus]` — Alert status
    
</dd>
</dl>

<dl>
<dd>

**cloud_account:** `typing.Optional[str]` — Cloud account
    
</dd>
</dl>

<dl>
<dd>

**cloud_account_id:** `typing.Optional[str]` — Cloud account Id
    
</dd>
</dl>

<dl>
<dd>

**account_group:** `typing.Optional[str]` — Account group
    
</dd>
</dl>

<dl>
<dd>

**cloud_type:** `typing.Optional[str]` — Cloud type
    
</dd>
</dl>

<dl>
<dd>

**cloud_region:** `typing.Optional[str]` — Cloud region
    
</dd>
</dl>

<dl>
<dd>

**cloud_service:** `typing.Optional[str]` — Cloud service
    
</dd>
</dl>

<dl>
<dd>

**policy_id:** `typing.Optional[str]` — Policy ID
    
</dd>
</dl>

<dl>
<dd>

**policy_name:** `typing.Optional[str]` — Policy name
    
</dd>
</dl>

<dl>
<dd>

**policy_severity:** `typing.Optional[GetAlertsGroupedRequestPolicySeverity]` — Policy severity
    
</dd>
</dl>

<dl>
<dd>

**policy_label:** `typing.Optional[str]` — Policy label
    
</dd>
</dl>

<dl>
<dd>

**policy_type:** `typing.Optional[GetAlertsGroupedRequestPolicyType]` — Policy type
    
</dd>
</dl>

<dl>
<dd>

**policy_compliance_standard:** `typing.Optional[str]` — Policy compliance standard name
    
</dd>
</dl>

<dl>
<dd>

**policy_compliance_requirement:** `typing.Optional[str]` — Policy compliance requirement name
    
</dd>
</dl>

<dl>
<dd>

**policy_compliance_section:** `typing.Optional[str]` — Policy compliance section ID
    
</dd>
</dl>

<dl>
<dd>

**policy_remediable:** `typing.Optional[GetAlertsGroupedRequestPolicyRemediable]` — Policy is remediable
    
</dd>
</dl>

<dl>
<dd>

**alert_rule_name:** `typing.Optional[str]` — Alert rule name
    
</dd>
</dl>

<dl>
<dd>

**resource_id:** `typing.Optional[str]` — Resource ID
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `typing.Optional[str]` — Resource name
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `typing.Optional[str]` — Resource TYPE
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">post_alerts_grouped</a>(...) -> typing.List[AlertModel]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns alert counts grouped by policy. You can use body parameters to narrow the response.  

In the response object:

* Property **alertRules** is not populated.       
* Property **riskDetail** is deprecated.
* Property **resource.cloudServiceName** is not populated.

#### Rate Limits ####

The following rate limits apply:
* Request rate limit: 1/sec 
* Burst limit: 5/sec        
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
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.post_alerts_grouped()

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

**request:** `FilterModel` 
    
</dd>
</dl>

<dl>
<dd>

**detailed:** `typing.Optional[bool]` — true = Return detailed alert data. Default is false. Overrides **detailed** in body param.
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">get_alert</a>(...) -> AlertModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about an alert for the specified ID.  

In the response object, field **riskDetail** is deprecated.

When `detailed` flag is set to **true**, following fields will be returned within the policy and response object:

- `complianceMetadata`
- `name`
- `description`
- `labels`
- `deleted`
- `recommendation`
- `lastModifiedBy`
- `lastModifiedOn`
- `severity`

The `resource` response object will include `cloudAccountGroups` field when `detailed` is set to **true**

#### Rate Limits ####

The following rate limits apply:
* Request rate limit: 5/sec 
* Burst limit: 10/sec        
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
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.get_alert(
    id="id",
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

**id:** `str` — Alert ID
    
</dd>
</dl>

<dl>
<dd>

**detailed:** `typing.Optional[bool]` — true = Return detailed alert data. Default is false.
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">dismiss_alerts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Dismisses one or more alerts on the Prisma Cloud platform. If the caller specifies a dismissal time range, then alerts will snooze for that time period rather than be dismissed.
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
from fern import FernApi, AlertStatusChangeRequestModelFilter
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.dismiss_alerts(
    filter=AlertStatusChangeRequestModelFilter(),
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

**request:** `AlertStatusChangeRequestModel` 
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">is_dismissal_note_required</a>() -> RequireDismissalNoteConfigModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Indicates whether or not the user is required to specify a reason (dismissal note) when dismissing an alert.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.is_dismissal_note_required()

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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">set_dismissal_note_required</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manages whether or not a user must provide a reason (dismissal note) when dismissing an alert on the Prisma Cloud platform.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.set_dismissal_note_required()

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

**request:** `RequireDismissalNoteConfigModel` 
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">reopen_alerts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets the status of one or more dismissed or snoozed alerts on the Prisma Cloud platform to **open**.
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
from fern import FernApi, AlertStatusChangeRequestModelFilter
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.reopen_alerts(
    filter=AlertStatusChangeRequestModelFilter(),
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

**request:** `AlertStatusChangeRequestModel` 
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">get_alert_count</a>(...) -> CountModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an alert count for the specified status.  

#### Rate Limits ####

The following rate limits apply:
* Request rate limit: 2/sec 
* Burst limit: 10/sec
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
from fern.alerts import GetAlertCountRequestStatus

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.get_alert_count(
    status=GetAlertCountRequestStatus.OPEN,
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

**status:** `GetAlertCountRequestStatus` — Alert Status
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">submit_job_for_listing_alerts</a>(...) -> AsyncJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits a job to generate an alerts list that matches the constraints in the body parameters and is downloadable in JSON format. Returns the job ID and job submission status.  

Filter model fields specific to pagination (**sortBy**, **limit**, and **pageToken**) do not apply to this request, 
even though the body parameters include them.

The **fields** body parameter allows you to request specific fields from the alert payload. These 
fields are separate from the filters you specify. The following are valid **fields** items.

* alert.id
* alert.status
* alert.time
* cloud.account
* cloud.accountId
* cloud.region
* resource.id
* resource.name
* policy.name
* policy.type
* policy.severity

 The **filters** body parameter enables you to narrow your request for alerts. See 
 [List Alert Filters](/prisma-cloud/api/cspm/get-alert-filter-and-options) 
 for an API request to list all the valid filters.

  #### Rate Limits ####

The following rate limits apply:
* Request rate limit: 2/sec 
* Burst limit: 10/sec        
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
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.submit_job_for_listing_alerts()

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

**request:** `FilterModel` 
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">get_alerts_job_status</a>(...) -> AsyncJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of the alerts list job with the specified job ID
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
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.get_alerts_job_status(
    id="id",
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

**id:** `str` 
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">download_alerts_list_json</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Downloads the generated alerts list in JSON format for the specified job ID.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.download_alerts_list_json(
    id="id",
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

**id:** `str` — Job ID
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">submit_an_alert_csv_download_job</a>(...) -> AsyncJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits a job to generate an alerts list that matches the constraints in the body parameters and is downloadable as a CSV file. Returns the job ID and job submission status.  

Filter model fields specific to pagination (**sortBy**, **limit**, and **pageToken**) do not apply to this request, 
even though the body parameters include them.

The **fields** request body parameter is ignored!

The **filters** body parameter enables you to narrow your request for alerts. See [List Alert Filters](/prisma-cloud/api/cspm/get-alert-filter-and-options) 
for an API request to list all the valid filters.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.submit_an_alert_csv_download_job()

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

**request:** `FilterModel` 
    
</dd>
</dl>

<dl>
<dd>

**detailed:** `typing.Optional[bool]` — true = Return detailed alert data. Default is false. Overrides **detailed** in body param.
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">get_alert_csv_job_status</a>(...) -> AsyncJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the status of an alert CSV generation job with the specified job ID.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.get_alert_csv_job_status(
    id="id",
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

**id:** `str` 
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">download_alert_csv</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Downloads the alert list that Prisma Cloud generated for the specified job ID, in CSV format.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.download_alert_csv(
    id="id",
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

**id:** `str` — Job ID
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">submit_a_job_for_listing_alerts_grouped_by_policy</a>(...) -> AsyncJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits a job to generate a list of alerts grouped by the policy they violated. Returns the job ID and job submission status.  

Filter model fields specific to pagination (**sortBy**, **limit**, and **pageToken**) do not apply to this request, 
even though the body parameters include them.

The **fields** body parameter allows you to request specific fields from the alert payload. These 
fields are separate from the filters you specify. The following are valid **fields** items.

* alert.id
* alert.status
* alert.time
* cloud.account
* cloud.accountId
* cloud.region
* resource.id
* resource.name
* policy.name
* policy.type
* policy.severity

The **filters*8 body parameter enables you to narrow your request for alerts. 
See [List Alert Filters](/prisma-cloud/api/cspm/get-alert-filter-and-options)
for an API request to list all the valid filters.

#### Rate Limits ####

The following rate limits apply:
* Request rate limit: 1/sec 
* Burst limit: 5/sec        
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
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.submit_a_job_for_listing_alerts_grouped_by_policy()

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

**request:** `FilterModel` 
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">get_async_policy_alert_job_status</a>(...) -> AsyncJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the status of a job submitted to list alerts by policy. Uses the specified job ID to identify the job.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.get_async_policy_alert_job_status(
    id="id",
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

**id:** `str` — Job ID
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">download_policy_alerts_json</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Downloads the policy alerts results in JSON format for the specified job ID.
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
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.download_policy_alerts_json(
    id="id",
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

**id:** `str` — Job ID
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">get_alerts_remediation</a>(...) -> RemediationCliModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates and returns a list of remediation commands for the specified alerts and policies. Data returned for a successful call include fully constructed commands for remediation.  

This request requires the following filter request body parameters:

* filter.timeRange.type
* filter.timeRange.value

The rest of the filter parameters are ignored.
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
from fern.alerts import AlertsLookupKeyModelFilter

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.get_alerts_remediation(
    filter=AlertsLookupKeyModelFilter(),
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

**filter:** `AlertsLookupKeyModelFilter` — Filter to narrow or manage the search
    
</dd>
</dl>

<dl>
<dd>

**alerts:** `typing.Optional[typing.List[str]]` — List of alert IDs. One or more alert IDs associated with a single policy are required if no policies are specified. If a policy is specified, then all the alerts specified must belong to that policy.
    
</dd>
</dl>

<dl>
<dd>

**policies:** `typing.Optional[typing.List[str]]` — List of policy IDs. A single policy ID is required if no alerts are specified.
    
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

<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">perform_remediation_for_alert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remediates the alert with the specified ID if that alert is associated with a remediable policy. 
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
    environment=FernApiEnvironment.DEFAULT,
)

client.alerts.perform_remediation_for_alert(
    id="id",
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

**id:** `str` — Alert ID
    
</dd>
</dl>

<dl>
<dd>

**finding_id:** `typing.Optional[str]` 
    
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

