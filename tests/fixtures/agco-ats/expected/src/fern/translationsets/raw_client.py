

import datetime as dt
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
from ..types.api_i_paged_response_global_resources_shared_models_translation_set import (
    ApiIPagedResponseGlobalResourcesSharedModelsTranslationSet,
)
from ..types.api_i_paged_response_global_resources_shared_models_translation_set_attribute import (
    ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute,
)
from ..types.api_i_paged_response_global_resources_shared_models_translation_set_source_string import (
    ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString,
)
from ..types.api_i_paged_response_global_resources_shared_models_translation_set_string import (
    ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetString,
)
from ..types.global_resources_shared_models_translation_set import GlobalResourcesSharedModelsTranslationSet
from ..types.global_resources_shared_models_translation_set_attribute import (
    GlobalResourcesSharedModelsTranslationSetAttribute,
)
from ..types.global_resources_shared_models_translation_set_state import GlobalResourcesSharedModelsTranslationSetState
from ..types.global_resources_shared_models_translation_set_statistics import (
    GlobalResourcesSharedModelsTranslationSetStatistics,
)
from ..types.global_resources_shared_models_translation_set_string import (
    GlobalResourcesSharedModelsTranslationSetString,
)
from .types.translation_sets_get_translation_sets_request_state import TranslationSetsGetTranslationSetsRequestState
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTranslationsetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def updatetranslationsetattributes(
        self,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/TranslationSetAttributes/Batch",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute],
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

    def updatetranslationsetattribute(
        self,
        id_: int,
        *,
        name: str,
        id: typing.Optional[int] = OMIT,
        translation_set_id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int


        name : str
            The name of this Attribute.

        id : typing.Optional[int]
            The ID of this attribute.

        translation_set_id : typing.Optional[int]
            The ID of the translation set to which this attribute belongs.

        value : typing.Optional[str]
            The value of this Attribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSetAttributes/{encode_path_param(id_)}",
            method="PUT",
            json={
                "ID": id,
                "Name": name,
                "TranslationSetID": translation_set_id,
                "Value": value,
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

    def deletetranslationsetattribute(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSetAttributes/{encode_path_param(id)}",
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

    def gettranslationsets(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        translation_request_id: typing.Optional[int] = None,
        state: typing.Optional[TranslationSetsGetTranslationSetsRequestState] = None,
        string_id: typing.Optional[str] = None,
        language_id: typing.Optional[int] = None,
        include_attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsTranslationSet]:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]


        offset : typing.Optional[int]


        translation_request_id : typing.Optional[int]


        state : typing.Optional[TranslationSetsGetTranslationSetsRequestState]


        string_id : typing.Optional[str]


        language_id : typing.Optional[int]


        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this submission. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsTranslationSet]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/TranslationSets",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "translationRequestID": translation_request_id,
                "state": state,
                "stringId": string_id,
                "languageId": language_id,
                "includeAttributes": include_attributes,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseGlobalResourcesSharedModelsTranslationSet,
                    parse_obj_as(
                        type_=ApiIPagedResponseGlobalResourcesSharedModelsTranslationSet,
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

    def gettranslationset(
        self,
        id: int,
        *,
        include_attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GlobalResourcesSharedModelsTranslationSet]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this Translation set. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GlobalResourcesSharedModelsTranslationSet]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSets/{encode_path_param(id)}",
            method="GET",
            params={
                "includeAttributes": include_attributes,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalResourcesSharedModelsTranslationSet,
                    parse_obj_as(
                        type_=GlobalResourcesSharedModelsTranslationSet,
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

    def updatetranslationset(
        self,
        id_: int,
        *,
        file_i_ds: typing.Sequence[str],
        state: GlobalResourcesSharedModelsTranslationSetState,
        attributes: typing.Optional[typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute]] = OMIT,
        id: typing.Optional[int] = OMIT,
        in_date: typing.Optional[dt.datetime] = OMIT,
        notes: typing.Optional[str] = OMIT,
        out_date: typing.Optional[dt.datetime] = OMIT,
        translation_request_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int


        file_i_ds : typing.Sequence[str]
            IDs for files related to this translation set. For example, the original and processed files

        state : GlobalResourcesSharedModelsTranslationSetState
            An enum indicating the state of the translation set

        attributes : typing.Optional[typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute]]
            Attributes of the Translation Set

        id : typing.Optional[int]
            The id of the TranslationSet.

        in_date : typing.Optional[dt.datetime]
            Read Only. The date the translation set was returned.

        notes : typing.Optional[str]
            Notes on the TranslationSet

        out_date : typing.Optional[dt.datetime]
            Read Only. The date the translation set was sent out.

        translation_request_id : typing.Optional[int]
            Read Only. The Id of the TranslationRequest which generated this translation set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSets/{encode_path_param(id_)}",
            method="PUT",
            json={
                "Attributes": convert_and_respect_annotation_metadata(
                    object_=attributes,
                    annotation=typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute],
                    direction="write",
                ),
                "FileIDs": file_i_ds,
                "Id": id,
                "InDate": in_date,
                "Notes": notes,
                "OutDate": out_date,
                "State": state,
                "TranslationRequestID": translation_request_id,
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

    def gettranslationsetattributes(
        self,
        id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        limit : typing.Optional[int]


        offset : typing.Optional[int]


        name : typing.Optional[str]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSets/{encode_path_param(id)}/Attributes",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute,
                    parse_obj_as(
                        type_=ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute,
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

    def posttranslationsetattribute(
        self,
        id_: int,
        *,
        name: str,
        id: typing.Optional[int] = OMIT,
        translation_set_id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int


        name : str
            The name of this Attribute.

        id : typing.Optional[int]
            The ID of this attribute.

        translation_set_id : typing.Optional[int]
            The ID of the translation set to which this attribute belongs.

        value : typing.Optional[str]
            The value of this Attribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSets/{encode_path_param(id_)}/Attributes",
            method="POST",
            json={
                "ID": id,
                "Name": name,
                "TranslationSetID": translation_set_id,
                "Value": value,
            },
            headers={
                "content-type": "application/json",
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

    def posttranslationsetattributes(
        self,
        id: int,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int

        request : typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSets/{encode_path_param(id)}/Attributes/Batch",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute],
                direction="write",
            ),
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

    def getsourcestrings(
        self,
        id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        limit : typing.Optional[int]


        offset : typing.Optional[int]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSets/{encode_path_param(id)}/SourceStrings",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString,
                    parse_obj_as(
                        type_=ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString,
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

    def getstatistics(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GlobalResourcesSharedModelsTranslationSetStatistics]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GlobalResourcesSharedModelsTranslationSetStatistics]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSets/{encode_path_param(id)}/Statistics",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalResourcesSharedModelsTranslationSetStatistics,
                    parse_obj_as(
                        type_=GlobalResourcesSharedModelsTranslationSetStatistics,
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

    def gettranslationsetstrings(
        self,
        id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetString]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        limit : typing.Optional[int]


        offset : typing.Optional[int]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetString]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSets/{encode_path_param(id)}/Strings",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetString,
                    parse_obj_as(
                        type_=ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetString,
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

    def updatetranslationsetstrings(
        self,
        id: int,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsTranslationSetString],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int

        request : typing.Sequence[GlobalResourcesSharedModelsTranslationSetString]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSets/{encode_path_param(id)}/Strings",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[GlobalResourcesSharedModelsTranslationSetString],
                direction="write",
            ),
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


class AsyncRawTranslationsetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def updatetranslationsetattributes(
        self,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/TranslationSetAttributes/Batch",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute],
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

    async def updatetranslationsetattribute(
        self,
        id_: int,
        *,
        name: str,
        id: typing.Optional[int] = OMIT,
        translation_set_id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int


        name : str
            The name of this Attribute.

        id : typing.Optional[int]
            The ID of this attribute.

        translation_set_id : typing.Optional[int]
            The ID of the translation set to which this attribute belongs.

        value : typing.Optional[str]
            The value of this Attribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSetAttributes/{encode_path_param(id_)}",
            method="PUT",
            json={
                "ID": id,
                "Name": name,
                "TranslationSetID": translation_set_id,
                "Value": value,
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

    async def deletetranslationsetattribute(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSetAttributes/{encode_path_param(id)}",
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

    async def gettranslationsets(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        translation_request_id: typing.Optional[int] = None,
        state: typing.Optional[TranslationSetsGetTranslationSetsRequestState] = None,
        string_id: typing.Optional[str] = None,
        language_id: typing.Optional[int] = None,
        include_attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsTranslationSet]:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]


        offset : typing.Optional[int]


        translation_request_id : typing.Optional[int]


        state : typing.Optional[TranslationSetsGetTranslationSetsRequestState]


        string_id : typing.Optional[str]


        language_id : typing.Optional[int]


        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this submission. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsTranslationSet]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/TranslationSets",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "translationRequestID": translation_request_id,
                "state": state,
                "stringId": string_id,
                "languageId": language_id,
                "includeAttributes": include_attributes,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseGlobalResourcesSharedModelsTranslationSet,
                    parse_obj_as(
                        type_=ApiIPagedResponseGlobalResourcesSharedModelsTranslationSet,
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

    async def gettranslationset(
        self,
        id: int,
        *,
        include_attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GlobalResourcesSharedModelsTranslationSet]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this Translation set. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GlobalResourcesSharedModelsTranslationSet]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSets/{encode_path_param(id)}",
            method="GET",
            params={
                "includeAttributes": include_attributes,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalResourcesSharedModelsTranslationSet,
                    parse_obj_as(
                        type_=GlobalResourcesSharedModelsTranslationSet,
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

    async def updatetranslationset(
        self,
        id_: int,
        *,
        file_i_ds: typing.Sequence[str],
        state: GlobalResourcesSharedModelsTranslationSetState,
        attributes: typing.Optional[typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute]] = OMIT,
        id: typing.Optional[int] = OMIT,
        in_date: typing.Optional[dt.datetime] = OMIT,
        notes: typing.Optional[str] = OMIT,
        out_date: typing.Optional[dt.datetime] = OMIT,
        translation_request_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int


        file_i_ds : typing.Sequence[str]
            IDs for files related to this translation set. For example, the original and processed files

        state : GlobalResourcesSharedModelsTranslationSetState
            An enum indicating the state of the translation set

        attributes : typing.Optional[typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute]]
            Attributes of the Translation Set

        id : typing.Optional[int]
            The id of the TranslationSet.

        in_date : typing.Optional[dt.datetime]
            Read Only. The date the translation set was returned.

        notes : typing.Optional[str]
            Notes on the TranslationSet

        out_date : typing.Optional[dt.datetime]
            Read Only. The date the translation set was sent out.

        translation_request_id : typing.Optional[int]
            Read Only. The Id of the TranslationRequest which generated this translation set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSets/{encode_path_param(id_)}",
            method="PUT",
            json={
                "Attributes": convert_and_respect_annotation_metadata(
                    object_=attributes,
                    annotation=typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute],
                    direction="write",
                ),
                "FileIDs": file_i_ds,
                "Id": id,
                "InDate": in_date,
                "Notes": notes,
                "OutDate": out_date,
                "State": state,
                "TranslationRequestID": translation_request_id,
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

    async def gettranslationsetattributes(
        self,
        id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        limit : typing.Optional[int]


        offset : typing.Optional[int]


        name : typing.Optional[str]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSets/{encode_path_param(id)}/Attributes",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute,
                    parse_obj_as(
                        type_=ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute,
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

    async def posttranslationsetattribute(
        self,
        id_: int,
        *,
        name: str,
        id: typing.Optional[int] = OMIT,
        translation_set_id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int


        name : str
            The name of this Attribute.

        id : typing.Optional[int]
            The ID of this attribute.

        translation_set_id : typing.Optional[int]
            The ID of the translation set to which this attribute belongs.

        value : typing.Optional[str]
            The value of this Attribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSets/{encode_path_param(id_)}/Attributes",
            method="POST",
            json={
                "ID": id,
                "Name": name,
                "TranslationSetID": translation_set_id,
                "Value": value,
            },
            headers={
                "content-type": "application/json",
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

    async def posttranslationsetattributes(
        self,
        id: int,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int

        request : typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSets/{encode_path_param(id)}/Attributes/Batch",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute],
                direction="write",
            ),
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

    async def getsourcestrings(
        self,
        id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        limit : typing.Optional[int]


        offset : typing.Optional[int]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSets/{encode_path_param(id)}/SourceStrings",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString,
                    parse_obj_as(
                        type_=ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString,
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

    async def getstatistics(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GlobalResourcesSharedModelsTranslationSetStatistics]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GlobalResourcesSharedModelsTranslationSetStatistics]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSets/{encode_path_param(id)}/Statistics",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalResourcesSharedModelsTranslationSetStatistics,
                    parse_obj_as(
                        type_=GlobalResourcesSharedModelsTranslationSetStatistics,
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

    async def gettranslationsetstrings(
        self,
        id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetString]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        limit : typing.Optional[int]


        offset : typing.Optional[int]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetString]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSets/{encode_path_param(id)}/Strings",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetString,
                    parse_obj_as(
                        type_=ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetString,
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

    async def updatetranslationsetstrings(
        self,
        id: int,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsTranslationSetString],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int

        request : typing.Sequence[GlobalResourcesSharedModelsTranslationSetString]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/TranslationSets/{encode_path_param(id)}/Strings",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[GlobalResourcesSharedModelsTranslationSetString],
                direction="write",
            ),
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
