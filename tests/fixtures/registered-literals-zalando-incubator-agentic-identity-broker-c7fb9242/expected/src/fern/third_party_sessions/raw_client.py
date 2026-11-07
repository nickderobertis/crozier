

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_gateway_error import BadGatewayError
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error import Error
from .types.get_affected_agents_response import GetAffectedAgentsResponse
from .types.get_session_details_response import GetSessionDetailsResponse
from .types.list_third_party_sessions_response import ListThirdPartySessionsResponse
from .types.refresh_third_party_session_response import RefreshThirdPartySessionResponse
from .types.terminate_session_response import TerminateSessionResponse
from pydantic import ValidationError


class RawThirdPartySessionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_third_party_sessions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListThirdPartySessionsResponse]:
        """
        Returns a list of all configured third-party OAuth2 services along with the current user's session status for each service.

        For services where the user has an active session, includes:

        - Session initiation timestamp
        - Token expiration status
        - Number of agents depending on this session, derived only from grants owned by the authenticated session principal
        - Encryption status indicator

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListThirdPartySessionsResponse]
            List of services with session status
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/third-party/sessions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListThirdPartySessionsResponse,
                    parse_obj_as(
                        type_=ListThirdPartySessionsResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def initiate_o_auth2flow(
        self, service_id: str, *, redirect_uri: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Initiates an OAuth2 authorization code flow with PKCE for the specified third-party service. Redirects the user to the third-party's authorization endpoint.

        PKCE applies to every service; the authorization-code exchange presents a client credential only for confidential services.

        The flow:

        1. Generates PKCE code verifier and challenge
        2. Creates JWE state token containing principal, PKCE verifier, service ID, redirect_uri
        3. Redirects user to third-party authorization endpoint

        The redirect_uri parameter must match the host of the incoming request (same-origin validation).

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        redirect_uri : str
            URI to redirect user after OAuth2 flow completes.
            Must match the host of the incoming request (same-origin validation).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/third-party/{encode_path_param(service_id)}/oauth2/authorize",
            method="GET",
            params={
                "redirect_uri": redirect_uri,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def handle_o_auth2callback(
        self,
        service_id: str,
        *,
        code: str,
        state: str,
        error: typing.Optional[str] = None,
        error_description: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Processes the OAuth2 callback after user authorization at the third-party.

        PKCE applies to every service; the authorization-code exchange presents a client credential only for confidential services.

        Validates:

        - State token decrypts successfully (JWE)
        - State token is not expired
        - Principal in token matches current authenticated principal (CSRF protection)
        - Service ID in token matches path parameter

        On success:

        - Exchanges authorization code for access/refresh tokens (with PKCE)
        - Encrypts tokens using EncryptionPort
        - Stores session in database
        - Redirects user to original redirect_uri with success status

        On error:

        - Redirects user to sessions page with error message

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        code : str
            OAuth2 authorization code from third-party

        state : str
            JWE state token (must match token from authorize request)

        error : typing.Optional[str]
            OAuth2 error code from third-party (if authorization failed)

        error_description : typing.Optional[str]
            OAuth2 error description from third-party

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/third-party/{encode_path_param(service_id)}/oauth2/callback",
            method="GET",
            params={
                "code": code,
                "state": state,
                "error": error,
                "error_description": error_description,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def get_session_details(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetSessionDetailsResponse]:
        """
        Returns detailed information about the user's session with a third-party service, including only agents with grants owned by the authenticated session principal that depend on this session.
        Used to populate the session card and termination warning dialog.

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSessionDetailsResponse]
            Session details retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/third-party/{encode_path_param(service_id)}/session",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSessionDetailsResponse,
                    parse_obj_as(
                        type_=GetSessionDetailsResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def terminate_session(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TerminateSessionResponse]:
        """
        Terminates the user's session with a third-party service by deleting stored tokens.
        Returns information about affected agents for the confirmation dialog shown before this request.

        Note: This does not revoke tokens at the third-party service.

        Agents that were using this session will detect the missing session and request re-authentication.

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TerminateSessionResponse]
            Session terminated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/third-party/{encode_path_param(service_id)}/session",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TerminateSessionResponse,
                    parse_obj_as(
                        type_=TerminateSessionResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def refresh_third_party_session(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RefreshThirdPartySessionResponse]:
        """
        Forces an immediate OAuth2 access-token refresh for the user's session with a
        third-party service, using the stored refresh token via the RFC 6749 refresh_token
        grant. Unlike the transparent refresh performed during token exchange, this refreshes
        even when the current access token has not yet expired. Requires a stored, non-expired
        refresh token.

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RefreshThirdPartySessionResponse]
            Access token refreshed successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/third-party/{encode_path_param(service_id)}/session/refresh",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RefreshThirdPartySessionResponse,
                    parse_obj_as(
                        type_=RefreshThirdPartySessionResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def get_affected_agents(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetAffectedAgentsResponse]:
        """
        Returns a list of agents that would lose access if the user terminates their session with this third-party service.
        Used to populate the termination warning dialog.

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetAffectedAgentsResponse]
            List of affected agents
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/third-party/{encode_path_param(service_id)}/session/affected-agents",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAffectedAgentsResponse,
                    parse_obj_as(
                        type_=GetAffectedAgentsResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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


class AsyncRawThirdPartySessionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_third_party_sessions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListThirdPartySessionsResponse]:
        """
        Returns a list of all configured third-party OAuth2 services along with the current user's session status for each service.

        For services where the user has an active session, includes:

        - Session initiation timestamp
        - Token expiration status
        - Number of agents depending on this session, derived only from grants owned by the authenticated session principal
        - Encryption status indicator

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListThirdPartySessionsResponse]
            List of services with session status
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/third-party/sessions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListThirdPartySessionsResponse,
                    parse_obj_as(
                        type_=ListThirdPartySessionsResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def initiate_o_auth2flow(
        self, service_id: str, *, redirect_uri: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Initiates an OAuth2 authorization code flow with PKCE for the specified third-party service. Redirects the user to the third-party's authorization endpoint.

        PKCE applies to every service; the authorization-code exchange presents a client credential only for confidential services.

        The flow:

        1. Generates PKCE code verifier and challenge
        2. Creates JWE state token containing principal, PKCE verifier, service ID, redirect_uri
        3. Redirects user to third-party authorization endpoint

        The redirect_uri parameter must match the host of the incoming request (same-origin validation).

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        redirect_uri : str
            URI to redirect user after OAuth2 flow completes.
            Must match the host of the incoming request (same-origin validation).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/third-party/{encode_path_param(service_id)}/oauth2/authorize",
            method="GET",
            params={
                "redirect_uri": redirect_uri,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def handle_o_auth2callback(
        self,
        service_id: str,
        *,
        code: str,
        state: str,
        error: typing.Optional[str] = None,
        error_description: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Processes the OAuth2 callback after user authorization at the third-party.

        PKCE applies to every service; the authorization-code exchange presents a client credential only for confidential services.

        Validates:

        - State token decrypts successfully (JWE)
        - State token is not expired
        - Principal in token matches current authenticated principal (CSRF protection)
        - Service ID in token matches path parameter

        On success:

        - Exchanges authorization code for access/refresh tokens (with PKCE)
        - Encrypts tokens using EncryptionPort
        - Stores session in database
        - Redirects user to original redirect_uri with success status

        On error:

        - Redirects user to sessions page with error message

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        code : str
            OAuth2 authorization code from third-party

        state : str
            JWE state token (must match token from authorize request)

        error : typing.Optional[str]
            OAuth2 error code from third-party (if authorization failed)

        error_description : typing.Optional[str]
            OAuth2 error description from third-party

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/third-party/{encode_path_param(service_id)}/oauth2/callback",
            method="GET",
            params={
                "code": code,
                "state": state,
                "error": error,
                "error_description": error_description,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def get_session_details(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetSessionDetailsResponse]:
        """
        Returns detailed information about the user's session with a third-party service, including only agents with grants owned by the authenticated session principal that depend on this session.
        Used to populate the session card and termination warning dialog.

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSessionDetailsResponse]
            Session details retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/third-party/{encode_path_param(service_id)}/session",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSessionDetailsResponse,
                    parse_obj_as(
                        type_=GetSessionDetailsResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def terminate_session(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TerminateSessionResponse]:
        """
        Terminates the user's session with a third-party service by deleting stored tokens.
        Returns information about affected agents for the confirmation dialog shown before this request.

        Note: This does not revoke tokens at the third-party service.

        Agents that were using this session will detect the missing session and request re-authentication.

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TerminateSessionResponse]
            Session terminated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/third-party/{encode_path_param(service_id)}/session",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TerminateSessionResponse,
                    parse_obj_as(
                        type_=TerminateSessionResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def refresh_third_party_session(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RefreshThirdPartySessionResponse]:
        """
        Forces an immediate OAuth2 access-token refresh for the user's session with a
        third-party service, using the stored refresh token via the RFC 6749 refresh_token
        grant. Unlike the transparent refresh performed during token exchange, this refreshes
        even when the current access token has not yet expired. Requires a stored, non-expired
        refresh token.

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RefreshThirdPartySessionResponse]
            Access token refreshed successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/third-party/{encode_path_param(service_id)}/session/refresh",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RefreshThirdPartySessionResponse,
                    parse_obj_as(
                        type_=RefreshThirdPartySessionResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def get_affected_agents(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetAffectedAgentsResponse]:
        """
        Returns a list of agents that would lose access if the user terminates their session with this third-party service.
        Used to populate the termination warning dialog.

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetAffectedAgentsResponse]
            List of affected agents
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/third-party/{encode_path_param(service_id)}/session/affected-agents",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAffectedAgentsResponse,
                    parse_obj_as(
                        type_=GetAffectedAgentsResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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
