

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.namespaces_get_response import NamespacesGetResponse
from ..types.resource_get_response import ResourceGetResponse
from ..types.resources_get_response import ResourcesGetResponse
from ..types.resources_kinds_get_response import ResourcesKindsGetResponse
from ..types.resources_search_get_response import ResourcesSearchGetResponse
from ..types.resources_sync_post_response import ResourcesSyncPostResponse
from .raw_client import AsyncRawResourcesClient, RawResourcesClient


OMIT = typing.cast(typing.Any, ...)


class ResourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawResourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawResourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawResourcesClient
        """
        return self._raw_client

    def list_resources_filtered_by_kind_and_optional_namespace(
        self,
        *,
        kind: str,
        api_version: str,
        namespace: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        offset: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResourcesGetResponse:
        """
        List resources filtered by kind and optional namespace

        Parameters
        ----------
        kind : str
            Resource kind (e.g., Pod, Deployment)

        api_version : str
            API version (e.g., v1, apps/v1)

        namespace : typing.Optional[str]
            Filter by namespace

        limit : typing.Optional[float]
            Maximum results to return

        offset : typing.Optional[float]
            Offset for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResourcesGetResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.resources.list_resources_filtered_by_kind_and_optional_namespace(
            kind="kind",
            api_version="apiVersion",
        )
        """
        _response = self._raw_client.list_resources_filtered_by_kind_and_optional_namespace(
            kind=kind,
            api_version=api_version,
            namespace=namespace,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def list_all_resource_kinds_available_in_the_cluster_with_counts(
        self, *, namespace: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ResourcesKindsGetResponse:
        """
        List all resource kinds available in the cluster with counts

        Parameters
        ----------
        namespace : typing.Optional[str]
            Filter kinds by namespace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResourcesKindsGetResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.resources.list_all_resource_kinds_available_in_the_cluster_with_counts()
        """
        _response = self._raw_client.list_all_resource_kinds_available_in_the_cluster_with_counts(
            namespace=namespace, request_options=request_options
        )
        return _response.data

    def search_for_resources_using_semantic_search(
        self, *, q: str, limit: float, offset: float, request_options: typing.Optional[RequestOptions] = None
    ) -> ResourcesSearchGetResponse:
        """
        Search for resources using semantic search

        Parameters
        ----------
        q : str
            Search query

        limit : float
            Maximum results to return

        offset : float
            Offset for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResourcesSearchGetResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.resources.search_for_resources_using_semantic_search(
            q="q",
            limit=1.1,
            offset=1.1,
        )
        """
        _response = self._raw_client.search_for_resources_using_semantic_search(
            q=q, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def sync_resources_from_the_kubernetes_controller(
        self,
        *,
        upserts: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        deletes: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        is_resync: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResourcesSyncPostResponse:
        """
        Sync resources from the Kubernetes controller

        Parameters
        ----------
        upserts : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Resources to upsert

        deletes : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Resources to delete (requires namespace, name, kind, apiVersion)

        is_resync : typing.Optional[bool]
            When true, performs full reconciliation - deletes resources not in upserts list

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResourcesSyncPostResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.resources.sync_resources_from_the_kubernetes_controller()
        """
        _response = self._raw_client.sync_resources_from_the_kubernetes_controller(
            upserts=upserts, deletes=deletes, is_resync=is_resync, request_options=request_options
        )
        return _response.data

    def get_a_single_resource_with_full_details_including_live_status(
        self,
        *,
        kind: str,
        api_version: str,
        name: str,
        namespace: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResourceGetResponse:
        """
        Get a single resource with full details including live status

        Parameters
        ----------
        kind : str
            Resource kind

        api_version : str
            API version

        name : str
            Resource name

        namespace : typing.Optional[str]
            Namespace (for namespaced resources)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResourceGetResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.resources.get_a_single_resource_with_full_details_including_live_status(
            kind="kind",
            api_version="apiVersion",
            name="name",
        )
        """
        _response = self._raw_client.get_a_single_resource_with_full_details_including_live_status(
            kind=kind, api_version=api_version, name=name, namespace=namespace, request_options=request_options
        )
        return _response.data

    def list_all_namespaces_in_the_cluster(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NamespacesGetResponse:
        """
        List all namespaces in the cluster

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamespacesGetResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.resources.list_all_namespaces_in_the_cluster()
        """
        _response = self._raw_client.list_all_namespaces_in_the_cluster(request_options=request_options)
        return _response.data


class AsyncResourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawResourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawResourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawResourcesClient
        """
        return self._raw_client

    async def list_resources_filtered_by_kind_and_optional_namespace(
        self,
        *,
        kind: str,
        api_version: str,
        namespace: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        offset: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResourcesGetResponse:
        """
        List resources filtered by kind and optional namespace

        Parameters
        ----------
        kind : str
            Resource kind (e.g., Pod, Deployment)

        api_version : str
            API version (e.g., v1, apps/v1)

        namespace : typing.Optional[str]
            Filter by namespace

        limit : typing.Optional[float]
            Maximum results to return

        offset : typing.Optional[float]
            Offset for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResourcesGetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.resources.list_resources_filtered_by_kind_and_optional_namespace(
                kind="kind",
                api_version="apiVersion",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_resources_filtered_by_kind_and_optional_namespace(
            kind=kind,
            api_version=api_version,
            namespace=namespace,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def list_all_resource_kinds_available_in_the_cluster_with_counts(
        self, *, namespace: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ResourcesKindsGetResponse:
        """
        List all resource kinds available in the cluster with counts

        Parameters
        ----------
        namespace : typing.Optional[str]
            Filter kinds by namespace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResourcesKindsGetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.resources.list_all_resource_kinds_available_in_the_cluster_with_counts()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_resource_kinds_available_in_the_cluster_with_counts(
            namespace=namespace, request_options=request_options
        )
        return _response.data

    async def search_for_resources_using_semantic_search(
        self, *, q: str, limit: float, offset: float, request_options: typing.Optional[RequestOptions] = None
    ) -> ResourcesSearchGetResponse:
        """
        Search for resources using semantic search

        Parameters
        ----------
        q : str
            Search query

        limit : float
            Maximum results to return

        offset : float
            Offset for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResourcesSearchGetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.resources.search_for_resources_using_semantic_search(
                q="q",
                limit=1.1,
                offset=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_for_resources_using_semantic_search(
            q=q, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def sync_resources_from_the_kubernetes_controller(
        self,
        *,
        upserts: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        deletes: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        is_resync: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResourcesSyncPostResponse:
        """
        Sync resources from the Kubernetes controller

        Parameters
        ----------
        upserts : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Resources to upsert

        deletes : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Resources to delete (requires namespace, name, kind, apiVersion)

        is_resync : typing.Optional[bool]
            When true, performs full reconciliation - deletes resources not in upserts list

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResourcesSyncPostResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.resources.sync_resources_from_the_kubernetes_controller()


        asyncio.run(main())
        """
        _response = await self._raw_client.sync_resources_from_the_kubernetes_controller(
            upserts=upserts, deletes=deletes, is_resync=is_resync, request_options=request_options
        )
        return _response.data

    async def get_a_single_resource_with_full_details_including_live_status(
        self,
        *,
        kind: str,
        api_version: str,
        name: str,
        namespace: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResourceGetResponse:
        """
        Get a single resource with full details including live status

        Parameters
        ----------
        kind : str
            Resource kind

        api_version : str
            API version

        name : str
            Resource name

        namespace : typing.Optional[str]
            Namespace (for namespaced resources)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResourceGetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.resources.get_a_single_resource_with_full_details_including_live_status(
                kind="kind",
                api_version="apiVersion",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_single_resource_with_full_details_including_live_status(
            kind=kind, api_version=api_version, name=name, namespace=namespace, request_options=request_options
        )
        return _response.data

    async def list_all_namespaces_in_the_cluster(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NamespacesGetResponse:
        """
        List all namespaces in the cluster

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamespacesGetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.resources.list_all_namespaces_in_the_cluster()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_namespaces_in_the_cluster(request_options=request_options)
        return _response.data
