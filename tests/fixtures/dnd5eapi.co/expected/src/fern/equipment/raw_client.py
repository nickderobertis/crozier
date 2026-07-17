

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.equipment import Equipment
from ..types.equipment_category import EquipmentCategory
from ..types.magic_item import MagicItem
from ..types.weapon_property import WeaponProperty
from .types.get_api_weapon_properties_index_request_index import GetApiWeaponPropertiesIndexRequestIndex
from pydantic import ValidationError


class RawEquipmentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_an_equipment_category_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EquipmentCategory]:
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
        HttpResponse[EquipmentCategory]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/equipment-categories/{encode_path_param(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EquipmentCategory,
                    parse_obj_as(
                        type_=EquipmentCategory,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_an_equipment_item_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Equipment]:
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
        HttpResponse[Equipment]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/equipment/{encode_path_param(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Equipment,
                    parse_obj_as(
                        type_=Equipment,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_a_magic_item_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MagicItem]:
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
        HttpResponse[MagicItem]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/magic-items/{encode_path_param(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MagicItem,
                    parse_obj_as(
                        type_=MagicItem,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_a_weapon_property_by_index(
        self, index: GetApiWeaponPropertiesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WeaponProperty]:
        """
        Parameters
        ----------
        index : GetApiWeaponPropertiesIndexRequestIndex
            The `index` of the weapon property to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WeaponProperty]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/weapon-properties/{encode_path_param(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WeaponProperty,
                    parse_obj_as(
                        type_=WeaponProperty,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawEquipmentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_an_equipment_category_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EquipmentCategory]:
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
        AsyncHttpResponse[EquipmentCategory]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/equipment-categories/{encode_path_param(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EquipmentCategory,
                    parse_obj_as(
                        type_=EquipmentCategory,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_an_equipment_item_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Equipment]:
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
        AsyncHttpResponse[Equipment]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/equipment/{encode_path_param(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Equipment,
                    parse_obj_as(
                        type_=Equipment,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_a_magic_item_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MagicItem]:
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
        AsyncHttpResponse[MagicItem]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/magic-items/{encode_path_param(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MagicItem,
                    parse_obj_as(
                        type_=MagicItem,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_a_weapon_property_by_index(
        self, index: GetApiWeaponPropertiesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WeaponProperty]:
        """
        Parameters
        ----------
        index : GetApiWeaponPropertiesIndexRequestIndex
            The `index` of the weapon property to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WeaponProperty]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/weapon-properties/{encode_path_param(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WeaponProperty,
                    parse_obj_as(
                        type_=WeaponProperty,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
