

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.get_user_sent_private_messages_response import GetUserSentPrivateMessagesResponse
from .types.list_user_private_messages_response import ListUserPrivateMessagesResponse


class RawPrivateMessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_user_sent_private_messages(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetUserSentPrivateMessagesResponse]:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetUserSentPrivateMessagesResponse]
            private messages
        """
        _response = self._client_wrapper.httpx_client.request(
            f"topics/private-messages-sent/{jsonable_encoder(username)}.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUserSentPrivateMessagesResponse,
                    parse_obj_as(
                        type_=GetUserSentPrivateMessagesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_user_private_messages(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListUserPrivateMessagesResponse]:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListUserPrivateMessagesResponse]
            private messages
        """
        _response = self._client_wrapper.httpx_client.request(
            f"topics/private-messages/{jsonable_encoder(username)}.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListUserPrivateMessagesResponse,
                    parse_obj_as(
                        type_=ListUserPrivateMessagesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPrivateMessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_user_sent_private_messages(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetUserSentPrivateMessagesResponse]:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetUserSentPrivateMessagesResponse]
            private messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"topics/private-messages-sent/{jsonable_encoder(username)}.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUserSentPrivateMessagesResponse,
                    parse_obj_as(
                        type_=GetUserSentPrivateMessagesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_user_private_messages(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListUserPrivateMessagesResponse]:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListUserPrivateMessagesResponse]
            private messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"topics/private-messages/{jsonable_encoder(username)}.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListUserPrivateMessagesResponse,
                    parse_obj_as(
                        type_=ListUserPrivateMessagesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
