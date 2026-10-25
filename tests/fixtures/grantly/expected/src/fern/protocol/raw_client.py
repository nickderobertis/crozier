

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
from ..errors.unauthorized_error import UnauthorizedError
from ..types.registered_client import RegisteredClient
from .types.get_auth_request_code_challenge_method import GetAuthRequestCodeChallengeMethod
from .types.get_auth_request_prompt import GetAuthRequestPrompt
from .types.get_jwks_response import GetJwksResponse
from .types.get_me_response import GetMeResponse
from .types.post_introspect_request_token_type_hint import PostIntrospectRequestTokenTypeHint
from .types.post_introspect_response import PostIntrospectResponse
from .types.post_revoke_request_token_type_hint import PostRevokeRequestTokenTypeHint
from .types.post_token_request import PostTokenRequest
from .types.post_token_response import PostTokenResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawProtocolClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def discovery_document(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Returns issuer metadata - endpoint URLs, supported scopes, grant types, signing algorithms.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Discovery document
        """
        _response = self._client_wrapper.httpx_client.request(
            ".well-known/openid-configuration",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    def public_signing_keys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetJwksResponse]:
        """
        JSON Web Key Set used to verify id_tokens issued by this server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetJwksResponse]
            JWKS document
        """
        _response = self._client_wrapper.httpx_client.request(
            "jwks",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetJwksResponse,
                    parse_obj_as(
                        type_=GetJwksResponse,
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

    def authorization_endpoint(
        self,
        *,
        client_id: str,
        response_type: str,
        redirect_uri: str,
        scope: str,
        state: str,
        code_challenge: str,
        code_challenge_method: GetAuthRequestCodeChallengeMethod,
        prompt: typing.Optional[GetAuthRequestPrompt] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Starts an OAuth/OIDC authorization flow. Must be opened as a real browser navigation, not called via fetch/XHR - it involves interactive login and redirects.

        Parameters
        ----------
        client_id : str

        response_type : str

        redirect_uri : str

        scope : str

        state : str

        code_challenge : str
            PKCE code challenge (S256), required for all clients

        code_challenge_method : GetAuthRequestCodeChallengeMethod

        prompt : typing.Optional[GetAuthRequestPrompt]
            Set to "consent" to request a refresh token alongside offline_access scope

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "auth",
            method="GET",
            params={
                "client_id": client_id,
                "response_type": response_type,
                "redirect_uri": redirect_uri,
                "scope": scope,
                "state": state,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
                "prompt": prompt,
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

    def token_exchange(
        self, *, request: PostTokenRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostTokenResponse]:
        """
        Exchanges an authorization code or refresh token for tokens. Rate-limited to 20 requests/60s per IP. CORS-scoped to FRONTEND_URL.

        Parameters
        ----------
        request : PostTokenRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostTokenResponse]
            Token response
        """
        _response = self._client_wrapper.httpx_client.request(
            "token",
            method="POST",
            data=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostTokenRequest, direction="write"
            ),
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostTokenResponse,
                    parse_obj_as(
                        type_=PostTokenResponse,
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

    def userinfo(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[GetMeResponse]:
        """
        Returns claims for the access token's subject, scoped by the token's granted scopes. CORS-scoped to FRONTEND_URL.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMeResponse]
            Claims
        """
        _response = self._client_wrapper.httpx_client.request(
            "me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMeResponse,
                    parse_obj_as(
                        type_=GetMeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def dynamic_client_registration_rfc7591(
        self,
        *,
        redirect_uris: typing.Sequence[str],
        grant_types: typing.Optional[typing.Sequence[str]] = OMIT,
        response_types: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RegisteredClient]:
        """
        Anonymous client registration, gated by an Initial Access Token (minted via `npm run mint-token`).

        Parameters
        ----------
        redirect_uris : typing.Sequence[str]

        grant_types : typing.Optional[typing.Sequence[str]]

        response_types : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RegisteredClient]
            Client registered
        """
        _response = self._client_wrapper.httpx_client.request(
            "reg",
            method="POST",
            json={
                "redirect_uris": redirect_uris,
                "grant_types": grant_types,
                "response_types": response_types,
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
                    RegisteredClient,
                    parse_obj_as(
                        type_=RegisteredClient,
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

    def read_own_registration(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RegisteredClient]:
        """
        Parameters
        ----------
        client_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RegisteredClient]
            Current client configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            f"reg/{encode_path_param(client_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegisteredClient,
                    parse_obj_as(
                        type_=RegisteredClient,
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

    def update_own_registration(
        self,
        client_id_: str,
        *,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        redirect_uris: typing.Optional[typing.Sequence[str]] = OMIT,
        grant_types: typing.Optional[typing.Sequence[str]] = OMIT,
        response_types: typing.Optional[typing.Sequence[str]] = OMIT,
        registration_access_token: typing.Optional[str] = OMIT,
        registration_client_uri: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Replaces the full client metadata - not a partial patch.

        Parameters
        ----------
        client_id_ : str

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        redirect_uris : typing.Optional[typing.Sequence[str]]

        grant_types : typing.Optional[typing.Sequence[str]]

        response_types : typing.Optional[typing.Sequence[str]]

        registration_access_token : typing.Optional[str]

        registration_client_uri : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"reg/{encode_path_param(client_id_)}",
            method="PUT",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "redirect_uris": redirect_uris,
                "grant_types": grant_types,
                "response_types": response_types,
                "registration_access_token": registration_access_token,
                "registration_client_uri": registration_client_uri,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    def deregister(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        client_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"reg/{encode_path_param(client_id)}",
            method="DELETE",
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

    def token_revocation(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[PostRevokeRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[PostRevokeRequestTokenTypeHint]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "revoke",
            method="POST",
            data={
                "token": token,
                "token_type_hint": token_type_hint,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
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

    def token_introspection(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[PostIntrospectRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostIntrospectResponse]:
        """
        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[PostIntrospectRequestTokenTypeHint]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostIntrospectResponse]
            Token metadata
        """
        _response = self._client_wrapper.httpx_client.request(
            "introspect",
            method="POST",
            data={
                "token": token,
                "token_type_hint": token_type_hint,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostIntrospectResponse,
                    parse_obj_as(
                        type_=PostIntrospectResponse,
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

    def rp_initiated_logout(
        self,
        *,
        id_token_hint: typing.Optional[str] = None,
        post_logout_redirect_uri: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Must be opened as a browser navigation.

        Parameters
        ----------
        id_token_hint : typing.Optional[str]

        post_logout_redirect_uri : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "session/end",
            method="GET",
            params={
                "id_token_hint": id_token_hint,
                "post_logout_redirect_uri": post_logout_redirect_uri,
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


class AsyncRawProtocolClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def discovery_document(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Returns issuer metadata - endpoint URLs, supported scopes, grant types, signing algorithms.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Discovery document
        """
        _response = await self._client_wrapper.httpx_client.request(
            ".well-known/openid-configuration",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    async def public_signing_keys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetJwksResponse]:
        """
        JSON Web Key Set used to verify id_tokens issued by this server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetJwksResponse]
            JWKS document
        """
        _response = await self._client_wrapper.httpx_client.request(
            "jwks",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetJwksResponse,
                    parse_obj_as(
                        type_=GetJwksResponse,
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

    async def authorization_endpoint(
        self,
        *,
        client_id: str,
        response_type: str,
        redirect_uri: str,
        scope: str,
        state: str,
        code_challenge: str,
        code_challenge_method: GetAuthRequestCodeChallengeMethod,
        prompt: typing.Optional[GetAuthRequestPrompt] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Starts an OAuth/OIDC authorization flow. Must be opened as a real browser navigation, not called via fetch/XHR - it involves interactive login and redirects.

        Parameters
        ----------
        client_id : str

        response_type : str

        redirect_uri : str

        scope : str

        state : str

        code_challenge : str
            PKCE code challenge (S256), required for all clients

        code_challenge_method : GetAuthRequestCodeChallengeMethod

        prompt : typing.Optional[GetAuthRequestPrompt]
            Set to "consent" to request a refresh token alongside offline_access scope

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "auth",
            method="GET",
            params={
                "client_id": client_id,
                "response_type": response_type,
                "redirect_uri": redirect_uri,
                "scope": scope,
                "state": state,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
                "prompt": prompt,
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

    async def token_exchange(
        self, *, request: PostTokenRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostTokenResponse]:
        """
        Exchanges an authorization code or refresh token for tokens. Rate-limited to 20 requests/60s per IP. CORS-scoped to FRONTEND_URL.

        Parameters
        ----------
        request : PostTokenRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostTokenResponse]
            Token response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "token",
            method="POST",
            data=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostTokenRequest, direction="write"
            ),
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostTokenResponse,
                    parse_obj_as(
                        type_=PostTokenResponse,
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

    async def userinfo(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMeResponse]:
        """
        Returns claims for the access token's subject, scoped by the token's granted scopes. CORS-scoped to FRONTEND_URL.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMeResponse]
            Claims
        """
        _response = await self._client_wrapper.httpx_client.request(
            "me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMeResponse,
                    parse_obj_as(
                        type_=GetMeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def dynamic_client_registration_rfc7591(
        self,
        *,
        redirect_uris: typing.Sequence[str],
        grant_types: typing.Optional[typing.Sequence[str]] = OMIT,
        response_types: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RegisteredClient]:
        """
        Anonymous client registration, gated by an Initial Access Token (minted via `npm run mint-token`).

        Parameters
        ----------
        redirect_uris : typing.Sequence[str]

        grant_types : typing.Optional[typing.Sequence[str]]

        response_types : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RegisteredClient]
            Client registered
        """
        _response = await self._client_wrapper.httpx_client.request(
            "reg",
            method="POST",
            json={
                "redirect_uris": redirect_uris,
                "grant_types": grant_types,
                "response_types": response_types,
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
                    RegisteredClient,
                    parse_obj_as(
                        type_=RegisteredClient,
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

    async def read_own_registration(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RegisteredClient]:
        """
        Parameters
        ----------
        client_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RegisteredClient]
            Current client configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"reg/{encode_path_param(client_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RegisteredClient,
                    parse_obj_as(
                        type_=RegisteredClient,
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

    async def update_own_registration(
        self,
        client_id_: str,
        *,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        redirect_uris: typing.Optional[typing.Sequence[str]] = OMIT,
        grant_types: typing.Optional[typing.Sequence[str]] = OMIT,
        response_types: typing.Optional[typing.Sequence[str]] = OMIT,
        registration_access_token: typing.Optional[str] = OMIT,
        registration_client_uri: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Replaces the full client metadata - not a partial patch.

        Parameters
        ----------
        client_id_ : str

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        redirect_uris : typing.Optional[typing.Sequence[str]]

        grant_types : typing.Optional[typing.Sequence[str]]

        response_types : typing.Optional[typing.Sequence[str]]

        registration_access_token : typing.Optional[str]

        registration_client_uri : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"reg/{encode_path_param(client_id_)}",
            method="PUT",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "redirect_uris": redirect_uris,
                "grant_types": grant_types,
                "response_types": response_types,
                "registration_access_token": registration_access_token,
                "registration_client_uri": registration_client_uri,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    async def deregister(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        client_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"reg/{encode_path_param(client_id)}",
            method="DELETE",
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

    async def token_revocation(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[PostRevokeRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[PostRevokeRequestTokenTypeHint]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "revoke",
            method="POST",
            data={
                "token": token,
                "token_type_hint": token_type_hint,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
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

    async def token_introspection(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[PostIntrospectRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostIntrospectResponse]:
        """
        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[PostIntrospectRequestTokenTypeHint]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostIntrospectResponse]
            Token metadata
        """
        _response = await self._client_wrapper.httpx_client.request(
            "introspect",
            method="POST",
            data={
                "token": token,
                "token_type_hint": token_type_hint,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostIntrospectResponse,
                    parse_obj_as(
                        type_=PostIntrospectResponse,
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

    async def rp_initiated_logout(
        self,
        *,
        id_token_hint: typing.Optional[str] = None,
        post_logout_redirect_uri: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Must be opened as a browser navigation.

        Parameters
        ----------
        id_token_hint : typing.Optional[str]

        post_logout_redirect_uri : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "session/end",
            method="GET",
            params={
                "id_token_hint": id_token_hint,
                "post_logout_redirect_uri": post_logout_redirect_uri,
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
