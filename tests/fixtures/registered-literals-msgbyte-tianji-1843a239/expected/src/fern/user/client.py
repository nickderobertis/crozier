

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawUserClient, RawUserClient
from .types.user_login_response import UserLoginResponse
from .types.user_login_with_token_response import UserLoginWithTokenResponse
from .types.user_register_response import UserRegisterResponse


OMIT = typing.cast(typing.Any, ...)


class UserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserClient
        """
        return self._raw_client

    def login(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UserLoginResponse:
        """
        Parameters
        ----------
        username : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserLoginResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.login(
            username="username",
            password="password",
        )
        """
        _response = self._raw_client.login(username=username, password=password, request_options=request_options)
        return _response.data

    def loginwithtoken(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UserLoginWithTokenResponse:
        """
        Parameters
        ----------
        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserLoginWithTokenResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.loginwithtoken(
            token="token",
        )
        """
        _response = self._raw_client.loginwithtoken(token=token, request_options=request_options)
        return _response.data

    def register(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UserRegisterResponse:
        """
        Parameters
        ----------
        username : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserRegisterResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user.register(
            username="username",
            password="password",
        )
        """
        _response = self._raw_client.register(username=username, password=password, request_options=request_options)
        return _response.data


class AsyncUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserClient
        """
        return self._raw_client

    async def login(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UserLoginResponse:
        """
        Parameters
        ----------
        username : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserLoginResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.login(
                username="username",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.login(username=username, password=password, request_options=request_options)
        return _response.data

    async def loginwithtoken(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UserLoginWithTokenResponse:
        """
        Parameters
        ----------
        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserLoginWithTokenResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.loginwithtoken(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.loginwithtoken(token=token, request_options=request_options)
        return _response.data

    async def register(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UserRegisterResponse:
        """
        Parameters
        ----------
        username : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserRegisterResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.register(
                username="username",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register(
            username=username, password=password, request_options=request_options
        )
        return _response.data
