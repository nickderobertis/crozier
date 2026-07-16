

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.create_mobile_authorization_code_response import CreateMobileAuthorizationCodeResponse


OMIT = typing.cast(typing.Any, ...)


class RawMobileAuthorizationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_mobile_authorization_code(
        self, *, location_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CreateMobileAuthorizationCodeResponse]:
        """
        Generates code to authorize a mobile application to connect to a Square card reader

        Authorization codes are one-time-use and expire __60 minutes__ after being issued.

        __Important:__ The `Authorization` header you provide to this endpoint must have the following format:

        ```
        Authorization: Bearer ACCESS_TOKEN
        ```

        Replace `ACCESS_TOKEN` with a
        [valid production authorization credential](https://developer.squareup.com/docs/build-basics/access-tokens).

        Parameters
        ----------
        location_id : typing.Optional[str]
            The Square location ID the authorization code should be tied to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateMobileAuthorizationCodeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "mobile/authorization-code",
            method="POST",
            json={
                "location_id": location_id,
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
                    CreateMobileAuthorizationCodeResponse,
                    parse_obj_as(
                        type_=CreateMobileAuthorizationCodeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawMobileAuthorizationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_mobile_authorization_code(
        self, *, location_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CreateMobileAuthorizationCodeResponse]:
        """
        Generates code to authorize a mobile application to connect to a Square card reader

        Authorization codes are one-time-use and expire __60 minutes__ after being issued.

        __Important:__ The `Authorization` header you provide to this endpoint must have the following format:

        ```
        Authorization: Bearer ACCESS_TOKEN
        ```

        Replace `ACCESS_TOKEN` with a
        [valid production authorization credential](https://developer.squareup.com/docs/build-basics/access-tokens).

        Parameters
        ----------
        location_id : typing.Optional[str]
            The Square location ID the authorization code should be tied to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateMobileAuthorizationCodeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mobile/authorization-code",
            method="POST",
            json={
                "location_id": location_id,
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
                    CreateMobileAuthorizationCodeResponse,
                    parse_obj_as(
                        type_=CreateMobileAuthorizationCodeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
