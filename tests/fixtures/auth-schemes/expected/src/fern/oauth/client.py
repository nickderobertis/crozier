

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.token_response import TokenResponse
from .raw_client import AsyncRawOauthClient, RawOauthClient


OMIT = typing.cast(typing.Any, ...)


class OauthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOauthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOauthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOauthClient
        """
        return self._raw_client

    def gettoken(
        self, *, client_id: str, client_secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TokenResponse:
        """
        Parameters
        ----------
        client_id : str

        client_secret : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.oauth.gettoken(
            client_id="client_id",
            client_secret="client_secret",
        )
        """
        _response = self._raw_client.gettoken(
            client_id=client_id, client_secret=client_secret, request_options=request_options
        )
        return _response.data


class AsyncOauthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOauthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOauthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOauthClient
        """
        return self._raw_client

    async def gettoken(
        self, *, client_id: str, client_secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TokenResponse:
        """
        Parameters
        ----------
        client_id : str

        client_secret : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.oauth.gettoken(
                client_id="client_id",
                client_secret="client_secret",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gettoken(
            client_id=client_id, client_secret=client_secret, request_options=request_options
        )
        return _response.data
