

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.common_base_error import CommonBaseError
from ..types.internal_create_telemetry_entry_response import InternalCreateTelemetryEntryResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawInternalTelemetryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def internal_telemetry_create_telemetry_entry(
        self,
        *,
        number_of_users: int,
        number_of_accounts: int,
        number_of_connections: int,
        number_of_api_calls: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InternalCreateTelemetryEntryResponse]:
        """
        Create telemetry entry for a deployment

        Parameters
        ----------
        number_of_users : int

        number_of_accounts : int

        number_of_connections : int

        number_of_api_calls : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InternalCreateTelemetryEntryResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "internal/telemetry",
            method="POST",
            json={
                "numberOfUsers": number_of_users,
                "numberOfAccounts": number_of_accounts,
                "numberOfConnections": number_of_connections,
                "numberOfApiCalls": number_of_api_calls,
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
                    InternalCreateTelemetryEntryResponse,
                    parse_obj_as(
                        type_=InternalCreateTelemetryEntryResponse,
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


class AsyncRawInternalTelemetryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def internal_telemetry_create_telemetry_entry(
        self,
        *,
        number_of_users: int,
        number_of_accounts: int,
        number_of_connections: int,
        number_of_api_calls: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InternalCreateTelemetryEntryResponse]:
        """
        Create telemetry entry for a deployment

        Parameters
        ----------
        number_of_users : int

        number_of_accounts : int

        number_of_connections : int

        number_of_api_calls : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InternalCreateTelemetryEntryResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "internal/telemetry",
            method="POST",
            json={
                "numberOfUsers": number_of_users,
                "numberOfAccounts": number_of_accounts,
                "numberOfConnections": number_of_connections,
                "numberOfApiCalls": number_of_api_calls,
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
                    InternalCreateTelemetryEntryResponse,
                    parse_obj_as(
                        type_=InternalCreateTelemetryEntryResponse,
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
