

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_key_response import ApiKeyResponse
from .raw_client import AsyncRawAuthenticationClient, RawAuthenticationClient
from .types.dev_list_users_response import DevListUsersResponse
from .types.jwt_fetch_api_key_response import JwtFetchApiKeyResponse


OMIT = typing.cast(typing.Any, ...)


class AuthenticationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthenticationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthenticationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthenticationClient
        """
        return self._raw_client

    def fetch_api_key(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKeyResponse:
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
        ApiKeyResponse
            Valid credentials the client can use to access the Zulip API:

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.authentication.fetch_api_key(
            username="iago@zulip.com",
            password="abcd1234",
        )
        """
        _response = self._raw_client.fetch_api_key(
            username=username, password=password, request_options=request_options
        )
        return _response.data

    def jwt_fetch_api_key(
        self,
        *,
        token: str,
        include_profile: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JwtFetchApiKeyResponse:
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
        JwtFetchApiKeyResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.authentication.jwt_fetch_api_key(
            token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImhhbWxldEB6dWxpcC5jb20ifQ.EsHxSVt54zPR-ywgPH54TB1FYmrGKsfq7hsQEhp_9w0",
        )
        """
        _response = self._raw_client.jwt_fetch_api_key(
            token=token, include_profile=include_profile, request_options=request_options
        )
        return _response.data

    def dev_fetch_api_key(
        self, *, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKeyResponse:
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
        ApiKeyResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.authentication.dev_fetch_api_key(
            username="iago@zulip.com",
        )
        """
        _response = self._raw_client.dev_fetch_api_key(username=username, request_options=request_options)
        return _response.data

    def dev_list_users(self, *, request_options: typing.Optional[RequestOptions] = None) -> DevListUsersResponse:
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
        DevListUsersResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.authentication.dev_list_users()
        """
        _response = self._raw_client.dev_list_users(request_options=request_options)
        return _response.data


class AsyncAuthenticationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthenticationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthenticationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthenticationClient
        """
        return self._raw_client

    async def fetch_api_key(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKeyResponse:
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
        ApiKeyResponse
            Valid credentials the client can use to access the Zulip API:

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.authentication.fetch_api_key(
                username="iago@zulip.com",
                password="abcd1234",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_api_key(
            username=username, password=password, request_options=request_options
        )
        return _response.data

    async def jwt_fetch_api_key(
        self,
        *,
        token: str,
        include_profile: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JwtFetchApiKeyResponse:
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
        JwtFetchApiKeyResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.authentication.jwt_fetch_api_key(
                token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImhhbWxldEB6dWxpcC5jb20ifQ.EsHxSVt54zPR-ywgPH54TB1FYmrGKsfq7hsQEhp_9w0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.jwt_fetch_api_key(
            token=token, include_profile=include_profile, request_options=request_options
        )
        return _response.data

    async def dev_fetch_api_key(
        self, *, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKeyResponse:
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
        ApiKeyResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.authentication.dev_fetch_api_key(
                username="iago@zulip.com",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.dev_fetch_api_key(username=username, request_options=request_options)
        return _response.data

    async def dev_list_users(self, *, request_options: typing.Optional[RequestOptions] = None) -> DevListUsersResponse:
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
        DevListUsersResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.authentication.dev_list_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.dev_list_users(request_options=request_options)
        return _response.data
