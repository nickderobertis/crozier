

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawScalesClient, RawScalesClient


OMIT = typing.cast(typing.Any, ...)


class ScalesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawScalesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawScalesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawScalesClient
        """
        return self._raw_client

    def weigh_pallet(
        self, pallet_id: str, *, kilograms: float, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        pallet_id : str

        kilograms : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.scales.weigh_pallet(
            pallet_id="palletId",
            kilograms=1.1,
        )
        """
        _response = self._raw_client.weigh_pallet(pallet_id, kilograms=kilograms, request_options=request_options)
        return _response.data


class AsyncScalesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawScalesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawScalesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawScalesClient
        """
        return self._raw_client

    async def weigh_pallet(
        self, pallet_id: str, *, kilograms: float, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        pallet_id : str

        kilograms : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.scales.weigh_pallet(
                pallet_id="palletId",
                kilograms=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.weigh_pallet(pallet_id, kilograms=kilograms, request_options=request_options)
        return _response.data
