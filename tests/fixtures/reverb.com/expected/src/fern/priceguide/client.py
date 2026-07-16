

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPriceguideClient, RawPriceguideClient


class PriceguideClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPriceguideClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPriceguideClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPriceguideClient
        """
        return self._raw_client

    def get_a_summary_of_transactions_for_a_given_price_guide(
        self,
        id: str,
        *,
        number_of_months: typing.Optional[int] = None,
        condition: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get a summary of transactions for a given price guide

        Parameters
        ----------
        id : str

        number_of_months : typing.Optional[int]

        condition : typing.Optional[str]

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
        client.priceguide.get_a_summary_of_transactions_for_a_given_price_guide(
            id="id",
        )
        """
        _response = self._raw_client.get_a_summary_of_transactions_for_a_given_price_guide(
            id, number_of_months=number_of_months, condition=condition, request_options=request_options
        )
        return _response.data


class AsyncPriceguideClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPriceguideClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPriceguideClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPriceguideClient
        """
        return self._raw_client

    async def get_a_summary_of_transactions_for_a_given_price_guide(
        self,
        id: str,
        *,
        number_of_months: typing.Optional[int] = None,
        condition: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get a summary of transactions for a given price guide

        Parameters
        ----------
        id : str

        number_of_months : typing.Optional[int]

        condition : typing.Optional[str]

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
            await client.priceguide.get_a_summary_of_transactions_for_a_given_price_guide(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_summary_of_transactions_for_a_given_price_guide(
            id, number_of_months=number_of_months, condition=condition, request_options=request_options
        )
        return _response.data
