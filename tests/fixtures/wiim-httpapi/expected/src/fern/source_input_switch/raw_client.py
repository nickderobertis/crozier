

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.request_options import RequestOptions
from .types.set_player_cmd_switch_mode_request_mode import SetPlayerCmdSwitchModeRequestMode
from pydantic import ValidationError


class RawSourceInputSwitchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def set_player_cmd_switch_mode(
        self, mode: SetPlayerCmdSwitchModeRequestMode, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        http://10.10.10.254/httpapi.asp?command=setPlayerCmd:switchmode:%s

        the mode can be the text as below:
        - line-in (it refers to aux-in too)
        - bluetooth
        - optical
        - udisk
        - wifi
        - HDMI

        Parameters
        ----------
        mode : SetPlayerCmdSwitchModeRequestMode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"setPlayerCmd:switchmode:{encode_path_param(mode)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSourceInputSwitchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def set_player_cmd_switch_mode(
        self, mode: SetPlayerCmdSwitchModeRequestMode, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        http://10.10.10.254/httpapi.asp?command=setPlayerCmd:switchmode:%s

        the mode can be the text as below:
        - line-in (it refers to aux-in too)
        - bluetooth
        - optical
        - udisk
        - wifi
        - HDMI

        Parameters
        ----------
        mode : SetPlayerCmdSwitchModeRequestMode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"setPlayerCmd:switchmode:{encode_path_param(mode)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
