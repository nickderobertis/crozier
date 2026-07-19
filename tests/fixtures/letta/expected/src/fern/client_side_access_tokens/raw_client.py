

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from .types.client_side_access_tokens_create_client_side_access_token_request_policy_item import (
    ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem,
)
from .types.client_side_access_tokens_create_client_side_access_token_response import (
    ClientSideAccessTokensCreateClientSideAccessTokenResponse,
)
from .types.client_side_access_tokens_list_client_side_access_tokens_response import (
    ClientSideAccessTokensListClientSideAccessTokensResponse,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawClientSideAccessTokensClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def client_side_access_tokens_list_client_side_access_tokens(
        self,
        *,
        agent_id: typing.Optional[str] = None,
        offset: typing.Optional[float] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ClientSideAccessTokensListClientSideAccessTokensResponse]:
        """
        List all client side access tokens for the current account. This is only available for cloud users.

        Parameters
        ----------
        agent_id : typing.Optional[str]
            The agent ID to filter tokens by. If provided, only tokens for this agent will be returned.

        offset : typing.Optional[float]
            The offset for pagination. Defaults to 0.

        limit : typing.Optional[float]
            The number of tokens to return per page. Defaults to 10.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ClientSideAccessTokensListClientSideAccessTokensResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/client-side-access-tokens",
            method="GET",
            params={
                "agentId": agent_id,
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClientSideAccessTokensListClientSideAccessTokensResponse,
                    parse_obj_as(
                        type_=ClientSideAccessTokensListClientSideAccessTokensResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def client_side_access_tokens_create_client_side_access_token(
        self,
        *,
        policy: typing.Sequence[ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem],
        hostname: str,
        expires_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ClientSideAccessTokensCreateClientSideAccessTokenResponse]:
        """
        Create a new client side access token with the specified configuration.

        Parameters
        ----------
        policy : typing.Sequence[ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem]

        hostname : str
            The hostname of the client side application. Please specify the full URL including the protocol (http or https).

        expires_at : typing.Optional[str]
            The expiration date of the token. If not provided, the token will expire in 5 minutes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ClientSideAccessTokensCreateClientSideAccessTokenResponse]
            201
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/client-side-access-tokens",
            method="POST",
            json={
                "policy": convert_and_respect_annotation_metadata(
                    object_=policy,
                    annotation=typing.Sequence[ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem],
                    direction="write",
                ),
                "hostname": hostname,
                "expires_at": expires_at,
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
                    ClientSideAccessTokensCreateClientSideAccessTokenResponse,
                    parse_obj_as(
                        type_=ClientSideAccessTokensCreateClientSideAccessTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def client_side_access_tokens_delete_client_side_access_token(
        self, token: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Delete a client side access token.

        Parameters
        ----------
        token : str
            The access token to delete

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            204
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/client-side-access-tokens/{encode_path_param(token)}",
            method="DELETE",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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


class AsyncRawClientSideAccessTokensClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def client_side_access_tokens_list_client_side_access_tokens(
        self,
        *,
        agent_id: typing.Optional[str] = None,
        offset: typing.Optional[float] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ClientSideAccessTokensListClientSideAccessTokensResponse]:
        """
        List all client side access tokens for the current account. This is only available for cloud users.

        Parameters
        ----------
        agent_id : typing.Optional[str]
            The agent ID to filter tokens by. If provided, only tokens for this agent will be returned.

        offset : typing.Optional[float]
            The offset for pagination. Defaults to 0.

        limit : typing.Optional[float]
            The number of tokens to return per page. Defaults to 10.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ClientSideAccessTokensListClientSideAccessTokensResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/client-side-access-tokens",
            method="GET",
            params={
                "agentId": agent_id,
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClientSideAccessTokensListClientSideAccessTokensResponse,
                    parse_obj_as(
                        type_=ClientSideAccessTokensListClientSideAccessTokensResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def client_side_access_tokens_create_client_side_access_token(
        self,
        *,
        policy: typing.Sequence[ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem],
        hostname: str,
        expires_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ClientSideAccessTokensCreateClientSideAccessTokenResponse]:
        """
        Create a new client side access token with the specified configuration.

        Parameters
        ----------
        policy : typing.Sequence[ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem]

        hostname : str
            The hostname of the client side application. Please specify the full URL including the protocol (http or https).

        expires_at : typing.Optional[str]
            The expiration date of the token. If not provided, the token will expire in 5 minutes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ClientSideAccessTokensCreateClientSideAccessTokenResponse]
            201
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/client-side-access-tokens",
            method="POST",
            json={
                "policy": convert_and_respect_annotation_metadata(
                    object_=policy,
                    annotation=typing.Sequence[ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem],
                    direction="write",
                ),
                "hostname": hostname,
                "expires_at": expires_at,
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
                    ClientSideAccessTokensCreateClientSideAccessTokenResponse,
                    parse_obj_as(
                        type_=ClientSideAccessTokensCreateClientSideAccessTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def client_side_access_tokens_delete_client_side_access_token(
        self, token: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Delete a client side access token.

        Parameters
        ----------
        token : str
            The access token to delete

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            204
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/client-side-access-tokens/{encode_path_param(token)}",
            method="DELETE",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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
