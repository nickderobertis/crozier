

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.create_bridge_token_endpoint_output import CreateBridgeTokenEndpointOutput
from ..types.google_one_tap_login_endpoint_output import GoogleOneTapLoginEndpointOutput
from ..types.read_bridge_token_endpoint_keys_output import ReadBridgeTokenEndpointKeysOutput
from ..types.validation_problem_details import ValidationProblemDetails
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIdentityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def reads_the_bridge_token_keys_for_a_given_read_key(
        self, *, read_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ReadBridgeTokenEndpointKeysOutput]:
        """
        Returns 200 with the keys when available, 202 when they are not yet available, or 404 when not found.

        Parameters
        ----------
        read_key : str
            The read key to read the bridge token keys for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ReadBridgeTokenEndpointKeysOutput]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "identity/bridge-token",
            method="GET",
            params={
                "readKey": read_key,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReadBridgeTokenEndpointKeysOutput,
                    parse_obj_as(
                        type_=ReadBridgeTokenEndpointKeysOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def creates_a_pair_of_read_and_write_bridge_token_keys_for_a_client(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CreateBridgeTokenEndpointOutput]:
        """
        The write key stores the authentication result and the read key retrieves it.

        Parameters
        ----------
        client_id : str
            The client ID to create the keys for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateBridgeTokenEndpointOutput]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "identity/bridge-token",
            method="POST",
            params={
                "clientId": client_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateBridgeTokenEndpointOutput,
                    parse_obj_as(
                        type_=CreateBridgeTokenEndpointOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationProblemDetails,
                        parse_obj_as(
                            type_=ValidationProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def signs_in_a_user_using_a_token_received_from_google_one_tap(
        self, *, id_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GoogleOneTapLoginEndpointOutput]:
        """
        Redirects to the register confirmation page when the account requires email confirmation.

        Parameters
        ----------
        id_token : str
            The id token received from the Google One Tap login.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GoogleOneTapLoginEndpointOutput]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "identity/google-one-tap",
            method="POST",
            json={
                "idToken": id_token,
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
                    GoogleOneTapLoginEndpointOutput,
                    parse_obj_as(
                        type_=GoogleOneTapLoginEndpointOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationProblemDetails,
                        parse_obj_as(
                            type_=ValidationProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def stores_the_referrer_in_a_cookie_for_later_use_during_sign_up(
        self, *, referrer: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        referrer : str
            The referrer value to store.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "identity/referrer",
            method="POST",
            params={
                "referrer": referrer,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawIdentityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def reads_the_bridge_token_keys_for_a_given_read_key(
        self, *, read_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ReadBridgeTokenEndpointKeysOutput]:
        """
        Returns 200 with the keys when available, 202 when they are not yet available, or 404 when not found.

        Parameters
        ----------
        read_key : str
            The read key to read the bridge token keys for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ReadBridgeTokenEndpointKeysOutput]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "identity/bridge-token",
            method="GET",
            params={
                "readKey": read_key,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReadBridgeTokenEndpointKeysOutput,
                    parse_obj_as(
                        type_=ReadBridgeTokenEndpointKeysOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def creates_a_pair_of_read_and_write_bridge_token_keys_for_a_client(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CreateBridgeTokenEndpointOutput]:
        """
        The write key stores the authentication result and the read key retrieves it.

        Parameters
        ----------
        client_id : str
            The client ID to create the keys for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateBridgeTokenEndpointOutput]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "identity/bridge-token",
            method="POST",
            params={
                "clientId": client_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateBridgeTokenEndpointOutput,
                    parse_obj_as(
                        type_=CreateBridgeTokenEndpointOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationProblemDetails,
                        parse_obj_as(
                            type_=ValidationProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def signs_in_a_user_using_a_token_received_from_google_one_tap(
        self, *, id_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GoogleOneTapLoginEndpointOutput]:
        """
        Redirects to the register confirmation page when the account requires email confirmation.

        Parameters
        ----------
        id_token : str
            The id token received from the Google One Tap login.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GoogleOneTapLoginEndpointOutput]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "identity/google-one-tap",
            method="POST",
            json={
                "idToken": id_token,
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
                    GoogleOneTapLoginEndpointOutput,
                    parse_obj_as(
                        type_=GoogleOneTapLoginEndpointOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationProblemDetails,
                        parse_obj_as(
                            type_=ValidationProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def stores_the_referrer_in_a_cookie_for_later_use_during_sign_up(
        self, *, referrer: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        referrer : str
            The referrer value to store.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "identity/referrer",
            method="POST",
            params={
                "referrer": referrer,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
