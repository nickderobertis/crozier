

import datetime as dt
import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.time_on_page_reports_request_filter import TimeOnPageReportsRequestFilter
from ...types.time_on_page_reports_request_timeseries import TimeOnPageReportsRequestTimeseries
from ...types.top_dimensions_reports_request_filter import TopDimensionsReportsRequestFilter
from ...types.top_events_reports_request_filter import TopEventsReportsRequestFilter
from ...types.top_events_reports_request_timeseries import TopEventsReportsRequestTimeseries
from ...types.top_pages_reports_request_filter import TopPagesReportsRequestFilter
from ...types.top_pages_reports_request_timeseries import TopPagesReportsRequestTimeseries
from ...types.traffic_reports_request_filter import TrafficReportsRequestFilter
from .raw_client import AsyncRawReportsClient, RawReportsClient
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


class ReportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReportsClient
        """
        return self._raw_client

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
    ) -> TrafficReportsResponse:
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
        TrafficReportsResponse
            Time-series traffic report for the requested window and filters.

        Examples
        --------
        import datetime

        from fern.analyze.reports import TrafficReportsRequestMetricScope

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analyze.reports.traffic(
            site_id="580e63e98c9a982ac9b8b741",
            start_time=datetime.datetime.fromisoformat(
                "2026-04-01 00:00:00+00:00",
            ),
            end_time=datetime.datetime.fromisoformat(
                "2026-04-08 00:00:00+00:00",
            ),
            metric_scope=TrafficReportsRequestMetricScope.SESSION,
            bucket_time_zone="America/New_York",
            country="US",
            page_path="/towels",
            traffic_source="SO",
            referrer="google.com",
            browser="Chrome",
            utm_campaign="dont-panic-2026",
            utm_medium="email",
            utm_source="hitchhikers-guide",
        )
        """
        _response = self._raw_client.traffic(
            site_id,
            start_time=start_time,
            end_time=end_time,
            metric_scope=metric_scope,
            bucket_time_zone=bucket_time_zone,
            device_type=device_type,
            country=country,
            page_path=page_path,
            traffic_source=traffic_source,
            referrer=referrer,
            browser=browser,
            utm_campaign=utm_campaign,
            utm_medium=utm_medium,
            utm_source=utm_source,
            filter=filter,
            request_options=request_options,
        )
        return _response.data

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
    ) -> TopPagesReportsResponse:
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
        TopPagesReportsResponse
            Pages ranked by `sortBy` for the requested window and filters.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analyze.reports.top_pages(
            site_id="580e63e98c9a982ac9b8b741",
            start_time=datetime.datetime.fromisoformat(
                "2026-04-01 00:00:00+00:00",
            ),
            end_time=datetime.datetime.fromisoformat(
                "2026-04-08 00:00:00+00:00",
            ),
            country="US",
            page_path="/towels",
            traffic_source="SO",
            referrer="google.com",
            browser="Chrome",
            utm_campaign="dont-panic-2026",
            utm_medium="email",
            utm_source="hitchhikers-guide",
        )
        """
        _response = self._raw_client.top_pages(
            site_id,
            start_time=start_time,
            end_time=end_time,
            sort_by=sort_by,
            limit=limit,
            timeseries=timeseries,
            device_type=device_type,
            country=country,
            page_path=page_path,
            traffic_source=traffic_source,
            referrer=referrer,
            browser=browser,
            utm_campaign=utm_campaign,
            utm_medium=utm_medium,
            utm_source=utm_source,
            filter=filter,
            request_options=request_options,
        )
        return _response.data

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
    ) -> TopDimensionsReportsResponse:
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
        TopDimensionsReportsResponse
            Dimension values ranked by `count` for the requested window and filters.

        Examples
        --------
        import datetime

        from fern.analyze.reports import (
            TopDimensionsReportsRequestDimension,
            TopDimensionsReportsRequestMetricScope,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analyze.reports.top_dimensions(
            site_id="580e63e98c9a982ac9b8b741",
            start_time=datetime.datetime.fromisoformat(
                "2026-04-01 00:00:00+00:00",
            ),
            end_time=datetime.datetime.fromisoformat(
                "2026-04-08 00:00:00+00:00",
            ),
            dimension=TopDimensionsReportsRequestDimension.COUNTRY,
            metric_scope=TopDimensionsReportsRequestMetricScope.SESSION,
            country="US",
            page_path="/towels",
            traffic_source="SO",
            referrer="google.com",
            browser="Chrome",
            utm_campaign="dont-panic-2026",
            utm_medium="email",
            utm_source="hitchhikers-guide",
        )
        """
        _response = self._raw_client.top_dimensions(
            site_id,
            start_time=start_time,
            end_time=end_time,
            dimension=dimension,
            metric_scope=metric_scope,
            limit=limit,
            device_type=device_type,
            country=country,
            page_path=page_path,
            traffic_source=traffic_source,
            referrer=referrer,
            browser=browser,
            utm_campaign=utm_campaign,
            utm_medium=utm_medium,
            utm_source=utm_source,
            filter=filter,
            request_options=request_options,
        )
        return _response.data

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
    ) -> TopEventsReportsResponse:
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
        TopEventsReportsResponse
            Events ranked by how frequently they occurred, for the requested window and filters.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analyze.reports.top_events(
            site_id="580e63e98c9a982ac9b8b741",
            start_time=datetime.datetime.fromisoformat(
                "2026-04-01 00:00:00+00:00",
            ),
            end_time=datetime.datetime.fromisoformat(
                "2026-04-08 00:00:00+00:00",
            ),
            country="US",
            page_path="/towels",
            traffic_source="SO",
            browser="Chrome",
            utm_campaign="dont-panic-2026",
            utm_medium="email",
            utm_source="hitchhikers-guide",
        )
        """
        _response = self._raw_client.top_events(
            site_id,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            timeseries=timeseries,
            device_type=device_type,
            country=country,
            page_path=page_path,
            traffic_source=traffic_source,
            browser=browser,
            utm_campaign=utm_campaign,
            utm_medium=utm_medium,
            utm_source=utm_source,
            filter=filter,
            request_options=request_options,
        )
        return _response.data

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
    ) -> TimeOnPageReportsResponse:
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
        TimeOnPageReportsResponse
            Average time on page for the requested window and filters.

        Examples
        --------
        import datetime

        from fern.analyze.reports import TimeOnPageReportsRequestMetricScope

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analyze.reports.time_on_page(
            site_id="580e63e98c9a982ac9b8b741",
            start_time=datetime.datetime.fromisoformat(
                "2026-04-01 00:00:00+00:00",
            ),
            end_time=datetime.datetime.fromisoformat(
                "2026-04-08 00:00:00+00:00",
            ),
            metric_scope=TimeOnPageReportsRequestMetricScope.SESSION,
            country="US",
            page_path="/towels",
            traffic_source="SO",
            referrer="google.com",
            browser="Chrome",
            utm_campaign="dont-panic-2026",
            utm_medium="email",
            utm_source="hitchhikers-guide",
        )
        """
        _response = self._raw_client.time_on_page(
            site_id,
            start_time=start_time,
            end_time=end_time,
            metric_scope=metric_scope,
            timeseries=timeseries,
            device_type=device_type,
            country=country,
            page_path=page_path,
            traffic_source=traffic_source,
            referrer=referrer,
            browser=browser,
            utm_campaign=utm_campaign,
            utm_medium=utm_medium,
            utm_source=utm_source,
            filter=filter,
            request_options=request_options,
        )
        return _response.data


class AsyncReportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReportsClient
        """
        return self._raw_client

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
    ) -> TrafficReportsResponse:
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
        TrafficReportsResponse
            Time-series traffic report for the requested window and filters.

        Examples
        --------
        import asyncio
        import datetime

        from fern.analyze.reports import TrafficReportsRequestMetricScope

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analyze.reports.traffic(
                site_id="580e63e98c9a982ac9b8b741",
                start_time=datetime.datetime.fromisoformat(
                    "2026-04-01 00:00:00+00:00",
                ),
                end_time=datetime.datetime.fromisoformat(
                    "2026-04-08 00:00:00+00:00",
                ),
                metric_scope=TrafficReportsRequestMetricScope.SESSION,
                bucket_time_zone="America/New_York",
                country="US",
                page_path="/towels",
                traffic_source="SO",
                referrer="google.com",
                browser="Chrome",
                utm_campaign="dont-panic-2026",
                utm_medium="email",
                utm_source="hitchhikers-guide",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.traffic(
            site_id,
            start_time=start_time,
            end_time=end_time,
            metric_scope=metric_scope,
            bucket_time_zone=bucket_time_zone,
            device_type=device_type,
            country=country,
            page_path=page_path,
            traffic_source=traffic_source,
            referrer=referrer,
            browser=browser,
            utm_campaign=utm_campaign,
            utm_medium=utm_medium,
            utm_source=utm_source,
            filter=filter,
            request_options=request_options,
        )
        return _response.data

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
    ) -> TopPagesReportsResponse:
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
        TopPagesReportsResponse
            Pages ranked by `sortBy` for the requested window and filters.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analyze.reports.top_pages(
                site_id="580e63e98c9a982ac9b8b741",
                start_time=datetime.datetime.fromisoformat(
                    "2026-04-01 00:00:00+00:00",
                ),
                end_time=datetime.datetime.fromisoformat(
                    "2026-04-08 00:00:00+00:00",
                ),
                country="US",
                page_path="/towels",
                traffic_source="SO",
                referrer="google.com",
                browser="Chrome",
                utm_campaign="dont-panic-2026",
                utm_medium="email",
                utm_source="hitchhikers-guide",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.top_pages(
            site_id,
            start_time=start_time,
            end_time=end_time,
            sort_by=sort_by,
            limit=limit,
            timeseries=timeseries,
            device_type=device_type,
            country=country,
            page_path=page_path,
            traffic_source=traffic_source,
            referrer=referrer,
            browser=browser,
            utm_campaign=utm_campaign,
            utm_medium=utm_medium,
            utm_source=utm_source,
            filter=filter,
            request_options=request_options,
        )
        return _response.data

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
    ) -> TopDimensionsReportsResponse:
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
        TopDimensionsReportsResponse
            Dimension values ranked by `count` for the requested window and filters.

        Examples
        --------
        import asyncio
        import datetime

        from fern.analyze.reports import (
            TopDimensionsReportsRequestDimension,
            TopDimensionsReportsRequestMetricScope,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analyze.reports.top_dimensions(
                site_id="580e63e98c9a982ac9b8b741",
                start_time=datetime.datetime.fromisoformat(
                    "2026-04-01 00:00:00+00:00",
                ),
                end_time=datetime.datetime.fromisoformat(
                    "2026-04-08 00:00:00+00:00",
                ),
                dimension=TopDimensionsReportsRequestDimension.COUNTRY,
                metric_scope=TopDimensionsReportsRequestMetricScope.SESSION,
                country="US",
                page_path="/towels",
                traffic_source="SO",
                referrer="google.com",
                browser="Chrome",
                utm_campaign="dont-panic-2026",
                utm_medium="email",
                utm_source="hitchhikers-guide",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.top_dimensions(
            site_id,
            start_time=start_time,
            end_time=end_time,
            dimension=dimension,
            metric_scope=metric_scope,
            limit=limit,
            device_type=device_type,
            country=country,
            page_path=page_path,
            traffic_source=traffic_source,
            referrer=referrer,
            browser=browser,
            utm_campaign=utm_campaign,
            utm_medium=utm_medium,
            utm_source=utm_source,
            filter=filter,
            request_options=request_options,
        )
        return _response.data

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
    ) -> TopEventsReportsResponse:
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
        TopEventsReportsResponse
            Events ranked by how frequently they occurred, for the requested window and filters.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analyze.reports.top_events(
                site_id="580e63e98c9a982ac9b8b741",
                start_time=datetime.datetime.fromisoformat(
                    "2026-04-01 00:00:00+00:00",
                ),
                end_time=datetime.datetime.fromisoformat(
                    "2026-04-08 00:00:00+00:00",
                ),
                country="US",
                page_path="/towels",
                traffic_source="SO",
                browser="Chrome",
                utm_campaign="dont-panic-2026",
                utm_medium="email",
                utm_source="hitchhikers-guide",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.top_events(
            site_id,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            timeseries=timeseries,
            device_type=device_type,
            country=country,
            page_path=page_path,
            traffic_source=traffic_source,
            browser=browser,
            utm_campaign=utm_campaign,
            utm_medium=utm_medium,
            utm_source=utm_source,
            filter=filter,
            request_options=request_options,
        )
        return _response.data

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
    ) -> TimeOnPageReportsResponse:
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
        TimeOnPageReportsResponse
            Average time on page for the requested window and filters.

        Examples
        --------
        import asyncio
        import datetime

        from fern.analyze.reports import TimeOnPageReportsRequestMetricScope

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analyze.reports.time_on_page(
                site_id="580e63e98c9a982ac9b8b741",
                start_time=datetime.datetime.fromisoformat(
                    "2026-04-01 00:00:00+00:00",
                ),
                end_time=datetime.datetime.fromisoformat(
                    "2026-04-08 00:00:00+00:00",
                ),
                metric_scope=TimeOnPageReportsRequestMetricScope.SESSION,
                country="US",
                page_path="/towels",
                traffic_source="SO",
                referrer="google.com",
                browser="Chrome",
                utm_campaign="dont-panic-2026",
                utm_medium="email",
                utm_source="hitchhikers-guide",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.time_on_page(
            site_id,
            start_time=start_time,
            end_time=end_time,
            metric_scope=metric_scope,
            timeseries=timeseries,
            device_type=device_type,
            country=country,
            page_path=page_path,
            traffic_source=traffic_source,
            referrer=referrer,
            browser=browser,
            utm_campaign=utm_campaign,
            utm_medium=utm_medium,
            utm_source=utm_source,
            filter=filter,
            request_options=request_options,
        )
        return _response.data
