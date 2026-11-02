

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDispatchesClient, RawDispatchesClient


OMIT = typing.cast(typing.Any, ...)


class DispatchesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDispatchesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDispatchesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDispatchesClient
        """
        return self._raw_client

    def create_dispatch(
        self,
        *,
        parcel: str,
        fragile: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        parcel : str

        fragile : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dispatches.create_dispatch(
            parcel="parcel",
        )
        """
        _response = self._raw_client.create_dispatch(parcel=parcel, fragile=fragile, request_options=request_options)
        return _response.data


class AsyncDispatchesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDispatchesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDispatchesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDispatchesClient
        """
        return self._raw_client

    async def create_dispatch(
        self,
        *,
        parcel: str,
        fragile: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        parcel : str

        fragile : typing.Optional[bool]

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
            await client.dispatches.create_dispatch(
                parcel="parcel",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_dispatch(
            parcel=parcel, fragile=fragile, request_options=request_options
        )
        return _response.data
