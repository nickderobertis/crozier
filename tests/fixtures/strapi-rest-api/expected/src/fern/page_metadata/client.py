

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_page_metadata_request_populate import GetPageMetadataRequestPopulate
from ..types.list_page_metadata_request_populate import ListPageMetadataRequestPopulate
from ..types.page_metadata_attributes import PageMetadataAttributes
from ..types.page_metadata_list_response import PageMetadataListResponse
from ..types.page_metadata_single_response import PageMetadataSingleResponse
from .raw_client import AsyncRawPageMetadataClient, RawPageMetadataClient
from .types.get_page_metadata_request_status import GetPageMetadataRequestStatus
from .types.list_page_metadata_request_status import ListPageMetadataRequestStatus


OMIT = typing.cast(typing.Any, ...)


class PageMetadataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPageMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPageMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPageMetadataClient
        """
        return self._raw_client

    def list_page_metadata(
        self,
        *,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        populate: typing.Optional[ListPageMetadataRequestPopulate] = None,
        status: typing.Optional[ListPageMetadataRequestStatus] = None,
        locale: typing.Optional[str] = None,
        publication_filter: typing.Optional[str] = None,
        pagination_page: typing.Optional[int] = None,
        pagination_page_size: typing.Optional[int] = None,
        pagination_start: typing.Optional[int] = None,
        pagination_limit: typing.Optional[int] = None,
        pagination_with_count: typing.Optional[bool] = None,
        filters_page_path_eq: typing.Optional[str] = None,
        filters_robots_index_eq: typing.Optional[bool] = None,
        filters_robots_follow_eq: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageMetadataListResponse:
        """
        List entries of the Jentic instance's `page-metadata` collection. This is the collection-type list endpoint (`GET /{pluralApiId}`) with `pluralApiId = page-metadatas`.

        Parameters
        ----------
        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sort the response. Single field `sort=field:asc`, or multiple via `sort[0]=field:asc&sort[1]=other:desc`. Direction is `:asc` (default) or `:desc`.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Select only specific fields to return, e.g. `fields[0]=title&fields[1]=description`. Does not apply to relational/media/component/dynamic-zone fields.

        populate : typing.Optional[ListPageMetadataRequestPopulate]
            Populate relations, media, components, and dynamic zones (excluded by default). `populate=*` for all one level deep, or bracket syntax for specific/nested relations.

        status : typing.Optional[ListPageMetadataRequestStatus]
            Select the Draft & Publish status on reads.

        locale : typing.Optional[str]
            Select a locale (i18n plugin).

        publication_filter : typing.Optional[str]
            Select documents by how their draft and published versions relate.

        pagination_page : typing.Optional[int]
            Page-based pagination: page number. Cannot be combined with start/limit.

        pagination_page_size : typing.Optional[int]
            Page-based pagination: entries per page.

        pagination_start : typing.Optional[int]
            Offset-based pagination: index of the first entry. Cannot be combined with page/pageSize.

        pagination_limit : typing.Optional[int]
            Offset-based pagination: number of entries to return. Maximum is configurable per instance.

        pagination_with_count : typing.Optional[bool]
            Include the total count / page count in the pagination metadata.

        filters_page_path_eq : typing.Optional[str]
            Filter by exact page path.

        filters_robots_index_eq : typing.Optional[bool]
            Filter by robotsIndex flag.

        filters_robots_follow_eq : typing.Optional[bool]
            Filter by robotsFollow flag.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageMetadataListResponse
            Paginated list of page-metadata entries.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.page_metadata.list_page_metadata()
        """
        _response = self._raw_client.list_page_metadata(
            sort=sort,
            fields=fields,
            populate=populate,
            status=status,
            locale=locale,
            publication_filter=publication_filter,
            pagination_page=pagination_page,
            pagination_page_size=pagination_page_size,
            pagination_start=pagination_start,
            pagination_limit=pagination_limit,
            pagination_with_count=pagination_with_count,
            filters_page_path_eq=filters_page_path_eq,
            filters_robots_index_eq=filters_robots_index_eq,
            filters_robots_follow_eq=filters_robots_follow_eq,
            request_options=request_options,
        )
        return _response.data

    def create_page_metadata(
        self, *, data: PageMetadataAttributes, request_options: typing.Optional[RequestOptions] = None
    ) -> PageMetadataSingleResponse:
        """
        Create a `page-metadata` entry (`POST /{pluralApiId}`). Note: over REST the created entry is published even when `status=draft` is supplied; verify `publishedAt` on the response.

        Parameters
        ----------
        data : PageMetadataAttributes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageMetadataSingleResponse
            Created entry.

        Examples
        --------
        from fern import FernApi, PageMetadataAttributes

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.page_metadata.create_page_metadata(
            data=PageMetadataAttributes(),
        )
        """
        _response = self._raw_client.create_page_metadata(data=data, request_options=request_options)
        return _response.data

    def get_page_metadata(
        self,
        document_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        populate: typing.Optional[GetPageMetadataRequestPopulate] = None,
        status: typing.Optional[GetPageMetadataRequestStatus] = None,
        locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageMetadataSingleResponse:
        """
        Retrieve a single `page-metadata` entry by documentId (`GET /{pluralApiId}/{documentId}`).

        Parameters
        ----------
        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Select only specific fields to return, e.g. `fields[0]=title&fields[1]=description`. Does not apply to relational/media/component/dynamic-zone fields.

        populate : typing.Optional[GetPageMetadataRequestPopulate]
            Populate relations, media, components, and dynamic zones (excluded by default). `populate=*` for all one level deep, or bracket syntax for specific/nested relations.

        status : typing.Optional[GetPageMetadataRequestStatus]
            Select the Draft & Publish status on reads.

        locale : typing.Optional[str]
            Select a locale (i18n plugin).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageMetadataSingleResponse
            The page-metadata entry.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.page_metadata.get_page_metadata(
            document_id="documentId",
        )
        """
        _response = self._raw_client.get_page_metadata(
            document_id, fields=fields, populate=populate, status=status, locale=locale, request_options=request_options
        )
        return _response.data

    def update_page_metadata(
        self, document_id: str, *, data: PageMetadataAttributes, request_options: typing.Optional[RequestOptions] = None
    ) -> PageMetadataSingleResponse:
        """
        Partially update a `page-metadata` entry by documentId (`PUT /{pluralApiId}/{documentId}`). Used to flip `robotsIndex` / `robotsFollow`. Note: updating over REST publishes the entry; there is no REST route to unpublish. Verify `publishedAt` on the response.

        Parameters
        ----------
        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        data : PageMetadataAttributes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageMetadataSingleResponse
            Updated entry.

        Examples
        --------
        from fern import FernApi, PageMetadataAttributes

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.page_metadata.update_page_metadata(
            document_id="documentId",
            data=PageMetadataAttributes(),
        )
        """
        _response = self._raw_client.update_page_metadata(document_id, data=data, request_options=request_options)
        return _response.data

    def delete_page_metadata(
        self, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a `page-metadata` entry by documentId (`DELETE /{pluralApiId}/{documentId}`).

        Parameters
        ----------
        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.page_metadata.delete_page_metadata(
            document_id="documentId",
        )
        """
        _response = self._raw_client.delete_page_metadata(document_id, request_options=request_options)
        return _response.data


class AsyncPageMetadataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPageMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPageMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPageMetadataClient
        """
        return self._raw_client

    async def list_page_metadata(
        self,
        *,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        populate: typing.Optional[ListPageMetadataRequestPopulate] = None,
        status: typing.Optional[ListPageMetadataRequestStatus] = None,
        locale: typing.Optional[str] = None,
        publication_filter: typing.Optional[str] = None,
        pagination_page: typing.Optional[int] = None,
        pagination_page_size: typing.Optional[int] = None,
        pagination_start: typing.Optional[int] = None,
        pagination_limit: typing.Optional[int] = None,
        pagination_with_count: typing.Optional[bool] = None,
        filters_page_path_eq: typing.Optional[str] = None,
        filters_robots_index_eq: typing.Optional[bool] = None,
        filters_robots_follow_eq: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageMetadataListResponse:
        """
        List entries of the Jentic instance's `page-metadata` collection. This is the collection-type list endpoint (`GET /{pluralApiId}`) with `pluralApiId = page-metadatas`.

        Parameters
        ----------
        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sort the response. Single field `sort=field:asc`, or multiple via `sort[0]=field:asc&sort[1]=other:desc`. Direction is `:asc` (default) or `:desc`.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Select only specific fields to return, e.g. `fields[0]=title&fields[1]=description`. Does not apply to relational/media/component/dynamic-zone fields.

        populate : typing.Optional[ListPageMetadataRequestPopulate]
            Populate relations, media, components, and dynamic zones (excluded by default). `populate=*` for all one level deep, or bracket syntax for specific/nested relations.

        status : typing.Optional[ListPageMetadataRequestStatus]
            Select the Draft & Publish status on reads.

        locale : typing.Optional[str]
            Select a locale (i18n plugin).

        publication_filter : typing.Optional[str]
            Select documents by how their draft and published versions relate.

        pagination_page : typing.Optional[int]
            Page-based pagination: page number. Cannot be combined with start/limit.

        pagination_page_size : typing.Optional[int]
            Page-based pagination: entries per page.

        pagination_start : typing.Optional[int]
            Offset-based pagination: index of the first entry. Cannot be combined with page/pageSize.

        pagination_limit : typing.Optional[int]
            Offset-based pagination: number of entries to return. Maximum is configurable per instance.

        pagination_with_count : typing.Optional[bool]
            Include the total count / page count in the pagination metadata.

        filters_page_path_eq : typing.Optional[str]
            Filter by exact page path.

        filters_robots_index_eq : typing.Optional[bool]
            Filter by robotsIndex flag.

        filters_robots_follow_eq : typing.Optional[bool]
            Filter by robotsFollow flag.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageMetadataListResponse
            Paginated list of page-metadata entries.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.page_metadata.list_page_metadata()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_page_metadata(
            sort=sort,
            fields=fields,
            populate=populate,
            status=status,
            locale=locale,
            publication_filter=publication_filter,
            pagination_page=pagination_page,
            pagination_page_size=pagination_page_size,
            pagination_start=pagination_start,
            pagination_limit=pagination_limit,
            pagination_with_count=pagination_with_count,
            filters_page_path_eq=filters_page_path_eq,
            filters_robots_index_eq=filters_robots_index_eq,
            filters_robots_follow_eq=filters_robots_follow_eq,
            request_options=request_options,
        )
        return _response.data

    async def create_page_metadata(
        self, *, data: PageMetadataAttributes, request_options: typing.Optional[RequestOptions] = None
    ) -> PageMetadataSingleResponse:
        """
        Create a `page-metadata` entry (`POST /{pluralApiId}`). Note: over REST the created entry is published even when `status=draft` is supplied; verify `publishedAt` on the response.

        Parameters
        ----------
        data : PageMetadataAttributes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageMetadataSingleResponse
            Created entry.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PageMetadataAttributes

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.page_metadata.create_page_metadata(
                data=PageMetadataAttributes(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_page_metadata(data=data, request_options=request_options)
        return _response.data

    async def get_page_metadata(
        self,
        document_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        populate: typing.Optional[GetPageMetadataRequestPopulate] = None,
        status: typing.Optional[GetPageMetadataRequestStatus] = None,
        locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageMetadataSingleResponse:
        """
        Retrieve a single `page-metadata` entry by documentId (`GET /{pluralApiId}/{documentId}`).

        Parameters
        ----------
        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Select only specific fields to return, e.g. `fields[0]=title&fields[1]=description`. Does not apply to relational/media/component/dynamic-zone fields.

        populate : typing.Optional[GetPageMetadataRequestPopulate]
            Populate relations, media, components, and dynamic zones (excluded by default). `populate=*` for all one level deep, or bracket syntax for specific/nested relations.

        status : typing.Optional[GetPageMetadataRequestStatus]
            Select the Draft & Publish status on reads.

        locale : typing.Optional[str]
            Select a locale (i18n plugin).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageMetadataSingleResponse
            The page-metadata entry.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.page_metadata.get_page_metadata(
                document_id="documentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_page_metadata(
            document_id, fields=fields, populate=populate, status=status, locale=locale, request_options=request_options
        )
        return _response.data

    async def update_page_metadata(
        self, document_id: str, *, data: PageMetadataAttributes, request_options: typing.Optional[RequestOptions] = None
    ) -> PageMetadataSingleResponse:
        """
        Partially update a `page-metadata` entry by documentId (`PUT /{pluralApiId}/{documentId}`). Used to flip `robotsIndex` / `robotsFollow`. Note: updating over REST publishes the entry; there is no REST route to unpublish. Verify `publishedAt` on the response.

        Parameters
        ----------
        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        data : PageMetadataAttributes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageMetadataSingleResponse
            Updated entry.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PageMetadataAttributes

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.page_metadata.update_page_metadata(
                document_id="documentId",
                data=PageMetadataAttributes(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_page_metadata(document_id, data=data, request_options=request_options)
        return _response.data

    async def delete_page_metadata(
        self, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a `page-metadata` entry by documentId (`DELETE /{pluralApiId}/{documentId}`).

        Parameters
        ----------
        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.page_metadata.delete_page_metadata(
                document_id="documentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_page_metadata(document_id, request_options=request_options)
        return _response.data
