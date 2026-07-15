

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
from ..types.bank_account import BankAccount
from ..types.company_name import CompanyName
from ..types.create_customer_support_customer_response import CreateCustomerSupportCustomerResponse
from ..types.currency import Currency
from ..types.customer_support_customer_status import CustomerSupportCustomerStatus
from ..types.delete_customer_support_customer_response import DeleteCustomerSupportCustomerResponse
from ..types.email import Email
from ..types.first_name import FirstName
from ..types.get_customer_support_customer_response import GetCustomerSupportCustomerResponse
from ..types.get_customer_support_customers_response import GetCustomerSupportCustomersResponse
from ..types.last_name import LastName
from ..types.phone_number import PhoneNumber
from ..types.update_customer_support_customer_response import UpdateCustomerSupportCustomerResponse
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

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCustomerSupportCustomersResponse:
        """
        List Customer Support Customers

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomerSupportCustomersResponse
            CustomerSupportCustomers

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.customers.all_(
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.all_(
            raw=raw, cursor=cursor, limit=limit, fields=fields, request_options=request_options
        )
        return _response.data

    def add(
        self,
        *,
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        bank_accounts: typing.Optional[BankAccount] = OMIT,
        company_name: typing.Optional[CompanyName] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[str] = OMIT,
        individual: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        notes: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        status: typing.Optional[CustomerSupportCustomerStatus] = OMIT,
        tax_number: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCustomerSupportCustomerResponse:
        """
        Create Customer Support Customer

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        bank_accounts : typing.Optional[BankAccount]

        company_name : typing.Optional[CompanyName]

        created_at : typing.Optional[dt.datetime]
            The date and time when the object was created.

        created_by : typing.Optional[str]
            The user who created the object.

        currency : typing.Optional[Currency]

        emails : typing.Optional[typing.Sequence[Email]]

        first_name : typing.Optional[FirstName]

        id : typing.Optional[str]
            A unique identifier for an object.

        individual : typing.Optional[bool]

        last_name : typing.Optional[LastName]

        notes : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        status : typing.Optional[CustomerSupportCustomerStatus]
            Customer status

        tax_number : typing.Optional[str]

        updated_at : typing.Optional[dt.datetime]
            The date and time when the object was last updated.

        updated_by : typing.Optional[str]
            The user who last updated the object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCustomerSupportCustomerResponse
            CustomerSupportCustomers

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.customers.add()
        """
        _response = self._raw_client.add(
            raw=raw,
            addresses=addresses,
            bank_accounts=bank_accounts,
            company_name=company_name,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            emails=emails,
            first_name=first_name,
            id=id,
            individual=individual,
            last_name=last_name,
            notes=notes,
            phone_numbers=phone_numbers,
            status=status,
            tax_number=tax_number,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCustomerSupportCustomerResponse:
        """
        Get Customer Support Customer

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomerSupportCustomerResponse
            CustomerSupportCustomers

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.customers.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteCustomerSupportCustomerResponse:
        """
        Delete Customer Support Customer

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteCustomerSupportCustomerResponse
            CustomerSupportCustomers

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.customers.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    def update(
        self,
        id_: str,
        *,
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        bank_accounts: typing.Optional[BankAccount] = OMIT,
        company_name: typing.Optional[CompanyName] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[str] = OMIT,
        individual: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        notes: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        status: typing.Optional[CustomerSupportCustomerStatus] = OMIT,
        tax_number: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateCustomerSupportCustomerResponse:
        """
        Update Customer Support Customer

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        bank_accounts : typing.Optional[BankAccount]

        company_name : typing.Optional[CompanyName]

        created_at : typing.Optional[dt.datetime]
            The date and time when the object was created.

        created_by : typing.Optional[str]
            The user who created the object.

        currency : typing.Optional[Currency]

        emails : typing.Optional[typing.Sequence[Email]]

        first_name : typing.Optional[FirstName]

        id : typing.Optional[str]
            A unique identifier for an object.

        individual : typing.Optional[bool]

        last_name : typing.Optional[LastName]

        notes : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        status : typing.Optional[CustomerSupportCustomerStatus]
            Customer status

        tax_number : typing.Optional[str]

        updated_at : typing.Optional[dt.datetime]
            The date and time when the object was last updated.

        updated_by : typing.Optional[str]
            The user who last updated the object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCustomerSupportCustomerResponse
            CustomerSupportCustomers

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.customers.update(
            id_="id",
        )
        """
        _response = self._raw_client.update(
            id_,
            raw=raw,
            addresses=addresses,
            bank_accounts=bank_accounts,
            company_name=company_name,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            emails=emails,
            first_name=first_name,
            id=id,
            individual=individual,
            last_name=last_name,
            notes=notes,
            phone_numbers=phone_numbers,
            status=status,
            tax_number=tax_number,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
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

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCustomerSupportCustomersResponse:
        """
        List Customer Support Customers

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomerSupportCustomersResponse
            CustomerSupportCustomers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.customers.all_(
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            raw=raw, cursor=cursor, limit=limit, fields=fields, request_options=request_options
        )
        return _response.data

    async def add(
        self,
        *,
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        bank_accounts: typing.Optional[BankAccount] = OMIT,
        company_name: typing.Optional[CompanyName] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[str] = OMIT,
        individual: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        notes: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        status: typing.Optional[CustomerSupportCustomerStatus] = OMIT,
        tax_number: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCustomerSupportCustomerResponse:
        """
        Create Customer Support Customer

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        bank_accounts : typing.Optional[BankAccount]

        company_name : typing.Optional[CompanyName]

        created_at : typing.Optional[dt.datetime]
            The date and time when the object was created.

        created_by : typing.Optional[str]
            The user who created the object.

        currency : typing.Optional[Currency]

        emails : typing.Optional[typing.Sequence[Email]]

        first_name : typing.Optional[FirstName]

        id : typing.Optional[str]
            A unique identifier for an object.

        individual : typing.Optional[bool]

        last_name : typing.Optional[LastName]

        notes : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        status : typing.Optional[CustomerSupportCustomerStatus]
            Customer status

        tax_number : typing.Optional[str]

        updated_at : typing.Optional[dt.datetime]
            The date and time when the object was last updated.

        updated_by : typing.Optional[str]
            The user who last updated the object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCustomerSupportCustomerResponse
            CustomerSupportCustomers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.customers.add()


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            raw=raw,
            addresses=addresses,
            bank_accounts=bank_accounts,
            company_name=company_name,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            emails=emails,
            first_name=first_name,
            id=id,
            individual=individual,
            last_name=last_name,
            notes=notes,
            phone_numbers=phone_numbers,
            status=status,
            tax_number=tax_number,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCustomerSupportCustomerResponse:
        """
        Get Customer Support Customer

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomerSupportCustomerResponse
            CustomerSupportCustomers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.customers.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteCustomerSupportCustomerResponse:
        """
        Delete Customer Support Customer

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteCustomerSupportCustomerResponse
            CustomerSupportCustomers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.customers.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    async def update(
        self,
        id_: str,
        *,
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        bank_accounts: typing.Optional[BankAccount] = OMIT,
        company_name: typing.Optional[CompanyName] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[str] = OMIT,
        individual: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        notes: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        status: typing.Optional[CustomerSupportCustomerStatus] = OMIT,
        tax_number: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateCustomerSupportCustomerResponse:
        """
        Update Customer Support Customer

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        bank_accounts : typing.Optional[BankAccount]

        company_name : typing.Optional[CompanyName]

        created_at : typing.Optional[dt.datetime]
            The date and time when the object was created.

        created_by : typing.Optional[str]
            The user who created the object.

        currency : typing.Optional[Currency]

        emails : typing.Optional[typing.Sequence[Email]]

        first_name : typing.Optional[FirstName]

        id : typing.Optional[str]
            A unique identifier for an object.

        individual : typing.Optional[bool]

        last_name : typing.Optional[LastName]

        notes : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        status : typing.Optional[CustomerSupportCustomerStatus]
            Customer status

        tax_number : typing.Optional[str]

        updated_at : typing.Optional[dt.datetime]
            The date and time when the object was last updated.

        updated_by : typing.Optional[str]
            The user who last updated the object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCustomerSupportCustomerResponse
            CustomerSupportCustomers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.customers.update(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_,
            raw=raw,
            addresses=addresses,
            bank_accounts=bank_accounts,
            company_name=company_name,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            emails=emails,
            first_name=first_name,
            id=id,
            individual=individual,
            last_name=last_name,
            notes=notes,
            phone_numbers=phone_numbers,
            status=status,
            tax_number=tax_number,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data
