

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .types.toggle_assistant_request_channels_item import ToggleAssistantRequestChannelsItem
from .types.toggle_assistant_response import ToggleAssistantResponse
from pydantic import ValidationError


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def toggle_assistant(
        self,
        *,
        channels: typing.Optional[typing.Sequence[ToggleAssistantRequestChannelsItem]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ToggleAssistantResponse]:
        """
        Parameters
        ----------
        channels : typing.Optional[typing.Sequence[ToggleAssistantRequestChannelsItem]]
            Where the assistant answers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ToggleAssistantResponse]
            Toggled.
        """
        _response = self._client_wrapper.httpx_client.request(
            "assistant/toggle",
            method="POST",
            params={
                "channels": channels,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToggleAssistantResponse,
                    parse_obj_as(
                        type_=ToggleAssistantResponse,
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def toggle_assistant(
        self,
        *,
        channels: typing.Optional[typing.Sequence[ToggleAssistantRequestChannelsItem]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ToggleAssistantResponse]:
        """
        Parameters
        ----------
        channels : typing.Optional[typing.Sequence[ToggleAssistantRequestChannelsItem]]
            Where the assistant answers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ToggleAssistantResponse]
            Toggled.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assistant/toggle",
            method="POST",
            params={
                "channels": channels,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToggleAssistantResponse,
                    parse_obj_as(
                        type_=ToggleAssistantResponse,
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
