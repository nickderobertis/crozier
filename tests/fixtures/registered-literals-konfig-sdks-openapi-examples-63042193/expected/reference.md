# Reference
## Context
<details><summary><code>client.context.<a href="src/fern/context/client.py">listownercontexts</a>(...) -> ContextListOwnerContextsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all contexts for an owner.
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

client.context.listownercontexts()

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

**owner_id:** `typing.Optional[str]` — The unique ID of the owner of the context. Specify either this or owner-slug.
    
</dd>
</dl>

<dl>
<dd>

**owner_slug:** `typing.Optional[str]` — A string that represents an organization. Specify either this or owner-id. Cannot be used for accounts.
    
</dd>
</dl>

<dl>
<dd>

**owner_type:** `typing.Optional[ContextListOwnerContextsRequestOwnerType]` — The type of the owner. Defaults to "organization". Accounts are only used as context owners in server.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — A token to retrieve the next page of results.
    
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

<details><summary><code>client.context.<a href="src/fern/context/client.py">createnewcontext</a>(...) -> ContextCreateNewContextResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new context.
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
from fern.context import ContextCreateNewContextRequestOwnerId

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.context.createnewcontext(
    name="name",
    owner=ContextCreateNewContextRequestOwnerId(
        id="id",
    ),
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

**name:** `str` — The user defined name of the context.
    
</dd>
</dl>

<dl>
<dd>

**owner:** `ContextCreateNewContextRequestOwner` 
    
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

<details><summary><code>client.context.<a href="src/fern/context/client.py">getinformation</a>(...) -> ContextGetInformationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns basic information about a context.
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

client.context.getinformation(
    context_id="context-id",
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

**context_id:** `str` — ID of the context (UUID)
    
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

<details><summary><code>client.context.<a href="src/fern/context/client.py">removecontext</a>(...) -> ContextRemoveContextResponse</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.context.removecontext(
    context_id="context-id",
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

**context_id:** `str` — ID of the context (UUID)
    
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

<details><summary><code>client.context.<a href="src/fern/context/client.py">listenvironmentvariables</a>(...) -> ContextListEnvironmentVariablesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List information about environment variables in a context, not including their values.
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

client.context.listenvironmentvariables(
    context_id="context-id",
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

**context_id:** `str` — ID of the context (UUID)
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — A token to retrieve the next page of results.
    
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

<details><summary><code>client.context.<a href="src/fern/context/client.py">updateenvironmentvariable</a>(...) -> ContextUpdateEnvironmentVariableResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update an environment variable within a context. Returns information about the environment variable, not including its value.
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

client.context.updateenvironmentvariable(
    context_id="context-id",
    env_var_name="POSTGRES_USER",
    value="some-secret-value",
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

**context_id:** `str` — ID of the context (UUID)
    
</dd>
</dl>

<dl>
<dd>

**env_var_name:** `str` — The name of the environment variable
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — The value of the environment variable
    
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

<details><summary><code>client.context.<a href="src/fern/context/client.py">removeenvironmentvariable</a>(...) -> ContextRemoveEnvironmentVariableResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an environment variable from a context.
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

client.context.removeenvironmentvariable(
    context_id="context-id",
    env_var_name="POSTGRES_USER",
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

**context_id:** `str` — ID of the context (UUID)
    
</dd>
</dl>

<dl>
<dd>

**env_var_name:** `str` — The name of the environment variable
    
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

<details><summary><code>client.context.<a href="src/fern/context/client.py">getrestrictions</a>(...) -> ContextProjectRestrictionsList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[__EXPERIMENTAL__] Gets a list of project restrictions associated with a context.
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

client.context.getrestrictions(
    context_id="be8bb2e3-c3d6-4098-89f4-572ff976ba9a",
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

**context_id:** `str` — An opaque identifier of a context.
    
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

<details><summary><code>client.context.<a href="src/fern/context/client.py">createrestriction</a>(...) -> RestrictionCreated</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[__EXPERIMENTAL__] Creates project restriction on a context.
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

client.context.createrestriction(
    context_id="be8bb2e3-c3d6-4098-89f4-572ff976ba9a",
    restriction_type="project",
    restriction_value="405d8375-3514-403b-8c43-83ae74cfe0e9",
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

**context_id:** `str` — An opaque identifier of a context.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` 

Deprecated - Use "restriction_type" and "restriction_value"
instead.

The project ID to use for a project restriction. This is
mutually exclusive with restriction_type and restriction_value
and implies restriction_type is "project".
    
</dd>
</dl>

<dl>
<dd>

**restriction_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**restriction_value:** `typing.Optional[str]` 
    
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

<details><summary><code>client.context.<a href="src/fern/context/client.py">deleterestriction</a>(...) -> RestrictionDeleted</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[__EXPERIMENTAL__] Deletes a project restriction on a context.
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

client.context.deleterestriction(
    context_id="be8bb2e3-c3d6-4098-89f4-572ff976ba9a",
    restriction_id="1c23d2cb-07b1-4a28-8af3-e369732050ed",
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

**context_id:** `str` — An opaque identifier of a context.
    
</dd>
</dl>

<dl>
<dd>

**restriction_id:** `str` — An opaque identifier of a context restriction.
    
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

## Insights
<details><summary><code>client.insights.<a href="src/fern/insights/client.py">getprojectsummarymetrics</a>(...) -> InsightsGetProjectSummaryMetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get summary metrics and trends for a project at workflow and branch level.
             Workflow runs going back at most 90 days are included in the aggregation window.
             Trends are only supported upto last 30 days.
             Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.
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

client.insights.getprojectsummarymetrics(
    project_slug="gh/CircleCI-Public/api-preview-docs",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**reporting_window:** `typing.Optional[InsightsGetProjectSummaryMetricsRequestReportingWindow]` — The time window used to calculate summary metrics. If not provided, defaults to last-90-days
    
</dd>
</dl>

<dl>
<dd>

**branches:** `typing.Optional[typing.Dict[str, typing.Any]]` — The names of VCS branches to include in branch-level workflow metrics.
    
</dd>
</dl>

<dl>
<dd>

**workflow_names:** `typing.Optional[typing.Dict[str, typing.Any]]` — The names of workflows to include in workflow-level metrics.
    
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

<details><summary><code>client.insights.<a href="src/fern/insights/client.py">getjobtimeseriesdata</a>(...) -> InsightsGetJobTimeseriesDataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get timeseries data for all jobs within a workflow. Hourly granularity data is only retained for 48 hours while daily granularity data is retained for 90 days.
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
import datetime

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.insights.getjobtimeseriesdata(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    workflow_name="build-and-test",
    start_date=datetime.datetime.fromisoformat("2020-08-21T13:26:29+00:00"),
    end_date=datetime.datetime.fromisoformat("2020-09-04T13:26:29+00:00"),
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**workflow_name:** `str` — The name of the workflow.
    
</dd>
</dl>

<dl>
<dd>

**branch:** `typing.Optional[str]` — The name of a vcs branch. If not passed we will scope the API call to the default branch.
    
</dd>
</dl>

<dl>
<dd>

**granularity:** `typing.Optional[InsightsGetJobTimeseriesDataRequestGranularity]` — The granularity for which to query timeseries data.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — Include only executions that started at or after this date. This must be specified if an end-date is provided.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — Include only executions that started before this date. This date can be at most 90 days after the start-date.
    
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

<details><summary><code>client.insights.<a href="src/fern/insights/client.py">getsummarymetricswithtrends</a>(...) -> InsightsGetSummaryMetricsWithTrendsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets aggregated summary metrics with trends for the entire org.
              Also gets aggregated metrics and trends for each project belonging to the org.
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

client.insights.getsummarymetricswithtrends(
    org_slug="gh/CircleCI-Public",
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

**org_slug:** `str` — Org slug in the form `vcs-slug/org-name`. The `/` characters may be URL-escaped.
    
</dd>
</dl>

<dl>
<dd>

**reporting_window:** `typing.Optional[InsightsGetSummaryMetricsWithTrendsRequestReportingWindow]` — The time window used to calculate summary metrics. If not provided, defaults to last-90-days
    
</dd>
</dl>

<dl>
<dd>

**project_names:** `typing.Optional[typing.Dict[str, typing.Any]]` — List of project names.
    
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

<details><summary><code>client.insights.<a href="src/fern/insights/client.py">listprojectbranches</a>(...) -> InsightsListProjectBranchesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all branches for a specified project. The list will only contain branches currently available within Insights. The maximum number of branches returned by this endpoint is 5,000.
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

client.insights.listprojectbranches(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    workflow_name="build-and-test",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**workflow_name:** `typing.Optional[str]` — The name of a workflow. If not passed we will scope the API call to the project.
    
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

<details><summary><code>client.insights.<a href="src/fern/insights/client.py">getflakytests</a>(...) -> InsightsGetFlakyTestsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of flaky tests for a given project. Flaky tests are branch agnostic.
             A flaky test is a test that passed and failed in the same commit.
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

client.insights.getflakytests(
    project_slug="gh/CircleCI-Public/api-preview-docs",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
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

<details><summary><code>client.insights.<a href="src/fern/insights/client.py">getprojectworkflowmetrics</a>(...) -> InsightsGetProjectWorkflowMetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get summary metrics for a project's workflows.  Workflow runs going back at most 90 days are included in the aggregation window. Metrics are refreshed daily, and thus may not include executions from the last 24 hours.  Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.
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

client.insights.getprojectworkflowmetrics(
    project_slug="gh/CircleCI-Public/api-preview-docs",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — A token to retrieve the next page of results.
    
</dd>
</dl>

<dl>
<dd>

**all_branches:** `typing.Optional[bool]` — Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter.
    
</dd>
</dl>

<dl>
<dd>

**branch:** `typing.Optional[str]` — The name of a vcs branch. If not passed we will scope the API call to the default branch.
    
</dd>
</dl>

<dl>
<dd>

**reporting_window:** `typing.Optional[InsightsGetProjectWorkflowMetricsRequestReportingWindow]` — The time window used to calculate summary metrics. If not provided, defaults to last-90-days
    
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

<details><summary><code>client.insights.<a href="src/fern/insights/client.py">getrecentworkflowruns</a>(...) -> InsightsGetRecentWorkflowRunsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get recent runs of a workflow. Runs going back at most 90 days are returned. Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.
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
import datetime

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.insights.getrecentworkflowruns(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    workflow_name="build-and-test",
    start_date=datetime.datetime.fromisoformat("2020-08-21T13:26:29+00:00"),
    end_date=datetime.datetime.fromisoformat("2020-09-04T13:26:29+00:00"),
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**workflow_name:** `str` — The name of the workflow.
    
</dd>
</dl>

<dl>
<dd>

**all_branches:** `typing.Optional[bool]` — Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter.
    
</dd>
</dl>

<dl>
<dd>

**branch:** `typing.Optional[str]` — The name of a vcs branch. If not passed we will scope the API call to the default branch.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — A token to retrieve the next page of results.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — Include only executions that started at or after this date. This must be specified if an end-date is provided.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — Include only executions that started before this date. This date can be at most 90 days after the start-date.
    
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

<details><summary><code>client.insights.<a href="src/fern/insights/client.py">getprojectworkflowjobmetrics</a>(...) -> InsightsGetProjectWorkflowJobMetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get summary metrics for a project workflow's jobs. Job runs going back at most 90 days are included in the aggregation window. Metrics are refreshed daily, and thus may not include executions from the last 24 hours. Please note that Insights is not a financial reporting tool and should not be used for precise credit reporting.  Credit reporting from Insights does not use the same source of truth as the billing information that is found in the Plan Overview page in the CircleCI UI, nor does the underlying data have the same data accuracy guarantees as the billing information in the CircleCI UI.  This may lead to discrepancies between credits reported from Insights and the billing information in the Plan Overview page of the CircleCI UI.  For precise credit reporting, always use the Plan Overview page in the CircleCI UI.
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

client.insights.getprojectworkflowjobmetrics(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    workflow_name="build-and-test",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**workflow_name:** `str` — The name of the workflow.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — A token to retrieve the next page of results.
    
</dd>
</dl>

<dl>
<dd>

**all_branches:** `typing.Optional[bool]` — Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter.
    
</dd>
</dl>

<dl>
<dd>

**branch:** `typing.Optional[str]` — The name of a vcs branch. If not passed we will scope the API call to the default branch.
    
</dd>
</dl>

<dl>
<dd>

**reporting_window:** `typing.Optional[InsightsGetProjectWorkflowJobMetricsRequestReportingWindow]` — The time window used to calculate summary metrics. If not provided, defaults to last-90-days
    
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

<details><summary><code>client.insights.<a href="src/fern/insights/client.py">getworkflowsummarymetrics</a>(...) -> InsightsGetWorkflowSummaryMetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the metrics and trends for a particular workflow on a single branch or all branches
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

client.insights.getworkflowsummarymetrics(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    workflow_name="build-and-test",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**workflow_name:** `str` — The name of the workflow.
    
</dd>
</dl>

<dl>
<dd>

**all_branches:** `typing.Optional[bool]` — Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter.
    
</dd>
</dl>

<dl>
<dd>

**branch:** `typing.Optional[str]` — The name of a vcs branch. If not passed we will scope the API call to the default branch.
    
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

<details><summary><code>client.insights.<a href="src/fern/insights/client.py">getprojectworkflowtestmetrics</a>(...) -> InsightsGetProjectWorkflowTestMetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get test metrics for a project's workflows. Currently tests metrics are calculated based on 10 most recent workflow runs.
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

client.insights.getprojectworkflowtestmetrics(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    workflow_name="build-and-test",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**workflow_name:** `str` — The name of the workflow.
    
</dd>
</dl>

<dl>
<dd>

**branch:** `typing.Optional[str]` — The name of a vcs branch. If not passed we will scope the API call to the default branch.
    
</dd>
</dl>

<dl>
<dd>

**all_branches:** `typing.Optional[bool]` — Whether to retrieve data for all branches combined. Use either this parameter OR the branch name parameter.
    
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

## User
<details><summary><code>client.user.<a href="src/fern/user/client.py">getinformation</a>() -> UserGetInformationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides information about the user that is currently signed in.
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

client.user.getinformation()

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

<details><summary><code>client.user.<a href="src/fern/user/client.py">listcollaborations</a>() -> UserListCollaborationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides the set of organizations of which a user is a member or a collaborator.

The set of organizations that a user can collaborate on is composed of:

* Organizations that the current user belongs to across VCS types (e.g. BitBucket, GitHub)
* The parent organization of repository that the user can collaborate on, but is not necessarily a member of
* The organization of the current user's account
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

client.user.listcollaborations()

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

<details><summary><code>client.user.<a href="src/fern/user/client.py">getuserinformation</a>(...) -> UserGetUserInformationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides information about the user with the given ID.
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

client.user.getuserinformation(
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

**id:** `str` — The unique ID of the user.
    
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

## Pipeline
<details><summary><code>client.pipeline.<a href="src/fern/pipeline/client.py">listrecentpipelines</a>(...) -> PipelineListRecentPipelinesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all pipelines for the most recently built projects (max 250) you follow in an organization.
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

client.pipeline.listrecentpipelines(
    org_slug="gh/CircleCI-Public",
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

**org_slug:** `typing.Optional[str]` — Org slug in the form `vcs-slug/org-name`. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug` and replace the `org-name` with the organization ID (found in Organization Settings).
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — A token to retrieve the next page of results.
    
</dd>
</dl>

<dl>
<dd>

**mine:** `typing.Optional[bool]` — Only include entries created by your user.
    
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

<details><summary><code>client.pipeline.<a href="src/fern/pipeline/client.py">continueexecution</a>(...) -> PipelineContinueExecutionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Continue a pipeline from the setup phase. For information on using pipeline parameters with dynamic configuration, see the [Pipeline values and parameters](https://circleci.com/docs/pipeline-variables/#pipeline-parameters-and-dynamic-configuration) docs.
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

client.pipeline.continueexecution(
    continuation_key="continuation-key",
    configuration="configuration",
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

**continuation_key:** `str` — A pipeline continuation key.
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `str` — A configuration string for the pipeline.
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.Dict[str, PipelineContinueExecutionRequestParametersValue]]` — An object containing pipeline parameters and their values.
    
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

<details><summary><code>client.pipeline.<a href="src/fern/pipeline/client.py">getbyid</a>(...) -> PipelineGetByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a pipeline by the pipeline ID.
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

client.pipeline.getbyid(
    pipeline_id="5034460f-c7c4-4c43-9457-de07e2029e7b",
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

**pipeline_id:** `str` — The unique ID of the pipeline.
    
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

<details><summary><code>client.pipeline.<a href="src/fern/pipeline/client.py">getconfigurationbyid</a>(...) -> PipelineGetConfigurationByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a pipeline's configuration by ID.
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

client.pipeline.getconfigurationbyid(
    pipeline_id="5034460f-c7c4-4c43-9457-de07e2029e7b",
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

**pipeline_id:** `str` — The unique ID of the pipeline.
    
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

<details><summary><code>client.pipeline.<a href="src/fern/pipeline/client.py">listworkflows</a>(...) -> PipelineListWorkflowsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of workflows by pipeline ID.
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

client.pipeline.listworkflows(
    pipeline_id="5034460f-c7c4-4c43-9457-de07e2029e7b",
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

**pipeline_id:** `str` — The unique ID of the pipeline.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — A token to retrieve the next page of results.
    
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

<details><summary><code>client.pipeline.<a href="src/fern/pipeline/client.py">getallpipelines</a>(...) -> PipelineGetAllPipelinesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all pipelines for this project.
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

client.pipeline.getallpipelines(
    project_slug="gh/CircleCI-Public/api-preview-docs",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**branch:** `typing.Optional[str]` — The name of a vcs branch.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — A token to retrieve the next page of results.
    
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

<details><summary><code>client.pipeline.<a href="src/fern/pipeline/client.py">triggernewpipeline</a>(...) -> PipelineTriggerNewPipelineResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Not yet available to projects that use GitLab or GitHub App. Triggers a new pipeline on the project.
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

client.pipeline.triggernewpipeline(
    project_slug="gh/CircleCI-Public/api-preview-docs",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.Dict[str, PipelineTriggerNewPipelineRequestParametersValue]]` — An object containing pipeline parameters and their values.
    
</dd>
</dl>

<dl>
<dd>

**branch:** `typing.Optional[str]` — The branch where the pipeline ran. The HEAD commit on this branch was used for the pipeline. Note that `branch` and `tag` are mutually exclusive. To trigger a pipeline for a PR by number use `pull/<number>/head` for the PR ref or `pull/<number>/merge` for the merge ref (GitHub only).
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` — The tag used by the pipeline. The commit that this tag points to was used for the pipeline. Note that `branch` and `tag` are mutually exclusive.
    
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

<details><summary><code>client.pipeline.<a href="src/fern/pipeline/client.py">listuserpipelines</a>(...) -> PipelineListUserPipelinesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a sequence of all pipelines for this project triggered by the user.
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

client.pipeline.listuserpipelines(
    project_slug="gh/CircleCI-Public/api-preview-docs",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — A token to retrieve the next page of results.
    
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

<details><summary><code>client.pipeline.<a href="src/fern/pipeline/client.py">getbynumber</a>(...) -> PipelineGetByNumberResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a pipeline by the pipeline number.
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

client.pipeline.getbynumber(
    project_slug="project-slug",
    pipeline_number="pipeline-number",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**pipeline_number:** `typing.Any` — The number of the pipeline.
    
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

## Project
<details><summary><code>client.project.<a href="src/fern/project/client.py">getbyslug</a>(...) -> ProjectGetBySlugResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a project by project slug.
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

client.project.getbyslug(
    project_slug="gh/CircleCI-Public/api-preview-docs",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py">listcheckoutkeys</a>(...) -> ProjectListCheckoutKeysResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a sequence of checkout keys for `:project`.
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

client.project.listcheckoutkeys(
    project_slug="gh/CircleCI-Public/api-preview-docs",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**digest:** `typing.Optional[ProjectListCheckoutKeysRequestDigest]` — The fingerprint digest type to return. This may be either `md5` or `sha256`. If not passed, defaults to `md5`.
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py">createcheckoutkey</a>(...) -> ProjectCreateCheckoutKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Not available to projects that use GitLab or GitHub App. Creates a new checkout key. This API request is only usable with a user API token.
                           Please ensure that you have authorized your account with GitHub before creating user keys.
                           This is necessary to give CircleCI the permission to create a user key associated with
                           your GitHub user account. You can find this page by visiting Project Settings > Checkout SSH Keys
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
from fern.project import ProjectCreateCheckoutKeyRequestType

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.project.createcheckoutkey(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    type=ProjectCreateCheckoutKeyRequestType.USER_KEY,
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**type:** `ProjectCreateCheckoutKeyRequestType` — The type of checkout key to create. This may be either `deploy-key` or `user-key`.
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py">getcheckoutkeybyfingerprint</a>(...) -> ProjectGetCheckoutKeyByFingerprintResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an individual checkout key via md5 or sha256 fingerprint. sha256 keys should be url-encoded.
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

client.project.getcheckoutkeybyfingerprint(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    fingerprint="c9:0b:1c:4f:d5:65:56:b9:ad:88:f9:81:2b:37:74:2f",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**fingerprint:** `str` — An SSH key fingerprint.
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py">deletecheckoutkeybyfingerprint</a>(...) -> ProjectDeleteCheckoutKeyByFingerprintResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the checkout key via md5 or sha256 fingerprint. sha256 keys should be url-encoded.
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

client.project.deletecheckoutkeybyfingerprint(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    fingerprint="c9:0b:1c:4f:d5:65:56:b9:ad:88:f9:81:2b:37:74:2f",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**fingerprint:** `str` — An SSH key fingerprint.
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py">listenvvarvalues</a>(...) -> ProjectListEnvVarValuesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns four 'x' characters, in addition to the last four ASCII characters of the value, consistent with the display of environment variable values on the CircleCI website.
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

client.project.listenvvarvalues(
    project_slug="gh/CircleCI-Public/api-preview-docs",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py">createenvvar</a>(...) -> ProjectCreateEnvVarResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new environment variable.
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

client.project.createenvvar(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    name="foo",
    value="xxxx1234",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the environment variable.
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — The value of the environment variable.
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py">getmaskedenvvar</a>(...) -> ProjectGetMaskedEnvVarResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the masked value of environment variable :name.
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

client.project.getmaskedenvvar(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    name="foo",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the environment variable.
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py">deleteenvironmentvariable</a>(...) -> ProjectDeleteEnvironmentVariableResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the environment variable named :name.
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

client.project.deleteenvironmentvariable(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    name="foo",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the environment variable.
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py">createprojectdefaultsettings</a>(...) -> ProjectSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[__EXPERIMENTAL__]  Creates a new CircleCI project, and returns a list of the default advanced settings. Can only be called on a repo with a main branch and an existing config.yml file. Not yet available to projects that use GitLab or GitHub App.
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

client.project.createprojectdefaultsettings(
    provider="gh",
    organization="CircleCI-Public",
    project="api-preview-docs",
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

**provider:** `str` — The `provider` segment of a project or org slug, the first of the three. This may be a VCS. For projects that use GitLab or GitHub App, use `circleci`.
    
</dd>
</dl>

<dl>
<dd>

**organization:** `str` — The `organization` segment of a project or org slug, the second of the three. For GitHub OAuth or Bitbucket projects, this is the organization name. For projects that use GitLab or GitHub App, use the organization ID (found in Organization Settings).
    
</dd>
</dl>

<dl>
<dd>

**project:** `str` — The `project` segment of a project slug, the third of the three. For GitHub OAuth or Bitbucket projects, this is the repository name. For projects that use GitLab or GitHub App, use the project ID (found in Project Settings).
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py">getsettings</a>(...) -> ProjectSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[__EXPERIMENTAL__] Returns a list of the advanced settings for a CircleCI project, whether enabled (true) or not (false).
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

client.project.getsettings(
    provider="gh",
    organization="CircleCI-Public",
    project="api-preview-docs",
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

**provider:** `str` — The `provider` segment of a project or org slug, the first of the three. This may be a VCS. For projects that use GitLab or GitHub App, use `circleci`.
    
</dd>
</dl>

<dl>
<dd>

**organization:** `str` — The `organization` segment of a project or org slug, the second of the three. For GitHub OAuth or Bitbucket projects, this is the organization name. For projects that use GitLab or GitHub App, use the organization ID (found in Organization Settings).
    
</dd>
</dl>

<dl>
<dd>

**project:** `str` — The `project` segment of a project slug, the third of the three. For GitHub OAuth or Bitbucket projects, this is the repository name. For projects that use GitLab or GitHub App, use the project ID (found in Project Settings).
    
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

<details><summary><code>client.project.<a href="src/fern/project/client.py">updatesettings</a>(...) -> ProjectSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[__EXPERIMENTAL__] Updates one or more of the advanced settings for a CircleCI project.
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
from fern import FernApi, ProjectSettingsAdvanced
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.project.updatesettings(
    provider="gh",
    organization="CircleCI-Public",
    project="api-preview-docs",
    advanced=ProjectSettingsAdvanced(
        autocancel_builds=False,
        build_prs_only=True,
        pr_only_branch_overrides=[
            "main"
        ],
    ),
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

**provider:** `str` — The `provider` segment of a project or org slug, the first of the three. This may be a VCS. For projects that use GitLab or GitHub App, use `circleci`.
    
</dd>
</dl>

<dl>
<dd>

**organization:** `str` — The `organization` segment of a project or org slug, the second of the three. For GitHub OAuth or Bitbucket projects, this is the organization name. For projects that use GitLab or GitHub App, use the organization ID (found in Organization Settings).
    
</dd>
</dl>

<dl>
<dd>

**project:** `str` — The `project` segment of a project slug, the third of the three. For GitHub OAuth or Bitbucket projects, this is the repository name. For projects that use GitLab or GitHub App, use the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**request:** `ProjectSettings` 
    
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

## Job
<details><summary><code>client.job.<a href="src/fern/job/client.py">getdetails</a>(...) -> JobGetDetailsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns job details.
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

client.job.getdetails(
    project_slug="project-slug",
    job_number="job-number",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**job_number:** `typing.Any` — The number of the job.
    
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

<details><summary><code>client.job.<a href="src/fern/job/client.py">cancelwithnumber</a>(...) -> JobCancelWithNumberResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel job with a given job number.
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

client.job.cancelwithnumber(
    project_slug="project-slug",
    job_number="job-number",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**job_number:** `typing.Any` — The number of the job.
    
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

<details><summary><code>client.job.<a href="src/fern/job/client.py">getartifacts</a>(...) -> JobGetArtifactsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a job's artifacts.
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

client.job.getartifacts(
    project_slug="project-slug",
    job_number="job-number",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**job_number:** `typing.Any` — The number of the job.
    
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

<details><summary><code>client.job.<a href="src/fern/job/client.py">gettestmetadata</a>(...) -> JobGetTestMetadataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get test metadata for a build. In the rare case where there is more than 250MB of test data on the job, no results will be returned.
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

client.job.gettestmetadata(
    project_slug="project-slug",
    job_number="job-number",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**job_number:** `typing.Any` — The number of the job.
    
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

## Schedule
<details><summary><code>client.schedule.<a href="src/fern/schedule/client.py">getallschedules</a>(...) -> ScheduleGetAllSchedulesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all schedules for this project.
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

client.schedule.getallschedules(
    project_slug="gh/CircleCI-Public/api-preview-docs",
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — A token to retrieve the next page of results.
    
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

<details><summary><code>client.schedule.<a href="src/fern/schedule/client.py">createnewschedule</a>(...) -> ScheduleCreateNewScheduleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Not yet available to projects that use GitLab or GitHub App. Creates a schedule and returns the created schedule.
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
from fern.schedule import ScheduleCreateNewScheduleRequestTimetableZero, ScheduleCreateNewScheduleRequestTimetableZeroDaysOfWeekItem, ScheduleCreateNewScheduleRequestAttributionActor

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.schedule.createnewschedule(
    project_slug="gh/CircleCI-Public/api-preview-docs",
    parameters={
        "deploy_prod": True,
        "branch": "feature/design-new-api"
    },
    name="name",
    timetable=ScheduleCreateNewScheduleRequestTimetableZero(
        per_hour=1,
        hours_of_day=[
            1
        ],
        days_of_week=[
            ScheduleCreateNewScheduleRequestTimetableZeroDaysOfWeekItem.TUE
        ],
    ),
    attribution_actor=ScheduleCreateNewScheduleRequestAttributionActor.CURRENT,
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

**project_slug:** `str` — Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Dict[str, ScheduleCreateNewScheduleRequestParametersValue]` — Pipeline parameters represented as key-value pairs. Must contain branch or tag.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the schedule.
    
</dd>
</dl>

<dl>
<dd>

**timetable:** `ScheduleCreateNewScheduleRequestTimetable` — Timetable that specifies when a schedule triggers.
    
</dd>
</dl>

<dl>
<dd>

**attribution_actor:** `ScheduleCreateNewScheduleRequestAttributionActor` — The attribution-actor of the scheduled pipeline.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the schedule.
    
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

<details><summary><code>client.schedule.<a href="src/fern/schedule/client.py">getbyid</a>(...) -> ScheduleGetByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a schedule by id.
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

client.schedule.getbyid(
    schedule_id="schedule-id",
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

**schedule_id:** `str` — The unique ID of the schedule.
    
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

<details><summary><code>client.schedule.<a href="src/fern/schedule/client.py">removebyid</a>(...) -> ScheduleRemoveByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Not yet available to projects that use GitLab or GitHub App. Deletes the schedule by id.
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

client.schedule.removebyid(
    schedule_id="schedule-id",
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

**schedule_id:** `str` — The unique ID of the schedule.
    
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

<details><summary><code>client.schedule.<a href="src/fern/schedule/client.py">updateschedule</a>(...) -> ScheduleUpdateScheduleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Not yet available to projects that use GitLab or GitHub App. Updates a schedule and returns the updated schedule.
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

client.schedule.updateschedule(
    schedule_id="schedule-id",
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

**schedule_id:** `str` — The unique ID of the schedule.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the schedule.
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.Dict[str, ScheduleUpdateScheduleRequestParametersValue]]` — Pipeline parameters represented as key-value pairs. Must contain branch or tag.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the schedule.
    
</dd>
</dl>

<dl>
<dd>

**timetable:** `typing.Optional[ScheduleUpdateScheduleRequestTimetable]` — Timetable that specifies when a schedule triggers.
    
</dd>
</dl>

<dl>
<dd>

**attribution_actor:** `typing.Optional[ScheduleUpdateScheduleRequestAttributionActor]` — The attribution-actor of the scheduled pipeline.
    
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

## Webhook
<details><summary><code>client.webhook.<a href="src/fern/webhook/client.py">listmatchingscope</a>(...) -> WebhookListMatchingScopeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of outbound webhooks that match the given scope-type and scope-id
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
from fern.webhook import WebhookListMatchingScopeRequestScopeType

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhook.listmatchingscope(
    scope_id="scope-id",
    scope_type=WebhookListMatchingScopeRequestScopeType.PROJECT,
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

**scope_id:** `str` — ID of the scope being used (at the moment, only project ID is supported)
    
</dd>
</dl>

<dl>
<dd>

**scope_type:** `WebhookListMatchingScopeRequestScopeType` — Type of the scope being used
    
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

<details><summary><code>client.webhook.<a href="src/fern/webhook/client.py">createoutboundwebhook</a>(...) -> WebhookCreateOutboundWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an outbound webhook.
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
from fern.webhook import WebhookCreateOutboundWebhookRequestEventsItem, WebhookCreateOutboundWebhookRequestScope, WebhookCreateOutboundWebhookRequestScopeType

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhook.createoutboundwebhook(
    name="name",
    events=[
        WebhookCreateOutboundWebhookRequestEventsItem.WORKFLOW_COMPLETED
    ],
    url="url",
    verify_tls=True,
    signing_secret="signing-secret",
    scope=WebhookCreateOutboundWebhookRequestScope(
        id="id",
        type=WebhookCreateOutboundWebhookRequestScopeType.PROJECT,
    ),
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

**name:** `str` — Name of the webhook
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.List[WebhookCreateOutboundWebhookRequestEventsItem]` — Events that will trigger the webhook
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — URL to deliver the webhook to. Note: protocol must be included as well (only https is supported)
    
</dd>
</dl>

<dl>
<dd>

**verify_tls:** `bool` — Whether to enforce TLS certificate verification when delivering the webhook
    
</dd>
</dl>

<dl>
<dd>

**signing_secret:** `str` — Secret used to build an HMAC hash of the payload and passed as a header in the webhook request
    
</dd>
</dl>

<dl>
<dd>

**scope:** `WebhookCreateOutboundWebhookRequestScope` — The scope in which the relevant events that will trigger webhooks
    
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

<details><summary><code>client.webhook.<a href="src/fern/webhook/client.py">getbyid</a>(...) -> WebhookGetByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an outbound webhook by id.
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

client.webhook.getbyid(
    webhook_id="webhook-id",
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

**webhook_id:** `str` — ID of the webhook (UUID)
    
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

<details><summary><code>client.webhook.<a href="src/fern/webhook/client.py">updateoutboundwebhook</a>(...) -> WebhookUpdateOutboundWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an outbound webhook.
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

client.webhook.updateoutboundwebhook(
    webhook_id="webhook-id",
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

**webhook_id:** `str` — ID of the webhook (UUID)
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the webhook
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.Optional[typing.List[WebhookUpdateOutboundWebhookRequestEventsItem]]` — Events that will trigger the webhook
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — URL to deliver the webhook to. Note: protocol must be included as well (only https is supported)
    
</dd>
</dl>

<dl>
<dd>

**signing_secret:** `typing.Optional[str]` — Secret used to build an HMAC hash of the payload and passed as a header in the webhook request
    
</dd>
</dl>

<dl>
<dd>

**verify_tls:** `typing.Optional[bool]` — Whether to enforce TLS certificate verification when delivering the webhook
    
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

<details><summary><code>client.webhook.<a href="src/fern/webhook/client.py">deleteoutboundwebhook</a>(...) -> WebhookDeleteOutboundWebhookResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an outbound webhook
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

client.webhook.deleteoutboundwebhook(
    webhook_id="webhook-id",
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

**webhook_id:** `str` — ID of the webhook (UUID)
    
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

## Workflow
<details><summary><code>client.workflow.<a href="src/fern/workflow/client.py">getbyid</a>(...) -> WorkflowGetByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns summary fields of a workflow by ID.
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

client.workflow.getbyid(
    id="5034460f-c7c4-4c43-9457-de07e2029e7b",
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

**id:** `str` — The unique ID of the workflow.
    
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

<details><summary><code>client.workflow.<a href="src/fern/workflow/client.py">approvejob</a>(...) -> WorkflowApproveJobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Approves a pending approval job in a workflow.
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

client.workflow.approvejob(
    id="5034460f-c7c4-4c43-9457-de07e2029e7b",
    approval_request_id="approval_request_id",
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

**id:** `str` — The unique ID of the workflow.
    
</dd>
</dl>

<dl>
<dd>

**approval_request_id:** `str` — The ID of the job being approved.
    
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

<details><summary><code>client.workflow.<a href="src/fern/workflow/client.py">cancelworkflow</a>(...) -> WorkflowCancelWorkflowResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels a running workflow.
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

client.workflow.cancelworkflow(
    id="5034460f-c7c4-4c43-9457-de07e2029e7b",
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

**id:** `str` — The unique ID of the workflow.
    
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

<details><summary><code>client.workflow.<a href="src/fern/workflow/client.py">getjobs</a>(...) -> WorkflowGetJobsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a sequence of jobs for a workflow.
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

client.workflow.getjobs(
    id="5034460f-c7c4-4c43-9457-de07e2029e7b",
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

**id:** `str` — The unique ID of the workflow.
    
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

<details><summary><code>client.workflow.<a href="src/fern/workflow/client.py">rerunworkflow</a>(...) -> WorkflowRerunWorkflowResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reruns a workflow.
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

client.workflow.rerunworkflow(
    id="5034460f-c7c4-4c43-9457-de07e2029e7b",
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

**id:** `str` — The unique ID of the workflow.
    
</dd>
</dl>

<dl>
<dd>

**enable_ssh:** `typing.Optional[bool]` — Whether to enable SSH access for the triggering user on the newly-rerun job. Requires the jobs parameter to be used and so is mutually exclusive with the from_failed parameter.
    
</dd>
</dl>

<dl>
<dd>

**from_failed:** `typing.Optional[bool]` — Whether to rerun the workflow from the failed job. Mutually exclusive with the jobs parameter.
    
</dd>
</dl>

<dl>
<dd>

**jobs:** `typing.Optional[typing.List[str]]` — A list of job IDs to rerun.
    
</dd>
</dl>

<dl>
<dd>

**sparse_tree:** `typing.Optional[bool]` — Completes rerun using sparse trees logic, an optimization for workflows that have disconnected subgraphs. Requires jobs parameter and so is mutually exclusive with the from_failed parameter.
    
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

## OIDC Token Management
<details><summary><code>client.oidc_token_management.<a href="src/fern/oidc_token_management/client.py">oidc_token_management_get_org_claims</a>(...) -> ClaimResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches org-level custom claims of OIDC identity tokens
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

client.oidc_token_management.oidc_token_management_get_org_claims(
    org_id="orgID",
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

**org_id:** `str` 
    
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

<details><summary><code>client.oidc_token_management.<a href="src/fern/oidc_token_management/client.py">oidc_token_management_delete_org_claims</a>(...) -> ClaimResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes org-level custom claims of OIDC identity tokens
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

client.oidc_token_management.oidc_token_management_delete_org_claims(
    org_id="orgID",
    claims="claims",
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

**org_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**claims:** `str` — comma separated list of claims to delete. Valid values are "audience" and "ttl".
    
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

<details><summary><code>client.oidc_token_management.<a href="src/fern/oidc_token_management/client.py">oidc_token_management_update_org_claims</a>(...) -> ClaimResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates/Updates org-level custom claims of OIDC identity tokens
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

client.oidc_token_management.oidc_token_management_update_org_claims(
    org_id="orgID",
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

**org_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PatchClaimsRequest` 
    
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

<details><summary><code>client.oidc_token_management.<a href="src/fern/oidc_token_management/client.py">oidc_token_management_get_project_claims</a>(...) -> ClaimResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches project-level custom claims of OIDC identity tokens
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

client.oidc_token_management.oidc_token_management_get_project_claims(
    org_id="orgID",
    project_id="projectID",
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

**org_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `str` 
    
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

<details><summary><code>client.oidc_token_management.<a href="src/fern/oidc_token_management/client.py">oidc_token_management_delete_project_claims</a>(...) -> ClaimResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes project-level custom claims of OIDC identity tokens
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

client.oidc_token_management.oidc_token_management_delete_project_claims(
    org_id="orgID",
    project_id="projectID",
    claims="claims",
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

**org_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**claims:** `str` — comma separated list of claims to delete. Valid values are "audience" and "ttl".
    
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

<details><summary><code>client.oidc_token_management.<a href="src/fern/oidc_token_management/client.py">oidc_token_management_update_project_claims</a>(...) -> ClaimResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates/Updates project-level custom claims of OIDC identity tokens
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

client.oidc_token_management.oidc_token_management_update_project_claims(
    org_id="orgID",
    project_id="projectID",
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

**org_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PatchClaimsRequest` 
    
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

## Policy Management
<details><summary><code>client.policy_management.<a href="src/fern/policy_management/client.py">policy_management_get_decision_audit_logs</a>(...) -> PolicyManagementGetDecisionAuditLogsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return a list of decision audit logs that were made using this owner's policies.
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

client.policy_management.policy_management_get_decision_audit_logs(
    owner_id="ownerID",
    context="context",
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

**owner_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**context:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Return decisions matching this decision status.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[datetime.datetime]` — Return decisions made after this date.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[datetime.datetime]` — Return decisions made before this date.
    
</dd>
</dl>

<dl>
<dd>

**branch:** `typing.Optional[str]` — Return decisions made on this branch.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Return decisions made for this project.
    
</dd>
</dl>

<dl>
<dd>

**build_number:** `typing.Optional[str]` — Return decisions made for this build number.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Sets the offset when retrieving the decisions, for paging.
    
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

<details><summary><code>client.policy_management.<a href="src/fern/policy_management/client.py">policy_management_evaluate_input_data</a>(...) -> Decision</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will evaluate input data (config+metadata) against owner's stored policies and return a decision.
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

client.policy_management.policy_management_evaluate_input_data(
    owner_id="ownerID",
    context="context",
    input="input",
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

**owner_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**context:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**input:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
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

<details><summary><code>client.policy_management.<a href="src/fern/policy_management/client.py">policy_management_get_decision_settings</a>(...) -> DecisionSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint retrieves the current decision settings (eg enable/disable policy evaluation)
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

client.policy_management.policy_management_get_decision_settings(
    owner_id="ownerID",
    context="context",
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

**owner_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**context:** `str` 
    
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

<details><summary><code>client.policy_management.<a href="src/fern/policy_management/client.py">policy_management_modify_decision_settings</a>(...) -> DecisionSettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows modifying decision settings (eg enable/disable policy evaluation)
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

client.policy_management.policy_management_modify_decision_settings(
    owner_id="ownerID",
    context="context",
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

**owner_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**context:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `DecisionSettings` 
    
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

<details><summary><code>client.policy_management.<a href="src/fern/policy_management/client.py">policy_management_get_decision_audit_log_by_given_id</a>(...) -> DecisionLog</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will retrieve a decision for a given decision log ID
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

client.policy_management.policy_management_get_decision_audit_log_by_given_id(
    owner_id="ownerID",
    context="context",
    decision_id="decisionID",
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

**owner_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**context:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**decision_id:** `str` 
    
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

<details><summary><code>client.policy_management.<a href="src/fern/policy_management/client.py">policy_management_get_policy_bundle_for_decision</a>(...) -> PolicyBundle</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will retrieve a policy bundle for a given decision log ID
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

client.policy_management.policy_management_get_policy_bundle_for_decision(
    owner_id="ownerID",
    context="context",
    decision_id="decisionID",
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

**owner_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**context:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**decision_id:** `str` 
    
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

<details><summary><code>client.policy_management.<a href="src/fern/policy_management/client.py">policy_management_get_policy_bundle</a>(...) -> PolicyBundle</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will retrieve a policy bundle
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

client.policy_management.policy_management_get_policy_bundle(
    owner_id="ownerID",
    context="context",
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

**owner_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**context:** `str` 
    
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

<details><summary><code>client.policy_management.<a href="src/fern/policy_management/client.py">policy_management_create_policy_bundle_for_context</a>(...) -> BundleDiff</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint replaces the current policy bundle with the provided policy bundle
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

client.policy_management.policy_management_create_policy_bundle_for_context(
    owner_id="ownerID",
    context="context",
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

**owner_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**context:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**dry:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**policies:** `typing.Optional[typing.Dict[str, str]]` 
    
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

<details><summary><code>client.policy_management.<a href="src/fern/policy_management/client.py">policy_management_get_document</a>(...) -> Policy</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will retrieve a policy document.
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

client.policy_management.policy_management_get_document(
    owner_id="ownerID",
    context="context",
    policy_name="policyName",
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

**owner_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**context:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**policy_name:** `str` — the policy name set by the rego policy_name rule
    
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

