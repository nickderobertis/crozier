

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.amount import Amount
from ..types.invoice import Invoice
from ..types.line_item import LineItem
from .raw_client import AsyncRawInvoicesClient, RawInvoicesClient


OMIT = typing.cast(typing.Any, ...)


class InvoicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInvoicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInvoicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInvoicesClient
        """
        return self._raw_client

    def createinvoice(
        self,
        *,
        order_uuid: str,
        invoice_number: str,
        amount: Amount,
        invoice_url: typing.Optional[str] = OMIT,
        line_items: typing.Optional[typing.Sequence[LineItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Invoice:
        """
        Parameters
        ----------
        order_uuid : str

        invoice_number : str

        amount : Amount

        invoice_url : typing.Optional[str]

        line_items : typing.Optional[typing.Sequence[LineItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Invoice
            Invoice created

        Examples
        --------
        from fern import Amount, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.invoices.createinvoice(
            order_uuid="order_uuid",
            invoice_number="invoice_number",
            amount=Amount(
                net=1.1,
                gross=1.1,
                tax=1.1,
            ),
        )
        """
        _response = self._raw_client.createinvoice(
            order_uuid=order_uuid,
            invoice_number=invoice_number,
            amount=amount,
            invoice_url=invoice_url,
            line_items=line_items,
            request_options=request_options,
        )
        return _response.data

    def getinvoice(self, capture_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Invoice:
        """
        Parameters
        ----------
        capture_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Invoice
            Invoice details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.invoices.getinvoice(
            capture_id="captureId",
        )
        """
        _response = self._raw_client.getinvoice(capture_id, request_options=request_options)
        return _response.data

    def cancelinvoice(self, capture_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        capture_id : str

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
        client.invoices.cancelinvoice(
            capture_id="captureId",
        )
        """
        _response = self._raw_client.cancelinvoice(capture_id, request_options=request_options)
        return _response.data

    def updateinvoice(
        self,
        capture_id: str,
        *,
        invoice_number: typing.Optional[str] = OMIT,
        invoice_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        capture_id : str

        invoice_number : typing.Optional[str]

        invoice_url : typing.Optional[str]

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
        client.invoices.updateinvoice(
            capture_id="captureId",
        )
        """
        _response = self._raw_client.updateinvoice(
            capture_id, invoice_number=invoice_number, invoice_url=invoice_url, request_options=request_options
        )
        return _response.data

    def confirminvoicepayment(
        self, capture_id: str, *, paid_amount: float, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        capture_id : str

        paid_amount : float

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
        client.invoices.confirminvoicepayment(
            capture_id="captureId",
            paid_amount=1.1,
        )
        """
        _response = self._raw_client.confirminvoicepayment(
            capture_id, paid_amount=paid_amount, request_options=request_options
        )
        return _response.data

    def extendinvoiceduration(
        self, capture_id: str, *, duration: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        capture_id : str

        duration : int
            New duration in days

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
        client.invoices.extendinvoiceduration(
            capture_id="captureId",
            duration=1,
        )
        """
        _response = self._raw_client.extendinvoiceduration(
            capture_id, duration=duration, request_options=request_options
        )
        return _response.data

    def pauseinvoicedunning(self, capture_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        capture_id : str

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
        client.invoices.pauseinvoicedunning(
            capture_id="captureId",
        )
        """
        _response = self._raw_client.pauseinvoicedunning(capture_id, request_options=request_options)
        return _response.data


class AsyncInvoicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInvoicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInvoicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInvoicesClient
        """
        return self._raw_client

    async def createinvoice(
        self,
        *,
        order_uuid: str,
        invoice_number: str,
        amount: Amount,
        invoice_url: typing.Optional[str] = OMIT,
        line_items: typing.Optional[typing.Sequence[LineItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Invoice:
        """
        Parameters
        ----------
        order_uuid : str

        invoice_number : str

        amount : Amount

        invoice_url : typing.Optional[str]

        line_items : typing.Optional[typing.Sequence[LineItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Invoice
            Invoice created

        Examples
        --------
        import asyncio

        from fern import Amount, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invoices.createinvoice(
                order_uuid="order_uuid",
                invoice_number="invoice_number",
                amount=Amount(
                    net=1.1,
                    gross=1.1,
                    tax=1.1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createinvoice(
            order_uuid=order_uuid,
            invoice_number=invoice_number,
            amount=amount,
            invoice_url=invoice_url,
            line_items=line_items,
            request_options=request_options,
        )
        return _response.data

    async def getinvoice(self, capture_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Invoice:
        """
        Parameters
        ----------
        capture_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Invoice
            Invoice details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invoices.getinvoice(
                capture_id="captureId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getinvoice(capture_id, request_options=request_options)
        return _response.data

    async def cancelinvoice(self, capture_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        capture_id : str

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
            await client.invoices.cancelinvoice(
                capture_id="captureId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancelinvoice(capture_id, request_options=request_options)
        return _response.data

    async def updateinvoice(
        self,
        capture_id: str,
        *,
        invoice_number: typing.Optional[str] = OMIT,
        invoice_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        capture_id : str

        invoice_number : typing.Optional[str]

        invoice_url : typing.Optional[str]

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
            await client.invoices.updateinvoice(
                capture_id="captureId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateinvoice(
            capture_id, invoice_number=invoice_number, invoice_url=invoice_url, request_options=request_options
        )
        return _response.data

    async def confirminvoicepayment(
        self, capture_id: str, *, paid_amount: float, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        capture_id : str

        paid_amount : float

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
            await client.invoices.confirminvoicepayment(
                capture_id="captureId",
                paid_amount=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.confirminvoicepayment(
            capture_id, paid_amount=paid_amount, request_options=request_options
        )
        return _response.data

    async def extendinvoiceduration(
        self, capture_id: str, *, duration: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        capture_id : str

        duration : int
            New duration in days

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
            await client.invoices.extendinvoiceduration(
                capture_id="captureId",
                duration=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.extendinvoiceduration(
            capture_id, duration=duration, request_options=request_options
        )
        return _response.data

    async def pauseinvoicedunning(
        self, capture_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        capture_id : str

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
            await client.invoices.pauseinvoicedunning(
                capture_id="captureId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pauseinvoicedunning(capture_id, request_options=request_options)
        return _response.data
