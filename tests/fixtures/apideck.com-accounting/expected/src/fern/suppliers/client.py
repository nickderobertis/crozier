

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
from ..types.bank_account import BankAccount
from ..types.company_name import CompanyName
from ..types.create_supplier_response import CreateSupplierResponse
from ..types.created_at import CreatedAt
from ..types.created_by import CreatedBy
from ..types.currency import Currency
from ..types.delete_supplier_response import DeleteSupplierResponse
from ..types.downstream_id import DownstreamId
from ..types.email import Email
from ..types.first_name import FirstName
from ..types.get_supplier_response import GetSupplierResponse
from ..types.get_suppliers_response import GetSuppliersResponse
from ..types.id import Id
from ..types.last_name import LastName
from ..types.linked_ledger_account import LinkedLedgerAccount
from ..types.linked_tax_rate import LinkedTaxRate
from ..types.middle_name import MiddleName
from ..types.pass_through_query import PassThroughQuery
from ..types.phone_number import PhoneNumber
from ..types.row_version import RowVersion
from ..types.suffix import Suffix
from ..types.supplier_status import SupplierStatus
from ..types.suppliers_filter import SuppliersFilter
from ..types.tax_number import TaxNumber
from ..types.title import Title
from ..types.update_supplier_response import UpdateSupplierResponse
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy
from ..types.website import Website
from .raw_client import AsyncRawSuppliersClient, RawSuppliersClient


OMIT = typing.cast(typing.Any, ...)


class SuppliersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSuppliersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSuppliersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSuppliersClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[SuppliersFilter] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSuppliersResponse:
        """
        List Suppliers

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[SuppliersFilter]
            Apply filters

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSuppliersResponse
            Suppliers

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.suppliers.all_(
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.all_(
            raw=raw,
            cursor=cursor,
            limit=limit,
            filter=filter,
            pass_through=pass_through,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    def add(
        self,
        *,
        raw: typing.Optional[bool] = None,
        account: typing.Optional[LinkedLedgerAccount] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        bank_accounts: typing.Optional[typing.Sequence[BankAccount]] = OMIT,
        company_name: typing.Optional[CompanyName] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        downstream_id: typing.Optional[DownstreamId] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[Id] = OMIT,
        individual: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        middle_name: typing.Optional[MiddleName] = OMIT,
        notes: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[SupplierStatus] = OMIT,
        suffix: typing.Optional[Suffix] = OMIT,
        tax_number: typing.Optional[TaxNumber] = OMIT,
        tax_rate: typing.Optional[LinkedTaxRate] = OMIT,
        title: typing.Optional[Title] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSupplierResponse:
        """
        Create Supplier

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account : typing.Optional[LinkedLedgerAccount]

        addresses : typing.Optional[typing.Sequence[Address]]

        bank_accounts : typing.Optional[typing.Sequence[BankAccount]]

        company_name : typing.Optional[CompanyName]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        display_id : typing.Optional[str]
            Display ID

        display_name : typing.Optional[str]
            Display name

        downstream_id : typing.Optional[DownstreamId]

        emails : typing.Optional[typing.Sequence[Email]]

        first_name : typing.Optional[FirstName]

        id : typing.Optional[Id]

        individual : typing.Optional[bool]
            Is this an individual or business supplier

        last_name : typing.Optional[LastName]

        middle_name : typing.Optional[MiddleName]

        notes : typing.Optional[str]
            Some notes about this supplier

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[SupplierStatus]
            Supplier status

        suffix : typing.Optional[Suffix]

        tax_number : typing.Optional[TaxNumber]

        tax_rate : typing.Optional[LinkedTaxRate]

        title : typing.Optional[Title]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSupplierResponse
            Supplier created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.suppliers.add()
        """
        _response = self._raw_client.add(
            raw=raw,
            account=account,
            addresses=addresses,
            bank_accounts=bank_accounts,
            company_name=company_name,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            display_id=display_id,
            display_name=display_name,
            downstream_id=downstream_id,
            emails=emails,
            first_name=first_name,
            id=id,
            individual=individual,
            last_name=last_name,
            middle_name=middle_name,
            notes=notes,
            phone_numbers=phone_numbers,
            row_version=row_version,
            status=status,
            suffix=suffix,
            tax_number=tax_number,
            tax_rate=tax_rate,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            websites=websites,
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
    ) -> GetSupplierResponse:
        """
        Get Supplier

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
        GetSupplierResponse
            Supplier

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.suppliers.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteSupplierResponse:
        """
        Delete Supplier

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
        DeleteSupplierResponse
            Supplier deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.suppliers.delete(
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
        account: typing.Optional[LinkedLedgerAccount] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        bank_accounts: typing.Optional[typing.Sequence[BankAccount]] = OMIT,
        company_name: typing.Optional[CompanyName] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        downstream_id: typing.Optional[DownstreamId] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[Id] = OMIT,
        individual: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        middle_name: typing.Optional[MiddleName] = OMIT,
        notes: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[SupplierStatus] = OMIT,
        suffix: typing.Optional[Suffix] = OMIT,
        tax_number: typing.Optional[TaxNumber] = OMIT,
        tax_rate: typing.Optional[LinkedTaxRate] = OMIT,
        title: typing.Optional[Title] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSupplierResponse:
        """
        Update Supplier

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account : typing.Optional[LinkedLedgerAccount]

        addresses : typing.Optional[typing.Sequence[Address]]

        bank_accounts : typing.Optional[typing.Sequence[BankAccount]]

        company_name : typing.Optional[CompanyName]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        display_id : typing.Optional[str]
            Display ID

        display_name : typing.Optional[str]
            Display name

        downstream_id : typing.Optional[DownstreamId]

        emails : typing.Optional[typing.Sequence[Email]]

        first_name : typing.Optional[FirstName]

        id : typing.Optional[Id]

        individual : typing.Optional[bool]
            Is this an individual or business supplier

        last_name : typing.Optional[LastName]

        middle_name : typing.Optional[MiddleName]

        notes : typing.Optional[str]
            Some notes about this supplier

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[SupplierStatus]
            Supplier status

        suffix : typing.Optional[Suffix]

        tax_number : typing.Optional[TaxNumber]

        tax_rate : typing.Optional[LinkedTaxRate]

        title : typing.Optional[Title]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSupplierResponse
            Supplier updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.suppliers.update(
            id_="id",
        )
        """
        _response = self._raw_client.update(
            id_,
            raw=raw,
            account=account,
            addresses=addresses,
            bank_accounts=bank_accounts,
            company_name=company_name,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            display_id=display_id,
            display_name=display_name,
            downstream_id=downstream_id,
            emails=emails,
            first_name=first_name,
            id=id,
            individual=individual,
            last_name=last_name,
            middle_name=middle_name,
            notes=notes,
            phone_numbers=phone_numbers,
            row_version=row_version,
            status=status,
            suffix=suffix,
            tax_number=tax_number,
            tax_rate=tax_rate,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            websites=websites,
            request_options=request_options,
        )
        return _response.data


class AsyncSuppliersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSuppliersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSuppliersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSuppliersClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[SuppliersFilter] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSuppliersResponse:
        """
        List Suppliers

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[SuppliersFilter]
            Apply filters

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSuppliersResponse
            Suppliers

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
            await client.suppliers.all_(
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            raw=raw,
            cursor=cursor,
            limit=limit,
            filter=filter,
            pass_through=pass_through,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    async def add(
        self,
        *,
        raw: typing.Optional[bool] = None,
        account: typing.Optional[LinkedLedgerAccount] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        bank_accounts: typing.Optional[typing.Sequence[BankAccount]] = OMIT,
        company_name: typing.Optional[CompanyName] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        downstream_id: typing.Optional[DownstreamId] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[Id] = OMIT,
        individual: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        middle_name: typing.Optional[MiddleName] = OMIT,
        notes: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[SupplierStatus] = OMIT,
        suffix: typing.Optional[Suffix] = OMIT,
        tax_number: typing.Optional[TaxNumber] = OMIT,
        tax_rate: typing.Optional[LinkedTaxRate] = OMIT,
        title: typing.Optional[Title] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSupplierResponse:
        """
        Create Supplier

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account : typing.Optional[LinkedLedgerAccount]

        addresses : typing.Optional[typing.Sequence[Address]]

        bank_accounts : typing.Optional[typing.Sequence[BankAccount]]

        company_name : typing.Optional[CompanyName]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        display_id : typing.Optional[str]
            Display ID

        display_name : typing.Optional[str]
            Display name

        downstream_id : typing.Optional[DownstreamId]

        emails : typing.Optional[typing.Sequence[Email]]

        first_name : typing.Optional[FirstName]

        id : typing.Optional[Id]

        individual : typing.Optional[bool]
            Is this an individual or business supplier

        last_name : typing.Optional[LastName]

        middle_name : typing.Optional[MiddleName]

        notes : typing.Optional[str]
            Some notes about this supplier

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[SupplierStatus]
            Supplier status

        suffix : typing.Optional[Suffix]

        tax_number : typing.Optional[TaxNumber]

        tax_rate : typing.Optional[LinkedTaxRate]

        title : typing.Optional[Title]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSupplierResponse
            Supplier created

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
            await client.suppliers.add()


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            raw=raw,
            account=account,
            addresses=addresses,
            bank_accounts=bank_accounts,
            company_name=company_name,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            display_id=display_id,
            display_name=display_name,
            downstream_id=downstream_id,
            emails=emails,
            first_name=first_name,
            id=id,
            individual=individual,
            last_name=last_name,
            middle_name=middle_name,
            notes=notes,
            phone_numbers=phone_numbers,
            row_version=row_version,
            status=status,
            suffix=suffix,
            tax_number=tax_number,
            tax_rate=tax_rate,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            websites=websites,
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
    ) -> GetSupplierResponse:
        """
        Get Supplier

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
        GetSupplierResponse
            Supplier

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
            await client.suppliers.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteSupplierResponse:
        """
        Delete Supplier

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
        DeleteSupplierResponse
            Supplier deleted

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
            await client.suppliers.delete(
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
        account: typing.Optional[LinkedLedgerAccount] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        bank_accounts: typing.Optional[typing.Sequence[BankAccount]] = OMIT,
        company_name: typing.Optional[CompanyName] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        downstream_id: typing.Optional[DownstreamId] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[Id] = OMIT,
        individual: typing.Optional[bool] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        middle_name: typing.Optional[MiddleName] = OMIT,
        notes: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[SupplierStatus] = OMIT,
        suffix: typing.Optional[Suffix] = OMIT,
        tax_number: typing.Optional[TaxNumber] = OMIT,
        tax_rate: typing.Optional[LinkedTaxRate] = OMIT,
        title: typing.Optional[Title] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSupplierResponse:
        """
        Update Supplier

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        account : typing.Optional[LinkedLedgerAccount]

        addresses : typing.Optional[typing.Sequence[Address]]

        bank_accounts : typing.Optional[typing.Sequence[BankAccount]]

        company_name : typing.Optional[CompanyName]

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        display_id : typing.Optional[str]
            Display ID

        display_name : typing.Optional[str]
            Display name

        downstream_id : typing.Optional[DownstreamId]

        emails : typing.Optional[typing.Sequence[Email]]

        first_name : typing.Optional[FirstName]

        id : typing.Optional[Id]

        individual : typing.Optional[bool]
            Is this an individual or business supplier

        last_name : typing.Optional[LastName]

        middle_name : typing.Optional[MiddleName]

        notes : typing.Optional[str]
            Some notes about this supplier

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[SupplierStatus]
            Supplier status

        suffix : typing.Optional[Suffix]

        tax_number : typing.Optional[TaxNumber]

        tax_rate : typing.Optional[LinkedTaxRate]

        title : typing.Optional[Title]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSupplierResponse
            Supplier updated

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
            await client.suppliers.update(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_,
            raw=raw,
            account=account,
            addresses=addresses,
            bank_accounts=bank_accounts,
            company_name=company_name,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            display_id=display_id,
            display_name=display_name,
            downstream_id=downstream_id,
            emails=emails,
            first_name=first_name,
            id=id,
            individual=individual,
            last_name=last_name,
            middle_name=middle_name,
            notes=notes,
            phone_numbers=phone_numbers,
            row_version=row_version,
            status=status,
            suffix=suffix,
            tax_number=tax_number,
            tax_rate=tax_rate,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            websites=websites,
            request_options=request_options,
        )
        return _response.data
