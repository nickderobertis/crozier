# Reference
## Reports
<details><summary><code>client.reports.<a href="src/fern/reports/client.py">list_reports</a>(...) -> typing.List[ReportGenerationConfigApiModel]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of compliance report generation configurations, including the ID for each configuration. Accepts query parameters to narrow the list.  

Optional query parameters are available to narrow the reports list request. See 
[Get Report Overview Filters and Options](/prisma-cloud/api/cspm/get-report-filters-and-options) 
for the REST API request to get the available query parameters.
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

client.reports.list_reports()

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

**cloud_account:** `typing.Optional[str]` — Cloud account
    
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

**account_group:** `typing.Optional[str]` — Account group
    
</dd>
</dl>

<dl>
<dd>

**policy_compliance_standard:** `typing.Optional[str]` — Policy compliance standard name
    
</dd>
</dl>

<dl>
<dd>

**report_frequency:** `typing.Optional[ListReportsRequestReportFrequency]` — Report frequency
    
</dd>
</dl>

<dl>
<dd>

**report_schedule:** `typing.Optional[ListReportsRequestReportSchedule]` — Report schedule
    
</dd>
</dl>

<dl>
<dd>

**report_email_recipients:** `typing.Optional[str]` — Report email recipients
    
</dd>
</dl>

<dl>
<dd>

**report_view:** `typing.Optional[ListReportsRequestReportView]` — Report type. Default is COMPLIANCE
    
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

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">save_report</a>(...) -> ReportGenerationConfigApiModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a compliance report generation configuration based on the specified parameters. Report generation can be either one-time or recurring.
:::info
 **Replacement  Endpoint: [Add Report Config V2](/prisma-cloud/api/cspm/save-report-v-2)**
:::

  

You can use the body parameters to specify whether the report is a one-time report 
or a recurring report. Specify a recurring report by providing a valid 
**target.schedule** body parameter.
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
from fern import FernApi, ReportGenerationConfigApiModelCloudType
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.reports.save_report(
    cloud_type=ReportGenerationConfigApiModelCloudType.AWS,
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

**request:** `ReportGenerationConfigApiModel` 
    
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

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">save_report_v2</a>(...) -> ReportGenerationConfigApiModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a compliance report generation configuration based on the specified parameters. Report generation can be either one-time or recurring.  

You can use the body parameters to specify whether the report is a one-time report 
or a recurring report. Specify a recurring report by providing a valid 
**target.schedule** body parameter.

**Note:** The `complianceStandardIds` parameter is not applicable to `COMPLIANCE` or `RIS` report types
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
from fern.reports import BaseReportGenerationConfigApiModelCloudType

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.reports.save_report_v2(
    cloud_type=BaseReportGenerationConfigApiModelCloudType.AWS,
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

**cloud_type:** `BaseReportGenerationConfigApiModelCloudType` — Cloud type
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Report name
    
</dd>
</dl>

<dl>
<dd>

**counts:** `typing.Optional[BaseReportGenerationConfigApiModelCounts]` — Model for compliance aggregate count
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — Locale of caller (e.g. en_us, jp). Default is en_us.
    
</dd>
</dl>

<dl>
<dd>

**target:** `typing.Optional[BaseReportGenerationConfigApiModelTarget]` — Report definition
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[BaseReportGenerationConfigApiModelType]` — Report type. Default is COMPLIANCE.
    
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

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">get_report_types</a>() -> typing.Dict[str, typing.List[str]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of the compliance report types and identifies which report types are available for each cloud type.
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

client.reports.get_report_types()

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

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">get_specified_report</a>(...) -> ReportGenerationConfigApiModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the compliance report generation configuration with the specified ID. The response includes pass/fail counts for this ID.
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

client.reports.get_specified_report(
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

**id:** `str` — Report ID
    
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

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">update_report</a>(...) -> ReportGenerationConfigApiModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the compliance report generation configuration with the specified ID.   

You can update a recurring report schedule through this request. 
When using this request to update a report schedule, the only body 
parameter that is required is **target**.
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
from fern import FernApi, ReportGenerationConfigApiModelCloudType
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.reports.update_report(
    id_="id",
    cloud_type=ReportGenerationConfigApiModelCloudType.AWS,
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

**id:** `str` — Report ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `ReportGenerationConfigApiModel` 
    
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

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">delete_report</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the compliance report generation configuration with the specified ID.
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

client.reports.delete_report(
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

**id:** `str` — Report ID
    
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

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">download_report</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Downloads the compliance report with the specified ID. If the report is scheduled, then the request downloads the latest generated report.
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

client.reports.download_report(
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

**id:** `str` — Report ID
    
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

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">get_historical_report_by_id</a>(...) -> typing.List[ReportGenerationConfigApiModel]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of metadata for the scheduled compliance reports that have been run for the specified report ID.
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

client.reports.get_historical_report_by_id(
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

**id:** `str` — Report ID
    
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

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">get_last_scheduled_report_by_id</a>(...) -> ReportGenerationConfigApiModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for the scheduled compliance report that has the specified report ID and was generated on the given timestamp. Returned data includes pass/fail counts.
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

client.reports.get_last_scheduled_report_by_id(
    id="id",
    last_scheduled=1000000,
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

**id:** `str` — Report ID
    
</dd>
</dl>

<dl>
<dd>

**last_scheduled:** `int` — Timestamp of report generation
    
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

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">download_historical_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Downloads the compliance report that has the specified report ID and was generated on the specified timestamp.
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

client.reports.download_historical_by_id(
    id="id",
    last_scheduled=1000000,
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

**id:** `str` — Report ID
    
</dd>
</dl>

<dl>
<dd>

**last_scheduled:** `int` — Timestamp of report generation
    
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

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">get_report_filters_and_options</a>() -> ReportFilterSuggestion</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an object whose key/value pairs identify filter options for compliance posture data. The keys are supported filters, and the corresponding values identify the available and saved filter options.  

The keys in the response object are the filter names you can use in 
[List Report Overview Filter Autocomplete Suggestions](/prisma-cloud/api/cspm/get-report-posture-filter-options).
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

client.reports.get_report_filters_and_options()

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

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">get_report_posture_filter_options</a>(...) -> ParsedTableFilter</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the available options for a specific report posture filter. Also supports fuzzy autocomplete search for easier filtering.  

You can find the available filter names through 
[Get Report Overview Filters and Options request](/prisma-cloud/api/cspm/get-report-filters-and-options). 
The keys in the response object from that GET request are 
the available filter names.
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

client.reports.get_report_posture_filter_options(
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

