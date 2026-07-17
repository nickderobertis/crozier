

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error import Error
from .types.push_login_request_response import PushLoginRequestResponse
from pydantic import ValidationError


class RawLoginClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def push_login_request(
        self, *, callback: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PushLoginRequestResponse]:
        """
        push sign-in request
        See: https://github.com/skion/authentiq/wiki/JWT-Examples

        Parameters
        ----------
        callback : str
            URI App will connect to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PushLoginRequestResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "login",
            method="POST",
            params={
                "callback": callback,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PushLoginRequestResponse,
                    parse_obj_as(
                        type_=PushLoginRequestResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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


class AsyncRawLoginClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def push_login_request(
        self, *, callback: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PushLoginRequestResponse]:
        """
        push sign-in request
        See: https://github.com/skion/authentiq/wiki/JWT-Examples

        Parameters
        ----------
        callback : str
            URI App will connect to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PushLoginRequestResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "login",
            method="POST",
            params={
                "callback": callback,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PushLoginRequestResponse,
                    parse_obj_as(
                        type_=PushLoginRequestResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
