

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.trait import Trait
from .raw_client import AsyncRawTraitsClient, RawTraitsClient
from .types.get_api_traits_index_request_index import GetApiTraitsIndexRequestIndex


class TraitsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTraitsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTraitsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTraitsClient
        """
        return self._raw_client

    def get_a_trait_by_index(
        self, index: GetApiTraitsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Trait:
        """
        Parameters
        ----------
        index : GetApiTraitsIndexRequestIndex
            The `index` of the `Trait` to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Trait
            OK

        Examples
        --------
        from fern.traits import GetApiTraitsIndexRequestIndex

        from fern import FernApi

        client = FernApi()
        client.traits.get_a_trait_by_index(
            index=GetApiTraitsIndexRequestIndex.ARTIFICERS_LORE,
        )
        """
        _response = self._raw_client.get_a_trait_by_index(index, request_options=request_options)
        return _response.data


class AsyncTraitsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTraitsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTraitsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTraitsClient
        """
        return self._raw_client

    async def get_a_trait_by_index(
        self, index: GetApiTraitsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Trait:
        """
        Parameters
        ----------
        index : GetApiTraitsIndexRequestIndex
            The `index` of the `Trait` to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Trait
            OK

        Examples
        --------
        import asyncio

        from fern.traits import GetApiTraitsIndexRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.traits.get_a_trait_by_index(
                index=GetApiTraitsIndexRequestIndex.ARTIFICERS_LORE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_trait_by_index(index, request_options=request_options)
        return _response.data
