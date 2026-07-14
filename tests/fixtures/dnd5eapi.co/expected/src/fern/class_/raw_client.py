

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..types.class_ import Class
from ..types.error_response import ErrorResponse
from ..types.multiclassing import Multiclassing
from ..types.spellcasting import Spellcasting
from .types.get_api_classes_index_multi_classing_request_index import GetApiClassesIndexMultiClassingRequestIndex
from .types.get_api_classes_index_request_index import GetApiClassesIndexRequestIndex
from .types.get_api_classes_index_spellcasting_request_index import GetApiClassesIndexSpellcastingRequestIndex


class RawClassClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_a_class_by_index(
        self, index: GetApiClassesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Class]:
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
        HttpResponse[Class]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/classes/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Class,
                    parse_obj_as(
                        type_=Class,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_multiclassing_resource_for_a_class(
        self,
        index: GetApiClassesIndexMultiClassingRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Multiclassing]:
        """
        Parameters
        ----------
        index : GetApiClassesIndexMultiClassingRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Multiclassing]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/classes/{jsonable_encoder(index)}/multi-classing",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Multiclassing,
                    parse_obj_as(
                        type_=Multiclassing,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_spellcasting_info_for_a_class(
        self,
        index: GetApiClassesIndexSpellcastingRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Spellcasting]:
        """
        Parameters
        ----------
        index : GetApiClassesIndexSpellcastingRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Spellcasting]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/classes/{jsonable_encoder(index)}/spellcasting",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Spellcasting,
                    parse_obj_as(
                        type_=Spellcasting,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawClassClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_a_class_by_index(
        self, index: GetApiClassesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Class]:
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
        AsyncHttpResponse[Class]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/classes/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Class,
                    parse_obj_as(
                        type_=Class,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_multiclassing_resource_for_a_class(
        self,
        index: GetApiClassesIndexMultiClassingRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Multiclassing]:
        """
        Parameters
        ----------
        index : GetApiClassesIndexMultiClassingRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Multiclassing]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/classes/{jsonable_encoder(index)}/multi-classing",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Multiclassing,
                    parse_obj_as(
                        type_=Multiclassing,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_spellcasting_info_for_a_class(
        self,
        index: GetApiClassesIndexSpellcastingRequestIndex,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Spellcasting]:
        """
        Parameters
        ----------
        index : GetApiClassesIndexSpellcastingRequestIndex
            The `index` of the class to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Spellcasting]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/classes/{jsonable_encoder(index)}/spellcasting",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Spellcasting,
                    parse_obj_as(
                        type_=Spellcasting,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
