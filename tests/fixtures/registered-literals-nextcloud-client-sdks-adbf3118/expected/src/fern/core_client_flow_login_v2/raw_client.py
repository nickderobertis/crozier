

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.core_login_flow_v2 import CoreLoginFlowV2
from ..types.core_login_flow_v2credentials import CoreLoginFlowV2Credentials
from pydantic import ValidationError


class RawCoreClientFlowLoginV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def poll(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreLoginFlowV2Credentials]:
        """
        Parameters
        ----------
        token : str
            Token of the flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreLoginFlowV2Credentials]
            Login flow credentials returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "index.php/login/v2/poll",
            method="POST",
            params={
                "token": token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreLoginFlowV2Credentials,
                    parse_obj_as(
                        type_=CoreLoginFlowV2Credentials,
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

    def init(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[CoreLoginFlowV2]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreLoginFlowV2]

        """
        _response = self._client_wrapper.httpx_client.request(
            "index.php/login/v2",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreLoginFlowV2,
                    parse_obj_as(
                        type_=CoreLoginFlowV2,
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


class AsyncRawCoreClientFlowLoginV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def poll(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreLoginFlowV2Credentials]:
        """
        Parameters
        ----------
        token : str
            Token of the flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreLoginFlowV2Credentials]
            Login flow credentials returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "index.php/login/v2/poll",
            method="POST",
            params={
                "token": token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreLoginFlowV2Credentials,
                    parse_obj_as(
                        type_=CoreLoginFlowV2Credentials,
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

    async def init(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreLoginFlowV2]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreLoginFlowV2]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "index.php/login/v2",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreLoginFlowV2,
                    parse_obj_as(
                        type_=CoreLoginFlowV2,
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
