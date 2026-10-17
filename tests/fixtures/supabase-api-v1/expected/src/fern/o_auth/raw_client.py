

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.forbidden_error import ForbiddenError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.o_auth_token_body_grant_type import OAuthTokenBodyGrantType
from ..types.o_auth_token_response_output import OAuthTokenResponseOutput
from .types.v1authorize_user_request_code_challenge_method import V1AuthorizeUserRequestCodeChallengeMethod
from .types.v1authorize_user_request_response_type import V1AuthorizeUserRequestResponseType
from .types.v1oauth_authorize_project_claim_request_code_challenge_method import (
    V1OauthAuthorizeProjectClaimRequestCodeChallengeMethod,
)
from .types.v1oauth_authorize_project_claim_request_response_type import V1OauthAuthorizeProjectClaimRequestResponseType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOAuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def v1authorize_user(
        self,
        *,
        client_id: str,
        response_type: V1AuthorizeUserRequestResponseType,
        redirect_uri: str,
        scope: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        response_mode: typing.Optional[str] = None,
        code_challenge: typing.Optional[str] = None,
        code_challenge_method: typing.Optional[V1AuthorizeUserRequestCodeChallengeMethod] = None,
        organization_slug: typing.Optional[str] = None,
        target_flow: typing.Optional[str] = None,
        resource: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        client_id : str

        response_type : V1AuthorizeUserRequestResponseType

        redirect_uri : str

        scope : typing.Optional[str]

        state : typing.Optional[str]

        response_mode : typing.Optional[str]

        code_challenge : typing.Optional[str]

        code_challenge_method : typing.Optional[V1AuthorizeUserRequestCodeChallengeMethod]

        organization_slug : typing.Optional[str]
            Organization slug

        target_flow : typing.Optional[str]

        resource : typing.Optional[str]
            Resource indicator for MCP (Model Context Protocol) clients

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/oauth/authorize",
            method="GET",
            params={
                "client_id": client_id,
                "response_type": response_type,
                "redirect_uri": redirect_uri,
                "scope": scope,
                "state": state,
                "response_mode": response_mode,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
                "organization_slug": organization_slug,
                "target_flow": target_flow,
                "resource": resource,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def v1exchange_oauth_token(
        self,
        *,
        grant_type: typing.Optional[OAuthTokenBodyGrantType] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        assertion: typing.Optional[str] = OMIT,
        resource: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OAuthTokenResponseOutput]:
        """
        Supports `authorization_code`, `refresh_token`, and `urn:ietf:params:oauth:grant-type:jwt-bearer` grant types. The `jwt-bearer` grant type (IDJAG — identity-directed JWT assertion) is in beta and available on Team and Enterprise plans only.

        Parameters
        ----------
        grant_type : typing.Optional[OAuthTokenBodyGrantType]

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        code : typing.Optional[str]

        code_verifier : typing.Optional[str]

        redirect_uri : typing.Optional[str]

        refresh_token : typing.Optional[str]

        assertion : typing.Optional[str]
            IDJAG assertion JWT for grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer. Beta - available on Team and Enterprise plans only.

        resource : typing.Optional[str]
            Resource indicator for MCP (Model Context Protocol) clients

        scope : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OAuthTokenResponseOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/oauth/token",
            method="POST",
            data={
                "grant_type": grant_type,
                "client_id": client_id,
                "client_secret": client_secret,
                "code": code,
                "code_verifier": code_verifier,
                "redirect_uri": redirect_uri,
                "refresh_token": refresh_token,
                "assertion": assertion,
                "resource": resource,
                "scope": scope,
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
                    OAuthTokenResponseOutput,
                    parse_obj_as(
                        type_=OAuthTokenResponseOutput,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def v1revoke_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        refresh_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        client_id : str

        client_secret : str

        refresh_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/oauth/revoke",
            method="POST",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "refresh_token": refresh_token,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def v1oauth_authorize_project_claim(
        self,
        *,
        project_ref: str,
        client_id: str,
        response_type: V1OauthAuthorizeProjectClaimRequestResponseType,
        redirect_uri: str,
        state: typing.Optional[str] = None,
        response_mode: typing.Optional[str] = None,
        code_challenge: typing.Optional[str] = None,
        code_challenge_method: typing.Optional[V1OauthAuthorizeProjectClaimRequestCodeChallengeMethod] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Initiates the OAuth authorization flow for the specified provider. After successful authentication, the user can claim ownership of the specified project.

        Parameters
        ----------
        project_ref : str
            Project ref

        client_id : str

        response_type : V1OauthAuthorizeProjectClaimRequestResponseType

        redirect_uri : str

        state : typing.Optional[str]

        response_mode : typing.Optional[str]

        code_challenge : typing.Optional[str]

        code_challenge_method : typing.Optional[V1OauthAuthorizeProjectClaimRequestCodeChallengeMethod]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/oauth/authorize/project-claim",
            method="GET",
            params={
                "project_ref": project_ref,
                "client_id": client_id,
                "response_type": response_type,
                "redirect_uri": redirect_uri,
                "state": state,
                "response_mode": response_mode,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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


class AsyncRawOAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def v1authorize_user(
        self,
        *,
        client_id: str,
        response_type: V1AuthorizeUserRequestResponseType,
        redirect_uri: str,
        scope: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        response_mode: typing.Optional[str] = None,
        code_challenge: typing.Optional[str] = None,
        code_challenge_method: typing.Optional[V1AuthorizeUserRequestCodeChallengeMethod] = None,
        organization_slug: typing.Optional[str] = None,
        target_flow: typing.Optional[str] = None,
        resource: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        client_id : str

        response_type : V1AuthorizeUserRequestResponseType

        redirect_uri : str

        scope : typing.Optional[str]

        state : typing.Optional[str]

        response_mode : typing.Optional[str]

        code_challenge : typing.Optional[str]

        code_challenge_method : typing.Optional[V1AuthorizeUserRequestCodeChallengeMethod]

        organization_slug : typing.Optional[str]
            Organization slug

        target_flow : typing.Optional[str]

        resource : typing.Optional[str]
            Resource indicator for MCP (Model Context Protocol) clients

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/oauth/authorize",
            method="GET",
            params={
                "client_id": client_id,
                "response_type": response_type,
                "redirect_uri": redirect_uri,
                "scope": scope,
                "state": state,
                "response_mode": response_mode,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
                "organization_slug": organization_slug,
                "target_flow": target_flow,
                "resource": resource,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def v1exchange_oauth_token(
        self,
        *,
        grant_type: typing.Optional[OAuthTokenBodyGrantType] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        assertion: typing.Optional[str] = OMIT,
        resource: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OAuthTokenResponseOutput]:
        """
        Supports `authorization_code`, `refresh_token`, and `urn:ietf:params:oauth:grant-type:jwt-bearer` grant types. The `jwt-bearer` grant type (IDJAG — identity-directed JWT assertion) is in beta and available on Team and Enterprise plans only.

        Parameters
        ----------
        grant_type : typing.Optional[OAuthTokenBodyGrantType]

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        code : typing.Optional[str]

        code_verifier : typing.Optional[str]

        redirect_uri : typing.Optional[str]

        refresh_token : typing.Optional[str]

        assertion : typing.Optional[str]
            IDJAG assertion JWT for grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer. Beta - available on Team and Enterprise plans only.

        resource : typing.Optional[str]
            Resource indicator for MCP (Model Context Protocol) clients

        scope : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OAuthTokenResponseOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/oauth/token",
            method="POST",
            data={
                "grant_type": grant_type,
                "client_id": client_id,
                "client_secret": client_secret,
                "code": code,
                "code_verifier": code_verifier,
                "redirect_uri": redirect_uri,
                "refresh_token": refresh_token,
                "assertion": assertion,
                "resource": resource,
                "scope": scope,
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
                    OAuthTokenResponseOutput,
                    parse_obj_as(
                        type_=OAuthTokenResponseOutput,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def v1revoke_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        refresh_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        client_id : str

        client_secret : str

        refresh_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/oauth/revoke",
            method="POST",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "refresh_token": refresh_token,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def v1oauth_authorize_project_claim(
        self,
        *,
        project_ref: str,
        client_id: str,
        response_type: V1OauthAuthorizeProjectClaimRequestResponseType,
        redirect_uri: str,
        state: typing.Optional[str] = None,
        response_mode: typing.Optional[str] = None,
        code_challenge: typing.Optional[str] = None,
        code_challenge_method: typing.Optional[V1OauthAuthorizeProjectClaimRequestCodeChallengeMethod] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Initiates the OAuth authorization flow for the specified provider. After successful authentication, the user can claim ownership of the specified project.

        Parameters
        ----------
        project_ref : str
            Project ref

        client_id : str

        response_type : V1OauthAuthorizeProjectClaimRequestResponseType

        redirect_uri : str

        state : typing.Optional[str]

        response_mode : typing.Optional[str]

        code_challenge : typing.Optional[str]

        code_challenge_method : typing.Optional[V1OauthAuthorizeProjectClaimRequestCodeChallengeMethod]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/oauth/authorize/project-claim",
            method="GET",
            params={
                "project_ref": project_ref,
                "client_id": client_id,
                "response_type": response_type,
                "redirect_uri": redirect_uri,
                "state": state,
                "response_mode": response_mode,
                "code_challenge": code_challenge,
                "code_challenge_method": code_challenge_method,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
