

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_reference_list import ApiReferenceList
from ..types.subrace import Subrace
from .raw_client import AsyncRawSubracesClient, RawSubracesClient
from .types.get_api_subraces_index_proficiencies_request_index import GetApiSubracesIndexProficienciesRequestIndex
from .types.get_api_subraces_index_request_index import GetApiSubracesIndexRequestIndex
from .types.get_api_subraces_index_traits_request_index import GetApiSubracesIndexTraitsRequestIndex


class SubracesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSubracesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSubracesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSubracesClient
        """
        return self._raw_client

    def get_a_subrace_by_index(
        self, index: GetApiSubracesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Subrace:
        """
        Subraces reflect the different varieties of a certain parent race.

        Parameters
        ----------
        index : GetApiSubracesIndexRequestIndex
            The `index` of the subrace to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Subrace
            OK

        Examples
        --------
        from fern.subraces import GetApiSubracesIndexRequestIndex

        from fern import FernApi

        client = FernApi()
        client.subraces.get_a_subrace_by_index(
            index=GetApiSubracesIndexRequestIndex.HIGH_ELF,
        )
        """
        _response = self._raw_client.get_a_subrace_by_index(index, request_options=request_options)
        return _response.data

    def get_proficiences_available_for_a_subrace(
        self,
        index: GetApiSubracesIndexProficienciesRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiSubracesIndexProficienciesRequestIndex
            The `index` of the subrace to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            List of proficiences for the subrace.

        Examples
        --------
        from fern.subraces import GetApiSubracesIndexProficienciesRequestIndex

        from fern import FernApi

        client = FernApi()
        client.subraces.get_proficiences_available_for_a_subrace(
            index=GetApiSubracesIndexProficienciesRequestIndex.HIGH_ELF,
        )
        """
        _response = self._raw_client.get_proficiences_available_for_a_subrace(index, request_options=request_options)
        return _response.data

    def get_traits_available_for_a_subrace(
        self, index: GetApiSubracesIndexTraitsRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiSubracesIndexTraitsRequestIndex
            The `index` of the subrace to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            List of traits for the subrace.

        Examples
        --------
        from fern.subraces import GetApiSubracesIndexTraitsRequestIndex

        from fern import FernApi

        client = FernApi()
        client.subraces.get_traits_available_for_a_subrace(
            index=GetApiSubracesIndexTraitsRequestIndex.HIGH_ELF,
        )
        """
        _response = self._raw_client.get_traits_available_for_a_subrace(index, request_options=request_options)
        return _response.data


class AsyncSubracesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSubracesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSubracesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSubracesClient
        """
        return self._raw_client

    async def get_a_subrace_by_index(
        self, index: GetApiSubracesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Subrace:
        """
        Subraces reflect the different varieties of a certain parent race.

        Parameters
        ----------
        index : GetApiSubracesIndexRequestIndex
            The `index` of the subrace to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Subrace
            OK

        Examples
        --------
        import asyncio

        from fern.subraces import GetApiSubracesIndexRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subraces.get_a_subrace_by_index(
                index=GetApiSubracesIndexRequestIndex.HIGH_ELF,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_subrace_by_index(index, request_options=request_options)
        return _response.data

    async def get_proficiences_available_for_a_subrace(
        self,
        index: GetApiSubracesIndexProficienciesRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiSubracesIndexProficienciesRequestIndex
            The `index` of the subrace to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            List of proficiences for the subrace.

        Examples
        --------
        import asyncio

        from fern.subraces import GetApiSubracesIndexProficienciesRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subraces.get_proficiences_available_for_a_subrace(
                index=GetApiSubracesIndexProficienciesRequestIndex.HIGH_ELF,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_proficiences_available_for_a_subrace(
            index, request_options=request_options
        )
        return _response.data

    async def get_traits_available_for_a_subrace(
        self, index: GetApiSubracesIndexTraitsRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiSubracesIndexTraitsRequestIndex
            The `index` of the subrace to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            List of traits for the subrace.

        Examples
        --------
        import asyncio

        from fern.subraces import GetApiSubracesIndexTraitsRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subraces.get_traits_available_for_a_subrace(
                index=GetApiSubracesIndexTraitsRequestIndex.HIGH_ELF,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_traits_available_for_a_subrace(index, request_options=request_options)
        return _response.data
