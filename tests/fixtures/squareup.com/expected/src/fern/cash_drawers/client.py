

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_cash_drawer_shift_events_response import ListCashDrawerShiftEventsResponse
from ..types.list_cash_drawer_shifts_response import ListCashDrawerShiftsResponse
from ..types.retrieve_cash_drawer_shift_response import RetrieveCashDrawerShiftResponse
from .raw_client import AsyncRawCashDrawersClient, RawCashDrawersClient


class CashDrawersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCashDrawersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCashDrawersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCashDrawersClient
        """
        return self._raw_client

    def list_cash_drawer_shifts(
        self,
        *,
        location_id: str,
        sort_order: typing.Optional[str] = None,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCashDrawerShiftsResponse:
        """
        Provides the details for all of the cash drawer shifts for a location
        in a date range.

        Parameters
        ----------
        location_id : str
            The ID of the location to query for a list of cash drawer shifts.

        sort_order : typing.Optional[str]
            The order in which cash drawer shifts are listed in the response,
            based on their opened_at field. Default value: ASC

        begin_time : typing.Optional[str]
            The inclusive start time of the query on opened_at, in ISO 8601 format.

        end_time : typing.Optional[str]
            The exclusive end date of the query on opened_at, in ISO 8601 format.

        limit : typing.Optional[int]
            Number of cash drawer shift events in a page of results (200 by
            default, 1000 max).

        cursor : typing.Optional[str]
            Opaque cursor for fetching the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCashDrawerShiftsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.cash_drawers.list_cash_drawer_shifts(
            location_id="location_id",
        )
        """
        _response = self._raw_client.list_cash_drawer_shifts(
            location_id=location_id,
            sort_order=sort_order,
            begin_time=begin_time,
            end_time=end_time,
            limit=limit,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data

    def retrieve_cash_drawer_shift(
        self, shift_id: str, *, location_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveCashDrawerShiftResponse:
        """
        Provides the summary details for a single cash drawer shift. See
        [ListCashDrawerShiftEvents](https://developer.squareup.com/reference/square_2021-08-18/cash-drawers-api/list-cash-drawer-shift-events) for a list of cash drawer shift events.

        Parameters
        ----------
        shift_id : str
            The shift ID.

        location_id : str
            The ID of the location to retrieve cash drawer shifts from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveCashDrawerShiftResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.cash_drawers.retrieve_cash_drawer_shift(
            shift_id="shift_id",
            location_id="location_id",
        )
        """
        _response = self._raw_client.retrieve_cash_drawer_shift(
            shift_id, location_id=location_id, request_options=request_options
        )
        return _response.data

    def list_cash_drawer_shift_events(
        self,
        shift_id: str,
        *,
        location_id: str,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCashDrawerShiftEventsResponse:
        """
        Provides a paginated list of events for a single cash drawer shift.

        Parameters
        ----------
        shift_id : str
            The shift ID.

        location_id : str
            The ID of the location to list cash drawer shifts for.

        limit : typing.Optional[int]
            Number of resources to be returned in a page of results (200 by
            default, 1000 max).

        cursor : typing.Optional[str]
            Opaque cursor for fetching the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCashDrawerShiftEventsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.cash_drawers.list_cash_drawer_shift_events(
            shift_id="shift_id",
            location_id="location_id",
        )
        """
        _response = self._raw_client.list_cash_drawer_shift_events(
            shift_id, location_id=location_id, limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data


class AsyncCashDrawersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCashDrawersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCashDrawersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCashDrawersClient
        """
        return self._raw_client

    async def list_cash_drawer_shifts(
        self,
        *,
        location_id: str,
        sort_order: typing.Optional[str] = None,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCashDrawerShiftsResponse:
        """
        Provides the details for all of the cash drawer shifts for a location
        in a date range.

        Parameters
        ----------
        location_id : str
            The ID of the location to query for a list of cash drawer shifts.

        sort_order : typing.Optional[str]
            The order in which cash drawer shifts are listed in the response,
            based on their opened_at field. Default value: ASC

        begin_time : typing.Optional[str]
            The inclusive start time of the query on opened_at, in ISO 8601 format.

        end_time : typing.Optional[str]
            The exclusive end date of the query on opened_at, in ISO 8601 format.

        limit : typing.Optional[int]
            Number of cash drawer shift events in a page of results (200 by
            default, 1000 max).

        cursor : typing.Optional[str]
            Opaque cursor for fetching the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCashDrawerShiftsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cash_drawers.list_cash_drawer_shifts(
                location_id="location_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_cash_drawer_shifts(
            location_id=location_id,
            sort_order=sort_order,
            begin_time=begin_time,
            end_time=end_time,
            limit=limit,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_cash_drawer_shift(
        self, shift_id: str, *, location_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveCashDrawerShiftResponse:
        """
        Provides the summary details for a single cash drawer shift. See
        [ListCashDrawerShiftEvents](https://developer.squareup.com/reference/square_2021-08-18/cash-drawers-api/list-cash-drawer-shift-events) for a list of cash drawer shift events.

        Parameters
        ----------
        shift_id : str
            The shift ID.

        location_id : str
            The ID of the location to retrieve cash drawer shifts from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveCashDrawerShiftResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cash_drawers.retrieve_cash_drawer_shift(
                shift_id="shift_id",
                location_id="location_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_cash_drawer_shift(
            shift_id, location_id=location_id, request_options=request_options
        )
        return _response.data

    async def list_cash_drawer_shift_events(
        self,
        shift_id: str,
        *,
        location_id: str,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCashDrawerShiftEventsResponse:
        """
        Provides a paginated list of events for a single cash drawer shift.

        Parameters
        ----------
        shift_id : str
            The shift ID.

        location_id : str
            The ID of the location to list cash drawer shifts for.

        limit : typing.Optional[int]
            Number of resources to be returned in a page of results (200 by
            default, 1000 max).

        cursor : typing.Optional[str]
            Opaque cursor for fetching the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCashDrawerShiftEventsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cash_drawers.list_cash_drawer_shift_events(
                shift_id="shift_id",
                location_id="location_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_cash_drawer_shift_events(
            shift_id, location_id=location_id, limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data
