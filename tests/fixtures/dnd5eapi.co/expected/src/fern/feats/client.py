

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.feat import Feat
from .raw_client import AsyncRawFeatsClient, RawFeatsClient
from .types.get_api_feats_index_request_index import GetApiFeatsIndexRequestIndex


class FeatsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFeatsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFeatsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFeatsClient
        """
        return self._raw_client

    def get_a_feat_by_index(
        self, index: GetApiFeatsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Feat:
        """
        # Feat

        A feat is a boon a character can receive at level up instead of an ability score increase.

        Parameters
        ----------
        index : GetApiFeatsIndexRequestIndex
            The `index` of the feat to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Feat
            OK

        Examples
        --------
        from fern.feats import GetApiFeatsIndexRequestIndex

        from fern import FernApi

        client = FernApi()
        client.feats.get_a_feat_by_index(
            index=GetApiFeatsIndexRequestIndex.GRAPPLER,
        )
        """
        _response = self._raw_client.get_a_feat_by_index(index, request_options=request_options)
        return _response.data


class AsyncFeatsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFeatsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFeatsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFeatsClient
        """
        return self._raw_client

    async def get_a_feat_by_index(
        self, index: GetApiFeatsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Feat:
        """
        # Feat

        A feat is a boon a character can receive at level up instead of an ability score increase.

        Parameters
        ----------
        index : GetApiFeatsIndexRequestIndex
            The `index` of the feat to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Feat
            OK

        Examples
        --------
        import asyncio

        from fern.feats import GetApiFeatsIndexRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.feats.get_a_feat_by_index(
                index=GetApiFeatsIndexRequestIndex.GRAPPLER,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_feat_by_index(index, request_options=request_options)
        return _response.data
