

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPaymentMethodsClient, RawPaymentMethodsClient


class PaymentMethodsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPaymentMethodsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPaymentMethodsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPaymentMethodsClient
        """
        return self._raw_client

    def get_list_of_payment_methods(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get list of payment methods

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
        client.payment_methods.get_list_of_payment_methods()
        """
        _response = self._raw_client.get_list_of_payment_methods(request_options=request_options)
        return _response.data


class AsyncPaymentMethodsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPaymentMethodsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPaymentMethodsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPaymentMethodsClient
        """
        return self._raw_client

    async def get_list_of_payment_methods(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get list of payment methods

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
            await client.payment_methods.get_list_of_payment_methods()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_list_of_payment_methods(request_options=request_options)
        return _response.data
