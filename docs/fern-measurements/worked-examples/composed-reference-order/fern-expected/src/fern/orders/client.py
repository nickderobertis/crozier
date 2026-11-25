

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.buyer import Buyer
from ..types.charterer import Charterer
from ..types.lessee import Lessee
from ..types.receipt import Receipt
from ..types.terms import Terms
from .raw_client import AsyncRawOrdersClient, RawOrdersClient


OMIT = typing.cast(typing.Any, ...)


class OrdersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrdersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrdersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrdersClient
        """
        return self._raw_client

    def place_order(
        self,
        *,
        buyer: Buyer,
        charterer: Charterer,
        lessee: Lessee,
        terms: Terms,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Receipt:
        """
        Parameters
        ----------
        buyer : Buyer

        charterer : Charterer

        lessee : Lessee

        terms : Terms

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Receipt
            Placed

        Examples
        --------
        from fern import Buyer, Charterer, FernApi, Lessee, Terms

        client = FernApi()
        client.orders.place_order(
            buyer=Buyer(
                pier="pier",
                slip=1,
                name="name",
                phone="phone",
            ),
            charterer=Charterer(
                pier="pier",
                slip=1,
                name="name",
                phone="phone",
            ),
            lessee=Lessee(
                pier="pier",
                slip=1,
                name="name",
                phone="phone",
                deck="deck",
            ),
            terms=Terms(
                kind="kind",
                due_on="due_on",
            ),
        )
        """
        _response = self._raw_client.place_order(
            buyer=buyer, charterer=charterer, lessee=lessee, terms=terms, request_options=request_options
        )
        return _response.data


class AsyncOrdersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrdersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrdersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrdersClient
        """
        return self._raw_client

    async def place_order(
        self,
        *,
        buyer: Buyer,
        charterer: Charterer,
        lessee: Lessee,
        terms: Terms,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Receipt:
        """
        Parameters
        ----------
        buyer : Buyer

        charterer : Charterer

        lessee : Lessee

        terms : Terms

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Receipt
            Placed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Buyer, Charterer, Lessee, Terms

        client = AsyncFernApi()


        async def main() -> None:
            await client.orders.place_order(
                buyer=Buyer(
                    pier="pier",
                    slip=1,
                    name="name",
                    phone="phone",
                ),
                charterer=Charterer(
                    pier="pier",
                    slip=1,
                    name="name",
                    phone="phone",
                ),
                lessee=Lessee(
                    pier="pier",
                    slip=1,
                    name="name",
                    phone="phone",
                    deck="deck",
                ),
                terms=Terms(
                    kind="kind",
                    due_on="due_on",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.place_order(
            buyer=buyer, charterer=charterer, lessee=lessee, terms=terms, request_options=request_options
        )
        return _response.data
