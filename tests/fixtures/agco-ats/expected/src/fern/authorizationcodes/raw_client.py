

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
from ..types.api_i_paged_response_authorization_codes_shared_models_authorization_code import (
    ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode,
)
from ..types.authorization_codes_shared_models_authorization_code import AuthorizationCodesSharedModelsAuthorizationCode
from ..types.authorization_codes_shared_models_authorization_contact_information import (
    AuthorizationCodesSharedModelsAuthorizationContactInformation,
)
from ..types.authorization_codes_shared_models_code_validation_model import (
    AuthorizationCodesSharedModelsCodeValidationModel,
)
from ..types.authorization_codes_shared_models_parameter import AuthorizationCodesSharedModelsParameter
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAuthorizationcodesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getauthorizationcodes(
        self,
        *,
        code: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        definition_id: typing.Optional[str] = None,
        created_by_user_id: typing.Optional[int] = None,
        deleted_by_user_id: typing.Optional[int] = None,
        include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode]:
        """
        Additional searches: validationParameters[Name]=Value and dataParameters[Name]=Value. These can be used to search for authorization codes that have been generated using specified values for data or validation parameters.

        Parameters
        ----------
        code : typing.Optional[str]
            Optional. If provided, searches for entities with the provided authorization code.

        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        definition_id : typing.Optional[str]
            Optional. If specified, filters codes by definition id.

        created_by_user_id : typing.Optional[int]
            Optional. If specified, filters codes to those created by the given User ID.

        deleted_by_user_id : typing.Optional[int]
            Optional. If specified, filters codes to those deleted by the given User ID.

        include_deleted : typing.Optional[bool]
            Optional. Whether to include deleted codes. 'False' by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/AuthorizationCodes",
            method="GET",
            params={
                "code": code,
                "limit": limit,
                "offset": offset,
                "definitionID": definition_id,
                "createdByUserID": created_by_user_id,
                "deletedByUserID": deleted_by_user_id,
                "includeDeleted": include_deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode,
                    parse_obj_as(
                        type_=ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode,
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

    def postauthorizationcode(
        self,
        *,
        code: typing.Optional[str] = OMIT,
        created_by_user_id: typing.Optional[int] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        data_parameters: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]] = OMIT,
        definition_id: typing.Optional[str] = OMIT,
        deleted_by_user_id: typing.Optional[int] = OMIT,
        deleted_date: typing.Optional[dt.datetime] = OMIT,
        effective_date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_deleted: typing.Optional[bool] = OMIT,
        validation_parameters: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        code : typing.Optional[str]
            The code to enter to unlock a feature. Read only.

        created_by_user_id : typing.Optional[int]
            The ID of the user that created this authorization code. Read only.

        created_date : typing.Optional[dt.datetime]
            A timestamp of when this code was created. Read only.

        data_parameters : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]]
            The parameters and values contained as data in this authorization code. May not be updated.

        definition_id : typing.Optional[str]
            The id of the definition for this authorization code. May not be updated.

        deleted_by_user_id : typing.Optional[int]
            The ID of the user that deleted this authorization code. Read only.

        deleted_date : typing.Optional[dt.datetime]
            A timestamp of when this authorization code was deleted. Read only.

        effective_date : typing.Optional[dt.datetime]
            A date at which this code should begin being valid. Optional. Set on create only.

        id : typing.Optional[int]
            The identifier for the authorization code. Read only.

        is_deleted : typing.Optional[bool]
            Indicates whether this code is deleted.

        validation_parameters : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]]
            The parameters and values used to validate this authorization code. May not be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/AuthorizationCodes",
            method="POST",
            json={
                "Code": code,
                "CreatedByUserID": created_by_user_id,
                "CreatedDate": created_date,
                "DataParameters": convert_and_respect_annotation_metadata(
                    object_=data_parameters,
                    annotation=typing.Sequence[AuthorizationCodesSharedModelsParameter],
                    direction="write",
                ),
                "DefinitionID": definition_id,
                "DeletedByUserID": deleted_by_user_id,
                "DeletedDate": deleted_date,
                "EffectiveDate": effective_date,
                "ID": id,
                "IsDeleted": is_deleted,
                "ValidationParameters": convert_and_respect_annotation_metadata(
                    object_=validation_parameters,
                    annotation=typing.Sequence[AuthorizationCodesSharedModelsParameter],
                    direction="write",
                ),
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

    def getauthorizationcode(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AuthorizationCodesSharedModelsAuthorizationCode]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The id of the authorization code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AuthorizationCodesSharedModelsAuthorizationCode]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/AuthorizationCodes/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AuthorizationCodesSharedModelsAuthorizationCode,
                    parse_obj_as(
                        type_=AuthorizationCodesSharedModelsAuthorizationCode,
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

    def putauthorizationcode(
        self,
        id_: int,
        *,
        code: typing.Optional[str] = OMIT,
        created_by_user_id: typing.Optional[int] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        data_parameters: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]] = OMIT,
        definition_id: typing.Optional[str] = OMIT,
        deleted_by_user_id: typing.Optional[int] = OMIT,
        deleted_date: typing.Optional[dt.datetime] = OMIT,
        effective_date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_deleted: typing.Optional[bool] = OMIT,
        validation_parameters: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int
            The id of the authorization code.

        code : typing.Optional[str]
            The code to enter to unlock a feature. Read only.

        created_by_user_id : typing.Optional[int]
            The ID of the user that created this authorization code. Read only.

        created_date : typing.Optional[dt.datetime]
            A timestamp of when this code was created. Read only.

        data_parameters : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]]
            The parameters and values contained as data in this authorization code. May not be updated.

        definition_id : typing.Optional[str]
            The id of the definition for this authorization code. May not be updated.

        deleted_by_user_id : typing.Optional[int]
            The ID of the user that deleted this authorization code. Read only.

        deleted_date : typing.Optional[dt.datetime]
            A timestamp of when this authorization code was deleted. Read only.

        effective_date : typing.Optional[dt.datetime]
            A date at which this code should begin being valid. Optional. Set on create only.

        id : typing.Optional[int]
            The identifier for the authorization code. Read only.

        is_deleted : typing.Optional[bool]
            Indicates whether this code is deleted.

        validation_parameters : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]]
            The parameters and values used to validate this authorization code. May not be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/AuthorizationCodes/{encode_path_param(id_)}",
            method="PUT",
            json={
                "Code": code,
                "CreatedByUserID": created_by_user_id,
                "CreatedDate": created_date,
                "DataParameters": convert_and_respect_annotation_metadata(
                    object_=data_parameters,
                    annotation=typing.Sequence[AuthorizationCodesSharedModelsParameter],
                    direction="write",
                ),
                "DefinitionID": definition_id,
                "DeletedByUserID": deleted_by_user_id,
                "DeletedDate": deleted_date,
                "EffectiveDate": effective_date,
                "ID": id,
                "IsDeleted": is_deleted,
                "ValidationParameters": convert_and_respect_annotation_metadata(
                    object_=validation_parameters,
                    annotation=typing.Sequence[AuthorizationCodesSharedModelsParameter],
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

    def deleteauthorizationcode(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The id of the authorization code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/AuthorizationCodes/{encode_path_param(id)}",
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

    def getcontactinformation(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AuthorizationCodesSharedModelsAuthorizationContactInformation]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The id of the authorization code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AuthorizationCodesSharedModelsAuthorizationContactInformation]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/AuthorizationCodes/{encode_path_param(id)}/ContactInformation",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AuthorizationCodesSharedModelsAuthorizationContactInformation,
                    parse_obj_as(
                        type_=AuthorizationCodesSharedModelsAuthorizationContactInformation,
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

    def validateauthorizationcode(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AuthorizationCodesSharedModelsCodeValidationModel]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AuthorizationCodesSharedModelsCodeValidationModel]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/AuthorizationCodes/{encode_path_param(id)}/Validate",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AuthorizationCodesSharedModelsCodeValidationModel,
                    parse_obj_as(
                        type_=AuthorizationCodesSharedModelsCodeValidationModel,
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


class AsyncRawAuthorizationcodesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getauthorizationcodes(
        self,
        *,
        code: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        definition_id: typing.Optional[str] = None,
        created_by_user_id: typing.Optional[int] = None,
        deleted_by_user_id: typing.Optional[int] = None,
        include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode]:
        """
        Additional searches: validationParameters[Name]=Value and dataParameters[Name]=Value. These can be used to search for authorization codes that have been generated using specified values for data or validation parameters.

        Parameters
        ----------
        code : typing.Optional[str]
            Optional. If provided, searches for entities with the provided authorization code.

        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        definition_id : typing.Optional[str]
            Optional. If specified, filters codes by definition id.

        created_by_user_id : typing.Optional[int]
            Optional. If specified, filters codes to those created by the given User ID.

        deleted_by_user_id : typing.Optional[int]
            Optional. If specified, filters codes to those deleted by the given User ID.

        include_deleted : typing.Optional[bool]
            Optional. Whether to include deleted codes. 'False' by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/AuthorizationCodes",
            method="GET",
            params={
                "code": code,
                "limit": limit,
                "offset": offset,
                "definitionID": definition_id,
                "createdByUserID": created_by_user_id,
                "deletedByUserID": deleted_by_user_id,
                "includeDeleted": include_deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode,
                    parse_obj_as(
                        type_=ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode,
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

    async def postauthorizationcode(
        self,
        *,
        code: typing.Optional[str] = OMIT,
        created_by_user_id: typing.Optional[int] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        data_parameters: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]] = OMIT,
        definition_id: typing.Optional[str] = OMIT,
        deleted_by_user_id: typing.Optional[int] = OMIT,
        deleted_date: typing.Optional[dt.datetime] = OMIT,
        effective_date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_deleted: typing.Optional[bool] = OMIT,
        validation_parameters: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        code : typing.Optional[str]
            The code to enter to unlock a feature. Read only.

        created_by_user_id : typing.Optional[int]
            The ID of the user that created this authorization code. Read only.

        created_date : typing.Optional[dt.datetime]
            A timestamp of when this code was created. Read only.

        data_parameters : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]]
            The parameters and values contained as data in this authorization code. May not be updated.

        definition_id : typing.Optional[str]
            The id of the definition for this authorization code. May not be updated.

        deleted_by_user_id : typing.Optional[int]
            The ID of the user that deleted this authorization code. Read only.

        deleted_date : typing.Optional[dt.datetime]
            A timestamp of when this authorization code was deleted. Read only.

        effective_date : typing.Optional[dt.datetime]
            A date at which this code should begin being valid. Optional. Set on create only.

        id : typing.Optional[int]
            The identifier for the authorization code. Read only.

        is_deleted : typing.Optional[bool]
            Indicates whether this code is deleted.

        validation_parameters : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]]
            The parameters and values used to validate this authorization code. May not be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/AuthorizationCodes",
            method="POST",
            json={
                "Code": code,
                "CreatedByUserID": created_by_user_id,
                "CreatedDate": created_date,
                "DataParameters": convert_and_respect_annotation_metadata(
                    object_=data_parameters,
                    annotation=typing.Sequence[AuthorizationCodesSharedModelsParameter],
                    direction="write",
                ),
                "DefinitionID": definition_id,
                "DeletedByUserID": deleted_by_user_id,
                "DeletedDate": deleted_date,
                "EffectiveDate": effective_date,
                "ID": id,
                "IsDeleted": is_deleted,
                "ValidationParameters": convert_and_respect_annotation_metadata(
                    object_=validation_parameters,
                    annotation=typing.Sequence[AuthorizationCodesSharedModelsParameter],
                    direction="write",
                ),
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

    async def getauthorizationcode(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AuthorizationCodesSharedModelsAuthorizationCode]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The id of the authorization code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AuthorizationCodesSharedModelsAuthorizationCode]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/AuthorizationCodes/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AuthorizationCodesSharedModelsAuthorizationCode,
                    parse_obj_as(
                        type_=AuthorizationCodesSharedModelsAuthorizationCode,
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

    async def putauthorizationcode(
        self,
        id_: int,
        *,
        code: typing.Optional[str] = OMIT,
        created_by_user_id: typing.Optional[int] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        data_parameters: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]] = OMIT,
        definition_id: typing.Optional[str] = OMIT,
        deleted_by_user_id: typing.Optional[int] = OMIT,
        deleted_date: typing.Optional[dt.datetime] = OMIT,
        effective_date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_deleted: typing.Optional[bool] = OMIT,
        validation_parameters: typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int
            The id of the authorization code.

        code : typing.Optional[str]
            The code to enter to unlock a feature. Read only.

        created_by_user_id : typing.Optional[int]
            The ID of the user that created this authorization code. Read only.

        created_date : typing.Optional[dt.datetime]
            A timestamp of when this code was created. Read only.

        data_parameters : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]]
            The parameters and values contained as data in this authorization code. May not be updated.

        definition_id : typing.Optional[str]
            The id of the definition for this authorization code. May not be updated.

        deleted_by_user_id : typing.Optional[int]
            The ID of the user that deleted this authorization code. Read only.

        deleted_date : typing.Optional[dt.datetime]
            A timestamp of when this authorization code was deleted. Read only.

        effective_date : typing.Optional[dt.datetime]
            A date at which this code should begin being valid. Optional. Set on create only.

        id : typing.Optional[int]
            The identifier for the authorization code. Read only.

        is_deleted : typing.Optional[bool]
            Indicates whether this code is deleted.

        validation_parameters : typing.Optional[typing.Sequence[AuthorizationCodesSharedModelsParameter]]
            The parameters and values used to validate this authorization code. May not be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/AuthorizationCodes/{encode_path_param(id_)}",
            method="PUT",
            json={
                "Code": code,
                "CreatedByUserID": created_by_user_id,
                "CreatedDate": created_date,
                "DataParameters": convert_and_respect_annotation_metadata(
                    object_=data_parameters,
                    annotation=typing.Sequence[AuthorizationCodesSharedModelsParameter],
                    direction="write",
                ),
                "DefinitionID": definition_id,
                "DeletedByUserID": deleted_by_user_id,
                "DeletedDate": deleted_date,
                "EffectiveDate": effective_date,
                "ID": id,
                "IsDeleted": is_deleted,
                "ValidationParameters": convert_and_respect_annotation_metadata(
                    object_=validation_parameters,
                    annotation=typing.Sequence[AuthorizationCodesSharedModelsParameter],
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

    async def deleteauthorizationcode(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The id of the authorization code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/AuthorizationCodes/{encode_path_param(id)}",
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

    async def getcontactinformation(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AuthorizationCodesSharedModelsAuthorizationContactInformation]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            The id of the authorization code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AuthorizationCodesSharedModelsAuthorizationContactInformation]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/AuthorizationCodes/{encode_path_param(id)}/ContactInformation",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AuthorizationCodesSharedModelsAuthorizationContactInformation,
                    parse_obj_as(
                        type_=AuthorizationCodesSharedModelsAuthorizationContactInformation,
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

    async def validateauthorizationcode(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AuthorizationCodesSharedModelsCodeValidationModel]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AuthorizationCodesSharedModelsCodeValidationModel]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/AuthorizationCodes/{encode_path_param(id)}/Validate",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AuthorizationCodesSharedModelsCodeValidationModel,
                    parse_obj_as(
                        type_=AuthorizationCodesSharedModelsCodeValidationModel,
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
