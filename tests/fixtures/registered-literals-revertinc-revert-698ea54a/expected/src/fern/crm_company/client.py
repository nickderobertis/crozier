

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.common_company_address import CommonCompanyAddress
from ..types.common_company_association import CommonCompanyAssociation
from ..types.crm_create_or_update_company_response import CrmCreateOrUpdateCompanyResponse
from ..types.crm_get_companies_response import CrmGetCompaniesResponse
from ..types.crm_get_company_response import CrmGetCompanyResponse
from ..types.crm_search_companies_response import CrmSearchCompaniesResponse
from .raw_client import AsyncRawCrmCompanyClient, RawCrmCompanyClient


OMIT = typing.cast(typing.Any, ...)


class CrmCompanyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCrmCompanyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCrmCompanyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCrmCompanyClient
        """
        return self._raw_client

    def crm_company_get_company(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetCompanyResponse:
        """
        Get details of a company

        Parameters
        ----------
        id : str
            The unique `id` of the company in the CRM.

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetCompanyResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_company.crm_company_get_company(
            id="id",
        )
        """
        _response = self._raw_client.crm_company_get_company(
            id, fields=fields, associations=associations, request_options=request_options
        )
        return _response.data

    def crm_company_update_company(
        self,
        id_: str,
        *,
        name: str,
        industry: str,
        description: str,
        annual_revenue: int,
        size: int,
        phone: str,
        address: CommonCompanyAddress,
        id: str,
        remote_id: str,
        created_timestamp: typing.Any,
        updated_timestamp: typing.Any,
        additional: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateCompanyResponse:
        """
        Update a company

        Parameters
        ----------
        id_ : str

        name : str
            Name of the company in a CRM.

        industry : str
            Industry associated with this company. (not supported by pipedrive)

        description : str
            Description of the company. (not supported by pipedrive)

        annual_revenue : int
            Annual revenue of the company. (not supported by pipedrive)

        size : int
            Number of employees or size of the company.

        phone : str
            Phone number of the company. (not supported by pipedrive)

        address : CommonCompanyAddress
            Company address.

        id : str
            The unique `id` of this object in Revert

        remote_id : str
            The unique `id` of this object in the downstream CRM.

        created_timestamp : typing.Any

        updated_timestamp : typing.Any

        additional : typing.Optional[typing.Any]
            Any fields that are not unified yet/non-unifiable come inside this `json` object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateCompanyResponse


        Examples
        --------
        from fern import CommonCompanyAddress, FernApi

        client = FernApi()
        client.crm_company.crm_company_update_company(
            id_="id",
            name="name",
            industry="industry",
            description="description",
            annual_revenue=1,
            size=1,
            phone="phone",
            address=CommonCompanyAddress(
                city="city",
                state="state",
                country="country",
                zip="zip",
                postal_code="postalCode",
            ),
            id="id",
            remote_id="remoteId",
            created_timestamp={"key": "value"},
            updated_timestamp={"key": "value"},
        )
        """
        _response = self._raw_client.crm_company_update_company(
            id_,
            name=name,
            industry=industry,
            description=description,
            annual_revenue=annual_revenue,
            size=size,
            phone=phone,
            address=address,
            id=id,
            remote_id=remote_id,
            created_timestamp=created_timestamp,
            updated_timestamp=updated_timestamp,
            additional=additional,
            request_options=request_options,
        )
        return _response.data

    def crm_company_get_companies(
        self,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetCompaniesResponse:
        """
        Get all the companies

        Parameters
        ----------
        fields : typing.Optional[str]

        associations : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetCompaniesResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_company.crm_company_get_companies()
        """
        _response = self._raw_client.crm_company_get_companies(
            fields=fields,
            associations=associations,
            page_size=page_size,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data

    def crm_company_create_company(
        self,
        *,
        name: str,
        industry: str,
        description: str,
        annual_revenue: int,
        size: int,
        phone: str,
        address: CommonCompanyAddress,
        id: str,
        remote_id: str,
        created_timestamp: typing.Any,
        updated_timestamp: typing.Any,
        associations: typing.Optional[CommonCompanyAssociation] = OMIT,
        additional: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateCompanyResponse:
        """
        Create a new company

        Parameters
        ----------
        name : str
            Name of the company in a CRM.

        industry : str
            Industry associated with this company. (not supported by pipedrive)

        description : str
            Description of the company. (not supported by pipedrive)

        annual_revenue : int
            Annual revenue of the company. (not supported by pipedrive)

        size : int
            Number of employees or size of the company.

        phone : str
            Phone number of the company. (not supported by pipedrive)

        address : CommonCompanyAddress
            Company address.

        id : str
            The unique `id` of this object in Revert

        remote_id : str
            The unique `id` of this object in the downstream CRM.

        created_timestamp : typing.Any

        updated_timestamp : typing.Any

        associations : typing.Optional[CommonCompanyAssociation]

        additional : typing.Optional[typing.Any]
            Any fields that are not unified yet/non-unifiable come inside this `json` object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateCompanyResponse


        Examples
        --------
        from fern import CommonCompanyAddress, FernApi

        client = FernApi()
        client.crm_company.crm_company_create_company(
            name="name",
            industry="industry",
            description="description",
            annual_revenue=1,
            size=1,
            phone="phone",
            address=CommonCompanyAddress(
                city="city",
                state="state",
                country="country",
                zip="zip",
                postal_code="postalCode",
            ),
            id="id",
            remote_id="remoteId",
            created_timestamp={"key": "value"},
            updated_timestamp={"key": "value"},
        )
        """
        _response = self._raw_client.crm_company_create_company(
            name=name,
            industry=industry,
            description=description,
            annual_revenue=annual_revenue,
            size=size,
            phone=phone,
            address=address,
            id=id,
            remote_id=remote_id,
            created_timestamp=created_timestamp,
            updated_timestamp=updated_timestamp,
            associations=associations,
            additional=additional,
            request_options=request_options,
        )
        return _response.data

    def crm_company_search_companies(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmSearchCompaniesResponse:
        """
        Search for companies

        Parameters
        ----------
        search_criteria : typing.Any

        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmSearchCompaniesResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_company.crm_company_search_companies(
            search_criteria={"key": "value"},
        )
        """
        _response = self._raw_client.crm_company_search_companies(
            search_criteria=search_criteria,
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data


class AsyncCrmCompanyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCrmCompanyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCrmCompanyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCrmCompanyClient
        """
        return self._raw_client

    async def crm_company_get_company(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetCompanyResponse:
        """
        Get details of a company

        Parameters
        ----------
        id : str
            The unique `id` of the company in the CRM.

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetCompanyResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_company.crm_company_get_company(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_company_get_company(
            id, fields=fields, associations=associations, request_options=request_options
        )
        return _response.data

    async def crm_company_update_company(
        self,
        id_: str,
        *,
        name: str,
        industry: str,
        description: str,
        annual_revenue: int,
        size: int,
        phone: str,
        address: CommonCompanyAddress,
        id: str,
        remote_id: str,
        created_timestamp: typing.Any,
        updated_timestamp: typing.Any,
        additional: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateCompanyResponse:
        """
        Update a company

        Parameters
        ----------
        id_ : str

        name : str
            Name of the company in a CRM.

        industry : str
            Industry associated with this company. (not supported by pipedrive)

        description : str
            Description of the company. (not supported by pipedrive)

        annual_revenue : int
            Annual revenue of the company. (not supported by pipedrive)

        size : int
            Number of employees or size of the company.

        phone : str
            Phone number of the company. (not supported by pipedrive)

        address : CommonCompanyAddress
            Company address.

        id : str
            The unique `id` of this object in Revert

        remote_id : str
            The unique `id` of this object in the downstream CRM.

        created_timestamp : typing.Any

        updated_timestamp : typing.Any

        additional : typing.Optional[typing.Any]
            Any fields that are not unified yet/non-unifiable come inside this `json` object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateCompanyResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CommonCompanyAddress

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_company.crm_company_update_company(
                id_="id",
                name="name",
                industry="industry",
                description="description",
                annual_revenue=1,
                size=1,
                phone="phone",
                address=CommonCompanyAddress(
                    city="city",
                    state="state",
                    country="country",
                    zip="zip",
                    postal_code="postalCode",
                ),
                id="id",
                remote_id="remoteId",
                created_timestamp={"key": "value"},
                updated_timestamp={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_company_update_company(
            id_,
            name=name,
            industry=industry,
            description=description,
            annual_revenue=annual_revenue,
            size=size,
            phone=phone,
            address=address,
            id=id,
            remote_id=remote_id,
            created_timestamp=created_timestamp,
            updated_timestamp=updated_timestamp,
            additional=additional,
            request_options=request_options,
        )
        return _response.data

    async def crm_company_get_companies(
        self,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetCompaniesResponse:
        """
        Get all the companies

        Parameters
        ----------
        fields : typing.Optional[str]

        associations : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetCompaniesResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_company.crm_company_get_companies()


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_company_get_companies(
            fields=fields,
            associations=associations,
            page_size=page_size,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data

    async def crm_company_create_company(
        self,
        *,
        name: str,
        industry: str,
        description: str,
        annual_revenue: int,
        size: int,
        phone: str,
        address: CommonCompanyAddress,
        id: str,
        remote_id: str,
        created_timestamp: typing.Any,
        updated_timestamp: typing.Any,
        associations: typing.Optional[CommonCompanyAssociation] = OMIT,
        additional: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateCompanyResponse:
        """
        Create a new company

        Parameters
        ----------
        name : str
            Name of the company in a CRM.

        industry : str
            Industry associated with this company. (not supported by pipedrive)

        description : str
            Description of the company. (not supported by pipedrive)

        annual_revenue : int
            Annual revenue of the company. (not supported by pipedrive)

        size : int
            Number of employees or size of the company.

        phone : str
            Phone number of the company. (not supported by pipedrive)

        address : CommonCompanyAddress
            Company address.

        id : str
            The unique `id` of this object in Revert

        remote_id : str
            The unique `id` of this object in the downstream CRM.

        created_timestamp : typing.Any

        updated_timestamp : typing.Any

        associations : typing.Optional[CommonCompanyAssociation]

        additional : typing.Optional[typing.Any]
            Any fields that are not unified yet/non-unifiable come inside this `json` object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateCompanyResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CommonCompanyAddress

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_company.crm_company_create_company(
                name="name",
                industry="industry",
                description="description",
                annual_revenue=1,
                size=1,
                phone="phone",
                address=CommonCompanyAddress(
                    city="city",
                    state="state",
                    country="country",
                    zip="zip",
                    postal_code="postalCode",
                ),
                id="id",
                remote_id="remoteId",
                created_timestamp={"key": "value"},
                updated_timestamp={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_company_create_company(
            name=name,
            industry=industry,
            description=description,
            annual_revenue=annual_revenue,
            size=size,
            phone=phone,
            address=address,
            id=id,
            remote_id=remote_id,
            created_timestamp=created_timestamp,
            updated_timestamp=updated_timestamp,
            associations=associations,
            additional=additional,
            request_options=request_options,
        )
        return _response.data

    async def crm_company_search_companies(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmSearchCompaniesResponse:
        """
        Search for companies

        Parameters
        ----------
        search_criteria : typing.Any

        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmSearchCompaniesResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_company.crm_company_search_companies(
                search_criteria={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_company_search_companies(
            search_criteria=search_criteria,
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data
