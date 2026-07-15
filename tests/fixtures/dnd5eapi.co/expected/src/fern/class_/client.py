

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.class_ import Class
from ..types.multiclassing import Multiclassing
from ..types.spellcasting import Spellcasting
from .raw_client import AsyncRawClassClient, RawClassClient
from .types.get_api_classes_index_multi_classing_request_index import GetApiClassesIndexMultiClassingRequestIndex
from .types.get_api_classes_index_request_index import GetApiClassesIndexRequestIndex
from .types.get_api_classes_index_spellcasting_request_index import GetApiClassesIndexSpellcastingRequestIndex


class ClassClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClassClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClassClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClassClient
        """
        return self._raw_client

    def get_a_class_by_index(
        self, index: GetApiClassesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Class:
        """
        # Class

        A character class is a fundamental part of the identity and nature of
        characters in the Dungeons & Dragons role-playing game. A character's
        capabilities, strengths, and weaknesses are largely defined by its class.
        A character's class affects a character's available skills and abilities. [[SRD p8-55](https://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf#page=8)]

        Parameters
        ----------
        index : GetApiClassesIndexRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Class
            OK

        Examples
        --------
        from fern.class_ import GetApiClassesIndexRequestIndex

        from fern import FernApi

        client = FernApi()
        client.class_.get_a_class_by_index(
            index=GetApiClassesIndexRequestIndex.BARBARIAN,
        )
        """
        _response = self._raw_client.get_a_class_by_index(index, request_options=request_options)
        return _response.data

    def get_multiclassing_resource_for_a_class(
        self,
        index: GetApiClassesIndexMultiClassingRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Multiclassing:
        """
        Parameters
        ----------
        index : GetApiClassesIndexMultiClassingRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Multiclassing
            OK

        Examples
        --------
        from fern.class_ import GetApiClassesIndexMultiClassingRequestIndex

        from fern import FernApi

        client = FernApi()
        client.class_.get_multiclassing_resource_for_a_class(
            index=GetApiClassesIndexMultiClassingRequestIndex.BARBARIAN,
        )
        """
        _response = self._raw_client.get_multiclassing_resource_for_a_class(index, request_options=request_options)
        return _response.data

    def get_spellcasting_info_for_a_class(
        self,
        index: GetApiClassesIndexSpellcastingRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Spellcasting:
        """
        Parameters
        ----------
        index : GetApiClassesIndexSpellcastingRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Spellcasting
            OK

        Examples
        --------
        from fern.class_ import GetApiClassesIndexSpellcastingRequestIndex

        from fern import FernApi

        client = FernApi()
        client.class_.get_spellcasting_info_for_a_class(
            index=GetApiClassesIndexSpellcastingRequestIndex.BARBARIAN,
        )
        """
        _response = self._raw_client.get_spellcasting_info_for_a_class(index, request_options=request_options)
        return _response.data


class AsyncClassClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClassClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClassClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClassClient
        """
        return self._raw_client

    async def get_a_class_by_index(
        self, index: GetApiClassesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Class:
        """
        # Class

        A character class is a fundamental part of the identity and nature of
        characters in the Dungeons & Dragons role-playing game. A character's
        capabilities, strengths, and weaknesses are largely defined by its class.
        A character's class affects a character's available skills and abilities. [[SRD p8-55](https://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf#page=8)]

        Parameters
        ----------
        index : GetApiClassesIndexRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Class
            OK

        Examples
        --------
        import asyncio

        from fern.class_ import GetApiClassesIndexRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.class_.get_a_class_by_index(
                index=GetApiClassesIndexRequestIndex.BARBARIAN,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_class_by_index(index, request_options=request_options)
        return _response.data

    async def get_multiclassing_resource_for_a_class(
        self,
        index: GetApiClassesIndexMultiClassingRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Multiclassing:
        """
        Parameters
        ----------
        index : GetApiClassesIndexMultiClassingRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Multiclassing
            OK

        Examples
        --------
        import asyncio

        from fern.class_ import GetApiClassesIndexMultiClassingRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.class_.get_multiclassing_resource_for_a_class(
                index=GetApiClassesIndexMultiClassingRequestIndex.BARBARIAN,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_multiclassing_resource_for_a_class(
            index, request_options=request_options
        )
        return _response.data

    async def get_spellcasting_info_for_a_class(
        self,
        index: GetApiClassesIndexSpellcastingRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Spellcasting:
        """
        Parameters
        ----------
        index : GetApiClassesIndexSpellcastingRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Spellcasting
            OK

        Examples
        --------
        import asyncio

        from fern.class_ import GetApiClassesIndexSpellcastingRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.class_.get_spellcasting_info_for_a_class(
                index=GetApiClassesIndexSpellcastingRequestIndex.BARBARIAN,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_spellcasting_info_for_a_class(index, request_options=request_options)
        return _response.data
