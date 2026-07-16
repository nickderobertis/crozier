

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.add_group_to_customer_response import AddGroupToCustomerResponse
from ..types.address import Address
from ..types.create_customer_card_response import CreateCustomerCardResponse
from ..types.create_customer_response import CreateCustomerResponse
from ..types.customer_query import CustomerQuery
from ..types.delete_customer_card_response import DeleteCustomerCardResponse
from ..types.delete_customer_response import DeleteCustomerResponse
from ..types.list_customers_response import ListCustomersResponse
from ..types.remove_group_from_customer_response import RemoveGroupFromCustomerResponse
from ..types.retrieve_customer_response import RetrieveCustomerResponse
from ..types.search_customers_response import SearchCustomersResponse
from ..types.update_customer_response import UpdateCustomerResponse
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

    def list_customers(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sort_field: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCustomersResponse:
        """
        Lists customer profiles associated with a Square account.

        Under normal operating conditions, newly created or updated customer profiles become available
        for the listing operation in well under 30 seconds. Occasionally, propagation of the new or updated
        profiles can take closer to one minute or longer, especially during network incidents and outages.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for your original query.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        limit : typing.Optional[int]
            The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.
            The limit is ignored if it is less than 1 or greater than 100. The default value is 100.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        sort_field : typing.Optional[str]
            Indicates how customers should be sorted.

            The default value is `DEFAULT`.

        sort_order : typing.Optional[str]
            Indicates whether customers should be sorted in ascending (`ASC`) or
            descending (`DESC`) order.

            The default value is `ASC`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCustomersResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.customers.list_customers()
        """
        _response = self._raw_client.list_customers(
            cursor=cursor, limit=limit, sort_field=sort_field, sort_order=sort_order, request_options=request_options
        )
        return _response.data

    def create_customer(
        self,
        *,
        address: typing.Optional[Address] = OMIT,
        birthday: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        email_address: typing.Optional[str] = OMIT,
        family_name: typing.Optional[str] = OMIT,
        given_name: typing.Optional[str] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        nickname: typing.Optional[str] = OMIT,
        note: typing.Optional[str] = OMIT,
        phone_number: typing.Optional[str] = OMIT,
        reference_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCustomerResponse:
        """
        Creates a new customer for a business.

        You must provide at least one of the following values in your request to this
        endpoint:

        - `given_name`
        - `family_name`
        - `company_name`
        - `email_address`
        - `phone_number`

        Parameters
        ----------
        address : typing.Optional[Address]

        birthday : typing.Optional[str]
            The birthday associated with the customer profile, in RFC 3339 format. The year is optional. The timezone and time are not allowed.
            For example, `0000-09-21T00:00:00-00:00` represents a birthday on September 21 and `1998-09-21T00:00:00-00:00` represents a birthday on September 21, 1998.
            You can also specify this value in `YYYY-MM-DD` format.

        company_name : typing.Optional[str]
            A business name associated with the customer profile.

        email_address : typing.Optional[str]
            The email address associated with the customer profile.

        family_name : typing.Optional[str]
            The family name (that is, the last name) associated with the customer profile.

        given_name : typing.Optional[str]
            The given name (that is, the first name) associated with the customer profile.

        idempotency_key : typing.Optional[str]
            The idempotency key for the request.    For more information, see
            [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        nickname : typing.Optional[str]
            A nickname for the customer profile.

        note : typing.Optional[str]
            A custom note associated with the customer profile.

        phone_number : typing.Optional[str]
            The 11-digit phone number associated with the customer profile.

        reference_id : typing.Optional[str]
            An optional second ID used to associate the customer profile with an
            entity in another system.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCustomerResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.customers.create_customer()
        """
        _response = self._raw_client.create_customer(
            address=address,
            birthday=birthday,
            company_name=company_name,
            email_address=email_address,
            family_name=family_name,
            given_name=given_name,
            idempotency_key=idempotency_key,
            nickname=nickname,
            note=note,
            phone_number=phone_number,
            reference_id=reference_id,
            request_options=request_options,
        )
        return _response.data

    def search_customers(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[CustomerQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchCustomersResponse:
        """
        Searches the customer profiles associated with a Square account using a supported query filter.

        Calling `SearchCustomers` without any explicit query filter returns all
        customer profiles ordered alphabetically based on `given_name` and
        `family_name`.

        Under normal operating conditions, newly created or updated customer profiles become available
        for the search operation in well under 30 seconds. Occasionally, propagation of the new or updated
        profiles can take closer to one minute or longer, especially during network incidents and outages.

        Parameters
        ----------
        cursor : typing.Optional[str]
            Include the pagination cursor in subsequent calls to this endpoint to retrieve
            the next set of results associated with the original query.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        limit : typing.Optional[int]
            The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.
            The limit is ignored if it is less than the minimum or greater than the maximum value. The default value is 100.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        query : typing.Optional[CustomerQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchCustomersResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.customers.search_customers()
        """
        _response = self._raw_client.search_customers(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    def retrieve_customer(
        self, customer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveCustomerResponse:
        """
        Returns details for a single customer.

        Parameters
        ----------
        customer_id : str
            The ID of the customer to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveCustomerResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.customers.retrieve_customer(
            customer_id="customer_id",
        )
        """
        _response = self._raw_client.retrieve_customer(customer_id, request_options=request_options)
        return _response.data

    def update_customer(
        self,
        customer_id: str,
        *,
        address: typing.Optional[Address] = OMIT,
        birthday: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        email_address: typing.Optional[str] = OMIT,
        family_name: typing.Optional[str] = OMIT,
        given_name: typing.Optional[str] = OMIT,
        nickname: typing.Optional[str] = OMIT,
        note: typing.Optional[str] = OMIT,
        phone_number: typing.Optional[str] = OMIT,
        reference_id: typing.Optional[str] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateCustomerResponse:
        """
        Updates a customer profile. To change an attribute, specify the new value. To remove an attribute, specify the value as an empty string or empty object.

        As a best practice, you should include the `version` field in the request to enable [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency) control. The value must be set to the current version of the customer profile.

        To update a customer profile that was created by merging existing profiles, you must use the ID of the newly created profile.

        You cannot use this endpoint to change cards on file. To make changes, use the [Cards API](https://developer.squareup.com/reference/square_2021-08-18/cards-api) or [Gift Cards API](https://developer.squareup.com/reference/square_2021-08-18/gift-cards-api).

        Parameters
        ----------
        customer_id : str
            The ID of the customer to update.

        address : typing.Optional[Address]

        birthday : typing.Optional[str]
            The birthday associated with the customer profile, in RFC 3339 format. The year is optional. The timezone and time are not allowed.
            For example, `0000-09-21T00:00:00-00:00` represents a birthday on September 21 and `1998-09-21T00:00:00-00:00` represents a birthday on September 21, 1998.
            You can also specify this value in `YYYY-MM-DD` format.

        company_name : typing.Optional[str]
            A business name associated with the customer profile.

        email_address : typing.Optional[str]
            The email address associated with the customer profile.

        family_name : typing.Optional[str]
            The family name (that is, the last name) associated with the customer profile.

        given_name : typing.Optional[str]
            The given name (that is, the first name) associated with the customer profile.

        nickname : typing.Optional[str]
            A nickname for the customer profile.

        note : typing.Optional[str]
            A custom note associated with the customer profile.

        phone_number : typing.Optional[str]
            The 11-digit phone number associated with the customer profile.

        reference_id : typing.Optional[str]
            An optional second ID used to associate the customer profile with an
            entity in another system.

        version : typing.Optional[int]
            The current version of the customer profile.

            As a best practice, you should include this field to enable [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency) control. For more information, see [Update a customer profile](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#update-a-customer-profile).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCustomerResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.customers.update_customer(
            customer_id="customer_id",
        )
        """
        _response = self._raw_client.update_customer(
            customer_id,
            address=address,
            birthday=birthday,
            company_name=company_name,
            email_address=email_address,
            family_name=family_name,
            given_name=given_name,
            nickname=nickname,
            note=note,
            phone_number=phone_number,
            reference_id=reference_id,
            version=version,
            request_options=request_options,
        )
        return _response.data

    def delete_customer(
        self,
        customer_id: str,
        *,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteCustomerResponse:
        """
        Deletes a customer profile from a business. This operation also unlinks any associated cards on file.

        As a best practice, you should include the `version` field in the request to enable [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency) control. The value must be set to the current version of the customer profile.

        To delete a customer profile that was created by merging existing profiles, you must use the ID of the newly created profile.

        Parameters
        ----------
        customer_id : str
            The ID of the customer to delete.

        version : typing.Optional[int]
            The current version of the customer profile.

            As a best practice, you should include this parameter to enable [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency) control.  For more information, see [Delete a customer profile](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#delete-customer-profile).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteCustomerResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.customers.delete_customer(
            customer_id="customer_id",
        )
        """
        _response = self._raw_client.delete_customer(customer_id, version=version, request_options=request_options)
        return _response.data

    def create_customer_card(
        self,
        customer_id: str,
        *,
        card_nonce: str,
        billing_address: typing.Optional[Address] = OMIT,
        cardholder_name: typing.Optional[str] = OMIT,
        verification_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCustomerCardResponse:
        """
        Adds a card on file to an existing customer.

        As with charges, calls to `CreateCustomerCard` are idempotent. Multiple
        calls with the same card nonce return the same card record that was created
        with the provided nonce during the _first_ call.

        Parameters
        ----------
        customer_id : str
            The Square ID of the customer profile the card is linked to.

        card_nonce : str
            A card nonce representing the credit card to link to the customer.

            Card nonces are generated by the Square payment form when customers enter
            their card information. For more information, see
            [Walkthrough: Integrate Square Payments in a Website](https://developer.squareup.com/docs/web-payments/take-card-payment).

            __NOTE:__ Card nonces generated by digital wallets (such as Apple Pay)
            cannot be used to create a customer card.

        billing_address : typing.Optional[Address]

        cardholder_name : typing.Optional[str]
            The full name printed on the credit card.

        verification_token : typing.Optional[str]
            An identifying token generated by [Payments.verifyBuyer()](https://developer.squareup.com/reference/sdks/web/payments/objects/Payments#Payments.verifyBuyer).
            Verification tokens encapsulate customer device information and 3-D Secure
            challenge results to indicate that Square has verified the buyer identity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCustomerCardResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.customers.create_customer_card(
            customer_id="customer_id",
            card_nonce="card_nonce",
        )
        """
        _response = self._raw_client.create_customer_card(
            customer_id,
            card_nonce=card_nonce,
            billing_address=billing_address,
            cardholder_name=cardholder_name,
            verification_token=verification_token,
            request_options=request_options,
        )
        return _response.data

    def delete_customer_card(
        self, customer_id: str, card_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteCustomerCardResponse:
        """
        Removes a card on file from a customer.

        Parameters
        ----------
        customer_id : str
            The ID of the customer that the card on file belongs to.

        card_id : str
            The ID of the card on file to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteCustomerCardResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.customers.delete_customer_card(
            customer_id="customer_id",
            card_id="card_id",
        )
        """
        _response = self._raw_client.delete_customer_card(customer_id, card_id, request_options=request_options)
        return _response.data

    def add_group_to_customer(
        self, customer_id: str, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AddGroupToCustomerResponse:
        """
        Adds a group membership to a customer.

        The customer is identified by the `customer_id` value
        and the customer group is identified by the `group_id` value.

        Parameters
        ----------
        customer_id : str
            The ID of the customer to add to a group.

        group_id : str
            The ID of the customer group to add the customer to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddGroupToCustomerResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.customers.add_group_to_customer(
            customer_id="customer_id",
            group_id="group_id",
        )
        """
        _response = self._raw_client.add_group_to_customer(customer_id, group_id, request_options=request_options)
        return _response.data

    def remove_group_from_customer(
        self, customer_id: str, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RemoveGroupFromCustomerResponse:
        """
        Removes a group membership from a customer.

        The customer is identified by the `customer_id` value
        and the customer group is identified by the `group_id` value.

        Parameters
        ----------
        customer_id : str
            The ID of the customer to remove from the group.

        group_id : str
            The ID of the customer group to remove the customer from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoveGroupFromCustomerResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.customers.remove_group_from_customer(
            customer_id="customer_id",
            group_id="group_id",
        )
        """
        _response = self._raw_client.remove_group_from_customer(customer_id, group_id, request_options=request_options)
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

    async def list_customers(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sort_field: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCustomersResponse:
        """
        Lists customer profiles associated with a Square account.

        Under normal operating conditions, newly created or updated customer profiles become available
        for the listing operation in well under 30 seconds. Occasionally, propagation of the new or updated
        profiles can take closer to one minute or longer, especially during network incidents and outages.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for your original query.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        limit : typing.Optional[int]
            The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.
            The limit is ignored if it is less than 1 or greater than 100. The default value is 100.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        sort_field : typing.Optional[str]
            Indicates how customers should be sorted.

            The default value is `DEFAULT`.

        sort_order : typing.Optional[str]
            Indicates whether customers should be sorted in ascending (`ASC`) or
            descending (`DESC`) order.

            The default value is `ASC`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCustomersResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.list_customers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_customers(
            cursor=cursor, limit=limit, sort_field=sort_field, sort_order=sort_order, request_options=request_options
        )
        return _response.data

    async def create_customer(
        self,
        *,
        address: typing.Optional[Address] = OMIT,
        birthday: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        email_address: typing.Optional[str] = OMIT,
        family_name: typing.Optional[str] = OMIT,
        given_name: typing.Optional[str] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        nickname: typing.Optional[str] = OMIT,
        note: typing.Optional[str] = OMIT,
        phone_number: typing.Optional[str] = OMIT,
        reference_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCustomerResponse:
        """
        Creates a new customer for a business.

        You must provide at least one of the following values in your request to this
        endpoint:

        - `given_name`
        - `family_name`
        - `company_name`
        - `email_address`
        - `phone_number`

        Parameters
        ----------
        address : typing.Optional[Address]

        birthday : typing.Optional[str]
            The birthday associated with the customer profile, in RFC 3339 format. The year is optional. The timezone and time are not allowed.
            For example, `0000-09-21T00:00:00-00:00` represents a birthday on September 21 and `1998-09-21T00:00:00-00:00` represents a birthday on September 21, 1998.
            You can also specify this value in `YYYY-MM-DD` format.

        company_name : typing.Optional[str]
            A business name associated with the customer profile.

        email_address : typing.Optional[str]
            The email address associated with the customer profile.

        family_name : typing.Optional[str]
            The family name (that is, the last name) associated with the customer profile.

        given_name : typing.Optional[str]
            The given name (that is, the first name) associated with the customer profile.

        idempotency_key : typing.Optional[str]
            The idempotency key for the request.    For more information, see
            [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        nickname : typing.Optional[str]
            A nickname for the customer profile.

        note : typing.Optional[str]
            A custom note associated with the customer profile.

        phone_number : typing.Optional[str]
            The 11-digit phone number associated with the customer profile.

        reference_id : typing.Optional[str]
            An optional second ID used to associate the customer profile with an
            entity in another system.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCustomerResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.create_customer()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_customer(
            address=address,
            birthday=birthday,
            company_name=company_name,
            email_address=email_address,
            family_name=family_name,
            given_name=given_name,
            idempotency_key=idempotency_key,
            nickname=nickname,
            note=note,
            phone_number=phone_number,
            reference_id=reference_id,
            request_options=request_options,
        )
        return _response.data

    async def search_customers(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[CustomerQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchCustomersResponse:
        """
        Searches the customer profiles associated with a Square account using a supported query filter.

        Calling `SearchCustomers` without any explicit query filter returns all
        customer profiles ordered alphabetically based on `given_name` and
        `family_name`.

        Under normal operating conditions, newly created or updated customer profiles become available
        for the search operation in well under 30 seconds. Occasionally, propagation of the new or updated
        profiles can take closer to one minute or longer, especially during network incidents and outages.

        Parameters
        ----------
        cursor : typing.Optional[str]
            Include the pagination cursor in subsequent calls to this endpoint to retrieve
            the next set of results associated with the original query.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        limit : typing.Optional[int]
            The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.
            The limit is ignored if it is less than the minimum or greater than the maximum value. The default value is 100.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        query : typing.Optional[CustomerQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchCustomersResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.search_customers()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_customers(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    async def retrieve_customer(
        self, customer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveCustomerResponse:
        """
        Returns details for a single customer.

        Parameters
        ----------
        customer_id : str
            The ID of the customer to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveCustomerResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.retrieve_customer(
                customer_id="customer_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_customer(customer_id, request_options=request_options)
        return _response.data

    async def update_customer(
        self,
        customer_id: str,
        *,
        address: typing.Optional[Address] = OMIT,
        birthday: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        email_address: typing.Optional[str] = OMIT,
        family_name: typing.Optional[str] = OMIT,
        given_name: typing.Optional[str] = OMIT,
        nickname: typing.Optional[str] = OMIT,
        note: typing.Optional[str] = OMIT,
        phone_number: typing.Optional[str] = OMIT,
        reference_id: typing.Optional[str] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateCustomerResponse:
        """
        Updates a customer profile. To change an attribute, specify the new value. To remove an attribute, specify the value as an empty string or empty object.

        As a best practice, you should include the `version` field in the request to enable [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency) control. The value must be set to the current version of the customer profile.

        To update a customer profile that was created by merging existing profiles, you must use the ID of the newly created profile.

        You cannot use this endpoint to change cards on file. To make changes, use the [Cards API](https://developer.squareup.com/reference/square_2021-08-18/cards-api) or [Gift Cards API](https://developer.squareup.com/reference/square_2021-08-18/gift-cards-api).

        Parameters
        ----------
        customer_id : str
            The ID of the customer to update.

        address : typing.Optional[Address]

        birthday : typing.Optional[str]
            The birthday associated with the customer profile, in RFC 3339 format. The year is optional. The timezone and time are not allowed.
            For example, `0000-09-21T00:00:00-00:00` represents a birthday on September 21 and `1998-09-21T00:00:00-00:00` represents a birthday on September 21, 1998.
            You can also specify this value in `YYYY-MM-DD` format.

        company_name : typing.Optional[str]
            A business name associated with the customer profile.

        email_address : typing.Optional[str]
            The email address associated with the customer profile.

        family_name : typing.Optional[str]
            The family name (that is, the last name) associated with the customer profile.

        given_name : typing.Optional[str]
            The given name (that is, the first name) associated with the customer profile.

        nickname : typing.Optional[str]
            A nickname for the customer profile.

        note : typing.Optional[str]
            A custom note associated with the customer profile.

        phone_number : typing.Optional[str]
            The 11-digit phone number associated with the customer profile.

        reference_id : typing.Optional[str]
            An optional second ID used to associate the customer profile with an
            entity in another system.

        version : typing.Optional[int]
            The current version of the customer profile.

            As a best practice, you should include this field to enable [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency) control. For more information, see [Update a customer profile](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#update-a-customer-profile).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCustomerResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.update_customer(
                customer_id="customer_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_customer(
            customer_id,
            address=address,
            birthday=birthday,
            company_name=company_name,
            email_address=email_address,
            family_name=family_name,
            given_name=given_name,
            nickname=nickname,
            note=note,
            phone_number=phone_number,
            reference_id=reference_id,
            version=version,
            request_options=request_options,
        )
        return _response.data

    async def delete_customer(
        self,
        customer_id: str,
        *,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteCustomerResponse:
        """
        Deletes a customer profile from a business. This operation also unlinks any associated cards on file.

        As a best practice, you should include the `version` field in the request to enable [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency) control. The value must be set to the current version of the customer profile.

        To delete a customer profile that was created by merging existing profiles, you must use the ID of the newly created profile.

        Parameters
        ----------
        customer_id : str
            The ID of the customer to delete.

        version : typing.Optional[int]
            The current version of the customer profile.

            As a best practice, you should include this parameter to enable [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency) control.  For more information, see [Delete a customer profile](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#delete-customer-profile).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteCustomerResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.delete_customer(
                customer_id="customer_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_customer(
            customer_id, version=version, request_options=request_options
        )
        return _response.data

    async def create_customer_card(
        self,
        customer_id: str,
        *,
        card_nonce: str,
        billing_address: typing.Optional[Address] = OMIT,
        cardholder_name: typing.Optional[str] = OMIT,
        verification_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCustomerCardResponse:
        """
        Adds a card on file to an existing customer.

        As with charges, calls to `CreateCustomerCard` are idempotent. Multiple
        calls with the same card nonce return the same card record that was created
        with the provided nonce during the _first_ call.

        Parameters
        ----------
        customer_id : str
            The Square ID of the customer profile the card is linked to.

        card_nonce : str
            A card nonce representing the credit card to link to the customer.

            Card nonces are generated by the Square payment form when customers enter
            their card information. For more information, see
            [Walkthrough: Integrate Square Payments in a Website](https://developer.squareup.com/docs/web-payments/take-card-payment).

            __NOTE:__ Card nonces generated by digital wallets (such as Apple Pay)
            cannot be used to create a customer card.

        billing_address : typing.Optional[Address]

        cardholder_name : typing.Optional[str]
            The full name printed on the credit card.

        verification_token : typing.Optional[str]
            An identifying token generated by [Payments.verifyBuyer()](https://developer.squareup.com/reference/sdks/web/payments/objects/Payments#Payments.verifyBuyer).
            Verification tokens encapsulate customer device information and 3-D Secure
            challenge results to indicate that Square has verified the buyer identity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCustomerCardResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.create_customer_card(
                customer_id="customer_id",
                card_nonce="card_nonce",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_customer_card(
            customer_id,
            card_nonce=card_nonce,
            billing_address=billing_address,
            cardholder_name=cardholder_name,
            verification_token=verification_token,
            request_options=request_options,
        )
        return _response.data

    async def delete_customer_card(
        self, customer_id: str, card_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteCustomerCardResponse:
        """
        Removes a card on file from a customer.

        Parameters
        ----------
        customer_id : str
            The ID of the customer that the card on file belongs to.

        card_id : str
            The ID of the card on file to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteCustomerCardResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.delete_customer_card(
                customer_id="customer_id",
                card_id="card_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_customer_card(customer_id, card_id, request_options=request_options)
        return _response.data

    async def add_group_to_customer(
        self, customer_id: str, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AddGroupToCustomerResponse:
        """
        Adds a group membership to a customer.

        The customer is identified by the `customer_id` value
        and the customer group is identified by the `group_id` value.

        Parameters
        ----------
        customer_id : str
            The ID of the customer to add to a group.

        group_id : str
            The ID of the customer group to add the customer to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddGroupToCustomerResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.add_group_to_customer(
                customer_id="customer_id",
                group_id="group_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_group_to_customer(customer_id, group_id, request_options=request_options)
        return _response.data

    async def remove_group_from_customer(
        self, customer_id: str, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RemoveGroupFromCustomerResponse:
        """
        Removes a group membership from a customer.

        The customer is identified by the `customer_id` value
        and the customer group is identified by the `group_id` value.

        Parameters
        ----------
        customer_id : str
            The ID of the customer to remove from the group.

        group_id : str
            The ID of the customer group to remove the customer from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoveGroupFromCustomerResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customers.remove_group_from_customer(
                customer_id="customer_id",
                group_id="group_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_group_from_customer(
            customer_id, group_id, request_options=request_options
        )
        return _response.data
