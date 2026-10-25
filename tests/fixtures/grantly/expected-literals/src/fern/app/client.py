

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_envelope import ApiEnvelope
from .raw_client import AsyncRawAppClient, RawAppClient
from .types.get_auth_external_provider_request_provider import GetAuthExternalProviderRequestProvider


OMIT = typing.cast(typing.Any, ...)


class AppClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAppClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAppClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAppClient
        """
        return self._raw_client

    def provider_picker_login_page_html(
        self, *, interaction: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Renders Grantly's own login page listing enabled identity providers. Used both for third-party OIDC client logins (with an `interaction` param) and standalone visits.

        Parameters
        ----------
        interaction : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML login page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.app.provider_picker_login_page_html()
        """
        _response = self._raw_client.provider_picker_login_page_html(
            interaction=interaction, request_options=request_options
        )
        return _response.data

    def current_session_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiEnvelope:
        """
        Plain session-cookie check, distinct from /me (which requires a Bearer access token). A frontend dashboard calls this on load to decide whether to show a login or authenticated view. CORS-scoped to FRONTEND_URL, credentials required.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiEnvelope
            Logged-in user

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.app.current_session_user()
        """
        _response = self._raw_client.current_session_user(request_options=request_options)
        return _response.data

    def log_out(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Revokes every OIDC Grant (and its tokens) belonging to the session's user across all client apps, then destroys the local session.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.app.log_out()
        """
        _response = self._raw_client.log_out(request_options=request_options)
        return _response.data

    def start_upstream_o_auth_login(
        self,
        provider: GetAuthExternalProviderRequestProvider,
        *,
        interaction_uid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Redirects to the given identity provider's consent screen. Rate-limited to 10 requests/60s per IP. Must be opened as a browser navigation.

        Parameters
        ----------
        provider : GetAuthExternalProviderRequestProvider

        interaction_uid : typing.Optional[str]
            Only set when resuming a third-party OIDC interaction, never for Grantly's own dashboard login

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.app.start_upstream_o_auth_login(
            provider="google",
        )
        """
        _response = self._raw_client.start_upstream_o_auth_login(
            provider, interaction_uid=interaction_uid, request_options=request_options
        )
        return _response.data

    def upstream_o_auth_callback(
        self, provider: str, *, code: str, state: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Validates the `state` parameter (CSRF protection), exchanges the code with the provider, links or creates a user by verified email, establishes a session, then redirects either to the resumed OIDC interaction or to FRONTEND_URL/dashboard.

        Parameters
        ----------
        provider : str

        code : str

        state : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.app.upstream_o_auth_callback(
            provider="provider",
            code="code",
            state="state",
        )
        """
        _response = self._raw_client.upstream_o_auth_callback(
            provider, code=code, state=state, request_options=request_options
        )
        return _response.data

    def resolve_login_consent_prompt(
        self, uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Internal to the OIDC interaction flow - resolves the login and/or consent prompt for the given interaction.

        Parameters
        ----------
        uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.app.resolve_login_consent_prompt(
            uid="uid",
        )
        """
        _response = self._raw_client.resolve_login_consent_prompt(uid, request_options=request_options)
        return _response.data

    def list_my_applications(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiEnvelope:
        """
        Requires an active session. Never includes client_secret.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiEnvelope
            List of the user's applications

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.app.list_my_applications()
        """
        _response = self._raw_client.list_my_applications(request_options=request_options)
        return _response.data

    def create_an_o_auth_application(
        self,
        *,
        name: str,
        redirect_uris: typing.Sequence[str],
        grant_types: typing.Optional[typing.Sequence[str]] = OMIT,
        response_types: typing.Optional[typing.Sequence[str]] = OMIT,
        scopes: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiEnvelope:
        """
        Requires an active session. Creates a new client owned by the logged-in user. The response includes client_secret in plaintext exactly once - it is never retrievable again.

        Parameters
        ----------
        name : str

        redirect_uris : typing.Sequence[str]

        grant_types : typing.Optional[typing.Sequence[str]]

        response_types : typing.Optional[typing.Sequence[str]]

        scopes : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiEnvelope
            Created client, including plaintext secret

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.app.create_an_o_auth_application(
            name="name",
            redirect_uris=["redirectUris"],
        )
        """
        _response = self._raw_client.create_an_o_auth_application(
            name=name,
            redirect_uris=redirect_uris,
            grant_types=grant_types,
            response_types=response_types,
            scopes=scopes,
            request_options=request_options,
        )
        return _response.data

    def get_one_application(self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Requires an active session. Returns 404 whether the client doesn't exist or belongs to another user (same response either way, by design).

        Parameters
        ----------
        client_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.app.get_one_application(
            client_id="clientId",
        )
        """
        _response = self._raw_client.get_one_application(client_id, request_options=request_options)
        return _response.data

    def delete_an_application(self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        client_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.app.delete_an_application(
            client_id="clientId",
        )
        """
        _response = self._raw_client.delete_an_application(client_id, request_options=request_options)
        return _response.data


class AsyncAppClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAppClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAppClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAppClient
        """
        return self._raw_client

    async def provider_picker_login_page_html(
        self, *, interaction: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Renders Grantly's own login page listing enabled identity providers. Used both for third-party OIDC client logins (with an `interaction` param) and standalone visits.

        Parameters
        ----------
        interaction : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML login page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.app.provider_picker_login_page_html()


        asyncio.run(main())
        """
        _response = await self._raw_client.provider_picker_login_page_html(
            interaction=interaction, request_options=request_options
        )
        return _response.data

    async def current_session_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiEnvelope:
        """
        Plain session-cookie check, distinct from /me (which requires a Bearer access token). A frontend dashboard calls this on load to decide whether to show a login or authenticated view. CORS-scoped to FRONTEND_URL, credentials required.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiEnvelope
            Logged-in user

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.app.current_session_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.current_session_user(request_options=request_options)
        return _response.data

    async def log_out(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Revokes every OIDC Grant (and its tokens) belonging to the session's user across all client apps, then destroys the local session.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.app.log_out()


        asyncio.run(main())
        """
        _response = await self._raw_client.log_out(request_options=request_options)
        return _response.data

    async def start_upstream_o_auth_login(
        self,
        provider: GetAuthExternalProviderRequestProvider,
        *,
        interaction_uid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Redirects to the given identity provider's consent screen. Rate-limited to 10 requests/60s per IP. Must be opened as a browser navigation.

        Parameters
        ----------
        provider : GetAuthExternalProviderRequestProvider

        interaction_uid : typing.Optional[str]
            Only set when resuming a third-party OIDC interaction, never for Grantly's own dashboard login

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.app.start_upstream_o_auth_login(
                provider="google",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_upstream_o_auth_login(
            provider, interaction_uid=interaction_uid, request_options=request_options
        )
        return _response.data

    async def upstream_o_auth_callback(
        self, provider: str, *, code: str, state: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Validates the `state` parameter (CSRF protection), exchanges the code with the provider, links or creates a user by verified email, establishes a session, then redirects either to the resumed OIDC interaction or to FRONTEND_URL/dashboard.

        Parameters
        ----------
        provider : str

        code : str

        state : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.app.upstream_o_auth_callback(
                provider="provider",
                code="code",
                state="state",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upstream_o_auth_callback(
            provider, code=code, state=state, request_options=request_options
        )
        return _response.data

    async def resolve_login_consent_prompt(
        self, uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Internal to the OIDC interaction flow - resolves the login and/or consent prompt for the given interaction.

        Parameters
        ----------
        uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.app.resolve_login_consent_prompt(
                uid="uid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resolve_login_consent_prompt(uid, request_options=request_options)
        return _response.data

    async def list_my_applications(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiEnvelope:
        """
        Requires an active session. Never includes client_secret.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiEnvelope
            List of the user's applications

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.app.list_my_applications()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_my_applications(request_options=request_options)
        return _response.data

    async def create_an_o_auth_application(
        self,
        *,
        name: str,
        redirect_uris: typing.Sequence[str],
        grant_types: typing.Optional[typing.Sequence[str]] = OMIT,
        response_types: typing.Optional[typing.Sequence[str]] = OMIT,
        scopes: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiEnvelope:
        """
        Requires an active session. Creates a new client owned by the logged-in user. The response includes client_secret in plaintext exactly once - it is never retrievable again.

        Parameters
        ----------
        name : str

        redirect_uris : typing.Sequence[str]

        grant_types : typing.Optional[typing.Sequence[str]]

        response_types : typing.Optional[typing.Sequence[str]]

        scopes : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiEnvelope
            Created client, including plaintext secret

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.app.create_an_o_auth_application(
                name="name",
                redirect_uris=["redirectUris"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_an_o_auth_application(
            name=name,
            redirect_uris=redirect_uris,
            grant_types=grant_types,
            response_types=response_types,
            scopes=scopes,
            request_options=request_options,
        )
        return _response.data

    async def get_one_application(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Requires an active session. Returns 404 whether the client doesn't exist or belongs to another user (same response either way, by design).

        Parameters
        ----------
        client_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.app.get_one_application(
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_one_application(client_id, request_options=request_options)
        return _response.data

    async def delete_an_application(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        client_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.app.delete_an_application(
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_an_application(client_id, request_options=request_options)
        return _response.data
