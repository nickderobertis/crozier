

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_reference_list import ApiReferenceList
from ..types.spell import Spell
from .raw_client import AsyncRawSpellsClient, RawSpellsClient


class SpellsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSpellsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSpellsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSpellsClient
        """
        return self._raw_client

    def get_list_of_spells_with_optional_filtering(
        self,
        *,
        level: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        school: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        level : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            The level or levels to filter on.

        school : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The magic school or schools to filter on.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.spells.get_list_of_spells_with_optional_filtering()
        """
        _response = self._raw_client.get_list_of_spells_with_optional_filtering(
            level=level, school=school, request_options=request_options
        )
        return _response.data

    def get_a_spell_by_index(self, index: str, *, request_options: typing.Optional[RequestOptions] = None) -> Spell:
        """
        Parameters
        ----------
        index : str
            The `index` of the `Spell` to get.

            Available values can be found in the [`ResourceList`](#get-/api/-endpoint-) for `spells`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Spell
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.spells.get_a_spell_by_index(
            index="sacred-flame",
        )
        """
        _response = self._raw_client.get_a_spell_by_index(index, request_options=request_options)
        return _response.data


class AsyncSpellsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSpellsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSpellsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSpellsClient
        """
        return self._raw_client

    async def get_list_of_spells_with_optional_filtering(
        self,
        *,
        level: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        school: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiReferenceList:
        """
        Parameters
        ----------
        level : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            The level or levels to filter on.

        school : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The magic school or schools to filter on.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.spells.get_list_of_spells_with_optional_filtering()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_list_of_spells_with_optional_filtering(
            level=level, school=school, request_options=request_options
        )
        return _response.data

    async def get_a_spell_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Spell:
        """
        Parameters
        ----------
        index : str
            The `index` of the `Spell` to get.

            Available values can be found in the [`ResourceList`](#get-/api/-endpoint-) for `spells`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Spell
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.spells.get_a_spell_by_index(
                index="sacred-flame",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_spell_by_index(index, request_options=request_options)
        return _response.data
