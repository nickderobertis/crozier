

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.feature import Feature
from .raw_client import AsyncRawFeaturesClient, RawFeaturesClient


class FeaturesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFeaturesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFeaturesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFeaturesClient
        """
        return self._raw_client

    def get_a_feature_by_index(self, index: str, *, request_options: typing.Optional[RequestOptions] = None) -> Feature:
        """
        # Feature

        When you gain a new level in a class, you get its features for that level.
        You don’t, however, receive the class’s starting Equipment, and a few
        features have additional rules when you’re multiclassing: Channel Divinity,
        Extra Attack, Unarmored Defense, and Spellcasting.

        Parameters
        ----------
        index : str
            The `index` of the feature to get.

            Available values can be found in the [`ResourceList`](#get-/api/-endpoint-) for `features`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Feature
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.features.get_a_feature_by_index(
            index="action-surge-1-use",
        )
        """
        _response = self._raw_client.get_a_feature_by_index(index, request_options=request_options)
        return _response.data


class AsyncFeaturesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFeaturesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFeaturesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFeaturesClient
        """
        return self._raw_client

    async def get_a_feature_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Feature:
        """
        # Feature

        When you gain a new level in a class, you get its features for that level.
        You don’t, however, receive the class’s starting Equipment, and a few
        features have additional rules when you’re multiclassing: Channel Divinity,
        Extra Attack, Unarmored Defense, and Spellcasting.

        Parameters
        ----------
        index : str
            The `index` of the feature to get.

            Available values can be found in the [`ResourceList`](#get-/api/-endpoint-) for `features`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Feature
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.features.get_a_feature_by_index(
                index="action-surge-1-use",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_feature_by_index(index, request_options=request_options)
        return _response.data
