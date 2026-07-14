

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_reference_list import ApiReferenceList
from ..types.race import Race
from .raw_client import AsyncRawRacesClient, RawRacesClient
from .types.get_api_races_index_proficiencies_request_index import GetApiRacesIndexProficienciesRequestIndex
from .types.get_api_races_index_request_index import GetApiRacesIndexRequestIndex
from .types.get_api_races_index_subraces_request_index import GetApiRacesIndexSubracesRequestIndex
from .types.get_api_races_index_traits_request_index import GetApiRacesIndexTraitsRequestIndex


class RacesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRacesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRacesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRacesClient
        """
        return self._raw_client

    def get_a_race_by_index(
        self, index: GetApiRacesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Race:
        """
        Each race grants your character ability and skill bonuses as well as racial traits.

        Parameters
        ----------
        index : GetApiRacesIndexRequestIndex
            The `index` of the race to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Race
            OK

        Examples
        --------
        from fern.races import GetApiRacesIndexRequestIndex

        from fern import FernApi

        client = FernApi()
        client.races.get_a_race_by_index(
            index=GetApiRacesIndexRequestIndex.DRAGONBORN,
        )
        """
        _response = self._raw_client.get_a_race_by_index(index, request_options=request_options)
        return _response.data

    def get_proficiencies_available_for_a_race(
        self,
        index: GetApiRacesIndexProficienciesRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiRacesIndexProficienciesRequestIndex
            The `index` of the race to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            List of proficiencies for the race.

        Examples
        --------
        from fern.races import GetApiRacesIndexProficienciesRequestIndex

        from fern import FernApi

        client = FernApi()
        client.races.get_proficiencies_available_for_a_race(
            index=GetApiRacesIndexProficienciesRequestIndex.DRAGONBORN,
        )
        """
        _response = self._raw_client.get_proficiencies_available_for_a_race(index, request_options=request_options)
        return _response.data

    def get_subraces_available_for_a_race(
        self, index: GetApiRacesIndexSubracesRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiRacesIndexSubracesRequestIndex
            The `index` of the race to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            List of subraces for the race.

        Examples
        --------
        from fern.races import GetApiRacesIndexSubracesRequestIndex

        from fern import FernApi

        client = FernApi()
        client.races.get_subraces_available_for_a_race(
            index=GetApiRacesIndexSubracesRequestIndex.DRAGONBORN,
        )
        """
        _response = self._raw_client.get_subraces_available_for_a_race(index, request_options=request_options)
        return _response.data

    def get_traits_available_for_a_race(
        self, index: GetApiRacesIndexTraitsRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiRacesIndexTraitsRequestIndex
            The `index` of the race to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            List of traits for the race.

        Examples
        --------
        from fern.races import GetApiRacesIndexTraitsRequestIndex

        from fern import FernApi

        client = FernApi()
        client.races.get_traits_available_for_a_race(
            index=GetApiRacesIndexTraitsRequestIndex.DRAGONBORN,
        )
        """
        _response = self._raw_client.get_traits_available_for_a_race(index, request_options=request_options)
        return _response.data


class AsyncRacesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRacesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRacesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRacesClient
        """
        return self._raw_client

    async def get_a_race_by_index(
        self, index: GetApiRacesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Race:
        """
        Each race grants your character ability and skill bonuses as well as racial traits.

        Parameters
        ----------
        index : GetApiRacesIndexRequestIndex
            The `index` of the race to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Race
            OK

        Examples
        --------
        import asyncio

        from fern.races import GetApiRacesIndexRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.races.get_a_race_by_index(
                index=GetApiRacesIndexRequestIndex.DRAGONBORN,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_race_by_index(index, request_options=request_options)
        return _response.data

    async def get_proficiencies_available_for_a_race(
        self,
        index: GetApiRacesIndexProficienciesRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiRacesIndexProficienciesRequestIndex
            The `index` of the race to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            List of proficiencies for the race.

        Examples
        --------
        import asyncio

        from fern.races import GetApiRacesIndexProficienciesRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.races.get_proficiencies_available_for_a_race(
                index=GetApiRacesIndexProficienciesRequestIndex.DRAGONBORN,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_proficiencies_available_for_a_race(
            index, request_options=request_options
        )
        return _response.data

    async def get_subraces_available_for_a_race(
        self, index: GetApiRacesIndexSubracesRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiRacesIndexSubracesRequestIndex
            The `index` of the race to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            List of subraces for the race.

        Examples
        --------
        import asyncio

        from fern.races import GetApiRacesIndexSubracesRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.races.get_subraces_available_for_a_race(
                index=GetApiRacesIndexSubracesRequestIndex.DRAGONBORN,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_subraces_available_for_a_race(index, request_options=request_options)
        return _response.data

    async def get_traits_available_for_a_race(
        self, index: GetApiRacesIndexTraitsRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        index : GetApiRacesIndexTraitsRequestIndex
            The `index` of the race to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            List of traits for the race.

        Examples
        --------
        import asyncio

        from fern.races import GetApiRacesIndexTraitsRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.races.get_traits_available_for_a_race(
                index=GetApiRacesIndexTraitsRequestIndex.DRAGONBORN,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_traits_available_for_a_race(index, request_options=request_options)
        return _response.data
