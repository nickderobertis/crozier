

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBerthsClient, RawBerthsClient


OMIT = typing.cast(typing.Any, ...)


class BerthsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBerthsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBerthsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBerthsClient
        """
        return self._raw_client

    def create_berth(
        self,
        *,
        code: str,
        pontoon: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        code : str

        pontoon : typing.Optional[str]
            Pontoon the berth is moored to

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
        client.berths.create_berth(
            code="code",
        )
        """
        _response = self._raw_client.create_berth(code=code, pontoon=pontoon, request_options=request_options)
        return _response.data


class AsyncBerthsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBerthsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBerthsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBerthsClient
        """
        return self._raw_client

    async def create_berth(
        self,
        *,
        code: str,
        pontoon: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        code : str

        pontoon : typing.Optional[str]
            Pontoon the berth is moored to

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
            await client.berths.create_berth(
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_berth(code=code, pontoon=pontoon, request_options=request_options)
        return _response.data
