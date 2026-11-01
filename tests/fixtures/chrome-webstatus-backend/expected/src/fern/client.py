

from __future__ import annotations

import datetime as dt
import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.baseline_status_metrics_page import BaselineStatusMetricsPage
from .types.browser_release_feature_metrics_page import BrowserReleaseFeatureMetricsPage
from .types.chrome_daily_stats_page import ChromeDailyStatsPage
from .types.code_subscription_page import CodeSubscriptionPage
from .types.create_notification_channel_request_config import CreateNotificationChannelRequestConfig
from .types.feature import Feature
from .types.feature_metadata import FeatureMetadata
from .types.feature_page import FeaturePage
from .types.global_saved_search_page import GlobalSavedSearchPage
from .types.handle_vcs_webhook_request_provider import HandleVcsWebhookRequestProvider
from .types.list_aggregated_wpt_metrics_request_channel import ListAggregatedWptMetricsRequestChannel
from .types.list_code_subscriptions_request_provider import ListCodeSubscriptionsRequestProvider
from .types.list_feature_wpt_metrics_request_channel import ListFeatureWptMetricsRequestChannel
from .types.list_features_request_sort import ListFeaturesRequestSort
from .types.missing_one_impl_features_page import MissingOneImplFeaturesPage
from .types.notification_channel_page import NotificationChannelPage
from .types.notification_channel_response import NotificationChannelResponse
from .types.saved_search_response import SavedSearchResponse
from .types.saved_search_update_request_update_mask_item import SavedSearchUpdateRequestUpdateMaskItem
from .types.subscription_channel_type import SubscriptionChannelType
from .types.subscription_frequency import SubscriptionFrequency
from .types.subscription_page import SubscriptionPage
from .types.subscription_response import SubscriptionResponse
from .types.subscription_trigger_writable import SubscriptionTriggerWritable
from .types.supported_browsers import SupportedBrowsers
from .types.update_notification_channel_request_config import UpdateNotificationChannelRequestConfig
from .types.update_notification_channel_request_update_mask_item import UpdateNotificationChannelRequestUpdateMaskItem
from .types.update_subscription_request_update_mask_item import UpdateSubscriptionRequestUpdateMaskItem
from .types.user_saved_search_page import UserSavedSearchPage
from .types.wpt_metric_view import WptMetricView
from .types.wpt_run_metrics_page import WptRunMetricsPage

if typing.TYPE_CHECKING:
    from .healthchecks.client import AsyncHealthchecksClient, HealthchecksClient

OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.PRODUCTION



    no_auth : str
    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        no_auth="YOUR_NO_AUTH",
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.PRODUCTION,
        no_auth: str,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            no_auth=no_auth,
            token=token,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)
        self._healthchecks: typing.Optional[HealthchecksClient] = None

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def list_features(
        self,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        wpt_metric_view: typing.Optional[WptMetricView] = None,
        q: typing.Optional[str] = None,
        sort: typing.Optional[ListFeaturesRequestSort] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeaturePage:
        """
        Parameters
        ----------
        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        wpt_metric_view : typing.Optional[WptMetricView]

        q : typing.Optional[str]
            A query string to represent the filters to apply the datastore while searching. The query must follow the ANTLR grammar. Please read the query readme at antlr/FeatureSearch.md. The query must be url safe.

        sort : typing.Optional[ListFeaturesRequestSort]
            Field to sort by, with 'asc' for ascending and 'desc' for descending order. Defaults to sorting by 'name' in ascending order (e.g., 'name_asc').

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeaturePage
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.list_features()
        """
        _response = self._raw_client.list_features(
            page_token=page_token,
            page_size=page_size,
            wpt_metric_view=wpt_metric_view,
            q=q,
            sort=sort,
            request_options=request_options,
        )
        return _response.data

    def get_feature(
        self,
        feature_id: str,
        *,
        wpt_metric_view: typing.Optional[WptMetricView] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Feature:
        """
        Parameters
        ----------
        feature_id : str
            Feature ID

        wpt_metric_view : typing.Optional[WptMetricView]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Feature
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.get_feature(
            feature_id="feature_id",
        )
        """
        _response = self._raw_client.get_feature(
            feature_id, wpt_metric_view=wpt_metric_view, request_options=request_options
        )
        return _response.data

    def get_feature_metadata(
        self, feature_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FeatureMetadata:
        """
        Parameters
        ----------
        feature_id : str
            Feature ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeatureMetadata
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.get_feature_metadata(
            feature_id="feature_id",
        )
        """
        _response = self._raw_client.get_feature_metadata(feature_id, request_options=request_options)
        return _response.data

    def list_feature_wpt_metrics(
        self,
        feature_id: str,
        browser: SupportedBrowsers,
        channel: ListFeatureWptMetricsRequestChannel,
        metric_view: WptMetricView,
        *,
        start_at: dt.date,
        end_at: dt.date,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WptRunMetricsPage:
        """
        Parameters
        ----------
        feature_id : str
            Feature ID

        browser : SupportedBrowsers
            Browser name

        channel : ListFeatureWptMetricsRequestChannel
            Browser name

        metric_view : WptMetricView
            Specified metric view of the WPT data.

        start_at : dt.date
            Start date (RFC 3339, section 5.6, for example, 2017-07-21). The date is inclusive.

        end_at : dt.date
            End date (RFC 3339, section 5.6, for example, 2017-07-21). The date is exclusive.

        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WptRunMetricsPage
            OK

        Examples
        --------
        import datetime

        from fern import (
            FernApi,
            ListFeatureWptMetricsRequestChannel,
            SupportedBrowsers,
            WptMetricView,
        )

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.list_feature_wpt_metrics(
            feature_id="feature_id",
            browser=SupportedBrowsers.CHROME,
            channel=ListFeatureWptMetricsRequestChannel.STABLE,
            metric_view=WptMetricView.TEST_COUNTS,
            start_at=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            end_at=datetime.date.fromisoformat(
                "2023-01-15",
            ),
        )
        """
        _response = self._raw_client.list_feature_wpt_metrics(
            feature_id,
            browser,
            channel,
            metric_view,
            start_at=start_at,
            end_at=end_at,
            page_token=page_token,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    def list_chrome_daily_usage_stats(
        self,
        feature_id: str,
        *,
        start_at: dt.date,
        end_at: dt.date,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChromeDailyStatsPage:
        """
        Parameters
        ----------
        feature_id : str
            Feature ID

        start_at : dt.date
            Start date (RFC 3339, section 5.6, for example, 2017-07-21). The date is inclusive.

        end_at : dt.date
            End date (RFC 3339, section 5.6, for example, 2017-07-21). The date is exclusive.

        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChromeDailyStatsPage
            OK

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.list_chrome_daily_usage_stats(
            feature_id="feature_id",
            start_at=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            end_at=datetime.date.fromisoformat(
                "2023-01-15",
            ),
        )
        """
        _response = self._raw_client.list_chrome_daily_usage_stats(
            feature_id,
            start_at=start_at,
            end_at=end_at,
            page_token=page_token,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    def list_global_saved_searches(
        self,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GlobalSavedSearchPage:
        """
        Parameters
        ----------
        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalSavedSearchPage
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.list_global_saved_searches()
        """
        _response = self._raw_client.list_global_saved_searches(
            page_token=page_token, page_size=page_size, request_options=request_options
        )
        return _response.data

    def list_aggregated_feature_support(
        self,
        browser: SupportedBrowsers,
        *,
        start_at: dt.date,
        end_at: dt.date,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        include_baseline_mobile_browsers: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BrowserReleaseFeatureMetricsPage:
        """
        Parameters
        ----------
        browser : SupportedBrowsers
            Browser name

        start_at : dt.date
            Start date (RFC 3339, section 5.6, for example, 2017-07-21). The date is inclusive.

        end_at : dt.date
            End date (RFC 3339, section 5.6, for example, 2017-07-21). The date is exclusive.

        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        include_baseline_mobile_browsers : typing.Optional[bool]
            Include baseline mobile browsers in the response. This is only applicable for desktop browsers with a corresponding mobile browser.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BrowserReleaseFeatureMetricsPage
            OK

        Examples
        --------
        import datetime

        from fern import FernApi, SupportedBrowsers

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.list_aggregated_feature_support(
            browser=SupportedBrowsers.CHROME,
            start_at=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            end_at=datetime.date.fromisoformat(
                "2023-01-15",
            ),
        )
        """
        _response = self._raw_client.list_aggregated_feature_support(
            browser,
            start_at=start_at,
            end_at=end_at,
            page_token=page_token,
            page_size=page_size,
            include_baseline_mobile_browsers=include_baseline_mobile_browsers,
            request_options=request_options,
        )
        return _response.data

    def list_missing_one_implementation_counts(
        self,
        browser_path_param: SupportedBrowsers,
        *,
        start_at: dt.date,
        end_at: dt.date,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        include_baseline_mobile_browsers: typing.Optional[bool] = None,
        browser: typing.Optional[typing.Union[SupportedBrowsers, typing.Sequence[SupportedBrowsers]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BrowserReleaseFeatureMetricsPage:
        """
        Parameters
        ----------
        browser_path_param : SupportedBrowsers
            Browser name

        start_at : dt.date
            Start date (RFC 3339, section 5.6, for example, 2017-07-21). The date is inclusive.

        end_at : dt.date
            End date (RFC 3339, section 5.6, for example, 2017-07-21). The date is exclusive.

        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        include_baseline_mobile_browsers : typing.Optional[bool]
            Include baseline mobile browsers in the response. This is only applicable for desktop browsers with a corresponding mobile browser.

        browser : typing.Optional[typing.Union[SupportedBrowsers, typing.Sequence[SupportedBrowsers]]]
            A list of browsers to check if {browser} is lagging behind on features. The list is provided by specifying repeating query parameters. Example: ?browser=fooBrowser&browser=bazBrowser

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BrowserReleaseFeatureMetricsPage
            OK

        Examples
        --------
        import datetime

        from fern import FernApi, SupportedBrowsers

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.list_missing_one_implementation_counts(
            browser_path_param=SupportedBrowsers.CHROME,
            start_at=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            end_at=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            browser=[SupportedBrowsers.CHROME],
        )
        """
        _response = self._raw_client.list_missing_one_implementation_counts(
            browser_path_param,
            start_at=start_at,
            end_at=end_at,
            page_token=page_token,
            page_size=page_size,
            include_baseline_mobile_browsers=include_baseline_mobile_browsers,
            browser=browser,
            request_options=request_options,
        )
        return _response.data

    def list_missing_one_implementation_features(
        self,
        browser_path_param: SupportedBrowsers,
        date: dt.date,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        include_baseline_mobile_browsers: typing.Optional[bool] = None,
        browser: typing.Optional[typing.Union[SupportedBrowsers, typing.Sequence[SupportedBrowsers]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MissingOneImplFeaturesPage:
        """
        Parameters
        ----------
        browser_path_param : SupportedBrowsers
            Browser name

        date : dt.date
            The date for which to retrieve the feature IDs.

        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        include_baseline_mobile_browsers : typing.Optional[bool]
            Include baseline mobile browsers in the response. This is only applicable for desktop browsers with a corresponding mobile browser.

        browser : typing.Optional[typing.Union[SupportedBrowsers, typing.Sequence[SupportedBrowsers]]]
            A list of browsers to check if {browser} is lagging behind on features. The list is provided by specifying repeating query parameters. Example:?browser=fooBrowser&browser=bazBrowser

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MissingOneImplFeaturesPage
            OK

        Examples
        --------
        import datetime

        from fern import FernApi, SupportedBrowsers

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.list_missing_one_implementation_features(
            browser_path_param=SupportedBrowsers.CHROME,
            date=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            browser=[SupportedBrowsers.CHROME],
        )
        """
        _response = self._raw_client.list_missing_one_implementation_features(
            browser_path_param,
            date,
            page_token=page_token,
            page_size=page_size,
            include_baseline_mobile_browsers=include_baseline_mobile_browsers,
            browser=browser,
            request_options=request_options,
        )
        return _response.data

    def list_aggregated_wpt_metrics(
        self,
        browser: SupportedBrowsers,
        channel: ListAggregatedWptMetricsRequestChannel,
        metric_view: WptMetricView,
        *,
        start_at: dt.date,
        end_at: dt.date,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        feature_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WptRunMetricsPage:
        """
        Parameters
        ----------
        browser : SupportedBrowsers
            Browser name

        channel : ListAggregatedWptMetricsRequestChannel
            Browser name

        metric_view : WptMetricView
            Specified metric view of the WPT data.

        start_at : dt.date
            Start date (RFC 3339, section 5.6, for example, 2017-07-21). The date is inclusive.

        end_at : dt.date
            End date (RFC 3339, section 5.6, for example, 2017-07-21). The date is exclusive.

        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        feature_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A list of feature IDs to filter results. TThe list is provided by specifying repeating query parameters. Example: ?featureId=id1&featureId=id2

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WptRunMetricsPage
            OK

        Examples
        --------
        import datetime

        from fern import (
            FernApi,
            ListAggregatedWptMetricsRequestChannel,
            SupportedBrowsers,
            WptMetricView,
        )

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.list_aggregated_wpt_metrics(
            browser=SupportedBrowsers.CHROME,
            channel=ListAggregatedWptMetricsRequestChannel.STABLE,
            metric_view=WptMetricView.TEST_COUNTS,
            start_at=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            end_at=datetime.date.fromisoformat(
                "2023-01-15",
            ),
        )
        """
        _response = self._raw_client.list_aggregated_wpt_metrics(
            browser,
            channel,
            metric_view,
            start_at=start_at,
            end_at=end_at,
            page_token=page_token,
            page_size=page_size,
            feature_id=feature_id,
            request_options=request_options,
        )
        return _response.data

    def list_aggregated_baseline_status_counts(
        self,
        *,
        start_at: dt.date,
        end_at: dt.date,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaselineStatusMetricsPage:
        """
        Parameters
        ----------
        start_at : dt.date
            Start date (RFC 3339, section 5.6, for example, 2017-07-21). The date is inclusive.

        end_at : dt.date
            End date (RFC 3339, section 5.6, for example, 2017-07-21). The date is exclusive.

        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaselineStatusMetricsPage
            OK

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.list_aggregated_baseline_status_counts(
            start_at=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            end_at=datetime.date.fromisoformat(
                "2023-01-15",
            ),
        )
        """
        _response = self._raw_client.list_aggregated_baseline_status_counts(
            start_at=start_at,
            end_at=end_at,
            page_token=page_token,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    def ping_user(
        self, *, github_token: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Signals to the backend that a user has just authenticated.
        This allows the backend to perform tasks like creating or updating the user's profile
        with the latest information from the identity provider (e.g., refreshing their email address).

        This endpoint should be called by clients once, immediately after a successful login.

        Parameters
        ----------
        github_token : typing.Optional[str]
            The GitHub OAuth access token obtained by the frontend during interactive sign-in. Used by the backend to perform a one-time sync of user profile data (like email) directly from GitHub. This token is not stored by the backend.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.ping_user()
        """
        _response = self._raw_client.ping_user(github_token=github_token, request_options=request_options)
        return _response.data

    def list_notification_channels(
        self,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationChannelPage:
        """
        Parameters
        ----------
        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationChannelPage
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.list_notification_channels()
        """
        _response = self._raw_client.list_notification_channels(
            page_token=page_token, page_size=page_size, request_options=request_options
        )
        return _response.data

    def create_notification_channel(
        self,
        *,
        name: str,
        config: CreateNotificationChannelRequestConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationChannelResponse:
        """
        Parameters
        ----------
        name : str
            A user-defined name for the channel.

        config : CreateNotificationChannelRequestConfig
            Configuration specific to the channel type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationChannelResponse
            Created

        Examples
        --------
        from fern import CreateNotificationChannelRequestConfig_Webhook, FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.create_notification_channel(
            name="name",
            config=CreateNotificationChannelRequestConfig_Webhook(
                url="url",
            ),
        )
        """
        _response = self._raw_client.create_notification_channel(
            name=name, config=config, request_options=request_options
        )
        return _response.data

    def get_notification_channel(
        self, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NotificationChannelResponse:
        """
        Parameters
        ----------
        channel_id : str
            Notification Channel ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationChannelResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.get_notification_channel(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.get_notification_channel(channel_id, request_options=request_options)
        return _response.data

    def delete_notification_channel(
        self, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        channel_id : str
            Notification Channel ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.delete_notification_channel(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.delete_notification_channel(channel_id, request_options=request_options)
        return _response.data

    def update_notification_channel(
        self,
        channel_id: str,
        *,
        update_mask: typing.Sequence[UpdateNotificationChannelRequestUpdateMaskItem],
        name: typing.Optional[str] = OMIT,
        config: typing.Optional[UpdateNotificationChannelRequestConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationChannelResponse:
        """
        Parameters
        ----------
        channel_id : str
            Notification Channel ID

        update_mask : typing.Sequence[UpdateNotificationChannelRequestUpdateMaskItem]
            A list of fields to update. Required. Allowed values are: `name`, `config`.

        name : typing.Optional[str]

        config : typing.Optional[UpdateNotificationChannelRequestConfig]
            Configuration specific to the channel type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationChannelResponse
            OK

        Examples
        --------
        from fern import FernApi, UpdateNotificationChannelRequestUpdateMaskItem

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.update_notification_channel(
            channel_id="channel_id",
            update_mask=[UpdateNotificationChannelRequestUpdateMaskItem.NAME],
        )
        """
        _response = self._raw_client.update_notification_channel(
            channel_id, update_mask=update_mask, name=name, config=config, request_options=request_options
        )
        return _response.data

    def list_user_saved_searches(
        self,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserSavedSearchPage:
        """
        Parameters
        ----------
        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserSavedSearchPage
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.list_user_saved_searches()
        """
        _response = self._raw_client.list_user_saved_searches(
            page_token=page_token, page_size=page_size, request_options=request_options
        )
        return _response.data

    def put_user_saved_search_bookmark(
        self, search_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        search_id : str
            Saved Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.put_user_saved_search_bookmark(
            search_id="search_id",
        )
        """
        _response = self._raw_client.put_user_saved_search_bookmark(search_id, request_options=request_options)
        return _response.data

    def remove_user_saved_search_bookmark(
        self, search_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        search_id : str
            Saved Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.remove_user_saved_search_bookmark(
            search_id="search_id",
        )
        """
        _response = self._raw_client.remove_user_saved_search_bookmark(search_id, request_options=request_options)
        return _response.data

    def create_saved_search(
        self,
        *,
        name: str,
        query: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SavedSearchResponse:
        """
        Parameters
        ----------
        name : str

        query : str

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SavedSearchResponse
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.create_saved_search(
            name="name",
            query="query",
        )
        """
        _response = self._raw_client.create_saved_search(
            name=name, query=query, description=description, request_options=request_options
        )
        return _response.data

    def get_saved_search(
        self, search_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SavedSearchResponse:
        """
        Parameters
        ----------
        search_id : str
            Saved Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SavedSearchResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.get_saved_search(
            search_id="search_id",
        )
        """
        _response = self._raw_client.get_saved_search(search_id, request_options=request_options)
        return _response.data

    def remove_saved_search(self, search_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        search_id : str
            Saved Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.remove_saved_search(
            search_id="search_id",
        )
        """
        _response = self._raw_client.remove_saved_search(search_id, request_options=request_options)
        return _response.data

    def update_saved_search(
        self,
        search_id: str,
        *,
        update_mask: typing.Sequence[SavedSearchUpdateRequestUpdateMaskItem],
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        query: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SavedSearchResponse:
        """
        Parameters
        ----------
        search_id : str
            Saved Search ID

        update_mask : typing.Sequence[SavedSearchUpdateRequestUpdateMaskItem]
            A list of fields to update. Required. Allowed values are: `name`, `description`, `query`.

        name : typing.Optional[str]

        description : typing.Optional[str]

        query : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SavedSearchResponse
            OK

        Examples
        --------
        from fern import FernApi, SavedSearchUpdateRequestUpdateMaskItem

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.update_saved_search(
            search_id="search_id",
            update_mask=[SavedSearchUpdateRequestUpdateMaskItem.NAME],
        )
        """
        _response = self._raw_client.update_saved_search(
            search_id,
            update_mask=update_mask,
            name=name,
            description=description,
            query=query,
            request_options=request_options,
        )
        return _response.data

    def list_subscriptions(
        self,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionPage:
        """
        Parameters
        ----------
        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionPage
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.list_subscriptions()
        """
        _response = self._raw_client.list_subscriptions(
            page_token=page_token, page_size=page_size, request_options=request_options
        )
        return _response.data

    def create_subscription(
        self,
        *,
        saved_search_id: str,
        frequency: SubscriptionFrequency,
        triggers: typing.Sequence[SubscriptionTriggerWritable],
        channel_id: typing.Optional[str] = OMIT,
        channel_type: typing.Optional[SubscriptionChannelType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionResponse:
        """
        Parameters
        ----------
        saved_search_id : str

        frequency : SubscriptionFrequency

        triggers : typing.Sequence[SubscriptionTriggerWritable]

        channel_id : typing.Optional[str]
            Explicit Mode: Provide a specific channel ID. Required for manual channels (Webhook/Email). Mutually exclusive with 'channel_type'.

        channel_type : typing.Optional[SubscriptionChannelType]
            Implicit Mode: Provide a channel type. Used for system-managed channels (e.g., 'rss') where the system automatically resolves or creates the channel. Mutually exclusive with 'channel_id'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionResponse
            Created

        Examples
        --------
        from fern import FernApi, SubscriptionFrequency, SubscriptionTriggerWritable

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.create_subscription(
            saved_search_id="saved_search_id",
            frequency=SubscriptionFrequency.IMMEDIATE,
            triggers=[SubscriptionTriggerWritable.FEATURE_BASELINE_TO_NEWLY],
        )
        """
        _response = self._raw_client.create_subscription(
            saved_search_id=saved_search_id,
            frequency=frequency,
            triggers=triggers,
            channel_id=channel_id,
            channel_type=channel_type,
            request_options=request_options,
        )
        return _response.data

    def get_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SubscriptionResponse:
        """
        Parameters
        ----------
        subscription_id : str
            Subscription ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.get_subscription(
            subscription_id="subscription_id",
        )
        """
        _response = self._raw_client.get_subscription(subscription_id, request_options=request_options)
        return _response.data

    def delete_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str
            Subscription ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.delete_subscription(
            subscription_id="subscription_id",
        )
        """
        _response = self._raw_client.delete_subscription(subscription_id, request_options=request_options)
        return _response.data

    def update_subscription(
        self,
        subscription_id: str,
        *,
        update_mask: typing.Sequence[UpdateSubscriptionRequestUpdateMaskItem],
        triggers: typing.Optional[typing.Sequence[SubscriptionTriggerWritable]] = OMIT,
        frequency: typing.Optional[SubscriptionFrequency] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionResponse:
        """
        Parameters
        ----------
        subscription_id : str
            Subscription ID

        update_mask : typing.Sequence[UpdateSubscriptionRequestUpdateMaskItem]
            A list of fields to update. Required. Allowed values are: `triggers`, `frequency`.

        triggers : typing.Optional[typing.Sequence[SubscriptionTriggerWritable]]

        frequency : typing.Optional[SubscriptionFrequency]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionResponse
            OK

        Examples
        --------
        from fern import FernApi, UpdateSubscriptionRequestUpdateMaskItem

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.update_subscription(
            subscription_id="subscription_id",
            update_mask=[UpdateSubscriptionRequestUpdateMaskItem.TRIGGERS],
        )
        """
        _response = self._raw_client.update_subscription(
            subscription_id,
            update_mask=update_mask,
            triggers=triggers,
            frequency=frequency,
            request_options=request_options,
        )
        return _response.data

    def get_subscription_rss(
        self,
        subscription_id: str,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str
            Subscription ID

        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.get_subscription_rss(
            subscription_id="subscription_id",
        )
        """
        _response = self._raw_client.get_subscription_rss(
            subscription_id, page_token=page_token, page_size=page_size, request_options=request_options
        )
        return _response.data

    def list_code_subscriptions(
        self,
        provider: ListCodeSubscriptionsRequestProvider,
        repository_id: str,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CodeSubscriptionPage:
        """
        Parameters
        ----------
        provider : ListCodeSubscriptionsRequestProvider

        repository_id : str

        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CodeSubscriptionPage
            OK

        Examples
        --------
        from fern import FernApi, ListCodeSubscriptionsRequestProvider

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.list_code_subscriptions(
            provider=ListCodeSubscriptionsRequestProvider.GITHUB,
            repository_id="repository_id",
        )
        """
        _response = self._raw_client.list_code_subscriptions(
            provider, repository_id, page_token=page_token, page_size=page_size, request_options=request_options
        )
        return _response.data

    def handle_vcs_webhook(
        self,
        provider: HandleVcsWebhookRequestProvider,
        *,
        request: bytes,
        hub_signature256: typing.Optional[str] = None,
        git_hub_delivery: typing.Optional[str] = None,
        git_hub_event: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        provider : HandleVcsWebhookRequestProvider

        request : bytes

        hub_signature256 : typing.Optional[str]

        git_hub_delivery : typing.Optional[str]

        git_hub_event : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, HandleVcsWebhookRequestProvider

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.handle_vcs_webhook(
            provider=HandleVcsWebhookRequestProvider.GITHUB,
            request="string",
        )
        """
        _response = self._raw_client.handle_vcs_webhook(
            provider,
            request=request,
            hub_signature256=hub_signature256,
            git_hub_delivery=git_hub_delivery,
            git_hub_event=git_hub_event,
            request_options=request_options,
        )
        return _response.data

    @property
    def healthchecks(self):
        if self._healthchecks is None:
            from .healthchecks.client import HealthchecksClient

            self._healthchecks = HealthchecksClient(client_wrapper=self._client_wrapper)
        return self._healthchecks


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.PRODUCTION



    no_auth : str
    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    async_token : typing.Optional[typing.Callable[[], typing.Awaitable[str]]]
        An async callable that returns a bearer token. Use this when token acquisition involves async I/O (e.g., refreshing tokens via an async HTTP client). When provided, this is used instead of the synchronous token for async requests.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        no_auth="YOUR_NO_AUTH",
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.PRODUCTION,
        no_auth: str,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        async_token: typing.Optional[typing.Callable[[], typing.Awaitable[str]]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            no_auth=no_auth,
            token=token,
            headers=headers,
            async_token=async_token,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)
        self._healthchecks: typing.Optional[AsyncHealthchecksClient] = None

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def list_features(
        self,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        wpt_metric_view: typing.Optional[WptMetricView] = None,
        q: typing.Optional[str] = None,
        sort: typing.Optional[ListFeaturesRequestSort] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeaturePage:
        """
        Parameters
        ----------
        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        wpt_metric_view : typing.Optional[WptMetricView]

        q : typing.Optional[str]
            A query string to represent the filters to apply the datastore while searching. The query must follow the ANTLR grammar. Please read the query readme at antlr/FeatureSearch.md. The query must be url safe.

        sort : typing.Optional[ListFeaturesRequestSort]
            Field to sort by, with 'asc' for ascending and 'desc' for descending order. Defaults to sorting by 'name' in ascending order (e.g., 'name_asc').

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeaturePage
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_features()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_features(
            page_token=page_token,
            page_size=page_size,
            wpt_metric_view=wpt_metric_view,
            q=q,
            sort=sort,
            request_options=request_options,
        )
        return _response.data

    async def get_feature(
        self,
        feature_id: str,
        *,
        wpt_metric_view: typing.Optional[WptMetricView] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Feature:
        """
        Parameters
        ----------
        feature_id : str
            Feature ID

        wpt_metric_view : typing.Optional[WptMetricView]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Feature
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_feature(
                feature_id="feature_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_feature(
            feature_id, wpt_metric_view=wpt_metric_view, request_options=request_options
        )
        return _response.data

    async def get_feature_metadata(
        self, feature_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FeatureMetadata:
        """
        Parameters
        ----------
        feature_id : str
            Feature ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeatureMetadata
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_feature_metadata(
                feature_id="feature_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_feature_metadata(feature_id, request_options=request_options)
        return _response.data

    async def list_feature_wpt_metrics(
        self,
        feature_id: str,
        browser: SupportedBrowsers,
        channel: ListFeatureWptMetricsRequestChannel,
        metric_view: WptMetricView,
        *,
        start_at: dt.date,
        end_at: dt.date,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WptRunMetricsPage:
        """
        Parameters
        ----------
        feature_id : str
            Feature ID

        browser : SupportedBrowsers
            Browser name

        channel : ListFeatureWptMetricsRequestChannel
            Browser name

        metric_view : WptMetricView
            Specified metric view of the WPT data.

        start_at : dt.date
            Start date (RFC 3339, section 5.6, for example, 2017-07-21). The date is inclusive.

        end_at : dt.date
            End date (RFC 3339, section 5.6, for example, 2017-07-21). The date is exclusive.

        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WptRunMetricsPage
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern import (
            AsyncFernApi,
            ListFeatureWptMetricsRequestChannel,
            SupportedBrowsers,
            WptMetricView,
        )

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_feature_wpt_metrics(
                feature_id="feature_id",
                browser=SupportedBrowsers.CHROME,
                channel=ListFeatureWptMetricsRequestChannel.STABLE,
                metric_view=WptMetricView.TEST_COUNTS,
                start_at=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
                end_at=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_feature_wpt_metrics(
            feature_id,
            browser,
            channel,
            metric_view,
            start_at=start_at,
            end_at=end_at,
            page_token=page_token,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    async def list_chrome_daily_usage_stats(
        self,
        feature_id: str,
        *,
        start_at: dt.date,
        end_at: dt.date,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChromeDailyStatsPage:
        """
        Parameters
        ----------
        feature_id : str
            Feature ID

        start_at : dt.date
            Start date (RFC 3339, section 5.6, for example, 2017-07-21). The date is inclusive.

        end_at : dt.date
            End date (RFC 3339, section 5.6, for example, 2017-07-21). The date is exclusive.

        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChromeDailyStatsPage
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_chrome_daily_usage_stats(
                feature_id="feature_id",
                start_at=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
                end_at=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_chrome_daily_usage_stats(
            feature_id,
            start_at=start_at,
            end_at=end_at,
            page_token=page_token,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    async def list_global_saved_searches(
        self,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GlobalSavedSearchPage:
        """
        Parameters
        ----------
        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalSavedSearchPage
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_global_saved_searches()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_global_saved_searches(
            page_token=page_token, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def list_aggregated_feature_support(
        self,
        browser: SupportedBrowsers,
        *,
        start_at: dt.date,
        end_at: dt.date,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        include_baseline_mobile_browsers: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BrowserReleaseFeatureMetricsPage:
        """
        Parameters
        ----------
        browser : SupportedBrowsers
            Browser name

        start_at : dt.date
            Start date (RFC 3339, section 5.6, for example, 2017-07-21). The date is inclusive.

        end_at : dt.date
            End date (RFC 3339, section 5.6, for example, 2017-07-21). The date is exclusive.

        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        include_baseline_mobile_browsers : typing.Optional[bool]
            Include baseline mobile browsers in the response. This is only applicable for desktop browsers with a corresponding mobile browser.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BrowserReleaseFeatureMetricsPage
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, SupportedBrowsers

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_aggregated_feature_support(
                browser=SupportedBrowsers.CHROME,
                start_at=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
                end_at=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_aggregated_feature_support(
            browser,
            start_at=start_at,
            end_at=end_at,
            page_token=page_token,
            page_size=page_size,
            include_baseline_mobile_browsers=include_baseline_mobile_browsers,
            request_options=request_options,
        )
        return _response.data

    async def list_missing_one_implementation_counts(
        self,
        browser_path_param: SupportedBrowsers,
        *,
        start_at: dt.date,
        end_at: dt.date,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        include_baseline_mobile_browsers: typing.Optional[bool] = None,
        browser: typing.Optional[typing.Union[SupportedBrowsers, typing.Sequence[SupportedBrowsers]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BrowserReleaseFeatureMetricsPage:
        """
        Parameters
        ----------
        browser_path_param : SupportedBrowsers
            Browser name

        start_at : dt.date
            Start date (RFC 3339, section 5.6, for example, 2017-07-21). The date is inclusive.

        end_at : dt.date
            End date (RFC 3339, section 5.6, for example, 2017-07-21). The date is exclusive.

        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        include_baseline_mobile_browsers : typing.Optional[bool]
            Include baseline mobile browsers in the response. This is only applicable for desktop browsers with a corresponding mobile browser.

        browser : typing.Optional[typing.Union[SupportedBrowsers, typing.Sequence[SupportedBrowsers]]]
            A list of browsers to check if {browser} is lagging behind on features. The list is provided by specifying repeating query parameters. Example: ?browser=fooBrowser&browser=bazBrowser

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BrowserReleaseFeatureMetricsPage
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, SupportedBrowsers

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_missing_one_implementation_counts(
                browser_path_param=SupportedBrowsers.CHROME,
                start_at=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
                end_at=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
                browser=[SupportedBrowsers.CHROME],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_missing_one_implementation_counts(
            browser_path_param,
            start_at=start_at,
            end_at=end_at,
            page_token=page_token,
            page_size=page_size,
            include_baseline_mobile_browsers=include_baseline_mobile_browsers,
            browser=browser,
            request_options=request_options,
        )
        return _response.data

    async def list_missing_one_implementation_features(
        self,
        browser_path_param: SupportedBrowsers,
        date: dt.date,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        include_baseline_mobile_browsers: typing.Optional[bool] = None,
        browser: typing.Optional[typing.Union[SupportedBrowsers, typing.Sequence[SupportedBrowsers]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MissingOneImplFeaturesPage:
        """
        Parameters
        ----------
        browser_path_param : SupportedBrowsers
            Browser name

        date : dt.date
            The date for which to retrieve the feature IDs.

        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        include_baseline_mobile_browsers : typing.Optional[bool]
            Include baseline mobile browsers in the response. This is only applicable for desktop browsers with a corresponding mobile browser.

        browser : typing.Optional[typing.Union[SupportedBrowsers, typing.Sequence[SupportedBrowsers]]]
            A list of browsers to check if {browser} is lagging behind on features. The list is provided by specifying repeating query parameters. Example:?browser=fooBrowser&browser=bazBrowser

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MissingOneImplFeaturesPage
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, SupportedBrowsers

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_missing_one_implementation_features(
                browser_path_param=SupportedBrowsers.CHROME,
                date=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
                browser=[SupportedBrowsers.CHROME],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_missing_one_implementation_features(
            browser_path_param,
            date,
            page_token=page_token,
            page_size=page_size,
            include_baseline_mobile_browsers=include_baseline_mobile_browsers,
            browser=browser,
            request_options=request_options,
        )
        return _response.data

    async def list_aggregated_wpt_metrics(
        self,
        browser: SupportedBrowsers,
        channel: ListAggregatedWptMetricsRequestChannel,
        metric_view: WptMetricView,
        *,
        start_at: dt.date,
        end_at: dt.date,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        feature_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WptRunMetricsPage:
        """
        Parameters
        ----------
        browser : SupportedBrowsers
            Browser name

        channel : ListAggregatedWptMetricsRequestChannel
            Browser name

        metric_view : WptMetricView
            Specified metric view of the WPT data.

        start_at : dt.date
            Start date (RFC 3339, section 5.6, for example, 2017-07-21). The date is inclusive.

        end_at : dt.date
            End date (RFC 3339, section 5.6, for example, 2017-07-21). The date is exclusive.

        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        feature_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A list of feature IDs to filter results. TThe list is provided by specifying repeating query parameters. Example: ?featureId=id1&featureId=id2

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WptRunMetricsPage
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern import (
            AsyncFernApi,
            ListAggregatedWptMetricsRequestChannel,
            SupportedBrowsers,
            WptMetricView,
        )

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_aggregated_wpt_metrics(
                browser=SupportedBrowsers.CHROME,
                channel=ListAggregatedWptMetricsRequestChannel.STABLE,
                metric_view=WptMetricView.TEST_COUNTS,
                start_at=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
                end_at=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_aggregated_wpt_metrics(
            browser,
            channel,
            metric_view,
            start_at=start_at,
            end_at=end_at,
            page_token=page_token,
            page_size=page_size,
            feature_id=feature_id,
            request_options=request_options,
        )
        return _response.data

    async def list_aggregated_baseline_status_counts(
        self,
        *,
        start_at: dt.date,
        end_at: dt.date,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaselineStatusMetricsPage:
        """
        Parameters
        ----------
        start_at : dt.date
            Start date (RFC 3339, section 5.6, for example, 2017-07-21). The date is inclusive.

        end_at : dt.date
            End date (RFC 3339, section 5.6, for example, 2017-07-21). The date is exclusive.

        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaselineStatusMetricsPage
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_aggregated_baseline_status_counts(
                start_at=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
                end_at=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_aggregated_baseline_status_counts(
            start_at=start_at,
            end_at=end_at,
            page_token=page_token,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    async def ping_user(
        self, *, github_token: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Signals to the backend that a user has just authenticated.
        This allows the backend to perform tasks like creating or updating the user's profile
        with the latest information from the identity provider (e.g., refreshing their email address).

        This endpoint should be called by clients once, immediately after a successful login.

        Parameters
        ----------
        github_token : typing.Optional[str]
            The GitHub OAuth access token obtained by the frontend during interactive sign-in. Used by the backend to perform a one-time sync of user profile data (like email) directly from GitHub. This token is not stored by the backend.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ping_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.ping_user(github_token=github_token, request_options=request_options)
        return _response.data

    async def list_notification_channels(
        self,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationChannelPage:
        """
        Parameters
        ----------
        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationChannelPage
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_notification_channels()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_notification_channels(
            page_token=page_token, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def create_notification_channel(
        self,
        *,
        name: str,
        config: CreateNotificationChannelRequestConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationChannelResponse:
        """
        Parameters
        ----------
        name : str
            A user-defined name for the channel.

        config : CreateNotificationChannelRequestConfig
            Configuration specific to the channel type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationChannelResponse
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CreateNotificationChannelRequestConfig_Webhook

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_notification_channel(
                name="name",
                config=CreateNotificationChannelRequestConfig_Webhook(
                    url="url",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_notification_channel(
            name=name, config=config, request_options=request_options
        )
        return _response.data

    async def get_notification_channel(
        self, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NotificationChannelResponse:
        """
        Parameters
        ----------
        channel_id : str
            Notification Channel ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationChannelResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_notification_channel(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_notification_channel(channel_id, request_options=request_options)
        return _response.data

    async def delete_notification_channel(
        self, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        channel_id : str
            Notification Channel ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_notification_channel(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_notification_channel(channel_id, request_options=request_options)
        return _response.data

    async def update_notification_channel(
        self,
        channel_id: str,
        *,
        update_mask: typing.Sequence[UpdateNotificationChannelRequestUpdateMaskItem],
        name: typing.Optional[str] = OMIT,
        config: typing.Optional[UpdateNotificationChannelRequestConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationChannelResponse:
        """
        Parameters
        ----------
        channel_id : str
            Notification Channel ID

        update_mask : typing.Sequence[UpdateNotificationChannelRequestUpdateMaskItem]
            A list of fields to update. Required. Allowed values are: `name`, `config`.

        name : typing.Optional[str]

        config : typing.Optional[UpdateNotificationChannelRequestConfig]
            Configuration specific to the channel type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationChannelResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, UpdateNotificationChannelRequestUpdateMaskItem

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.update_notification_channel(
                channel_id="channel_id",
                update_mask=[UpdateNotificationChannelRequestUpdateMaskItem.NAME],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_notification_channel(
            channel_id, update_mask=update_mask, name=name, config=config, request_options=request_options
        )
        return _response.data

    async def list_user_saved_searches(
        self,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserSavedSearchPage:
        """
        Parameters
        ----------
        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserSavedSearchPage
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_user_saved_searches()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_user_saved_searches(
            page_token=page_token, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def put_user_saved_search_bookmark(
        self, search_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        search_id : str
            Saved Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.put_user_saved_search_bookmark(
                search_id="search_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_user_saved_search_bookmark(search_id, request_options=request_options)
        return _response.data

    async def remove_user_saved_search_bookmark(
        self, search_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        search_id : str
            Saved Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.remove_user_saved_search_bookmark(
                search_id="search_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_user_saved_search_bookmark(search_id, request_options=request_options)
        return _response.data

    async def create_saved_search(
        self,
        *,
        name: str,
        query: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SavedSearchResponse:
        """
        Parameters
        ----------
        name : str

        query : str

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SavedSearchResponse
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_saved_search(
                name="name",
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_saved_search(
            name=name, query=query, description=description, request_options=request_options
        )
        return _response.data

    async def get_saved_search(
        self, search_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SavedSearchResponse:
        """
        Parameters
        ----------
        search_id : str
            Saved Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SavedSearchResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_saved_search(
                search_id="search_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_saved_search(search_id, request_options=request_options)
        return _response.data

    async def remove_saved_search(
        self, search_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        search_id : str
            Saved Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.remove_saved_search(
                search_id="search_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_saved_search(search_id, request_options=request_options)
        return _response.data

    async def update_saved_search(
        self,
        search_id: str,
        *,
        update_mask: typing.Sequence[SavedSearchUpdateRequestUpdateMaskItem],
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        query: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SavedSearchResponse:
        """
        Parameters
        ----------
        search_id : str
            Saved Search ID

        update_mask : typing.Sequence[SavedSearchUpdateRequestUpdateMaskItem]
            A list of fields to update. Required. Allowed values are: `name`, `description`, `query`.

        name : typing.Optional[str]

        description : typing.Optional[str]

        query : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SavedSearchResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SavedSearchUpdateRequestUpdateMaskItem

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.update_saved_search(
                search_id="search_id",
                update_mask=[SavedSearchUpdateRequestUpdateMaskItem.NAME],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_saved_search(
            search_id,
            update_mask=update_mask,
            name=name,
            description=description,
            query=query,
            request_options=request_options,
        )
        return _response.data

    async def list_subscriptions(
        self,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionPage:
        """
        Parameters
        ----------
        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionPage
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_subscriptions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_subscriptions(
            page_token=page_token, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def create_subscription(
        self,
        *,
        saved_search_id: str,
        frequency: SubscriptionFrequency,
        triggers: typing.Sequence[SubscriptionTriggerWritable],
        channel_id: typing.Optional[str] = OMIT,
        channel_type: typing.Optional[SubscriptionChannelType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionResponse:
        """
        Parameters
        ----------
        saved_search_id : str

        frequency : SubscriptionFrequency

        triggers : typing.Sequence[SubscriptionTriggerWritable]

        channel_id : typing.Optional[str]
            Explicit Mode: Provide a specific channel ID. Required for manual channels (Webhook/Email). Mutually exclusive with 'channel_type'.

        channel_type : typing.Optional[SubscriptionChannelType]
            Implicit Mode: Provide a channel type. Used for system-managed channels (e.g., 'rss') where the system automatically resolves or creates the channel. Mutually exclusive with 'channel_id'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionResponse
            Created

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            SubscriptionFrequency,
            SubscriptionTriggerWritable,
        )

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_subscription(
                saved_search_id="saved_search_id",
                frequency=SubscriptionFrequency.IMMEDIATE,
                triggers=[SubscriptionTriggerWritable.FEATURE_BASELINE_TO_NEWLY],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_subscription(
            saved_search_id=saved_search_id,
            frequency=frequency,
            triggers=triggers,
            channel_id=channel_id,
            channel_type=channel_type,
            request_options=request_options,
        )
        return _response.data

    async def get_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SubscriptionResponse:
        """
        Parameters
        ----------
        subscription_id : str
            Subscription ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_subscription(
                subscription_id="subscription_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_subscription(subscription_id, request_options=request_options)
        return _response.data

    async def delete_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str
            Subscription ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_subscription(
                subscription_id="subscription_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_subscription(subscription_id, request_options=request_options)
        return _response.data

    async def update_subscription(
        self,
        subscription_id: str,
        *,
        update_mask: typing.Sequence[UpdateSubscriptionRequestUpdateMaskItem],
        triggers: typing.Optional[typing.Sequence[SubscriptionTriggerWritable]] = OMIT,
        frequency: typing.Optional[SubscriptionFrequency] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionResponse:
        """
        Parameters
        ----------
        subscription_id : str
            Subscription ID

        update_mask : typing.Sequence[UpdateSubscriptionRequestUpdateMaskItem]
            A list of fields to update. Required. Allowed values are: `triggers`, `frequency`.

        triggers : typing.Optional[typing.Sequence[SubscriptionTriggerWritable]]

        frequency : typing.Optional[SubscriptionFrequency]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, UpdateSubscriptionRequestUpdateMaskItem

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.update_subscription(
                subscription_id="subscription_id",
                update_mask=[UpdateSubscriptionRequestUpdateMaskItem.TRIGGERS],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_subscription(
            subscription_id,
            update_mask=update_mask,
            triggers=triggers,
            frequency=frequency,
            request_options=request_options,
        )
        return _response.data

    async def get_subscription_rss(
        self,
        subscription_id: str,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str
            Subscription ID

        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_subscription_rss(
                subscription_id="subscription_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_subscription_rss(
            subscription_id, page_token=page_token, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def list_code_subscriptions(
        self,
        provider: ListCodeSubscriptionsRequestProvider,
        repository_id: str,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CodeSubscriptionPage:
        """
        Parameters
        ----------
        provider : ListCodeSubscriptionsRequestProvider

        repository_id : str

        page_token : typing.Optional[str]
            Pagination token

        page_size : typing.Optional[int]
            Number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CodeSubscriptionPage
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ListCodeSubscriptionsRequestProvider

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.list_code_subscriptions(
                provider=ListCodeSubscriptionsRequestProvider.GITHUB,
                repository_id="repository_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_code_subscriptions(
            provider, repository_id, page_token=page_token, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def handle_vcs_webhook(
        self,
        provider: HandleVcsWebhookRequestProvider,
        *,
        request: bytes,
        hub_signature256: typing.Optional[str] = None,
        git_hub_delivery: typing.Optional[str] = None,
        git_hub_event: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        provider : HandleVcsWebhookRequestProvider

        request : bytes

        hub_signature256 : typing.Optional[str]

        git_hub_delivery : typing.Optional[str]

        git_hub_event : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, HandleVcsWebhookRequestProvider

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.handle_vcs_webhook(
                provider=HandleVcsWebhookRequestProvider.GITHUB,
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.handle_vcs_webhook(
            provider,
            request=request,
            hub_signature256=hub_signature256,
            git_hub_delivery=git_hub_delivery,
            git_hub_event=git_hub_event,
            request_options=request_options,
        )
        return _response.data

    @property
    def healthchecks(self):
        if self._healthchecks is None:
            from .healthchecks.client import AsyncHealthchecksClient

            self._healthchecks = AsyncHealthchecksClient(client_wrapper=self._client_wrapper)
        return self._healthchecks


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
