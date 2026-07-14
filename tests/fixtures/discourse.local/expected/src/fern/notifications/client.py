

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawNotificationsClient, RawNotificationsClient
from .types.get_notifications_response import GetNotificationsResponse
from .types.mark_notifications_as_read_response import MarkNotificationsAsReadResponse


OMIT = typing.cast(typing.Any, ...)


class NotificationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNotificationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNotificationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNotificationsClient
        """
        return self._raw_client

    def get_notifications(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetNotificationsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetNotificationsResponse
            notifications

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.notifications.get_notifications()
        """
        _response = self._raw_client.get_notifications(request_options=request_options)
        return _response.data

    def mark_notifications_as_read(
        self, *, id: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> MarkNotificationsAsReadResponse:
        """
        Parameters
        ----------
        id : typing.Optional[int]
            (optional) Leave off to mark all notifications as
            read

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarkNotificationsAsReadResponse
            notifications marked read

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.notifications.mark_notifications_as_read()
        """
        _response = self._raw_client.mark_notifications_as_read(id=id, request_options=request_options)
        return _response.data


class AsyncNotificationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNotificationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNotificationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNotificationsClient
        """
        return self._raw_client

    async def get_notifications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetNotificationsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetNotificationsResponse
            notifications

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.notifications.get_notifications()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_notifications(request_options=request_options)
        return _response.data

    async def mark_notifications_as_read(
        self, *, id: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> MarkNotificationsAsReadResponse:
        """
        Parameters
        ----------
        id : typing.Optional[int]
            (optional) Leave off to mark all notifications as
            read

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MarkNotificationsAsReadResponse
            notifications marked read

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.notifications.mark_notifications_as_read()


        asyncio.run(main())
        """
        _response = await self._raw_client.mark_notifications_as_read(id=id, request_options=request_options)
        return _response.data
