

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
from ..types.api_i_paged_response_global_resources_shared_models_string_definition import (
    ApiIPagedResponseGlobalResourcesSharedModelsStringDefinition,
)
from ..types.global_resources_shared_models_string_definition import GlobalResourcesSharedModelsStringDefinition
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawStringdefinitionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getdefinitions(
        self,
        *,
        limit: typing.Optional[int] = None,
        modified_after_timestamp: typing.Optional[str] = None,
        include_translations: typing.Optional[bool] = None,
        string_text: typing.Optional[str] = None,
        description_text: typing.Optional[str] = None,
        use_full_text: typing.Optional[bool] = None,
        include_deleted_languages: typing.Optional[bool] = None,
        language_ids: typing.Optional[str] = None,
        string_ids: typing.Optional[str] = None,
        matching_translations_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsStringDefinition]:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10. Ignored if 'stringIds' is provided.

        modified_after_timestamp : typing.Optional[str]
            Optional. Return only the StringDefinition objects that have a Timestamp value greater than that provided. This will be an encoded byte array.

        include_translations : typing.Optional[bool]
            Optional. Indicates whether to include the StringTranslations for the StringDefinition. Defaults to false.

        string_text : typing.Optional[str]
            Optional. The text for which to search in the StringDefinition object’s translations. Only StringDefinition objects for matching StringTranslation objects are returned. Does not filter if no value is provided. Supports beginning and/or ending wildcards. includeTranslations must be true.

        description_text : typing.Optional[str]
            Optional. The text for which to search in the StringDefinition description field. Only matching objects are returned. Does not filter if no value is provided. Supports beginning and/or ending wildcards.

        use_full_text : typing.Optional[bool]
            Optional. This flag is used to determin whether to use the FullText Search or not.

        include_deleted_languages : typing.Optional[bool]
            Optional. Indicates whether to include languages marked as deleted. includeTranslations must be true. Defaults to false.

        language_ids : typing.Optional[str]
            Optional. A comma-delimited list of language ids. Only StringTranslation objects with a matching language id will be returned. Optional. By default all locales are returned. includeTranslations must be true. The StringDefinition is still returned even if the filtered translations list is empty.

        string_ids : typing.Optional[str]
            Optional. A comma-delimited list of string ids. Up to 40 string IDs may be provided. May not be used with 'modifiedAfterTimestamp', 'stringText', 'descriptionText', or 'useFullText'.

        matching_translations_only : typing.Optional[bool]
            Optional. If false, all translations for returned String Definitions are included. Must be used with 'stringText' provided and 'includeTranslations' = true.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsStringDefinition]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/StringDefinitions",
            method="GET",
            params={
                "limit": limit,
                "modifiedAfterTimestamp": modified_after_timestamp,
                "includeTranslations": include_translations,
                "stringText": string_text,
                "descriptionText": description_text,
                "useFullText": use_full_text,
                "includeDeletedLanguages": include_deleted_languages,
                "languageIds": language_ids,
                "stringIds": string_ids,
                "matchingTranslationsOnly": matching_translations_only,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseGlobalResourcesSharedModelsStringDefinition,
                    parse_obj_as(
                        type_=ApiIPagedResponseGlobalResourcesSharedModelsStringDefinition,
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

    def postdefinition(
        self,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsStringDefinition],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[GlobalResourcesSharedModelsStringDefinition]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/StringDefinitions/Batch",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[GlobalResourcesSharedModelsStringDefinition],
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

    def updatedefinitions(
        self,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsStringDefinition],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[GlobalResourcesSharedModelsStringDefinition]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/StringDefinitions/Batch",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[GlobalResourcesSharedModelsStringDefinition],
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

    def getdefinition(
        self,
        id: str,
        *,
        include_translations: typing.Optional[bool] = None,
        include_deleted_languages: typing.Optional[bool] = None,
        language_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GlobalResourcesSharedModelsStringDefinition]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str

        include_translations : typing.Optional[bool]
            Optional. Indicates whether to include the StringTranslations for the StringDefinition. Defaults to false.

        include_deleted_languages : typing.Optional[bool]
            Optional. Indicates whether to include languages marked as deleted. includeTranslations must be true. Defaults to false.

        language_ids : typing.Optional[str]
            Optional. A comma-delimited list of language ids. Only StringTranslation objects with a matching language id will be returned. Optional. By default all locales are returned. includeTranslations must be true. The StringDefinition is still returned even if the filtered translations list is empty.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GlobalResourcesSharedModelsStringDefinition]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/StringDefinitions/{encode_path_param(id)}",
            method="GET",
            params={
                "includeTranslations": include_translations,
                "includeDeletedLanguages": include_deleted_languages,
                "languageIds": language_ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalResourcesSharedModelsStringDefinition,
                    parse_obj_as(
                        type_=GlobalResourcesSharedModelsStringDefinition,
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


class AsyncRawStringdefinitionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getdefinitions(
        self,
        *,
        limit: typing.Optional[int] = None,
        modified_after_timestamp: typing.Optional[str] = None,
        include_translations: typing.Optional[bool] = None,
        string_text: typing.Optional[str] = None,
        description_text: typing.Optional[str] = None,
        use_full_text: typing.Optional[bool] = None,
        include_deleted_languages: typing.Optional[bool] = None,
        language_ids: typing.Optional[str] = None,
        string_ids: typing.Optional[str] = None,
        matching_translations_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsStringDefinition]:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10. Ignored if 'stringIds' is provided.

        modified_after_timestamp : typing.Optional[str]
            Optional. Return only the StringDefinition objects that have a Timestamp value greater than that provided. This will be an encoded byte array.

        include_translations : typing.Optional[bool]
            Optional. Indicates whether to include the StringTranslations for the StringDefinition. Defaults to false.

        string_text : typing.Optional[str]
            Optional. The text for which to search in the StringDefinition object’s translations. Only StringDefinition objects for matching StringTranslation objects are returned. Does not filter if no value is provided. Supports beginning and/or ending wildcards. includeTranslations must be true.

        description_text : typing.Optional[str]
            Optional. The text for which to search in the StringDefinition description field. Only matching objects are returned. Does not filter if no value is provided. Supports beginning and/or ending wildcards.

        use_full_text : typing.Optional[bool]
            Optional. This flag is used to determin whether to use the FullText Search or not.

        include_deleted_languages : typing.Optional[bool]
            Optional. Indicates whether to include languages marked as deleted. includeTranslations must be true. Defaults to false.

        language_ids : typing.Optional[str]
            Optional. A comma-delimited list of language ids. Only StringTranslation objects with a matching language id will be returned. Optional. By default all locales are returned. includeTranslations must be true. The StringDefinition is still returned even if the filtered translations list is empty.

        string_ids : typing.Optional[str]
            Optional. A comma-delimited list of string ids. Up to 40 string IDs may be provided. May not be used with 'modifiedAfterTimestamp', 'stringText', 'descriptionText', or 'useFullText'.

        matching_translations_only : typing.Optional[bool]
            Optional. If false, all translations for returned String Definitions are included. Must be used with 'stringText' provided and 'includeTranslations' = true.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsStringDefinition]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/StringDefinitions",
            method="GET",
            params={
                "limit": limit,
                "modifiedAfterTimestamp": modified_after_timestamp,
                "includeTranslations": include_translations,
                "stringText": string_text,
                "descriptionText": description_text,
                "useFullText": use_full_text,
                "includeDeletedLanguages": include_deleted_languages,
                "languageIds": language_ids,
                "stringIds": string_ids,
                "matchingTranslationsOnly": matching_translations_only,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseGlobalResourcesSharedModelsStringDefinition,
                    parse_obj_as(
                        type_=ApiIPagedResponseGlobalResourcesSharedModelsStringDefinition,
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

    async def postdefinition(
        self,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsStringDefinition],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[GlobalResourcesSharedModelsStringDefinition]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/StringDefinitions/Batch",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[GlobalResourcesSharedModelsStringDefinition],
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

    async def updatedefinitions(
        self,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsStringDefinition],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[GlobalResourcesSharedModelsStringDefinition]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/StringDefinitions/Batch",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[GlobalResourcesSharedModelsStringDefinition],
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

    async def getdefinition(
        self,
        id: str,
        *,
        include_translations: typing.Optional[bool] = None,
        include_deleted_languages: typing.Optional[bool] = None,
        language_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GlobalResourcesSharedModelsStringDefinition]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str

        include_translations : typing.Optional[bool]
            Optional. Indicates whether to include the StringTranslations for the StringDefinition. Defaults to false.

        include_deleted_languages : typing.Optional[bool]
            Optional. Indicates whether to include languages marked as deleted. includeTranslations must be true. Defaults to false.

        language_ids : typing.Optional[str]
            Optional. A comma-delimited list of language ids. Only StringTranslation objects with a matching language id will be returned. Optional. By default all locales are returned. includeTranslations must be true. The StringDefinition is still returned even if the filtered translations list is empty.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GlobalResourcesSharedModelsStringDefinition]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/StringDefinitions/{encode_path_param(id)}",
            method="GET",
            params={
                "includeTranslations": include_translations,
                "includeDeletedLanguages": include_deleted_languages,
                "languageIds": language_ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalResourcesSharedModelsStringDefinition,
                    parse_obj_as(
                        type_=GlobalResourcesSharedModelsStringDefinition,
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
