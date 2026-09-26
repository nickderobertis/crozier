

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawReferenceDataClient, RawReferenceDataClient


class ReferenceDataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReferenceDataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReferenceDataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReferenceDataClient
        """
        return self._raw_client

    def get_legal_forms(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Returns a list of available legal forms for company registration.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Legal forms retrieved

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.reference_data.get_legal_forms()
        """
        _response = self._raw_client.get_legal_forms(request_options=request_options)
        return _response.data


class AsyncReferenceDataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReferenceDataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReferenceDataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReferenceDataClient
        """
        return self._raw_client

    async def get_legal_forms(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Returns a list of available legal forms for company registration.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Legal forms retrieved

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.reference_data.get_legal_forms()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_legal_forms(request_options=request_options)
        return _response.data
