

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCustomersClient, RawCustomersClient
from .types.get_customer_response import GetCustomerResponse


OMIT = typing.cast(typing.Any, ...)


class CustomersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCustomersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCustomersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCustomersClient
        """
        return self._raw_client

    def get_customer(
        self, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCustomerResponse:
        """
        Look up a customer by email to load their details, including purchases and subscriptions.

        Parameters
        ----------
        email : str
            Customer email address

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomerResponse
            Customer details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customers.get_customer(
            email="email",
        )
        """
        _response = self._raw_client.get_customer(email=email, request_options=request_options)
        return _response.data


class AsyncCustomersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCustomersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCustomersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCustomersClient
        """
        return self._raw_client

    async def get_customer(
        self, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCustomerResponse:
        """
        Look up a customer by email to load their details, including purchases and subscriptions.

        Parameters
        ----------
        email : str
            Customer email address

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomerResponse
            Customer details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.get_customer(
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_customer(email=email, request_options=request_options)
        return _response.data
