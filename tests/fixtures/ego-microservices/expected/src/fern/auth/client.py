

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.refresh_token_response import RefreshTokenResponse
from ..types.tokens_response import TokensResponse
from ..types.update_login_user_response import UpdateLoginUserResponse
from ..types.verify_status import VerifyStatus
from .raw_client import AsyncRawAuthClient, RawAuthClient
from .types.update_login_user_request_password import UpdateLoginUserRequestPassword
from .types.update_login_user_request_user_email import UpdateLoginUserRequestUserEmail


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

    def user_registration(
        self, *, username: str, password: str, user_email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TokensResponse:
        """
        Регистрация пользователя

        Parameters
        ----------
        username : str
            Никнейм пользователя

        password : str
            Пароль пользователя

        user_email : str
            Почта пользователя

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokensResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.user_registration(
            username="username",
            password="password",
            user_email="user_email",
        )
        """
        _response = self._raw_client.user_registration(
            username=username, password=password, user_email=user_email, request_options=request_options
        )
        return _response.data

    def user_login(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TokensResponse:
        """
        Вход пользователя и выдача токенов

        Parameters
        ----------
        username : str
            Никнейм пользователя

        password : str
            Пароль пользователя

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokensResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.user_login(
            username="username",
            password="password",
        )
        """
        _response = self._raw_client.user_login(username=username, password=password, request_options=request_options)
        return _response.data

    def token_verify(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> VerifyStatus:
        """
        Проверка токена

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifyStatus
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.token_verify(
            authorization="Authorization",
        )
        """
        _response = self._raw_client.token_verify(authorization=authorization, request_options=request_options)
        return _response.data

    def token_refresh(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RefreshTokenResponse:
        """
        Обновление токена

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RefreshTokenResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.token_refresh(
            authorization="Authorization",
        )
        """
        _response = self._raw_client.token_refresh(authorization=authorization, request_options=request_options)
        return _response.data

    def update_user_data_auth_users_update_user_patch(
        self,
        *,
        authorization: str,
        password: typing.Optional[UpdateLoginUserRequestPassword] = OMIT,
        user_email: typing.Optional[UpdateLoginUserRequestUserEmail] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateLoginUserResponse:
        """
        Обнавление данных пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        password : typing.Optional[UpdateLoginUserRequestPassword]

        user_email : typing.Optional[UpdateLoginUserRequestUserEmail]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateLoginUserResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.update_user_data_auth_users_update_user_patch(
            authorization="Authorization",
        )
        """
        _response = self._raw_client.update_user_data_auth_users_update_user_patch(
            authorization=authorization, password=password, user_email=user_email, request_options=request_options
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

    async def user_registration(
        self, *, username: str, password: str, user_email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TokensResponse:
        """
        Регистрация пользователя

        Parameters
        ----------
        username : str
            Никнейм пользователя

        password : str
            Пароль пользователя

        user_email : str
            Почта пользователя

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokensResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.user_registration(
                username="username",
                password="password",
                user_email="user_email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.user_registration(
            username=username, password=password, user_email=user_email, request_options=request_options
        )
        return _response.data

    async def user_login(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TokensResponse:
        """
        Вход пользователя и выдача токенов

        Parameters
        ----------
        username : str
            Никнейм пользователя

        password : str
            Пароль пользователя

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokensResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.user_login(
                username="username",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.user_login(
            username=username, password=password, request_options=request_options
        )
        return _response.data

    async def token_verify(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> VerifyStatus:
        """
        Проверка токена

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifyStatus
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.token_verify(
                authorization="Authorization",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.token_verify(authorization=authorization, request_options=request_options)
        return _response.data

    async def token_refresh(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RefreshTokenResponse:
        """
        Обновление токена

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RefreshTokenResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.token_refresh(
                authorization="Authorization",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.token_refresh(authorization=authorization, request_options=request_options)
        return _response.data

    async def update_user_data_auth_users_update_user_patch(
        self,
        *,
        authorization: str,
        password: typing.Optional[UpdateLoginUserRequestPassword] = OMIT,
        user_email: typing.Optional[UpdateLoginUserRequestUserEmail] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateLoginUserResponse:
        """
        Обнавление данных пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        password : typing.Optional[UpdateLoginUserRequestPassword]

        user_email : typing.Optional[UpdateLoginUserRequestUserEmail]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateLoginUserResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.update_user_data_auth_users_update_user_patch(
                authorization="Authorization",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user_data_auth_users_update_user_patch(
            authorization=authorization, password=password, user_email=user_email, request_options=request_options
        )
        return _response.data
