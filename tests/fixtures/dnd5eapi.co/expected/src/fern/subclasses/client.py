

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_reference_list import ApiReferenceList
from ..types.subclass import Subclass
from ..types.subclass_level import SubclassLevel
from ..types.subclass_level_resource import SubclassLevelResource
from .raw_client import AsyncRawSubclassesClient, RawSubclassesClient
from .types.get_api_subclasses_index_features_request_index import GetApiSubclassesIndexFeaturesRequestIndex
from .types.get_api_subclasses_index_levels_request_index import GetApiSubclassesIndexLevelsRequestIndex
from .types.get_api_subclasses_index_levels_subclass_level_features_request_index import (
    GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex,
)
from .types.get_api_subclasses_index_levels_subclass_level_request_index import (
    GetApiSubclassesIndexLevelsSubclassLevelRequestIndex,
)
from .types.get_api_subclasses_index_request_index import GetApiSubclassesIndexRequestIndex


class SubclassesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSubclassesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSubclassesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSubclassesClient
        """
        return self._raw_client

    def get_a_subclass_by_index(
        self, index: GetApiSubclassesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Subclass:
        """
        Subclasses reflect the different paths a class may take as levels are gained.

        Parameters
        ----------
        index : GetApiSubclassesIndexRequestIndex
            The `index` of the subclass to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Subclass
            OK

        Examples
        --------
        from fern.subclasses import GetApiSubclassesIndexRequestIndex

        from fern import FernApi

        client = FernApi()
        client.subclasses.get_a_subclass_by_index(
            index=GetApiSubclassesIndexRequestIndex.BERSERKER,
        )
        """
        _response = self._raw_client.get_a_subclass_by_index(index, request_options=request_options)
        return _response.data

    def get_features_available_for_a_subclass(
        self,
        index: GetApiSubclassesIndexFeaturesRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiSubclassesIndexFeaturesRequestIndex
            The `index` of the subclass to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            List of features for the subclass.

        Examples
        --------
        from fern.subclasses import GetApiSubclassesIndexFeaturesRequestIndex

        from fern import FernApi

        client = FernApi()
        client.subclasses.get_features_available_for_a_subclass(
            index=GetApiSubclassesIndexFeaturesRequestIndex.BERSERKER,
        )
        """
        _response = self._raw_client.get_features_available_for_a_subclass(index, request_options=request_options)
        return _response.data

    def get_all_level_resources_for_a_subclass(
        self, index: GetApiSubclassesIndexLevelsRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SubclassLevelResource]:
        """
        Parameters
        ----------
        index : GetApiSubclassesIndexLevelsRequestIndex
            The `index` of the subclass to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SubclassLevelResource]
            List of level resource for the subclass.

        Examples
        --------
        from fern.subclasses import GetApiSubclassesIndexLevelsRequestIndex

        from fern import FernApi

        client = FernApi()
        client.subclasses.get_all_level_resources_for_a_subclass(
            index=GetApiSubclassesIndexLevelsRequestIndex.BERSERKER,
        )
        """
        _response = self._raw_client.get_all_level_resources_for_a_subclass(index, request_options=request_options)
        return _response.data

    def get_level_resources_for_a_subclass_and_level(
        self,
        index: GetApiSubclassesIndexLevelsSubclassLevelRequestIndex,
        subclass_level: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubclassLevel:
        """
        Parameters
        ----------
        index : GetApiSubclassesIndexLevelsSubclassLevelRequestIndex
            The `index` of the subclass to get.

        subclass_level : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubclassLevel
            Level resource for the subclass and level.

        Examples
        --------
        from fern.subclasses import GetApiSubclassesIndexLevelsSubclassLevelRequestIndex

        from fern import FernApi

        client = FernApi()
        client.subclasses.get_level_resources_for_a_subclass_and_level(
            index=GetApiSubclassesIndexLevelsSubclassLevelRequestIndex.BERSERKER,
            subclass_level=1,
        )
        """
        _response = self._raw_client.get_level_resources_for_a_subclass_and_level(
            index, subclass_level, request_options=request_options
        )
        return _response.data

    def get_features_of_the_requested_spell_level_available_to_the_class(
        self,
        index: GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex,
        subclass_level: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex
            The `index` of the subclass to get.

        subclass_level : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            List of features for the subclass and level.

        Examples
        --------
        from fern.subclasses import (
            GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex,
        )

        from fern import FernApi

        client = FernApi()
        client.subclasses.get_features_of_the_requested_spell_level_available_to_the_class(
            index=GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex.BERSERKER,
            subclass_level=1,
        )
        """
        _response = self._raw_client.get_features_of_the_requested_spell_level_available_to_the_class(
            index, subclass_level, request_options=request_options
        )
        return _response.data


class AsyncSubclassesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSubclassesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSubclassesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSubclassesClient
        """
        return self._raw_client

    async def get_a_subclass_by_index(
        self, index: GetApiSubclassesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Subclass:
        """
        Subclasses reflect the different paths a class may take as levels are gained.

        Parameters
        ----------
        index : GetApiSubclassesIndexRequestIndex
            The `index` of the subclass to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Subclass
            OK

        Examples
        --------
        import asyncio

        from fern.subclasses import GetApiSubclassesIndexRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subclasses.get_a_subclass_by_index(
                index=GetApiSubclassesIndexRequestIndex.BERSERKER,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_subclass_by_index(index, request_options=request_options)
        return _response.data

    async def get_features_available_for_a_subclass(
        self,
        index: GetApiSubclassesIndexFeaturesRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiSubclassesIndexFeaturesRequestIndex
            The `index` of the subclass to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            List of features for the subclass.

        Examples
        --------
        import asyncio

        from fern.subclasses import GetApiSubclassesIndexFeaturesRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subclasses.get_features_available_for_a_subclass(
                index=GetApiSubclassesIndexFeaturesRequestIndex.BERSERKER,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_features_available_for_a_subclass(index, request_options=request_options)
        return _response.data

    async def get_all_level_resources_for_a_subclass(
        self, index: GetApiSubclassesIndexLevelsRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SubclassLevelResource]:
        """
        Parameters
        ----------
        index : GetApiSubclassesIndexLevelsRequestIndex
            The `index` of the subclass to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SubclassLevelResource]
            List of level resource for the subclass.

        Examples
        --------
        import asyncio

        from fern.subclasses import GetApiSubclassesIndexLevelsRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subclasses.get_all_level_resources_for_a_subclass(
                index=GetApiSubclassesIndexLevelsRequestIndex.BERSERKER,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_level_resources_for_a_subclass(
            index, request_options=request_options
        )
        return _response.data

    async def get_level_resources_for_a_subclass_and_level(
        self,
        index: GetApiSubclassesIndexLevelsSubclassLevelRequestIndex,
        subclass_level: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubclassLevel:
        """
        Parameters
        ----------
        index : GetApiSubclassesIndexLevelsSubclassLevelRequestIndex
            The `index` of the subclass to get.

        subclass_level : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubclassLevel
            Level resource for the subclass and level.

        Examples
        --------
        import asyncio

        from fern.subclasses import GetApiSubclassesIndexLevelsSubclassLevelRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subclasses.get_level_resources_for_a_subclass_and_level(
                index=GetApiSubclassesIndexLevelsSubclassLevelRequestIndex.BERSERKER,
                subclass_level=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_level_resources_for_a_subclass_and_level(
            index, subclass_level, request_options=request_options
        )
        return _response.data

    async def get_features_of_the_requested_spell_level_available_to_the_class(
        self,
        index: GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex,
        subclass_level: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex
            The `index` of the subclass to get.

        subclass_level : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            List of features for the subclass and level.

        Examples
        --------
        import asyncio

        from fern.subclasses import (
            GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subclasses.get_features_of_the_requested_spell_level_available_to_the_class(
                index=GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex.BERSERKER,
                subclass_level=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_features_of_the_requested_spell_level_available_to_the_class(
            index, subclass_level, request_options=request_options
        )
        return _response.data
