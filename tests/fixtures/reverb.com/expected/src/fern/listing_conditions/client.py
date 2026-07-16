

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawListingConditionsClient, RawListingConditionsClient


class ListingConditionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawListingConditionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawListingConditionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawListingConditionsClient
        """
        return self._raw_client

    def list_of_supported_product_conditions(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List of supported product conditions

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
        client.listing_conditions.list_of_supported_product_conditions()
        """
        _response = self._raw_client.list_of_supported_product_conditions(request_options=request_options)
        return _response.data


class AsyncListingConditionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawListingConditionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawListingConditionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawListingConditionsClient
        """
        return self._raw_client

    async def list_of_supported_product_conditions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List of supported product conditions

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
            await client.listing_conditions.list_of_supported_product_conditions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_of_supported_product_conditions(request_options=request_options)
        return _response.data
