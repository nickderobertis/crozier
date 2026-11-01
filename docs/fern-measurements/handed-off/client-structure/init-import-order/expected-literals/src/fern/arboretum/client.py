

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tree import Tree
from .raw_client import AsyncRawArboretumClient, RawArboretumClient
from .types.plant_tree_request_zone import PlantTreeRequestZone


OMIT = typing.cast(typing.Any, ...)


class ArboretumClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawArboretumClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawArboretumClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawArboretumClient
        """
        return self._raw_client

    def plant_tree(
        self,
        *,
        species: str,
        zone: typing.Optional[PlantTreeRequestZone] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tree:
        """
        Parameters
        ----------
        species : str

        zone : typing.Optional[PlantTreeRequestZone]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tree
            The planted tree.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.arboretum.plant_tree(
            species="species",
        )
        """
        _response = self._raw_client.plant_tree(species=species, zone=zone, request_options=request_options)
        return _response.data


class AsyncArboretumClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawArboretumClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawArboretumClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawArboretumClient
        """
        return self._raw_client

    async def plant_tree(
        self,
        *,
        species: str,
        zone: typing.Optional[PlantTreeRequestZone] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tree:
        """
        Parameters
        ----------
        species : str

        zone : typing.Optional[PlantTreeRequestZone]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tree
            The planted tree.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.arboretum.plant_tree(
                species="species",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.plant_tree(species=species, zone=zone, request_options=request_options)
        return _response.data
