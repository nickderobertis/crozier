

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.amount import Amount
from ..types.debtor import Debtor
from ..types.debtor_person import DebtorPerson
from ..types.line_item import LineItem
from ..types.order import Order
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

    def createorder(
        self,
        *,
        amount: Amount,
        duration: int,
        debtor: Debtor,
        debtor_person: typing.Optional[DebtorPerson] = OMIT,
        line_items: typing.Optional[typing.Sequence[LineItem]] = OMIT,
        external_code: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Order:
        """
        Parameters
        ----------
        amount : Amount

        duration : int
            Payment term in days

        debtor : Debtor

        debtor_person : typing.Optional[DebtorPerson]

        line_items : typing.Optional[typing.Sequence[LineItem]]

        external_code : typing.Optional[str]

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Order
            Order created

        Examples
        --------
        from fern import Amount, Debtor, DebtorAddress, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.createorder(
            amount=Amount(
                net=1.1,
                gross=1.1,
                tax=1.1,
            ),
            duration=1,
            debtor=Debtor(
                name="name",
                address=DebtorAddress(
                    street="street",
                    city="city",
                    postal_code="postal_code",
                    country="country",
                ),
            ),
        )
        """
        _response = self._raw_client.createorder(
            amount=amount,
            duration=duration,
            debtor=debtor,
            debtor_person=debtor_person,
            line_items=line_items,
            external_code=external_code,
            comment=comment,
            request_options=request_options,
        )
        return _response.data

    def getorder(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Order:
        """
        Parameters
        ----------
        id : str
            Order UUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Order
            Order details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.getorder(
            id="id",
        )
        """
        _response = self._raw_client.getorder(id, request_options=request_options)
        return _response.data

    def updateorder(
        self,
        id: str,
        *,
        amount: typing.Optional[Amount] = OMIT,
        duration: typing.Optional[int] = OMIT,
        external_code: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Order:
        """
        Parameters
        ----------
        id : str

        amount : typing.Optional[Amount]

        duration : typing.Optional[int]

        external_code : typing.Optional[str]

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Order
            Order updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.updateorder(
            id="id",
        )
        """
        _response = self._raw_client.updateorder(
            id,
            amount=amount,
            duration=duration,
            external_code=external_code,
            comment=comment,
            request_options=request_options,
        )
        return _response.data

    def cancelorder(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
        client.orders.cancelorder(
            id="id",
        )
        """
        _response = self._raw_client.cancelorder(id, request_options=request_options)
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

    async def createorder(
        self,
        *,
        amount: Amount,
        duration: int,
        debtor: Debtor,
        debtor_person: typing.Optional[DebtorPerson] = OMIT,
        line_items: typing.Optional[typing.Sequence[LineItem]] = OMIT,
        external_code: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Order:
        """
        Parameters
        ----------
        amount : Amount

        duration : int
            Payment term in days

        debtor : Debtor

        debtor_person : typing.Optional[DebtorPerson]

        line_items : typing.Optional[typing.Sequence[LineItem]]

        external_code : typing.Optional[str]

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Order
            Order created

        Examples
        --------
        import asyncio

        from fern import Amount, AsyncFernApi, Debtor, DebtorAddress

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.createorder(
                amount=Amount(
                    net=1.1,
                    gross=1.1,
                    tax=1.1,
                ),
                duration=1,
                debtor=Debtor(
                    name="name",
                    address=DebtorAddress(
                        street="street",
                        city="city",
                        postal_code="postal_code",
                        country="country",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createorder(
            amount=amount,
            duration=duration,
            debtor=debtor,
            debtor_person=debtor_person,
            line_items=line_items,
            external_code=external_code,
            comment=comment,
            request_options=request_options,
        )
        return _response.data

    async def getorder(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Order:
        """
        Parameters
        ----------
        id : str
            Order UUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Order
            Order details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.getorder(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getorder(id, request_options=request_options)
        return _response.data

    async def updateorder(
        self,
        id: str,
        *,
        amount: typing.Optional[Amount] = OMIT,
        duration: typing.Optional[int] = OMIT,
        external_code: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Order:
        """
        Parameters
        ----------
        id : str

        amount : typing.Optional[Amount]

        duration : typing.Optional[int]

        external_code : typing.Optional[str]

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Order
            Order updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.updateorder(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateorder(
            id,
            amount=amount,
            duration=duration,
            external_code=external_code,
            comment=comment,
            request_options=request_options,
        )
        return _response.data

    async def cancelorder(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            await client.orders.cancelorder(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancelorder(id, request_options=request_options)
        return _response.data
