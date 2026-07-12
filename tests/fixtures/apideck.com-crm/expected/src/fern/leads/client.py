

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
from ..types.create_lead_response import CreateLeadResponse
from ..types.currency import Currency
from ..types.custom_field import CustomField
from ..types.delete_lead_response import DeleteLeadResponse
from ..types.email import Email
from ..types.get_lead_response import GetLeadResponse
from ..types.get_leads_response import GetLeadsResponse
from ..types.leads_filter import LeadsFilter
from ..types.leads_sort import LeadsSort
from ..types.phone_number import PhoneNumber
from ..types.social_link import SocialLink
from ..types.tags import Tags
from ..types.update_lead_response import UpdateLeadResponse
from ..types.website import Website
from .raw_client import AsyncRawLeadsClient, RawLeadsClient


OMIT = typing.cast(typing.Any, ...)


class LeadsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLeadsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLeadsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLeadsClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[LeadsFilter] = None,
        sort: typing.Optional[LeadsSort] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetLeadsResponse:
        """
        List leads

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[LeadsFilter]
            Apply filters

        sort : typing.Optional[LeadsSort]
            Apply sorting

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLeadsResponse
            Leads

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.leads.all_(
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
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        description: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        lead_source: typing.Optional[str] = OMIT,
        monetary_amount: typing.Optional[float] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateLeadResponse:
        """
        Create lead

        Parameters
        ----------
        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        company_id : typing.Optional[str]

        company_name : typing.Optional[str]

        contact_id : typing.Optional[str]

        created_at : typing.Optional[str]

        currency : typing.Optional[Currency]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        description : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_name : typing.Optional[str]

        id : typing.Optional[str]

        language : typing.Optional[str]
            language code according to ISO 639-1. For the United States - EN

        last_name : typing.Optional[str]

        lead_source : typing.Optional[str]

        monetary_amount : typing.Optional[float]

        owner_id : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        prefix : typing.Optional[str]

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        tags : typing.Optional[Tags]

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateLeadResponse
            Lead created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.leads.add(
            name="Elon Musk",
        )
        """
        _response = self._raw_client.add(
            name=name,
            raw=raw,
            addresses=addresses,
            company_id=company_id,
            company_name=company_name,
            contact_id=contact_id,
            created_at=created_at,
            currency=currency,
            custom_fields=custom_fields,
            description=description,
            emails=emails,
            fax=fax,
            first_name=first_name,
            id=id,
            language=language,
            last_name=last_name,
            lead_source=lead_source,
            monetary_amount=monetary_amount,
            owner_id=owner_id,
            phone_numbers=phone_numbers,
            prefix=prefix,
            social_links=social_links,
            status=status,
            tags=tags,
            title=title,
            updated_at=updated_at,
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
    ) -> GetLeadResponse:
        """
        Get lead

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
        GetLeadResponse
            Lead

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.leads.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteLeadResponse:
        """
        Delete lead

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
        DeleteLeadResponse
            Lead deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.leads.delete(
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
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        description: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        lead_source: typing.Optional[str] = OMIT,
        monetary_amount: typing.Optional[float] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateLeadResponse:
        """
        Update lead

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        company_id : typing.Optional[str]

        company_name : typing.Optional[str]

        contact_id : typing.Optional[str]

        created_at : typing.Optional[str]

        currency : typing.Optional[Currency]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        description : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_name : typing.Optional[str]

        id : typing.Optional[str]

        language : typing.Optional[str]
            language code according to ISO 639-1. For the United States - EN

        last_name : typing.Optional[str]

        lead_source : typing.Optional[str]

        monetary_amount : typing.Optional[float]

        owner_id : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        prefix : typing.Optional[str]

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        tags : typing.Optional[Tags]

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateLeadResponse
            Lead updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.leads.update(
            id_="id",
            name="Elon Musk",
        )
        """
        _response = self._raw_client.update(
            id_,
            name=name,
            raw=raw,
            addresses=addresses,
            company_id=company_id,
            company_name=company_name,
            contact_id=contact_id,
            created_at=created_at,
            currency=currency,
            custom_fields=custom_fields,
            description=description,
            emails=emails,
            fax=fax,
            first_name=first_name,
            id=id,
            language=language,
            last_name=last_name,
            lead_source=lead_source,
            monetary_amount=monetary_amount,
            owner_id=owner_id,
            phone_numbers=phone_numbers,
            prefix=prefix,
            social_links=social_links,
            status=status,
            tags=tags,
            title=title,
            updated_at=updated_at,
            websites=websites,
            request_options=request_options,
        )
        return _response.data


class AsyncLeadsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLeadsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLeadsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLeadsClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[LeadsFilter] = None,
        sort: typing.Optional[LeadsSort] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetLeadsResponse:
        """
        List leads

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[LeadsFilter]
            Apply filters

        sort : typing.Optional[LeadsSort]
            Apply sorting

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLeadsResponse
            Leads

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
            await client.leads.all_(
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
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        description: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        lead_source: typing.Optional[str] = OMIT,
        monetary_amount: typing.Optional[float] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateLeadResponse:
        """
        Create lead

        Parameters
        ----------
        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        company_id : typing.Optional[str]

        company_name : typing.Optional[str]

        contact_id : typing.Optional[str]

        created_at : typing.Optional[str]

        currency : typing.Optional[Currency]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        description : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_name : typing.Optional[str]

        id : typing.Optional[str]

        language : typing.Optional[str]
            language code according to ISO 639-1. For the United States - EN

        last_name : typing.Optional[str]

        lead_source : typing.Optional[str]

        monetary_amount : typing.Optional[float]

        owner_id : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        prefix : typing.Optional[str]

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        tags : typing.Optional[Tags]

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateLeadResponse
            Lead created

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
            await client.leads.add(
                name="Elon Musk",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            name=name,
            raw=raw,
            addresses=addresses,
            company_id=company_id,
            company_name=company_name,
            contact_id=contact_id,
            created_at=created_at,
            currency=currency,
            custom_fields=custom_fields,
            description=description,
            emails=emails,
            fax=fax,
            first_name=first_name,
            id=id,
            language=language,
            last_name=last_name,
            lead_source=lead_source,
            monetary_amount=monetary_amount,
            owner_id=owner_id,
            phone_numbers=phone_numbers,
            prefix=prefix,
            social_links=social_links,
            status=status,
            tags=tags,
            title=title,
            updated_at=updated_at,
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
    ) -> GetLeadResponse:
        """
        Get lead

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
        GetLeadResponse
            Lead

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
            await client.leads.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteLeadResponse:
        """
        Delete lead

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
        DeleteLeadResponse
            Lead deleted

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
            await client.leads.delete(
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
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        description: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        lead_source: typing.Optional[str] = OMIT,
        monetary_amount: typing.Optional[float] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateLeadResponse:
        """
        Update lead

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        addresses : typing.Optional[typing.Sequence[Address]]

        company_id : typing.Optional[str]

        company_name : typing.Optional[str]

        contact_id : typing.Optional[str]

        created_at : typing.Optional[str]

        currency : typing.Optional[Currency]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        description : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_name : typing.Optional[str]

        id : typing.Optional[str]

        language : typing.Optional[str]
            language code according to ISO 639-1. For the United States - EN

        last_name : typing.Optional[str]

        lead_source : typing.Optional[str]

        monetary_amount : typing.Optional[float]

        owner_id : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        prefix : typing.Optional[str]

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        tags : typing.Optional[Tags]

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateLeadResponse
            Lead updated

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
            await client.leads.update(
                id_="id",
                name="Elon Musk",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_,
            name=name,
            raw=raw,
            addresses=addresses,
            company_id=company_id,
            company_name=company_name,
            contact_id=contact_id,
            created_at=created_at,
            currency=currency,
            custom_fields=custom_fields,
            description=description,
            emails=emails,
            fax=fax,
            first_name=first_name,
            id=id,
            language=language,
            last_name=last_name,
            lead_source=lead_source,
            monetary_amount=monetary_amount,
            owner_id=owner_id,
            phone_numbers=phone_numbers,
            prefix=prefix,
            social_links=social_links,
            status=status,
            tags=tags,
            title=title,
            updated_at=updated_at,
            websites=websites,
            request_options=request_options,
        )
        return _response.data
