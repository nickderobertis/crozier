

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.notice import Notice
from .raw_client import AsyncRawNoticesClient, RawNoticesClient


class NoticesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNoticesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNoticesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNoticesClient
        """
        return self._raw_client

    def latest_notice(self, *, request_options: typing.Optional[RequestOptions] = None) -> Notice:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Notice
            The most recent door notice.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.notices.latest_notice()
        """
        _response = self._raw_client.latest_notice(request_options=request_options)
        return _response.data


class AsyncNoticesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNoticesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNoticesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNoticesClient
        """
        return self._raw_client

    async def latest_notice(self, *, request_options: typing.Optional[RequestOptions] = None) -> Notice:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Notice
            The most recent door notice.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.notices.latest_notice()


        asyncio.run(main())
        """
        _response = await self._raw_client.latest_notice(request_options=request_options)
        return _response.data
