

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.delete_technical_user200response_dto import DeleteTechnicalUser200ResponseDto
from ..types.error_response_dto import ErrorResponseDto
from ..types.technical_user_credentials_dto import TechnicalUserCredentialsDto
from ..types.technical_user_dto import TechnicalUserDto
from ..types.token_response_dto import TokenResponseDto
from .types.get_technical_user_token_request_grant_type import GetTechnicalUserTokenRequestGrantType
from .types.get_technical_user_token_request_subject_token_type import GetTechnicalUserTokenRequestSubjectTokenType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUserMachineClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_technical_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[TechnicalUserDto]]:
        """
        Retrieves a list of all active machine-to-machine (M2M) clients (OAuth 2.0 clients) to the current legal entity.
        These users authenticate via client credentials and act on behalf of applications, not humans.

        Returns the client IDs of all M2M clients that are currently active
        and available for authentication.

        **Authorization Required:** SUPER_USER role

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[TechnicalUserDto]]
            List of M2M clients returned successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "clients",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TechnicalUserDto],
                    parse_obj_as(
                        type_=typing.List[TechnicalUserDto],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def create_technical_user(
        self, *, with_admin_role: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TechnicalUserCredentialsDto]:
        """
        Creates a new machine-to-machine (M2M) client for API authentication via OAuth 2.0.

        The created user will have M2M role permissions, necessary for getting the bearer token.

        When `withAdminRole` is set to `true`, the M2M client will additionally receive the ADMIN role,
        granting it full access to all ADMIN-level endpoints (e.g., trusted key registration).
        This requires the `cyoda.security.web.jwt.m2m.admin-role-enabled` feature flag to be enabled;
        otherwise, a 401 Unauthorized response is returned.

        **Authorization Required:** SUPER_USER role

        Parameters
        ----------
        with_admin_role : typing.Optional[str]
            When true, the created M2M client will additionally receive the ADMIN role. Requires the M2M admin role feature flag to be enabled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TechnicalUserCredentialsDto]
            M2M client created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "clients",
            method="POST",
            params={
                "withAdminRole": with_admin_role,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TechnicalUserCredentialsDto,
                    parse_obj_as(
                        type_=TechnicalUserCredentialsDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def delete_technical_user(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteTechnicalUser200ResponseDto]:
        """
        Deletes a M2M client and invalidates all associated credentials.

        This operation cannot be undone without a support ticket. Any applications using this client's
        credentials will immediately lose access and must be reconfigured with new credentials.

        **Authorization Required:** SUPER_USER role

        Parameters
        ----------
        client_id : str
            The client ID of the M2M client to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteTechnicalUser200ResponseDto]
            M2M client deleted successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"clients/{encode_path_param(client_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteTechnicalUser200ResponseDto,
                    parse_obj_as(
                        type_=DeleteTechnicalUser200ResponseDto,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def reset_technical_user_secret(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TechnicalUserCredentialsDto]:
        """
        Generates a new client secret for an existing M2M client.

        This operation invalidates the current client secret and generates a new one.
        Any applications using the old secret will need to be updated with the new credentials.

        **Authorization Required:** SUPER_USER role

        Parameters
        ----------
        client_id : str
            The client ID of the M2M client whose secret should be reset

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TechnicalUserCredentialsDto]
            Client secret reset successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"clients/{encode_path_param(client_id)}/secret",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TechnicalUserCredentialsDto,
                    parse_obj_as(
                        type_=TechnicalUserCredentialsDto,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def get_technical_user_token(
        self,
        *,
        grant_type: typing.Optional[GetTechnicalUserTokenRequestGrantType] = OMIT,
        subject_token: typing.Optional[str] = OMIT,
        subject_token_type: typing.Optional[GetTechnicalUserTokenRequestSubjectTokenType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TokenResponseDto]:
        """
        Authenticates a M2M client and returns an access token.

        Supports two grant types:

        1. **client_credentials** — Standard OAuth 2.0 Client Credentials Grant for M2M authentication.
        2. **urn:ietf:params:oauth:grant-type:token-exchange** — RFC 8693 Token Exchange.
           The M2M client acts on behalf of a user by presenting the user's JWT as `subject_token`.

        In both cases the M2M client authenticates via HTTP Basic Authentication
        (client_id and client_secret in the Authorization header).

        **Note:** This endpoint does not require an existing access token, as it serves as the authentication entry point.

        Parameters
        ----------
        grant_type : typing.Optional[GetTechnicalUserTokenRequestGrantType]
            The OAuth 2.0 grant type

        subject_token : typing.Optional[str]
            The subject token to exchange

        subject_token_type : typing.Optional[GetTechnicalUserTokenRequestSubjectTokenType]
            The type of the subject token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TokenResponseDto]
            Access token issued successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth/token",
            method="POST",
            data={
                "grant_type": grant_type,
                "subject_token": subject_token,
                "subject_token_type": subject_token_type,
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
                    TokenResponseDto,
                    parse_obj_as(
                        type_=TokenResponseDto,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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


class AsyncRawUserMachineClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_technical_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[TechnicalUserDto]]:
        """
        Retrieves a list of all active machine-to-machine (M2M) clients (OAuth 2.0 clients) to the current legal entity.
        These users authenticate via client credentials and act on behalf of applications, not humans.

        Returns the client IDs of all M2M clients that are currently active
        and available for authentication.

        **Authorization Required:** SUPER_USER role

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[TechnicalUserDto]]
            List of M2M clients returned successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "clients",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TechnicalUserDto],
                    parse_obj_as(
                        type_=typing.List[TechnicalUserDto],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def create_technical_user(
        self, *, with_admin_role: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TechnicalUserCredentialsDto]:
        """
        Creates a new machine-to-machine (M2M) client for API authentication via OAuth 2.0.

        The created user will have M2M role permissions, necessary for getting the bearer token.

        When `withAdminRole` is set to `true`, the M2M client will additionally receive the ADMIN role,
        granting it full access to all ADMIN-level endpoints (e.g., trusted key registration).
        This requires the `cyoda.security.web.jwt.m2m.admin-role-enabled` feature flag to be enabled;
        otherwise, a 401 Unauthorized response is returned.

        **Authorization Required:** SUPER_USER role

        Parameters
        ----------
        with_admin_role : typing.Optional[str]
            When true, the created M2M client will additionally receive the ADMIN role. Requires the M2M admin role feature flag to be enabled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TechnicalUserCredentialsDto]
            M2M client created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "clients",
            method="POST",
            params={
                "withAdminRole": with_admin_role,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TechnicalUserCredentialsDto,
                    parse_obj_as(
                        type_=TechnicalUserCredentialsDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def delete_technical_user(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteTechnicalUser200ResponseDto]:
        """
        Deletes a M2M client and invalidates all associated credentials.

        This operation cannot be undone without a support ticket. Any applications using this client's
        credentials will immediately lose access and must be reconfigured with new credentials.

        **Authorization Required:** SUPER_USER role

        Parameters
        ----------
        client_id : str
            The client ID of the M2M client to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteTechnicalUser200ResponseDto]
            M2M client deleted successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"clients/{encode_path_param(client_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteTechnicalUser200ResponseDto,
                    parse_obj_as(
                        type_=DeleteTechnicalUser200ResponseDto,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def reset_technical_user_secret(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TechnicalUserCredentialsDto]:
        """
        Generates a new client secret for an existing M2M client.

        This operation invalidates the current client secret and generates a new one.
        Any applications using the old secret will need to be updated with the new credentials.

        **Authorization Required:** SUPER_USER role

        Parameters
        ----------
        client_id : str
            The client ID of the M2M client whose secret should be reset

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TechnicalUserCredentialsDto]
            Client secret reset successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"clients/{encode_path_param(client_id)}/secret",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TechnicalUserCredentialsDto,
                    parse_obj_as(
                        type_=TechnicalUserCredentialsDto,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def get_technical_user_token(
        self,
        *,
        grant_type: typing.Optional[GetTechnicalUserTokenRequestGrantType] = OMIT,
        subject_token: typing.Optional[str] = OMIT,
        subject_token_type: typing.Optional[GetTechnicalUserTokenRequestSubjectTokenType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TokenResponseDto]:
        """
        Authenticates a M2M client and returns an access token.

        Supports two grant types:

        1. **client_credentials** — Standard OAuth 2.0 Client Credentials Grant for M2M authentication.
        2. **urn:ietf:params:oauth:grant-type:token-exchange** — RFC 8693 Token Exchange.
           The M2M client acts on behalf of a user by presenting the user's JWT as `subject_token`.

        In both cases the M2M client authenticates via HTTP Basic Authentication
        (client_id and client_secret in the Authorization header).

        **Note:** This endpoint does not require an existing access token, as it serves as the authentication entry point.

        Parameters
        ----------
        grant_type : typing.Optional[GetTechnicalUserTokenRequestGrantType]
            The OAuth 2.0 grant type

        subject_token : typing.Optional[str]
            The subject token to exchange

        subject_token_type : typing.Optional[GetTechnicalUserTokenRequestSubjectTokenType]
            The type of the subject token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TokenResponseDto]
            Access token issued successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth/token",
            method="POST",
            data={
                "grant_type": grant_type,
                "subject_token": subject_token,
                "subject_token_type": subject_token_type,
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
                    TokenResponseDto,
                    parse_obj_as(
                        type_=TokenResponseDto,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
