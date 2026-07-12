

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
from ..types.bank_account import BankAccount
from ..types.companies_filter import CompaniesFilter
from ..types.companies_sort import CompaniesSort
from ..types.company_row_type import CompanyRowType
from ..types.create_company_response import CreateCompanyResponse
from ..types.currency import Currency
from ..types.custom_field import CustomField
from ..types.delete_company_response import DeleteCompanyResponse
from ..types.email import Email
from ..types.first_name import FirstName
from ..types.get_companies_response import GetCompaniesResponse
from ..types.get_company_response import GetCompanyResponse
from ..types.last_name import LastName
from ..types.phone_number import PhoneNumber
from ..types.social_link import SocialLink
from ..types.tags import Tags
from ..types.update_company_response import UpdateCompanyResponse
from ..types.website import Website
from .raw_client import AsyncRawCompaniesClient, RawCompaniesClient


OMIT = typing.cast(typing.Any, ...)


class CompaniesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCompaniesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCompaniesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCompaniesClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[CompaniesFilter] = None,
        sort: typing.Optional[CompaniesSort] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCompaniesResponse:
        """
        List companies

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[CompaniesFilter]
            Apply filters

        sort : typing.Optional[CompaniesSort]
            Apply sorting

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCompaniesResponse
            Companies

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.companies.all_(
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.all_(
            raw=raw,
            cursor=cursor,
            limit=limit,
            filter=filter,
            sort=sort,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    def add(
        self,
        *,
        name: str,
        raw: typing.Optional[bool] = None,
        abn_branch: typing.Optional[str] = OMIT,
        abn_or_tfn: typing.Optional[str] = OMIT,
        acn: typing.Optional[str] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        annual_revenue: typing.Optional[str] = OMIT,
        bank_accounts: typing.Optional[typing.Sequence[BankAccount]] = OMIT,
        birthday: typing.Optional[dt.date] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        industry: typing.Optional[str] = OMIT,
        interaction_count: typing.Optional[int] = OMIT,
        last_activity_at: typing.Optional[dt.datetime] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        number_of_employees: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        ownership: typing.Optional[str] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        payee_number: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        row_type: typing.Optional[CompanyRowType] = OMIT,
        sales_tax_number: typing.Optional[str] = OMIT,
        salutation: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        vat_number: typing.Optional[str] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCompanyResponse:
        """
        Create company

        Parameters
        ----------
        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        abn_branch : typing.Optional[str]
            An ABN Branch (also known as a GST Branch) is used if part of your business needs to account for GST separately from its parent entity.

        abn_or_tfn : typing.Optional[str]
            An ABN is necessary for operating a business, while a TFN (Tax File Number) is required for any person working in Australia.

        acn : typing.Optional[str]
            The Australian Company Number (ACN) is a nine digit number with the last digit being a check digit calculated using a modified modulus 10 calculation. ASIC has adopted a convention of always printing and displaying the ACN in the format XXX XXX XXX; three blocks of three characters, each block separated by a blank.

        addresses : typing.Optional[typing.Sequence[Address]]

        annual_revenue : typing.Optional[str]
            Annual revenue

        bank_accounts : typing.Optional[typing.Sequence[BankAccount]]

        birthday : typing.Optional[dt.date]
            The date of birth of the person.

        created_at : typing.Optional[dt.datetime]

        created_by : typing.Optional[str]

        currency : typing.Optional[Currency]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        deleted : typing.Optional[bool]

        description : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_name : typing.Optional[FirstName]

        id : typing.Optional[str]

        image : typing.Optional[str]

        industry : typing.Optional[str]
            Industry

        interaction_count : typing.Optional[int]

        last_activity_at : typing.Optional[dt.datetime]

        last_name : typing.Optional[LastName]

        number_of_employees : typing.Optional[str]
            Number of employees

        owner_id : typing.Optional[str]

        ownership : typing.Optional[str]
            Ownership

        parent_id : typing.Optional[str]
            Parent ID

        payee_number : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        read_only : typing.Optional[bool]

        row_type : typing.Optional[CompanyRowType]

        sales_tax_number : typing.Optional[str]

        salutation : typing.Optional[str]
            A formal salutation for the person. For example, 'Mr', 'Mrs'

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        tags : typing.Optional[Tags]

        updated_at : typing.Optional[dt.datetime]

        updated_by : typing.Optional[str]

        vat_number : typing.Optional[str]
            VAT number

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCompanyResponse
            Company created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.companies.add(
            name="SpaceX",
        )
        """
        _response = self._raw_client.add(
            name=name,
            raw=raw,
            abn_branch=abn_branch,
            abn_or_tfn=abn_or_tfn,
            acn=acn,
            addresses=addresses,
            annual_revenue=annual_revenue,
            bank_accounts=bank_accounts,
            birthday=birthday,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            custom_fields=custom_fields,
            deleted=deleted,
            description=description,
            emails=emails,
            fax=fax,
            first_name=first_name,
            id=id,
            image=image,
            industry=industry,
            interaction_count=interaction_count,
            last_activity_at=last_activity_at,
            last_name=last_name,
            number_of_employees=number_of_employees,
            owner_id=owner_id,
            ownership=ownership,
            parent_id=parent_id,
            payee_number=payee_number,
            phone_numbers=phone_numbers,
            read_only=read_only,
            row_type=row_type,
            sales_tax_number=sales_tax_number,
            salutation=salutation,
            social_links=social_links,
            status=status,
            tags=tags,
            updated_at=updated_at,
            updated_by=updated_by,
            vat_number=vat_number,
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
    ) -> GetCompanyResponse:
        """
        Get company

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
        GetCompanyResponse
            Company

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.companies.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteCompanyResponse:
        """
        Delete company

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
        DeleteCompanyResponse
            Company deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.companies.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    def update(
        self,
        id_: str,
        *,
        name: str,
        raw: typing.Optional[bool] = None,
        abn_branch: typing.Optional[str] = OMIT,
        abn_or_tfn: typing.Optional[str] = OMIT,
        acn: typing.Optional[str] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        annual_revenue: typing.Optional[str] = OMIT,
        bank_accounts: typing.Optional[typing.Sequence[BankAccount]] = OMIT,
        birthday: typing.Optional[dt.date] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        industry: typing.Optional[str] = OMIT,
        interaction_count: typing.Optional[int] = OMIT,
        last_activity_at: typing.Optional[dt.datetime] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        number_of_employees: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        ownership: typing.Optional[str] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        payee_number: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        row_type: typing.Optional[CompanyRowType] = OMIT,
        sales_tax_number: typing.Optional[str] = OMIT,
        salutation: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        vat_number: typing.Optional[str] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateCompanyResponse:
        """
        Update company

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        abn_branch : typing.Optional[str]
            An ABN Branch (also known as a GST Branch) is used if part of your business needs to account for GST separately from its parent entity.

        abn_or_tfn : typing.Optional[str]
            An ABN is necessary for operating a business, while a TFN (Tax File Number) is required for any person working in Australia.

        acn : typing.Optional[str]
            The Australian Company Number (ACN) is a nine digit number with the last digit being a check digit calculated using a modified modulus 10 calculation. ASIC has adopted a convention of always printing and displaying the ACN in the format XXX XXX XXX; three blocks of three characters, each block separated by a blank.

        addresses : typing.Optional[typing.Sequence[Address]]

        annual_revenue : typing.Optional[str]
            Annual revenue

        bank_accounts : typing.Optional[typing.Sequence[BankAccount]]

        birthday : typing.Optional[dt.date]
            The date of birth of the person.

        created_at : typing.Optional[dt.datetime]

        created_by : typing.Optional[str]

        currency : typing.Optional[Currency]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        deleted : typing.Optional[bool]

        description : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_name : typing.Optional[FirstName]

        id : typing.Optional[str]

        image : typing.Optional[str]

        industry : typing.Optional[str]
            Industry

        interaction_count : typing.Optional[int]

        last_activity_at : typing.Optional[dt.datetime]

        last_name : typing.Optional[LastName]

        number_of_employees : typing.Optional[str]
            Number of employees

        owner_id : typing.Optional[str]

        ownership : typing.Optional[str]
            Ownership

        parent_id : typing.Optional[str]
            Parent ID

        payee_number : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        read_only : typing.Optional[bool]

        row_type : typing.Optional[CompanyRowType]

        sales_tax_number : typing.Optional[str]

        salutation : typing.Optional[str]
            A formal salutation for the person. For example, 'Mr', 'Mrs'

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        tags : typing.Optional[Tags]

        updated_at : typing.Optional[dt.datetime]

        updated_by : typing.Optional[str]

        vat_number : typing.Optional[str]
            VAT number

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCompanyResponse
            Company updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.companies.update(
            id_="id",
            name="SpaceX",
        )
        """
        _response = self._raw_client.update(
            id_,
            name=name,
            raw=raw,
            abn_branch=abn_branch,
            abn_or_tfn=abn_or_tfn,
            acn=acn,
            addresses=addresses,
            annual_revenue=annual_revenue,
            bank_accounts=bank_accounts,
            birthday=birthday,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            custom_fields=custom_fields,
            deleted=deleted,
            description=description,
            emails=emails,
            fax=fax,
            first_name=first_name,
            id=id,
            image=image,
            industry=industry,
            interaction_count=interaction_count,
            last_activity_at=last_activity_at,
            last_name=last_name,
            number_of_employees=number_of_employees,
            owner_id=owner_id,
            ownership=ownership,
            parent_id=parent_id,
            payee_number=payee_number,
            phone_numbers=phone_numbers,
            read_only=read_only,
            row_type=row_type,
            sales_tax_number=sales_tax_number,
            salutation=salutation,
            social_links=social_links,
            status=status,
            tags=tags,
            updated_at=updated_at,
            updated_by=updated_by,
            vat_number=vat_number,
            websites=websites,
            request_options=request_options,
        )
        return _response.data


class AsyncCompaniesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCompaniesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCompaniesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCompaniesClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[CompaniesFilter] = None,
        sort: typing.Optional[CompaniesSort] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCompaniesResponse:
        """
        List companies

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[CompaniesFilter]
            Apply filters

        sort : typing.Optional[CompaniesSort]
            Apply sorting

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCompaniesResponse
            Companies

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.companies.all_(
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            raw=raw,
            cursor=cursor,
            limit=limit,
            filter=filter,
            sort=sort,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    async def add(
        self,
        *,
        name: str,
        raw: typing.Optional[bool] = None,
        abn_branch: typing.Optional[str] = OMIT,
        abn_or_tfn: typing.Optional[str] = OMIT,
        acn: typing.Optional[str] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        annual_revenue: typing.Optional[str] = OMIT,
        bank_accounts: typing.Optional[typing.Sequence[BankAccount]] = OMIT,
        birthday: typing.Optional[dt.date] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        industry: typing.Optional[str] = OMIT,
        interaction_count: typing.Optional[int] = OMIT,
        last_activity_at: typing.Optional[dt.datetime] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        number_of_employees: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        ownership: typing.Optional[str] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        payee_number: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        row_type: typing.Optional[CompanyRowType] = OMIT,
        sales_tax_number: typing.Optional[str] = OMIT,
        salutation: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        vat_number: typing.Optional[str] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCompanyResponse:
        """
        Create company

        Parameters
        ----------
        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        abn_branch : typing.Optional[str]
            An ABN Branch (also known as a GST Branch) is used if part of your business needs to account for GST separately from its parent entity.

        abn_or_tfn : typing.Optional[str]
            An ABN is necessary for operating a business, while a TFN (Tax File Number) is required for any person working in Australia.

        acn : typing.Optional[str]
            The Australian Company Number (ACN) is a nine digit number with the last digit being a check digit calculated using a modified modulus 10 calculation. ASIC has adopted a convention of always printing and displaying the ACN in the format XXX XXX XXX; three blocks of three characters, each block separated by a blank.

        addresses : typing.Optional[typing.Sequence[Address]]

        annual_revenue : typing.Optional[str]
            Annual revenue

        bank_accounts : typing.Optional[typing.Sequence[BankAccount]]

        birthday : typing.Optional[dt.date]
            The date of birth of the person.

        created_at : typing.Optional[dt.datetime]

        created_by : typing.Optional[str]

        currency : typing.Optional[Currency]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        deleted : typing.Optional[bool]

        description : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_name : typing.Optional[FirstName]

        id : typing.Optional[str]

        image : typing.Optional[str]

        industry : typing.Optional[str]
            Industry

        interaction_count : typing.Optional[int]

        last_activity_at : typing.Optional[dt.datetime]

        last_name : typing.Optional[LastName]

        number_of_employees : typing.Optional[str]
            Number of employees

        owner_id : typing.Optional[str]

        ownership : typing.Optional[str]
            Ownership

        parent_id : typing.Optional[str]
            Parent ID

        payee_number : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        read_only : typing.Optional[bool]

        row_type : typing.Optional[CompanyRowType]

        sales_tax_number : typing.Optional[str]

        salutation : typing.Optional[str]
            A formal salutation for the person. For example, 'Mr', 'Mrs'

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        tags : typing.Optional[Tags]

        updated_at : typing.Optional[dt.datetime]

        updated_by : typing.Optional[str]

        vat_number : typing.Optional[str]
            VAT number

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCompanyResponse
            Company created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.companies.add(
                name="SpaceX",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            name=name,
            raw=raw,
            abn_branch=abn_branch,
            abn_or_tfn=abn_or_tfn,
            acn=acn,
            addresses=addresses,
            annual_revenue=annual_revenue,
            bank_accounts=bank_accounts,
            birthday=birthday,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            custom_fields=custom_fields,
            deleted=deleted,
            description=description,
            emails=emails,
            fax=fax,
            first_name=first_name,
            id=id,
            image=image,
            industry=industry,
            interaction_count=interaction_count,
            last_activity_at=last_activity_at,
            last_name=last_name,
            number_of_employees=number_of_employees,
            owner_id=owner_id,
            ownership=ownership,
            parent_id=parent_id,
            payee_number=payee_number,
            phone_numbers=phone_numbers,
            read_only=read_only,
            row_type=row_type,
            sales_tax_number=sales_tax_number,
            salutation=salutation,
            social_links=social_links,
            status=status,
            tags=tags,
            updated_at=updated_at,
            updated_by=updated_by,
            vat_number=vat_number,
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
    ) -> GetCompanyResponse:
        """
        Get company

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
        GetCompanyResponse
            Company

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.companies.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteCompanyResponse:
        """
        Delete company

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
        DeleteCompanyResponse
            Company deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.companies.delete(
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
        name: str,
        raw: typing.Optional[bool] = None,
        abn_branch: typing.Optional[str] = OMIT,
        abn_or_tfn: typing.Optional[str] = OMIT,
        acn: typing.Optional[str] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        annual_revenue: typing.Optional[str] = OMIT,
        bank_accounts: typing.Optional[typing.Sequence[BankAccount]] = OMIT,
        birthday: typing.Optional[dt.date] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_name: typing.Optional[FirstName] = OMIT,
        id: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        industry: typing.Optional[str] = OMIT,
        interaction_count: typing.Optional[int] = OMIT,
        last_activity_at: typing.Optional[dt.datetime] = OMIT,
        last_name: typing.Optional[LastName] = OMIT,
        number_of_employees: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        ownership: typing.Optional[str] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        payee_number: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        row_type: typing.Optional[CompanyRowType] = OMIT,
        sales_tax_number: typing.Optional[str] = OMIT,
        salutation: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        vat_number: typing.Optional[str] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateCompanyResponse:
        """
        Update company

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        abn_branch : typing.Optional[str]
            An ABN Branch (also known as a GST Branch) is used if part of your business needs to account for GST separately from its parent entity.

        abn_or_tfn : typing.Optional[str]
            An ABN is necessary for operating a business, while a TFN (Tax File Number) is required for any person working in Australia.

        acn : typing.Optional[str]
            The Australian Company Number (ACN) is a nine digit number with the last digit being a check digit calculated using a modified modulus 10 calculation. ASIC has adopted a convention of always printing and displaying the ACN in the format XXX XXX XXX; three blocks of three characters, each block separated by a blank.

        addresses : typing.Optional[typing.Sequence[Address]]

        annual_revenue : typing.Optional[str]
            Annual revenue

        bank_accounts : typing.Optional[typing.Sequence[BankAccount]]

        birthday : typing.Optional[dt.date]
            The date of birth of the person.

        created_at : typing.Optional[dt.datetime]

        created_by : typing.Optional[str]

        currency : typing.Optional[Currency]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        deleted : typing.Optional[bool]

        description : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_name : typing.Optional[FirstName]

        id : typing.Optional[str]

        image : typing.Optional[str]

        industry : typing.Optional[str]
            Industry

        interaction_count : typing.Optional[int]

        last_activity_at : typing.Optional[dt.datetime]

        last_name : typing.Optional[LastName]

        number_of_employees : typing.Optional[str]
            Number of employees

        owner_id : typing.Optional[str]

        ownership : typing.Optional[str]
            Ownership

        parent_id : typing.Optional[str]
            Parent ID

        payee_number : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        read_only : typing.Optional[bool]

        row_type : typing.Optional[CompanyRowType]

        sales_tax_number : typing.Optional[str]

        salutation : typing.Optional[str]
            A formal salutation for the person. For example, 'Mr', 'Mrs'

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        tags : typing.Optional[Tags]

        updated_at : typing.Optional[dt.datetime]

        updated_by : typing.Optional[str]

        vat_number : typing.Optional[str]
            VAT number

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCompanyResponse
            Company updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.companies.update(
                id_="id",
                name="SpaceX",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_,
            name=name,
            raw=raw,
            abn_branch=abn_branch,
            abn_or_tfn=abn_or_tfn,
            acn=acn,
            addresses=addresses,
            annual_revenue=annual_revenue,
            bank_accounts=bank_accounts,
            birthday=birthday,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            custom_fields=custom_fields,
            deleted=deleted,
            description=description,
            emails=emails,
            fax=fax,
            first_name=first_name,
            id=id,
            image=image,
            industry=industry,
            interaction_count=interaction_count,
            last_activity_at=last_activity_at,
            last_name=last_name,
            number_of_employees=number_of_employees,
            owner_id=owner_id,
            ownership=ownership,
            parent_id=parent_id,
            payee_number=payee_number,
            phone_numbers=phone_numbers,
            read_only=read_only,
            row_type=row_type,
            sales_tax_number=sales_tax_number,
            salutation=salutation,
            social_links=social_links,
            status=status,
            tags=tags,
            updated_at=updated_at,
            updated_by=updated_by,
            vat_number=vat_number,
            websites=websites,
            request_options=request_options,
        )
        return _response.data
