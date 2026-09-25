

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_key_response import ApiKeyResponse
from .types.dev_list_users_response import DevListUsersResponse
from .types.jwt_fetch_api_key_response import JwtFetchApiKeyResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAuthenticationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def fetch_api_key(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ApiKeyResponse]:
        """
        This API endpoint is used by clients such as the Zulip mobile and
        terminal apps to implement password-based authentication. Given the
        user's Zulip login credentials, it returns a Zulip API key that the client
        can use to make requests as the user.

        This endpoint is only useful for Zulip servers/organizations with
        EmailAuthBackend or LDAPAuthBackend enabled.

        The Zulip mobile apps also support SSO/social authentication (GitHub
        auth, Google auth, SAML, etc.) that does not use this endpoint. Instead,
        the mobile apps reuse the web login flow passing the `mobile_flow_otp` in
        a webview, and the credentials are returned to the app (encrypted) via a redirect
        to a `zulip://` URL.

        !!! warn ""

            **Note:** If you signed up using passwordless authentication and
            never had a password, you can [reset your password](/help/change-your-password).

        See the [API keys](/api/api-keys) documentation for more details
        on how to download an API key manually.

        In a [Zulip development environment](https://zulip.readthedocs.io/en/latest/development/overview.html),
        see also [the unauthenticated variant](/api/dev-fetch-api-key).

        Parameters
        ----------
        username : str
            The username to be used for authentication (typically, the email
            address, but depending on configuration, it could be an LDAP username).

            See the `require_email_format_usernames` parameter documented in
            [GET /server_settings](/api/get-server-settings) for details.

        password : str
            The user's Zulip password (or LDAP password, if LDAP authentication is in use).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiKeyResponse]
            Valid credentials the client can use to access the Zulip API:
        """
        _response = self._client_wrapper.httpx_client.request(
            "fetch_api_key",
            method="POST",
            data={
                "username": username,
                "password": password,
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
                    ApiKeyResponse,
                    parse_obj_as(
                        type_=ApiKeyResponse,
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

    def jwt_fetch_api_key(
        self,
        *,
        token: str,
        include_profile: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JwtFetchApiKeyResponse]:
        """
        This API endpoint is used by clients to implement JSON Web Token
        (JWT) authentication. Given a JWT identifying a Zulip user, it
        returns a Zulip API key that the client can use to make requests
        as the user.

        !!! warn ""

            **Note:** This endpoint is only useful for Zulip servers/organizations
            with [JSON web token authentication][prod-jwt-auth] enabled.

        See the [API keys](/api/api-keys) documentation for more details
        on how to manage API keys manually.

        **Changes**: New in Zulip 7.0 (feature level 160).

        [prod-jwt-auth]: https://zulip.readthedocs.io/en/latest/production/authentication-methods.html#json-web-tokens-jwt

        Parameters
        ----------
        token : str
            A JSON Web Token for the target user.

            The token payload must contain a custom `email` claim with the target
            user's email address, e.g., `{"email": "<target user email>"}`.

        include_profile : typing.Optional[bool]
            Whether to include a `user` object containing the target
            user's profile details in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JwtFetchApiKeyResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "jwt/fetch_api_key",
            method="POST",
            data={
                "token": token,
                "include_profile": include_profile,
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
                    JwtFetchApiKeyResponse,
                    parse_obj_as(
                        type_=JwtFetchApiKeyResponse,
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

    def dev_fetch_api_key(
        self, *, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ApiKeyResponse]:
        """
        For easy testing of mobile apps and other clients and against Zulip
        development servers, we support fetching a Zulip API key for any user
        on the development server without authentication (so that they can
        implement analogues of the one-click login process available for Zulip
        development servers on the web).

        !!! warn ""

            **Note:** This endpoint is only available on Zulip development
            servers; for obvious security reasons it will always return an error
            in a Zulip production server.

        Parameters
        ----------
        username : str
            The email address for the user that owns the API key.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiKeyResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "dev_fetch_api_key",
            method="POST",
            data={
                "username": username,
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
                    ApiKeyResponse,
                    parse_obj_as(
                        type_=ApiKeyResponse,
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

    def dev_list_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DevListUsersResponse]:
        """
        Get a list of all, non-bot users in a [Zulip development
        server](https://zulip.readthedocs.io/en/latest/development/overview.html).
        This endpoint is used by mobile developers to fetch users for the
        development login flow.

        !!! warn ""

            **Note:** This endpoint is only available on Zulip development
            servers; for obvious security reasons it will always return an error
            in a Zulip production server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DevListUsersResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "dev_list_users",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DevListUsersResponse,
                    parse_obj_as(
                        type_=DevListUsersResponse,
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


class AsyncRawAuthenticationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def fetch_api_key(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApiKeyResponse]:
        """
        This API endpoint is used by clients such as the Zulip mobile and
        terminal apps to implement password-based authentication. Given the
        user's Zulip login credentials, it returns a Zulip API key that the client
        can use to make requests as the user.

        This endpoint is only useful for Zulip servers/organizations with
        EmailAuthBackend or LDAPAuthBackend enabled.

        The Zulip mobile apps also support SSO/social authentication (GitHub
        auth, Google auth, SAML, etc.) that does not use this endpoint. Instead,
        the mobile apps reuse the web login flow passing the `mobile_flow_otp` in
        a webview, and the credentials are returned to the app (encrypted) via a redirect
        to a `zulip://` URL.

        !!! warn ""

            **Note:** If you signed up using passwordless authentication and
            never had a password, you can [reset your password](/help/change-your-password).

        See the [API keys](/api/api-keys) documentation for more details
        on how to download an API key manually.

        In a [Zulip development environment](https://zulip.readthedocs.io/en/latest/development/overview.html),
        see also [the unauthenticated variant](/api/dev-fetch-api-key).

        Parameters
        ----------
        username : str
            The username to be used for authentication (typically, the email
            address, but depending on configuration, it could be an LDAP username).

            See the `require_email_format_usernames` parameter documented in
            [GET /server_settings](/api/get-server-settings) for details.

        password : str
            The user's Zulip password (or LDAP password, if LDAP authentication is in use).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiKeyResponse]
            Valid credentials the client can use to access the Zulip API:
        """
        _response = await self._client_wrapper.httpx_client.request(
            "fetch_api_key",
            method="POST",
            data={
                "username": username,
                "password": password,
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
                    ApiKeyResponse,
                    parse_obj_as(
                        type_=ApiKeyResponse,
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

    async def jwt_fetch_api_key(
        self,
        *,
        token: str,
        include_profile: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JwtFetchApiKeyResponse]:
        """
        This API endpoint is used by clients to implement JSON Web Token
        (JWT) authentication. Given a JWT identifying a Zulip user, it
        returns a Zulip API key that the client can use to make requests
        as the user.

        !!! warn ""

            **Note:** This endpoint is only useful for Zulip servers/organizations
            with [JSON web token authentication][prod-jwt-auth] enabled.

        See the [API keys](/api/api-keys) documentation for more details
        on how to manage API keys manually.

        **Changes**: New in Zulip 7.0 (feature level 160).

        [prod-jwt-auth]: https://zulip.readthedocs.io/en/latest/production/authentication-methods.html#json-web-tokens-jwt

        Parameters
        ----------
        token : str
            A JSON Web Token for the target user.

            The token payload must contain a custom `email` claim with the target
            user's email address, e.g., `{"email": "<target user email>"}`.

        include_profile : typing.Optional[bool]
            Whether to include a `user` object containing the target
            user's profile details in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JwtFetchApiKeyResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "jwt/fetch_api_key",
            method="POST",
            data={
                "token": token,
                "include_profile": include_profile,
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
                    JwtFetchApiKeyResponse,
                    parse_obj_as(
                        type_=JwtFetchApiKeyResponse,
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

    async def dev_fetch_api_key(
        self, *, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApiKeyResponse]:
        """
        For easy testing of mobile apps and other clients and against Zulip
        development servers, we support fetching a Zulip API key for any user
        on the development server without authentication (so that they can
        implement analogues of the one-click login process available for Zulip
        development servers on the web).

        !!! warn ""

            **Note:** This endpoint is only available on Zulip development
            servers; for obvious security reasons it will always return an error
            in a Zulip production server.

        Parameters
        ----------
        username : str
            The email address for the user that owns the API key.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiKeyResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "dev_fetch_api_key",
            method="POST",
            data={
                "username": username,
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
                    ApiKeyResponse,
                    parse_obj_as(
                        type_=ApiKeyResponse,
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

    async def dev_list_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DevListUsersResponse]:
        """
        Get a list of all, non-bot users in a [Zulip development
        server](https://zulip.readthedocs.io/en/latest/development/overview.html).
        This endpoint is used by mobile developers to fetch users for the
        development login flow.

        !!! warn ""

            **Note:** This endpoint is only available on Zulip development
            servers; for obvious security reasons it will always return an error
            in a Zulip production server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DevListUsersResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "dev_list_users",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DevListUsersResponse,
                    parse_obj_as(
                        type_=DevListUsersResponse,
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
