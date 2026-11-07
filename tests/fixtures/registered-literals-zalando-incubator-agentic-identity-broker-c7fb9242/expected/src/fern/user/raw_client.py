

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
from ..types.get_user_info_response import GetUserInfoResponse
from pydantic import ValidationError


class RawUserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_current_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetUserInfoResponse]:
        """
        Returns information about the currently authenticated user.

        The user information includes:

        - **Principal**: Unique identifier (email, UUID, etc.) from authentication system
        - **Display Name**: Human-readable name for display in UI
        - **Picture URL**: Optional avatar/profile picture URL

        The principal is extracted from the `X-Remote-User` header set by the upstream authentication proxy (oauth2-proxy, nginx, etc.).

        **Use Cases**:

        - Display user info in application header
        - Show "logged in as" indicators
        - Personalize UI with user's name/avatar
        - Verify authentication status

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetUserInfoResponse]
            User information retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUserInfoResponse,
                    parse_obj_as(
                        type_=GetUserInfoResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_current_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetUserInfoResponse]:
        """
        Returns information about the currently authenticated user.

        The user information includes:

        - **Principal**: Unique identifier (email, UUID, etc.) from authentication system
        - **Display Name**: Human-readable name for display in UI
        - **Picture URL**: Optional avatar/profile picture URL

        The principal is extracted from the `X-Remote-User` header set by the upstream authentication proxy (oauth2-proxy, nginx, etc.).

        **Use Cases**:

        - Display user info in application header
        - Show "logged in as" indicators
        - Personalize UI with user's name/avatar
        - Verify authentication status

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetUserInfoResponse]
            User information retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUserInfoResponse,
                    parse_obj_as(
                        type_=GetUserInfoResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
