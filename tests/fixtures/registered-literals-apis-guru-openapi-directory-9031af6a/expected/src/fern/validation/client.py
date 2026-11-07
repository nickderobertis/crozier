

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawValidationClient, RawValidationClient
from .types.get_validity_response import GetValidityResponse


class ValidationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawValidationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawValidationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawValidationClient
        """
        return self._raw_client

    def get_validity(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetValidityResponse:
        """
        Endpoint used to test the validity and some basic information about a specific API Key.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetValidityResponse
            Key validation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.validation.get_validity()
        """
        _response = self._raw_client.get_validity(request_options=request_options)
        return _response.data


class AsyncValidationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawValidationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawValidationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawValidationClient
        """
        return self._raw_client

    async def get_validity(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetValidityResponse:
        """
        Endpoint used to test the validity and some basic information about a specific API Key.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetValidityResponse
            Key validation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.validation.get_validity()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_validity(request_options=request_options)
        return _response.data
