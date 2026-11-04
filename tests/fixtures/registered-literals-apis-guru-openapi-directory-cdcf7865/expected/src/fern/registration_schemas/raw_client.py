

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.registration_schema_read_response import RegistrationSchemaReadResponse
from .types.registration_schemas_list_response import RegistrationSchemasListResponse
from pydantic import ValidationError


class RawRegistrationSchemasClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RegistrationSchemasListResponse]:
        """
        Retrieve a paginated list of all active Registration Schemas. Registration Schemas describe the supplemental questions that accompany a registration. Registration Schemas are read-only for API users.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.
        The `data` key contains an array of 10 Registration Schemas. Each resource in the array is a separate Registration Schemas object.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Errors
        This request should never return an error.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RegistrationSchemasListResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "schemas/registrations/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegistrationSchemasListResponse,
                    parse_obj_as(
                        type_=RegistrationSchemasListResponse,
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

    def registration_schema_read(
        self, registration_schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RegistrationSchemaReadResponse]:
        """
        Retrieves the details of a given Registration Schema. Registration Schemas defines the desired supplemental information that should accompany be included in a Registration. Registration Schemas are Read-only to API users.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Registration Schemas, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        registration_schema_id : str
            The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RegistrationSchemaReadResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"schemas/registrations/{encode_path_param(registration_schema_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegistrationSchemaReadResponse,
                    parse_obj_as(
                        type_=RegistrationSchemaReadResponse,
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


class AsyncRawRegistrationSchemasClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RegistrationSchemasListResponse]:
        """
        Retrieve a paginated list of all active Registration Schemas. Registration Schemas describe the supplemental questions that accompany a registration. Registration Schemas are read-only for API users.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.
        The `data` key contains an array of 10 Registration Schemas. Each resource in the array is a separate Registration Schemas object.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Errors
        This request should never return an error.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RegistrationSchemasListResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "schemas/registrations/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegistrationSchemasListResponse,
                    parse_obj_as(
                        type_=RegistrationSchemasListResponse,
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

    async def registration_schema_read(
        self, registration_schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RegistrationSchemaReadResponse]:
        """
        Retrieves the details of a given Registration Schema. Registration Schemas defines the desired supplemental information that should accompany be included in a Registration. Registration Schemas are Read-only to API users.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Registration Schemas, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        registration_schema_id : str
            The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RegistrationSchemaReadResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"schemas/registrations/{encode_path_param(registration_schema_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegistrationSchemaReadResponse,
                    parse_obj_as(
                        type_=RegistrationSchemaReadResponse,
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
