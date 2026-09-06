

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
from ..types.authorization_codes_shared_models_authorization_code_definition import (
    AuthorizationCodesSharedModelsAuthorizationCodeDefinition,
)
from ..types.authorization_codes_shared_models_authorization_code_definition_duration_units import (
    AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits,
)
from ..types.authorization_codes_shared_models_data_field import AuthorizationCodesSharedModelsDataField
from ..types.authorization_codes_shared_models_validation_field import AuthorizationCodesSharedModelsValidationField
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAuthorizationcodedefinitionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getauthorizationcodedefinition(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AuthorizationCodesSharedModelsAuthorizationCodeDefinition]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the authorization code definition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AuthorizationCodesSharedModelsAuthorizationCodeDefinition]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/AuthorizationCodeDefinitions/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AuthorizationCodesSharedModelsAuthorizationCodeDefinition,
                    parse_obj_as(
                        type_=AuthorizationCodesSharedModelsAuthorizationCodeDefinition,
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

    def postauthorizationcodedefinition(
        self,
        *,
        name: str,
        authorization_id: typing.Optional[str] = OMIT,
        created_by_user_id: typing.Optional[int] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        data_fields: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsDataField]] = OMIT,
        deleted_by_user_id: typing.Optional[int] = OMIT,
        deleted_date: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        duration_accuracy: typing.Optional[int] = OMIT,
        duration_amount: typing.Optional[int] = OMIT,
        duration_units: typing.Optional[AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits] = OMIT,
        hash_length: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        is_deleted: typing.Optional[bool] = OMIT,
        random_length: typing.Optional[int] = OMIT,
        validation_fields: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsValidationField]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        name : str
            The name of the authorization code definition. May not be updated.

        authorization_id : typing.Optional[str]
            The value used for securing codes generated.

        created_by_user_id : typing.Optional[int]
            The ID of the user that created this definition. Read only.

        created_date : typing.Optional[dt.datetime]
            A timestamp of when this definition was created. Read only.

        data_fields : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsDataField]]
            The defined fields to include in authorization codes generated from this definition. May not be updated.

        deleted_by_user_id : typing.Optional[int]
            The ID of the user that deleted this definition. Read only.

        deleted_date : typing.Optional[dt.datetime]
            A timestamp of when this definition was deleted. Read only.

        description : typing.Optional[str]
            A description of this definition. May not be updated.

        duration_accuracy : typing.Optional[int]
            The number of bits used for timestamp verification. Defaults to 5. May not be updated.

        duration_amount : typing.Optional[int]
            The amount of duration for the specified duration unit used to calculate the Authorization Code. Defaults to 1. May not be updated.

        duration_units : typing.Optional[AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits]
            The units of duration used to calculate the Authorization Code. Defaults to 'Days'. May not be updated.

        hash_length : typing.Optional[int]
            The bit length of the hash data which will be used for the authorization code. Defaults to 20. May not be updated.

        id : typing.Optional[str]
            The ID of the authorization code definition. Read only.

        is_deleted : typing.Optional[bool]
            Indicates whether this definition is enabled. True if generating codes is disabled.

        random_length : typing.Optional[int]
            The bit length of random data which will be included in the authorization code.  This is necessary to allow creation of "identical" authorization codes containing the same timestamp. Defaults to 5. May not be updated.

        validation_fields : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsValidationField]]
            The defined fields to verify when reading authorization codes generated from this definition. May not be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/AuthorizationCodeDefinitions",
            method="POST",
            json={
                "AuthorizationID": authorization_id,
                "CreatedByUserID": created_by_user_id,
                "CreatedDate": created_date,
                "DataFields": convert_and_respect_annotation_metadata(
                    object_=data_fields,
                    annotation=typing.Sequence[AuthorizationCodesSharedModelsDataField],
                    direction="write",
                ),
                "DeletedByUserID": deleted_by_user_id,
                "DeletedDate": deleted_date,
                "Description": description,
                "DurationAccuracy": duration_accuracy,
                "DurationAmount": duration_amount,
                "DurationUnits": duration_units,
                "HashLength": hash_length,
                "ID": id,
                "IsDeleted": is_deleted,
                "Name": name,
                "RandomLength": random_length,
                "ValidationFields": convert_and_respect_annotation_metadata(
                    object_=validation_fields,
                    annotation=typing.Sequence[AuthorizationCodesSharedModelsValidationField],
                    direction="write",
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    def addcategorytodefinition(
        self, id: str, category_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str

        category_id : str
            A category ID, as a GUID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/AuthorizationCodeDefinitions/{encode_path_param(id)}/Categories/{encode_path_param(category_id)}",
            method="POST",
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

    def removecategoryfromdefinition(
        self, id: str, category_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str

        category_id : str
            A category ID, as a GUID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/AuthorizationCodeDefinitions/{encode_path_param(id)}/Categories/{encode_path_param(category_id)}",
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

    def putauthorizationcodedefinition(
        self,
        id_: str,
        *,
        name: str,
        authorization_id: typing.Optional[str] = OMIT,
        created_by_user_id: typing.Optional[int] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        data_fields: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsDataField]] = OMIT,
        deleted_by_user_id: typing.Optional[int] = OMIT,
        deleted_date: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        duration_accuracy: typing.Optional[int] = OMIT,
        duration_amount: typing.Optional[int] = OMIT,
        duration_units: typing.Optional[AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits] = OMIT,
        hash_length: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        is_deleted: typing.Optional[bool] = OMIT,
        random_length: typing.Optional[int] = OMIT,
        validation_fields: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsValidationField]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : str
            The ID of the authorization code definition.

        name : str
            The name of the authorization code definition. May not be updated.

        authorization_id : typing.Optional[str]
            The value used for securing codes generated.

        created_by_user_id : typing.Optional[int]
            The ID of the user that created this definition. Read only.

        created_date : typing.Optional[dt.datetime]
            A timestamp of when this definition was created. Read only.

        data_fields : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsDataField]]
            The defined fields to include in authorization codes generated from this definition. May not be updated.

        deleted_by_user_id : typing.Optional[int]
            The ID of the user that deleted this definition. Read only.

        deleted_date : typing.Optional[dt.datetime]
            A timestamp of when this definition was deleted. Read only.

        description : typing.Optional[str]
            A description of this definition. May not be updated.

        duration_accuracy : typing.Optional[int]
            The number of bits used for timestamp verification. Defaults to 5. May not be updated.

        duration_amount : typing.Optional[int]
            The amount of duration for the specified duration unit used to calculate the Authorization Code. Defaults to 1. May not be updated.

        duration_units : typing.Optional[AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits]
            The units of duration used to calculate the Authorization Code. Defaults to 'Days'. May not be updated.

        hash_length : typing.Optional[int]
            The bit length of the hash data which will be used for the authorization code. Defaults to 20. May not be updated.

        id : typing.Optional[str]
            The ID of the authorization code definition. Read only.

        is_deleted : typing.Optional[bool]
            Indicates whether this definition is enabled. True if generating codes is disabled.

        random_length : typing.Optional[int]
            The bit length of random data which will be included in the authorization code.  This is necessary to allow creation of "identical" authorization codes containing the same timestamp. Defaults to 5. May not be updated.

        validation_fields : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsValidationField]]
            The defined fields to verify when reading authorization codes generated from this definition. May not be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/AuthorizationCodeDefinitions/{encode_path_param(id_)}",
            method="PUT",
            json={
                "AuthorizationID": authorization_id,
                "CreatedByUserID": created_by_user_id,
                "CreatedDate": created_date,
                "DataFields": convert_and_respect_annotation_metadata(
                    object_=data_fields,
                    annotation=typing.Sequence[AuthorizationCodesSharedModelsDataField],
                    direction="write",
                ),
                "DeletedByUserID": deleted_by_user_id,
                "DeletedDate": deleted_date,
                "Description": description,
                "DurationAccuracy": duration_accuracy,
                "DurationAmount": duration_amount,
                "DurationUnits": duration_units,
                "HashLength": hash_length,
                "ID": id,
                "IsDeleted": is_deleted,
                "Name": name,
                "RandomLength": random_length,
                "ValidationFields": convert_and_respect_annotation_metadata(
                    object_=validation_fields,
                    annotation=typing.Sequence[AuthorizationCodesSharedModelsValidationField],
                    direction="write",
                ),
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

    def deleteauthorizationcodedefinition(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the authorization code definition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/AuthorizationCodeDefinitions/{encode_path_param(id)}",
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


class AsyncRawAuthorizationcodedefinitionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getauthorizationcodedefinition(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AuthorizationCodesSharedModelsAuthorizationCodeDefinition]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the authorization code definition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AuthorizationCodesSharedModelsAuthorizationCodeDefinition]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/AuthorizationCodeDefinitions/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AuthorizationCodesSharedModelsAuthorizationCodeDefinition,
                    parse_obj_as(
                        type_=AuthorizationCodesSharedModelsAuthorizationCodeDefinition,
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

    async def postauthorizationcodedefinition(
        self,
        *,
        name: str,
        authorization_id: typing.Optional[str] = OMIT,
        created_by_user_id: typing.Optional[int] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        data_fields: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsDataField]] = OMIT,
        deleted_by_user_id: typing.Optional[int] = OMIT,
        deleted_date: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        duration_accuracy: typing.Optional[int] = OMIT,
        duration_amount: typing.Optional[int] = OMIT,
        duration_units: typing.Optional[AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits] = OMIT,
        hash_length: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        is_deleted: typing.Optional[bool] = OMIT,
        random_length: typing.Optional[int] = OMIT,
        validation_fields: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsValidationField]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        name : str
            The name of the authorization code definition. May not be updated.

        authorization_id : typing.Optional[str]
            The value used for securing codes generated.

        created_by_user_id : typing.Optional[int]
            The ID of the user that created this definition. Read only.

        created_date : typing.Optional[dt.datetime]
            A timestamp of when this definition was created. Read only.

        data_fields : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsDataField]]
            The defined fields to include in authorization codes generated from this definition. May not be updated.

        deleted_by_user_id : typing.Optional[int]
            The ID of the user that deleted this definition. Read only.

        deleted_date : typing.Optional[dt.datetime]
            A timestamp of when this definition was deleted. Read only.

        description : typing.Optional[str]
            A description of this definition. May not be updated.

        duration_accuracy : typing.Optional[int]
            The number of bits used for timestamp verification. Defaults to 5. May not be updated.

        duration_amount : typing.Optional[int]
            The amount of duration for the specified duration unit used to calculate the Authorization Code. Defaults to 1. May not be updated.

        duration_units : typing.Optional[AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits]
            The units of duration used to calculate the Authorization Code. Defaults to 'Days'. May not be updated.

        hash_length : typing.Optional[int]
            The bit length of the hash data which will be used for the authorization code. Defaults to 20. May not be updated.

        id : typing.Optional[str]
            The ID of the authorization code definition. Read only.

        is_deleted : typing.Optional[bool]
            Indicates whether this definition is enabled. True if generating codes is disabled.

        random_length : typing.Optional[int]
            The bit length of random data which will be included in the authorization code.  This is necessary to allow creation of "identical" authorization codes containing the same timestamp. Defaults to 5. May not be updated.

        validation_fields : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsValidationField]]
            The defined fields to verify when reading authorization codes generated from this definition. May not be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/AuthorizationCodeDefinitions",
            method="POST",
            json={
                "AuthorizationID": authorization_id,
                "CreatedByUserID": created_by_user_id,
                "CreatedDate": created_date,
                "DataFields": convert_and_respect_annotation_metadata(
                    object_=data_fields,
                    annotation=typing.Sequence[AuthorizationCodesSharedModelsDataField],
                    direction="write",
                ),
                "DeletedByUserID": deleted_by_user_id,
                "DeletedDate": deleted_date,
                "Description": description,
                "DurationAccuracy": duration_accuracy,
                "DurationAmount": duration_amount,
                "DurationUnits": duration_units,
                "HashLength": hash_length,
                "ID": id,
                "IsDeleted": is_deleted,
                "Name": name,
                "RandomLength": random_length,
                "ValidationFields": convert_and_respect_annotation_metadata(
                    object_=validation_fields,
                    annotation=typing.Sequence[AuthorizationCodesSharedModelsValidationField],
                    direction="write",
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    async def addcategorytodefinition(
        self, id: str, category_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str

        category_id : str
            A category ID, as a GUID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/AuthorizationCodeDefinitions/{encode_path_param(id)}/Categories/{encode_path_param(category_id)}",
            method="POST",
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

    async def removecategoryfromdefinition(
        self, id: str, category_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str

        category_id : str
            A category ID, as a GUID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/AuthorizationCodeDefinitions/{encode_path_param(id)}/Categories/{encode_path_param(category_id)}",
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

    async def putauthorizationcodedefinition(
        self,
        id_: str,
        *,
        name: str,
        authorization_id: typing.Optional[str] = OMIT,
        created_by_user_id: typing.Optional[int] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        data_fields: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsDataField]] = OMIT,
        deleted_by_user_id: typing.Optional[int] = OMIT,
        deleted_date: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        duration_accuracy: typing.Optional[int] = OMIT,
        duration_amount: typing.Optional[int] = OMIT,
        duration_units: typing.Optional[AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits] = OMIT,
        hash_length: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        is_deleted: typing.Optional[bool] = OMIT,
        random_length: typing.Optional[int] = OMIT,
        validation_fields: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsValidationField]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : str
            The ID of the authorization code definition.

        name : str
            The name of the authorization code definition. May not be updated.

        authorization_id : typing.Optional[str]
            The value used for securing codes generated.

        created_by_user_id : typing.Optional[int]
            The ID of the user that created this definition. Read only.

        created_date : typing.Optional[dt.datetime]
            A timestamp of when this definition was created. Read only.

        data_fields : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsDataField]]
            The defined fields to include in authorization codes generated from this definition. May not be updated.

        deleted_by_user_id : typing.Optional[int]
            The ID of the user that deleted this definition. Read only.

        deleted_date : typing.Optional[dt.datetime]
            A timestamp of when this definition was deleted. Read only.

        description : typing.Optional[str]
            A description of this definition. May not be updated.

        duration_accuracy : typing.Optional[int]
            The number of bits used for timestamp verification. Defaults to 5. May not be updated.

        duration_amount : typing.Optional[int]
            The amount of duration for the specified duration unit used to calculate the Authorization Code. Defaults to 1. May not be updated.

        duration_units : typing.Optional[AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits]
            The units of duration used to calculate the Authorization Code. Defaults to 'Days'. May not be updated.

        hash_length : typing.Optional[int]
            The bit length of the hash data which will be used for the authorization code. Defaults to 20. May not be updated.

        id : typing.Optional[str]
            The ID of the authorization code definition. Read only.

        is_deleted : typing.Optional[bool]
            Indicates whether this definition is enabled. True if generating codes is disabled.

        random_length : typing.Optional[int]
            The bit length of random data which will be included in the authorization code.  This is necessary to allow creation of "identical" authorization codes containing the same timestamp. Defaults to 5. May not be updated.

        validation_fields : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsValidationField]]
            The defined fields to verify when reading authorization codes generated from this definition. May not be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/AuthorizationCodeDefinitions/{encode_path_param(id_)}",
            method="PUT",
            json={
                "AuthorizationID": authorization_id,
                "CreatedByUserID": created_by_user_id,
                "CreatedDate": created_date,
                "DataFields": convert_and_respect_annotation_metadata(
                    object_=data_fields,
                    annotation=typing.Sequence[AuthorizationCodesSharedModelsDataField],
                    direction="write",
                ),
                "DeletedByUserID": deleted_by_user_id,
                "DeletedDate": deleted_date,
                "Description": description,
                "DurationAccuracy": duration_accuracy,
                "DurationAmount": duration_amount,
                "DurationUnits": duration_units,
                "HashLength": hash_length,
                "ID": id,
                "IsDeleted": is_deleted,
                "Name": name,
                "RandomLength": random_length,
                "ValidationFields": convert_and_respect_annotation_metadata(
                    object_=validation_fields,
                    annotation=typing.Sequence[AuthorizationCodesSharedModelsValidationField],
                    direction="write",
                ),
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

    async def deleteauthorizationcodedefinition(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the authorization code definition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/AuthorizationCodeDefinitions/{encode_path_param(id)}",
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
