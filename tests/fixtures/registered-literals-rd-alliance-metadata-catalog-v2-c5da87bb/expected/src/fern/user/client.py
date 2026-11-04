

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.response_password import ResponsePassword
from .raw_client import AsyncRawUserClient, RawUserClient
from .types.get_api2user_token_response import GetApi2UserTokenResponse


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

    def change_api_user_password(
        self, *, new_password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePassword:
        """
        Parameters
        ----------
        new_password : str
            New password to use for subsequent calls.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePassword
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user.change_api_user_password(
            new_password="new_password",
        )
        """
        _response = self._raw_client.change_api_user_password(
            new_password=new_password, request_options=request_options
        )
        return _response.data

    def request_an_authorization_token(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApi2UserTokenResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApi2UserTokenResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user.request_an_authorization_token()
        """
        _response = self._raw_client.request_an_authorization_token(request_options=request_options)
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

    async def change_api_user_password(
        self, *, new_password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ResponsePassword:
        """
        Parameters
        ----------
        new_password : str
            New password to use for subsequent calls.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResponsePassword
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user.change_api_user_password(
                new_password="new_password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.change_api_user_password(
            new_password=new_password, request_options=request_options
        )
        return _response.data

    async def request_an_authorization_token(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApi2UserTokenResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApi2UserTokenResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.user.request_an_authorization_token()


        asyncio.run(main())
        """
        _response = await self._raw_client.request_an_authorization_token(request_options=request_options)
        return _response.data
