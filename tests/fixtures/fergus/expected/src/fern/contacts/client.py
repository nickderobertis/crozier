

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.contact_by_id_response import ContactByIdResponse
from ..types.contact_item_payload import ContactItemPayload
from ..types.contacts_response import ContactsResponse
from .raw_client import AsyncRawContactsClient, RawContactsClient
from .types.create_contact_payload_contact_type import CreateContactPayloadContactType
from .types.get_contacts_request_filter_contact_type import GetContactsRequestFilterContactType
from .types.get_contacts_request_sort_field import GetContactsRequestSortField
from .types.get_contacts_request_sort_order import GetContactsRequestSortOrder


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

    def get_contacts(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetContactsRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetContactsRequestSortField] = None,
        filter_contact_type: typing.Optional[GetContactsRequestFilterContactType] = None,
        filter_customer_id: typing.Optional[float] = None,
        filter_site_id: typing.Optional[float] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactsResponse:
        """
        Returns a list of contacts. The list can be filtered by contact type.

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetContactsRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetContactsRequestSortField]

        filter_contact_type : typing.Optional[GetContactsRequestFilterContactType]

        filter_customer_id : typing.Optional[float]

        filter_site_id : typing.Optional[float]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `firstName`
            - `lastName`
            - `email`
            - `phoneNumber`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contacts.get_contacts()
        """
        _response = self._raw_client.get_contacts(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            filter_contact_type=filter_contact_type,
            filter_customer_id=filter_customer_id,
            filter_site_id=filter_site_id,
            filter_search_text=filter_search_text,
            request_options=request_options,
        )
        return _response.data

    def post_contacts(
        self,
        *,
        first_name: str,
        email: str,
        contact_type: CreateContactPayloadContactType,
        last_name: typing.Optional[str] = OMIT,
        position: typing.Optional[str] = OMIT,
        company: typing.Optional[str] = OMIT,
        contact_items: typing.Optional[typing.Sequence[ContactItemPayload]] = OMIT,
        is_main: typing.Optional[bool] = OMIT,
        is_billing: typing.Optional[bool] = OMIT,
        site_id: typing.Optional[float] = OMIT,
        customer_id: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactByIdResponse:
        """
        Creates a new contact for a customer or site.

          - **firstName** is required
          - **email** is required and must be a valid email address. This will be added as a contact item.
          - **contactType** is required and must be one of the following: `CUSTOMER`, `SITE`.
            - When **contactType** is `CUSTOMER`:
              - **customerId** is required
              - **isMain** cannot be set to true and is optional. To update the main contact, use the '/customers' endpoint.
              - **isBilling** is optional and defaults to false.
            - When **contactType** is `SITE`:
              - **siteId** is required
              - **isMain** is optional and defaults to false.
              - **isBilling** is optional and defaults to false.

        Parameters
        ----------
        first_name : str

        email : str

        contact_type : CreateContactPayloadContactType

        last_name : typing.Optional[str]

        position : typing.Optional[str]

        company : typing.Optional[str]

        contact_items : typing.Optional[typing.Sequence[ContactItemPayload]]

        is_main : typing.Optional[bool]

        is_billing : typing.Optional[bool]

        site_id : typing.Optional[float]

        customer_id : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactByIdResponse
            Resource created successfully

        Examples
        --------
        from fern.contacts import CreateContactPayloadContactType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contacts.post_contacts(
            first_name="firstName",
            email="email",
            contact_type=CreateContactPayloadContactType.CUSTOMER,
        )
        """
        _response = self._raw_client.post_contacts(
            first_name=first_name,
            email=email,
            contact_type=contact_type,
            last_name=last_name,
            position=position,
            company=company,
            contact_items=contact_items,
            is_main=is_main,
            is_billing=is_billing,
            site_id=site_id,
            customer_id=customer_id,
            request_options=request_options,
        )
        return _response.data

    def get_contacts_contact_id(
        self, contact_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContactByIdResponse:
        """
        Returns a contact by ID.

        Parameters
        ----------
        contact_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactByIdResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contacts.get_contacts_contact_id(
            contact_id=1.1,
        )
        """
        _response = self._raw_client.get_contacts_contact_id(contact_id, request_options=request_options)
        return _response.data

    def put_contacts_contact_id(
        self,
        contact_id: float,
        *,
        first_name: str,
        contact_items: typing.Sequence[ContactItemPayload],
        last_name: typing.Optional[str] = OMIT,
        position: typing.Optional[str] = OMIT,
        company: typing.Optional[str] = OMIT,
        is_main: typing.Optional[bool] = OMIT,
        is_billing: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactByIdResponse:
        """
        Updates a customer contact or site contact.

          - **firstName** is required
          - NOTE: To update the main contact of a `CUSTOMER`, please use the /customers endpoint.
            - When the contact to update is of type `CUSTOMER`:
              - **isMain** cannot be set to true and is optional. To update the main contact, use the '/customers' endpoint.
              - **isBilling** is optional and defaults to false.
          - NOTE: To unset the main contact of a `SITE` as non-main is not allowed, either use the create endpoint or update another contact of this site and set it as the main contact.
            - When the contact to update is of type `SITE`:
              - **isMain** is optional and defaults to false.
              - **isBilling** is optional and defaults to false.
              - If the contact to update is the main and billing contact of the `SITE`, the **isBilling** flag will have no impact and the contact details will be updated. If you want to change the contact that is assigned as the billing contact, please use the create method or update another contact of this site and set it as a billing contact.
          - **contactItems** at least one contact item of type email is required.
            - It will replace the existing contact items.
            - To update a specific contact item, you have to provide the id of the contact item to update. Otherwise, new contact items will be added.

        Parameters
        ----------
        contact_id : float

        first_name : str

        contact_items : typing.Sequence[ContactItemPayload]

        last_name : typing.Optional[str]

        position : typing.Optional[str]

        company : typing.Optional[str]

        is_main : typing.Optional[bool]

        is_billing : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactByIdResponse
            Successful Response

        Examples
        --------
        from fern import ContactItemPayload, ContactItemPayloadContactType, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contacts.put_contacts_contact_id(
            contact_id=1.1,
            first_name="firstName",
            contact_items=[
                ContactItemPayload(
                    contact_type=ContactItemPayloadContactType.EMAIL,
                    contact_value="contactValue",
                )
            ],
        )
        """
        _response = self._raw_client.put_contacts_contact_id(
            contact_id,
            first_name=first_name,
            contact_items=contact_items,
            last_name=last_name,
            position=position,
            company=company,
            is_main=is_main,
            is_billing=is_billing,
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

    async def get_contacts(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetContactsRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetContactsRequestSortField] = None,
        filter_contact_type: typing.Optional[GetContactsRequestFilterContactType] = None,
        filter_customer_id: typing.Optional[float] = None,
        filter_site_id: typing.Optional[float] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactsResponse:
        """
        Returns a list of contacts. The list can be filtered by contact type.

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetContactsRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetContactsRequestSortField]

        filter_contact_type : typing.Optional[GetContactsRequestFilterContactType]

        filter_customer_id : typing.Optional[float]

        filter_site_id : typing.Optional[float]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `firstName`
            - `lastName`
            - `email`
            - `phoneNumber`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contacts.get_contacts()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_contacts(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            filter_contact_type=filter_contact_type,
            filter_customer_id=filter_customer_id,
            filter_site_id=filter_site_id,
            filter_search_text=filter_search_text,
            request_options=request_options,
        )
        return _response.data

    async def post_contacts(
        self,
        *,
        first_name: str,
        email: str,
        contact_type: CreateContactPayloadContactType,
        last_name: typing.Optional[str] = OMIT,
        position: typing.Optional[str] = OMIT,
        company: typing.Optional[str] = OMIT,
        contact_items: typing.Optional[typing.Sequence[ContactItemPayload]] = OMIT,
        is_main: typing.Optional[bool] = OMIT,
        is_billing: typing.Optional[bool] = OMIT,
        site_id: typing.Optional[float] = OMIT,
        customer_id: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactByIdResponse:
        """
        Creates a new contact for a customer or site.

          - **firstName** is required
          - **email** is required and must be a valid email address. This will be added as a contact item.
          - **contactType** is required and must be one of the following: `CUSTOMER`, `SITE`.
            - When **contactType** is `CUSTOMER`:
              - **customerId** is required
              - **isMain** cannot be set to true and is optional. To update the main contact, use the '/customers' endpoint.
              - **isBilling** is optional and defaults to false.
            - When **contactType** is `SITE`:
              - **siteId** is required
              - **isMain** is optional and defaults to false.
              - **isBilling** is optional and defaults to false.

        Parameters
        ----------
        first_name : str

        email : str

        contact_type : CreateContactPayloadContactType

        last_name : typing.Optional[str]

        position : typing.Optional[str]

        company : typing.Optional[str]

        contact_items : typing.Optional[typing.Sequence[ContactItemPayload]]

        is_main : typing.Optional[bool]

        is_billing : typing.Optional[bool]

        site_id : typing.Optional[float]

        customer_id : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactByIdResponse
            Resource created successfully

        Examples
        --------
        import asyncio

        from fern.contacts import CreateContactPayloadContactType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contacts.post_contacts(
                first_name="firstName",
                email="email",
                contact_type=CreateContactPayloadContactType.CUSTOMER,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_contacts(
            first_name=first_name,
            email=email,
            contact_type=contact_type,
            last_name=last_name,
            position=position,
            company=company,
            contact_items=contact_items,
            is_main=is_main,
            is_billing=is_billing,
            site_id=site_id,
            customer_id=customer_id,
            request_options=request_options,
        )
        return _response.data

    async def get_contacts_contact_id(
        self, contact_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContactByIdResponse:
        """
        Returns a contact by ID.

        Parameters
        ----------
        contact_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactByIdResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contacts.get_contacts_contact_id(
                contact_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_contacts_contact_id(contact_id, request_options=request_options)
        return _response.data

    async def put_contacts_contact_id(
        self,
        contact_id: float,
        *,
        first_name: str,
        contact_items: typing.Sequence[ContactItemPayload],
        last_name: typing.Optional[str] = OMIT,
        position: typing.Optional[str] = OMIT,
        company: typing.Optional[str] = OMIT,
        is_main: typing.Optional[bool] = OMIT,
        is_billing: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactByIdResponse:
        """
        Updates a customer contact or site contact.

          - **firstName** is required
          - NOTE: To update the main contact of a `CUSTOMER`, please use the /customers endpoint.
            - When the contact to update is of type `CUSTOMER`:
              - **isMain** cannot be set to true and is optional. To update the main contact, use the '/customers' endpoint.
              - **isBilling** is optional and defaults to false.
          - NOTE: To unset the main contact of a `SITE` as non-main is not allowed, either use the create endpoint or update another contact of this site and set it as the main contact.
            - When the contact to update is of type `SITE`:
              - **isMain** is optional and defaults to false.
              - **isBilling** is optional and defaults to false.
              - If the contact to update is the main and billing contact of the `SITE`, the **isBilling** flag will have no impact and the contact details will be updated. If you want to change the contact that is assigned as the billing contact, please use the create method or update another contact of this site and set it as a billing contact.
          - **contactItems** at least one contact item of type email is required.
            - It will replace the existing contact items.
            - To update a specific contact item, you have to provide the id of the contact item to update. Otherwise, new contact items will be added.

        Parameters
        ----------
        contact_id : float

        first_name : str

        contact_items : typing.Sequence[ContactItemPayload]

        last_name : typing.Optional[str]

        position : typing.Optional[str]

        company : typing.Optional[str]

        is_main : typing.Optional[bool]

        is_billing : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactByIdResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ContactItemPayload, ContactItemPayloadContactType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contacts.put_contacts_contact_id(
                contact_id=1.1,
                first_name="firstName",
                contact_items=[
                    ContactItemPayload(
                        contact_type=ContactItemPayloadContactType.EMAIL,
                        contact_value="contactValue",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_contacts_contact_id(
            contact_id,
            first_name=first_name,
            contact_items=contact_items,
            last_name=last_name,
            position=position,
            company=company,
            is_main=is_main,
            is_billing=is_billing,
            request_options=request_options,
        )
        return _response.data
