

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.credential_requests_peek_response import CredentialRequestsPeekResponse
from .types.credential_requests_submit_response import CredentialRequestsSubmitResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCredentialRequestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def peek(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CredentialRequestsPeekResponse]:
        """
        Returns the service/field/label the link collects. The token travels in the body so it never appears in URLs or access logs.

        Parameters
        ----------
        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CredentialRequestsPeekResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/credential-requests/peek",
            method="POST",
            json={
                "token": token,
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
                    CredentialRequestsPeekResponse,
                    parse_obj_as(
                        type_=CredentialRequestsPeekResponse,
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

    def submit(
        self, *, token: str, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CredentialRequestsSubmitResponse]:
        """
        Single-use: atomically claims the link, forwards the value to the assistant's credential store, and marks the link redeemed.

        Parameters
        ----------
        token : str

        value : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CredentialRequestsSubmitResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/credential-requests/submit",
            method="POST",
            json={
                "token": token,
                "value": value,
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
                    CredentialRequestsSubmitResponse,
                    parse_obj_as(
                        type_=CredentialRequestsSubmitResponse,
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


class AsyncRawCredentialRequestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def peek(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CredentialRequestsPeekResponse]:
        """
        Returns the service/field/label the link collects. The token travels in the body so it never appears in URLs or access logs.

        Parameters
        ----------
        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CredentialRequestsPeekResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/credential-requests/peek",
            method="POST",
            json={
                "token": token,
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
                    CredentialRequestsPeekResponse,
                    parse_obj_as(
                        type_=CredentialRequestsPeekResponse,
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

    async def submit(
        self, *, token: str, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CredentialRequestsSubmitResponse]:
        """
        Single-use: atomically claims the link, forwards the value to the assistant's credential store, and marks the link redeemed.

        Parameters
        ----------
        token : str

        value : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CredentialRequestsSubmitResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/credential-requests/submit",
            method="POST",
            json={
                "token": token,
                "value": value,
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
                    CredentialRequestsSubmitResponse,
                    parse_obj_as(
                        type_=CredentialRequestsSubmitResponse,
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
