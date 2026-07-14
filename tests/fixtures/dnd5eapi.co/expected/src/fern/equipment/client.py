

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.equipment import Equipment
from ..types.equipment_category import EquipmentCategory
from ..types.magic_item import MagicItem
from ..types.weapon_property import WeaponProperty
from .raw_client import AsyncRawEquipmentClient, RawEquipmentClient
from .types.get_api_weapon_properties_index_request_index import GetApiWeaponPropertiesIndexRequestIndex


class EquipmentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEquipmentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEquipmentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEquipmentClient
        """
        return self._raw_client

    def get_an_equipment_category_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EquipmentCategory:
        """
        These are the categories that various equipment fall under.

        Parameters
        ----------
        index : str
            The `index` of the equipment category score to get.

            Available values can be found in the resource list for this endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EquipmentCategory
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equipment.get_an_equipment_category_by_index(
            index="waterborne-vehicles",
        )
        """
        _response = self._raw_client.get_an_equipment_category_by_index(index, request_options=request_options)
        return _response.data

    def get_an_equipment_item_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Equipment:
        """
        # Equipment

        Opportunities abound to find treasure, equipment, weapons, armor, and more
        in the dungeons you explore. Normally, you can sell your treasures and
        trinkets when you return to a town or other settlement, provided that you
        can find buyers and merchants interested in your loot.

        Parameters
        ----------
        index : str
            The `index` of the equipment to get.

            Available values can be found in the [`ResourceList`](#get-/api/-endpoint-) for `equipment`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Equipment
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equipment.get_an_equipment_item_by_index(
            index="club",
        )
        """
        _response = self._raw_client.get_an_equipment_item_by_index(index, request_options=request_options)
        return _response.data

    def get_a_magic_item_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MagicItem:
        """
        These are the various magic items you can find in the game.

        Parameters
        ----------
        index : str
            The `index` of the magic item to get.

            Available values can be found in the resource list for this endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MagicItem
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equipment.get_a_magic_item_by_index(
            index="adamantine-armor",
        )
        """
        _response = self._raw_client.get_a_magic_item_by_index(index, request_options=request_options)
        return _response.data

    def get_a_weapon_property_by_index(
        self, index: GetApiWeaponPropertiesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WeaponProperty:
        """
        Parameters
        ----------
        index : GetApiWeaponPropertiesIndexRequestIndex
            The `index` of the weapon property to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WeaponProperty
            OK

        Examples
        --------
        from fern.equipment import GetApiWeaponPropertiesIndexRequestIndex

        from fern import FernApi

        client = FernApi()
        client.equipment.get_a_weapon_property_by_index(
            index=GetApiWeaponPropertiesIndexRequestIndex.AMMUNITION,
        )
        """
        _response = self._raw_client.get_a_weapon_property_by_index(index, request_options=request_options)
        return _response.data


class AsyncEquipmentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEquipmentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEquipmentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEquipmentClient
        """
        return self._raw_client

    async def get_an_equipment_category_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EquipmentCategory:
        """
        These are the categories that various equipment fall under.

        Parameters
        ----------
        index : str
            The `index` of the equipment category score to get.

            Available values can be found in the resource list for this endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EquipmentCategory
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.equipment.get_an_equipment_category_by_index(
                index="waterborne-vehicles",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_an_equipment_category_by_index(index, request_options=request_options)
        return _response.data

    async def get_an_equipment_item_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Equipment:
        """
        # Equipment

        Opportunities abound to find treasure, equipment, weapons, armor, and more
        in the dungeons you explore. Normally, you can sell your treasures and
        trinkets when you return to a town or other settlement, provided that you
        can find buyers and merchants interested in your loot.

        Parameters
        ----------
        index : str
            The `index` of the equipment to get.

            Available values can be found in the [`ResourceList`](#get-/api/-endpoint-) for `equipment`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Equipment
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.equipment.get_an_equipment_item_by_index(
                index="club",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_an_equipment_item_by_index(index, request_options=request_options)
        return _response.data

    async def get_a_magic_item_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MagicItem:
        """
        These are the various magic items you can find in the game.

        Parameters
        ----------
        index : str
            The `index` of the magic item to get.

            Available values can be found in the resource list for this endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MagicItem
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.equipment.get_a_magic_item_by_index(
                index="adamantine-armor",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_magic_item_by_index(index, request_options=request_options)
        return _response.data

    async def get_a_weapon_property_by_index(
        self, index: GetApiWeaponPropertiesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WeaponProperty:
        """
        Parameters
        ----------
        index : GetApiWeaponPropertiesIndexRequestIndex
            The `index` of the weapon property to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WeaponProperty
            OK

        Examples
        --------
        import asyncio

        from fern.equipment import GetApiWeaponPropertiesIndexRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.equipment.get_a_weapon_property_by_index(
                index=GetApiWeaponPropertiesIndexRequestIndex.AMMUNITION,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_weapon_property_by_index(index, request_options=request_options)
        return _response.data
