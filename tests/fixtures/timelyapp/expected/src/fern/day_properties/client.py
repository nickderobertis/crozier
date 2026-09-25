

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1day_property import V1DayProperty
from .raw_client import AsyncRawDayPropertiesClient, RawDayPropertiesClient
from .types.v1day_properties_create_day_property import V1DayPropertiesCreateDayProperty
from .types.v1day_properties_update_day_property import V1DayPropertiesUpdateDayProperty


OMIT = typing.cast(typing.Any, ...)


class DayPropertiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDayPropertiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDayPropertiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDayPropertiesClient
        """
        return self._raw_client

    def list_day_properties(
        self,
        account_id: int,
        *,
        since: typing.Optional[dt.date] = None,
        until: typing.Optional[dt.date] = None,
        dates: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1DayProperty]:
        """
        Retrieve day properties (locked days) for users in the account. Day properties control whether time entries can be modified for specific dates.

        You can filter by date range using `since` and `until` parameters, or by specific dates using the `dates` parameter.

        Parameters
        ----------
        account_id : int
            Account ID

        since : typing.Optional[dt.date]
            Start date for filtering (YYYY-MM-DD)

        until : typing.Optional[dt.date]
            End date for filtering (YYYY-MM-DD)

        dates : typing.Optional[str]
            Comma-separated list of specific dates (YYYY-MM-DD)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1DayProperty]
            Day properties retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.day_properties.list_day_properties(
            account_id=1,
        )
        """
        _response = self._raw_client.list_day_properties(
            account_id, since=since, until=until, dates=dates, request_options=request_options
        )
        return _response.data

    def create_day_properties(
        self,
        account_id: int,
        *,
        day_property: V1DayPropertiesCreateDayProperty,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1DayProperty]:
        """
        Create or update day properties to lock or unlock days for time entry modifications. This endpoint allows bulk operations across multiple users and dates.

        When a day is locked, users cannot create, update, or delete time entries for that date. Only users with appropriate permissions (admins or managers) can lock/unlock days.

        Parameters
        ----------
        account_id : int
            Account ID

        day_property : V1DayPropertiesCreateDayProperty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1DayProperty]
            Day properties created successfully

        Examples
        --------
        from fern.day_properties import V1DayPropertiesCreateDayProperty

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.day_properties.create_day_properties(
            account_id=1,
            day_property=V1DayPropertiesCreateDayProperty(
                dates=["2024-01-01", "2024-01-02"],
                user_ids=[1],
                locked=True,
            ),
        )
        """
        _response = self._raw_client.create_day_properties(
            account_id, day_property=day_property, request_options=request_options
        )
        return _response.data

    def update_day_properties(
        self,
        account_id: int,
        *,
        day_property: V1DayPropertiesUpdateDayProperty,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1DayProperty]:
        """
        Update day properties to lock or unlock days for time entry modifications. This endpoint allows bulk operations across multiple users and dates.

        Use `locked: false` to unlock previously locked days, allowing users to modify time entries for those dates again.

        Parameters
        ----------
        account_id : int
            Account ID

        day_property : V1DayPropertiesUpdateDayProperty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1DayProperty]
            Day properties updated successfully

        Examples
        --------
        from fern.day_properties import V1DayPropertiesUpdateDayProperty

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.day_properties.update_day_properties(
            account_id=1,
            day_property=V1DayPropertiesUpdateDayProperty(
                dates=["2024-01-01"],
                user_ids=[1],
                locked=False,
            ),
        )
        """
        _response = self._raw_client.update_day_properties(
            account_id, day_property=day_property, request_options=request_options
        )
        return _response.data


class AsyncDayPropertiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDayPropertiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDayPropertiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDayPropertiesClient
        """
        return self._raw_client

    async def list_day_properties(
        self,
        account_id: int,
        *,
        since: typing.Optional[dt.date] = None,
        until: typing.Optional[dt.date] = None,
        dates: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1DayProperty]:
        """
        Retrieve day properties (locked days) for users in the account. Day properties control whether time entries can be modified for specific dates.

        You can filter by date range using `since` and `until` parameters, or by specific dates using the `dates` parameter.

        Parameters
        ----------
        account_id : int
            Account ID

        since : typing.Optional[dt.date]
            Start date for filtering (YYYY-MM-DD)

        until : typing.Optional[dt.date]
            End date for filtering (YYYY-MM-DD)

        dates : typing.Optional[str]
            Comma-separated list of specific dates (YYYY-MM-DD)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1DayProperty]
            Day properties retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.day_properties.list_day_properties(
                account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_day_properties(
            account_id, since=since, until=until, dates=dates, request_options=request_options
        )
        return _response.data

    async def create_day_properties(
        self,
        account_id: int,
        *,
        day_property: V1DayPropertiesCreateDayProperty,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1DayProperty]:
        """
        Create or update day properties to lock or unlock days for time entry modifications. This endpoint allows bulk operations across multiple users and dates.

        When a day is locked, users cannot create, update, or delete time entries for that date. Only users with appropriate permissions (admins or managers) can lock/unlock days.

        Parameters
        ----------
        account_id : int
            Account ID

        day_property : V1DayPropertiesCreateDayProperty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1DayProperty]
            Day properties created successfully

        Examples
        --------
        import asyncio

        from fern.day_properties import V1DayPropertiesCreateDayProperty

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.day_properties.create_day_properties(
                account_id=1,
                day_property=V1DayPropertiesCreateDayProperty(
                    dates=["2024-01-01", "2024-01-02"],
                    user_ids=[1],
                    locked=True,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_day_properties(
            account_id, day_property=day_property, request_options=request_options
        )
        return _response.data

    async def update_day_properties(
        self,
        account_id: int,
        *,
        day_property: V1DayPropertiesUpdateDayProperty,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1DayProperty]:
        """
        Update day properties to lock or unlock days for time entry modifications. This endpoint allows bulk operations across multiple users and dates.

        Use `locked: false` to unlock previously locked days, allowing users to modify time entries for those dates again.

        Parameters
        ----------
        account_id : int
            Account ID

        day_property : V1DayPropertiesUpdateDayProperty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1DayProperty]
            Day properties updated successfully

        Examples
        --------
        import asyncio

        from fern.day_properties import V1DayPropertiesUpdateDayProperty

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.day_properties.update_day_properties(
                account_id=1,
                day_property=V1DayPropertiesUpdateDayProperty(
                    dates=["2024-01-01"],
                    user_ids=[1],
                    locked=False,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_day_properties(
            account_id, day_property=day_property, request_options=request_options
        )
        return _response.data
