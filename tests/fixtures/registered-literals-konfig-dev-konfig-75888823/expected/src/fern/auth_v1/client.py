

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_id import AppId
from ..types.login_response import LoginResponse
from .raw_client import AsyncRawAuthV1Client, RawAuthV1Client


OMIT = typing.cast(typing.Any, ...)


class AuthV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthV1Client
        """
        return self._raw_client

    def login_anonymous(
        self, app_id: AppId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LoginResponse:
        """
        Returns a unique player token for an anonymous user.

        Parameters
        ----------
        app_id : AppId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginResponse
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth_v1.login_anonymous(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
        )
        """
        _response = self._raw_client.login_anonymous(app_id, request_options=request_options)
        return _response.data

    def login_nickname(
        self, app_id: AppId, *, nickname: str, request_options: typing.Optional[RequestOptions] = None
    ) -> LoginResponse:
        """
        Returns a unique player token with a specified nickname for a user.

        Parameters
        ----------
        app_id : AppId

        nickname : str
            An alias to represent a player.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginResponse
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth_v1.login_nickname(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            nickname="squiddytwoshoes",
        )
        """
        _response = self._raw_client.login_nickname(app_id, nickname=nickname, request_options=request_options)
        return _response.data

    def login_google(
        self, app_id: AppId, *, id_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> LoginResponse:
        """
        Returns a unique player token using a Google-signed OIDC `idToken`.

        Parameters
        ----------
        app_id : AppId

        id_token : str
            A Google-signed OIDC ID token representing a player's authenticated identity. Learn how to get an `idToken` [here](https://cloud.google.com/docs/authentication/get-id-token).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginResponse
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth_v1.login_google(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            id_token="eyJhbGciOiJSUzI1NiIsImtpZCI6ImZkNDhhNzUxMzhkOWQ0OGYwYWE2MzVlZjU2OWM0ZTE5NmY3YWU4ZDYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiODQ4NDEyODI2Nzg4LW00bXNyYjZxNDRkbTJ1ZTNrZ3Z1aTBmcTdrZGE1NWxzLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiODQ4NDEyODI2Nzg4LW00bXNyYjZxNDRkbTJ1ZTNrZ3Z1aTBmcTdrZGE1NWxzLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTE0NTQyMzMwNzI3MTU2MTMzNzc2IiwiZW1haWwiOiJocGFdkeivmeuzQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhdF9oYXNoIjoidno1NGhhdTNxbnVR",
        )
        """
        _response = self._raw_client.login_google(app_id, id_token=id_token, request_options=request_options)
        return _response.data


class AsyncAuthV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthV1Client
        """
        return self._raw_client

    async def login_anonymous(
        self, app_id: AppId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LoginResponse:
        """
        Returns a unique player token for an anonymous user.

        Parameters
        ----------
        app_id : AppId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginResponse
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth_v1.login_anonymous(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.login_anonymous(app_id, request_options=request_options)
        return _response.data

    async def login_nickname(
        self, app_id: AppId, *, nickname: str, request_options: typing.Optional[RequestOptions] = None
    ) -> LoginResponse:
        """
        Returns a unique player token with a specified nickname for a user.

        Parameters
        ----------
        app_id : AppId

        nickname : str
            An alias to represent a player.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginResponse
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth_v1.login_nickname(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                nickname="squiddytwoshoes",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.login_nickname(app_id, nickname=nickname, request_options=request_options)
        return _response.data

    async def login_google(
        self, app_id: AppId, *, id_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> LoginResponse:
        """
        Returns a unique player token using a Google-signed OIDC `idToken`.

        Parameters
        ----------
        app_id : AppId

        id_token : str
            A Google-signed OIDC ID token representing a player's authenticated identity. Learn how to get an `idToken` [here](https://cloud.google.com/docs/authentication/get-id-token).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginResponse
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth_v1.login_google(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                id_token="eyJhbGciOiJSUzI1NiIsImtpZCI6ImZkNDhhNzUxMzhkOWQ0OGYwYWE2MzVlZjU2OWM0ZTE5NmY3YWU4ZDYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiODQ4NDEyODI2Nzg4LW00bXNyYjZxNDRkbTJ1ZTNrZ3Z1aTBmcTdrZGE1NWxzLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiODQ4NDEyODI2Nzg4LW00bXNyYjZxNDRkbTJ1ZTNrZ3Z1aTBmcTdrZGE1NWxzLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTE0NTQyMzMwNzI3MTU2MTMzNzc2IiwiZW1haWwiOiJocGFdkeivmeuzQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhdF9oYXNoIjoidno1NGhhdTNxbnVR",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.login_google(app_id, id_token=id_token, request_options=request_options)
        return _response.data
