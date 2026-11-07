

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.invoice import Invoice
from ..types.payment_method import PaymentMethod
from .raw_client import AsyncRawBillingV1Client, RawBillingV1Client


OMIT = typing.cast(typing.Any, ...)


class BillingV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBillingV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBillingV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBillingV1Client
        """
        return self._raw_client

    def get_balance(self, *, request_options: typing.Optional[RequestOptions] = None) -> float:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing_v1.get_balance()
        """
        _response = self._raw_client.get_balance(request_options=request_options)
        return _response.data

    def get_payment_method(self, *, request_options: typing.Optional[RequestOptions] = None) -> PaymentMethod:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentMethod
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing_v1.get_payment_method()
        """
        _response = self._raw_client.get_payment_method(request_options=request_options)
        return _response.data

    def init_stripe_customer_portal_url(
        self, *, return_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        return_url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing_v1.init_stripe_customer_portal_url(
            return_url="returnUrl",
        )
        """
        _response = self._raw_client.init_stripe_customer_portal_url(
            return_url=return_url, request_options=request_options
        )
        return _response.data

    def get_invoices(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Invoice]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Invoice]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing_v1.get_invoices()
        """
        _response = self._raw_client.get_invoices(request_options=request_options)
        return _response.data


class AsyncBillingV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBillingV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBillingV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBillingV1Client
        """
        return self._raw_client

    async def get_balance(self, *, request_options: typing.Optional[RequestOptions] = None) -> float:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing_v1.get_balance()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_balance(request_options=request_options)
        return _response.data

    async def get_payment_method(self, *, request_options: typing.Optional[RequestOptions] = None) -> PaymentMethod:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentMethod
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing_v1.get_payment_method()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_payment_method(request_options=request_options)
        return _response.data

    async def init_stripe_customer_portal_url(
        self, *, return_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        return_url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing_v1.init_stripe_customer_portal_url(
                return_url="returnUrl",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.init_stripe_customer_portal_url(
            return_url=return_url, request_options=request_options
        )
        return _response.data

    async def get_invoices(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Invoice]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Invoice]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing_v1.get_invoices()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_invoices(request_options=request_options)
        return _response.data
