

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.event_log import EventLog
from ..types.event_log_collection import EventLogCollection
from .raw_client import AsyncRawEventLogClient, RawEventLogClient


class EventLogClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEventLogClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEventLogClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEventLogClient
        """
        return self._raw_client

    def get_event_logs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EventLogCollection:
        """
        List log entries from event log.

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventLogCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.event_log.get_event_logs()
        """
        _response = self._raw_client.get_event_logs(
            limit=limit, offset=offset, order_by=order_by, request_options=request_options
        )
        return _response.data

    def get_event_log(self, event_log_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> EventLog:
        """
        Parameters
        ----------
        event_log_id : int
            The event log ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventLog
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.event_log.get_event_log(
            event_log_id=1,
        )
        """
        _response = self._raw_client.get_event_log(event_log_id, request_options=request_options)
        return _response.data


class AsyncEventLogClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEventLogClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEventLogClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEventLogClient
        """
        return self._raw_client

    async def get_event_logs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EventLogCollection:
        """
        List log entries from event log.

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventLogCollection
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.event_log.get_event_logs()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_event_logs(
            limit=limit, offset=offset, order_by=order_by, request_options=request_options
        )
        return _response.data

    async def get_event_log(
        self, event_log_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EventLog:
        """
        Parameters
        ----------
        event_log_id : int
            The event log ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventLog
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.event_log.get_event_log(
                event_log_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_event_log(event_log_id, request_options=request_options)
        return _response.data
