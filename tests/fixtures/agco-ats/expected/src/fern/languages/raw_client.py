

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_i_paged_response_global_resources_shared_models_language import (
    ApiIPagedResponseGlobalResourcesSharedModelsLanguage,
)
from ..types.global_resources_shared_models_language import GlobalResourcesSharedModelsLanguage
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLanguagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getlanguages(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsLanguage]:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            limit the number of Language objects returned. Optional (defaults to 10).

        offset : typing.Optional[int]
            the number of Language objects to skip. Optional (defaults to 0).

        include_deleted : typing.Optional[bool]
            whether to include languages marked as deleted. Defaults to false

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsLanguage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Languages",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "includeDeleted": include_deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseGlobalResourcesSharedModelsLanguage,
                    parse_obj_as(
                        type_=ApiIPagedResponseGlobalResourcesSharedModelsLanguage,
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

    def createlanguage(
        self,
        *,
        description: str,
        locale_id: int,
        is_deleted: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        description : str
            The description of the language (e.g. “English – United States”).

        locale_id : int
            The Locale Id of the language.

        is_deleted : typing.Optional[bool]
            Indicates whether the API supports the language. Must be false when created. Read Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Languages",
            method="POST",
            json={
                "Description": description,
                "IsDeleted": is_deleted,
                "LocaleId": locale_id,
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

    def getlanguage(
        self, locale_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GlobalResourcesSharedModelsLanguage]:
        """
        No Documentation Found.

        Parameters
        ----------
        locale_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GlobalResourcesSharedModelsLanguage]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Languages/{encode_path_param(locale_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalResourcesSharedModelsLanguage,
                    parse_obj_as(
                        type_=GlobalResourcesSharedModelsLanguage,
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

    def updatelanguage(
        self,
        locale_id_: int,
        *,
        description: str,
        locale_id: int,
        is_deleted: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        locale_id_ : int


        description : str
            The description of the language (e.g. “English – United States”).

        locale_id : int
            The Locale Id of the language.

        is_deleted : typing.Optional[bool]
            Indicates whether the API supports the language. Must be false when created. Read Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Languages/{encode_path_param(locale_id_)}",
            method="PUT",
            json={
                "Description": description,
                "IsDeleted": is_deleted,
                "LocaleId": locale_id,
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

    def deletelanguage(
        self, locale_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        locale_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Languages/{encode_path_param(locale_id)}",
            method="DELETE",
            request_options=request_options,
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


class AsyncRawLanguagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getlanguages(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsLanguage]:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            limit the number of Language objects returned. Optional (defaults to 10).

        offset : typing.Optional[int]
            the number of Language objects to skip. Optional (defaults to 0).

        include_deleted : typing.Optional[bool]
            whether to include languages marked as deleted. Defaults to false

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsLanguage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Languages",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "includeDeleted": include_deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseGlobalResourcesSharedModelsLanguage,
                    parse_obj_as(
                        type_=ApiIPagedResponseGlobalResourcesSharedModelsLanguage,
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

    async def createlanguage(
        self,
        *,
        description: str,
        locale_id: int,
        is_deleted: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        description : str
            The description of the language (e.g. “English – United States”).

        locale_id : int
            The Locale Id of the language.

        is_deleted : typing.Optional[bool]
            Indicates whether the API supports the language. Must be false when created. Read Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Languages",
            method="POST",
            json={
                "Description": description,
                "IsDeleted": is_deleted,
                "LocaleId": locale_id,
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

    async def getlanguage(
        self, locale_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GlobalResourcesSharedModelsLanguage]:
        """
        No Documentation Found.

        Parameters
        ----------
        locale_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GlobalResourcesSharedModelsLanguage]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Languages/{encode_path_param(locale_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalResourcesSharedModelsLanguage,
                    parse_obj_as(
                        type_=GlobalResourcesSharedModelsLanguage,
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

    async def updatelanguage(
        self,
        locale_id_: int,
        *,
        description: str,
        locale_id: int,
        is_deleted: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        locale_id_ : int


        description : str
            The description of the language (e.g. “English – United States”).

        locale_id : int
            The Locale Id of the language.

        is_deleted : typing.Optional[bool]
            Indicates whether the API supports the language. Must be false when created. Read Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Languages/{encode_path_param(locale_id_)}",
            method="PUT",
            json={
                "Description": description,
                "IsDeleted": is_deleted,
                "LocaleId": locale_id,
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

    async def deletelanguage(
        self, locale_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        locale_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Languages/{encode_path_param(locale_id)}",
            method="DELETE",
            request_options=request_options,
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
