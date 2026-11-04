

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.user_status_user_status_get_status200response import UserStatusUserStatusGetStatus200Response
from pydantic import ValidationError


class RawUserStatusHeartbeatClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def heartbeat(
        self, *, status: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserStatusUserStatusGetStatus200Response]:
        """
        Parameters
        ----------
        status : str
            Only online, away

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserStatusUserStatusGetStatus200Response]
            Status successfully updated
        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/user_status/api/v1/heartbeat",
            method="PUT",
            params={
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserStatusUserStatusGetStatus200Response,
                    parse_obj_as(
                        type_=UserStatusUserStatusGetStatus200Response,
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


class AsyncRawUserStatusHeartbeatClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def heartbeat(
        self, *, status: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserStatusUserStatusGetStatus200Response]:
        """
        Parameters
        ----------
        status : str
            Only online, away

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserStatusUserStatusGetStatus200Response]
            Status successfully updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/user_status/api/v1/heartbeat",
            method="PUT",
            params={
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserStatusUserStatusGetStatus200Response,
                    parse_obj_as(
                        type_=UserStatusUserStatusGetStatus200Response,
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
