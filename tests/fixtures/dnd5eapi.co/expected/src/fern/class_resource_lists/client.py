

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_reference_list import ApiReferenceList
from .raw_client import AsyncRawClassResourceListsClient, RawClassResourceListsClient
from .types.get_api_classes_index_features_request_index import GetApiClassesIndexFeaturesRequestIndex
from .types.get_api_classes_index_proficiencies_request_index import GetApiClassesIndexProficienciesRequestIndex
from .types.get_api_classes_index_spells_request_index import GetApiClassesIndexSpellsRequestIndex
from .types.get_api_classes_index_subclasses_request_index import GetApiClassesIndexSubclassesRequestIndex


class ClassResourceListsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClassResourceListsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClassResourceListsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClassResourceListsClient
        """
        return self._raw_client

    def get_features_available_for_a_class(
        self, index: GetApiClassesIndexFeaturesRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiClassesIndexFeaturesRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            List of features for the class.

        Examples
        --------
        from fern.class_resource_lists import GetApiClassesIndexFeaturesRequestIndex

        from fern import FernApi

        client = FernApi()
        client.class_resource_lists.get_features_available_for_a_class(
            index=GetApiClassesIndexFeaturesRequestIndex.BARBARIAN,
        )
        """
        _response = self._raw_client.get_features_available_for_a_class(index, request_options=request_options)
        return _response.data

    def get_proficiencies_available_for_a_class(
        self,
        index: GetApiClassesIndexProficienciesRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiClassesIndexProficienciesRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            List of proficiencies for the class.

        Examples
        --------
        from fern.class_resource_lists import (
            GetApiClassesIndexProficienciesRequestIndex,
        )

        from fern import FernApi

        client = FernApi()
        client.class_resource_lists.get_proficiencies_available_for_a_class(
            index=GetApiClassesIndexProficienciesRequestIndex.BARBARIAN,
        )
        """
        _response = self._raw_client.get_proficiencies_available_for_a_class(index, request_options=request_options)
        return _response.data

    def get_spells_available_for_a_class(
        self, index: GetApiClassesIndexSpellsRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiClassesIndexSpellsRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            OK

        Examples
        --------
        from fern.class_resource_lists import GetApiClassesIndexSpellsRequestIndex

        from fern import FernApi

        client = FernApi()
        client.class_resource_lists.get_spells_available_for_a_class(
            index=GetApiClassesIndexSpellsRequestIndex.BARBARIAN,
        )
        """
        _response = self._raw_client.get_spells_available_for_a_class(index, request_options=request_options)
        return _response.data

    def get_subclasses_available_for_a_class(
        self,
        index: GetApiClassesIndexSubclassesRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiClassesIndexSubclassesRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            OK

        Examples
        --------
        from fern.class_resource_lists import GetApiClassesIndexSubclassesRequestIndex

        from fern import FernApi

        client = FernApi()
        client.class_resource_lists.get_subclasses_available_for_a_class(
            index=GetApiClassesIndexSubclassesRequestIndex.BARBARIAN,
        )
        """
        _response = self._raw_client.get_subclasses_available_for_a_class(index, request_options=request_options)
        return _response.data


class AsyncClassResourceListsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClassResourceListsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClassResourceListsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClassResourceListsClient
        """
        return self._raw_client

    async def get_features_available_for_a_class(
        self, index: GetApiClassesIndexFeaturesRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiClassesIndexFeaturesRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            List of features for the class.

        Examples
        --------
        import asyncio

        from fern.class_resource_lists import GetApiClassesIndexFeaturesRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.class_resource_lists.get_features_available_for_a_class(
                index=GetApiClassesIndexFeaturesRequestIndex.BARBARIAN,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_features_available_for_a_class(index, request_options=request_options)
        return _response.data

    async def get_proficiencies_available_for_a_class(
        self,
        index: GetApiClassesIndexProficienciesRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiClassesIndexProficienciesRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            List of proficiencies for the class.

        Examples
        --------
        import asyncio

        from fern.class_resource_lists import (
            GetApiClassesIndexProficienciesRequestIndex,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.class_resource_lists.get_proficiencies_available_for_a_class(
                index=GetApiClassesIndexProficienciesRequestIndex.BARBARIAN,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_proficiencies_available_for_a_class(
            index, request_options=request_options
        )
        return _response.data

    async def get_spells_available_for_a_class(
        self, index: GetApiClassesIndexSpellsRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiClassesIndexSpellsRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            OK

        Examples
        --------
        import asyncio

        from fern.class_resource_lists import GetApiClassesIndexSpellsRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.class_resource_lists.get_spells_available_for_a_class(
                index=GetApiClassesIndexSpellsRequestIndex.BARBARIAN,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_spells_available_for_a_class(index, request_options=request_options)
        return _response.data

    async def get_subclasses_available_for_a_class(
        self,
        index: GetApiClassesIndexSubclassesRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiClassesIndexSubclassesRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            OK

        Examples
        --------
        import asyncio

        from fern.class_resource_lists import GetApiClassesIndexSubclassesRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.class_resource_lists.get_subclasses_available_for_a_class(
                index=GetApiClassesIndexSubclassesRequestIndex.BARBARIAN,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_subclasses_available_for_a_class(index, request_options=request_options)
        return _response.data
