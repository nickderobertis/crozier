

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCoilsClient, RawCoilsClient


OMIT = typing.cast(typing.Any, ...)


class CoilsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCoilsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCoilsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCoilsClient
        """
        return self._raw_client

    def order_coil(self, *, length_m: int, fibre: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        length_m : int

        fibre : str

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
        client.coils.order_coil(
            length_m=1,
            fibre="fibre",
        )
        """
        _response = self._raw_client.order_coil(length_m=length_m, fibre=fibre, request_options=request_options)
        return _response.data


class AsyncCoilsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCoilsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCoilsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCoilsClient
        """
        return self._raw_client

    async def order_coil(
        self, *, length_m: int, fibre: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        length_m : int

        fibre : str

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
            await client.coils.order_coil(
                length_m=1,
                fibre="fibre",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.order_coil(length_m=length_m, fibre=fibre, request_options=request_options)
        return _response.data
