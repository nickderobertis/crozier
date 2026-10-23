

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawManagementApiContactsClient, RawManagementApiContactsClient
from .types.create_contact_response import CreateContactResponse
from .types.upload_bulk_contacts_request_contacts_item import UploadBulkContactsRequestContactsItem
from .types.upload_bulk_contacts_response import UploadBulkContactsResponse


OMIT = typing.cast(typing.Any, ...)


class ManagementApiContactsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawManagementApiContactsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawManagementApiContactsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawManagementApiContactsClient
        """
        return self._raw_client

    def upload_bulk_contacts(
        self,
        *,
        workspace_id: str,
        contacts: typing.Sequence[UploadBulkContactsRequestContactsItem],
        environment_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadBulkContactsResponse:
        """
        Uploads contacts in bulk. This endpoint expects the bulk request shape: `contacts` must be an array, and each contact item must contain an `attributes` array of `{ attributeKey, value }` objects. Unlike `POST /management/contacts`, this endpoint does not accept a top-level `attributes` object. Each contact must include an `email` attribute in its `attributes` array, and that email must be valid. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        workspace_id : str

        contacts : typing.Sequence[UploadBulkContactsRequestContactsItem]

        environment_id : typing.Optional[str]
            Deprecated alias for workspaceId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadBulkContactsResponse
            Contacts uploaded successfully.

        Examples
        --------
        from fern.management_api_contacts import (
            UploadBulkContactsRequestContactsItem,
            UploadBulkContactsRequestContactsItemAttributesItem,
            UploadBulkContactsRequestContactsItemAttributesItemAttributeKey,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.management_api_contacts.upload_bulk_contacts(
            workspace_id="ws_01h2xce9q8p3w4x5y6z7a8b9c0",
            contacts=[
                UploadBulkContactsRequestContactsItem(
                    attributes=[
                        UploadBulkContactsRequestContactsItemAttributesItem(
                            attribute_key=UploadBulkContactsRequestContactsItemAttributesItemAttributeKey(
                                key="email",
                                name="Email Address",
                            ),
                            value="john.doe@example.com",
                        ),
                        UploadBulkContactsRequestContactsItemAttributesItem(
                            attribute_key=UploadBulkContactsRequestContactsItemAttributesItemAttributeKey(
                                key="firstName",
                                name="First Name",
                            ),
                            value="John",
                        ),
                        UploadBulkContactsRequestContactsItemAttributesItem(
                            attribute_key=UploadBulkContactsRequestContactsItemAttributesItemAttributeKey(
                                key="lastName",
                                name="Last Name",
                            ),
                            value="Doe",
                        ),
                    ],
                ),
                UploadBulkContactsRequestContactsItem(
                    attributes=[
                        UploadBulkContactsRequestContactsItemAttributesItem(
                            attribute_key=UploadBulkContactsRequestContactsItemAttributesItemAttributeKey(
                                key="email",
                                name="Email Address",
                            ),
                            value="jane.smith@example.com",
                        ),
                        UploadBulkContactsRequestContactsItemAttributesItem(
                            attribute_key=UploadBulkContactsRequestContactsItemAttributesItemAttributeKey(
                                key="firstName",
                                name="First Name",
                            ),
                            value="Jane",
                        ),
                        UploadBulkContactsRequestContactsItemAttributesItem(
                            attribute_key=UploadBulkContactsRequestContactsItemAttributesItemAttributeKey(
                                key="lastName",
                                name="Last Name",
                            ),
                            value="Smith",
                        ),
                    ],
                ),
            ],
        )
        """
        _response = self._raw_client.upload_bulk_contacts(
            workspace_id=workspace_id, contacts=contacts, environment_id=environment_id, request_options=request_options
        )
        return _response.data

    def create_contact(
        self,
        *,
        workspace_id: str,
        attributes: typing.Dict[str, str],
        environment_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateContactResponse:
        """
        Creates a single contact in the database. This endpoint expects a top-level `attributes` object. For bulk uploads, use `PUT /management/contacts/bulk`, which expects `contacts[].attributes[]` instead. Each contact must have a valid email address in the attributes. All attribute keys must already exist in the Workspace. The email is used as the unique identifier along with the Workspace. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        workspace_id : str

        attributes : typing.Dict[str, str]

        environment_id : typing.Optional[str]
            Deprecated alias for workspaceId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateContactResponse
            Contact created successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.management_api_contacts.create_contact(
            workspace_id="ws_01h2xce9q8p3w4x5y6z7a8b9c0",
            attributes={
                "email": "john.doe@example.com",
                "firstName": "John",
                "lastName": "Doe",
                "userId": "h2xce9q8p3w4x5y6z7a8b9c1",
            },
        )
        """
        _response = self._raw_client.create_contact(
            workspace_id=workspace_id,
            attributes=attributes,
            environment_id=environment_id,
            request_options=request_options,
        )
        return _response.data


class AsyncManagementApiContactsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawManagementApiContactsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawManagementApiContactsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawManagementApiContactsClient
        """
        return self._raw_client

    async def upload_bulk_contacts(
        self,
        *,
        workspace_id: str,
        contacts: typing.Sequence[UploadBulkContactsRequestContactsItem],
        environment_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadBulkContactsResponse:
        """
        Uploads contacts in bulk. This endpoint expects the bulk request shape: `contacts` must be an array, and each contact item must contain an `attributes` array of `{ attributeKey, value }` objects. Unlike `POST /management/contacts`, this endpoint does not accept a top-level `attributes` object. Each contact must include an `email` attribute in its `attributes` array, and that email must be valid. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        workspace_id : str

        contacts : typing.Sequence[UploadBulkContactsRequestContactsItem]

        environment_id : typing.Optional[str]
            Deprecated alias for workspaceId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadBulkContactsResponse
            Contacts uploaded successfully.

        Examples
        --------
        import asyncio

        from fern.management_api_contacts import (
            UploadBulkContactsRequestContactsItem,
            UploadBulkContactsRequestContactsItemAttributesItem,
            UploadBulkContactsRequestContactsItemAttributesItemAttributeKey,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.management_api_contacts.upload_bulk_contacts(
                workspace_id="ws_01h2xce9q8p3w4x5y6z7a8b9c0",
                contacts=[
                    UploadBulkContactsRequestContactsItem(
                        attributes=[
                            UploadBulkContactsRequestContactsItemAttributesItem(
                                attribute_key=UploadBulkContactsRequestContactsItemAttributesItemAttributeKey(
                                    key="email",
                                    name="Email Address",
                                ),
                                value="john.doe@example.com",
                            ),
                            UploadBulkContactsRequestContactsItemAttributesItem(
                                attribute_key=UploadBulkContactsRequestContactsItemAttributesItemAttributeKey(
                                    key="firstName",
                                    name="First Name",
                                ),
                                value="John",
                            ),
                            UploadBulkContactsRequestContactsItemAttributesItem(
                                attribute_key=UploadBulkContactsRequestContactsItemAttributesItemAttributeKey(
                                    key="lastName",
                                    name="Last Name",
                                ),
                                value="Doe",
                            ),
                        ],
                    ),
                    UploadBulkContactsRequestContactsItem(
                        attributes=[
                            UploadBulkContactsRequestContactsItemAttributesItem(
                                attribute_key=UploadBulkContactsRequestContactsItemAttributesItemAttributeKey(
                                    key="email",
                                    name="Email Address",
                                ),
                                value="jane.smith@example.com",
                            ),
                            UploadBulkContactsRequestContactsItemAttributesItem(
                                attribute_key=UploadBulkContactsRequestContactsItemAttributesItemAttributeKey(
                                    key="firstName",
                                    name="First Name",
                                ),
                                value="Jane",
                            ),
                            UploadBulkContactsRequestContactsItemAttributesItem(
                                attribute_key=UploadBulkContactsRequestContactsItemAttributesItemAttributeKey(
                                    key="lastName",
                                    name="Last Name",
                                ),
                                value="Smith",
                            ),
                        ],
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_bulk_contacts(
            workspace_id=workspace_id, contacts=contacts, environment_id=environment_id, request_options=request_options
        )
        return _response.data

    async def create_contact(
        self,
        *,
        workspace_id: str,
        attributes: typing.Dict[str, str],
        environment_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateContactResponse:
        """
        Creates a single contact in the database. This endpoint expects a top-level `attributes` object. For bulk uploads, use `PUT /management/contacts/bulk`, which expects `contacts[].attributes[]` instead. Each contact must have a valid email address in the attributes. All attribute keys must already exist in the Workspace. The email is used as the unique identifier along with the Workspace. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        workspace_id : str

        attributes : typing.Dict[str, str]

        environment_id : typing.Optional[str]
            Deprecated alias for workspaceId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateContactResponse
            Contact created successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.management_api_contacts.create_contact(
                workspace_id="ws_01h2xce9q8p3w4x5y6z7a8b9c0",
                attributes={
                    "email": "john.doe@example.com",
                    "firstName": "John",
                    "lastName": "Doe",
                    "userId": "h2xce9q8p3w4x5y6z7a8b9c1",
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_contact(
            workspace_id=workspace_id,
            attributes=attributes,
            environment_id=environment_id,
            request_options=request_options,
        )
        return _response.data
