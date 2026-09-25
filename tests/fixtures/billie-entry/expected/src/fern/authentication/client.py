

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.token_response import TokenResponse
from .raw_client import AsyncRawAuthenticationClient, RawAuthenticationClient


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

    def createoauthtoken(
        self,
        *,
        grant_type: str,
        client_id: str,
        client_secret: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokenResponse:
        """
        Parameters
        ----------
        grant_type : str

        client_id : str

        client_secret : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Token created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authentication.createoauthtoken(
            grant_type="client_credentials",
            client_id="client_id",
            client_secret="client_secret",
        )
        """
        _response = self._raw_client.createoauthtoken(
            grant_type=grant_type, client_id=client_id, client_secret=client_secret, request_options=request_options
        )
        return _response.data

    def validateoauthtoken(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.authentication.validateoauthtoken()
        """
        _response = self._raw_client.validateoauthtoken(request_options=request_options)
        return _response.data

    def revokeoauthtoken(self, *, token: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        token : str

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
        client.authentication.revokeoauthtoken(
            token="token",
        )
        """
        _response = self._raw_client.revokeoauthtoken(token=token, request_options=request_options)
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

    async def createoauthtoken(
        self,
        *,
        grant_type: str,
        client_id: str,
        client_secret: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokenResponse:
        """
        Parameters
        ----------
        grant_type : str

        client_id : str

        client_secret : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Token created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authentication.createoauthtoken(
                grant_type="client_credentials",
                client_id="client_id",
                client_secret="client_secret",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createoauthtoken(
            grant_type=grant_type, client_id=client_id, client_secret=client_secret, request_options=request_options
        )
        return _response.data

    async def validateoauthtoken(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.authentication.validateoauthtoken()


        asyncio.run(main())
        """
        _response = await self._raw_client.validateoauthtoken(request_options=request_options)
        return _response.data

    async def revokeoauthtoken(self, *, token: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        token : str

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
            await client.authentication.revokeoauthtoken(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revokeoauthtoken(token=token, request_options=request_options)
        return _response.data
