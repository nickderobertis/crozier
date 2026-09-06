

from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCollectionsClient, RawCollectionsClient
from .types.create_collections_request_fields_item import CreateCollectionsRequestFieldsItem
from .types.create_collections_response import CreateCollectionsResponse
from .types.get_collections_response import GetCollectionsResponse
from .types.list_collections_response import ListCollectionsResponse
from .types.patch_collections_request_field_groups_item import PatchCollectionsRequestFieldGroupsItem
from .types.patch_collections_response import PatchCollectionsResponse

if typing.TYPE_CHECKING:
    from .fields.client import AsyncFieldsClient, FieldsClient
    from .items.client import AsyncItemsClient, ItemsClient

OMIT = typing.cast(typing.Any, ...)


class CollectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCollectionsClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._fields: typing.Optional[FieldsClient] = None
        self._items: typing.Optional[ItemsClient] = None

    @property
    def with_raw_response(self) -> RawCollectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCollectionsClient
        """
        return self._raw_client

    def list(self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ListCollectionsResponse:
        """
        List of all Collections within a Site.

        Required scope | `cms:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCollectionsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collections.list(
            site_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.list(site_id, request_options=request_options)
        return _response.data

    def create(
        self,
        site_id: str,
        *,
        display_name: str,
        singular_name: str,
        slug: typing.Optional[str] = OMIT,
        fields: typing.Optional[typing.Sequence[CreateCollectionsRequestFieldsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCollectionsResponse:
        """
        Create a Collection for a site with collection fields.

        Each collection includes the required _name_ and _slug_ fields, which are generated automatically. You can update the `displayName` of these fields, but the slug for them cannot be changed. Fields slugs are automatically converted to lowercase. Spaces in slugs are replaced with hyphens.

        Required scope | `cms:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        display_name : str
            Name of the collection. Each collection name must be distinct.

        singular_name : str
            Singular name of each item.

        slug : typing.Optional[str]
            Part of a URL that identifier

        fields : typing.Optional[typing.Sequence[CreateCollectionsRequestFieldsItem]]
            An array of custom fields to add to the collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCollectionsResponse
            Request was successful

        Examples
        --------
        from fern.collections import (
            ReferenceField,
            ReferenceFieldMetadata,
            ReferenceFieldType,
            StaticField,
            StaticFieldType,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collections.create(
            site_id="580e63e98c9a982ac9b8b741",
            display_name="Blog Posts",
            singular_name="Blog Post",
            slug="posts",
            fields=[
                StaticField(
                    is_required=True,
                    type=StaticFieldType.PLAIN_TEXT,
                    display_name="Title",
                    help_text="The title of the blog post",
                ),
                StaticField(
                    is_required=True,
                    type=StaticFieldType.RICH_TEXT,
                    display_name="Content",
                    help_text="The content of the blog post",
                ),
                ReferenceField(
                    is_required=True,
                    type=ReferenceFieldType.REFERENCE,
                    display_name="Author",
                    help_text="The author of the blog post",
                    metadata=ReferenceFieldMetadata(
                        collection_id="23cc2d952d4e4631ffd4345d2743db4e",
                    ),
                ),
            ],
        )
        """
        _response = self._raw_client.create(
            site_id,
            display_name=display_name,
            singular_name=singular_name,
            slug=slug,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    def get(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCollectionsResponse:
        """
        Get the full details of a collection from its ID.

        Required scope | `cms:read`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCollectionsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collections.get(
            collection_id="580e63fc8c9a982ac9b8b745",
        )
        """
        _response = self._raw_client.get(collection_id, request_options=request_options)
        return _response.data

    def delete(self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a collection using its ID.

        Required scope | `cms:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

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
        client.collections.delete(
            collection_id="580e63fc8c9a982ac9b8b745",
        )
        """
        _response = self._raw_client.delete(collection_id, request_options=request_options)
        return _response.data

    def patch(
        self,
        collection_id: str,
        *,
        display_name: typing.Optional[str] = OMIT,
        singular_name: typing.Optional[str] = OMIT,
        slug: typing.Optional[str] = OMIT,
        field_groups: typing.Optional[typing.Sequence[PatchCollectionsRequestFieldGroupsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatchCollectionsResponse:
        """
        Update a collection's display name, singular name, slug, or field groups.

        **Field group rules:**
        - A collection can have a maximum of 50 field groups
        - Each `displayName` must be unique across all field groups in the collection
        - Each `fieldId` must be unique across all field groups in the collection
        - Ecommerce collections do not support field groups

        Required scope | `cms:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        display_name : typing.Optional[str]
            Name given to the Collection

        singular_name : typing.Optional[str]
            The name of one Item in Collection (e.g. ”Blog Post” if the Collection is called “Blog Posts”)

        slug : typing.Optional[str]
            Slug of Collection in Site URL structure

        field_groups : typing.Optional[typing.Sequence[PatchCollectionsRequestFieldGroupsItem]]
            The list of field groups in the Collection. Replaces the existing field groups.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchCollectionsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collections.patch(
            collection_id="580e63fc8c9a982ac9b8b745",
        )
        """
        _response = self._raw_client.patch(
            collection_id,
            display_name=display_name,
            singular_name=singular_name,
            slug=slug,
            field_groups=field_groups,
            request_options=request_options,
        )
        return _response.data

    @property
    def fields(self):
        if self._fields is None:
            from .fields.client import FieldsClient

            self._fields = FieldsClient(client_wrapper=self._client_wrapper)
        return self._fields

    @property
    def items(self):
        if self._items is None:
            from .items.client import ItemsClient

            self._items = ItemsClient(client_wrapper=self._client_wrapper)
        return self._items


class AsyncCollectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCollectionsClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._fields: typing.Optional[AsyncFieldsClient] = None
        self._items: typing.Optional[AsyncItemsClient] = None

    @property
    def with_raw_response(self) -> AsyncRawCollectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCollectionsClient
        """
        return self._raw_client

    async def list(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListCollectionsResponse:
        """
        List of all Collections within a Site.

        Required scope | `cms:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCollectionsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collections.list(
                site_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(site_id, request_options=request_options)
        return _response.data

    async def create(
        self,
        site_id: str,
        *,
        display_name: str,
        singular_name: str,
        slug: typing.Optional[str] = OMIT,
        fields: typing.Optional[typing.Sequence[CreateCollectionsRequestFieldsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCollectionsResponse:
        """
        Create a Collection for a site with collection fields.

        Each collection includes the required _name_ and _slug_ fields, which are generated automatically. You can update the `displayName` of these fields, but the slug for them cannot be changed. Fields slugs are automatically converted to lowercase. Spaces in slugs are replaced with hyphens.

        Required scope | `cms:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        display_name : str
            Name of the collection. Each collection name must be distinct.

        singular_name : str
            Singular name of each item.

        slug : typing.Optional[str]
            Part of a URL that identifier

        fields : typing.Optional[typing.Sequence[CreateCollectionsRequestFieldsItem]]
            An array of custom fields to add to the collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCollectionsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.collections import (
            ReferenceField,
            ReferenceFieldMetadata,
            ReferenceFieldType,
            StaticField,
            StaticFieldType,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collections.create(
                site_id="580e63e98c9a982ac9b8b741",
                display_name="Blog Posts",
                singular_name="Blog Post",
                slug="posts",
                fields=[
                    StaticField(
                        is_required=True,
                        type=StaticFieldType.PLAIN_TEXT,
                        display_name="Title",
                        help_text="The title of the blog post",
                    ),
                    StaticField(
                        is_required=True,
                        type=StaticFieldType.RICH_TEXT,
                        display_name="Content",
                        help_text="The content of the blog post",
                    ),
                    ReferenceField(
                        is_required=True,
                        type=ReferenceFieldType.REFERENCE,
                        display_name="Author",
                        help_text="The author of the blog post",
                        metadata=ReferenceFieldMetadata(
                            collection_id="23cc2d952d4e4631ffd4345d2743db4e",
                        ),
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            site_id,
            display_name=display_name,
            singular_name=singular_name,
            slug=slug,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    async def get(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCollectionsResponse:
        """
        Get the full details of a collection from its ID.

        Required scope | `cms:read`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCollectionsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collections.get(
                collection_id="580e63fc8c9a982ac9b8b745",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(collection_id, request_options=request_options)
        return _response.data

    async def delete(self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a collection using its ID.

        Required scope | `cms:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

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
            await client.collections.delete(
                collection_id="580e63fc8c9a982ac9b8b745",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(collection_id, request_options=request_options)
        return _response.data

    async def patch(
        self,
        collection_id: str,
        *,
        display_name: typing.Optional[str] = OMIT,
        singular_name: typing.Optional[str] = OMIT,
        slug: typing.Optional[str] = OMIT,
        field_groups: typing.Optional[typing.Sequence[PatchCollectionsRequestFieldGroupsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatchCollectionsResponse:
        """
        Update a collection's display name, singular name, slug, or field groups.

        **Field group rules:**
        - A collection can have a maximum of 50 field groups
        - Each `displayName` must be unique across all field groups in the collection
        - Each `fieldId` must be unique across all field groups in the collection
        - Ecommerce collections do not support field groups

        Required scope | `cms:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        display_name : typing.Optional[str]
            Name given to the Collection

        singular_name : typing.Optional[str]
            The name of one Item in Collection (e.g. ”Blog Post” if the Collection is called “Blog Posts”)

        slug : typing.Optional[str]
            Slug of Collection in Site URL structure

        field_groups : typing.Optional[typing.Sequence[PatchCollectionsRequestFieldGroupsItem]]
            The list of field groups in the Collection. Replaces the existing field groups.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchCollectionsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collections.patch(
                collection_id="580e63fc8c9a982ac9b8b745",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch(
            collection_id,
            display_name=display_name,
            singular_name=singular_name,
            slug=slug,
            field_groups=field_groups,
            request_options=request_options,
        )
        return _response.data

    @property
    def fields(self):
        if self._fields is None:
            from .fields.client import AsyncFieldsClient

            self._fields = AsyncFieldsClient(client_wrapper=self._client_wrapper)
        return self._fields

    @property
    def items(self):
        if self._items is None:
            from .items.client import AsyncItemsClient

            self._items = AsyncItemsClient(client_wrapper=self._client_wrapper)
        return self._items
