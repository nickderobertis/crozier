

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCredentialRequestsClient, RawCredentialRequestsClient
from .types.credential_requests_peek_response import CredentialRequestsPeekResponse
from .types.credential_requests_submit_response import CredentialRequestsSubmitResponse


OMIT = typing.cast(typing.Any, ...)


class CredentialRequestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCredentialRequestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCredentialRequestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCredentialRequestsClient
        """
        return self._raw_client

    def peek(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CredentialRequestsPeekResponse:
        """
        Returns the service/field/label the link collects. The token travels in the body so it never appears in URLs or access logs.

        Parameters
        ----------
        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CredentialRequestsPeekResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.credential_requests.peek(
            token="token",
        )
        """
        _response = self._raw_client.peek(token=token, request_options=request_options)
        return _response.data

    def submit(
        self, *, token: str, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CredentialRequestsSubmitResponse:
        """
        Single-use: atomically claims the link, forwards the value to the assistant's credential store, and marks the link redeemed.

        Parameters
        ----------
        token : str

        value : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CredentialRequestsSubmitResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.credential_requests.submit(
            token="token",
            value="value",
        )
        """
        _response = self._raw_client.submit(token=token, value=value, request_options=request_options)
        return _response.data


class AsyncCredentialRequestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCredentialRequestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCredentialRequestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCredentialRequestsClient
        """
        return self._raw_client

    async def peek(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CredentialRequestsPeekResponse:
        """
        Returns the service/field/label the link collects. The token travels in the body so it never appears in URLs or access logs.

        Parameters
        ----------
        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CredentialRequestsPeekResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.credential_requests.peek(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.peek(token=token, request_options=request_options)
        return _response.data

    async def submit(
        self, *, token: str, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CredentialRequestsSubmitResponse:
        """
        Single-use: atomically claims the link, forwards the value to the assistant's credential store, and marks the link redeemed.

        Parameters
        ----------
        token : str

        value : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CredentialRequestsSubmitResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.credential_requests.submit(
                token="token",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit(token=token, value=value, request_options=request_options)
        return _response.data
