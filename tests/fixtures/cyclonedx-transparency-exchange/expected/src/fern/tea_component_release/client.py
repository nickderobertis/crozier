

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.collection import Collection
from ..types.component_release_with_collection import ComponentReleaseWithCollection
from ..types.identifier_type import IdentifierType
from ..types.paginated_collection_response import PaginatedCollectionResponse
from ..types.paginated_component_release_response import PaginatedComponentReleaseResponse
from ..types.uuid_ import Uuid
from .raw_client import AsyncRawTeaComponentReleaseClient, RawTeaComponentReleaseClient
from .types.get_collections_by_release_id_request_sort_field import GetCollectionsByReleaseIdRequestSortField
from .types.get_collections_by_release_id_request_sort_order import GetCollectionsByReleaseIdRequestSortOrder
from .types.query_tea_component_releases_request_sort_field import QueryTeaComponentReleasesRequestSortField
from .types.query_tea_component_releases_request_sort_order import QueryTeaComponentReleasesRequestSortOrder


class TeaComponentReleaseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTeaComponentReleaseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTeaComponentReleaseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTeaComponentReleaseClient
        """
        return self._raw_client

    def query_tea_component_releases(
        self,
        *,
        id_type: typing.Optional[IdentifierType] = None,
        id_value: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_field: typing.Optional[QueryTeaComponentReleasesRequestSortField] = None,
        sort_order: typing.Optional[QueryTeaComponentReleasesRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedComponentReleaseResponse:
        """
        Returns a list of TEA component releases. Note that multiple component releases may match.

        Parameters
        ----------
        id_type : typing.Optional[IdentifierType]
            Type of identifier specified in the `idValue` parameter

        id_value : typing.Optional[str]
            If present, only the objects with the given identifier value will be returned.

        page_size : typing.Optional[int]
            The maximum number of results to return.

        page_token : typing.Optional[str]
            An opaque continuation token produced by a previous response.
            This token MUST be copied verbatim from the `nextPageToken` value returned by the previous response.
            Clients MUST NOT parse, construct, or modify this token.

            The token represents continuation state for the original query, including
            `sortField`, `sortOrder`, result-affecting filters such as `idType` and `idValue`,
            and path parameters such as parent `uuid`.
            When `pageToken` is supplied, clients MUST NOT change those result-affecting query
            parameters. Servers MUST return `400 Bad Request` if supplied result-affecting query
            parameters conflict with the token state. To change any result-affecting parameter,
            clients MUST start a new pagination sequence without `pageToken`.

            A `pageToken` is only valid with the same request path and same path parameter values
            used to obtain it. Clients MUST NOT reuse a `pageToken` across different parent
            resource paths or different path `uuid` values. Servers MUST return `400 Bad Request`
            when a `pageToken` is used with a different path or different path parameter values.

            Servers MUST return `400 Bad Request` for malformed, invalid, expired, or conflicting
            `pageToken` values.

        sort_field : typing.Optional[QueryTeaComponentReleasesRequestSortField]
            The field by which to sort the results.

            Paginated results MUST be ordered first by the selected `sortField`, then by `uuid`
            as a deterministic secondary tie-breaker.

            When `version` is selected, ordering is by the stored version string according to
            the server's documented string collation; semantic-version precedence is not implied.
            Servers MUST apply a stable and deterministic string collation for version sorting,
            and the same collation MUST be used consistently across pages for a pagination sequence.

            When `releaseDate` is selected, releases without a `releaseDate` MUST be ordered
            consistently. Missing `releaseDate` values sort after populated `releaseDate` values
            for ascending order and before populated `releaseDate` values for descending order.

        sort_order : typing.Optional[QueryTeaComponentReleasesRequestSortOrder]
            The direction of the sort.

            The selected sort order applies to both the primary `sortField` and the
            resource-specific deterministic secondary tie-breaker. For products, components,
            product releases, and component releases, the secondary key is `uuid`. For collections,
            the secondary key is `version` if additional tie-breaking is needed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedComponentReleaseResponse
            A paginated response containing TEA Component Releases

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tea_component_release.query_tea_component_releases()
        """
        _response = self._raw_client.query_tea_component_releases(
            id_type=id_type,
            id_value=id_value,
            page_size=page_size,
            page_token=page_token,
            sort_field=sort_field,
            sort_order=sort_order,
            request_options=request_options,
        )
        return _response.data

    def get_component_release_by_id(
        self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ComponentReleaseWithCollection:
        """
        Get the TEA Component Release with its latest collection

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Component Release in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComponentReleaseWithCollection
            Requested TEA Component Release and its latest Collection found and returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tea_component_release.get_component_release_by_id(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_component_release_by_id(uuid_, request_options=request_options)
        return _response.data

    def get_latest_collection(
        self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Collection:
        """
        Get the latest TEA Collection belonging to the TEA Component Release

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Component Release in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collection
            Requested TEA Collection found and returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tea_component_release.get_latest_collection(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_latest_collection(uuid_, request_options=request_options)
        return _response.data

    def get_collections_by_release_id(
        self,
        uuid_: Uuid,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_field: typing.Optional[GetCollectionsByReleaseIdRequestSortField] = None,
        sort_order: typing.Optional[GetCollectionsByReleaseIdRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedCollectionResponse:
        """
        Get the TEA Collections belonging to the TEA Component Release

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Component Release in the TEA server

        page_size : typing.Optional[int]
            The maximum number of results to return.

        page_token : typing.Optional[str]
            An opaque continuation token produced by a previous response.
            This token MUST be copied verbatim from the `nextPageToken` value returned by the previous response.
            Clients MUST NOT parse, construct, or modify this token.

            The token represents continuation state for the original query, including
            `sortField`, `sortOrder`, result-affecting filters such as `idType` and `idValue`,
            and path parameters such as parent `uuid`.
            When `pageToken` is supplied, clients MUST NOT change those result-affecting query
            parameters. Servers MUST return `400 Bad Request` if supplied result-affecting query
            parameters conflict with the token state. To change any result-affecting parameter,
            clients MUST start a new pagination sequence without `pageToken`.

            A `pageToken` is only valid with the same request path and same path parameter values
            used to obtain it. Clients MUST NOT reuse a `pageToken` across different parent
            resource paths or different path `uuid` values. Servers MUST return `400 Bad Request`
            when a `pageToken` is used with a different path or different path parameter values.

            Servers MUST return `400 Bad Request` for malformed, invalid, expired, or conflicting
            `pageToken` values.

        sort_field : typing.Optional[GetCollectionsByReleaseIdRequestSortField]
            The field by which to sort the results.

            Paginated collection results MUST be ordered first by the selected `sortField`,
            then by `version` as the deterministic secondary key if additional tie-breaking
            is needed. Collection UUIDs are not used as tie-breakers because collection UUIDs
            match the associated release UUID and can be shared across collection revisions.

            The only currently supported collection `sortField` is `version`, so the secondary
            `version` key is redundant unless additional collection sort fields are added later.

        sort_order : typing.Optional[GetCollectionsByReleaseIdRequestSortOrder]
            The direction of the sort.

            The selected sort order applies to both the primary `sortField` and the
            resource-specific deterministic secondary tie-breaker. For products, components,
            product releases, and component releases, the secondary key is `uuid`. For collections,
            the secondary key is `version` if additional tie-breaking is needed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedCollectionResponse
            A paginated response containing TEA Collections

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tea_component_release.get_collections_by_release_id(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_collections_by_release_id(
            uuid_,
            page_size=page_size,
            page_token=page_token,
            sort_field=sort_field,
            sort_order=sort_order,
            request_options=request_options,
        )
        return _response.data

    def get_collection(
        self, uuid_: Uuid, collection_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Collection:
        """
        Get a specific Collection (by version) for a TEA Component Release by its UUID

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Collection in the TEA server

        collection_version : int
            Version of TEA Collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collection
            Requested TEA Collection Version found and returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tea_component_release.get_collection(
            uuid_="uuid",
            collection_version=1,
        )
        """
        _response = self._raw_client.get_collection(uuid_, collection_version, request_options=request_options)
        return _response.data


class AsyncTeaComponentReleaseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTeaComponentReleaseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTeaComponentReleaseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTeaComponentReleaseClient
        """
        return self._raw_client

    async def query_tea_component_releases(
        self,
        *,
        id_type: typing.Optional[IdentifierType] = None,
        id_value: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_field: typing.Optional[QueryTeaComponentReleasesRequestSortField] = None,
        sort_order: typing.Optional[QueryTeaComponentReleasesRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedComponentReleaseResponse:
        """
        Returns a list of TEA component releases. Note that multiple component releases may match.

        Parameters
        ----------
        id_type : typing.Optional[IdentifierType]
            Type of identifier specified in the `idValue` parameter

        id_value : typing.Optional[str]
            If present, only the objects with the given identifier value will be returned.

        page_size : typing.Optional[int]
            The maximum number of results to return.

        page_token : typing.Optional[str]
            An opaque continuation token produced by a previous response.
            This token MUST be copied verbatim from the `nextPageToken` value returned by the previous response.
            Clients MUST NOT parse, construct, or modify this token.

            The token represents continuation state for the original query, including
            `sortField`, `sortOrder`, result-affecting filters such as `idType` and `idValue`,
            and path parameters such as parent `uuid`.
            When `pageToken` is supplied, clients MUST NOT change those result-affecting query
            parameters. Servers MUST return `400 Bad Request` if supplied result-affecting query
            parameters conflict with the token state. To change any result-affecting parameter,
            clients MUST start a new pagination sequence without `pageToken`.

            A `pageToken` is only valid with the same request path and same path parameter values
            used to obtain it. Clients MUST NOT reuse a `pageToken` across different parent
            resource paths or different path `uuid` values. Servers MUST return `400 Bad Request`
            when a `pageToken` is used with a different path or different path parameter values.

            Servers MUST return `400 Bad Request` for malformed, invalid, expired, or conflicting
            `pageToken` values.

        sort_field : typing.Optional[QueryTeaComponentReleasesRequestSortField]
            The field by which to sort the results.

            Paginated results MUST be ordered first by the selected `sortField`, then by `uuid`
            as a deterministic secondary tie-breaker.

            When `version` is selected, ordering is by the stored version string according to
            the server's documented string collation; semantic-version precedence is not implied.
            Servers MUST apply a stable and deterministic string collation for version sorting,
            and the same collation MUST be used consistently across pages for a pagination sequence.

            When `releaseDate` is selected, releases without a `releaseDate` MUST be ordered
            consistently. Missing `releaseDate` values sort after populated `releaseDate` values
            for ascending order and before populated `releaseDate` values for descending order.

        sort_order : typing.Optional[QueryTeaComponentReleasesRequestSortOrder]
            The direction of the sort.

            The selected sort order applies to both the primary `sortField` and the
            resource-specific deterministic secondary tie-breaker. For products, components,
            product releases, and component releases, the secondary key is `uuid`. For collections,
            the secondary key is `version` if additional tie-breaking is needed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedComponentReleaseResponse
            A paginated response containing TEA Component Releases

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tea_component_release.query_tea_component_releases()


        asyncio.run(main())
        """
        _response = await self._raw_client.query_tea_component_releases(
            id_type=id_type,
            id_value=id_value,
            page_size=page_size,
            page_token=page_token,
            sort_field=sort_field,
            sort_order=sort_order,
            request_options=request_options,
        )
        return _response.data

    async def get_component_release_by_id(
        self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ComponentReleaseWithCollection:
        """
        Get the TEA Component Release with its latest collection

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Component Release in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComponentReleaseWithCollection
            Requested TEA Component Release and its latest Collection found and returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tea_component_release.get_component_release_by_id(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_component_release_by_id(uuid_, request_options=request_options)
        return _response.data

    async def get_latest_collection(
        self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Collection:
        """
        Get the latest TEA Collection belonging to the TEA Component Release

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Component Release in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collection
            Requested TEA Collection found and returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tea_component_release.get_latest_collection(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_latest_collection(uuid_, request_options=request_options)
        return _response.data

    async def get_collections_by_release_id(
        self,
        uuid_: Uuid,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_field: typing.Optional[GetCollectionsByReleaseIdRequestSortField] = None,
        sort_order: typing.Optional[GetCollectionsByReleaseIdRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedCollectionResponse:
        """
        Get the TEA Collections belonging to the TEA Component Release

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Component Release in the TEA server

        page_size : typing.Optional[int]
            The maximum number of results to return.

        page_token : typing.Optional[str]
            An opaque continuation token produced by a previous response.
            This token MUST be copied verbatim from the `nextPageToken` value returned by the previous response.
            Clients MUST NOT parse, construct, or modify this token.

            The token represents continuation state for the original query, including
            `sortField`, `sortOrder`, result-affecting filters such as `idType` and `idValue`,
            and path parameters such as parent `uuid`.
            When `pageToken` is supplied, clients MUST NOT change those result-affecting query
            parameters. Servers MUST return `400 Bad Request` if supplied result-affecting query
            parameters conflict with the token state. To change any result-affecting parameter,
            clients MUST start a new pagination sequence without `pageToken`.

            A `pageToken` is only valid with the same request path and same path parameter values
            used to obtain it. Clients MUST NOT reuse a `pageToken` across different parent
            resource paths or different path `uuid` values. Servers MUST return `400 Bad Request`
            when a `pageToken` is used with a different path or different path parameter values.

            Servers MUST return `400 Bad Request` for malformed, invalid, expired, or conflicting
            `pageToken` values.

        sort_field : typing.Optional[GetCollectionsByReleaseIdRequestSortField]
            The field by which to sort the results.

            Paginated collection results MUST be ordered first by the selected `sortField`,
            then by `version` as the deterministic secondary key if additional tie-breaking
            is needed. Collection UUIDs are not used as tie-breakers because collection UUIDs
            match the associated release UUID and can be shared across collection revisions.

            The only currently supported collection `sortField` is `version`, so the secondary
            `version` key is redundant unless additional collection sort fields are added later.

        sort_order : typing.Optional[GetCollectionsByReleaseIdRequestSortOrder]
            The direction of the sort.

            The selected sort order applies to both the primary `sortField` and the
            resource-specific deterministic secondary tie-breaker. For products, components,
            product releases, and component releases, the secondary key is `uuid`. For collections,
            the secondary key is `version` if additional tie-breaking is needed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedCollectionResponse
            A paginated response containing TEA Collections

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tea_component_release.get_collections_by_release_id(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collections_by_release_id(
            uuid_,
            page_size=page_size,
            page_token=page_token,
            sort_field=sort_field,
            sort_order=sort_order,
            request_options=request_options,
        )
        return _response.data

    async def get_collection(
        self, uuid_: Uuid, collection_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Collection:
        """
        Get a specific Collection (by version) for a TEA Component Release by its UUID

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Collection in the TEA server

        collection_version : int
            Version of TEA Collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collection
            Requested TEA Collection Version found and returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tea_component_release.get_collection(
                uuid_="uuid",
                collection_version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collection(uuid_, collection_version, request_options=request_options)
        return _response.data
