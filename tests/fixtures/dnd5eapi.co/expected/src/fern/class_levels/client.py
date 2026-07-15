

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_reference_list import ApiReferenceList
from ..types.class_level import ClassLevel
from .raw_client import AsyncRawClassLevelsClient, RawClassLevelsClient
from .types.get_api_classes_index_levels_class_level_features_request_index import (
    GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex,
)
from .types.get_api_classes_index_levels_class_level_request_index import GetApiClassesIndexLevelsClassLevelRequestIndex
from .types.get_api_classes_index_levels_request_index import GetApiClassesIndexLevelsRequestIndex
from .types.get_api_classes_index_levels_spell_level_spells_request_index import (
    GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex,
)


class ClassLevelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClassLevelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClassLevelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClassLevelsClient
        """
        return self._raw_client

    def get_all_level_resources_for_a_class(
        self,
        index: GetApiClassesIndexLevelsRequestIndex,
        *,
        subclass: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ClassLevel]:
        """
        Parameters
        ----------
        index : GetApiClassesIndexLevelsRequestIndex
            The `index` of the class to get.

        subclass : typing.Optional[str]
            Adds subclasses for class to the response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ClassLevel]
            OK

        Examples
        --------
        from fern.class_levels import GetApiClassesIndexLevelsRequestIndex

        from fern import FernApi

        client = FernApi()
        client.class_levels.get_all_level_resources_for_a_class(
            index=GetApiClassesIndexLevelsRequestIndex.BARBARIAN,
            subclass="ber",
        )
        """
        _response = self._raw_client.get_all_level_resources_for_a_class(
            index, subclass=subclass, request_options=request_options
        )
        return _response.data

    def get_level_resource_for_a_class_and_level(
        self,
        index: GetApiClassesIndexLevelsClassLevelRequestIndex,
        class_level: float,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClassLevel:
        """
        Parameters
        ----------
        index : GetApiClassesIndexLevelsClassLevelRequestIndex
            The `index` of the class to get.

        class_level : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClassLevel
            OK

        Examples
        --------
        from fern.class_levels import GetApiClassesIndexLevelsClassLevelRequestIndex

        from fern import FernApi

        client = FernApi()
        client.class_levels.get_level_resource_for_a_class_and_level(
            index=GetApiClassesIndexLevelsClassLevelRequestIndex.BARBARIAN,
            class_level=3.0,
        )
        """
        _response = self._raw_client.get_level_resource_for_a_class_and_level(
            index, class_level, request_options=request_options
        )
        return _response.data

    def get_features_available_to_a_class_at_the_requested_level(
        self,
        index: GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex,
        class_level: float,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex
            The `index` of the class to get.

        class_level : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            OK

        Examples
        --------
        from fern.class_levels import (
            GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex,
        )

        from fern import FernApi

        client = FernApi()
        client.class_levels.get_features_available_to_a_class_at_the_requested_level(
            index=GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex.BARBARIAN,
            class_level=3.0,
        )
        """
        _response = self._raw_client.get_features_available_to_a_class_at_the_requested_level(
            index, class_level, request_options=request_options
        )
        return _response.data

    def get_spells_of_the_requested_level_available_to_the_class(
        self,
        index: GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex,
        spell_level: float,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex
            The `index` of the class to get.

        spell_level : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            OK

        Examples
        --------
        from fern.class_levels import (
            GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex,
        )

        from fern import FernApi

        client = FernApi()
        client.class_levels.get_spells_of_the_requested_level_available_to_the_class(
            index=GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex.BARBARIAN,
            spell_level=4.0,
        )
        """
        _response = self._raw_client.get_spells_of_the_requested_level_available_to_the_class(
            index, spell_level, request_options=request_options
        )
        return _response.data


class AsyncClassLevelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClassLevelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClassLevelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClassLevelsClient
        """
        return self._raw_client

    async def get_all_level_resources_for_a_class(
        self,
        index: GetApiClassesIndexLevelsRequestIndex,
        *,
        subclass: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ClassLevel]:
        """
        Parameters
        ----------
        index : GetApiClassesIndexLevelsRequestIndex
            The `index` of the class to get.

        subclass : typing.Optional[str]
            Adds subclasses for class to the response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ClassLevel]
            OK

        Examples
        --------
        import asyncio

        from fern.class_levels import GetApiClassesIndexLevelsRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.class_levels.get_all_level_resources_for_a_class(
                index=GetApiClassesIndexLevelsRequestIndex.BARBARIAN,
                subclass="ber",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_level_resources_for_a_class(
            index, subclass=subclass, request_options=request_options
        )
        return _response.data

    async def get_level_resource_for_a_class_and_level(
        self,
        index: GetApiClassesIndexLevelsClassLevelRequestIndex,
        class_level: float,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClassLevel:
        """
        Parameters
        ----------
        index : GetApiClassesIndexLevelsClassLevelRequestIndex
            The `index` of the class to get.

        class_level : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClassLevel
            OK

        Examples
        --------
        import asyncio

        from fern.class_levels import GetApiClassesIndexLevelsClassLevelRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.class_levels.get_level_resource_for_a_class_and_level(
                index=GetApiClassesIndexLevelsClassLevelRequestIndex.BARBARIAN,
                class_level=3.0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_level_resource_for_a_class_and_level(
            index, class_level, request_options=request_options
        )
        return _response.data

    async def get_features_available_to_a_class_at_the_requested_level(
        self,
        index: GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex,
        class_level: float,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex
            The `index` of the class to get.

        class_level : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            OK

        Examples
        --------
        import asyncio

        from fern.class_levels import (
            GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.class_levels.get_features_available_to_a_class_at_the_requested_level(
                index=GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex.BARBARIAN,
                class_level=3.0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_features_available_to_a_class_at_the_requested_level(
            index, class_level, request_options=request_options
        )
        return _response.data

    async def get_spells_of_the_requested_level_available_to_the_class(
        self,
        index: GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex,
        spell_level: float,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex
            The `index` of the class to get.

        spell_level : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            OK

        Examples
        --------
        import asyncio

        from fern.class_levels import (
            GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.class_levels.get_spells_of_the_requested_level_available_to_the_class(
                index=GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex.BARBARIAN,
                spell_level=4.0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_spells_of_the_requested_level_available_to_the_class(
            index, spell_level, request_options=request_options
        )
        return _response.data
