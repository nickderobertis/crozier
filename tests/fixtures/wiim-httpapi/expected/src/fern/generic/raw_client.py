

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.request_options import RequestOptions
from pydantic import ValidationError


class RawGenericClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def command(self, command: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[str]:
        """
        Generic command to the device. All calls will follow the format /httpapi.asp?command={command}.


        The actual command is passed as a path parameter. With this, you can test out any command that is not explicitly defined in this API.

        The response could be a simple 'OK' or an object with data. The actual response will depend on the command sent. If you get an 'unknown command' response, the command is not supported by the device.


        Examples:
        -  'getStatusEx' will do an /httpapi.asp?command=getStatusEx
        -  'setPlayerCmd:pause' will do an /httpapi.asp?command=setPlayerCmd:pause
        -  'setPlayerCmd:resume' will do an /httpapi.asp?command=setPlayerCmd:resume

        Parameters
        ----------
        command : str
            The actual command to send to the device. Note that the command is case-sensitive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{encode_path_param(command)}",
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


class AsyncRawGenericClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def command(
        self, command: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Generic command to the device. All calls will follow the format /httpapi.asp?command={command}.


        The actual command is passed as a path parameter. With this, you can test out any command that is not explicitly defined in this API.

        The response could be a simple 'OK' or an object with data. The actual response will depend on the command sent. If you get an 'unknown command' response, the command is not supported by the device.


        Examples:
        -  'getStatusEx' will do an /httpapi.asp?command=getStatusEx
        -  'setPlayerCmd:pause' will do an /httpapi.asp?command=setPlayerCmd:pause
        -  'setPlayerCmd:resume' will do an /httpapi.asp?command=setPlayerCmd:resume

        Parameters
        ----------
        command : str
            The actual command to send to the device. Note that the command is case-sensitive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{encode_path_param(command)}",
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
