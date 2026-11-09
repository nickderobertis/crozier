

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.common_contact_association import CommonContactAssociation
from ..types.crm_create_or_update_contact_response import CrmCreateOrUpdateContactResponse
from ..types.crm_get_contact_response import CrmGetContactResponse
from ..types.crm_get_contacts_response import CrmGetContactsResponse
from ..types.crm_search_contacts_response import CrmSearchContactsResponse
from .raw_client import AsyncRawCrmContactClient, RawCrmContactClient


OMIT = typing.cast(typing.Any, ...)


class CrmContactClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCrmContactClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCrmContactClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCrmContactClient
        """
        return self._raw_client

    def crm_contact_get_contact(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetContactResponse:
        """
        Get details of a contact

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetContactResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_contact.crm_contact_get_contact(
            id="id",
        )
        """
        _response = self._raw_client.crm_contact_get_contact(
            id, fields=fields, associations=associations, request_options=request_options
        )
        return _response.data

    def crm_contact_update_contact(
        self,
        id: str,
        *,
        additional: typing.Any,
        first_name: str,
        last_name: str,
        phone: str,
        email: str,
        associations: typing.Optional[CommonContactAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateContactResponse:
        """
        Update a contact

        Parameters
        ----------
        id : str

        additional : typing.Any

        first_name : str
            The first name of the contact in a CRM.

        last_name : str
            The last name of the contact in a CRM.

        phone : str
            The phone number of the contact in a CRM.

        email : str
            The email of the contact in a CRM.

        associations : typing.Optional[CommonContactAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateContactResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_contact.crm_contact_update_contact(
            id="id",
            additional={"key": "value"},
            first_name="firstName",
            last_name="lastName",
            phone="phone",
            email="email",
        )
        """
        _response = self._raw_client.crm_contact_update_contact(
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

    def crm_contact_get_contacts(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetContactsResponse:
        """
        Get all the contacts

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
        CrmGetContactsResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_contact.crm_contact_get_contacts()
        """
        _response = self._raw_client.crm_contact_get_contacts(
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    def crm_contact_create_contact(
        self,
        *,
        additional: typing.Any,
        first_name: str,
        last_name: str,
        phone: str,
        email: str,
        associations: typing.Optional[CommonContactAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateContactResponse:
        """
        Create a new contact

        Parameters
        ----------
        additional : typing.Any

        first_name : str
            The first name of the contact in a CRM.

        last_name : str
            The last name of the contact in a CRM.

        phone : str
            The phone number of the contact in a CRM.

        email : str
            The email of the contact in a CRM.

        associations : typing.Optional[CommonContactAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateContactResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_contact.crm_contact_create_contact(
            additional={"key": "value"},
            first_name="firstName",
            last_name="lastName",
            phone="phone",
            email="email",
        )
        """
        _response = self._raw_client.crm_contact_create_contact(
            additional=additional,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    def crm_contact_search_contacts(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmSearchContactsResponse:
        """
        Search for contacts

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
        CrmSearchContactsResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_contact.crm_contact_search_contacts(
            search_criteria={"key": "value"},
        )
        """
        _response = self._raw_client.crm_contact_search_contacts(
            search_criteria=search_criteria,
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data


class AsyncCrmContactClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCrmContactClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCrmContactClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCrmContactClient
        """
        return self._raw_client

    async def crm_contact_get_contact(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetContactResponse:
        """
        Get details of a contact

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetContactResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_contact.crm_contact_get_contact(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_contact_get_contact(
            id, fields=fields, associations=associations, request_options=request_options
        )
        return _response.data

    async def crm_contact_update_contact(
        self,
        id: str,
        *,
        additional: typing.Any,
        first_name: str,
        last_name: str,
        phone: str,
        email: str,
        associations: typing.Optional[CommonContactAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateContactResponse:
        """
        Update a contact

        Parameters
        ----------
        id : str

        additional : typing.Any

        first_name : str
            The first name of the contact in a CRM.

        last_name : str
            The last name of the contact in a CRM.

        phone : str
            The phone number of the contact in a CRM.

        email : str
            The email of the contact in a CRM.

        associations : typing.Optional[CommonContactAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateContactResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_contact.crm_contact_update_contact(
                id="id",
                additional={"key": "value"},
                first_name="firstName",
                last_name="lastName",
                phone="phone",
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_contact_update_contact(
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

    async def crm_contact_get_contacts(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetContactsResponse:
        """
        Get all the contacts

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
        CrmGetContactsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_contact.crm_contact_get_contacts()


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_contact_get_contacts(
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    async def crm_contact_create_contact(
        self,
        *,
        additional: typing.Any,
        first_name: str,
        last_name: str,
        phone: str,
        email: str,
        associations: typing.Optional[CommonContactAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateContactResponse:
        """
        Create a new contact

        Parameters
        ----------
        additional : typing.Any

        first_name : str
            The first name of the contact in a CRM.

        last_name : str
            The last name of the contact in a CRM.

        phone : str
            The phone number of the contact in a CRM.

        email : str
            The email of the contact in a CRM.

        associations : typing.Optional[CommonContactAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateContactResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_contact.crm_contact_create_contact(
                additional={"key": "value"},
                first_name="firstName",
                last_name="lastName",
                phone="phone",
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_contact_create_contact(
            additional=additional,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    async def crm_contact_search_contacts(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmSearchContactsResponse:
        """
        Search for contacts

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
        CrmSearchContactsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_contact.crm_contact_search_contacts(
                search_criteria={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_contact_search_contacts(
            search_criteria=search_criteria,
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data
