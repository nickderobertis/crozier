

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.customer import Customer
from ..types.payment_instrument_response import PaymentInstrumentResponse
from ..types.personal_details import PersonalDetails
from .raw_client import AsyncRawCustomersClient, RawCustomersClient


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

    def create_customer(
        self,
        *,
        customer_id: str,
        personal_details: typing.Optional[PersonalDetails] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Customer:
        """
        Creates a new saved customer resource which you can later manipulate and save payment instruments to.

        Parameters
        ----------
        customer_id : str
            Unique identifier of the customer.

        personal_details : typing.Optional[PersonalDetails]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Customer
            Returns the customer resource.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customers.create_customer(
            customer_id="831ff8d4cd5958ab5670",
        )
        """
        _response = self._raw_client.create_customer(
            customer_id=customer_id, personal_details=personal_details, request_options=request_options
        )
        return _response.data

    def get_customer(self, customer_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Customer:
        """
        Retrieves an identified saved customer resource through the unique `customer_id` parameter, generated upon customer creation.

        Parameters
        ----------
        customer_id : str
            Unique identifier of the saved customer resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Customer
            Returns the customer resource.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customers.get_customer(
            customer_id="831ff8d4cd5958ab5670",
        )
        """
        _response = self._raw_client.get_customer(customer_id, request_options=request_options)
        return _response.data

    def update_customer(
        self,
        customer_id: str,
        *,
        personal_details: typing.Optional[PersonalDetails] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Customer:
        """
        Updates an identified saved customer resource's personal details.

        The request only overwrites the parameters included in the request, all other parameters will remain with their initially assigned values.

        Parameters
        ----------
        customer_id : str
            Unique identifier of the saved customer resource.

        personal_details : typing.Optional[PersonalDetails]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Customer
            Returns the customer resource.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customers.update_customer(
            customer_id="831ff8d4cd5958ab5670",
        )
        """
        _response = self._raw_client.update_customer(
            customer_id, personal_details=personal_details, request_options=request_options
        )
        return _response.data

    def list_payment_instruments(
        self, customer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PaymentInstrumentResponse]:
        """
        Lists all payment instrument resources that are saved for an identified customer.

        Parameters
        ----------
        customer_id : str
            Unique identifier of the saved customer resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PaymentInstrumentResponse]
            Returns the list of saved payment instruments for the customer.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customers.list_payment_instruments(
            customer_id="831ff8d4cd5958ab5670",
        )
        """
        _response = self._raw_client.list_payment_instruments(customer_id, request_options=request_options)
        return _response.data

    def deactivate_payment_instrument(
        self, customer_id: str, token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deactivates an identified card payment instrument resource for a customer.

        Parameters
        ----------
        customer_id : str
            Unique identifier of the saved customer resource.

        token : str
            Unique token identifying the card saved as a payment instrument resource.

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
        client.customers.deactivate_payment_instrument(
            customer_id="831ff8d4cd5958ab5670",
            token="bcfc8e5f-3b47-4cb9-854b-3b7a4cce7be3",
        )
        """
        _response = self._raw_client.deactivate_payment_instrument(customer_id, token, request_options=request_options)
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

    async def create_customer(
        self,
        *,
        customer_id: str,
        personal_details: typing.Optional[PersonalDetails] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Customer:
        """
        Creates a new saved customer resource which you can later manipulate and save payment instruments to.

        Parameters
        ----------
        customer_id : str
            Unique identifier of the customer.

        personal_details : typing.Optional[PersonalDetails]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Customer
            Returns the customer resource.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.create_customer(
                customer_id="831ff8d4cd5958ab5670",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_customer(
            customer_id=customer_id, personal_details=personal_details, request_options=request_options
        )
        return _response.data

    async def get_customer(
        self, customer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Customer:
        """
        Retrieves an identified saved customer resource through the unique `customer_id` parameter, generated upon customer creation.

        Parameters
        ----------
        customer_id : str
            Unique identifier of the saved customer resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Customer
            Returns the customer resource.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.get_customer(
                customer_id="831ff8d4cd5958ab5670",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_customer(customer_id, request_options=request_options)
        return _response.data

    async def update_customer(
        self,
        customer_id: str,
        *,
        personal_details: typing.Optional[PersonalDetails] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Customer:
        """
        Updates an identified saved customer resource's personal details.

        The request only overwrites the parameters included in the request, all other parameters will remain with their initially assigned values.

        Parameters
        ----------
        customer_id : str
            Unique identifier of the saved customer resource.

        personal_details : typing.Optional[PersonalDetails]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Customer
            Returns the customer resource.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.update_customer(
                customer_id="831ff8d4cd5958ab5670",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_customer(
            customer_id, personal_details=personal_details, request_options=request_options
        )
        return _response.data

    async def list_payment_instruments(
        self, customer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PaymentInstrumentResponse]:
        """
        Lists all payment instrument resources that are saved for an identified customer.

        Parameters
        ----------
        customer_id : str
            Unique identifier of the saved customer resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PaymentInstrumentResponse]
            Returns the list of saved payment instruments for the customer.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.list_payment_instruments(
                customer_id="831ff8d4cd5958ab5670",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_payment_instruments(customer_id, request_options=request_options)
        return _response.data

    async def deactivate_payment_instrument(
        self, customer_id: str, token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deactivates an identified card payment instrument resource for a customer.

        Parameters
        ----------
        customer_id : str
            Unique identifier of the saved customer resource.

        token : str
            Unique token identifying the card saved as a payment instrument resource.

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
            await client.customers.deactivate_payment_instrument(
                customer_id="831ff8d4cd5958ab5670",
                token="bcfc8e5f-3b47-4cb9-854b-3b7a4cce7be3",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deactivate_payment_instrument(
            customer_id, token, request_options=request_options
        )
        return _response.data
