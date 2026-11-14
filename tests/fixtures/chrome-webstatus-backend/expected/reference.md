# Reference
<details><summary><code>client.<a href="src/fern/client.py#L154-L207">list_features</a>(...) -> FeaturePage</code></summary>
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
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.list_features()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return
    
</dd>
</dl>

<dl>
<dd>

**wpt_metric_view:** `typing.Optional[WptMetricView]` 
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — A query string to represent the filters to apply the datastore while searching. The query must follow the ANTLR grammar. Please read the query readme at antlr/FeatureSearch.md. The query must be url safe.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListFeaturesRequestSort]` — Field to sort by, with 'asc' for ascending and 'desc' for descending order. Defaults to sorting by 'name' in ascending order (e.g., 'name_asc').
    
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

<details><summary><code>client.<a href="src/fern/client.py#L209-L247">get_feature</a>(...) -> Feature</code></summary>
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
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.get_feature(
    feature_id="feature_id",
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

**feature_id:** `str` — Feature ID
    
</dd>
</dl>

<dl>
<dd>

**wpt_metric_view:** `typing.Optional[WptMetricView]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py#L249-L279">get_feature_metadata</a>(...) -> FeatureMetadata</code></summary>
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
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.get_feature_metadata(
    feature_id="feature_id",
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

**feature_id:** `str` — Feature ID
    
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

<details><summary><code>client.<a href="src/fern/client.py#L281-L368">list_feature_wpt_metrics</a>(...) -> WptRunMetricsPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SupportedBrowsers, ListFeatureWptMetricsRequestChannel, WptMetricView
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.list_feature_wpt_metrics(
    feature_id="feature_id",
    browser=SupportedBrowsers.CHROME,
    channel=ListFeatureWptMetricsRequestChannel.STABLE,
    metric_view=WptMetricView.TEST_COUNTS,
    start_at=datetime.date.fromisoformat("2023-01-15"),
    end_at=datetime.date.fromisoformat("2023-01-15"),
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

**feature_id:** `str` — Feature ID
    
</dd>
</dl>

<dl>
<dd>

**browser:** `SupportedBrowsers` — Browser name
    
</dd>
</dl>

<dl>
<dd>

**channel:** `ListFeatureWptMetricsRequestChannel` — Browser name
    
</dd>
</dl>

<dl>
<dd>

**metric_view:** `WptMetricView` — Specified metric view of the WPT data.
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `datetime.date` — Start date (RFC 3339, section 5.6, for example, 2017-07-21). The date is inclusive.
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `datetime.date` — End date (RFC 3339, section 5.6, for example, 2017-07-21). The date is exclusive.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return
    
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

<details><summary><code>client.<a href="src/fern/client.py#L370-L434">list_chrome_daily_usage_stats</a>(...) -> ChromeDailyStatsPage</code></summary>
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
import datetime

client = FernApi(
    token="<token>",
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.list_chrome_daily_usage_stats(
    feature_id="feature_id",
    start_at=datetime.date.fromisoformat("2023-01-15"),
    end_at=datetime.date.fromisoformat("2023-01-15"),
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

**feature_id:** `str` — Feature ID
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `datetime.date` — Start date (RFC 3339, section 5.6, for example, 2017-07-21). The date is inclusive.
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `datetime.date` — End date (RFC 3339, section 5.6, for example, 2017-07-21). The date is exclusive.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return
    
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

<details><summary><code>client.<a href="src/fern/client.py#L436-L473">list_global_saved_searches</a>(...) -> GlobalSavedSearchPage</code></summary>
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
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.list_global_saved_searches()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return
    
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

<details><summary><code>client.<a href="src/fern/client.py#L475-L544">list_aggregated_feature_support</a>(...) -> BrowserReleaseFeatureMetricsPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SupportedBrowsers
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.list_aggregated_feature_support(
    browser=SupportedBrowsers.CHROME,
    start_at=datetime.date.fromisoformat("2023-01-15"),
    end_at=datetime.date.fromisoformat("2023-01-15"),
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

**browser:** `SupportedBrowsers` — Browser name
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `datetime.date` — Start date (RFC 3339, section 5.6, for example, 2017-07-21). The date is inclusive.
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `datetime.date` — End date (RFC 3339, section 5.6, for example, 2017-07-21). The date is exclusive.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return
    
</dd>
</dl>

<dl>
<dd>

**include_baseline_mobile_browsers:** `typing.Optional[bool]` — Include baseline mobile browsers in the response. This is only applicable for desktop browsers with a corresponding mobile browser.
    
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

<details><summary><code>client.<a href="src/fern/client.py#L546-L621">list_missing_one_implementation_counts</a>(...) -> BrowserReleaseFeatureMetricsPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SupportedBrowsers
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.list_missing_one_implementation_counts(
    browser_path_param=SupportedBrowsers.CHROME,
    start_at=datetime.date.fromisoformat("2023-01-15"),
    end_at=datetime.date.fromisoformat("2023-01-15"),
    browser=[
        SupportedBrowsers.CHROME
    ],
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

**browser_path_param:** `SupportedBrowsers` — Browser name
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `datetime.date` — Start date (RFC 3339, section 5.6, for example, 2017-07-21). The date is inclusive.
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `datetime.date` — End date (RFC 3339, section 5.6, for example, 2017-07-21). The date is exclusive.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return
    
</dd>
</dl>

<dl>
<dd>

**include_baseline_mobile_browsers:** `typing.Optional[bool]` — Include baseline mobile browsers in the response. This is only applicable for desktop browsers with a corresponding mobile browser.
    
</dd>
</dl>

<dl>
<dd>

**browser:** `typing.Optional[typing.Union[SupportedBrowsers, typing.Sequence[SupportedBrowsers]]]` — A list of browsers to check if {browser} is lagging behind on features. The list is provided by specifying repeating query parameters. Example: ?browser=fooBrowser&browser=bazBrowser
    
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

<details><summary><code>client.<a href="src/fern/client.py#L623-L690">list_missing_one_implementation_features</a>(...) -> MissingOneImplFeaturesPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SupportedBrowsers
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.list_missing_one_implementation_features(
    browser_path_param=SupportedBrowsers.CHROME,
    date=datetime.date.fromisoformat("2023-01-15"),
    browser=[
        SupportedBrowsers.CHROME
    ],
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

**browser_path_param:** `SupportedBrowsers` — Browser name
    
</dd>
</dl>

<dl>
<dd>

**date:** `datetime.date` — The date for which to retrieve the feature IDs.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return
    
</dd>
</dl>

<dl>
<dd>

**include_baseline_mobile_browsers:** `typing.Optional[bool]` — Include baseline mobile browsers in the response. This is only applicable for desktop browsers with a corresponding mobile browser.
    
</dd>
</dl>

<dl>
<dd>

**browser:** `typing.Optional[typing.Union[SupportedBrowsers, typing.Sequence[SupportedBrowsers]]]` — A list of browsers to check if {browser} is lagging behind on features. The list is provided by specifying repeating query parameters. Example:?browser=fooBrowser&browser=bazBrowser
    
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

<details><summary><code>client.<a href="src/fern/client.py#L692-L778">list_aggregated_wpt_metrics</a>(...) -> WptRunMetricsPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SupportedBrowsers, ListAggregatedWptMetricsRequestChannel, WptMetricView
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.list_aggregated_wpt_metrics(
    browser=SupportedBrowsers.CHROME,
    channel=ListAggregatedWptMetricsRequestChannel.STABLE,
    metric_view=WptMetricView.TEST_COUNTS,
    start_at=datetime.date.fromisoformat("2023-01-15"),
    end_at=datetime.date.fromisoformat("2023-01-15"),
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

**browser:** `SupportedBrowsers` — Browser name
    
</dd>
</dl>

<dl>
<dd>

**channel:** `ListAggregatedWptMetricsRequestChannel` — Browser name
    
</dd>
</dl>

<dl>
<dd>

**metric_view:** `WptMetricView` — Specified metric view of the WPT data.
    
</dd>
</dl>

<dl>
<dd>

**start_at:** `datetime.date` — Start date (RFC 3339, section 5.6, for example, 2017-07-21). The date is inclusive.
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `datetime.date` — End date (RFC 3339, section 5.6, for example, 2017-07-21). The date is exclusive.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return
    
</dd>
</dl>

<dl>
<dd>

**feature_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of feature IDs to filter results. TThe list is provided by specifying repeating query parameters. Example: ?featureId=id1&featureId=id2
    
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

<details><summary><code>client.<a href="src/fern/client.py#L780-L838">list_aggregated_baseline_status_counts</a>(...) -> BaselineStatusMetricsPage</code></summary>
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
import datetime

client = FernApi(
    token="<token>",
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.list_aggregated_baseline_status_counts(
    start_at=datetime.date.fromisoformat("2023-01-15"),
    end_at=datetime.date.fromisoformat("2023-01-15"),
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

**start_at:** `datetime.date` — Start date (RFC 3339, section 5.6, for example, 2017-07-21). The date is inclusive.
    
</dd>
</dl>

<dl>
<dd>

**end_at:** `datetime.date` — End date (RFC 3339, section 5.6, for example, 2017-07-21). The date is exclusive.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return
    
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

<details><summary><code>client.<a href="src/fern/client.py#L840-L873">ping_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Signals to the backend that a user has just authenticated.
This allows the backend to perform tasks like creating or updating the user's profile
with the latest information from the identity provider (e.g., refreshing their email address).

This endpoint should be called by clients once, immediately after a successful login.
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
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.ping_user()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**github_token:** `typing.Optional[str]` — The GitHub OAuth access token obtained by the frontend during interactive sign-in. Used by the backend to perform a one-time sync of user profile data (like email) directly from GitHub. This token is not stored by the backend.
    
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

<details><summary><code>client.<a href="src/fern/client.py#L875-L912">list_notification_channels</a>(...) -> NotificationChannelPage</code></summary>
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
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.list_notification_channels()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return
    
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

<details><summary><code>client.<a href="src/fern/client.py#L914-L956">create_notification_channel</a>(...) -> NotificationChannelResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, CreateNotificationChannelRequestConfig_Webhook
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.create_notification_channel(
    name="name",
    config=CreateNotificationChannelRequestConfig_Webhook(
        url="url",
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

**name:** `str` — A user-defined name for the channel.
    
</dd>
</dl>

<dl>
<dd>

**config:** `CreateNotificationChannelRequestConfig` — Configuration specific to the channel type.
    
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

<details><summary><code>client.<a href="src/fern/client.py#L958-L988">get_notification_channel</a>(...) -> NotificationChannelResponse</code></summary>
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
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.get_notification_channel(
    channel_id="channel_id",
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

**channel_id:** `str` — Notification Channel ID
    
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

<details><summary><code>client.<a href="src/fern/client.py#L990-L1019">delete_notification_channel</a>(...)</code></summary>
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
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.delete_notification_channel(
    channel_id="channel_id",
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

**channel_id:** `str` — Notification Channel ID
    
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

<details><summary><code>client.<a href="src/fern/client.py#L1021-L1068">update_notification_channel</a>(...) -> NotificationChannelResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, UpdateNotificationChannelRequestUpdateMaskItem
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.update_notification_channel(
    channel_id="channel_id",
    update_mask=[
        UpdateNotificationChannelRequestUpdateMaskItem.NAME
    ],
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

**channel_id:** `str` — Notification Channel ID
    
</dd>
</dl>

<dl>
<dd>

**update_mask:** `typing.List[UpdateNotificationChannelRequestUpdateMaskItem]` — A list of fields to update. Required. Allowed values are: `name`, `config`.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[UpdateNotificationChannelRequestConfig]` — Configuration specific to the channel type.
    
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

<details><summary><code>client.<a href="src/fern/client.py#L1070-L1107">list_user_saved_searches</a>(...) -> UserSavedSearchPage</code></summary>
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
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.list_user_saved_searches()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return
    
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

<details><summary><code>client.<a href="src/fern/client.py#L1109-L1138">put_user_saved_search_bookmark</a>(...)</code></summary>
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
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.put_user_saved_search_bookmark(
    search_id="search_id",
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

**search_id:** `str` — Saved Search ID
    
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

<details><summary><code>client.<a href="src/fern/client.py#L1140-L1169">remove_user_saved_search_bookmark</a>(...)</code></summary>
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
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.remove_user_saved_search_bookmark(
    search_id="search_id",
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

**search_id:** `str` — Saved Search ID
    
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

<details><summary><code>client.<a href="src/fern/client.py#L1171-L1212">create_saved_search</a>(...) -> SavedSearchResponse</code></summary>
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
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.create_saved_search(
    name="name",
    query="query",
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

**request:** `SavedSearch` 
    
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

<details><summary><code>client.<a href="src/fern/client.py#L1214-L1244">get_saved_search</a>(...) -> SavedSearchResponse</code></summary>
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
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.get_saved_search(
    search_id="search_id",
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

**search_id:** `str` — Saved Search ID
    
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

<details><summary><code>client.<a href="src/fern/client.py#L1246-L1273">remove_saved_search</a>(...)</code></summary>
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
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.remove_saved_search(
    search_id="search_id",
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

**search_id:** `str` — Saved Search ID
    
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

<details><summary><code>client.<a href="src/fern/client.py#L1275-L1329">update_saved_search</a>(...) -> SavedSearchResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SavedSearchUpdateRequestUpdateMaskItem
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.update_saved_search(
    search_id="search_id",
    update_mask=[
        SavedSearchUpdateRequestUpdateMaskItem.NAME
    ],
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

**search_id:** `str` — Saved Search ID
    
</dd>
</dl>

<dl>
<dd>

**update_mask:** `typing.List[SavedSearchUpdateRequestUpdateMaskItem]` — A list of fields to update. Required. Allowed values are: `name`, `description`, `query`.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py#L1331-L1368">list_subscriptions</a>(...) -> SubscriptionPage</code></summary>
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
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.list_subscriptions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return
    
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

<details><summary><code>client.<a href="src/fern/client.py#L1370-L1425">create_subscription</a>(...) -> SubscriptionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SubscriptionFrequency, SubscriptionTriggerWritable
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.create_subscription(
    saved_search_id="saved_search_id",
    frequency=SubscriptionFrequency.IMMEDIATE,
    triggers=[
        SubscriptionTriggerWritable.FEATURE_BASELINE_TO_NEWLY
    ],
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

**saved_search_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**frequency:** `SubscriptionFrequency` 
    
</dd>
</dl>

<dl>
<dd>

**triggers:** `typing.List[SubscriptionTriggerWritable]` 
    
</dd>
</dl>

<dl>
<dd>

**channel_id:** `typing.Optional[str]` — Explicit Mode: Provide a specific channel ID. Required for manual channels (Webhook/Email). Mutually exclusive with 'channel_type'.
    
</dd>
</dl>

<dl>
<dd>

**channel_type:** `typing.Optional[SubscriptionChannelType]` — Implicit Mode: Provide a channel type. Used for system-managed channels (e.g., 'rss') where the system automatically resolves or creates the channel. Mutually exclusive with 'channel_id'.
    
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

<details><summary><code>client.<a href="src/fern/client.py#L1427-L1457">get_subscription</a>(...) -> SubscriptionResponse</code></summary>
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
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.get_subscription(
    subscription_id="subscription_id",
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

**subscription_id:** `str` — Subscription ID
    
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

<details><summary><code>client.<a href="src/fern/client.py#L1459-L1488">delete_subscription</a>(...)</code></summary>
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
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.delete_subscription(
    subscription_id="subscription_id",
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

**subscription_id:** `str` — Subscription ID
    
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

<details><summary><code>client.<a href="src/fern/client.py#L1490-L1540">update_subscription</a>(...) -> SubscriptionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, UpdateSubscriptionRequestUpdateMaskItem
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.update_subscription(
    subscription_id="subscription_id",
    update_mask=[
        UpdateSubscriptionRequestUpdateMaskItem.TRIGGERS
    ],
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

**subscription_id:** `str` — Subscription ID
    
</dd>
</dl>

<dl>
<dd>

**update_mask:** `typing.List[UpdateSubscriptionRequestUpdateMaskItem]` — A list of fields to update. Required. Allowed values are: `triggers`, `frequency`.
    
</dd>
</dl>

<dl>
<dd>

**triggers:** `typing.Optional[typing.List[SubscriptionTriggerWritable]]` 
    
</dd>
</dl>

<dl>
<dd>

**frequency:** `typing.Optional[SubscriptionFrequency]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py#L1542-L1584">get_subscription_rss</a>(...)</code></summary>
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
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.get_subscription_rss(
    subscription_id="subscription_id",
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

**subscription_id:** `str` — Subscription ID
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return
    
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

<details><summary><code>client.<a href="src/fern/client.py#L1586-L1632">list_code_subscriptions</a>(...) -> CodeSubscriptionPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ListCodeSubscriptionsRequestProvider
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.list_code_subscriptions(
    provider=ListCodeSubscriptionsRequestProvider.GITHUB,
    repository_id="repository_id",
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

**provider:** `ListCodeSubscriptionsRequestProvider` 
    
</dd>
</dl>

<dl>
<dd>

**repository_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return
    
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

<details><summary><code>client.<a href="src/fern/client.py#L1634-L1685">handle_vcs_webhook</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, HandleVcsWebhookRequestProvider
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.handle_vcs_webhook(
    provider=HandleVcsWebhookRequestProvider.GITHUB,
    request="string",
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

**provider:** `HandleVcsWebhookRequestProvider` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `bytes` 
    
</dd>
</dl>

<dl>
<dd>

**hub_signature256:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**git_hub_delivery:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**git_hub_event:** `typing.Optional[str]` 
    
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

## Healthchecks
<details><summary><code>client.healthchecks.<a href="src/fern/healthchecks/client.py#L26-L53">get_healthcheck_liveness</a>() -> HealthcheckResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a 200 OK status to indicate that the service process is alive and responsive.
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
    no_auth="<X-No-Auth>",
    environment=FernApiEnvironment.PRODUCTION,
)

client.healthchecks.get_healthcheck_liveness()

```
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

