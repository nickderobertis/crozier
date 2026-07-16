

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.calendar import Calendar
from ..types.calendar_attributes import CalendarAttributes
from .raw_client import AsyncRawCalendarsClient, RawCalendarsClient


OMIT = typing.cast(typing.Any, ...)


class CalendarsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCalendarsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCalendarsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCalendarsClient
        """
        return self._raw_client

    def fetch_a_list_of_calendars(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Calendar]:
        """
        Without params, it returns a list of Calendars the user has access to

        Parameters
        ----------
        all_ : typing.Optional[bool]
            Can only be used by admins or managers to fetch all entities

        user_id : typing.Optional[int]
            Standard users can use this only with their own _userId_

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Calendar]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.calendars.fetch_a_list_of_calendars()
        """
        _response = self._raw_client.fetch_a_list_of_calendars(
            all_=all_, user_id=user_id, request_options=request_options
        )
        return _response.data

    def create_a_calendar(
        self,
        *,
        attributes: typing.Optional[CalendarAttributes] = OMIT,
        data: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Calendar:
        """
        Parameters
        ----------
        attributes : typing.Optional[CalendarAttributes]

        data : typing.Optional[str]
            base64 encoded in iCalendar format

        id : typing.Optional[int]

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Calendar
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.calendars.create_a_calendar()
        """
        _response = self._raw_client.create_a_calendar(
            attributes=attributes, data=data, id=id, name=name, request_options=request_options
        )
        return _response.data

    def update_a_calendar(
        self,
        id_: int,
        *,
        attributes: typing.Optional[CalendarAttributes] = OMIT,
        data: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Calendar:
        """
        Parameters
        ----------
        id_ : int

        attributes : typing.Optional[CalendarAttributes]

        data : typing.Optional[str]
            base64 encoded in iCalendar format

        id : typing.Optional[int]

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Calendar
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.calendars.update_a_calendar(
            id_=1,
        )
        """
        _response = self._raw_client.update_a_calendar(
            id_, attributes=attributes, data=data, id=id, name=name, request_options=request_options
        )
        return _response.data

    def delete_a_calendar(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.calendars.delete_a_calendar(
            id=1,
        )
        """
        _response = self._raw_client.delete_a_calendar(id, request_options=request_options)
        return _response.data


class AsyncCalendarsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCalendarsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCalendarsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCalendarsClient
        """
        return self._raw_client

    async def fetch_a_list_of_calendars(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Calendar]:
        """
        Without params, it returns a list of Calendars the user has access to

        Parameters
        ----------
        all_ : typing.Optional[bool]
            Can only be used by admins or managers to fetch all entities

        user_id : typing.Optional[int]
            Standard users can use this only with their own _userId_

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Calendar]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.calendars.fetch_a_list_of_calendars()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_a_list_of_calendars(
            all_=all_, user_id=user_id, request_options=request_options
        )
        return _response.data

    async def create_a_calendar(
        self,
        *,
        attributes: typing.Optional[CalendarAttributes] = OMIT,
        data: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Calendar:
        """
        Parameters
        ----------
        attributes : typing.Optional[CalendarAttributes]

        data : typing.Optional[str]
            base64 encoded in iCalendar format

        id : typing.Optional[int]

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Calendar
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.calendars.create_a_calendar()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_calendar(
            attributes=attributes, data=data, id=id, name=name, request_options=request_options
        )
        return _response.data

    async def update_a_calendar(
        self,
        id_: int,
        *,
        attributes: typing.Optional[CalendarAttributes] = OMIT,
        data: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Calendar:
        """
        Parameters
        ----------
        id_ : int

        attributes : typing.Optional[CalendarAttributes]

        data : typing.Optional[str]
            base64 encoded in iCalendar format

        id : typing.Optional[int]

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Calendar
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.calendars.update_a_calendar(
                id_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_a_calendar(
            id_, attributes=attributes, data=data, id=id, name=name, request_options=request_options
        )
        return _response.data

    async def delete_a_calendar(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.calendars.delete_a_calendar(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_calendar(id, request_options=request_options)
        return _response.data
