

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
from ..errors.internal_server_error import InternalServerError
from ..types.access_token_id_list_response import AccessTokenIdListResponse
from ..types.access_token_response import AccessTokenResponse
from ..types.exception import Exception
from ..types.success import Success
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAuthenticationApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def generate_new_token(
        self, *, client_id: str, client_secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AccessTokenResponse]:
        """
        This endpoint allows you to generate a new access token, which is a required field for all UniCourt API endpoints except for the Authentication API. To generate a new token, you must provide your Client ID and Client Secret ID which you can find by logging into your UniCourt account. At any time, you can have a maximum of 10 active access tokens. The tokens never expire and, if you make a request which would otherwise lead to you having more than 10 active tokens, you will receive an error message.

        Parameters
        ----------
        client_id : str
            Your Client ID obtainable by logging into your UniCourt account.

        client_secret : str
            Your Client Secret ID obtainable by logging into your UniCourt account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AccessTokenResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "generateNewToken",
            method="POST",
            json={
                "clientId": client_id,
                "clientSecret": client_secret,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AccessTokenResponse,
                    parse_obj_as(
                        type_=AccessTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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

    def invalidate_all_tokens(
        self, *, client_id: str, client_secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Success]:
        """
        An endpoint which allows you to invalidate all existing access tokens associated with your UniCourt account.

        Parameters
        ----------
        client_id : str
            Your Client ID obtainable by logging into your UniCourt account.

        client_secret : str
            Your Client Secret ID obtainable by logging into your UniCourt account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Success]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "invalidateAllTokens",
            method="PUT",
            json={
                "clientId": client_id,
                "clientSecret": client_secret,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Success,
                    parse_obj_as(
                        type_=Success,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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

    def invalidate_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        token_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Success]:
        """
        An endpoint which allows you to invalidate a given access token.

        Parameters
        ----------
        client_id : str
            Your Client ID obtainable by logging into your UniCourt account.

        client_secret : str
            Your Client Secret ID obtainable by logging into your UniCourt account.

        token_id : str
            The Token ID of token being invalidated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Success]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "invalidateToken",
            method="PUT",
            json={
                "clientId": client_id,
                "clientSecret": client_secret,
                "tokenId": token_id,
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
                    Success,
                    parse_obj_as(
                        type_=Success,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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

    def list_all_token_ids(
        self, *, client_id: str, client_secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AccessTokenIdListResponse]:
        """
        An endpoint which allows you to view all active access tokens associated with your Client ID and Client Secret ID.

        Parameters
        ----------
        client_id : str
            Your Client ID obtainable by logging into your UniCourt account.

        client_secret : str
            Your Client Secret ID obtainable by logging into your UniCourt account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AccessTokenIdListResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "listAllTokenIds",
            method="PUT",
            json={
                "clientId": client_id,
                "clientSecret": client_secret,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AccessTokenIdListResponse,
                    parse_obj_as(
                        type_=AccessTokenIdListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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


class AsyncRawAuthenticationApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def generate_new_token(
        self, *, client_id: str, client_secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AccessTokenResponse]:
        """
        This endpoint allows you to generate a new access token, which is a required field for all UniCourt API endpoints except for the Authentication API. To generate a new token, you must provide your Client ID and Client Secret ID which you can find by logging into your UniCourt account. At any time, you can have a maximum of 10 active access tokens. The tokens never expire and, if you make a request which would otherwise lead to you having more than 10 active tokens, you will receive an error message.

        Parameters
        ----------
        client_id : str
            Your Client ID obtainable by logging into your UniCourt account.

        client_secret : str
            Your Client Secret ID obtainable by logging into your UniCourt account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AccessTokenResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "generateNewToken",
            method="POST",
            json={
                "clientId": client_id,
                "clientSecret": client_secret,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AccessTokenResponse,
                    parse_obj_as(
                        type_=AccessTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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

    async def invalidate_all_tokens(
        self, *, client_id: str, client_secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Success]:
        """
        An endpoint which allows you to invalidate all existing access tokens associated with your UniCourt account.

        Parameters
        ----------
        client_id : str
            Your Client ID obtainable by logging into your UniCourt account.

        client_secret : str
            Your Client Secret ID obtainable by logging into your UniCourt account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Success]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "invalidateAllTokens",
            method="PUT",
            json={
                "clientId": client_id,
                "clientSecret": client_secret,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Success,
                    parse_obj_as(
                        type_=Success,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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

    async def invalidate_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        token_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Success]:
        """
        An endpoint which allows you to invalidate a given access token.

        Parameters
        ----------
        client_id : str
            Your Client ID obtainable by logging into your UniCourt account.

        client_secret : str
            Your Client Secret ID obtainable by logging into your UniCourt account.

        token_id : str
            The Token ID of token being invalidated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Success]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "invalidateToken",
            method="PUT",
            json={
                "clientId": client_id,
                "clientSecret": client_secret,
                "tokenId": token_id,
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
                    Success,
                    parse_obj_as(
                        type_=Success,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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

    async def list_all_token_ids(
        self, *, client_id: str, client_secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AccessTokenIdListResponse]:
        """
        An endpoint which allows you to view all active access tokens associated with your Client ID and Client Secret ID.

        Parameters
        ----------
        client_id : str
            Your Client ID obtainable by logging into your UniCourt account.

        client_secret : str
            Your Client Secret ID obtainable by logging into your UniCourt account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AccessTokenIdListResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "listAllTokenIds",
            method="PUT",
            json={
                "clientId": client_id,
                "clientSecret": client_secret,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AccessTokenIdListResponse,
                    parse_obj_as(
                        type_=AccessTokenIdListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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
