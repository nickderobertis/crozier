

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPurchaseOrdersClient, RawPurchaseOrdersClient


OMIT = typing.cast(typing.Any, ...)


class PurchaseOrdersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPurchaseOrdersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPurchaseOrdersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPurchaseOrdersClient
        """
        return self._raw_client

    def listpurchaseorders(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        per_page : typing.Optional[int]

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
        client.purchase_orders.listpurchaseorders()
        """
        _response = self._raw_client.listpurchaseorders(page=page, per_page=per_page, request_options=request_options)
        return _response.data

    def createpurchaseorder(
        self,
        *,
        supplier_id: str,
        description: str,
        amount: float,
        currency: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        supplier_id : str

        description : str

        amount : float

        currency : str

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
        client.purchase_orders.createpurchaseorder(
            supplier_id="supplier_id",
            description="description",
            amount=1.1,
            currency="currency",
        )
        """
        _response = self._raw_client.createpurchaseorder(
            supplier_id=supplier_id,
            description=description,
            amount=amount,
            currency=currency,
            request_options=request_options,
        )
        return _response.data

    def getpurchaseorder(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.purchase_orders.getpurchaseorder(
            id="id",
        )
        """
        _response = self._raw_client.getpurchaseorder(id, request_options=request_options)
        return _response.data

    def cancelpurchaseorder(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.purchase_orders.cancelpurchaseorder(
            id="id",
        )
        """
        _response = self._raw_client.cancelpurchaseorder(id, request_options=request_options)
        return _response.data

    def closepurchaseorder(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.purchase_orders.closepurchaseorder(
            id="id",
        )
        """
        _response = self._raw_client.closepurchaseorder(id, request_options=request_options)
        return _response.data


class AsyncPurchaseOrdersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPurchaseOrdersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPurchaseOrdersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPurchaseOrdersClient
        """
        return self._raw_client

    async def listpurchaseorders(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        per_page : typing.Optional[int]

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
            await client.purchase_orders.listpurchaseorders()


        asyncio.run(main())
        """
        _response = await self._raw_client.listpurchaseorders(
            page=page, per_page=per_page, request_options=request_options
        )
        return _response.data

    async def createpurchaseorder(
        self,
        *,
        supplier_id: str,
        description: str,
        amount: float,
        currency: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        supplier_id : str

        description : str

        amount : float

        currency : str

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
            await client.purchase_orders.createpurchaseorder(
                supplier_id="supplier_id",
                description="description",
                amount=1.1,
                currency="currency",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createpurchaseorder(
            supplier_id=supplier_id,
            description=description,
            amount=amount,
            currency=currency,
            request_options=request_options,
        )
        return _response.data

    async def getpurchaseorder(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.purchase_orders.getpurchaseorder(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpurchaseorder(id, request_options=request_options)
        return _response.data

    async def cancelpurchaseorder(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.purchase_orders.cancelpurchaseorder(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancelpurchaseorder(id, request_options=request_options)
        return _response.data

    async def closepurchaseorder(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.purchase_orders.closepurchaseorder(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.closepurchaseorder(id, request_options=request_options)
        return _response.data
