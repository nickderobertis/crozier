

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tree import Tree
from .raw_client import AsyncRawTreesClient, RawTreesClient


OMIT = typing.cast(typing.Any, ...)


class TreesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTreesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTreesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTreesClient
        """
        return self._raw_client

    def plant_tree(self, *, variety: str, request_options: typing.Optional[RequestOptions] = None) -> Tree:
        """
        Parameters
        ----------
        variety : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tree
            The planted tree.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            "spring",
        )
        client.trees.plant_tree(
            variety="variety",
        )
        """
        _response = self._raw_client.plant_tree(variety=variety, request_options=request_options)
        return _response.data


class AsyncTreesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTreesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTreesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTreesClient
        """
        return self._raw_client

    async def plant_tree(self, *, variety: str, request_options: typing.Optional[RequestOptions] = None) -> Tree:
        """
        Parameters
        ----------
        variety : str

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

        client = AsyncFernApi(
            "spring",
        )


        async def main() -> None:
            await client.trees.plant_tree(
                variety="variety",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.plant_tree(variety=variety, request_options=request_options)
        return _response.data
