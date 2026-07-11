

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.http_status import HttpStatus
from ..types.priority import Priority
from ..types.ticket import Ticket
from .raw_client import AsyncRawEnumsClient, RawEnumsClient


OMIT = typing.cast(typing.Any, ...)


class EnumsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEnumsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEnumsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEnumsClient
        """
        return self._raw_client

    def setpriority(
        self, *, level: Priority, request: HttpStatus, request_options: typing.Optional[RequestOptions] = None
    ) -> Ticket:
        """
        Parameters
        ----------
        level : Priority

        request : HttpStatus

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ticket


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.enums.setpriority(
            level=1,
            request=1000000,
        )
        """
        _response = self._raw_client.setpriority(level=level, request=request, request_options=request_options)
        return _response.data


class AsyncEnumsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEnumsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEnumsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEnumsClient
        """
        return self._raw_client

    async def setpriority(
        self, *, level: Priority, request: HttpStatus, request_options: typing.Optional[RequestOptions] = None
    ) -> Ticket:
        """
        Parameters
        ----------
        level : Priority

        request : HttpStatus

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ticket


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.enums.setpriority(
                level=1,
                request=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.setpriority(level=level, request=request, request_options=request_options)
        return _response.data
