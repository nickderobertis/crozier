

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.common_lead_association import CommonLeadAssociation
from ..types.crm_create_or_update_lead_response import CrmCreateOrUpdateLeadResponse
from ..types.crm_get_lead_response import CrmGetLeadResponse
from ..types.crm_get_leads_response import CrmGetLeadsResponse
from ..types.crm_search_leads_response import CrmSearchLeadsResponse
from .raw_client import AsyncRawCrmLeadClient, RawCrmLeadClient


OMIT = typing.cast(typing.Any, ...)


class CrmLeadClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCrmLeadClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCrmLeadClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCrmLeadClient
        """
        return self._raw_client

    def crm_lead_get_lead(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetLeadResponse:
        """
        Get details of a lead

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetLeadResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_lead.crm_lead_get_lead(
            id="id",
        )
        """
        _response = self._raw_client.crm_lead_get_lead(
            id, fields=fields, associations=associations, request_options=request_options
        )
        return _response.data

    def crm_lead_update_lead(
        self,
        id: str,
        *,
        additional: typing.Any,
        first_name: str,
        last_name: str,
        phone: str,
        email: str,
        associations: typing.Optional[CommonLeadAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateLeadResponse:
        """
        Update a lead

        Parameters
        ----------
        id : str

        additional : typing.Any

        first_name : str
            The first name of the lead in a CRM.

        last_name : str
            The last name of the lead in a CRM.

        phone : str
            The phone number of the lead in a CRM.

        email : str
            The email of the lead in a CRM.

        associations : typing.Optional[CommonLeadAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateLeadResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_lead.crm_lead_update_lead(
            id="id",
            additional={"key": "value"},
            first_name="firstName",
            last_name="lastName",
            phone="phone",
            email="email",
        )
        """
        _response = self._raw_client.crm_lead_update_lead(
            id,
            additional=additional,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    def crm_lead_get_leads(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetLeadsResponse:
        """
        Get all the leads

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetLeadsResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_lead.crm_lead_get_leads()
        """
        _response = self._raw_client.crm_lead_get_leads(
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    def crm_lead_create_lead(
        self,
        *,
        additional: typing.Any,
        first_name: str,
        last_name: str,
        phone: str,
        email: str,
        associations: typing.Optional[CommonLeadAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateLeadResponse:
        """
        Create a new lead

        Parameters
        ----------
        additional : typing.Any

        first_name : str
            The first name of the lead in a CRM.

        last_name : str
            The last name of the lead in a CRM.

        phone : str
            The phone number of the lead in a CRM.

        email : str
            The email of the lead in a CRM.

        associations : typing.Optional[CommonLeadAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateLeadResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_lead.crm_lead_create_lead(
            additional={"key": "value"},
            first_name="firstName",
            last_name="lastName",
            phone="phone",
            email="email",
        )
        """
        _response = self._raw_client.crm_lead_create_lead(
            additional=additional,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    def crm_lead_search_leads(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmSearchLeadsResponse:
        """
        Search for leads

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
        CrmSearchLeadsResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_lead.crm_lead_search_leads(
            search_criteria={"key": "value"},
        )
        """
        _response = self._raw_client.crm_lead_search_leads(
            search_criteria=search_criteria,
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data


class AsyncCrmLeadClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCrmLeadClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCrmLeadClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCrmLeadClient
        """
        return self._raw_client

    async def crm_lead_get_lead(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetLeadResponse:
        """
        Get details of a lead

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetLeadResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_lead.crm_lead_get_lead(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_lead_get_lead(
            id, fields=fields, associations=associations, request_options=request_options
        )
        return _response.data

    async def crm_lead_update_lead(
        self,
        id: str,
        *,
        additional: typing.Any,
        first_name: str,
        last_name: str,
        phone: str,
        email: str,
        associations: typing.Optional[CommonLeadAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateLeadResponse:
        """
        Update a lead

        Parameters
        ----------
        id : str

        additional : typing.Any

        first_name : str
            The first name of the lead in a CRM.

        last_name : str
            The last name of the lead in a CRM.

        phone : str
            The phone number of the lead in a CRM.

        email : str
            The email of the lead in a CRM.

        associations : typing.Optional[CommonLeadAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateLeadResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_lead.crm_lead_update_lead(
                id="id",
                additional={"key": "value"},
                first_name="firstName",
                last_name="lastName",
                phone="phone",
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_lead_update_lead(
            id,
            additional=additional,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    async def crm_lead_get_leads(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetLeadsResponse:
        """
        Get all the leads

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetLeadsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_lead.crm_lead_get_leads()


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_lead_get_leads(
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    async def crm_lead_create_lead(
        self,
        *,
        additional: typing.Any,
        first_name: str,
        last_name: str,
        phone: str,
        email: str,
        associations: typing.Optional[CommonLeadAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateLeadResponse:
        """
        Create a new lead

        Parameters
        ----------
        additional : typing.Any

        first_name : str
            The first name of the lead in a CRM.

        last_name : str
            The last name of the lead in a CRM.

        phone : str
            The phone number of the lead in a CRM.

        email : str
            The email of the lead in a CRM.

        associations : typing.Optional[CommonLeadAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateLeadResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_lead.crm_lead_create_lead(
                additional={"key": "value"},
                first_name="firstName",
                last_name="lastName",
                phone="phone",
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_lead_create_lead(
            additional=additional,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    async def crm_lead_search_leads(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmSearchLeadsResponse:
        """
        Search for leads

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
        CrmSearchLeadsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_lead.crm_lead_search_leads(
                search_criteria={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_lead_search_leads(
            search_criteria=search_criteria,
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data
