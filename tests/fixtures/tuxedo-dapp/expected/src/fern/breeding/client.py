

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBreedingClient, RawBreedingClient


OMIT = typing.cast(typing.Any, ...)


class BreedingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBreedingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBreedingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBreedingClient
        """
        return self._raw_client

    def breed_kitty(
        self,
        *,
        mom: typing.Optional[str] = OMIT,
        dad: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Breed two tradable, ready for it kitties, to get a new one

        Parameters
        ----------
        mom : typing.Optional[str]
            dna of mom

        dad : typing.Optional[str]
            dna of dad

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.breeding.breed_kitty()
        """
        _response = self._raw_client.breed_kitty(mom=mom, dad=dad, request_options=request_options)
        return _response.data


class AsyncBreedingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBreedingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBreedingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBreedingClient
        """
        return self._raw_client

    async def breed_kitty(
        self,
        *,
        mom: typing.Optional[str] = OMIT,
        dad: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Breed two tradable, ready for it kitties, to get a new one

        Parameters
        ----------
        mom : typing.Optional[str]
            dna of mom

        dad : typing.Optional[str]
            dna of dad

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.breeding.breed_kitty()


        asyncio.run(main())
        """
        _response = await self._raw_client.breed_kitty(mom=mom, dad=dad, request_options=request_options)
        return _response.data
