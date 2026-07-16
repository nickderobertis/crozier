

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.session_server_create import SessionServerCreate
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSessionServerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_session_server(
        self, *, secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SessionServerCreate]:
        """
        Create a new session for a DeviceServer. Provide the Installation token in the "X-Bunq-Client-Authentication" header. And don't forget to create the "X-Bunq-Client-Signature" header. The response contains a Session token that should be used for as the "X-Bunq-Client-Authentication" header for all future API calls. The ip address making this call needs to match the ip address bound to your API key.

        Parameters
        ----------
        secret : str
            The API key of the user you want to login. If your API key has not been used before, it will be bound to the ip address of this DeviceServer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SessionServerCreate]
            Once you have created an Installation and a DeviceServer with that Installation, then you are ready to start a session! A session expires after the same amount of time you have set for Auto Logout in your user account. By default this is 1 week. If a request is made 30 seconds before a session expires, it will be extended from that moment by your auto logout time, but never by more than 5 minutes.
        """
        _response = self._client_wrapper.httpx_client.request(
            "session-server",
            method="POST",
            json={
                "secret": secret,
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
                    SessionServerCreate,
                    parse_obj_as(
                        type_=SessionServerCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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


class AsyncRawSessionServerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_session_server(
        self, *, secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SessionServerCreate]:
        """
        Create a new session for a DeviceServer. Provide the Installation token in the "X-Bunq-Client-Authentication" header. And don't forget to create the "X-Bunq-Client-Signature" header. The response contains a Session token that should be used for as the "X-Bunq-Client-Authentication" header for all future API calls. The ip address making this call needs to match the ip address bound to your API key.

        Parameters
        ----------
        secret : str
            The API key of the user you want to login. If your API key has not been used before, it will be bound to the ip address of this DeviceServer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SessionServerCreate]
            Once you have created an Installation and a DeviceServer with that Installation, then you are ready to start a session! A session expires after the same amount of time you have set for Auto Logout in your user account. By default this is 1 week. If a request is made 30 seconds before a session expires, it will be extended from that moment by your auto logout time, but never by more than 5 minutes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "session-server",
            method="POST",
            json={
                "secret": secret,
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
                    SessionServerCreate,
                    parse_obj_as(
                        type_=SessionServerCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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
