

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.datetime_utils import serialize_datetime
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.jsonable_encoder import encode_path_param
from ...core.parse_error import ParsingError
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...core.serialization import convert_and_respect_annotation_metadata
from ...errors.bad_request_error import BadRequestError
from ...errors.forbidden_error import ForbiddenError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...errors.too_many_requests_error import TooManyRequestsError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.time_on_page_reports_request_filter import TimeOnPageReportsRequestFilter
from ...types.time_on_page_reports_request_timeseries import TimeOnPageReportsRequestTimeseries
from ...types.top_dimensions_reports_request_filter import TopDimensionsReportsRequestFilter
from ...types.top_events_reports_request_filter import TopEventsReportsRequestFilter
from ...types.top_events_reports_request_timeseries import TopEventsReportsRequestTimeseries
from ...types.top_pages_reports_request_filter import TopPagesReportsRequestFilter
from ...types.top_pages_reports_request_timeseries import TopPagesReportsRequestTimeseries
from ...types.traffic_reports_request_filter import TrafficReportsRequestFilter
from .types.time_on_page_reports_request_device_type import TimeOnPageReportsRequestDeviceType
from .types.time_on_page_reports_request_metric_scope import TimeOnPageReportsRequestMetricScope
from .types.time_on_page_reports_response import TimeOnPageReportsResponse
from .types.top_dimensions_reports_request_device_type import TopDimensionsReportsRequestDeviceType
from .types.top_dimensions_reports_request_dimension import TopDimensionsReportsRequestDimension
from .types.top_dimensions_reports_request_metric_scope import TopDimensionsReportsRequestMetricScope
from .types.top_dimensions_reports_response import TopDimensionsReportsResponse
from .types.top_events_reports_request_device_type import TopEventsReportsRequestDeviceType
from .types.top_events_reports_response import TopEventsReportsResponse
from .types.top_pages_reports_request_device_type import TopPagesReportsRequestDeviceType
from .types.top_pages_reports_request_sort_by import TopPagesReportsRequestSortBy
from .types.top_pages_reports_response import TopPagesReportsResponse
from .types.traffic_reports_request_device_type import TrafficReportsRequestDeviceType
from .types.traffic_reports_request_metric_scope import TrafficReportsRequestMetricScope
from .types.traffic_reports_response import TrafficReportsResponse
from pydantic import ValidationError


class RawReportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def traffic(
        self,
        site_id: str,
        *,
        start_time: dt.datetime,
        end_time: dt.datetime,
        metric_scope: TrafficReportsRequestMetricScope,
        bucket_time_zone: str,
        device_type: typing.Optional[TrafficReportsRequestDeviceType] = None,
        country: typing.Optional[str] = None,
        page_path: typing.Optional[str] = None,
        traffic_source: typing.Optional[str] = None,
        referrer: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        utm_campaign: typing.Optional[str] = None,
        utm_medium: typing.Optional[str] = None,
        utm_source: typing.Optional[str] = None,
        filter: typing.Optional[TrafficReportsRequestFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TrafficReportsResponse]:
        """
        Returns a daily time series of a single metric — sessions, users, or pageviews — over a time window.

        Filter the report with top-level query parameters (`country`, `deviceType`, `pagePath`, etc.) or via the `filter` parameter for multi-value and negation matching.

        <Warning title="Analyze add-on required">This endpoint requires a workspace with the Analyze add-on.</Warning>

        <Note title="Concurrency limit: 1 request at a time">Each access token can have one Analyze request in flight at a time, across all Analyze endpoints. Additional concurrent requests return `429 Too Many Requests`; wait for your in-flight request to finish, or for the `Retry-After` interval, then retry.</Note>

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        start_time : dt.datetime
            Inclusive start of the reporting window. Must be a UTC timestamp in ISO 8601 / RFC 3339 format ending in `Z` (for example, `2026-04-01T00:00:00Z`); numeric offsets such as `-04:00` or `+00:00` are not accepted. Must be on or after `2025-04-09T00:00:00Z`.

        end_time : dt.datetime
            Exclusive end of the reporting window. Must be a UTC timestamp in ISO 8601 / RFC 3339 format ending in `Z` (for example, `2026-04-08T00:00:00Z`); numeric offsets such as `-04:00` or `+00:00` are not accepted. Must be greater than `startTime` and within 100 days of it.

        metric_scope : TrafficReportsRequestMetricScope
            The unit each `count` data point is measured in.

        bucket_time_zone : str
            IANA time zone used to align daily bucket boundaries.

        device_type : typing.Optional[TrafficReportsRequestDeviceType]
            Restrict the report to a single device type.

        country : typing.Optional[str]
            Restrict the report to a single country. ISO 3166-1 alpha-2 (two letters, normalized to uppercase).

        page_path : typing.Optional[str]
            Restrict the report to a single page path.

        traffic_source : typing.Optional[str]
            Restrict the report to a single traffic source code (for example, `SO` for Organic Search).

        referrer : typing.Optional[str]
            Restrict the report to a single referrer domain.

        browser : typing.Optional[str]
            Restrict the report to a single browser.

        utm_campaign : typing.Optional[str]
            Restrict the report to a single `utm_campaign` value.

        utm_medium : typing.Optional[str]
            Restrict the report to a single `utm_medium` value.

        utm_source : typing.Optional[str]
            Restrict the report to a single `utm_source` value.

        filter : typing.Optional[TrafficReportsRequestFilter]
            Filter the report by dimension. Use bracket notation. Scalars take a single value (`filter[country][eq]=US`, `filter[country][ne]=US`). Arrays use indexed brackets (`filter[country][in][0]=US&filter[country][in][1]=CA`, `filter[country][nin][0]=US&filter[country][nin][1]=CA`).
            Each dimension entry takes at least one of `eq`, `in`, `ne`, or `nin`. Filter a given dimension in one place — either a top-level query parameter or a `filter` entry. See the `TrafficFilter` schema for the full list of supported dimensions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TrafficReportsResponse]
            Time-series traffic report for the requested window and filters.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/analyze/reports/traffic",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "startTime": serialize_datetime(start_time),
                "endTime": serialize_datetime(end_time),
                "metricScope": metric_scope,
                "bucketTimeZone": bucket_time_zone,
                "deviceType": device_type,
                "country": country,
                "pagePath": page_path,
                "trafficSource": traffic_source,
                "referrer": referrer,
                "browser": browser,
                "utmCampaign": utm_campaign,
                "utmMedium": utm_medium,
                "utmSource": utm_source,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=TrafficReportsRequestFilter, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrafficReportsResponse,
                    parse_obj_as(
                        type_=TrafficReportsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def top_pages(
        self,
        site_id: str,
        *,
        start_time: dt.datetime,
        end_time: dt.datetime,
        sort_by: typing.Optional[TopPagesReportsRequestSortBy] = None,
        limit: typing.Optional[int] = None,
        timeseries: typing.Optional[TopPagesReportsRequestTimeseries] = None,
        device_type: typing.Optional[TopPagesReportsRequestDeviceType] = None,
        country: typing.Optional[str] = None,
        page_path: typing.Optional[str] = None,
        traffic_source: typing.Optional[str] = None,
        referrer: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        utm_campaign: typing.Optional[str] = None,
        utm_medium: typing.Optional[str] = None,
        utm_source: typing.Optional[str] = None,
        filter: typing.Optional[TopPagesReportsRequestFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TopPagesReportsResponse]:
        """
        Returns the most-visited pages over a time window, ranked by `sortBy` (sessions, users, or pageviews).

        Each row carries all three scope counts; `sortBy` only governs ordering. Filter the report with top-level query parameters (`country`, `deviceType`, `pagePath`, etc.) or via the `filter` parameter for multi-value and negation matching.

        Set `timeseries[bucketTimeZone]` to attach a daily pageview `timeseries` to each row. Bucket counts are always pageviews regardless of `sortBy` — row-level counts honor the requested sort; the timeseries does not.

        <Warning title="Analyze add-on required">This endpoint requires a workspace with the Analyze add-on.</Warning>

        <Note title="Concurrency limit: 1 request at a time">Each access token can have one Analyze request in flight at a time, across all Analyze endpoints. Additional concurrent requests return `429 Too Many Requests`; wait for your in-flight request to finish, or for the `Retry-After` interval, then retry.</Note>

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        start_time : dt.datetime
            Inclusive start of the reporting window. Must be a UTC timestamp in ISO 8601 / RFC 3339 format ending in `Z` (for example, `2026-04-01T00:00:00Z`); numeric offsets such as `-04:00` or `+00:00` are not accepted. Must be on or after `2025-04-09T00:00:00Z`.

        end_time : dt.datetime
            Exclusive end of the reporting window. Must be a UTC timestamp in ISO 8601 / RFC 3339 format ending in `Z` (for example, `2026-04-08T00:00:00Z`); numeric offsets such as `-04:00` or `+00:00` are not accepted. Must be greater than `startTime` and within 100 days of it.

        sort_by : typing.Optional[TopPagesReportsRequestSortBy]
            Metric used to rank rows in the response, descending. Defaults to `session`.

        limit : typing.Optional[int]
            Maximum number of rows to return. Defaults to `25`, up to a maximum of `250`.

        timeseries : typing.Optional[TopPagesReportsRequestTimeseries]
            Include a daily pageview `timeseries` for each row, bucketed in the supplied IANA time zone. Omit this parameter to return ranked rows without per-page timeseries data.

        device_type : typing.Optional[TopPagesReportsRequestDeviceType]
            Restrict the report to a single device type.

        country : typing.Optional[str]
            Restrict the report to a single country. ISO 3166-1 alpha-2 (two letters, normalized to uppercase).

        page_path : typing.Optional[str]
            Restrict the report to a single page path.

        traffic_source : typing.Optional[str]
            Restrict the report to a single traffic source code (for example, `SO` for Organic Search).

        referrer : typing.Optional[str]
            Restrict the report to a single referrer domain.

        browser : typing.Optional[str]
            Restrict the report to a single browser.

        utm_campaign : typing.Optional[str]
            Restrict the report to a single `utm_campaign` value.

        utm_medium : typing.Optional[str]
            Restrict the report to a single `utm_medium` value.

        utm_source : typing.Optional[str]
            Restrict the report to a single `utm_source` value.

        filter : typing.Optional[TopPagesReportsRequestFilter]
            Filter the report by dimension. Use bracket notation. Scalars take a single value (`filter[country][eq]=US`, `filter[country][ne]=US`). Arrays use indexed brackets (`filter[country][in][0]=US&filter[country][in][1]=CA`, `filter[country][nin][0]=US&filter[country][nin][1]=CA`).
            Each dimension entry takes at least one of `eq`, `in`, `ne`, or `nin`. Filter a given dimension in one place — either a top-level query parameter or a `filter` entry. See the `TopPagesFilter` schema for the full list of supported dimensions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TopPagesReportsResponse]
            Pages ranked by `sortBy` for the requested window and filters.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/analyze/reports/top_pages",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "startTime": serialize_datetime(start_time),
                "endTime": serialize_datetime(end_time),
                "sortBy": sort_by,
                "limit": limit,
                "timeseries": convert_and_respect_annotation_metadata(
                    object_=timeseries, annotation=TopPagesReportsRequestTimeseries, direction="write"
                ),
                "deviceType": device_type,
                "country": country,
                "pagePath": page_path,
                "trafficSource": traffic_source,
                "referrer": referrer,
                "browser": browser,
                "utmCampaign": utm_campaign,
                "utmMedium": utm_medium,
                "utmSource": utm_source,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=TopPagesReportsRequestFilter, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TopPagesReportsResponse,
                    parse_obj_as(
                        type_=TopPagesReportsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def top_dimensions(
        self,
        site_id: str,
        *,
        start_time: dt.datetime,
        end_time: dt.datetime,
        dimension: TopDimensionsReportsRequestDimension,
        metric_scope: TopDimensionsReportsRequestMetricScope,
        limit: typing.Optional[int] = None,
        device_type: typing.Optional[TopDimensionsReportsRequestDeviceType] = None,
        country: typing.Optional[str] = None,
        page_path: typing.Optional[str] = None,
        traffic_source: typing.Optional[str] = None,
        referrer: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        utm_campaign: typing.Optional[str] = None,
        utm_medium: typing.Optional[str] = None,
        utm_source: typing.Optional[str] = None,
        filter: typing.Optional[TopDimensionsReportsRequestFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TopDimensionsReportsResponse]:
        """
        Returns the top values within a chosen `dimension` — top countries, top traffic sources, top campaigns, top audiences, and so on — over a time window, ranked by sessions or users.

        Filter the report with top-level query parameters (`country`, `deviceType`, `pagePath`, etc.) or via the `filter` parameter for multi-value and negation matching.

        <Warning title="Analyze add-on required">This endpoint requires a workspace with the Analyze add-on.</Warning>

        <Note title="Concurrency limit: 1 request at a time">Each access token can have one Analyze request in flight at a time, across all Analyze endpoints. Additional concurrent requests return `429 Too Many Requests`; wait for your in-flight request to finish, or for the `Retry-After` interval, then retry.</Note>

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        start_time : dt.datetime
            Inclusive start of the reporting window. Must be a UTC timestamp in ISO 8601 / RFC 3339 format ending in `Z` (for example, `2026-04-01T00:00:00Z`); numeric offsets such as `-04:00` or `+00:00` are not accepted. Must be on or after `2025-04-09T00:00:00Z`.

        end_time : dt.datetime
            Exclusive end of the reporting window. Must be a UTC timestamp in ISO 8601 / RFC 3339 format ending in `Z` (for example, `2026-04-08T00:00:00Z`); numeric offsets such as `-04:00` or `+00:00` are not accepted. Must be greater than `startTime` and within 100 days of it.

        dimension : TopDimensionsReportsRequestDimension
            The dimension whose top values are ranked. See `TopDimensionsDimension` for the supported values.

        metric_scope : TopDimensionsReportsRequestMetricScope
            The unit each row's `count` is measured in — sessions or users.

        limit : typing.Optional[int]
            Maximum number of rows to return. Defaults to `25`, up to a maximum of `100`.

        device_type : typing.Optional[TopDimensionsReportsRequestDeviceType]
            Restrict the report to a single device type.

        country : typing.Optional[str]
            Restrict the report to a single country. ISO 3166-1 alpha-2 (two letters, normalized to uppercase).

        page_path : typing.Optional[str]
            Restrict the report to a single page path.

        traffic_source : typing.Optional[str]
            Restrict the report to a single traffic source code (for example, `SO` for Organic Search).

        referrer : typing.Optional[str]
            Restrict the report to a single referrer domain.

        browser : typing.Optional[str]
            Restrict the report to a single browser.

        utm_campaign : typing.Optional[str]
            Restrict the report to a single `utm_campaign` value.

        utm_medium : typing.Optional[str]
            Restrict the report to a single `utm_medium` value.

        utm_source : typing.Optional[str]
            Restrict the report to a single `utm_source` value.

        filter : typing.Optional[TopDimensionsReportsRequestFilter]
            Filter the report by dimension. Use bracket notation. Scalars take a single value (`filter[country][eq]=US`, `filter[country][ne]=US`). Arrays use indexed brackets (`filter[country][in][0]=US&filter[country][in][1]=CA`, `filter[country][nin][0]=US&filter[country][nin][1]=CA`).
            Each dimension entry takes at least one of `eq`, `in`, `ne`, or `nin`. Filter a given dimension in one place — either a top-level query parameter or a `filter` entry. See the `TopDimensionsFilter` schema for the full list of supported dimensions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TopDimensionsReportsResponse]
            Dimension values ranked by `count` for the requested window and filters.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/analyze/reports/top_dimensions",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "startTime": serialize_datetime(start_time),
                "endTime": serialize_datetime(end_time),
                "dimension": dimension,
                "metricScope": metric_scope,
                "limit": limit,
                "deviceType": device_type,
                "country": country,
                "pagePath": page_path,
                "trafficSource": traffic_source,
                "referrer": referrer,
                "browser": browser,
                "utmCampaign": utm_campaign,
                "utmMedium": utm_medium,
                "utmSource": utm_source,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=TopDimensionsReportsRequestFilter, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TopDimensionsReportsResponse,
                    parse_obj_as(
                        type_=TopDimensionsReportsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def top_events(
        self,
        site_id: str,
        *,
        start_time: dt.datetime,
        end_time: dt.datetime,
        limit: typing.Optional[int] = None,
        timeseries: typing.Optional[TopEventsReportsRequestTimeseries] = None,
        device_type: typing.Optional[TopEventsReportsRequestDeviceType] = None,
        country: typing.Optional[str] = None,
        page_path: typing.Optional[str] = None,
        traffic_source: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        utm_campaign: typing.Optional[str] = None,
        utm_medium: typing.Optional[str] = None,
        utm_source: typing.Optional[str] = None,
        filter: typing.Optional[TopEventsReportsRequestFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TopEventsReportsResponse]:
        """
        Returns the top events over a time window, ranked by how often they occurred.

        Events are counted individually, not rolled up into sessions, users, or pageviews — so this report has no `metricScope`. Each row's `count` is how many times the event occurred. Filter the report with top-level query parameters (`country`, `deviceType`, `pagePath`, etc.) or via the `filter` parameter for multi-value and negation matching.

        Set `timeseries[bucketTimeZone]` to attach a daily event count `timeseries` to each row.

        <Warning title="Analyze add-on required">This endpoint requires a workspace with the Analyze add-on.</Warning>

        <Note title="Concurrency limit: 1 request at a time">Each access token can have one Analyze request in flight at a time, across all Analyze endpoints. Additional concurrent requests return `429 Too Many Requests`; wait for your in-flight request to finish, or for the `Retry-After` interval, then retry.</Note>

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        start_time : dt.datetime
            Inclusive start of the reporting window. Must be a UTC timestamp in ISO 8601 / RFC 3339 format ending in `Z` (for example, `2026-04-01T00:00:00Z`); numeric offsets such as `-04:00` or `+00:00` are not accepted. Must be on or after `2025-04-09T00:00:00Z`.

        end_time : dt.datetime
            Exclusive end of the reporting window. Must be a UTC timestamp in ISO 8601 / RFC 3339 format ending in `Z` (for example, `2026-04-08T00:00:00Z`); numeric offsets such as `-04:00` or `+00:00` are not accepted. Must be greater than `startTime` and within 100 days of it.

        limit : typing.Optional[int]
            Maximum number of rows to return. Defaults to `25`, up to a maximum of `250`.

        timeseries : typing.Optional[TopEventsReportsRequestTimeseries]
            Include a daily event count `timeseries` for each row, bucketed in the supplied IANA time zone. Omit this parameter to return ranked rows without per-event timeseries data.

        device_type : typing.Optional[TopEventsReportsRequestDeviceType]
            Restrict the report to a single device type.

        country : typing.Optional[str]
            Restrict the report to a single country. ISO 3166-1 alpha-2 (two letters, normalized to uppercase).

        page_path : typing.Optional[str]
            Restrict the report to a single page path.

        traffic_source : typing.Optional[str]
            Restrict the report to a single traffic source code (for example, `SO` for Organic Search).

        browser : typing.Optional[str]
            Restrict the report to a single browser.

        utm_campaign : typing.Optional[str]
            Restrict the report to a single `utm_campaign` value.

        utm_medium : typing.Optional[str]
            Restrict the report to a single `utm_medium` value.

        utm_source : typing.Optional[str]
            Restrict the report to a single `utm_source` value.

        filter : typing.Optional[TopEventsReportsRequestFilter]
            Filter the report by dimension. Use bracket notation. Scalars take a single value (`filter[country][eq]=US`, `filter[country][ne]=US`). Arrays use indexed brackets (`filter[country][in][0]=US&filter[country][in][1]=CA`, `filter[country][nin][0]=US&filter[country][nin][1]=CA`).
            Each dimension entry takes at least one of `eq`, `in`, `ne`, or `nin`. Filter a given dimension in one place — either a top-level query parameter or a `filter` entry. See the `TopEventsFilter` schema for the full list of supported dimensions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TopEventsReportsResponse]
            Events ranked by how frequently they occurred, for the requested window and filters.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/analyze/reports/top_events",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "startTime": serialize_datetime(start_time),
                "endTime": serialize_datetime(end_time),
                "limit": limit,
                "timeseries": convert_and_respect_annotation_metadata(
                    object_=timeseries, annotation=TopEventsReportsRequestTimeseries, direction="write"
                ),
                "deviceType": device_type,
                "country": country,
                "pagePath": page_path,
                "trafficSource": traffic_source,
                "browser": browser,
                "utmCampaign": utm_campaign,
                "utmMedium": utm_medium,
                "utmSource": utm_source,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=TopEventsReportsRequestFilter, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TopEventsReportsResponse,
                    parse_obj_as(
                        type_=TopEventsReportsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def time_on_page(
        self,
        site_id: str,
        *,
        start_time: dt.datetime,
        end_time: dt.datetime,
        metric_scope: TimeOnPageReportsRequestMetricScope,
        timeseries: typing.Optional[TimeOnPageReportsRequestTimeseries] = None,
        device_type: typing.Optional[TimeOnPageReportsRequestDeviceType] = None,
        country: typing.Optional[str] = None,
        page_path: typing.Optional[str] = None,
        traffic_source: typing.Optional[str] = None,
        referrer: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        utm_campaign: typing.Optional[str] = None,
        utm_medium: typing.Optional[str] = None,
        utm_source: typing.Optional[str] = None,
        filter: typing.Optional[TimeOnPageReportsRequestFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TimeOnPageReportsResponse]:
        """
        Returns the average time on page over a time window — as a single aggregate value, or bucketed by day or week when `timeseries` is supplied.

        Choose how the average is computed with `metricScope` (per session, user, or pageview). Filter the report with top-level query parameters (`country`, `deviceType`, `pagePath`, etc.) or via the `filter` parameter for multi-value and negation matching.

        <Warning title="Analyze add-on required">This endpoint requires a workspace with the Analyze add-on.</Warning>

        <Note title="Concurrency limit: 1 request at a time">Each access token can have one Analyze request in flight at a time, across all Analyze endpoints. Additional concurrent requests return `429 Too Many Requests`; wait for your in-flight request to finish, or for the `Retry-After` interval, then retry.</Note>

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        start_time : dt.datetime
            Inclusive start of the reporting window. Must be a UTC timestamp in ISO 8601 / RFC 3339 format ending in `Z` (for example, `2026-04-01T00:00:00Z`); numeric offsets such as `-04:00` or `+00:00` are not accepted. Must be on or after `2025-04-09T00:00:00Z`.

        end_time : dt.datetime
            Exclusive end of the reporting window. Must be a UTC timestamp in ISO 8601 / RFC 3339 format ending in `Z` (for example, `2026-04-08T00:00:00Z`); numeric offsets such as `-04:00` or `+00:00` are not accepted. Must be greater than `startTime` and within 100 days of it.

        metric_scope : TimeOnPageReportsRequestMetricScope
            How the average time on page is computed — per session, user, or pageview.

        timeseries : typing.Optional[TimeOnPageReportsRequestTimeseries]
            Include bucketed average time data using the supplied granularity and IANA time zone. Omit this parameter to return a single aggregate value for the requested window.

        device_type : typing.Optional[TimeOnPageReportsRequestDeviceType]
            Restrict the report to a single device type.

        country : typing.Optional[str]
            Restrict the report to a single country. ISO 3166-1 alpha-2 (two letters, normalized to uppercase).

        page_path : typing.Optional[str]
            Restrict the report to a single page path.

        traffic_source : typing.Optional[str]
            Restrict the report to a single traffic source code (for example, `SO` for Organic Search).

        referrer : typing.Optional[str]
            Restrict the report to a single referrer domain.

        browser : typing.Optional[str]
            Restrict the report to a single browser.

        utm_campaign : typing.Optional[str]
            Restrict the report to a single `utm_campaign` value.

        utm_medium : typing.Optional[str]
            Restrict the report to a single `utm_medium` value.

        utm_source : typing.Optional[str]
            Restrict the report to a single `utm_source` value.

        filter : typing.Optional[TimeOnPageReportsRequestFilter]
            Filter the report by dimension. Use bracket notation. Scalars take a single value (`filter[country][eq]=US`, `filter[country][ne]=US`). Arrays use indexed brackets (`filter[country][in][0]=US&filter[country][in][1]=CA`, `filter[country][nin][0]=US&filter[country][nin][1]=CA`).
            Each dimension entry takes at least one of `eq`, `in`, `ne`, or `nin`. Filter a given dimension in one place — either a top-level query parameter or a `filter` entry. See the `TimeOnPageFilter` schema for the full list of supported dimensions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TimeOnPageReportsResponse]
            Average time on page for the requested window and filters.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/analyze/reports/time_on_page",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "startTime": serialize_datetime(start_time),
                "endTime": serialize_datetime(end_time),
                "metricScope": metric_scope,
                "timeseries": convert_and_respect_annotation_metadata(
                    object_=timeseries, annotation=TimeOnPageReportsRequestTimeseries, direction="write"
                ),
                "deviceType": device_type,
                "country": country,
                "pagePath": page_path,
                "trafficSource": traffic_source,
                "referrer": referrer,
                "browser": browser,
                "utmCampaign": utm_campaign,
                "utmMedium": utm_medium,
                "utmSource": utm_source,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=TimeOnPageReportsRequestFilter, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TimeOnPageReportsResponse,
                    parse_obj_as(
                        type_=TimeOnPageReportsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawReportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def traffic(
        self,
        site_id: str,
        *,
        start_time: dt.datetime,
        end_time: dt.datetime,
        metric_scope: TrafficReportsRequestMetricScope,
        bucket_time_zone: str,
        device_type: typing.Optional[TrafficReportsRequestDeviceType] = None,
        country: typing.Optional[str] = None,
        page_path: typing.Optional[str] = None,
        traffic_source: typing.Optional[str] = None,
        referrer: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        utm_campaign: typing.Optional[str] = None,
        utm_medium: typing.Optional[str] = None,
        utm_source: typing.Optional[str] = None,
        filter: typing.Optional[TrafficReportsRequestFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TrafficReportsResponse]:
        """
        Returns a daily time series of a single metric — sessions, users, or pageviews — over a time window.

        Filter the report with top-level query parameters (`country`, `deviceType`, `pagePath`, etc.) or via the `filter` parameter for multi-value and negation matching.

        <Warning title="Analyze add-on required">This endpoint requires a workspace with the Analyze add-on.</Warning>

        <Note title="Concurrency limit: 1 request at a time">Each access token can have one Analyze request in flight at a time, across all Analyze endpoints. Additional concurrent requests return `429 Too Many Requests`; wait for your in-flight request to finish, or for the `Retry-After` interval, then retry.</Note>

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        start_time : dt.datetime
            Inclusive start of the reporting window. Must be a UTC timestamp in ISO 8601 / RFC 3339 format ending in `Z` (for example, `2026-04-01T00:00:00Z`); numeric offsets such as `-04:00` or `+00:00` are not accepted. Must be on or after `2025-04-09T00:00:00Z`.

        end_time : dt.datetime
            Exclusive end of the reporting window. Must be a UTC timestamp in ISO 8601 / RFC 3339 format ending in `Z` (for example, `2026-04-08T00:00:00Z`); numeric offsets such as `-04:00` or `+00:00` are not accepted. Must be greater than `startTime` and within 100 days of it.

        metric_scope : TrafficReportsRequestMetricScope
            The unit each `count` data point is measured in.

        bucket_time_zone : str
            IANA time zone used to align daily bucket boundaries.

        device_type : typing.Optional[TrafficReportsRequestDeviceType]
            Restrict the report to a single device type.

        country : typing.Optional[str]
            Restrict the report to a single country. ISO 3166-1 alpha-2 (two letters, normalized to uppercase).

        page_path : typing.Optional[str]
            Restrict the report to a single page path.

        traffic_source : typing.Optional[str]
            Restrict the report to a single traffic source code (for example, `SO` for Organic Search).

        referrer : typing.Optional[str]
            Restrict the report to a single referrer domain.

        browser : typing.Optional[str]
            Restrict the report to a single browser.

        utm_campaign : typing.Optional[str]
            Restrict the report to a single `utm_campaign` value.

        utm_medium : typing.Optional[str]
            Restrict the report to a single `utm_medium` value.

        utm_source : typing.Optional[str]
            Restrict the report to a single `utm_source` value.

        filter : typing.Optional[TrafficReportsRequestFilter]
            Filter the report by dimension. Use bracket notation. Scalars take a single value (`filter[country][eq]=US`, `filter[country][ne]=US`). Arrays use indexed brackets (`filter[country][in][0]=US&filter[country][in][1]=CA`, `filter[country][nin][0]=US&filter[country][nin][1]=CA`).
            Each dimension entry takes at least one of `eq`, `in`, `ne`, or `nin`. Filter a given dimension in one place — either a top-level query parameter or a `filter` entry. See the `TrafficFilter` schema for the full list of supported dimensions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TrafficReportsResponse]
            Time-series traffic report for the requested window and filters.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/analyze/reports/traffic",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "startTime": serialize_datetime(start_time),
                "endTime": serialize_datetime(end_time),
                "metricScope": metric_scope,
                "bucketTimeZone": bucket_time_zone,
                "deviceType": device_type,
                "country": country,
                "pagePath": page_path,
                "trafficSource": traffic_source,
                "referrer": referrer,
                "browser": browser,
                "utmCampaign": utm_campaign,
                "utmMedium": utm_medium,
                "utmSource": utm_source,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=TrafficReportsRequestFilter, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrafficReportsResponse,
                    parse_obj_as(
                        type_=TrafficReportsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def top_pages(
        self,
        site_id: str,
        *,
        start_time: dt.datetime,
        end_time: dt.datetime,
        sort_by: typing.Optional[TopPagesReportsRequestSortBy] = None,
        limit: typing.Optional[int] = None,
        timeseries: typing.Optional[TopPagesReportsRequestTimeseries] = None,
        device_type: typing.Optional[TopPagesReportsRequestDeviceType] = None,
        country: typing.Optional[str] = None,
        page_path: typing.Optional[str] = None,
        traffic_source: typing.Optional[str] = None,
        referrer: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        utm_campaign: typing.Optional[str] = None,
        utm_medium: typing.Optional[str] = None,
        utm_source: typing.Optional[str] = None,
        filter: typing.Optional[TopPagesReportsRequestFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TopPagesReportsResponse]:
        """
        Returns the most-visited pages over a time window, ranked by `sortBy` (sessions, users, or pageviews).

        Each row carries all three scope counts; `sortBy` only governs ordering. Filter the report with top-level query parameters (`country`, `deviceType`, `pagePath`, etc.) or via the `filter` parameter for multi-value and negation matching.

        Set `timeseries[bucketTimeZone]` to attach a daily pageview `timeseries` to each row. Bucket counts are always pageviews regardless of `sortBy` — row-level counts honor the requested sort; the timeseries does not.

        <Warning title="Analyze add-on required">This endpoint requires a workspace with the Analyze add-on.</Warning>

        <Note title="Concurrency limit: 1 request at a time">Each access token can have one Analyze request in flight at a time, across all Analyze endpoints. Additional concurrent requests return `429 Too Many Requests`; wait for your in-flight request to finish, or for the `Retry-After` interval, then retry.</Note>

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        start_time : dt.datetime
            Inclusive start of the reporting window. Must be a UTC timestamp in ISO 8601 / RFC 3339 format ending in `Z` (for example, `2026-04-01T00:00:00Z`); numeric offsets such as `-04:00` or `+00:00` are not accepted. Must be on or after `2025-04-09T00:00:00Z`.

        end_time : dt.datetime
            Exclusive end of the reporting window. Must be a UTC timestamp in ISO 8601 / RFC 3339 format ending in `Z` (for example, `2026-04-08T00:00:00Z`); numeric offsets such as `-04:00` or `+00:00` are not accepted. Must be greater than `startTime` and within 100 days of it.

        sort_by : typing.Optional[TopPagesReportsRequestSortBy]
            Metric used to rank rows in the response, descending. Defaults to `session`.

        limit : typing.Optional[int]
            Maximum number of rows to return. Defaults to `25`, up to a maximum of `250`.

        timeseries : typing.Optional[TopPagesReportsRequestTimeseries]
            Include a daily pageview `timeseries` for each row, bucketed in the supplied IANA time zone. Omit this parameter to return ranked rows without per-page timeseries data.

        device_type : typing.Optional[TopPagesReportsRequestDeviceType]
            Restrict the report to a single device type.

        country : typing.Optional[str]
            Restrict the report to a single country. ISO 3166-1 alpha-2 (two letters, normalized to uppercase).

        page_path : typing.Optional[str]
            Restrict the report to a single page path.

        traffic_source : typing.Optional[str]
            Restrict the report to a single traffic source code (for example, `SO` for Organic Search).

        referrer : typing.Optional[str]
            Restrict the report to a single referrer domain.

        browser : typing.Optional[str]
            Restrict the report to a single browser.

        utm_campaign : typing.Optional[str]
            Restrict the report to a single `utm_campaign` value.

        utm_medium : typing.Optional[str]
            Restrict the report to a single `utm_medium` value.

        utm_source : typing.Optional[str]
            Restrict the report to a single `utm_source` value.

        filter : typing.Optional[TopPagesReportsRequestFilter]
            Filter the report by dimension. Use bracket notation. Scalars take a single value (`filter[country][eq]=US`, `filter[country][ne]=US`). Arrays use indexed brackets (`filter[country][in][0]=US&filter[country][in][1]=CA`, `filter[country][nin][0]=US&filter[country][nin][1]=CA`).
            Each dimension entry takes at least one of `eq`, `in`, `ne`, or `nin`. Filter a given dimension in one place — either a top-level query parameter or a `filter` entry. See the `TopPagesFilter` schema for the full list of supported dimensions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TopPagesReportsResponse]
            Pages ranked by `sortBy` for the requested window and filters.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/analyze/reports/top_pages",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "startTime": serialize_datetime(start_time),
                "endTime": serialize_datetime(end_time),
                "sortBy": sort_by,
                "limit": limit,
                "timeseries": convert_and_respect_annotation_metadata(
                    object_=timeseries, annotation=TopPagesReportsRequestTimeseries, direction="write"
                ),
                "deviceType": device_type,
                "country": country,
                "pagePath": page_path,
                "trafficSource": traffic_source,
                "referrer": referrer,
                "browser": browser,
                "utmCampaign": utm_campaign,
                "utmMedium": utm_medium,
                "utmSource": utm_source,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=TopPagesReportsRequestFilter, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TopPagesReportsResponse,
                    parse_obj_as(
                        type_=TopPagesReportsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def top_dimensions(
        self,
        site_id: str,
        *,
        start_time: dt.datetime,
        end_time: dt.datetime,
        dimension: TopDimensionsReportsRequestDimension,
        metric_scope: TopDimensionsReportsRequestMetricScope,
        limit: typing.Optional[int] = None,
        device_type: typing.Optional[TopDimensionsReportsRequestDeviceType] = None,
        country: typing.Optional[str] = None,
        page_path: typing.Optional[str] = None,
        traffic_source: typing.Optional[str] = None,
        referrer: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        utm_campaign: typing.Optional[str] = None,
        utm_medium: typing.Optional[str] = None,
        utm_source: typing.Optional[str] = None,
        filter: typing.Optional[TopDimensionsReportsRequestFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TopDimensionsReportsResponse]:
        """
        Returns the top values within a chosen `dimension` — top countries, top traffic sources, top campaigns, top audiences, and so on — over a time window, ranked by sessions or users.

        Filter the report with top-level query parameters (`country`, `deviceType`, `pagePath`, etc.) or via the `filter` parameter for multi-value and negation matching.

        <Warning title="Analyze add-on required">This endpoint requires a workspace with the Analyze add-on.</Warning>

        <Note title="Concurrency limit: 1 request at a time">Each access token can have one Analyze request in flight at a time, across all Analyze endpoints. Additional concurrent requests return `429 Too Many Requests`; wait for your in-flight request to finish, or for the `Retry-After` interval, then retry.</Note>

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        start_time : dt.datetime
            Inclusive start of the reporting window. Must be a UTC timestamp in ISO 8601 / RFC 3339 format ending in `Z` (for example, `2026-04-01T00:00:00Z`); numeric offsets such as `-04:00` or `+00:00` are not accepted. Must be on or after `2025-04-09T00:00:00Z`.

        end_time : dt.datetime
            Exclusive end of the reporting window. Must be a UTC timestamp in ISO 8601 / RFC 3339 format ending in `Z` (for example, `2026-04-08T00:00:00Z`); numeric offsets such as `-04:00` or `+00:00` are not accepted. Must be greater than `startTime` and within 100 days of it.

        dimension : TopDimensionsReportsRequestDimension
            The dimension whose top values are ranked. See `TopDimensionsDimension` for the supported values.

        metric_scope : TopDimensionsReportsRequestMetricScope
            The unit each row's `count` is measured in — sessions or users.

        limit : typing.Optional[int]
            Maximum number of rows to return. Defaults to `25`, up to a maximum of `100`.

        device_type : typing.Optional[TopDimensionsReportsRequestDeviceType]
            Restrict the report to a single device type.

        country : typing.Optional[str]
            Restrict the report to a single country. ISO 3166-1 alpha-2 (two letters, normalized to uppercase).

        page_path : typing.Optional[str]
            Restrict the report to a single page path.

        traffic_source : typing.Optional[str]
            Restrict the report to a single traffic source code (for example, `SO` for Organic Search).

        referrer : typing.Optional[str]
            Restrict the report to a single referrer domain.

        browser : typing.Optional[str]
            Restrict the report to a single browser.

        utm_campaign : typing.Optional[str]
            Restrict the report to a single `utm_campaign` value.

        utm_medium : typing.Optional[str]
            Restrict the report to a single `utm_medium` value.

        utm_source : typing.Optional[str]
            Restrict the report to a single `utm_source` value.

        filter : typing.Optional[TopDimensionsReportsRequestFilter]
            Filter the report by dimension. Use bracket notation. Scalars take a single value (`filter[country][eq]=US`, `filter[country][ne]=US`). Arrays use indexed brackets (`filter[country][in][0]=US&filter[country][in][1]=CA`, `filter[country][nin][0]=US&filter[country][nin][1]=CA`).
            Each dimension entry takes at least one of `eq`, `in`, `ne`, or `nin`. Filter a given dimension in one place — either a top-level query parameter or a `filter` entry. See the `TopDimensionsFilter` schema for the full list of supported dimensions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TopDimensionsReportsResponse]
            Dimension values ranked by `count` for the requested window and filters.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/analyze/reports/top_dimensions",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "startTime": serialize_datetime(start_time),
                "endTime": serialize_datetime(end_time),
                "dimension": dimension,
                "metricScope": metric_scope,
                "limit": limit,
                "deviceType": device_type,
                "country": country,
                "pagePath": page_path,
                "trafficSource": traffic_source,
                "referrer": referrer,
                "browser": browser,
                "utmCampaign": utm_campaign,
                "utmMedium": utm_medium,
                "utmSource": utm_source,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=TopDimensionsReportsRequestFilter, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TopDimensionsReportsResponse,
                    parse_obj_as(
                        type_=TopDimensionsReportsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def top_events(
        self,
        site_id: str,
        *,
        start_time: dt.datetime,
        end_time: dt.datetime,
        limit: typing.Optional[int] = None,
        timeseries: typing.Optional[TopEventsReportsRequestTimeseries] = None,
        device_type: typing.Optional[TopEventsReportsRequestDeviceType] = None,
        country: typing.Optional[str] = None,
        page_path: typing.Optional[str] = None,
        traffic_source: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        utm_campaign: typing.Optional[str] = None,
        utm_medium: typing.Optional[str] = None,
        utm_source: typing.Optional[str] = None,
        filter: typing.Optional[TopEventsReportsRequestFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TopEventsReportsResponse]:
        """
        Returns the top events over a time window, ranked by how often they occurred.

        Events are counted individually, not rolled up into sessions, users, or pageviews — so this report has no `metricScope`. Each row's `count` is how many times the event occurred. Filter the report with top-level query parameters (`country`, `deviceType`, `pagePath`, etc.) or via the `filter` parameter for multi-value and negation matching.

        Set `timeseries[bucketTimeZone]` to attach a daily event count `timeseries` to each row.

        <Warning title="Analyze add-on required">This endpoint requires a workspace with the Analyze add-on.</Warning>

        <Note title="Concurrency limit: 1 request at a time">Each access token can have one Analyze request in flight at a time, across all Analyze endpoints. Additional concurrent requests return `429 Too Many Requests`; wait for your in-flight request to finish, or for the `Retry-After` interval, then retry.</Note>

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        start_time : dt.datetime
            Inclusive start of the reporting window. Must be a UTC timestamp in ISO 8601 / RFC 3339 format ending in `Z` (for example, `2026-04-01T00:00:00Z`); numeric offsets such as `-04:00` or `+00:00` are not accepted. Must be on or after `2025-04-09T00:00:00Z`.

        end_time : dt.datetime
            Exclusive end of the reporting window. Must be a UTC timestamp in ISO 8601 / RFC 3339 format ending in `Z` (for example, `2026-04-08T00:00:00Z`); numeric offsets such as `-04:00` or `+00:00` are not accepted. Must be greater than `startTime` and within 100 days of it.

        limit : typing.Optional[int]
            Maximum number of rows to return. Defaults to `25`, up to a maximum of `250`.

        timeseries : typing.Optional[TopEventsReportsRequestTimeseries]
            Include a daily event count `timeseries` for each row, bucketed in the supplied IANA time zone. Omit this parameter to return ranked rows without per-event timeseries data.

        device_type : typing.Optional[TopEventsReportsRequestDeviceType]
            Restrict the report to a single device type.

        country : typing.Optional[str]
            Restrict the report to a single country. ISO 3166-1 alpha-2 (two letters, normalized to uppercase).

        page_path : typing.Optional[str]
            Restrict the report to a single page path.

        traffic_source : typing.Optional[str]
            Restrict the report to a single traffic source code (for example, `SO` for Organic Search).

        browser : typing.Optional[str]
            Restrict the report to a single browser.

        utm_campaign : typing.Optional[str]
            Restrict the report to a single `utm_campaign` value.

        utm_medium : typing.Optional[str]
            Restrict the report to a single `utm_medium` value.

        utm_source : typing.Optional[str]
            Restrict the report to a single `utm_source` value.

        filter : typing.Optional[TopEventsReportsRequestFilter]
            Filter the report by dimension. Use bracket notation. Scalars take a single value (`filter[country][eq]=US`, `filter[country][ne]=US`). Arrays use indexed brackets (`filter[country][in][0]=US&filter[country][in][1]=CA`, `filter[country][nin][0]=US&filter[country][nin][1]=CA`).
            Each dimension entry takes at least one of `eq`, `in`, `ne`, or `nin`. Filter a given dimension in one place — either a top-level query parameter or a `filter` entry. See the `TopEventsFilter` schema for the full list of supported dimensions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TopEventsReportsResponse]
            Events ranked by how frequently they occurred, for the requested window and filters.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/analyze/reports/top_events",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "startTime": serialize_datetime(start_time),
                "endTime": serialize_datetime(end_time),
                "limit": limit,
                "timeseries": convert_and_respect_annotation_metadata(
                    object_=timeseries, annotation=TopEventsReportsRequestTimeseries, direction="write"
                ),
                "deviceType": device_type,
                "country": country,
                "pagePath": page_path,
                "trafficSource": traffic_source,
                "browser": browser,
                "utmCampaign": utm_campaign,
                "utmMedium": utm_medium,
                "utmSource": utm_source,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=TopEventsReportsRequestFilter, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TopEventsReportsResponse,
                    parse_obj_as(
                        type_=TopEventsReportsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def time_on_page(
        self,
        site_id: str,
        *,
        start_time: dt.datetime,
        end_time: dt.datetime,
        metric_scope: TimeOnPageReportsRequestMetricScope,
        timeseries: typing.Optional[TimeOnPageReportsRequestTimeseries] = None,
        device_type: typing.Optional[TimeOnPageReportsRequestDeviceType] = None,
        country: typing.Optional[str] = None,
        page_path: typing.Optional[str] = None,
        traffic_source: typing.Optional[str] = None,
        referrer: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        utm_campaign: typing.Optional[str] = None,
        utm_medium: typing.Optional[str] = None,
        utm_source: typing.Optional[str] = None,
        filter: typing.Optional[TimeOnPageReportsRequestFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TimeOnPageReportsResponse]:
        """
        Returns the average time on page over a time window — as a single aggregate value, or bucketed by day or week when `timeseries` is supplied.

        Choose how the average is computed with `metricScope` (per session, user, or pageview). Filter the report with top-level query parameters (`country`, `deviceType`, `pagePath`, etc.) or via the `filter` parameter for multi-value and negation matching.

        <Warning title="Analyze add-on required">This endpoint requires a workspace with the Analyze add-on.</Warning>

        <Note title="Concurrency limit: 1 request at a time">Each access token can have one Analyze request in flight at a time, across all Analyze endpoints. Additional concurrent requests return `429 Too Many Requests`; wait for your in-flight request to finish, or for the `Retry-After` interval, then retry.</Note>

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        start_time : dt.datetime
            Inclusive start of the reporting window. Must be a UTC timestamp in ISO 8601 / RFC 3339 format ending in `Z` (for example, `2026-04-01T00:00:00Z`); numeric offsets such as `-04:00` or `+00:00` are not accepted. Must be on or after `2025-04-09T00:00:00Z`.

        end_time : dt.datetime
            Exclusive end of the reporting window. Must be a UTC timestamp in ISO 8601 / RFC 3339 format ending in `Z` (for example, `2026-04-08T00:00:00Z`); numeric offsets such as `-04:00` or `+00:00` are not accepted. Must be greater than `startTime` and within 100 days of it.

        metric_scope : TimeOnPageReportsRequestMetricScope
            How the average time on page is computed — per session, user, or pageview.

        timeseries : typing.Optional[TimeOnPageReportsRequestTimeseries]
            Include bucketed average time data using the supplied granularity and IANA time zone. Omit this parameter to return a single aggregate value for the requested window.

        device_type : typing.Optional[TimeOnPageReportsRequestDeviceType]
            Restrict the report to a single device type.

        country : typing.Optional[str]
            Restrict the report to a single country. ISO 3166-1 alpha-2 (two letters, normalized to uppercase).

        page_path : typing.Optional[str]
            Restrict the report to a single page path.

        traffic_source : typing.Optional[str]
            Restrict the report to a single traffic source code (for example, `SO` for Organic Search).

        referrer : typing.Optional[str]
            Restrict the report to a single referrer domain.

        browser : typing.Optional[str]
            Restrict the report to a single browser.

        utm_campaign : typing.Optional[str]
            Restrict the report to a single `utm_campaign` value.

        utm_medium : typing.Optional[str]
            Restrict the report to a single `utm_medium` value.

        utm_source : typing.Optional[str]
            Restrict the report to a single `utm_source` value.

        filter : typing.Optional[TimeOnPageReportsRequestFilter]
            Filter the report by dimension. Use bracket notation. Scalars take a single value (`filter[country][eq]=US`, `filter[country][ne]=US`). Arrays use indexed brackets (`filter[country][in][0]=US&filter[country][in][1]=CA`, `filter[country][nin][0]=US&filter[country][nin][1]=CA`).
            Each dimension entry takes at least one of `eq`, `in`, `ne`, or `nin`. Filter a given dimension in one place — either a top-level query parameter or a `filter` entry. See the `TimeOnPageFilter` schema for the full list of supported dimensions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TimeOnPageReportsResponse]
            Average time on page for the requested window and filters.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/analyze/reports/time_on_page",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "startTime": serialize_datetime(start_time),
                "endTime": serialize_datetime(end_time),
                "metricScope": metric_scope,
                "timeseries": convert_and_respect_annotation_metadata(
                    object_=timeseries, annotation=TimeOnPageReportsRequestTimeseries, direction="write"
                ),
                "deviceType": device_type,
                "country": country,
                "pagePath": page_path,
                "trafficSource": traffic_source,
                "referrer": referrer,
                "browser": browser,
                "utmCampaign": utm_campaign,
                "utmMedium": utm_medium,
                "utmSource": utm_source,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=TimeOnPageReportsRequestFilter, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TimeOnPageReportsResponse,
                    parse_obj_as(
                        type_=TimeOnPageReportsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
