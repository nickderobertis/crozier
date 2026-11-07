

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTelemetryClient, RawTelemetryClient
from .types.log_list_request_direction import LogListRequestDirection
from .types.log_list_response import LogListResponse
from .types.trace_list_request_direction import TraceListRequestDirection
from .types.trace_list_request_order_by import TraceListRequestOrderBy
from .types.trace_list_response import TraceListResponse


class TelemetryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTelemetryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTelemetryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTelemetryClient
        """
        return self._raw_client

    def trace_list(
        self,
        *,
        direction: TraceListRequestDirection,
        limit: int,
        file_id: typing.Optional[str] = None,
        branch_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        start: typing.Optional[dt.datetime] = None,
        end: typing.Optional[dt.datetime] = None,
        order_by: typing.Optional[TraceListRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TraceListResponse:
        """
        Get OpenTelemetry traces within a specified time window with flexible pagination options: Pass in only the end time to paginate backwards from there. Pass in a start time to paginate backwards from now until the start time. Pass in both to get resources within the time window. Choose to return in end_time order instead to view traces that completed in a window or since a time. Filter additionally by branch_ids or file_id.

        Parameters
        ----------
        direction : TraceListRequestDirection
            Sort direction for the traces. Defaults to descending order of timestamp.

        limit : int
            Maximum items to return in each paginated response

        file_id : typing.Optional[str]
            Include only resources from a given file identified by its ID

        branch_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Branch IDs to filter by

        start : typing.Optional[dt.datetime]
            Start date of the time window (earliest time)

        end : typing.Optional[dt.datetime]
            End date of the time window (latest time)

        order_by : typing.Optional[TraceListRequestOrderBy]
            When set to end_time, traces are sorted by their end time, and pending traces are omitted. When set to start_time, all traces are included, with pending traces given "0" for their end time.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TraceListResponse
            A paginated result set

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.telemetry.trace_list(
            direction="asc",
            limit=1,
        )
        """
        _response = self._raw_client.trace_list(
            direction=direction,
            limit=limit,
            file_id=file_id,
            branch_ids=branch_ids,
            start=start,
            end=end,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    def log_list(
        self,
        *,
        direction: LogListRequestDirection,
        limit: int,
        trace_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        file_id: typing.Optional[str] = None,
        branch_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        start: typing.Optional[dt.datetime] = None,
        end: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogListResponse:
        """
        Get OpenTelemetry logs within a specified time window with flexible pagination options: Pass in only the end time to paginate backwards from there. Pass in a start time to paginate backwards from now until the start time. Pass in both to get resources within the time window. Filter additionally by branch_ids or file_id.

        Parameters
        ----------
        direction : LogListRequestDirection
            Sort direction for the traces. Defaults to descending order of timestamp.

        limit : int
            Maximum items to return in each paginated response

        trace_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        file_id : typing.Optional[str]
            Include only resources from a given file identified by its ID

        branch_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Branch IDs to filter by

        start : typing.Optional[dt.datetime]
            Start date of the time window (earliest time)

        end : typing.Optional[dt.datetime]
            End date of the time window (latest time)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogListResponse
            A paginated result set

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.telemetry.log_list(
            direction="asc",
            limit=1,
        )
        """
        _response = self._raw_client.log_list(
            direction=direction,
            limit=limit,
            trace_ids=trace_ids,
            file_id=file_id,
            branch_ids=branch_ids,
            start=start,
            end=end,
            request_options=request_options,
        )
        return _response.data


class AsyncTelemetryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTelemetryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTelemetryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTelemetryClient
        """
        return self._raw_client

    async def trace_list(
        self,
        *,
        direction: TraceListRequestDirection,
        limit: int,
        file_id: typing.Optional[str] = None,
        branch_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        start: typing.Optional[dt.datetime] = None,
        end: typing.Optional[dt.datetime] = None,
        order_by: typing.Optional[TraceListRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TraceListResponse:
        """
        Get OpenTelemetry traces within a specified time window with flexible pagination options: Pass in only the end time to paginate backwards from there. Pass in a start time to paginate backwards from now until the start time. Pass in both to get resources within the time window. Choose to return in end_time order instead to view traces that completed in a window or since a time. Filter additionally by branch_ids or file_id.

        Parameters
        ----------
        direction : TraceListRequestDirection
            Sort direction for the traces. Defaults to descending order of timestamp.

        limit : int
            Maximum items to return in each paginated response

        file_id : typing.Optional[str]
            Include only resources from a given file identified by its ID

        branch_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Branch IDs to filter by

        start : typing.Optional[dt.datetime]
            Start date of the time window (earliest time)

        end : typing.Optional[dt.datetime]
            End date of the time window (latest time)

        order_by : typing.Optional[TraceListRequestOrderBy]
            When set to end_time, traces are sorted by their end time, and pending traces are omitted. When set to start_time, all traces are included, with pending traces given "0" for their end time.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TraceListResponse
            A paginated result set

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.telemetry.trace_list(
                direction="asc",
                limit=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.trace_list(
            direction=direction,
            limit=limit,
            file_id=file_id,
            branch_ids=branch_ids,
            start=start,
            end=end,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    async def log_list(
        self,
        *,
        direction: LogListRequestDirection,
        limit: int,
        trace_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        file_id: typing.Optional[str] = None,
        branch_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        start: typing.Optional[dt.datetime] = None,
        end: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogListResponse:
        """
        Get OpenTelemetry logs within a specified time window with flexible pagination options: Pass in only the end time to paginate backwards from there. Pass in a start time to paginate backwards from now until the start time. Pass in both to get resources within the time window. Filter additionally by branch_ids or file_id.

        Parameters
        ----------
        direction : LogListRequestDirection
            Sort direction for the traces. Defaults to descending order of timestamp.

        limit : int
            Maximum items to return in each paginated response

        trace_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        file_id : typing.Optional[str]
            Include only resources from a given file identified by its ID

        branch_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Branch IDs to filter by

        start : typing.Optional[dt.datetime]
            Start date of the time window (earliest time)

        end : typing.Optional[dt.datetime]
            End date of the time window (latest time)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogListResponse
            A paginated result set

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.telemetry.log_list(
                direction="asc",
                limit=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.log_list(
            direction=direction,
            limit=limit,
            trace_ids=trace_ids,
            file_id=file_id,
            branch_ids=branch_ids,
            start=start,
            end=end,
            request_options=request_options,
        )
        return _response.data
