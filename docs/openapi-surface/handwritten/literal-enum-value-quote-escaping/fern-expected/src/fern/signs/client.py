

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.wording import Wording
from .raw_client import AsyncRawSignsClient, RawSignsClient


class SignsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSignsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSignsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSignsClient
        """
        return self._raw_client

    def list_signs(
        self, *, wording: typing.Optional[Wording] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        wording : typing.Optional[Wording]

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
        client.signs.list_signs()
        """
        _response = self._raw_client.list_signs(wording=wording, request_options=request_options)
        return _response.data


class AsyncSignsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSignsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSignsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSignsClient
        """
        return self._raw_client

    async def list_signs(
        self, *, wording: typing.Optional[Wording] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        wording : typing.Optional[Wording]

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
            await client.signs.list_signs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_signs(wording=wording, request_options=request_options)
        return _response.data
