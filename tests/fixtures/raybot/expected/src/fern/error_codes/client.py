

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.error_code_response import ErrorCodeResponse
from .raw_client import AsyncRawErrorCodesClient, RawErrorCodesClient


class ErrorCodesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawErrorCodesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawErrorCodesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawErrorCodesClient
        """
        return self._raw_client

    def get_error_codes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ErrorCodeResponse]:
        """
        Get all error codes

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ErrorCodeResponse]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.error_codes.get_error_codes()
        """
        _response = self._raw_client.get_error_codes(request_options=request_options)
        return _response.data


class AsyncErrorCodesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawErrorCodesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawErrorCodesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawErrorCodesClient
        """
        return self._raw_client

    async def get_error_codes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ErrorCodeResponse]:
        """
        Get all error codes

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ErrorCodeResponse]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.error_codes.get_error_codes()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_error_codes(request_options=request_options)
        return _response.data
