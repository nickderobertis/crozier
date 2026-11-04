

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_collaboration_resources_list_collection200response import (
    CoreCollaborationResourcesListCollection200Response,
)
from ..types.core_collaboration_resources_search_collections200response import (
    CoreCollaborationResourcesSearchCollections200Response,
)
from .raw_client import AsyncRawCoreCollaborationResourcesClient, RawCoreCollaborationResourcesClient


class CoreCollaborationResourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCoreCollaborationResourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCoreCollaborationResourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCoreCollaborationResourcesClient
        """
        return self._raw_client

    def search_collections(
        self, filter: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreCollaborationResourcesSearchCollections200Response:
        """
        Parameters
        ----------
        filter : str
            Filter collections

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreCollaborationResourcesSearchCollections200Response
            Collections returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_collaboration_resources.search_collections(
            filter="filter",
        )
        """
        _response = self._raw_client.search_collections(filter, request_options=request_options)
        return _response.data

    def list_collection(
        self, collection_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreCollaborationResourcesListCollection200Response:
        """
        Parameters
        ----------
        collection_id : int
            ID of the collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreCollaborationResourcesListCollection200Response
            Collection returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_collaboration_resources.list_collection(
            collection_id=1000000,
        )
        """
        _response = self._raw_client.list_collection(collection_id, request_options=request_options)
        return _response.data

    def add_resource(
        self,
        collection_id: int,
        *,
        resource_type: str,
        resource_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreCollaborationResourcesListCollection200Response:
        """
        Parameters
        ----------
        collection_id : int
            ID of the collection

        resource_type : str
            Name of the resource

        resource_id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreCollaborationResourcesListCollection200Response
            Collection returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_collaboration_resources.add_resource(
            collection_id=1000000,
            resource_type="resourceType",
            resource_id="resourceId",
        )
        """
        _response = self._raw_client.add_resource(
            collection_id, resource_type=resource_type, resource_id=resource_id, request_options=request_options
        )
        return _response.data

    def rename_collection(
        self, collection_id: int, *, collection_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreCollaborationResourcesListCollection200Response:
        """
        Parameters
        ----------
        collection_id : int
            ID of the collection

        collection_name : str
            New name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreCollaborationResourcesListCollection200Response
            Collection returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_collaboration_resources.rename_collection(
            collection_id=1000000,
            collection_name="collectionName",
        )
        """
        _response = self._raw_client.rename_collection(
            collection_id, collection_name=collection_name, request_options=request_options
        )
        return _response.data

    def remove_resource(
        self,
        collection_id: int,
        *,
        resource_type: str,
        resource_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreCollaborationResourcesListCollection200Response:
        """
        Parameters
        ----------
        collection_id : int
            ID of the collection

        resource_type : str
            Name of the resource

        resource_id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreCollaborationResourcesListCollection200Response
            Collection returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_collaboration_resources.remove_resource(
            collection_id=1000000,
            resource_type="resourceType",
            resource_id="resourceId",
        )
        """
        _response = self._raw_client.remove_resource(
            collection_id, resource_type=resource_type, resource_id=resource_id, request_options=request_options
        )
        return _response.data

    def get_collections_by_resource(
        self, resource_type: str, resource_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreCollaborationResourcesSearchCollections200Response:
        """
        Parameters
        ----------
        resource_type : str
            Type of the resource

        resource_id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreCollaborationResourcesSearchCollections200Response
            Collections returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_collaboration_resources.get_collections_by_resource(
            resource_type="resourceType",
            resource_id="resourceId",
        )
        """
        _response = self._raw_client.get_collections_by_resource(
            resource_type, resource_id, request_options=request_options
        )
        return _response.data

    def create_collection_on_resource(
        self,
        base_resource_type: str,
        base_resource_id: str,
        *,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreCollaborationResourcesListCollection200Response:
        """
        Parameters
        ----------
        base_resource_type : str
            Type of the base resource

        base_resource_id : str
            ID of the base resource

        name : str
            Name of the collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreCollaborationResourcesListCollection200Response
            Collection returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_collaboration_resources.create_collection_on_resource(
            base_resource_type="baseResourceType",
            base_resource_id="baseResourceId",
            name="name",
        )
        """
        _response = self._raw_client.create_collection_on_resource(
            base_resource_type, base_resource_id, name=name, request_options=request_options
        )
        return _response.data


class AsyncCoreCollaborationResourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCoreCollaborationResourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCoreCollaborationResourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCoreCollaborationResourcesClient
        """
        return self._raw_client

    async def search_collections(
        self, filter: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreCollaborationResourcesSearchCollections200Response:
        """
        Parameters
        ----------
        filter : str
            Filter collections

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreCollaborationResourcesSearchCollections200Response
            Collections returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_collaboration_resources.search_collections(
                filter="filter",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_collections(filter, request_options=request_options)
        return _response.data

    async def list_collection(
        self, collection_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreCollaborationResourcesListCollection200Response:
        """
        Parameters
        ----------
        collection_id : int
            ID of the collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreCollaborationResourcesListCollection200Response
            Collection returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_collaboration_resources.list_collection(
                collection_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_collection(collection_id, request_options=request_options)
        return _response.data

    async def add_resource(
        self,
        collection_id: int,
        *,
        resource_type: str,
        resource_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreCollaborationResourcesListCollection200Response:
        """
        Parameters
        ----------
        collection_id : int
            ID of the collection

        resource_type : str
            Name of the resource

        resource_id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreCollaborationResourcesListCollection200Response
            Collection returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_collaboration_resources.add_resource(
                collection_id=1000000,
                resource_type="resourceType",
                resource_id="resourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_resource(
            collection_id, resource_type=resource_type, resource_id=resource_id, request_options=request_options
        )
        return _response.data

    async def rename_collection(
        self, collection_id: int, *, collection_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreCollaborationResourcesListCollection200Response:
        """
        Parameters
        ----------
        collection_id : int
            ID of the collection

        collection_name : str
            New name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreCollaborationResourcesListCollection200Response
            Collection returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_collaboration_resources.rename_collection(
                collection_id=1000000,
                collection_name="collectionName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rename_collection(
            collection_id, collection_name=collection_name, request_options=request_options
        )
        return _response.data

    async def remove_resource(
        self,
        collection_id: int,
        *,
        resource_type: str,
        resource_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreCollaborationResourcesListCollection200Response:
        """
        Parameters
        ----------
        collection_id : int
            ID of the collection

        resource_type : str
            Name of the resource

        resource_id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreCollaborationResourcesListCollection200Response
            Collection returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_collaboration_resources.remove_resource(
                collection_id=1000000,
                resource_type="resourceType",
                resource_id="resourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_resource(
            collection_id, resource_type=resource_type, resource_id=resource_id, request_options=request_options
        )
        return _response.data

    async def get_collections_by_resource(
        self, resource_type: str, resource_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreCollaborationResourcesSearchCollections200Response:
        """
        Parameters
        ----------
        resource_type : str
            Type of the resource

        resource_id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreCollaborationResourcesSearchCollections200Response
            Collections returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_collaboration_resources.get_collections_by_resource(
                resource_type="resourceType",
                resource_id="resourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collections_by_resource(
            resource_type, resource_id, request_options=request_options
        )
        return _response.data

    async def create_collection_on_resource(
        self,
        base_resource_type: str,
        base_resource_id: str,
        *,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreCollaborationResourcesListCollection200Response:
        """
        Parameters
        ----------
        base_resource_type : str
            Type of the base resource

        base_resource_id : str
            ID of the base resource

        name : str
            Name of the collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreCollaborationResourcesListCollection200Response
            Collection returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_collaboration_resources.create_collection_on_resource(
                base_resource_type="baseResourceType",
                base_resource_id="baseResourceId",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_collection_on_resource(
            base_resource_type, base_resource_id, name=name, request_options=request_options
        )
        return _response.data
