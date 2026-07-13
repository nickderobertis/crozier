

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
from ..types.contact_gender import ContactGender
from ..types.contact_type import ContactType
from ..types.contacts_filter import ContactsFilter
from ..types.contacts_sort import ContactsSort
from ..types.create_contact_response import CreateContactResponse
from ..types.custom_field import CustomField
from ..types.delete_contact_response import DeleteContactResponse
from ..types.email import Email
from ..types.get_contact_response import GetContactResponse
from ..types.get_contacts_response import GetContactsResponse
from ..types.phone_number import PhoneNumber
from ..types.social_link import SocialLink
from ..types.tags import Tags
from ..types.update_contact_response import UpdateContactResponse
from ..types.website import Website
from .raw_client import AsyncRawContactsClient, RawContactsClient


OMIT = typing.cast(typing.Any, ...)


class ContactsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContactsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContactsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContactsClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[ContactsFilter] = None,
        sort: typing.Optional[ContactsSort] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetContactsResponse:
        """
        List contacts

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[ContactsFilter]
            Apply filters

        sort : typing.Optional[ContactsSort]
            Apply sorting

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetContactsResponse
            Contacts

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.contacts.all_(
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
        active: typing.Optional[bool] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        birthday: typing.Optional[str] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        current_balance: typing.Optional[float] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        department: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        email_domain: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_call_at: typing.Optional[dt.datetime] = OMIT,
        first_email_at: typing.Optional[dt.datetime] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        gender: typing.Optional[ContactGender] = OMIT,
        id: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_activity_at: typing.Optional[dt.datetime] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        lead_source: typing.Optional[str] = OMIT,
        middle_name: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        photo_url: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        suffix: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        title: typing.Optional[str] = OMIT,
        type: typing.Optional[ContactType] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateContactResponse:
        """
        Create contact

        Parameters
        ----------
        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]

        addresses : typing.Optional[typing.Sequence[Address]]

        birthday : typing.Optional[str]

        company_id : typing.Optional[str]

        company_name : typing.Optional[str]

        created_at : typing.Optional[dt.datetime]

        current_balance : typing.Optional[float]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        department : typing.Optional[str]

        description : typing.Optional[str]

        email_domain : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_call_at : typing.Optional[dt.datetime]

        first_email_at : typing.Optional[dt.datetime]

        first_name : typing.Optional[str]

        gender : typing.Optional[ContactGender]

        id : typing.Optional[str]

        image : typing.Optional[str]

        language : typing.Optional[str]
            language code according to ISO 639-1. For the United States - EN

        last_activity_at : typing.Optional[dt.datetime]

        last_name : typing.Optional[str]

        lead_id : typing.Optional[str]

        lead_source : typing.Optional[str]

        middle_name : typing.Optional[str]

        owner_id : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        photo_url : typing.Optional[str]
            The URL of the photo of a person.

        prefix : typing.Optional[str]

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        suffix : typing.Optional[str]

        tags : typing.Optional[Tags]

        title : typing.Optional[str]

        type : typing.Optional[ContactType]

        updated_at : typing.Optional[dt.datetime]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateContactResponse
            Contact created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.contacts.add(
            name="Elon Musk",
        )
        """
        _response = self._raw_client.add(
            name=name,
            raw=raw,
            active=active,
            addresses=addresses,
            birthday=birthday,
            company_id=company_id,
            company_name=company_name,
            created_at=created_at,
            current_balance=current_balance,
            custom_fields=custom_fields,
            department=department,
            description=description,
            email_domain=email_domain,
            emails=emails,
            fax=fax,
            first_call_at=first_call_at,
            first_email_at=first_email_at,
            first_name=first_name,
            gender=gender,
            id=id,
            image=image,
            language=language,
            last_activity_at=last_activity_at,
            last_name=last_name,
            lead_id=lead_id,
            lead_source=lead_source,
            middle_name=middle_name,
            owner_id=owner_id,
            phone_numbers=phone_numbers,
            photo_url=photo_url,
            prefix=prefix,
            social_links=social_links,
            status=status,
            suffix=suffix,
            tags=tags,
            title=title,
            type=type,
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
    ) -> GetContactResponse:
        """
        Get contact

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
        GetContactResponse
            Contact

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.contacts.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteContactResponse:
        """
        Delete contact

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
        DeleteContactResponse
            Contact deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.contacts.delete(
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
        active: typing.Optional[bool] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        birthday: typing.Optional[str] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        current_balance: typing.Optional[float] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        department: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        email_domain: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_call_at: typing.Optional[dt.datetime] = OMIT,
        first_email_at: typing.Optional[dt.datetime] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        gender: typing.Optional[ContactGender] = OMIT,
        id: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_activity_at: typing.Optional[dt.datetime] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        lead_source: typing.Optional[str] = OMIT,
        middle_name: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        photo_url: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        suffix: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        title: typing.Optional[str] = OMIT,
        type: typing.Optional[ContactType] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateContactResponse:
        """
        Update contact

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]

        addresses : typing.Optional[typing.Sequence[Address]]

        birthday : typing.Optional[str]

        company_id : typing.Optional[str]

        company_name : typing.Optional[str]

        created_at : typing.Optional[dt.datetime]

        current_balance : typing.Optional[float]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        department : typing.Optional[str]

        description : typing.Optional[str]

        email_domain : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_call_at : typing.Optional[dt.datetime]

        first_email_at : typing.Optional[dt.datetime]

        first_name : typing.Optional[str]

        gender : typing.Optional[ContactGender]

        id : typing.Optional[str]

        image : typing.Optional[str]

        language : typing.Optional[str]
            language code according to ISO 639-1. For the United States - EN

        last_activity_at : typing.Optional[dt.datetime]

        last_name : typing.Optional[str]

        lead_id : typing.Optional[str]

        lead_source : typing.Optional[str]

        middle_name : typing.Optional[str]

        owner_id : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        photo_url : typing.Optional[str]
            The URL of the photo of a person.

        prefix : typing.Optional[str]

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        suffix : typing.Optional[str]

        tags : typing.Optional[Tags]

        title : typing.Optional[str]

        type : typing.Optional[ContactType]

        updated_at : typing.Optional[dt.datetime]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateContactResponse
            Contact updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.contacts.update(
            id_="id",
            name="Elon Musk",
        )
        """
        _response = self._raw_client.update(
            id_,
            name=name,
            raw=raw,
            active=active,
            addresses=addresses,
            birthday=birthday,
            company_id=company_id,
            company_name=company_name,
            created_at=created_at,
            current_balance=current_balance,
            custom_fields=custom_fields,
            department=department,
            description=description,
            email_domain=email_domain,
            emails=emails,
            fax=fax,
            first_call_at=first_call_at,
            first_email_at=first_email_at,
            first_name=first_name,
            gender=gender,
            id=id,
            image=image,
            language=language,
            last_activity_at=last_activity_at,
            last_name=last_name,
            lead_id=lead_id,
            lead_source=lead_source,
            middle_name=middle_name,
            owner_id=owner_id,
            phone_numbers=phone_numbers,
            photo_url=photo_url,
            prefix=prefix,
            social_links=social_links,
            status=status,
            suffix=suffix,
            tags=tags,
            title=title,
            type=type,
            updated_at=updated_at,
            websites=websites,
            request_options=request_options,
        )
        return _response.data


class AsyncContactsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContactsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContactsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContactsClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[ContactsFilter] = None,
        sort: typing.Optional[ContactsSort] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetContactsResponse:
        """
        List contacts

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[ContactsFilter]
            Apply filters

        sort : typing.Optional[ContactsSort]
            Apply sorting

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetContactsResponse
            Contacts

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
            await client.contacts.all_(
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
        active: typing.Optional[bool] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        birthday: typing.Optional[str] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        current_balance: typing.Optional[float] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        department: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        email_domain: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_call_at: typing.Optional[dt.datetime] = OMIT,
        first_email_at: typing.Optional[dt.datetime] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        gender: typing.Optional[ContactGender] = OMIT,
        id: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_activity_at: typing.Optional[dt.datetime] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        lead_source: typing.Optional[str] = OMIT,
        middle_name: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        photo_url: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        suffix: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        title: typing.Optional[str] = OMIT,
        type: typing.Optional[ContactType] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateContactResponse:
        """
        Create contact

        Parameters
        ----------
        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]

        addresses : typing.Optional[typing.Sequence[Address]]

        birthday : typing.Optional[str]

        company_id : typing.Optional[str]

        company_name : typing.Optional[str]

        created_at : typing.Optional[dt.datetime]

        current_balance : typing.Optional[float]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        department : typing.Optional[str]

        description : typing.Optional[str]

        email_domain : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_call_at : typing.Optional[dt.datetime]

        first_email_at : typing.Optional[dt.datetime]

        first_name : typing.Optional[str]

        gender : typing.Optional[ContactGender]

        id : typing.Optional[str]

        image : typing.Optional[str]

        language : typing.Optional[str]
            language code according to ISO 639-1. For the United States - EN

        last_activity_at : typing.Optional[dt.datetime]

        last_name : typing.Optional[str]

        lead_id : typing.Optional[str]

        lead_source : typing.Optional[str]

        middle_name : typing.Optional[str]

        owner_id : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        photo_url : typing.Optional[str]
            The URL of the photo of a person.

        prefix : typing.Optional[str]

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        suffix : typing.Optional[str]

        tags : typing.Optional[Tags]

        title : typing.Optional[str]

        type : typing.Optional[ContactType]

        updated_at : typing.Optional[dt.datetime]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateContactResponse
            Contact created

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
            await client.contacts.add(
                name="Elon Musk",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            name=name,
            raw=raw,
            active=active,
            addresses=addresses,
            birthday=birthday,
            company_id=company_id,
            company_name=company_name,
            created_at=created_at,
            current_balance=current_balance,
            custom_fields=custom_fields,
            department=department,
            description=description,
            email_domain=email_domain,
            emails=emails,
            fax=fax,
            first_call_at=first_call_at,
            first_email_at=first_email_at,
            first_name=first_name,
            gender=gender,
            id=id,
            image=image,
            language=language,
            last_activity_at=last_activity_at,
            last_name=last_name,
            lead_id=lead_id,
            lead_source=lead_source,
            middle_name=middle_name,
            owner_id=owner_id,
            phone_numbers=phone_numbers,
            photo_url=photo_url,
            prefix=prefix,
            social_links=social_links,
            status=status,
            suffix=suffix,
            tags=tags,
            title=title,
            type=type,
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
    ) -> GetContactResponse:
        """
        Get contact

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
        GetContactResponse
            Contact

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
            await client.contacts.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteContactResponse:
        """
        Delete contact

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
        DeleteContactResponse
            Contact deleted

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
            await client.contacts.delete(
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
        active: typing.Optional[bool] = OMIT,
        addresses: typing.Optional[typing.Sequence[Address]] = OMIT,
        birthday: typing.Optional[str] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        company_name: typing.Optional[str] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        current_balance: typing.Optional[float] = OMIT,
        custom_fields: typing.Optional[typing.Sequence[CustomField]] = OMIT,
        department: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        email_domain: typing.Optional[str] = OMIT,
        emails: typing.Optional[typing.Sequence[Email]] = OMIT,
        fax: typing.Optional[str] = OMIT,
        first_call_at: typing.Optional[dt.datetime] = OMIT,
        first_email_at: typing.Optional[dt.datetime] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        gender: typing.Optional[ContactGender] = OMIT,
        id: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        last_activity_at: typing.Optional[dt.datetime] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        lead_source: typing.Optional[str] = OMIT,
        middle_name: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        phone_numbers: typing.Optional[typing.Sequence[PhoneNumber]] = OMIT,
        photo_url: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        social_links: typing.Optional[typing.Sequence[SocialLink]] = OMIT,
        status: typing.Optional[str] = OMIT,
        suffix: typing.Optional[str] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        title: typing.Optional[str] = OMIT,
        type: typing.Optional[ContactType] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        websites: typing.Optional[typing.Sequence[Website]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateContactResponse:
        """
        Update contact

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        name : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]

        addresses : typing.Optional[typing.Sequence[Address]]

        birthday : typing.Optional[str]

        company_id : typing.Optional[str]

        company_name : typing.Optional[str]

        created_at : typing.Optional[dt.datetime]

        current_balance : typing.Optional[float]

        custom_fields : typing.Optional[typing.Sequence[CustomField]]

        department : typing.Optional[str]

        description : typing.Optional[str]

        email_domain : typing.Optional[str]

        emails : typing.Optional[typing.Sequence[Email]]

        fax : typing.Optional[str]

        first_call_at : typing.Optional[dt.datetime]

        first_email_at : typing.Optional[dt.datetime]

        first_name : typing.Optional[str]

        gender : typing.Optional[ContactGender]

        id : typing.Optional[str]

        image : typing.Optional[str]

        language : typing.Optional[str]
            language code according to ISO 639-1. For the United States - EN

        last_activity_at : typing.Optional[dt.datetime]

        last_name : typing.Optional[str]

        lead_id : typing.Optional[str]

        lead_source : typing.Optional[str]

        middle_name : typing.Optional[str]

        owner_id : typing.Optional[str]

        phone_numbers : typing.Optional[typing.Sequence[PhoneNumber]]

        photo_url : typing.Optional[str]
            The URL of the photo of a person.

        prefix : typing.Optional[str]

        social_links : typing.Optional[typing.Sequence[SocialLink]]

        status : typing.Optional[str]

        suffix : typing.Optional[str]

        tags : typing.Optional[Tags]

        title : typing.Optional[str]

        type : typing.Optional[ContactType]

        updated_at : typing.Optional[dt.datetime]

        websites : typing.Optional[typing.Sequence[Website]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateContactResponse
            Contact updated

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
            await client.contacts.update(
                id_="id",
                name="Elon Musk",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_,
            name=name,
            raw=raw,
            active=active,
            addresses=addresses,
            birthday=birthday,
            company_id=company_id,
            company_name=company_name,
            created_at=created_at,
            current_balance=current_balance,
            custom_fields=custom_fields,
            department=department,
            description=description,
            email_domain=email_domain,
            emails=emails,
            fax=fax,
            first_call_at=first_call_at,
            first_email_at=first_email_at,
            first_name=first_name,
            gender=gender,
            id=id,
            image=image,
            language=language,
            last_activity_at=last_activity_at,
            last_name=last_name,
            lead_id=lead_id,
            lead_source=lead_source,
            middle_name=middle_name,
            owner_id=owner_id,
            phone_numbers=phone_numbers,
            photo_url=photo_url,
            prefix=prefix,
            social_links=social_links,
            status=status,
            suffix=suffix,
            tags=tags,
            title=title,
            type=type,
            updated_at=updated_at,
            websites=websites,
            request_options=request_options,
        )
        return _response.data
