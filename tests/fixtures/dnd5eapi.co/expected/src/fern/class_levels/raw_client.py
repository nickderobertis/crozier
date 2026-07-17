

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_reference_list import ApiReferenceList
from ..types.class_level import ClassLevel
from .types.get_api_classes_index_levels_class_level_features_request_index import (
    GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex,
)
from .types.get_api_classes_index_levels_class_level_request_index import GetApiClassesIndexLevelsClassLevelRequestIndex
from .types.get_api_classes_index_levels_request_index import GetApiClassesIndexLevelsRequestIndex
from .types.get_api_classes_index_levels_spell_level_spells_request_index import (
    GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex,
)
from pydantic import ValidationError


class RawClassLevelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_all_level_resources_for_a_class(
        self,
        index: GetApiClassesIndexLevelsRequestIndex,
        *,
        subclass: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ClassLevel]]:
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
        HttpResponse[typing.List[ClassLevel]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/classes/{encode_path_param(index)}/levels",
            method="GET",
            params={
                "subclass": subclass,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ClassLevel],
                    parse_obj_as(
                        type_=typing.List[ClassLevel],
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

    def get_level_resource_for_a_class_and_level(
        self,
        index: GetApiClassesIndexLevelsClassLevelRequestIndex,
        class_level: float,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ClassLevel]:
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
        HttpResponse[ClassLevel]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/classes/{encode_path_param(index)}/levels/{encode_path_param(class_level)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClassLevel,
                    parse_obj_as(
                        type_=ClassLevel,
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

    def get_features_available_to_a_class_at_the_requested_level(
        self,
        index: GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex,
        class_level: float,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiReferenceList]:
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
        HttpResponse[ApiReferenceList]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/classes/{encode_path_param(index)}/levels/{encode_path_param(class_level)}/features",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiReferenceList,
                    parse_obj_as(
                        type_=ApiReferenceList,
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

    def get_spells_of_the_requested_level_available_to_the_class(
        self,
        index: GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex,
        spell_level: float,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiReferenceList]:
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
        HttpResponse[ApiReferenceList]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/classes/{encode_path_param(index)}/levels/{encode_path_param(spell_level)}/spells",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiReferenceList,
                    parse_obj_as(
                        type_=ApiReferenceList,
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


class AsyncRawClassLevelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_all_level_resources_for_a_class(
        self,
        index: GetApiClassesIndexLevelsRequestIndex,
        *,
        subclass: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ClassLevel]]:
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
        AsyncHttpResponse[typing.List[ClassLevel]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/classes/{encode_path_param(index)}/levels",
            method="GET",
            params={
                "subclass": subclass,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ClassLevel],
                    parse_obj_as(
                        type_=typing.List[ClassLevel],
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

    async def get_level_resource_for_a_class_and_level(
        self,
        index: GetApiClassesIndexLevelsClassLevelRequestIndex,
        class_level: float,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ClassLevel]:
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
        AsyncHttpResponse[ClassLevel]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/classes/{encode_path_param(index)}/levels/{encode_path_param(class_level)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClassLevel,
                    parse_obj_as(
                        type_=ClassLevel,
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

    async def get_features_available_to_a_class_at_the_requested_level(
        self,
        index: GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex,
        class_level: float,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiReferenceList]:
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
        AsyncHttpResponse[ApiReferenceList]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/classes/{encode_path_param(index)}/levels/{encode_path_param(class_level)}/features",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiReferenceList,
                    parse_obj_as(
                        type_=ApiReferenceList,
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

    async def get_spells_of_the_requested_level_available_to_the_class(
        self,
        index: GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex,
        spell_level: float,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiReferenceList]:
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
        AsyncHttpResponse[ApiReferenceList]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/classes/{encode_path_param(index)}/levels/{encode_path_param(spell_level)}/spells",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiReferenceList,
                    parse_obj_as(
                        type_=ApiReferenceList,
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
