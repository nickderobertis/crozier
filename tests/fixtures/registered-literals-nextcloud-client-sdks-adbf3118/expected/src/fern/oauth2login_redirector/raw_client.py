

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.request_options import RequestOptions
from pydantic import ValidationError


class RawOauth2LoginRedirectorClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def authorize(
        self, *, client_id: str, state: str, response_type: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        client_id : str
            Client ID

        state : str
            State of the flow

        response_type : str
            Response type for the flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Client not found
        """
        _response = self._client_wrapper.httpx_client.request(
            "index.php/apps/oauth2/authorize",
            method="GET",
            params={
                "client_id": client_id,
                "state": state,
                "response_type": response_type,
            },
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


class AsyncRawOauth2LoginRedirectorClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def authorize(
        self, *, client_id: str, state: str, response_type: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        client_id : str
            Client ID

        state : str
            State of the flow

        response_type : str
            Response type for the flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Client not found
        """
        _response = await self._client_wrapper.httpx_client.request(
            "index.php/apps/oauth2/authorize",
            method="GET",
            params={
                "client_id": client_id,
                "state": state,
                "response_type": response_type,
            },
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
