

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.condition import Condition
from ..types.damage_type import DamageType
from ..types.magic_school import MagicSchool
from .raw_client import AsyncRawGameMechanicsClient, RawGameMechanicsClient
from .types.get_api_conditions_index_request_index import GetApiConditionsIndexRequestIndex
from .types.get_api_damage_types_index_request_index import GetApiDamageTypesIndexRequestIndex
from .types.get_api_magic_schools_index_request_index import GetApiMagicSchoolsIndexRequestIndex


class GameMechanicsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGameMechanicsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGameMechanicsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGameMechanicsClient
        """
        return self._raw_client

    def get_a_condition_by_index(
        self, index: GetApiConditionsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Condition:
        """
        # Condition

        A condition alters a creature’s capabilities in a variety of ways and can
        arise as a result of a spell, a class feature, a monster’s attack, or other
        effect. Most conditions, such as blinded, are impairments, but a few, such
        as invisible, can be advantageous.

        Parameters
        ----------
        index : GetApiConditionsIndexRequestIndex
            The `index` of the condition to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Condition
            OK

        Examples
        --------
        from fern.game_mechanics import GetApiConditionsIndexRequestIndex

        from fern import FernApi

        client = FernApi()
        client.game_mechanics.get_a_condition_by_index(
            index=GetApiConditionsIndexRequestIndex.BLINDED,
        )
        """
        _response = self._raw_client.get_a_condition_by_index(index, request_options=request_options)
        return _response.data

    def get_a_damage_type_by_index(
        self, index: GetApiDamageTypesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DamageType:
        """
        # Damage type

        Different attacks, damaging spells, and other harmful effects deal different
        types of damage. Damage types have no rules of their own, but other rules,
        such as damage resistance, rely on the types.

        Parameters
        ----------
        index : GetApiDamageTypesIndexRequestIndex
            The `index` of the damage type to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DamageType
            OK

        Examples
        --------
        from fern.game_mechanics import GetApiDamageTypesIndexRequestIndex

        from fern import FernApi

        client = FernApi()
        client.game_mechanics.get_a_damage_type_by_index(
            index=GetApiDamageTypesIndexRequestIndex.ACID,
        )
        """
        _response = self._raw_client.get_a_damage_type_by_index(index, request_options=request_options)
        return _response.data

    def get_a_magic_school_by_index(
        self, index: GetApiMagicSchoolsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MagicSchool:
        """
        # Magic School

        Academies of magic group spells into eight categories called schools of
        magic. Scholars, particularly wizards, apply these categories to all spells,
        believing that all magic functions in essentially the same way, whether it
        derives from rigorous study or is bestowed by a deity.

        Parameters
        ----------
        index : GetApiMagicSchoolsIndexRequestIndex
            The `index` of the magic school to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MagicSchool
            OK

        Examples
        --------
        from fern.game_mechanics import GetApiMagicSchoolsIndexRequestIndex

        from fern import FernApi

        client = FernApi()
        client.game_mechanics.get_a_magic_school_by_index(
            index=GetApiMagicSchoolsIndexRequestIndex.ABJURATION,
        )
        """
        _response = self._raw_client.get_a_magic_school_by_index(index, request_options=request_options)
        return _response.data


class AsyncGameMechanicsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGameMechanicsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGameMechanicsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGameMechanicsClient
        """
        return self._raw_client

    async def get_a_condition_by_index(
        self, index: GetApiConditionsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Condition:
        """
        # Condition

        A condition alters a creature’s capabilities in a variety of ways and can
        arise as a result of a spell, a class feature, a monster’s attack, or other
        effect. Most conditions, such as blinded, are impairments, but a few, such
        as invisible, can be advantageous.

        Parameters
        ----------
        index : GetApiConditionsIndexRequestIndex
            The `index` of the condition to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Condition
            OK

        Examples
        --------
        import asyncio

        from fern.game_mechanics import GetApiConditionsIndexRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.game_mechanics.get_a_condition_by_index(
                index=GetApiConditionsIndexRequestIndex.BLINDED,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_condition_by_index(index, request_options=request_options)
        return _response.data

    async def get_a_damage_type_by_index(
        self, index: GetApiDamageTypesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DamageType:
        """
        # Damage type

        Different attacks, damaging spells, and other harmful effects deal different
        types of damage. Damage types have no rules of their own, but other rules,
        such as damage resistance, rely on the types.

        Parameters
        ----------
        index : GetApiDamageTypesIndexRequestIndex
            The `index` of the damage type to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DamageType
            OK

        Examples
        --------
        import asyncio

        from fern.game_mechanics import GetApiDamageTypesIndexRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.game_mechanics.get_a_damage_type_by_index(
                index=GetApiDamageTypesIndexRequestIndex.ACID,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_damage_type_by_index(index, request_options=request_options)
        return _response.data

    async def get_a_magic_school_by_index(
        self, index: GetApiMagicSchoolsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MagicSchool:
        """
        # Magic School

        Academies of magic group spells into eight categories called schools of
        magic. Scholars, particularly wizards, apply these categories to all spells,
        believing that all magic functions in essentially the same way, whether it
        derives from rigorous study or is bestowed by a deity.

        Parameters
        ----------
        index : GetApiMagicSchoolsIndexRequestIndex
            The `index` of the magic school to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MagicSchool
            OK

        Examples
        --------
        import asyncio

        from fern.game_mechanics import GetApiMagicSchoolsIndexRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.game_mechanics.get_a_magic_school_by_index(
                index=GetApiMagicSchoolsIndexRequestIndex.ABJURATION,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_magic_school_by_index(index, request_options=request_options)
        return _response.data
