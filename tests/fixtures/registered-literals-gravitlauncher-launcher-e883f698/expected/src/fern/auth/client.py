

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.auth_token import AuthToken
from ..types.check_server_response import CheckServerResponse
from ..types.self_user import SelfUser
from .raw_client import AsyncRawAuthClient, RawAuthClient


OMIT = typing.cast(typing.Any, ...)


class AuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthClient
        """
        return self._raw_client

    def authenticate_with_login_password_optional_totp(
        self,
        *,
        login: str,
        password: typing.Optional[str] = OMIT,
        totp: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthToken:
        """
        Parameters
        ----------
        login : str

        password : typing.Optional[str]

        totp : typing.Optional[str]
            TOTP one-time code (6 digits).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthToken
            Authentication successful.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.authenticate_with_login_password_optional_totp(
            login="login",
        )
        """
        _response = self._raw_client.authenticate_with_login_password_optional_totp(
            login=login, password=password, totp=totp, request_options=request_options
        )
        return _response.data

    def refresh_an_access_token_using_a_refresh_token(
        self, *, refresh_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthToken:
        """
        Parameters
        ----------
        refresh_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthToken
            New token pair.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.refresh_an_access_token_using_a_refresh_token(
            refresh_token="refreshToken",
        )
        """
        _response = self._raw_client.refresh_an_access_token_using_a_refresh_token(
            refresh_token=refresh_token, request_options=request_options
        )
        return _response.data

    def invalidate_the_current_session(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
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
            token="YOUR_TOKEN",
        )
        client.auth.invalidate_the_current_session()
        """
        _response = self._raw_client.invalidate_the_current_session(request_options=request_options)
        return _response.data

    def get_the_authenticated_users_own_profile(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SelfUser:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SelfUser
            Current user.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.get_the_authenticated_users_own_profile()
        """
        _response = self._raw_client.get_the_authenticated_users_own_profile(request_options=request_options)
        return _response.data

    def join_a_game_server_identified_by_username(
        self,
        *,
        username: str,
        server_id: str,
        access_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        username : str

        server_id : str

        access_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.join_a_game_server_identified_by_username(
            username="username",
            server_id="serverId",
            access_token="accessToken",
        )
        """
        _response = self._raw_client.join_a_game_server_identified_by_username(
            username=username, server_id=server_id, access_token=access_token, request_options=request_options
        )
        return _response.data

    def join_a_game_server_identified_by_uuid(
        self, *, uuid_: str, server_id: str, access_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        uuid_ : str

        server_id : str

        access_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.join_a_game_server_identified_by_uuid(
            uuid_="uuid",
            server_id="serverId",
            access_token="accessToken",
        )
        """
        _response = self._raw_client.join_a_game_server_identified_by_uuid(
            uuid_=uuid_, server_id=server_id, access_token=access_token, request_options=request_options
        )
        return _response.data

    def verify_that_a_player_has_joined_a_server_server_side_validation(
        self,
        *,
        username: str,
        server_id: str,
        extended: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckServerResponse:
        """
        Parameters
        ----------
        username : str

        server_id : str

        extended : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckServerResponse
            Server check result.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.verify_that_a_player_has_joined_a_server_server_side_validation(
            username="username",
            server_id="serverId",
        )
        """
        _response = self._raw_client.verify_that_a_player_has_joined_a_server_server_side_validation(
            username=username, server_id=server_id, extended=extended, request_options=request_options
        )
        return _response.data


class AsyncAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthClient
        """
        return self._raw_client

    async def authenticate_with_login_password_optional_totp(
        self,
        *,
        login: str,
        password: typing.Optional[str] = OMIT,
        totp: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthToken:
        """
        Parameters
        ----------
        login : str

        password : typing.Optional[str]

        totp : typing.Optional[str]
            TOTP one-time code (6 digits).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthToken
            Authentication successful.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.authenticate_with_login_password_optional_totp(
                login="login",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.authenticate_with_login_password_optional_totp(
            login=login, password=password, totp=totp, request_options=request_options
        )
        return _response.data

    async def refresh_an_access_token_using_a_refresh_token(
        self, *, refresh_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthToken:
        """
        Parameters
        ----------
        refresh_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthToken
            New token pair.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.refresh_an_access_token_using_a_refresh_token(
                refresh_token="refreshToken",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.refresh_an_access_token_using_a_refresh_token(
            refresh_token=refresh_token, request_options=request_options
        )
        return _response.data

    async def invalidate_the_current_session(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.invalidate_the_current_session()


        asyncio.run(main())
        """
        _response = await self._raw_client.invalidate_the_current_session(request_options=request_options)
        return _response.data

    async def get_the_authenticated_users_own_profile(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SelfUser:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SelfUser
            Current user.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.get_the_authenticated_users_own_profile()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_the_authenticated_users_own_profile(request_options=request_options)
        return _response.data

    async def join_a_game_server_identified_by_username(
        self,
        *,
        username: str,
        server_id: str,
        access_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        username : str

        server_id : str

        access_token : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.join_a_game_server_identified_by_username(
                username="username",
                server_id="serverId",
                access_token="accessToken",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.join_a_game_server_identified_by_username(
            username=username, server_id=server_id, access_token=access_token, request_options=request_options
        )
        return _response.data

    async def join_a_game_server_identified_by_uuid(
        self, *, uuid_: str, server_id: str, access_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        uuid_ : str

        server_id : str

        access_token : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.join_a_game_server_identified_by_uuid(
                uuid_="uuid",
                server_id="serverId",
                access_token="accessToken",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.join_a_game_server_identified_by_uuid(
            uuid_=uuid_, server_id=server_id, access_token=access_token, request_options=request_options
        )
        return _response.data

    async def verify_that_a_player_has_joined_a_server_server_side_validation(
        self,
        *,
        username: str,
        server_id: str,
        extended: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckServerResponse:
        """
        Parameters
        ----------
        username : str

        server_id : str

        extended : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckServerResponse
            Server check result.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.verify_that_a_player_has_joined_a_server_server_side_validation(
                username="username",
                server_id="serverId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_that_a_player_has_joined_a_server_server_side_validation(
            username=username, server_id=server_id, extended=extended, request_options=request_options
        )
        return _response.data
