

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_i_paged_response_oas_support_shared_models_translation_key import (
    ApiIPagedResponseOasSupportSharedModelsTranslationKey,
)
from ..types.oas_support_shared_models_translation_key import OasSupportSharedModelsTranslationKey
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTranslationkeysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        key_names: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiIPagedResponseOasSupportSharedModelsTranslationKey]:
        """


        Parameters
        ----------
        limit : typing.Optional[int]


        offset : typing.Optional[int]


        key_names : typing.Optional[str]
            Can filter by keyNames, a comma deliminated list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiIPagedResponseOasSupportSharedModelsTranslationKey]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/TranslationKeys",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "keyNames": key_names,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseOasSupportSharedModelsTranslationKey,
                    parse_obj_as(
                        type_=ApiIPagedResponseOasSupportSharedModelsTranslationKey,
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

    def createtranslationkey(
        self,
        *,
        key_name: str,
        string_id: str,
        id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        key_name : str
            The key name of the item. One example is tkODX_HWIKM14R01

        string_id : str
            Foreign key to StringDefinitionID

        id : typing.Optional[int]
            The identifier for the translationKey. Read Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/TranslationKeys",
            method="POST",
            json={
                "ID": id,
                "KeyName": key_name,
                "StringID": string_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
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

    def gettranslationkey(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OasSupportSharedModelsTranslationKey]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OasSupportSharedModelsTranslationKey]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationKeys/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OasSupportSharedModelsTranslationKey,
                    parse_obj_as(
                        type_=OasSupportSharedModelsTranslationKey,
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

    def updatetranslationkey(
        self,
        id_: int,
        *,
        key_name: str,
        string_id: str,
        id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int


        key_name : str
            The key name of the item. One example is tkODX_HWIKM14R01

        string_id : str
            Foreign key to StringDefinitionID

        id : typing.Optional[int]
            The identifier for the translationKey. Read Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationKeys/{encode_path_param(id_)}",
            method="PUT",
            json={
                "ID": id,
                "KeyName": key_name,
                "StringID": string_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTranslationkeysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        key_names: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiIPagedResponseOasSupportSharedModelsTranslationKey]:
        """


        Parameters
        ----------
        limit : typing.Optional[int]


        offset : typing.Optional[int]


        key_names : typing.Optional[str]
            Can filter by keyNames, a comma deliminated list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiIPagedResponseOasSupportSharedModelsTranslationKey]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/TranslationKeys",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "keyNames": key_names,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseOasSupportSharedModelsTranslationKey,
                    parse_obj_as(
                        type_=ApiIPagedResponseOasSupportSharedModelsTranslationKey,
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

    async def createtranslationkey(
        self,
        *,
        key_name: str,
        string_id: str,
        id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        key_name : str
            The key name of the item. One example is tkODX_HWIKM14R01

        string_id : str
            Foreign key to StringDefinitionID

        id : typing.Optional[int]
            The identifier for the translationKey. Read Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/TranslationKeys",
            method="POST",
            json={
                "ID": id,
                "KeyName": key_name,
                "StringID": string_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
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

    async def gettranslationkey(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OasSupportSharedModelsTranslationKey]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OasSupportSharedModelsTranslationKey]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationKeys/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OasSupportSharedModelsTranslationKey,
                    parse_obj_as(
                        type_=OasSupportSharedModelsTranslationKey,
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

    async def updatetranslationkey(
        self,
        id_: int,
        *,
        key_name: str,
        string_id: str,
        id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int


        key_name : str
            The key name of the item. One example is tkODX_HWIKM14R01

        string_id : str
            Foreign key to StringDefinitionID

        id : typing.Optional[int]
            The identifier for the translationKey. Read Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationKeys/{encode_path_param(id_)}",
            method="PUT",
            json={
                "ID": id,
                "KeyName": key_name,
                "StringID": string_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
