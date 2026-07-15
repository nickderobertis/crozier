

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
from ..types.create_hris_company_response import CreateHrisCompanyResponse
from ..types.created_at import CreatedAt
from ..types.created_by import CreatedBy
from ..types.delete_hris_company_response import DeleteHrisCompanyResponse
from ..types.email import Email
from ..types.get_hris_companies_response import GetHrisCompaniesResponse
from ..types.get_hris_company_response import GetHrisCompanyResponse
from ..types.hris_company_status import HrisCompanyStatus
from ..types.id import Id
from ..types.phone_number import PhoneNumber
from ..types.update_hris_company_response import UpdateHrisCompanyResponse
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy
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
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetHrisCompaniesResponse:
        """
        List Companies

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
        GetHrisCompaniesResponse
            Companies

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.companies.all_(
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
        legal_name: str,
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        company_number: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        debtor_id: typing.Optional[str] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        id: typing.Optional[Id] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        status: typing.Optional[HrisCompanyStatus] = OMIT,
        subdomain: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateHrisCompanyResponse:
        """
        Create Company

        Parameters
        ----------
        legal_name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        company_number : typing.Optional[str]
            An Company Number, Company ID or Company Code, is a unique number that has been assigned to each company.

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        debtor_id : typing.Optional[str]

        deleted : typing.Optional[bool]

        display_name : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        id : typing.Optional[Id]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        status : typing.Optional[HrisCompanyStatus]

        subdomain : typing.Optional[str]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateHrisCompanyResponse
            Companies

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.companies.add(
            legal_name="SpaceX",
        )
        """
        _response = self._raw_client.add(
            legal_name=legal_name,
            raw=raw,
            addresses=addresses,
            company_number=company_number,
            created_at=created_at,
            created_by=created_by,
            debtor_id=debtor_id,
            deleted=deleted,
            display_name=display_name,
            emails=emails,
            id=id,
            phone_numbers=phone_numbers,
            status=status,
            subdomain=subdomain,
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
    ) -> GetHrisCompanyResponse:
        """
        Get Company

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
        GetHrisCompanyResponse
            Company

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
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
    ) -> DeleteHrisCompanyResponse:
        """
        Delete Company

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
        DeleteHrisCompanyResponse
            Companies

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
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
        legal_name: str,
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        company_number: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        debtor_id: typing.Optional[str] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        id: typing.Optional[Id] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        status: typing.Optional[HrisCompanyStatus] = OMIT,
        subdomain: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateHrisCompanyResponse:
        """
        Update Company

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        legal_name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        company_number : typing.Optional[str]
            An Company Number, Company ID or Company Code, is a unique number that has been assigned to each company.

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        debtor_id : typing.Optional[str]

        deleted : typing.Optional[bool]

        display_name : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        id : typing.Optional[Id]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        status : typing.Optional[HrisCompanyStatus]

        subdomain : typing.Optional[str]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateHrisCompanyResponse
            Companies

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.companies.update(
            id_="id",
            legal_name="SpaceX",
        )
        """
        _response = self._raw_client.update(
            id_,
            legal_name=legal_name,
            raw=raw,
            addresses=addresses,
            company_number=company_number,
            created_at=created_at,
            created_by=created_by,
            debtor_id=debtor_id,
            deleted=deleted,
            display_name=display_name,
            emails=emails,
            id=id,
            phone_numbers=phone_numbers,
            status=status,
            subdomain=subdomain,
            updated_at=updated_at,
            updated_by=updated_by,
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
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetHrisCompaniesResponse:
        """
        List Companies

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
        GetHrisCompaniesResponse
            Companies

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
            await client.companies.all_(
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
        legal_name: str,
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        company_number: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        debtor_id: typing.Optional[str] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        id: typing.Optional[Id] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        status: typing.Optional[HrisCompanyStatus] = OMIT,
        subdomain: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateHrisCompanyResponse:
        """
        Create Company

        Parameters
        ----------
        legal_name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        company_number : typing.Optional[str]
            An Company Number, Company ID or Company Code, is a unique number that has been assigned to each company.

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        debtor_id : typing.Optional[str]

        deleted : typing.Optional[bool]

        display_name : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        id : typing.Optional[Id]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        status : typing.Optional[HrisCompanyStatus]

        subdomain : typing.Optional[str]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateHrisCompanyResponse
            Companies

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
            await client.companies.add(
                legal_name="SpaceX",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            legal_name=legal_name,
            raw=raw,
            addresses=addresses,
            company_number=company_number,
            created_at=created_at,
            created_by=created_by,
            debtor_id=debtor_id,
            deleted=deleted,
            display_name=display_name,
            emails=emails,
            id=id,
            phone_numbers=phone_numbers,
            status=status,
            subdomain=subdomain,
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
    ) -> GetHrisCompanyResponse:
        """
        Get Company

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
        GetHrisCompanyResponse
            Company

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
    ) -> DeleteHrisCompanyResponse:
        """
        Delete Company

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
        DeleteHrisCompanyResponse
            Companies

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
        legal_name: str,
        raw: typing.Optional[bool] = None,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        company_number: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        debtor_id: typing.Optional[str] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        id: typing.Optional[Id] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        status: typing.Optional[HrisCompanyStatus] = OMIT,
        subdomain: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateHrisCompanyResponse:
        """
        Update Company

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        legal_name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        company_number : typing.Optional[str]
            An Company Number, Company ID or Company Code, is a unique number that has been assigned to each company.

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        debtor_id : typing.Optional[str]

        deleted : typing.Optional[bool]

        display_name : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        id : typing.Optional[Id]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        status : typing.Optional[HrisCompanyStatus]

        subdomain : typing.Optional[str]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateHrisCompanyResponse
            Companies

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
            await client.companies.update(
                id_="id",
                legal_name="SpaceX",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_,
            legal_name=legal_name,
            raw=raw,
            addresses=addresses,
            company_number=company_number,
            created_at=created_at,
            created_by=created_by,
            debtor_id=debtor_id,
            deleted=deleted,
            display_name=display_name,
            emails=emails,
            id=id,
            phone_numbers=phone_numbers,
            status=status,
            subdomain=subdomain,
            updated_at=updated_at,
            updated_by=updated_by,
            websites=websites,
            request_options=request_options,
        )
        return _response.data
