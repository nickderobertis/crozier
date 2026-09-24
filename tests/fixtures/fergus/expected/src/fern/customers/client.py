

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address_payload import AddressPayload
from ..types.get_customer_by_id_response import GetCustomerByIdResponse
from ..types.get_customers_response import GetCustomersResponse
from ..types.person_payload import PersonPayload
from .raw_client import AsyncRawCustomersClient, RawCustomersClient
from .types.get_customers_request_sort_field import GetCustomersRequestSortField
from .types.get_customers_request_sort_order import GetCustomersRequestSortOrder


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

    def get_customers(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetCustomersRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetCustomersRequestSortField] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCustomersResponse:
        """
        Returns a list of customers. The list can be filtered by customer name.<br/><br/>
            A note about contact items on each person:<br>
            <ul>
              <li>The contact items are an array of objects. Each object has a `contactType` and a `contactValue`.
              <li>The `contactType` can be one of the following: email, phone, mobile, or fax.
              <li>The `contactValue` can be an email address or phone number.
            </ul>


        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetCustomersRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetCustomersRequestSortField]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `customerFullName`
            - `mainContact.firstName`
            - `mainContact.lastName`
            - `mainContact.contactItems[].contactValue`
            - `billingContact.firstName`
            - `billingContact.lastName`,
            - `billingContact.contactItems[].contactValue`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomersResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customers.get_customers()
        """
        _response = self._raw_client.get_customers(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            filter_search_text=filter_search_text,
            request_options=request_options,
        )
        return _response.data

    def post_customers(
        self,
        *,
        customer_full_name: str,
        main_contact: PersonPayload,
        physical_address: typing.Optional[AddressPayload] = OMIT,
        postal_address: typing.Optional[AddressPayload] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCustomerByIdResponse:
        """
        Creates a new customer.

        Parameters
        ----------
        customer_full_name : str

        main_contact : PersonPayload

        physical_address : typing.Optional[AddressPayload]

        postal_address : typing.Optional[AddressPayload]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomerByIdResponse
            Resource created successfully

        Examples
        --------
        from fern import FernApi, PersonPayload

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customers.post_customers(
            customer_full_name="customerFullName",
            main_contact=PersonPayload(
                first_name="firstName",
            ),
        )
        """
        _response = self._raw_client.post_customers(
            customer_full_name=customer_full_name,
            main_contact=main_contact,
            physical_address=physical_address,
            postal_address=postal_address,
            request_options=request_options,
        )
        return _response.data

    def get_customers_customer_id(
        self, customer_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCustomerByIdResponse:
        """
        Returns a customer by ID.

        Parameters
        ----------
        customer_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomerByIdResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customers.get_customers_customer_id(
            customer_id=1.1,
        )
        """
        _response = self._raw_client.get_customers_customer_id(customer_id, request_options=request_options)
        return _response.data

    def put_customers_customer_id(
        self,
        customer_id: float,
        *,
        customer_full_name: str,
        main_contact: PersonPayload,
        physical_address: typing.Optional[AddressPayload] = OMIT,
        postal_address: typing.Optional[AddressPayload] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCustomerByIdResponse:
        """
        Update a customer.

        Parameters
        ----------
        customer_id : float

        customer_full_name : str

        main_contact : PersonPayload

        physical_address : typing.Optional[AddressPayload]

        postal_address : typing.Optional[AddressPayload]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomerByIdResponse
            Successful Response

        Examples
        --------
        from fern import FernApi, PersonPayload

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customers.put_customers_customer_id(
            customer_id=1.1,
            customer_full_name="customerFullName",
            main_contact=PersonPayload(
                first_name="firstName",
            ),
        )
        """
        _response = self._raw_client.put_customers_customer_id(
            customer_id,
            customer_full_name=customer_full_name,
            main_contact=main_contact,
            physical_address=physical_address,
            postal_address=postal_address,
            request_options=request_options,
        )
        return _response.data

    def delete_customers_customer_id(
        self, customer_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a customer by ID.

        Parameters
        ----------
        customer_id : float

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
        client.customers.delete_customers_customer_id(
            customer_id=1.1,
        )
        """
        _response = self._raw_client.delete_customers_customer_id(customer_id, request_options=request_options)
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

    async def get_customers(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetCustomersRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetCustomersRequestSortField] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCustomersResponse:
        """
        Returns a list of customers. The list can be filtered by customer name.<br/><br/>
            A note about contact items on each person:<br>
            <ul>
              <li>The contact items are an array of objects. Each object has a `contactType` and a `contactValue`.
              <li>The `contactType` can be one of the following: email, phone, mobile, or fax.
              <li>The `contactValue` can be an email address or phone number.
            </ul>


        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetCustomersRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetCustomersRequestSortField]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `customerFullName`
            - `mainContact.firstName`
            - `mainContact.lastName`
            - `mainContact.contactItems[].contactValue`
            - `billingContact.firstName`
            - `billingContact.lastName`,
            - `billingContact.contactItems[].contactValue`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomersResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.get_customers()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_customers(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            filter_search_text=filter_search_text,
            request_options=request_options,
        )
        return _response.data

    async def post_customers(
        self,
        *,
        customer_full_name: str,
        main_contact: PersonPayload,
        physical_address: typing.Optional[AddressPayload] = OMIT,
        postal_address: typing.Optional[AddressPayload] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCustomerByIdResponse:
        """
        Creates a new customer.

        Parameters
        ----------
        customer_full_name : str

        main_contact : PersonPayload

        physical_address : typing.Optional[AddressPayload]

        postal_address : typing.Optional[AddressPayload]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomerByIdResponse
            Resource created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PersonPayload

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.post_customers(
                customer_full_name="customerFullName",
                main_contact=PersonPayload(
                    first_name="firstName",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_customers(
            customer_full_name=customer_full_name,
            main_contact=main_contact,
            physical_address=physical_address,
            postal_address=postal_address,
            request_options=request_options,
        )
        return _response.data

    async def get_customers_customer_id(
        self, customer_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCustomerByIdResponse:
        """
        Returns a customer by ID.

        Parameters
        ----------
        customer_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomerByIdResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.get_customers_customer_id(
                customer_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_customers_customer_id(customer_id, request_options=request_options)
        return _response.data

    async def put_customers_customer_id(
        self,
        customer_id: float,
        *,
        customer_full_name: str,
        main_contact: PersonPayload,
        physical_address: typing.Optional[AddressPayload] = OMIT,
        postal_address: typing.Optional[AddressPayload] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCustomerByIdResponse:
        """
        Update a customer.

        Parameters
        ----------
        customer_id : float

        customer_full_name : str

        main_contact : PersonPayload

        physical_address : typing.Optional[AddressPayload]

        postal_address : typing.Optional[AddressPayload]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomerByIdResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PersonPayload

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.put_customers_customer_id(
                customer_id=1.1,
                customer_full_name="customerFullName",
                main_contact=PersonPayload(
                    first_name="firstName",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_customers_customer_id(
            customer_id,
            customer_full_name=customer_full_name,
            main_contact=main_contact,
            physical_address=physical_address,
            postal_address=postal_address,
            request_options=request_options,
        )
        return _response.data

    async def delete_customers_customer_id(
        self, customer_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a customer by ID.

        Parameters
        ----------
        customer_id : float

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
            await client.customers.delete_customers_customer_id(
                customer_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_customers_customer_id(customer_id, request_options=request_options)
        return _response.data
