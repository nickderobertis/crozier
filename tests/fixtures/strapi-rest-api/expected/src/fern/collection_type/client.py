

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.entry_list_response import EntryListResponse
from ..types.entry_single_response import EntrySingleResponse
from ..types.get_entry_request_populate import GetEntryRequestPopulate
from ..types.list_entries_request_populate import ListEntriesRequestPopulate
from .raw_client import AsyncRawCollectionTypeClient, RawCollectionTypeClient
from .types.get_entry_request_status import GetEntryRequestStatus
from .types.list_entries_request_status import ListEntriesRequestStatus


OMIT = typing.cast(typing.Any, ...)


class CollectionTypeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCollectionTypeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCollectionTypeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCollectionTypeClient
        """
        return self._raw_client

    def list_entries(
        self,
        api_id: str,
        *,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        populate: typing.Optional[ListEntriesRequestPopulate] = None,
        status: typing.Optional[ListEntriesRequestStatus] = None,
        locale: typing.Optional[str] = None,
        publication_filter: typing.Optional[str] = None,
        pagination_page: typing.Optional[int] = None,
        pagination_page_size: typing.Optional[int] = None,
        pagination_start: typing.Optional[int] = None,
        pagination_limit: typing.Optional[int] = None,
        pagination_with_count: typing.Optional[bool] = None,
        filters: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntryListResponse:
        """
        For a collection type (`apiId` = plural API ID, e.g. `articles`, `page-metadatas`) this lists entries with filtering, sorting, field selection, population, pagination, and status. For a single type (`apiId` = singular API ID, e.g. `homepage`) this returns the one global entry; the list query parameters do not apply. Collection and single types share this path position, so they are described by one templated path.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sort the response. Single field `sort=field:asc`, or multiple via `sort[0]=field:asc&sort[1]=other:desc`. Direction is `:asc` (default) or `:desc`.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Select only specific fields to return, e.g. `fields[0]=title&fields[1]=description`. Does not apply to relational/media/component/dynamic-zone fields.

        populate : typing.Optional[ListEntriesRequestPopulate]
            Populate relations, media, components, and dynamic zones (excluded by default). `populate=*` for all one level deep, or bracket syntax for specific/nested relations.

        status : typing.Optional[ListEntriesRequestStatus]
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

        filters : typing.Optional[typing.Dict[str, typing.Any]]
            Filter the response. Use bracket syntax `filters[field][$operator]=value`. Operators: $eq, $eqi, $ne, $nei, $lt, $lte, $gt, $gte, $in, $notIn, $contains, $notContains, $containsi, $notContainsi, $startsWith, $startsWithi, $endsWith, $endsWithi, $null, $notNull, $between, $or, $and, $not.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntryListResponse
            Paginated list of entries.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collection_type.list_entries(
            api_id="apiId",
        )
        """
        _response = self._raw_client.list_entries(
            api_id,
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
            filters=filters,
            request_options=request_options,
        )
        return _response.data

    def create_entry(
        self,
        api_id: str,
        *,
        data: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntrySingleResponse:
        """
        Create an entry of a collection type. The request body wraps attributes under a `data` key. Not applicable to single types (use PUT). Note: over REST the entry is auto-published even with `status=draft`; verify `publishedAt` on the response.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

        data : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntrySingleResponse
            Created entry.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collection_type.create_entry(
            api_id="apiId",
            data={"key": "value"},
        )
        """
        _response = self._raw_client.create_entry(api_id, data=data, request_options=request_options)
        return _response.data

    def get_entry(
        self,
        api_id: str,
        document_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        populate: typing.Optional[GetEntryRequestPopulate] = None,
        status: typing.Optional[GetEntryRequestStatus] = None,
        locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntrySingleResponse:
        """
        Retrieve a single collection-type entry by its `documentId`.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Select only specific fields to return, e.g. `fields[0]=title&fields[1]=description`. Does not apply to relational/media/component/dynamic-zone fields.

        populate : typing.Optional[GetEntryRequestPopulate]
            Populate relations, media, components, and dynamic zones (excluded by default). `populate=*` for all one level deep, or bracket syntax for specific/nested relations.

        status : typing.Optional[GetEntryRequestStatus]
            Select the Draft & Publish status on reads.

        locale : typing.Optional[str]
            Select a locale (i18n plugin).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntrySingleResponse
            The entry.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collection_type.get_entry(
            api_id="apiId",
            document_id="documentId",
        )
        """
        _response = self._raw_client.get_entry(
            api_id,
            document_id,
            fields=fields,
            populate=populate,
            status=status,
            locale=locale,
            request_options=request_options,
        )
        return _response.data

    def update_entry(
        self,
        api_id: str,
        document_id: str,
        *,
        data: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntrySingleResponse:
        """
        Partially update a collection-type entry by `documentId`. Note: updating over REST publishes the entry; there is no REST route to unpublish.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        data : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntrySingleResponse
            Updated entry.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collection_type.update_entry(
            api_id="apiId",
            document_id="documentId",
            data={"key": "value"},
        )
        """
        _response = self._raw_client.update_entry(api_id, document_id, data=data, request_options=request_options)
        return _response.data

    def delete_entry(
        self, api_id: str, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a collection-type entry by `documentId`.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

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
        client.collection_type.delete_entry(
            api_id="apiId",
            document_id="documentId",
        )
        """
        _response = self._raw_client.delete_entry(api_id, document_id, request_options=request_options)
        return _response.data


class AsyncCollectionTypeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCollectionTypeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCollectionTypeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCollectionTypeClient
        """
        return self._raw_client

    async def list_entries(
        self,
        api_id: str,
        *,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        populate: typing.Optional[ListEntriesRequestPopulate] = None,
        status: typing.Optional[ListEntriesRequestStatus] = None,
        locale: typing.Optional[str] = None,
        publication_filter: typing.Optional[str] = None,
        pagination_page: typing.Optional[int] = None,
        pagination_page_size: typing.Optional[int] = None,
        pagination_start: typing.Optional[int] = None,
        pagination_limit: typing.Optional[int] = None,
        pagination_with_count: typing.Optional[bool] = None,
        filters: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntryListResponse:
        """
        For a collection type (`apiId` = plural API ID, e.g. `articles`, `page-metadatas`) this lists entries with filtering, sorting, field selection, population, pagination, and status. For a single type (`apiId` = singular API ID, e.g. `homepage`) this returns the one global entry; the list query parameters do not apply. Collection and single types share this path position, so they are described by one templated path.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sort the response. Single field `sort=field:asc`, or multiple via `sort[0]=field:asc&sort[1]=other:desc`. Direction is `:asc` (default) or `:desc`.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Select only specific fields to return, e.g. `fields[0]=title&fields[1]=description`. Does not apply to relational/media/component/dynamic-zone fields.

        populate : typing.Optional[ListEntriesRequestPopulate]
            Populate relations, media, components, and dynamic zones (excluded by default). `populate=*` for all one level deep, or bracket syntax for specific/nested relations.

        status : typing.Optional[ListEntriesRequestStatus]
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

        filters : typing.Optional[typing.Dict[str, typing.Any]]
            Filter the response. Use bracket syntax `filters[field][$operator]=value`. Operators: $eq, $eqi, $ne, $nei, $lt, $lte, $gt, $gte, $in, $notIn, $contains, $notContains, $containsi, $notContainsi, $startsWith, $startsWithi, $endsWith, $endsWithi, $null, $notNull, $between, $or, $and, $not.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntryListResponse
            Paginated list of entries.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collection_type.list_entries(
                api_id="apiId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_entries(
            api_id,
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
            filters=filters,
            request_options=request_options,
        )
        return _response.data

    async def create_entry(
        self,
        api_id: str,
        *,
        data: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntrySingleResponse:
        """
        Create an entry of a collection type. The request body wraps attributes under a `data` key. Not applicable to single types (use PUT). Note: over REST the entry is auto-published even with `status=draft`; verify `publishedAt` on the response.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

        data : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntrySingleResponse
            Created entry.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collection_type.create_entry(
                api_id="apiId",
                data={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_entry(api_id, data=data, request_options=request_options)
        return _response.data

    async def get_entry(
        self,
        api_id: str,
        document_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        populate: typing.Optional[GetEntryRequestPopulate] = None,
        status: typing.Optional[GetEntryRequestStatus] = None,
        locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntrySingleResponse:
        """
        Retrieve a single collection-type entry by its `documentId`.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Select only specific fields to return, e.g. `fields[0]=title&fields[1]=description`. Does not apply to relational/media/component/dynamic-zone fields.

        populate : typing.Optional[GetEntryRequestPopulate]
            Populate relations, media, components, and dynamic zones (excluded by default). `populate=*` for all one level deep, or bracket syntax for specific/nested relations.

        status : typing.Optional[GetEntryRequestStatus]
            Select the Draft & Publish status on reads.

        locale : typing.Optional[str]
            Select a locale (i18n plugin).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntrySingleResponse
            The entry.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collection_type.get_entry(
                api_id="apiId",
                document_id="documentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_entry(
            api_id,
            document_id,
            fields=fields,
            populate=populate,
            status=status,
            locale=locale,
            request_options=request_options,
        )
        return _response.data

    async def update_entry(
        self,
        api_id: str,
        document_id: str,
        *,
        data: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntrySingleResponse:
        """
        Partially update a collection-type entry by `documentId`. Note: updating over REST publishes the entry; there is no REST route to unpublish.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        data : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntrySingleResponse
            Updated entry.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collection_type.update_entry(
                api_id="apiId",
                document_id="documentId",
                data={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_entry(api_id, document_id, data=data, request_options=request_options)
        return _response.data

    async def delete_entry(
        self, api_id: str, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a collection-type entry by `documentId`.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

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
            await client.collection_type.delete_entry(
                api_id="apiId",
                document_id="documentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_entry(api_id, document_id, request_options=request_options)
        return _response.data
