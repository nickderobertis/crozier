

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPrintsClient, RawPrintsClient


OMIT = typing.cast(typing.Any, ...)


class PrintsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPrintsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPrintsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPrintsClient
        """
        return self._raw_client

    def order_print(
        self,
        *,
        negative: typing.Optional[core.File] = OMIT,
        instructions: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        negative : typing.Optional[core.File]
            See core.File for more documentation

        instructions : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.prints.order_print()
        """
        _response = self._raw_client.order_print(
            negative=negative, instructions=instructions, request_options=request_options
        )
        return _response.data


class AsyncPrintsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPrintsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPrintsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPrintsClient
        """
        return self._raw_client

    async def order_print(
        self,
        *,
        negative: typing.Optional[core.File] = OMIT,
        instructions: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        negative : typing.Optional[core.File]
            See core.File for more documentation

        instructions : typing.Optional[typing.Any]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.prints.order_print()


        asyncio.run(main())
        """
        _response = await self._raw_client.order_print(
            negative=negative, instructions=instructions, request_options=request_options
        )
        return _response.data
