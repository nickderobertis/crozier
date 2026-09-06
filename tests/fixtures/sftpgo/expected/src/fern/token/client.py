

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_response import ApiResponse
from ..types.token import Token
from .raw_client import AsyncRawTokenClient, RawTokenClient


class TokenClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTokenClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTokenClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTokenClient
        """
        return self._raw_client

    def get_token(
        self, *, sftpgo_otp: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Token:
        """
        Returns an access token and its expiration

        Parameters
        ----------
        sftpgo_otp : typing.Optional[str]
            If you have 2FA configured for the admin attempting to log in you need to set the authentication code using this header parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.token.get_token()
        """
        _response = self._raw_client.get_token(sftpgo_otp=sftpgo_otp, request_options=request_options)
        return _response.data

    def logout(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        Allows to invalidate an admin token before its expiration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.token.logout()
        """
        _response = self._raw_client.logout(request_options=request_options)
        return _response.data

    def get_user_token(
        self, *, sftpgo_otp: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Token:
        """
        Returns an access token and its expiration

        Parameters
        ----------
        sftpgo_otp : typing.Optional[str]
            If you have 2FA configured, for the HTTP protocol, for the user attempting to log in you need to set the authentication code using this header parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.token.get_user_token()
        """
        _response = self._raw_client.get_user_token(sftpgo_otp=sftpgo_otp, request_options=request_options)
        return _response.data

    def client_logout(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        Allows to invalidate a client token before its expiration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.token.client_logout()
        """
        _response = self._raw_client.client_logout(request_options=request_options)
        return _response.data


class AsyncTokenClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTokenClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTokenClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTokenClient
        """
        return self._raw_client

    async def get_token(
        self, *, sftpgo_otp: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Token:
        """
        Returns an access token and its expiration

        Parameters
        ----------
        sftpgo_otp : typing.Optional[str]
            If you have 2FA configured for the admin attempting to log in you need to set the authentication code using this header parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.token.get_token()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_token(sftpgo_otp=sftpgo_otp, request_options=request_options)
        return _response.data

    async def logout(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        Allows to invalidate an admin token before its expiration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.token.logout()


        asyncio.run(main())
        """
        _response = await self._raw_client.logout(request_options=request_options)
        return _response.data

    async def get_user_token(
        self, *, sftpgo_otp: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Token:
        """
        Returns an access token and its expiration

        Parameters
        ----------
        sftpgo_otp : typing.Optional[str]
            If you have 2FA configured, for the HTTP protocol, for the user attempting to log in you need to set the authentication code using this header parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Token
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.token.get_user_token()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_token(sftpgo_otp=sftpgo_otp, request_options=request_options)
        return _response.data

    async def client_logout(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        Allows to invalidate a client token before its expiration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.token.client_logout()


        asyncio.run(main())
        """
        _response = await self._raw_client.client_logout(request_options=request_options)
        return _response.data
