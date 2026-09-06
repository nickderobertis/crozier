

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.api_i_paged_response_global_resources_shared_models_string_translation import (
    ApiIPagedResponseGlobalResourcesSharedModelsStringTranslation,
)
from ..types.global_resources_shared_models_string_translation import GlobalResourcesSharedModelsStringTranslation
from ..types.global_resources_shared_models_string_translation_state import (
    GlobalResourcesSharedModelsStringTranslationState,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawStringtranslationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def gettranslations(
        self,
        *,
        limit: typing.Optional[int] = None,
        modified_after_timestamp: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsStringTranslation]:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        modified_after_timestamp : typing.Optional[str]
            Optional. Return only the StringDefinition objects that have a Timestamp value greater than that provided. This will be an encoded byte array.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsStringTranslation]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/StringTranslations",
            method="GET",
            params={
                "limit": limit,
                "modifiedAfterTimestamp": modified_after_timestamp,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseGlobalResourcesSharedModelsStringTranslation,
                    parse_obj_as(
                        type_=ApiIPagedResponseGlobalResourcesSharedModelsStringTranslation,
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

    def updatetranslations(
        self,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsStringTranslation],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[GlobalResourcesSharedModelsStringTranslation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/StringTranslations/Batch",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[GlobalResourcesSharedModelsStringTranslation],
                direction="write",
            ),
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

    def gettranslation(
        self, string_id: str, language_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GlobalResourcesSharedModelsStringTranslation]:
        """
        No Documentation Found.

        Parameters
        ----------
        string_id : str


        language_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GlobalResourcesSharedModelsStringTranslation]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/StringTranslations/{encode_path_param(string_id)}/{encode_path_param(language_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalResourcesSharedModelsStringTranslation,
                    parse_obj_as(
                        type_=GlobalResourcesSharedModelsStringTranslation,
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

    def updatetranslation(
        self,
        string_id_: str,
        language_id_: int,
        *,
        string_value: str,
        author_id: typing.Optional[int] = OMIT,
        language_id: typing.Optional[int] = OMIT,
        state: typing.Optional[GlobalResourcesSharedModelsStringTranslationState] = OMIT,
        string_id: typing.Optional[str] = OMIT,
        timestamp: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        string_id_ : str


        language_id_ : int


        string_value : str
            The translated string

        author_id : typing.Optional[int]
            The id of the user to last edit thie translation

        language_id : typing.Optional[int]
            The id of the language of the translation

        state : typing.Optional[GlobalResourcesSharedModelsStringTranslationState]
            The state of the translation

        string_id : typing.Optional[str]
            The id of the string that is translated

        timestamp : typing.Optional[str]
            A value indicating the last modification of this translation. Read Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/StringTranslations/{encode_path_param(string_id_)}/{encode_path_param(language_id_)}",
            method="PUT",
            json={
                "AuthorId": author_id,
                "LanguageId": language_id,
                "State": state,
                "StringId": string_id,
                "StringValue": string_value,
                "Timestamp": timestamp,
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


class AsyncRawStringtranslationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def gettranslations(
        self,
        *,
        limit: typing.Optional[int] = None,
        modified_after_timestamp: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsStringTranslation]:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        modified_after_timestamp : typing.Optional[str]
            Optional. Return only the StringDefinition objects that have a Timestamp value greater than that provided. This will be an encoded byte array.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsStringTranslation]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/StringTranslations",
            method="GET",
            params={
                "limit": limit,
                "modifiedAfterTimestamp": modified_after_timestamp,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseGlobalResourcesSharedModelsStringTranslation,
                    parse_obj_as(
                        type_=ApiIPagedResponseGlobalResourcesSharedModelsStringTranslation,
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

    async def updatetranslations(
        self,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsStringTranslation],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[GlobalResourcesSharedModelsStringTranslation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/StringTranslations/Batch",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[GlobalResourcesSharedModelsStringTranslation],
                direction="write",
            ),
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

    async def gettranslation(
        self, string_id: str, language_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GlobalResourcesSharedModelsStringTranslation]:
        """
        No Documentation Found.

        Parameters
        ----------
        string_id : str


        language_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GlobalResourcesSharedModelsStringTranslation]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/StringTranslations/{encode_path_param(string_id)}/{encode_path_param(language_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalResourcesSharedModelsStringTranslation,
                    parse_obj_as(
                        type_=GlobalResourcesSharedModelsStringTranslation,
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

    async def updatetranslation(
        self,
        string_id_: str,
        language_id_: int,
        *,
        string_value: str,
        author_id: typing.Optional[int] = OMIT,
        language_id: typing.Optional[int] = OMIT,
        state: typing.Optional[GlobalResourcesSharedModelsStringTranslationState] = OMIT,
        string_id: typing.Optional[str] = OMIT,
        timestamp: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        string_id_ : str


        language_id_ : int


        string_value : str
            The translated string

        author_id : typing.Optional[int]
            The id of the user to last edit thie translation

        language_id : typing.Optional[int]
            The id of the language of the translation

        state : typing.Optional[GlobalResourcesSharedModelsStringTranslationState]
            The state of the translation

        string_id : typing.Optional[str]
            The id of the string that is translated

        timestamp : typing.Optional[str]
            A value indicating the last modification of this translation. Read Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/StringTranslations/{encode_path_param(string_id_)}/{encode_path_param(language_id_)}",
            method="PUT",
            json={
                "AuthorId": author_id,
                "LanguageId": language_id,
                "State": state,
                "StringId": string_id,
                "StringValue": string_value,
                "Timestamp": timestamp,
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
