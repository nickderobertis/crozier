

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.contact import Contact
from ..types.contact_id import ContactId
from ..types.contacts_page import ContactsPage
from ..types.organisation_id import OrganisationId
from .raw_client import AsyncRawContactsClient, RawContactsClient


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

    def get_the_contacts_for_the_given_organisation(
        self,
        organisation_id: OrganisationId,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactsPage:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        page : typing.Optional[int]
            The page number to return of the result set

        size : typing.Optional[int]
            The size of the pages to return

        sort : typing.Optional[str]
            The field name to sort

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactsPage
            Paged Contacts Snapshot

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )
        client.contacts.get_the_contacts_for_the_given_organisation(
            organisation_id="OrganisationId",
        )
        """
        _response = self._raw_client.get_the_contacts_for_the_given_organisation(
            organisation_id, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    def get_a_contact_by_id(
        self,
        organisation_id: OrganisationId,
        contact_id: ContactId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Contact:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        contact_id : ContactId
            The contact id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contact
            A contact object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )
        client.contacts.get_a_contact_by_id(
            organisation_id="OrganisationId",
            contact_id="ContactId",
        )
        """
        _response = self._raw_client.get_a_contact_by_id(organisation_id, contact_id, request_options=request_options)
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

    async def get_the_contacts_for_the_given_organisation(
        self,
        organisation_id: OrganisationId,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactsPage:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        page : typing.Optional[int]
            The page number to return of the result set

        size : typing.Optional[int]
            The size of the pages to return

        sort : typing.Optional[str]
            The field name to sort

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactsPage
            Paged Contacts Snapshot

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.contacts.get_the_contacts_for_the_given_organisation(
                organisation_id="OrganisationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_the_contacts_for_the_given_organisation(
            organisation_id, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    async def get_a_contact_by_id(
        self,
        organisation_id: OrganisationId,
        contact_id: ContactId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Contact:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        contact_id : ContactId
            The contact id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contact
            A contact object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.contacts.get_a_contact_by_id(
                organisation_id="OrganisationId",
                contact_id="ContactId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_contact_by_id(
            organisation_id, contact_id, request_options=request_options
        )
        return _response.data
