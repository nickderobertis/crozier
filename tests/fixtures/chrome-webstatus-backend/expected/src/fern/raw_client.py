

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .errors.bad_request_error import BadRequestError
from .errors.forbidden_error import ForbiddenError
from .errors.gone_error import GoneError
from .errors.internal_server_error import InternalServerError
from .errors.not_found_error import NotFoundError
from .errors.too_many_requests_error import TooManyRequestsError
from .errors.unauthorized_error import UnauthorizedError
from .types.baseline_status_metrics_page import BaselineStatusMetricsPage
from .types.basic_error_model import BasicErrorModel
from .types.browser_release_feature_metrics_page import BrowserReleaseFeatureMetricsPage
from .types.chrome_daily_stats_page import ChromeDailyStatsPage
from .types.code_subscription_page import CodeSubscriptionPage
from .types.create_notification_channel_request_config import CreateNotificationChannelRequestConfig
from .types.feature import Feature
from .types.feature_gone_error import FeatureGoneError
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_features(
        self,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        wpt_metric_view: typing.Optional[WptMetricView] = None,
        q: typing.Optional[str] = None,
        sort: typing.Optional[ListFeaturesRequestSort] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FeaturePage]:
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
        HttpResponse[FeaturePage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/features",
            method="GET",
            params={
                "page_token": page_token,
                "page_size": page_size,
                "wpt_metric_view": wpt_metric_view,
                "q": q,
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeaturePage,
                    parse_obj_as(
                        type_=FeaturePage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_feature(
        self,
        feature_id: str,
        *,
        wpt_metric_view: typing.Optional[WptMetricView] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Feature]:
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
        HttpResponse[Feature]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/features/{encode_path_param(feature_id)}",
            method="GET",
            params={
                "wpt_metric_view": wpt_metric_view,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Feature,
                    parse_obj_as(
                        type_=Feature,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        FeatureGoneError,
                        parse_obj_as(
                            type_=FeatureGoneError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_feature_metadata(
        self, feature_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FeatureMetadata]:
        """
        Parameters
        ----------
        feature_id : str
            Feature ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeatureMetadata]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/features/{encode_path_param(feature_id)}/feature-metadata",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeatureMetadata,
                    parse_obj_as(
                        type_=FeatureMetadata,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[WptRunMetricsPage]:
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
        HttpResponse[WptRunMetricsPage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/features/{encode_path_param(feature_id)}/stats/wpt/browsers/{encode_path_param(browser)}/channels/{encode_path_param(channel)}/{encode_path_param(metric_view)}",
            method="GET",
            params={
                "startAt": str(start_at),
                "endAt": str(end_at),
                "page_token": page_token,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WptRunMetricsPage,
                    parse_obj_as(
                        type_=WptRunMetricsPage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_chrome_daily_usage_stats(
        self,
        feature_id: str,
        *,
        start_at: dt.date,
        end_at: dt.date,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChromeDailyStatsPage]:
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
        HttpResponse[ChromeDailyStatsPage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/features/{encode_path_param(feature_id)}/stats/usage/chrome/daily_stats",
            method="GET",
            params={
                "startAt": str(start_at),
                "endAt": str(end_at),
                "page_token": page_token,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChromeDailyStatsPage,
                    parse_obj_as(
                        type_=ChromeDailyStatsPage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_global_saved_searches(
        self,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GlobalSavedSearchPage]:
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
        HttpResponse[GlobalSavedSearchPage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/global-saved-searches",
            method="GET",
            params={
                "page_token": page_token,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalSavedSearchPage,
                    parse_obj_as(
                        type_=GlobalSavedSearchPage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[BrowserReleaseFeatureMetricsPage]:
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
        HttpResponse[BrowserReleaseFeatureMetricsPage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/stats/features/browsers/{encode_path_param(browser)}/feature_counts",
            method="GET",
            params={
                "startAt": str(start_at),
                "endAt": str(end_at),
                "page_token": page_token,
                "page_size": page_size,
                "include_baseline_mobile_browsers": include_baseline_mobile_browsers,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BrowserReleaseFeatureMetricsPage,
                    parse_obj_as(
                        type_=BrowserReleaseFeatureMetricsPage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[BrowserReleaseFeatureMetricsPage]:
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
        HttpResponse[BrowserReleaseFeatureMetricsPage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/stats/features/browsers/{encode_path_param(browser_path_param)}/missing_one_implementation_counts",
            method="GET",
            params={
                "startAt": str(start_at),
                "endAt": str(end_at),
                "page_token": page_token,
                "page_size": page_size,
                "include_baseline_mobile_browsers": include_baseline_mobile_browsers,
                "browser": browser,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BrowserReleaseFeatureMetricsPage,
                    parse_obj_as(
                        type_=BrowserReleaseFeatureMetricsPage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[MissingOneImplFeaturesPage]:
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
        HttpResponse[MissingOneImplFeaturesPage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/stats/features/browsers/{encode_path_param(browser_path_param)}/missing_one_implementation_counts/{encode_path_param(date)}/features",
            method="GET",
            params={
                "page_token": page_token,
                "page_size": page_size,
                "include_baseline_mobile_browsers": include_baseline_mobile_browsers,
                "browser": browser,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MissingOneImplFeaturesPage,
                    parse_obj_as(
                        type_=MissingOneImplFeaturesPage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[WptRunMetricsPage]:
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
        HttpResponse[WptRunMetricsPage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/stats/wpt/browsers/{encode_path_param(browser)}/channels/{encode_path_param(channel)}/{encode_path_param(metric_view)}",
            method="GET",
            params={
                "startAt": str(start_at),
                "endAt": str(end_at),
                "page_token": page_token,
                "page_size": page_size,
                "featureId": feature_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WptRunMetricsPage,
                    parse_obj_as(
                        type_=WptRunMetricsPage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_aggregated_baseline_status_counts(
        self,
        *,
        start_at: dt.date,
        end_at: dt.date,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BaselineStatusMetricsPage]:
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
        HttpResponse[BaselineStatusMetricsPage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/stats/baseline_status/low_date_feature_counts",
            method="GET",
            params={
                "startAt": str(start_at),
                "endAt": str(end_at),
                "page_token": page_token,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BaselineStatusMetricsPage,
                    parse_obj_as(
                        type_=BaselineStatusMetricsPage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def ping_user(
        self, *, github_token: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/users/me/ping",
            method="POST",
            json={
                "github_token": github_token,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_notification_channels(
        self,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NotificationChannelPage]:
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
        HttpResponse[NotificationChannelPage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/users/me/notification-channels",
            method="GET",
            params={
                "page_token": page_token,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationChannelPage,
                    parse_obj_as(
                        type_=NotificationChannelPage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_notification_channel(
        self,
        *,
        name: str,
        config: CreateNotificationChannelRequestConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NotificationChannelResponse]:
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
        HttpResponse[NotificationChannelResponse]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/users/me/notification-channels",
            method="POST",
            json={
                "name": name,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=CreateNotificationChannelRequestConfig, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationChannelResponse,
                    parse_obj_as(
                        type_=NotificationChannelResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_notification_channel(
        self, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NotificationChannelResponse]:
        """
        Parameters
        ----------
        channel_id : str
            Notification Channel ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NotificationChannelResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/users/me/notification-channels/{encode_path_param(channel_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationChannelResponse,
                    parse_obj_as(
                        type_=NotificationChannelResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_notification_channel(
        self, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : str
            Notification Channel ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/users/me/notification-channels/{encode_path_param(channel_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_notification_channel(
        self,
        channel_id: str,
        *,
        update_mask: typing.Sequence[UpdateNotificationChannelRequestUpdateMaskItem],
        name: typing.Optional[str] = OMIT,
        config: typing.Optional[UpdateNotificationChannelRequestConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NotificationChannelResponse]:
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
        HttpResponse[NotificationChannelResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/users/me/notification-channels/{encode_path_param(channel_id)}",
            method="PATCH",
            json={
                "name": name,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=UpdateNotificationChannelRequestConfig, direction="write"
                ),
                "update_mask": update_mask,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationChannelResponse,
                    parse_obj_as(
                        type_=NotificationChannelResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_user_saved_searches(
        self,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UserSavedSearchPage]:
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
        HttpResponse[UserSavedSearchPage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/users/me/saved-searches",
            method="GET",
            params={
                "page_token": page_token,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserSavedSearchPage,
                    parse_obj_as(
                        type_=UserSavedSearchPage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def put_user_saved_search_bookmark(
        self, search_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        search_id : str
            Saved Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/users/me/saved-searches/{encode_path_param(search_id)}/bookmark_status",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def remove_user_saved_search_bookmark(
        self, search_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        search_id : str
            Saved Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/users/me/saved-searches/{encode_path_param(search_id)}/bookmark_status",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_saved_search(
        self,
        *,
        name: str,
        query: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SavedSearchResponse]:
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
        HttpResponse[SavedSearchResponse]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/saved-searches",
            method="POST",
            json={
                "name": name,
                "description": description,
                "query": query,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SavedSearchResponse,
                    parse_obj_as(
                        type_=SavedSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_saved_search(
        self, search_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SavedSearchResponse]:
        """
        Parameters
        ----------
        search_id : str
            Saved Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SavedSearchResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/saved-searches/{encode_path_param(search_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SavedSearchResponse,
                    parse_obj_as(
                        type_=SavedSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def remove_saved_search(
        self, search_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        search_id : str
            Saved Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/saved-searches/{encode_path_param(search_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_saved_search(
        self,
        search_id: str,
        *,
        update_mask: typing.Sequence[SavedSearchUpdateRequestUpdateMaskItem],
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        query: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SavedSearchResponse]:
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
        HttpResponse[SavedSearchResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/saved-searches/{encode_path_param(search_id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "query": query,
                "update_mask": update_mask,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SavedSearchResponse,
                    parse_obj_as(
                        type_=SavedSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_subscriptions(
        self,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubscriptionPage]:
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
        HttpResponse[SubscriptionPage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/users/me/subscriptions",
            method="GET",
            params={
                "page_token": page_token,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionPage,
                    parse_obj_as(
                        type_=SubscriptionPage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_subscription(
        self,
        *,
        saved_search_id: str,
        frequency: SubscriptionFrequency,
        triggers: typing.Sequence[SubscriptionTriggerWritable],
        channel_id: typing.Optional[str] = OMIT,
        channel_type: typing.Optional[SubscriptionChannelType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubscriptionResponse]:
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
        HttpResponse[SubscriptionResponse]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/users/me/subscriptions",
            method="POST",
            json={
                "saved_search_id": saved_search_id,
                "channel_id": channel_id,
                "channel_type": channel_type,
                "frequency": frequency,
                "triggers": triggers,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionResponse,
                    parse_obj_as(
                        type_=SubscriptionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SubscriptionResponse]:
        """
        Parameters
        ----------
        subscription_id : str
            Subscription ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubscriptionResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/users/me/subscriptions/{encode_path_param(subscription_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionResponse,
                    parse_obj_as(
                        type_=SubscriptionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str
            Subscription ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/users/me/subscriptions/{encode_path_param(subscription_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_subscription(
        self,
        subscription_id: str,
        *,
        update_mask: typing.Sequence[UpdateSubscriptionRequestUpdateMaskItem],
        triggers: typing.Optional[typing.Sequence[SubscriptionTriggerWritable]] = OMIT,
        frequency: typing.Optional[SubscriptionFrequency] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubscriptionResponse]:
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
        HttpResponse[SubscriptionResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/users/me/subscriptions/{encode_path_param(subscription_id)}",
            method="PATCH",
            json={
                "triggers": triggers,
                "frequency": frequency,
                "update_mask": update_mask,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionResponse,
                    parse_obj_as(
                        type_=SubscriptionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_subscription_rss(
        self,
        subscription_id: str,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/subscriptions/{encode_path_param(subscription_id)}/rss",
            method="GET",
            params={
                "page_token": page_token,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_code_subscriptions(
        self,
        provider: ListCodeSubscriptionsRequestProvider,
        repository_id: str,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CodeSubscriptionPage]:
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
        HttpResponse[CodeSubscriptionPage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/vcs/{encode_path_param(provider)}/repositories/{encode_path_param(repository_id)}/code-subscriptions",
            method="GET",
            params={
                "page_token": page_token,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CodeSubscriptionPage,
                    parse_obj_as(
                        type_=CodeSubscriptionPage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def handle_vcs_webhook(
        self,
        provider: HandleVcsWebhookRequestProvider,
        *,
        request: bytes,
        hub_signature256: typing.Optional[str] = None,
        git_hub_delivery: typing.Optional[str] = None,
        git_hub_event: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/webhooks/{encode_path_param(provider)}",
            method="POST",
            json=request,
            headers={
                "X-Hub-Signature-256": str(hub_signature256) if hub_signature256 is not None else None,
                "X-GitHub-Delivery": str(git_hub_delivery) if git_hub_delivery is not None else None,
                "X-GitHub-Event": str(git_hub_event) if git_hub_event is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_features(
        self,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        wpt_metric_view: typing.Optional[WptMetricView] = None,
        q: typing.Optional[str] = None,
        sort: typing.Optional[ListFeaturesRequestSort] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FeaturePage]:
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
        AsyncHttpResponse[FeaturePage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/features",
            method="GET",
            params={
                "page_token": page_token,
                "page_size": page_size,
                "wpt_metric_view": wpt_metric_view,
                "q": q,
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeaturePage,
                    parse_obj_as(
                        type_=FeaturePage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_feature(
        self,
        feature_id: str,
        *,
        wpt_metric_view: typing.Optional[WptMetricView] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Feature]:
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
        AsyncHttpResponse[Feature]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/features/{encode_path_param(feature_id)}",
            method="GET",
            params={
                "wpt_metric_view": wpt_metric_view,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Feature,
                    parse_obj_as(
                        type_=Feature,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        FeatureGoneError,
                        parse_obj_as(
                            type_=FeatureGoneError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_feature_metadata(
        self, feature_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FeatureMetadata]:
        """
        Parameters
        ----------
        feature_id : str
            Feature ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeatureMetadata]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/features/{encode_path_param(feature_id)}/feature-metadata",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeatureMetadata,
                    parse_obj_as(
                        type_=FeatureMetadata,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[WptRunMetricsPage]:
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
        AsyncHttpResponse[WptRunMetricsPage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/features/{encode_path_param(feature_id)}/stats/wpt/browsers/{encode_path_param(browser)}/channels/{encode_path_param(channel)}/{encode_path_param(metric_view)}",
            method="GET",
            params={
                "startAt": str(start_at),
                "endAt": str(end_at),
                "page_token": page_token,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WptRunMetricsPage,
                    parse_obj_as(
                        type_=WptRunMetricsPage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_chrome_daily_usage_stats(
        self,
        feature_id: str,
        *,
        start_at: dt.date,
        end_at: dt.date,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChromeDailyStatsPage]:
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
        AsyncHttpResponse[ChromeDailyStatsPage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/features/{encode_path_param(feature_id)}/stats/usage/chrome/daily_stats",
            method="GET",
            params={
                "startAt": str(start_at),
                "endAt": str(end_at),
                "page_token": page_token,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChromeDailyStatsPage,
                    parse_obj_as(
                        type_=ChromeDailyStatsPage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_global_saved_searches(
        self,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GlobalSavedSearchPage]:
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
        AsyncHttpResponse[GlobalSavedSearchPage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/global-saved-searches",
            method="GET",
            params={
                "page_token": page_token,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalSavedSearchPage,
                    parse_obj_as(
                        type_=GlobalSavedSearchPage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[BrowserReleaseFeatureMetricsPage]:
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
        AsyncHttpResponse[BrowserReleaseFeatureMetricsPage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/stats/features/browsers/{encode_path_param(browser)}/feature_counts",
            method="GET",
            params={
                "startAt": str(start_at),
                "endAt": str(end_at),
                "page_token": page_token,
                "page_size": page_size,
                "include_baseline_mobile_browsers": include_baseline_mobile_browsers,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BrowserReleaseFeatureMetricsPage,
                    parse_obj_as(
                        type_=BrowserReleaseFeatureMetricsPage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[BrowserReleaseFeatureMetricsPage]:
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
        AsyncHttpResponse[BrowserReleaseFeatureMetricsPage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/stats/features/browsers/{encode_path_param(browser_path_param)}/missing_one_implementation_counts",
            method="GET",
            params={
                "startAt": str(start_at),
                "endAt": str(end_at),
                "page_token": page_token,
                "page_size": page_size,
                "include_baseline_mobile_browsers": include_baseline_mobile_browsers,
                "browser": browser,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BrowserReleaseFeatureMetricsPage,
                    parse_obj_as(
                        type_=BrowserReleaseFeatureMetricsPage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[MissingOneImplFeaturesPage]:
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
        AsyncHttpResponse[MissingOneImplFeaturesPage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/stats/features/browsers/{encode_path_param(browser_path_param)}/missing_one_implementation_counts/{encode_path_param(date)}/features",
            method="GET",
            params={
                "page_token": page_token,
                "page_size": page_size,
                "include_baseline_mobile_browsers": include_baseline_mobile_browsers,
                "browser": browser,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MissingOneImplFeaturesPage,
                    parse_obj_as(
                        type_=MissingOneImplFeaturesPage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[WptRunMetricsPage]:
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
        AsyncHttpResponse[WptRunMetricsPage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/stats/wpt/browsers/{encode_path_param(browser)}/channels/{encode_path_param(channel)}/{encode_path_param(metric_view)}",
            method="GET",
            params={
                "startAt": str(start_at),
                "endAt": str(end_at),
                "page_token": page_token,
                "page_size": page_size,
                "featureId": feature_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WptRunMetricsPage,
                    parse_obj_as(
                        type_=WptRunMetricsPage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_aggregated_baseline_status_counts(
        self,
        *,
        start_at: dt.date,
        end_at: dt.date,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BaselineStatusMetricsPage]:
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
        AsyncHttpResponse[BaselineStatusMetricsPage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/stats/baseline_status/low_date_feature_counts",
            method="GET",
            params={
                "startAt": str(start_at),
                "endAt": str(end_at),
                "page_token": page_token,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BaselineStatusMetricsPage,
                    parse_obj_as(
                        type_=BaselineStatusMetricsPage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def ping_user(
        self, *, github_token: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/users/me/ping",
            method="POST",
            json={
                "github_token": github_token,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_notification_channels(
        self,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NotificationChannelPage]:
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
        AsyncHttpResponse[NotificationChannelPage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/users/me/notification-channels",
            method="GET",
            params={
                "page_token": page_token,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationChannelPage,
                    parse_obj_as(
                        type_=NotificationChannelPage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_notification_channel(
        self,
        *,
        name: str,
        config: CreateNotificationChannelRequestConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NotificationChannelResponse]:
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
        AsyncHttpResponse[NotificationChannelResponse]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/users/me/notification-channels",
            method="POST",
            json={
                "name": name,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=CreateNotificationChannelRequestConfig, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationChannelResponse,
                    parse_obj_as(
                        type_=NotificationChannelResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_notification_channel(
        self, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NotificationChannelResponse]:
        """
        Parameters
        ----------
        channel_id : str
            Notification Channel ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NotificationChannelResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/users/me/notification-channels/{encode_path_param(channel_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationChannelResponse,
                    parse_obj_as(
                        type_=NotificationChannelResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_notification_channel(
        self, channel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : str
            Notification Channel ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/users/me/notification-channels/{encode_path_param(channel_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_notification_channel(
        self,
        channel_id: str,
        *,
        update_mask: typing.Sequence[UpdateNotificationChannelRequestUpdateMaskItem],
        name: typing.Optional[str] = OMIT,
        config: typing.Optional[UpdateNotificationChannelRequestConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NotificationChannelResponse]:
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
        AsyncHttpResponse[NotificationChannelResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/users/me/notification-channels/{encode_path_param(channel_id)}",
            method="PATCH",
            json={
                "name": name,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=UpdateNotificationChannelRequestConfig, direction="write"
                ),
                "update_mask": update_mask,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationChannelResponse,
                    parse_obj_as(
                        type_=NotificationChannelResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_user_saved_searches(
        self,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UserSavedSearchPage]:
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
        AsyncHttpResponse[UserSavedSearchPage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/users/me/saved-searches",
            method="GET",
            params={
                "page_token": page_token,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserSavedSearchPage,
                    parse_obj_as(
                        type_=UserSavedSearchPage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def put_user_saved_search_bookmark(
        self, search_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        search_id : str
            Saved Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/users/me/saved-searches/{encode_path_param(search_id)}/bookmark_status",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def remove_user_saved_search_bookmark(
        self, search_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        search_id : str
            Saved Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/users/me/saved-searches/{encode_path_param(search_id)}/bookmark_status",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_saved_search(
        self,
        *,
        name: str,
        query: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SavedSearchResponse]:
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
        AsyncHttpResponse[SavedSearchResponse]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/saved-searches",
            method="POST",
            json={
                "name": name,
                "description": description,
                "query": query,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SavedSearchResponse,
                    parse_obj_as(
                        type_=SavedSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_saved_search(
        self, search_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SavedSearchResponse]:
        """
        Parameters
        ----------
        search_id : str
            Saved Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SavedSearchResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/saved-searches/{encode_path_param(search_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SavedSearchResponse,
                    parse_obj_as(
                        type_=SavedSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def remove_saved_search(
        self, search_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        search_id : str
            Saved Search ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/saved-searches/{encode_path_param(search_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_saved_search(
        self,
        search_id: str,
        *,
        update_mask: typing.Sequence[SavedSearchUpdateRequestUpdateMaskItem],
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        query: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SavedSearchResponse]:
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
        AsyncHttpResponse[SavedSearchResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/saved-searches/{encode_path_param(search_id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "query": query,
                "update_mask": update_mask,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SavedSearchResponse,
                    parse_obj_as(
                        type_=SavedSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_subscriptions(
        self,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubscriptionPage]:
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
        AsyncHttpResponse[SubscriptionPage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/users/me/subscriptions",
            method="GET",
            params={
                "page_token": page_token,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionPage,
                    parse_obj_as(
                        type_=SubscriptionPage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_subscription(
        self,
        *,
        saved_search_id: str,
        frequency: SubscriptionFrequency,
        triggers: typing.Sequence[SubscriptionTriggerWritable],
        channel_id: typing.Optional[str] = OMIT,
        channel_type: typing.Optional[SubscriptionChannelType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubscriptionResponse]:
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
        AsyncHttpResponse[SubscriptionResponse]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/users/me/subscriptions",
            method="POST",
            json={
                "saved_search_id": saved_search_id,
                "channel_id": channel_id,
                "channel_type": channel_type,
                "frequency": frequency,
                "triggers": triggers,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionResponse,
                    parse_obj_as(
                        type_=SubscriptionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SubscriptionResponse]:
        """
        Parameters
        ----------
        subscription_id : str
            Subscription ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubscriptionResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/users/me/subscriptions/{encode_path_param(subscription_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionResponse,
                    parse_obj_as(
                        type_=SubscriptionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        subscription_id : str
            Subscription ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/users/me/subscriptions/{encode_path_param(subscription_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_subscription(
        self,
        subscription_id: str,
        *,
        update_mask: typing.Sequence[UpdateSubscriptionRequestUpdateMaskItem],
        triggers: typing.Optional[typing.Sequence[SubscriptionTriggerWritable]] = OMIT,
        frequency: typing.Optional[SubscriptionFrequency] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubscriptionResponse]:
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
        AsyncHttpResponse[SubscriptionResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/users/me/subscriptions/{encode_path_param(subscription_id)}",
            method="PATCH",
            json={
                "triggers": triggers,
                "frequency": frequency,
                "update_mask": update_mask,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionResponse,
                    parse_obj_as(
                        type_=SubscriptionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_subscription_rss(
        self,
        subscription_id: str,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/subscriptions/{encode_path_param(subscription_id)}/rss",
            method="GET",
            params={
                "page_token": page_token,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_code_subscriptions(
        self,
        provider: ListCodeSubscriptionsRequestProvider,
        repository_id: str,
        *,
        page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CodeSubscriptionPage]:
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
        AsyncHttpResponse[CodeSubscriptionPage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/vcs/{encode_path_param(provider)}/repositories/{encode_path_param(repository_id)}/code-subscriptions",
            method="GET",
            params={
                "page_token": page_token,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CodeSubscriptionPage,
                    parse_obj_as(
                        type_=CodeSubscriptionPage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def handle_vcs_webhook(
        self,
        provider: HandleVcsWebhookRequestProvider,
        *,
        request: bytes,
        hub_signature256: typing.Optional[str] = None,
        git_hub_delivery: typing.Optional[str] = None,
        git_hub_event: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/webhooks/{encode_path_param(provider)}",
            method="POST",
            json=request,
            headers={
                "X-Hub-Signature-256": str(hub_signature256) if hub_signature256 is not None else None,
                "X-GitHub-Delivery": str(git_hub_delivery) if git_hub_delivery is not None else None,
                "X-GitHub-Event": str(git_hub_event) if git_hub_event is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BasicErrorModel,
                        parse_obj_as(
                            type_=BasicErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
