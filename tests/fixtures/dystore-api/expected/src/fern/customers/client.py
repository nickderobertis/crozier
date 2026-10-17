

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCustomersClient, RawCustomersClient
from .types.update_customer_request_data import UpdateCustomerRequestData


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

    def get_customer(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get customer

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
        client.customers.get_customer()
        """
        _response = self._raw_client.get_customer(request_options=request_options)
        return _response.data

    def update_customer(
        self,
        *,
        data: typing.Optional[UpdateCustomerRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update customer

        Parameters
        ----------
        data : typing.Optional[UpdateCustomerRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.customers import (
            UpdateCustomerRequestData,
            UpdateCustomerRequestDataAttributes,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customers.update_customer(
            data=UpdateCustomerRequestData(
                attributes=UpdateCustomerRequestDataAttributes(
                    account_ref="987654321",
                    company_name="Not Evil",
                    first_name="Jane",
                    last_name="Doe",
                    vat_no="1234567899",
                ),
                id="1",
                type="customers",
            ),
        )
        """
        _response = self._raw_client.update_customer(data=data, request_options=request_options)
        return _response.data

    def list_customer_addresses(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List customer addresses

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
        client.customers.list_customer_addresses()
        """
        _response = self._raw_client.list_customer_addresses(request_options=request_options)
        return _response.data

    def list_customer_addresses_relationships(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List customer addresses relationships

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
        client.customers.list_customer_addresses_relationships()
        """
        _response = self._raw_client.list_customer_addresses_relationships(request_options=request_options)
        return _response.data

    def list_customer_orders(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List customer orders

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
        client.customers.list_customer_orders()
        """
        _response = self._raw_client.list_customer_orders(request_options=request_options)
        return _response.data

    def list_customer_orders_relationships(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List customer orders relationships

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
        client.customers.list_customer_orders_relationships()
        """
        _response = self._raw_client.list_customer_orders_relationships(request_options=request_options)
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

    async def get_customer(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get customer

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
            await client.customers.get_customer()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_customer(request_options=request_options)
        return _response.data

    async def update_customer(
        self,
        *,
        data: typing.Optional[UpdateCustomerRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update customer

        Parameters
        ----------
        data : typing.Optional[UpdateCustomerRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.customers import (
            UpdateCustomerRequestData,
            UpdateCustomerRequestDataAttributes,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.update_customer(
                data=UpdateCustomerRequestData(
                    attributes=UpdateCustomerRequestDataAttributes(
                        account_ref="987654321",
                        company_name="Not Evil",
                        first_name="Jane",
                        last_name="Doe",
                        vat_no="1234567899",
                    ),
                    id="1",
                    type="customers",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_customer(data=data, request_options=request_options)
        return _response.data

    async def list_customer_addresses(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List customer addresses

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
            await client.customers.list_customer_addresses()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_customer_addresses(request_options=request_options)
        return _response.data

    async def list_customer_addresses_relationships(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List customer addresses relationships

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
            await client.customers.list_customer_addresses_relationships()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_customer_addresses_relationships(request_options=request_options)
        return _response.data

    async def list_customer_orders(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List customer orders

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
            await client.customers.list_customer_orders()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_customer_orders(request_options=request_options)
        return _response.data

    async def list_customer_orders_relationships(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List customer orders relationships

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
            await client.customers.list_customer_orders_relationships()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_customer_orders_relationships(request_options=request_options)
        return _response.data
