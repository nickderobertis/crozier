

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.o_auth2client_dto import OAuth2ClientDto
from .raw_client import AsyncRawOAuth2Client, RawOAuth2Client


class OAuth2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOAuth2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOAuth2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOAuth2Client
        """
        return self._raw_client

    def get_o_auth2providers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OAuth2ClientDto]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OAuth2ClientDto]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.o_auth2.get_o_auth2providers()
        """
        _response = self._raw_client.get_o_auth2providers(request_options=request_options)
        return _response.data


class AsyncOAuth2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOAuth2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOAuth2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOAuth2Client
        """
        return self._raw_client

    async def get_o_auth2providers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OAuth2ClientDto]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OAuth2ClientDto]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.o_auth2.get_o_auth2providers()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_o_auth2providers(request_options=request_options)
        return _response.data
