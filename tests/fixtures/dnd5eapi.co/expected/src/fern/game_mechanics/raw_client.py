

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.condition import Condition
from ..types.damage_type import DamageType
from ..types.magic_school import MagicSchool
from .types.get_api_conditions_index_request_index import GetApiConditionsIndexRequestIndex
from .types.get_api_damage_types_index_request_index import GetApiDamageTypesIndexRequestIndex
from .types.get_api_magic_schools_index_request_index import GetApiMagicSchoolsIndexRequestIndex


class RawGameMechanicsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_a_condition_by_index(
        self, index: GetApiConditionsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Condition]:
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
        HttpResponse[Condition]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/conditions/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Condition,
                    parse_obj_as(
                        type_=Condition,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_a_damage_type_by_index(
        self, index: GetApiDamageTypesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DamageType]:
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
        HttpResponse[DamageType]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/damage-types/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DamageType,
                    parse_obj_as(
                        type_=DamageType,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_a_magic_school_by_index(
        self, index: GetApiMagicSchoolsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MagicSchool]:
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
        HttpResponse[MagicSchool]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/magic-schools/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MagicSchool,
                    parse_obj_as(
                        type_=MagicSchool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawGameMechanicsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_a_condition_by_index(
        self, index: GetApiConditionsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Condition]:
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
        AsyncHttpResponse[Condition]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/conditions/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Condition,
                    parse_obj_as(
                        type_=Condition,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_a_damage_type_by_index(
        self, index: GetApiDamageTypesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DamageType]:
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
        AsyncHttpResponse[DamageType]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/damage-types/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DamageType,
                    parse_obj_as(
                        type_=DamageType,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_a_magic_school_by_index(
        self, index: GetApiMagicSchoolsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MagicSchool]:
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
        AsyncHttpResponse[MagicSchool]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/magic-schools/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MagicSchool,
                    parse_obj_as(
                        type_=MagicSchool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
