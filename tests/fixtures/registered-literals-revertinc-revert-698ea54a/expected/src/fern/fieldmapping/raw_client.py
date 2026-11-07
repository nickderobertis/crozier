

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.common_base_error import CommonBaseError
from ..types.create_account_field_mapping_response import CreateAccountFieldMappingResponse
from ..types.create_field_mapping_response import CreateFieldMappingResponse
from ..types.delete_account_field_mapping_config_response import DeleteAccountFieldMappingConfigResponse
from ..types.delete_field_mapping_response import DeleteFieldMappingResponse
from ..types.field_mapping_type import FieldMappingType
from ..types.get_field_mapping_config_response import GetFieldMappingConfigResponse
from ..types.get_field_mappings_response import GetFieldMappingsResponse
from ..types.mappable_field_type import MappableFieldType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFieldmappingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getfieldmappingconfig(
        self,
        *,
        revert_public_token: str,
        revert_t_id: str,
        revert_t_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetFieldMappingConfigResponse]:
        """
        Get field mappings configs for a connection

        Parameters
        ----------
        revert_public_token : str
            Your public key, to be used on the frontend usually.

        revert_t_id : str
            The unique customer id used when the customer linked their account.

        revert_t_token : str
            The temp used to identify tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetFieldMappingConfigResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "field-mapping",
            method="GET",
            headers={
                "x-revert-public-token": str(revert_public_token) if revert_public_token is not None else None,
                "x-revert-t-id": str(revert_t_id) if revert_t_id is not None else None,
                "x-revert-t-token": str(revert_t_token) if revert_t_token is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFieldMappingConfigResponse,
                    parse_obj_as(
                        type_=GetFieldMappingConfigResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def createfieldmapping(
        self,
        *,
        revert_public_token: str,
        revert_t_id: str,
        revert_t_token: str,
        standard_mappings: typing.Sequence[FieldMappingType],
        custom_mappings: typing.Sequence[FieldMappingType],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateFieldMappingResponse]:
        """
        Create field mappings for a connection after user input

        Parameters
        ----------
        revert_public_token : str
            Your public key, to be used on the frontend usually.

        revert_t_id : str
            The unique customer id used when the customer linked their account.

        revert_t_token : str
            The temp used to identify tenant.

        standard_mappings : typing.Sequence[FieldMappingType]

        custom_mappings : typing.Sequence[FieldMappingType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateFieldMappingResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "field-mapping",
            method="POST",
            json={
                "standardMappings": convert_and_respect_annotation_metadata(
                    object_=standard_mappings, annotation=typing.Sequence[FieldMappingType], direction="write"
                ),
                "customMappings": convert_and_respect_annotation_metadata(
                    object_=custom_mappings, annotation=typing.Sequence[FieldMappingType], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "x-revert-public-token": str(revert_public_token) if revert_public_token is not None else None,
                "x-revert-t-id": str(revert_t_id) if revert_t_id is not None else None,
                "x-revert-t-token": str(revert_t_token) if revert_t_token is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateFieldMappingResponse,
                    parse_obj_as(
                        type_=CreateFieldMappingResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def deletefieldmapping(
        self, *, revert_api_token: str, revert_t_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteFieldMappingResponse]:
        """
        Delete field mappings for a connection

        Parameters
        ----------
        revert_api_token : str
            Your official API key for accessing revert apis.

        revert_t_id : str
            The unique customer id used when the customer linked their account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteFieldMappingResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "field-mapping",
            method="DELETE",
            headers={
                "x-revert-api-token": str(revert_api_token) if revert_api_token is not None else None,
                "x-revert-t-id": str(revert_t_id) if revert_t_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteFieldMappingResponse,
                    parse_obj_as(
                        type_=DeleteFieldMappingResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getfieldmappings(
        self, *, revert_api_token: str, revert_t_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetFieldMappingsResponse]:
        """
        Get field mappings for a connection

        Parameters
        ----------
        revert_api_token : str
            Your official API key for accessing revert apis.

        revert_t_id : str
            The unique customer id used when the customer linked their account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetFieldMappingsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "field-mapping/mappings",
            method="GET",
            headers={
                "x-revert-api-token": str(revert_api_token) if revert_api_token is not None else None,
                "x-revert-t-id": str(revert_t_id) if revert_t_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFieldMappingsResponse,
                    parse_obj_as(
                        type_=GetFieldMappingsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def createaccountfieldmappingconfig(
        self,
        *,
        revert_api_token: str,
        allow_connection_override_custom_fields: bool,
        mappable_by_connection_field_list: typing.Sequence[MappableFieldType],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateAccountFieldMappingResponse]:
        """
        Create field mappings config for an account

        Parameters
        ----------
        revert_api_token : str
            Your official API key for accessing revert apis.

        allow_connection_override_custom_fields : bool

        mappable_by_connection_field_list : typing.Sequence[MappableFieldType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateAccountFieldMappingResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "field-mapping/config",
            method="POST",
            json={
                "allow_connection_override_custom_fields": allow_connection_override_custom_fields,
                "mappable_by_connection_field_list": convert_and_respect_annotation_metadata(
                    object_=mappable_by_connection_field_list,
                    annotation=typing.Sequence[MappableFieldType],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
                "x-revert-api-token": str(revert_api_token) if revert_api_token is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateAccountFieldMappingResponse,
                    parse_obj_as(
                        type_=CreateAccountFieldMappingResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def deleteaccountfieldmappingconfig(
        self, *, revert_api_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteAccountFieldMappingConfigResponse]:
        """
        Delete field mappings config for an account

        Parameters
        ----------
        revert_api_token : str
            Your official API key for accessing revert apis.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteAccountFieldMappingConfigResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "field-mapping/config",
            method="DELETE",
            headers={
                "x-revert-api-token": str(revert_api_token) if revert_api_token is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteAccountFieldMappingConfigResponse,
                    parse_obj_as(
                        type_=DeleteAccountFieldMappingConfigResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFieldmappingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getfieldmappingconfig(
        self,
        *,
        revert_public_token: str,
        revert_t_id: str,
        revert_t_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetFieldMappingConfigResponse]:
        """
        Get field mappings configs for a connection

        Parameters
        ----------
        revert_public_token : str
            Your public key, to be used on the frontend usually.

        revert_t_id : str
            The unique customer id used when the customer linked their account.

        revert_t_token : str
            The temp used to identify tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetFieldMappingConfigResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "field-mapping",
            method="GET",
            headers={
                "x-revert-public-token": str(revert_public_token) if revert_public_token is not None else None,
                "x-revert-t-id": str(revert_t_id) if revert_t_id is not None else None,
                "x-revert-t-token": str(revert_t_token) if revert_t_token is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFieldMappingConfigResponse,
                    parse_obj_as(
                        type_=GetFieldMappingConfigResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def createfieldmapping(
        self,
        *,
        revert_public_token: str,
        revert_t_id: str,
        revert_t_token: str,
        standard_mappings: typing.Sequence[FieldMappingType],
        custom_mappings: typing.Sequence[FieldMappingType],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateFieldMappingResponse]:
        """
        Create field mappings for a connection after user input

        Parameters
        ----------
        revert_public_token : str
            Your public key, to be used on the frontend usually.

        revert_t_id : str
            The unique customer id used when the customer linked their account.

        revert_t_token : str
            The temp used to identify tenant.

        standard_mappings : typing.Sequence[FieldMappingType]

        custom_mappings : typing.Sequence[FieldMappingType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateFieldMappingResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "field-mapping",
            method="POST",
            json={
                "standardMappings": convert_and_respect_annotation_metadata(
                    object_=standard_mappings, annotation=typing.Sequence[FieldMappingType], direction="write"
                ),
                "customMappings": convert_and_respect_annotation_metadata(
                    object_=custom_mappings, annotation=typing.Sequence[FieldMappingType], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "x-revert-public-token": str(revert_public_token) if revert_public_token is not None else None,
                "x-revert-t-id": str(revert_t_id) if revert_t_id is not None else None,
                "x-revert-t-token": str(revert_t_token) if revert_t_token is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateFieldMappingResponse,
                    parse_obj_as(
                        type_=CreateFieldMappingResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def deletefieldmapping(
        self, *, revert_api_token: str, revert_t_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteFieldMappingResponse]:
        """
        Delete field mappings for a connection

        Parameters
        ----------
        revert_api_token : str
            Your official API key for accessing revert apis.

        revert_t_id : str
            The unique customer id used when the customer linked their account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteFieldMappingResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "field-mapping",
            method="DELETE",
            headers={
                "x-revert-api-token": str(revert_api_token) if revert_api_token is not None else None,
                "x-revert-t-id": str(revert_t_id) if revert_t_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteFieldMappingResponse,
                    parse_obj_as(
                        type_=DeleteFieldMappingResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getfieldmappings(
        self, *, revert_api_token: str, revert_t_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetFieldMappingsResponse]:
        """
        Get field mappings for a connection

        Parameters
        ----------
        revert_api_token : str
            Your official API key for accessing revert apis.

        revert_t_id : str
            The unique customer id used when the customer linked their account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetFieldMappingsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "field-mapping/mappings",
            method="GET",
            headers={
                "x-revert-api-token": str(revert_api_token) if revert_api_token is not None else None,
                "x-revert-t-id": str(revert_t_id) if revert_t_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFieldMappingsResponse,
                    parse_obj_as(
                        type_=GetFieldMappingsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def createaccountfieldmappingconfig(
        self,
        *,
        revert_api_token: str,
        allow_connection_override_custom_fields: bool,
        mappable_by_connection_field_list: typing.Sequence[MappableFieldType],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateAccountFieldMappingResponse]:
        """
        Create field mappings config for an account

        Parameters
        ----------
        revert_api_token : str
            Your official API key for accessing revert apis.

        allow_connection_override_custom_fields : bool

        mappable_by_connection_field_list : typing.Sequence[MappableFieldType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateAccountFieldMappingResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "field-mapping/config",
            method="POST",
            json={
                "allow_connection_override_custom_fields": allow_connection_override_custom_fields,
                "mappable_by_connection_field_list": convert_and_respect_annotation_metadata(
                    object_=mappable_by_connection_field_list,
                    annotation=typing.Sequence[MappableFieldType],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
                "x-revert-api-token": str(revert_api_token) if revert_api_token is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateAccountFieldMappingResponse,
                    parse_obj_as(
                        type_=CreateAccountFieldMappingResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def deleteaccountfieldmappingconfig(
        self, *, revert_api_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteAccountFieldMappingConfigResponse]:
        """
        Delete field mappings config for an account

        Parameters
        ----------
        revert_api_token : str
            Your official API key for accessing revert apis.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteAccountFieldMappingConfigResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "field-mapping/config",
            method="DELETE",
            headers={
                "x-revert-api-token": str(revert_api_token) if revert_api_token is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteAccountFieldMappingConfigResponse,
                    parse_obj_as(
                        type_=DeleteAccountFieldMappingConfigResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
