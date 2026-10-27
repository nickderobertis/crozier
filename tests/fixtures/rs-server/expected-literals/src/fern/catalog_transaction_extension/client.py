

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.asset import Asset
from ..types.collection_input_summaries_value import CollectionInputSummariesValue
from ..types.collection_input_type import CollectionInputType
from ..types.extent import Extent
from ..types.item_input_geometry import ItemInputGeometry
from ..types.item_input_type import ItemInputType
from ..types.item_properties import ItemProperties
from ..types.links_input import LinksInput
from ..types.provider import Provider
from ..types.stac_pydantic_collection_collection_output import StacPydanticCollectionCollectionOutput
from ..types.stac_pydantic_item_item_output import StacPydanticItemItemOutput
from .raw_client import AsyncRawCatalogTransactionExtensionClient, RawCatalogTransactionExtensionClient
from .types.create_item_catalog_collections_collection_id_items_post_request_body import (
    CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody,
)
from .types.patch_collection_catalog_collections_collection_id_patch_request_body import (
    PatchCollectionCatalogCollectionsCollectionIdPatchRequestBody,
)
from .types.patch_item_catalog_collections_collection_id_items_item_id_patch_request_body import (
    PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBody,
)


OMIT = typing.cast(typing.Any, ...)


class CatalogTransactionExtensionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCatalogTransactionExtensionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCatalogTransactionExtensionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCatalogTransactionExtensionClient
        """
        return self._raw_client

    def update_item(
        self,
        collection_id: str,
        item_id: str,
        *,
        type: ItemInputType,
        properties: ItemProperties,
        id: str,
        assets: typing.Dict[str, Asset],
        links: LinksInput,
        bbox: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        geometry: typing.Optional[ItemInputGeometry] = OMIT,
        stac_version: typing.Optional[str] = OMIT,
        stac_extensions: typing.Optional[typing.Sequence[str]] = OMIT,
        collection: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StacPydanticItemItemOutput:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        item_id : str
            Item ID

        type : ItemInputType

        properties : ItemProperties

        id : str

        assets : typing.Dict[str, Asset]

        links : LinksInput

        bbox : typing.Optional[typing.Sequence[typing.Any]]

        geometry : typing.Optional[ItemInputGeometry]

        stac_version : typing.Optional[str]

        stac_extensions : typing.Optional[typing.Sequence[str]]

        collection : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StacPydanticItemItemOutput
            Successful Response

        Examples
        --------
        from fern import Asset, FernApi, ItemProperties, Link

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.catalog_transaction_extension.update_item(
            collection_id="collection_id",
            item_id="item_id",
            type="Feature",
            properties=ItemProperties(),
            id="id",
            assets={
                "key": Asset(
                    href="href",
                )
            },
            links=[
                Link(
                    href="href",
                    rel="rel",
                )
            ],
        )
        """
        _response = self._raw_client.update_item(
            collection_id,
            item_id,
            type=type,
            properties=properties,
            id=id,
            assets=assets,
            links=links,
            bbox=bbox,
            geometry=geometry,
            stac_version=stac_version,
            stac_extensions=stac_extensions,
            collection=collection,
            request_options=request_options,
        )
        return _response.data

    def delete_item(
        self, collection_id: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StacPydanticItemItemOutput:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        item_id : str
            Item ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StacPydanticItemItemOutput
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.catalog_transaction_extension.delete_item(
            collection_id="collection_id",
            item_id="item_id",
        )
        """
        _response = self._raw_client.delete_item(collection_id, item_id, request_options=request_options)
        return _response.data

    def patch_item(
        self,
        collection_id: str,
        item_id: str,
        *,
        request: PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StacPydanticItemItemOutput:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        item_id : str
            Item ID

        request : PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StacPydanticItemItemOutput
            Successful Response

        Examples
        --------
        from fern import FernApi, PartialItem

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.catalog_transaction_extension.patch_item(
            collection_id="collection_id",
            item_id="item_id",
            request=PartialItem(),
        )
        """
        _response = self._raw_client.patch_item(
            collection_id, item_id, request=request, request_options=request_options
        )
        return _response.data

    def create_collection(
        self,
        *,
        id: str,
        description: str,
        links: LinksInput,
        type: CollectionInputType,
        license: str,
        extent: Extent,
        stac_version: typing.Optional[str] = OMIT,
        stac_extensions: typing.Optional[typing.Sequence[str]] = OMIT,
        title: typing.Optional[str] = OMIT,
        assets: typing.Optional[typing.Dict[str, typing.Optional[Asset]]] = OMIT,
        keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        providers: typing.Optional[typing.Sequence[Provider]] = OMIT,
        summaries: typing.Optional[typing.Dict[str, typing.Optional[CollectionInputSummariesValue]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StacPydanticCollectionCollectionOutput:
        """
        Endpoint.

        Parameters
        ----------
        id : str

        description : str

        links : LinksInput

        type : CollectionInputType

        license : str

        extent : Extent

        stac_version : typing.Optional[str]

        stac_extensions : typing.Optional[typing.Sequence[str]]

        title : typing.Optional[str]

        assets : typing.Optional[typing.Dict[str, typing.Optional[Asset]]]

        keywords : typing.Optional[typing.Sequence[str]]

        providers : typing.Optional[typing.Sequence[Provider]]

        summaries : typing.Optional[typing.Dict[str, typing.Optional[CollectionInputSummariesValue]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StacPydanticCollectionCollectionOutput
            Successful Response

        Examples
        --------
        from fern import Extent, FernApi, Link, SpatialExtent, TimeInterval

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.catalog_transaction_extension.create_collection(
            id="id",
            description="description",
            links=[
                Link(
                    href="href",
                    rel="rel",
                )
            ],
            type="Collection",
            license="license",
            extent=Extent(
                spatial=SpatialExtent(
                    bbox=[[]],
                ),
                temporal=TimeInterval(
                    interval=[[]],
                ),
            ),
        )
        """
        _response = self._raw_client.create_collection(
            id=id,
            description=description,
            links=links,
            type=type,
            license=license,
            extent=extent,
            stac_version=stac_version,
            stac_extensions=stac_extensions,
            title=title,
            assets=assets,
            keywords=keywords,
            providers=providers,
            summaries=summaries,
            request_options=request_options,
        )
        return _response.data

    def update_collection(
        self,
        collection_id: str,
        *,
        id: str,
        description: str,
        links: LinksInput,
        type: CollectionInputType,
        license: str,
        extent: Extent,
        stac_version: typing.Optional[str] = OMIT,
        stac_extensions: typing.Optional[typing.Sequence[str]] = OMIT,
        title: typing.Optional[str] = OMIT,
        assets: typing.Optional[typing.Dict[str, typing.Optional[Asset]]] = OMIT,
        keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        providers: typing.Optional[typing.Sequence[Provider]] = OMIT,
        summaries: typing.Optional[typing.Dict[str, typing.Optional[CollectionInputSummariesValue]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StacPydanticCollectionCollectionOutput:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        id : str

        description : str

        links : LinksInput

        type : CollectionInputType

        license : str

        extent : Extent

        stac_version : typing.Optional[str]

        stac_extensions : typing.Optional[typing.Sequence[str]]

        title : typing.Optional[str]

        assets : typing.Optional[typing.Dict[str, typing.Optional[Asset]]]

        keywords : typing.Optional[typing.Sequence[str]]

        providers : typing.Optional[typing.Sequence[Provider]]

        summaries : typing.Optional[typing.Dict[str, typing.Optional[CollectionInputSummariesValue]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StacPydanticCollectionCollectionOutput
            Successful Response

        Examples
        --------
        from fern import Extent, FernApi, Link, SpatialExtent, TimeInterval

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.catalog_transaction_extension.update_collection(
            collection_id="collection_id",
            id="id",
            description="description",
            links=[
                Link(
                    href="href",
                    rel="rel",
                )
            ],
            type="Collection",
            license="license",
            extent=Extent(
                spatial=SpatialExtent(
                    bbox=[[]],
                ),
                temporal=TimeInterval(
                    interval=[[]],
                ),
            ),
        )
        """
        _response = self._raw_client.update_collection(
            collection_id,
            id=id,
            description=description,
            links=links,
            type=type,
            license=license,
            extent=extent,
            stac_version=stac_version,
            stac_extensions=stac_extensions,
            title=title,
            assets=assets,
            keywords=keywords,
            providers=providers,
            summaries=summaries,
            request_options=request_options,
        )
        return _response.data

    def delete_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StacPydanticCollectionCollectionOutput:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StacPydanticCollectionCollectionOutput
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.catalog_transaction_extension.delete_collection(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.delete_collection(collection_id, request_options=request_options)
        return _response.data

    def patch_collection(
        self,
        collection_id: str,
        *,
        request: PatchCollectionCatalogCollectionsCollectionIdPatchRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StacPydanticCollectionCollectionOutput:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        request : PatchCollectionCatalogCollectionsCollectionIdPatchRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StacPydanticCollectionCollectionOutput
            Successful Response

        Examples
        --------
        from fern import FernApi, PartialCollection

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.catalog_transaction_extension.patch_collection(
            collection_id="collection_id",
            request=PartialCollection(),
        )
        """
        _response = self._raw_client.patch_collection(collection_id, request=request, request_options=request_options)
        return _response.data

    def create_item(
        self,
        collection_id: str,
        *,
        request: CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StacPydanticItemItemOutput:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        request : CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StacPydanticItemItemOutput
            Successful Response

        Examples
        --------
        from fern.catalog_transaction_extension import (
            CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody_Feature,
        )

        from fern import Asset, FernApi, ItemProperties, Link

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.catalog_transaction_extension.create_item(
            collection_id="collection_id",
            request=CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody_Feature(
                type="Feature",
                properties=ItemProperties(),
                id="id",
                assets={
                    "key": Asset(
                        href="href",
                    )
                },
                links=[
                    Link(
                        href="href",
                        rel="rel",
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.create_item(collection_id, request=request, request_options=request_options)
        return _response.data


class AsyncCatalogTransactionExtensionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCatalogTransactionExtensionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCatalogTransactionExtensionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCatalogTransactionExtensionClient
        """
        return self._raw_client

    async def update_item(
        self,
        collection_id: str,
        item_id: str,
        *,
        type: ItemInputType,
        properties: ItemProperties,
        id: str,
        assets: typing.Dict[str, Asset],
        links: LinksInput,
        bbox: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        geometry: typing.Optional[ItemInputGeometry] = OMIT,
        stac_version: typing.Optional[str] = OMIT,
        stac_extensions: typing.Optional[typing.Sequence[str]] = OMIT,
        collection: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StacPydanticItemItemOutput:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        item_id : str
            Item ID

        type : ItemInputType

        properties : ItemProperties

        id : str

        assets : typing.Dict[str, Asset]

        links : LinksInput

        bbox : typing.Optional[typing.Sequence[typing.Any]]

        geometry : typing.Optional[ItemInputGeometry]

        stac_version : typing.Optional[str]

        stac_extensions : typing.Optional[typing.Sequence[str]]

        collection : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StacPydanticItemItemOutput
            Successful Response

        Examples
        --------
        import asyncio

        from fern import Asset, AsyncFernApi, ItemProperties, Link

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.catalog_transaction_extension.update_item(
                collection_id="collection_id",
                item_id="item_id",
                type="Feature",
                properties=ItemProperties(),
                id="id",
                assets={
                    "key": Asset(
                        href="href",
                    )
                },
                links=[
                    Link(
                        href="href",
                        rel="rel",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_item(
            collection_id,
            item_id,
            type=type,
            properties=properties,
            id=id,
            assets=assets,
            links=links,
            bbox=bbox,
            geometry=geometry,
            stac_version=stac_version,
            stac_extensions=stac_extensions,
            collection=collection,
            request_options=request_options,
        )
        return _response.data

    async def delete_item(
        self, collection_id: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StacPydanticItemItemOutput:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        item_id : str
            Item ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StacPydanticItemItemOutput
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.catalog_transaction_extension.delete_item(
                collection_id="collection_id",
                item_id="item_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_item(collection_id, item_id, request_options=request_options)
        return _response.data

    async def patch_item(
        self,
        collection_id: str,
        item_id: str,
        *,
        request: PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StacPydanticItemItemOutput:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        item_id : str
            Item ID

        request : PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StacPydanticItemItemOutput
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PartialItem

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.catalog_transaction_extension.patch_item(
                collection_id="collection_id",
                item_id="item_id",
                request=PartialItem(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_item(
            collection_id, item_id, request=request, request_options=request_options
        )
        return _response.data

    async def create_collection(
        self,
        *,
        id: str,
        description: str,
        links: LinksInput,
        type: CollectionInputType,
        license: str,
        extent: Extent,
        stac_version: typing.Optional[str] = OMIT,
        stac_extensions: typing.Optional[typing.Sequence[str]] = OMIT,
        title: typing.Optional[str] = OMIT,
        assets: typing.Optional[typing.Dict[str, typing.Optional[Asset]]] = OMIT,
        keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        providers: typing.Optional[typing.Sequence[Provider]] = OMIT,
        summaries: typing.Optional[typing.Dict[str, typing.Optional[CollectionInputSummariesValue]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StacPydanticCollectionCollectionOutput:
        """
        Endpoint.

        Parameters
        ----------
        id : str

        description : str

        links : LinksInput

        type : CollectionInputType

        license : str

        extent : Extent

        stac_version : typing.Optional[str]

        stac_extensions : typing.Optional[typing.Sequence[str]]

        title : typing.Optional[str]

        assets : typing.Optional[typing.Dict[str, typing.Optional[Asset]]]

        keywords : typing.Optional[typing.Sequence[str]]

        providers : typing.Optional[typing.Sequence[Provider]]

        summaries : typing.Optional[typing.Dict[str, typing.Optional[CollectionInputSummariesValue]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StacPydanticCollectionCollectionOutput
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Extent, Link, SpatialExtent, TimeInterval

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.catalog_transaction_extension.create_collection(
                id="id",
                description="description",
                links=[
                    Link(
                        href="href",
                        rel="rel",
                    )
                ],
                type="Collection",
                license="license",
                extent=Extent(
                    spatial=SpatialExtent(
                        bbox=[[]],
                    ),
                    temporal=TimeInterval(
                        interval=[[]],
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_collection(
            id=id,
            description=description,
            links=links,
            type=type,
            license=license,
            extent=extent,
            stac_version=stac_version,
            stac_extensions=stac_extensions,
            title=title,
            assets=assets,
            keywords=keywords,
            providers=providers,
            summaries=summaries,
            request_options=request_options,
        )
        return _response.data

    async def update_collection(
        self,
        collection_id: str,
        *,
        id: str,
        description: str,
        links: LinksInput,
        type: CollectionInputType,
        license: str,
        extent: Extent,
        stac_version: typing.Optional[str] = OMIT,
        stac_extensions: typing.Optional[typing.Sequence[str]] = OMIT,
        title: typing.Optional[str] = OMIT,
        assets: typing.Optional[typing.Dict[str, typing.Optional[Asset]]] = OMIT,
        keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        providers: typing.Optional[typing.Sequence[Provider]] = OMIT,
        summaries: typing.Optional[typing.Dict[str, typing.Optional[CollectionInputSummariesValue]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StacPydanticCollectionCollectionOutput:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        id : str

        description : str

        links : LinksInput

        type : CollectionInputType

        license : str

        extent : Extent

        stac_version : typing.Optional[str]

        stac_extensions : typing.Optional[typing.Sequence[str]]

        title : typing.Optional[str]

        assets : typing.Optional[typing.Dict[str, typing.Optional[Asset]]]

        keywords : typing.Optional[typing.Sequence[str]]

        providers : typing.Optional[typing.Sequence[Provider]]

        summaries : typing.Optional[typing.Dict[str, typing.Optional[CollectionInputSummariesValue]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StacPydanticCollectionCollectionOutput
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Extent, Link, SpatialExtent, TimeInterval

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.catalog_transaction_extension.update_collection(
                collection_id="collection_id",
                id="id",
                description="description",
                links=[
                    Link(
                        href="href",
                        rel="rel",
                    )
                ],
                type="Collection",
                license="license",
                extent=Extent(
                    spatial=SpatialExtent(
                        bbox=[[]],
                    ),
                    temporal=TimeInterval(
                        interval=[[]],
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_collection(
            collection_id,
            id=id,
            description=description,
            links=links,
            type=type,
            license=license,
            extent=extent,
            stac_version=stac_version,
            stac_extensions=stac_extensions,
            title=title,
            assets=assets,
            keywords=keywords,
            providers=providers,
            summaries=summaries,
            request_options=request_options,
        )
        return _response.data

    async def delete_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StacPydanticCollectionCollectionOutput:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StacPydanticCollectionCollectionOutput
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.catalog_transaction_extension.delete_collection(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_collection(collection_id, request_options=request_options)
        return _response.data

    async def patch_collection(
        self,
        collection_id: str,
        *,
        request: PatchCollectionCatalogCollectionsCollectionIdPatchRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StacPydanticCollectionCollectionOutput:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        request : PatchCollectionCatalogCollectionsCollectionIdPatchRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StacPydanticCollectionCollectionOutput
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PartialCollection

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.catalog_transaction_extension.patch_collection(
                collection_id="collection_id",
                request=PartialCollection(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_collection(
            collection_id, request=request, request_options=request_options
        )
        return _response.data

    async def create_item(
        self,
        collection_id: str,
        *,
        request: CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StacPydanticItemItemOutput:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        request : CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StacPydanticItemItemOutput
            Successful Response

        Examples
        --------
        import asyncio

        from fern.catalog_transaction_extension import (
            CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody_Feature,
        )

        from fern import Asset, AsyncFernApi, ItemProperties, Link

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.catalog_transaction_extension.create_item(
                collection_id="collection_id",
                request=CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody_Feature(
                    type="Feature",
                    properties=ItemProperties(),
                    id="id",
                    assets={
                        "key": Asset(
                            href="href",
                        )
                    },
                    links=[
                        Link(
                            href="href",
                            rel="rel",
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_item(collection_id, request=request, request_options=request_options)
        return _response.data
