

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.contact_attribute_key_id import ContactAttributeKeyId
from .raw_client import AsyncRawManagementApiContactAttributeKeysClient, RawManagementApiContactAttributeKeysClient
from .types.create_contact_attribute_key_response import CreateContactAttributeKeyResponse
from .types.delete_contact_attribute_key_response import DeleteContactAttributeKeyResponse
from .types.get_contact_attribute_key_response import GetContactAttributeKeyResponse
from .types.get_contact_attribute_keys_request_filter_date_field import GetContactAttributeKeysRequestFilterDateField
from .types.get_contact_attribute_keys_request_order import GetContactAttributeKeysRequestOrder
from .types.get_contact_attribute_keys_request_sort_by import GetContactAttributeKeysRequestSortBy
from .types.get_contact_attribute_keys_response import GetContactAttributeKeysResponse
from .types.update_contact_attribute_key_response import UpdateContactAttributeKeyResponse


OMIT = typing.cast(typing.Any, ...)


class ManagementApiContactAttributeKeysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawManagementApiContactAttributeKeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawManagementApiContactAttributeKeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawManagementApiContactAttributeKeysClient
        """
        return self._raw_client

    def get_contact_attribute_keys(
        self,
        *,
        limit: typing.Optional[float] = None,
        skip: typing.Optional[float] = None,
        sort_by: typing.Optional[GetContactAttributeKeysRequestSortBy] = None,
        order: typing.Optional[GetContactAttributeKeysRequestOrder] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter_date_field: typing.Optional[GetContactAttributeKeysRequestFilterDateField] = None,
        workspace_id: typing.Optional[str] = None,
        environment_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetContactAttributeKeysResponse:
        """
        Gets contact attribute keys from the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        limit : typing.Optional[float]
            Number of items to return

        skip : typing.Optional[float]
            Number of items to skip

        sort_by : typing.Optional[GetContactAttributeKeysRequestSortBy]
            Sort by field

        order : typing.Optional[GetContactAttributeKeysRequestOrder]
            Sort order

        start_date : typing.Optional[str]
            Start date

        end_date : typing.Optional[str]
            End date

        filter_date_field : typing.Optional[GetContactAttributeKeysRequestFilterDateField]
            Date field to filter by

        workspace_id : typing.Optional[str]
            The Workspace ID to filter by

        environment_id : typing.Optional[str]
            Deprecated alias for workspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetContactAttributeKeysResponse
            Contact attribute keys retrieved successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.management_api_contact_attribute_keys.get_contact_attribute_keys()
        """
        _response = self._raw_client.get_contact_attribute_keys(
            limit=limit,
            skip=skip,
            sort_by=sort_by,
            order=order,
            start_date=start_date,
            end_date=end_date,
            filter_date_field=filter_date_field,
            workspace_id=workspace_id,
            environment_id=environment_id,
            request_options=request_options,
        )
        return _response.data

    def create_contact_attribute_key(
        self,
        *,
        key: str,
        workspace_id: str,
        environment_id: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateContactAttributeKeyResponse:
        """
        Creates a contact attribute key in the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        key : str
            The attribute identifier used in the system

        workspace_id : str
            The ID of the Workspace this attribute belongs to

        environment_id : str
            Deprecated alias for workspaceId.

        name : typing.Optional[str]
            Display name for the attribute

        description : typing.Optional[str]
            Description of the attribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateContactAttributeKeyResponse
            Contact attribute key created successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.management_api_contact_attribute_keys.create_contact_attribute_key(
            key="email",
            name="Email Address",
            description="The user's email address",
            workspace_id="workspaceId",
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.create_contact_attribute_key(
            key=key,
            workspace_id=workspace_id,
            environment_id=environment_id,
            name=name,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def get_contact_attribute_key(
        self, id: ContactAttributeKeyId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetContactAttributeKeyResponse:
        """
        Gets a contact attribute key from the database.

        Parameters
        ----------
        id : ContactAttributeKeyId
            The ID of the contact attribute key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetContactAttributeKeyResponse
            Contact attribute key retrieved successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.management_api_contact_attribute_keys.get_contact_attribute_key(
            id="id",
        )
        """
        _response = self._raw_client.get_contact_attribute_key(id, request_options=request_options)
        return _response.data

    def update_contact_attribute_key(
        self,
        id: ContactAttributeKeyId,
        *,
        key: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateContactAttributeKeyResponse:
        """
        Updates a contact attribute key in the database.

        Parameters
        ----------
        id : ContactAttributeKeyId
            The ID of the contact attribute key

        key : str
            The attribute identifier used in the system

        name : typing.Optional[str]
            Display name for the attribute

        description : typing.Optional[str]
            Description of the attribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateContactAttributeKeyResponse
            Contact attribute key updated successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.management_api_contact_attribute_keys.update_contact_attribute_key(
            id="id",
            name="Email Address",
            description="The user's email address",
            key="email",
        )
        """
        _response = self._raw_client.update_contact_attribute_key(
            id, key=key, name=name, description=description, request_options=request_options
        )
        return _response.data

    def delete_contact_attribute_key(
        self, id: ContactAttributeKeyId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteContactAttributeKeyResponse:
        """
        Deletes a contact attribute key from the database.

        Parameters
        ----------
        id : ContactAttributeKeyId
            The ID of the contact attribute key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteContactAttributeKeyResponse
            Contact attribute key deleted successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.management_api_contact_attribute_keys.delete_contact_attribute_key(
            id="id",
        )
        """
        _response = self._raw_client.delete_contact_attribute_key(id, request_options=request_options)
        return _response.data


class AsyncManagementApiContactAttributeKeysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawManagementApiContactAttributeKeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawManagementApiContactAttributeKeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawManagementApiContactAttributeKeysClient
        """
        return self._raw_client

    async def get_contact_attribute_keys(
        self,
        *,
        limit: typing.Optional[float] = None,
        skip: typing.Optional[float] = None,
        sort_by: typing.Optional[GetContactAttributeKeysRequestSortBy] = None,
        order: typing.Optional[GetContactAttributeKeysRequestOrder] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter_date_field: typing.Optional[GetContactAttributeKeysRequestFilterDateField] = None,
        workspace_id: typing.Optional[str] = None,
        environment_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetContactAttributeKeysResponse:
        """
        Gets contact attribute keys from the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        limit : typing.Optional[float]
            Number of items to return

        skip : typing.Optional[float]
            Number of items to skip

        sort_by : typing.Optional[GetContactAttributeKeysRequestSortBy]
            Sort by field

        order : typing.Optional[GetContactAttributeKeysRequestOrder]
            Sort order

        start_date : typing.Optional[str]
            Start date

        end_date : typing.Optional[str]
            End date

        filter_date_field : typing.Optional[GetContactAttributeKeysRequestFilterDateField]
            Date field to filter by

        workspace_id : typing.Optional[str]
            The Workspace ID to filter by

        environment_id : typing.Optional[str]
            Deprecated alias for workspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetContactAttributeKeysResponse
            Contact attribute keys retrieved successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.management_api_contact_attribute_keys.get_contact_attribute_keys()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_contact_attribute_keys(
            limit=limit,
            skip=skip,
            sort_by=sort_by,
            order=order,
            start_date=start_date,
            end_date=end_date,
            filter_date_field=filter_date_field,
            workspace_id=workspace_id,
            environment_id=environment_id,
            request_options=request_options,
        )
        return _response.data

    async def create_contact_attribute_key(
        self,
        *,
        key: str,
        workspace_id: str,
        environment_id: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateContactAttributeKeyResponse:
        """
        Creates a contact attribute key in the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        key : str
            The attribute identifier used in the system

        workspace_id : str
            The ID of the Workspace this attribute belongs to

        environment_id : str
            Deprecated alias for workspaceId.

        name : typing.Optional[str]
            Display name for the attribute

        description : typing.Optional[str]
            Description of the attribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateContactAttributeKeyResponse
            Contact attribute key created successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.management_api_contact_attribute_keys.create_contact_attribute_key(
                key="email",
                name="Email Address",
                description="The user's email address",
                workspace_id="workspaceId",
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_contact_attribute_key(
            key=key,
            workspace_id=workspace_id,
            environment_id=environment_id,
            name=name,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def get_contact_attribute_key(
        self, id: ContactAttributeKeyId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetContactAttributeKeyResponse:
        """
        Gets a contact attribute key from the database.

        Parameters
        ----------
        id : ContactAttributeKeyId
            The ID of the contact attribute key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetContactAttributeKeyResponse
            Contact attribute key retrieved successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.management_api_contact_attribute_keys.get_contact_attribute_key(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_contact_attribute_key(id, request_options=request_options)
        return _response.data

    async def update_contact_attribute_key(
        self,
        id: ContactAttributeKeyId,
        *,
        key: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateContactAttributeKeyResponse:
        """
        Updates a contact attribute key in the database.

        Parameters
        ----------
        id : ContactAttributeKeyId
            The ID of the contact attribute key

        key : str
            The attribute identifier used in the system

        name : typing.Optional[str]
            Display name for the attribute

        description : typing.Optional[str]
            Description of the attribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateContactAttributeKeyResponse
            Contact attribute key updated successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.management_api_contact_attribute_keys.update_contact_attribute_key(
                id="id",
                name="Email Address",
                description="The user's email address",
                key="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_contact_attribute_key(
            id, key=key, name=name, description=description, request_options=request_options
        )
        return _response.data

    async def delete_contact_attribute_key(
        self, id: ContactAttributeKeyId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteContactAttributeKeyResponse:
        """
        Deletes a contact attribute key from the database.

        Parameters
        ----------
        id : ContactAttributeKeyId
            The ID of the contact attribute key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteContactAttributeKeyResponse
            Contact attribute key deleted successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.management_api_contact_attribute_keys.delete_contact_attribute_key(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_contact_attribute_key(id, request_options=request_options)
        return _response.data
