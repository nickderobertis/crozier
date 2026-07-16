

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.batch_delete_catalog_objects_response import BatchDeleteCatalogObjectsResponse
from ..types.batch_retrieve_catalog_objects_response import BatchRetrieveCatalogObjectsResponse
from ..types.batch_upsert_catalog_objects_response import BatchUpsertCatalogObjectsResponse
from ..types.catalog_info_response import CatalogInfoResponse
from ..types.catalog_object import CatalogObject
from ..types.catalog_object_batch import CatalogObjectBatch
from ..types.catalog_query import CatalogQuery
from ..types.custom_attribute_filter import CustomAttributeFilter
from ..types.delete_catalog_object_response import DeleteCatalogObjectResponse
from ..types.list_catalog_response import ListCatalogResponse
from ..types.retrieve_catalog_object_response import RetrieveCatalogObjectResponse
from ..types.search_catalog_items_response import SearchCatalogItemsResponse
from ..types.search_catalog_objects_response import SearchCatalogObjectsResponse
from ..types.update_item_modifier_lists_response import UpdateItemModifierListsResponse
from ..types.update_item_taxes_response import UpdateItemTaxesResponse
from ..types.upsert_catalog_object_response import UpsertCatalogObjectResponse
from .raw_client import AsyncRawCatalogClient, RawCatalogClient


OMIT = typing.cast(typing.Any, ...)


class CatalogClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCatalogClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCatalogClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCatalogClient
        """
        return self._raw_client

    def batch_delete_catalog_objects(
        self,
        *,
        object_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchDeleteCatalogObjectsResponse:
        """
        Deletes a set of [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem)s based on the
        provided list of target IDs and returns a set of successfully deleted IDs in
        the response. Deletion is a cascading event such that all children of the
        targeted object are also deleted. For example, deleting a CatalogItem will
        also delete all of its [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation)
        children.

        `BatchDeleteCatalogObjects` succeeds even if only a portion of the targeted
        IDs can be deleted. The response will only include IDs that were
        actually deleted.

        Parameters
        ----------
        object_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the CatalogObjects to be deleted. When an object is deleted, other objects
            in the graph that depend on that object will be deleted as well (for example, deleting a
            CatalogItem will delete its CatalogItemVariation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchDeleteCatalogObjectsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.catalog.batch_delete_catalog_objects()
        """
        _response = self._raw_client.batch_delete_catalog_objects(
            object_ids=object_ids, request_options=request_options
        )
        return _response.data

    def batch_retrieve_catalog_objects(
        self,
        *,
        object_ids: typing.Sequence[str],
        catalog_version: typing.Optional[int] = OMIT,
        include_related_objects: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchRetrieveCatalogObjectsResponse:
        """
        Returns a set of objects based on the provided ID.
        Each [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) returned in the set includes all of its
        child information including: all of its
        [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) objects, references to
        its [CatalogModifierList](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogModifierList) objects, and the ids of
        any [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax) objects that apply to it.

        Parameters
        ----------
        object_ids : typing.Sequence[str]
            The IDs of the CatalogObjects to be retrieved.

        catalog_version : typing.Optional[int]
            The specific version of the catalog objects to be included in the response.
            This allows you to retrieve historical versions of objects. The specified version value is matched against
            the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s' `version` attribute.

        include_related_objects : typing.Optional[bool]
            If `true`, the response will include additional objects that are related to the
            requested objects, as follows:

            If the `objects` field of the response contains a CatalogItem, its associated
            CatalogCategory objects, CatalogTax objects, CatalogImage objects and
            CatalogModifierLists will be returned in the `related_objects` field of the
            response. If the `objects` field of the response contains a CatalogItemVariation,
            its parent CatalogItem will be returned in the `related_objects` field of
            the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchRetrieveCatalogObjectsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.catalog.batch_retrieve_catalog_objects(
            object_ids=["object_ids"],
        )
        """
        _response = self._raw_client.batch_retrieve_catalog_objects(
            object_ids=object_ids,
            catalog_version=catalog_version,
            include_related_objects=include_related_objects,
            request_options=request_options,
        )
        return _response.data

    def batch_upsert_catalog_objects(
        self,
        *,
        batches: typing.Sequence[CatalogObjectBatch],
        idempotency_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchUpsertCatalogObjectsResponse:
        """
        Creates or updates up to 10,000 target objects based on the provided
        list of objects. The target objects are grouped into batches and each batch is
        inserted/updated in an all-or-nothing manner. If an object within a batch is
        malformed in some way, or violates a database constraint, the entire batch
        containing that item will be disregarded. However, other batches in the same
        request may still succeed. Each batch may contain up to 1,000 objects, and
        batches will be processed in order as long as the total object count for the
        request (items, variations, modifier lists, discounts, and taxes) is no more
        than 10,000.

        Parameters
        ----------
        batches : typing.Sequence[CatalogObjectBatch]
            A batch of CatalogObjects to be inserted/updated atomically.
            The objects within a batch will be inserted in an all-or-nothing fashion, i.e., if an error occurs
            attempting to insert or update an object within a batch, the entire batch will be rejected. However, an error
            in one batch will not affect other batches within the same request.

            For each object, its `updated_at` field is ignored and replaced with a current [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates), and its
            `is_deleted` field must not be set to `true`.

            To modify an existing object, supply its ID. To create a new object, use an ID starting
            with `#`. These IDs may be used to create relationships between an object and attributes of
            other objects that reference it. For example, you can create a CatalogItem with
            ID `#ABC` and a CatalogItemVariation with its `item_id` attribute set to
            `#ABC` in order to associate the CatalogItemVariation with its parent
            CatalogItem.

            Any `#`-prefixed IDs are valid only within a single atomic batch, and will be replaced by server-generated IDs.

            Each batch may contain up to 1,000 objects. The total number of objects across all batches for a single request
            may not exceed 10,000. If either of these limits is violated, an error will be returned and no objects will
            be inserted or updated.

        idempotency_key : str
            A value you specify that uniquely identifies this
            request among all your requests. A common way to create
            a valid idempotency key is to use a Universally unique
            identifier (UUID).

            If you're unsure whether a particular request was successful,
            you can reattempt it with the same idempotency key without
            worrying about creating duplicate objects.

            See [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchUpsertCatalogObjectsResponse
            Success

        Examples
        --------
        from fern import CatalogObject, CatalogObjectBatch, FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.catalog.batch_upsert_catalog_objects(
            batches=[
                CatalogObjectBatch(
                    objects=[
                        CatalogObject(
                            id="id",
                            type="type",
                        )
                    ],
                )
            ],
            idempotency_key="idempotency_key",
        )
        """
        _response = self._raw_client.batch_upsert_catalog_objects(
            batches=batches, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    def catalog_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> CatalogInfoResponse:
        """
        Retrieves information about the Square Catalog API, such as batch size
        limits that can be used by the `BatchUpsertCatalogObjects` endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CatalogInfoResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.catalog.catalog_info()
        """
        _response = self._raw_client.catalog_info(request_options=request_options)
        return _response.data

    def list_catalog(
        self,
        *,
        cursor: typing.Optional[str] = None,
        types: typing.Optional[str] = None,
        catalog_version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCatalogResponse:
        """
        Returns a list of [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s that includes
        all objects of a set of desired types (for example, all [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem)
        and [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax) objects) in the catalog. The `types` parameter
        is specified as a comma-separated list of valid [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) types:
        `ITEM`, `ITEM_VARIATION`, `MODIFIER`, `MODIFIER_LIST`, `CATEGORY`, `DISCOUNT`, `TAX`, `IMAGE`.

        __Important:__ ListCatalog does not return deleted catalog items. To retrieve
        deleted catalog items, use [SearchCatalogObjects](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-objects)
        and set the `include_deleted_objects` attribute value to `true`.

        Parameters
        ----------
        cursor : typing.Optional[str]
            The pagination cursor returned in the previous response. Leave unset for an initial request.
            The page size is currently set to be 100.
            See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.

        types : typing.Optional[str]
            An optional case-insensitive, comma-separated list of object types to retrieve.

            The valid values are defined in the [CatalogObjectType](https://developer.squareup.com/reference/square_2021-08-18/enums/CatalogObjectType) enum, including
            `ITEM`, `ITEM_VARIATION`, `CATEGORY`, `DISCOUNT`, `TAX`,
            `MODIFIER`, `MODIFIER_LIST`, or `IMAGE`.

            If this is unspecified, the operation returns objects of all the types at the version of the Square API used to make the request.

        catalog_version : typing.Optional[int]
            The specific version of the catalog objects to be included in the response.
            This allows you to retrieve historical
            versions of objects. The specified version value is matched against
            the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s' `version` attribute.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCatalogResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.catalog.list_catalog()
        """
        _response = self._raw_client.list_catalog(
            cursor=cursor, types=types, catalog_version=catalog_version, request_options=request_options
        )
        return _response.data

    def upsert_catalog_object(
        self, *, idempotency_key: str, object: CatalogObject, request_options: typing.Optional[RequestOptions] = None
    ) -> UpsertCatalogObjectResponse:
        """
        Creates or updates the target [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject).

        Parameters
        ----------
        idempotency_key : str
            A value you specify that uniquely identifies this
            request among all your requests. A common way to create
            a valid idempotency key is to use a Universally unique
            identifier (UUID).

            If you're unsure whether a particular request was successful,
            you can reattempt it with the same idempotency key without
            worrying about creating duplicate objects.

            See [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.

        object : CatalogObject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpsertCatalogObjectResponse
            Success

        Examples
        --------
        from fern import CatalogObject, FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.catalog.upsert_catalog_object(
            idempotency_key="idempotency_key",
            object=CatalogObject(
                id="id",
                type="type",
            ),
        )
        """
        _response = self._raw_client.upsert_catalog_object(
            idempotency_key=idempotency_key, object=object, request_options=request_options
        )
        return _response.data

    def retrieve_catalog_object(
        self,
        object_id: str,
        *,
        include_related_objects: typing.Optional[bool] = None,
        catalog_version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetrieveCatalogObjectResponse:
        """
        Returns a single [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) as a
        [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) based on the provided ID. The returned
        object includes all of the relevant [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem)
        information including: [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation)
        children, references to its
        [CatalogModifierList](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogModifierList) objects, and the ids of
        any [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax) objects that apply to it.

        Parameters
        ----------
        object_id : str
            The object ID of any type of catalog objects to be retrieved.

        include_related_objects : typing.Optional[bool]
            If `true`, the response will include additional objects that are related to the
            requested object, as follows:

            If the `object` field of the response contains a `CatalogItem`, its associated
            `CatalogCategory`, `CatalogTax`, `CatalogImage` and `CatalogModifierList` objects will
            be returned in the `related_objects` field of the response. If the `object` field of
            the response contains a `CatalogItemVariation`, its parent `CatalogItem` will be returned
            in the `related_objects` field of the response.

            Default value: `false`

        catalog_version : typing.Optional[int]
            Requests objects as of a specific version of the catalog. This allows you to retrieve historical
            versions of objects. The value to retrieve a specific version of an object can be found
            in the version field of [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveCatalogObjectResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.catalog.retrieve_catalog_object(
            object_id="object_id",
        )
        """
        _response = self._raw_client.retrieve_catalog_object(
            object_id,
            include_related_objects=include_related_objects,
            catalog_version=catalog_version,
            request_options=request_options,
        )
        return _response.data

    def delete_catalog_object(
        self, object_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteCatalogObjectResponse:
        """
        Deletes a single [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) based on the
        provided ID and returns the set of successfully deleted IDs in the response.
        Deletion is a cascading event such that all children of the targeted object
        are also deleted. For example, deleting a [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem)
        will also delete all of its
        [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) children.

        Parameters
        ----------
        object_id : str
            The ID of the catalog object to be deleted. When an object is deleted, other
            objects in the graph that depend on that object will be deleted as well (for example, deleting a
            catalog item will delete its catalog item variations).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteCatalogObjectResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.catalog.delete_catalog_object(
            object_id="object_id",
        )
        """
        _response = self._raw_client.delete_catalog_object(object_id, request_options=request_options)
        return _response.data

    def search_catalog_objects(
        self,
        *,
        begin_time: typing.Optional[str] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        include_deleted_objects: typing.Optional[bool] = OMIT,
        include_related_objects: typing.Optional[bool] = OMIT,
        limit: typing.Optional[int] = OMIT,
        object_types: typing.Optional[typing.Sequence[str]] = OMIT,
        query: typing.Optional[CatalogQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchCatalogObjectsResponse:
        """
        Searches for [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) of any type by matching supported search attribute values,
        excluding custom attribute values on items or item variations, against one or more of the specified query expressions.

        This (`SearchCatalogObjects`) endpoint differs from the [SearchCatalogItems](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-items)
        endpoint in the following aspects:

        - `SearchCatalogItems` can only search for items or item variations, whereas `SearchCatalogObjects` can search for any type of catalog objects.
        - `SearchCatalogItems` supports the custom attribute query filters to return items or item variations that contain custom attribute values, where `SearchCatalogObjects` does not.
        - `SearchCatalogItems` does not support the `include_deleted_objects` filter to search for deleted items or item variations, whereas `SearchCatalogObjects` does.
        - The both endpoints have different call conventions, including the query filter formats.

        Parameters
        ----------
        begin_time : typing.Optional[str]
            Return objects modified after this [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates), in RFC 3339
            format, e.g., `2016-09-04T23:59:33.123Z`. The timestamp is exclusive - objects with a
            timestamp equal to `begin_time` will not be included in the response.

        cursor : typing.Optional[str]
            The pagination cursor returned in the previous response. Leave unset for an initial request.
            See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.

        include_deleted_objects : typing.Optional[bool]
            If `true`, deleted objects will be included in the results. Deleted objects will have their
            `is_deleted` field set to `true`.

        include_related_objects : typing.Optional[bool]
            If `true`, the response will include additional objects that are related to the
            requested object, as follows:

            If a CatalogItem is returned in the object field of the response,
            its associated CatalogCategory, CatalogTax objects,
            CatalogImage objects and CatalogModifierList objects
            will be included in the `related_objects` field of the response.

            If a CatalogItemVariation is returned in the object field of the
            response, its parent CatalogItem will be included in the `related_objects` field of
            the response.

        limit : typing.Optional[int]
            A limit on the number of results to be returned in a single page. The limit is advisory -
            the implementation may return more or fewer results. If the supplied limit is negative, zero, or
            is higher than the maximum limit of 1,000, it will be ignored.

        object_types : typing.Optional[typing.Sequence[str]]
            The desired set of object types to appear in the search results.

        query : typing.Optional[CatalogQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchCatalogObjectsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.catalog.search_catalog_objects()
        """
        _response = self._raw_client.search_catalog_objects(
            begin_time=begin_time,
            cursor=cursor,
            include_deleted_objects=include_deleted_objects,
            include_related_objects=include_related_objects,
            limit=limit,
            object_types=object_types,
            query=query,
            request_options=request_options,
        )
        return _response.data

    def search_catalog_items(
        self,
        *,
        category_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        custom_attribute_filters: typing.Optional[typing.Sequence[CustomAttributeFilter]] = OMIT,
        enabled_location_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        product_types: typing.Optional[typing.Sequence[str]] = OMIT,
        sort_order: typing.Optional[str] = OMIT,
        stock_levels: typing.Optional[typing.Sequence[str]] = OMIT,
        text_filter: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchCatalogItemsResponse:
        """
        Searches for catalog items or item variations by matching supported search attribute values, including
        custom attribute values, against one or more of the specified query expressions.

        This (`SearchCatalogItems`) endpoint differs from the [SearchCatalogObjects](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-objects)
        endpoint in the following aspects:

        - `SearchCatalogItems` can only search for items or item variations, whereas `SearchCatalogObjects` can search for any type of catalog objects.
        - `SearchCatalogItems` supports the custom attribute query filters to return items or item variations that contain custom attribute values, where `SearchCatalogObjects` does not.
        - `SearchCatalogItems` does not support the `include_deleted_objects` filter to search for deleted items or item variations, whereas `SearchCatalogObjects` does.
        - The both endpoints use different call conventions, including the query filter formats.

        Parameters
        ----------
        category_ids : typing.Optional[typing.Sequence[str]]
            The category id query expression to return items containing the specified category IDs.

        cursor : typing.Optional[str]
            The pagination token, returned in the previous response, used to fetch the next batch of pending results.

        custom_attribute_filters : typing.Optional[typing.Sequence[CustomAttributeFilter]]
            The customer-attribute filter to return items or item variations matching the specified
            custom attribute expressions. A maximum number of 10 custom attribute expressions are supported in
            a single call to the [SearchCatalogItems](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-items) endpoint.

        enabled_location_ids : typing.Optional[typing.Sequence[str]]
            The enabled-location query expression to return items and item variations having specified enabled locations.

        limit : typing.Optional[int]
            The maximum number of results to return per page. The default value is 100.

        product_types : typing.Optional[typing.Sequence[str]]
            The product types query expression to return items or item variations having the specified product types.

        sort_order : typing.Optional[str]
            The order to sort the results by item names. The default sort order is ascending (`ASC`).

        stock_levels : typing.Optional[typing.Sequence[str]]
            The stock-level query expression to return item variations with the specified stock levels.

        text_filter : typing.Optional[str]
            The text filter expression to return items or item variations containing specified text in
            the `name`, `description`, or `abbreviation` attribute value of an item, or in
            the `name`, `sku`, or `upc` attribute value of an item variation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchCatalogItemsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.catalog.search_catalog_items()
        """
        _response = self._raw_client.search_catalog_items(
            category_ids=category_ids,
            cursor=cursor,
            custom_attribute_filters=custom_attribute_filters,
            enabled_location_ids=enabled_location_ids,
            limit=limit,
            product_types=product_types,
            sort_order=sort_order,
            stock_levels=stock_levels,
            text_filter=text_filter,
            request_options=request_options,
        )
        return _response.data

    def update_item_modifier_lists(
        self,
        *,
        item_ids: typing.Sequence[str],
        modifier_lists_to_disable: typing.Optional[typing.Sequence[str]] = OMIT,
        modifier_lists_to_enable: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateItemModifierListsResponse:
        """
        Updates the [CatalogModifierList](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogModifierList) objects
        that apply to the targeted [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) without having
        to perform an upsert on the entire item.

        Parameters
        ----------
        item_ids : typing.Sequence[str]
            The IDs of the catalog items associated with the CatalogModifierList objects being updated.

        modifier_lists_to_disable : typing.Optional[typing.Sequence[str]]
            The IDs of the CatalogModifierList objects to disable for the CatalogItem.

        modifier_lists_to_enable : typing.Optional[typing.Sequence[str]]
            The IDs of the CatalogModifierList objects to enable for the CatalogItem.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateItemModifierListsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.catalog.update_item_modifier_lists(
            item_ids=["item_ids"],
        )
        """
        _response = self._raw_client.update_item_modifier_lists(
            item_ids=item_ids,
            modifier_lists_to_disable=modifier_lists_to_disable,
            modifier_lists_to_enable=modifier_lists_to_enable,
            request_options=request_options,
        )
        return _response.data

    def update_item_taxes(
        self,
        *,
        item_ids: typing.Sequence[str],
        taxes_to_disable: typing.Optional[typing.Sequence[str]] = OMIT,
        taxes_to_enable: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateItemTaxesResponse:
        """
        Updates the [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax) objects that apply to the
        targeted [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) without having to perform an
        upsert on the entire item.

        Parameters
        ----------
        item_ids : typing.Sequence[str]
            IDs for the CatalogItems associated with the CatalogTax objects being updated.

        taxes_to_disable : typing.Optional[typing.Sequence[str]]
            IDs of the CatalogTax objects to disable.

        taxes_to_enable : typing.Optional[typing.Sequence[str]]
            IDs of the CatalogTax objects to enable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateItemTaxesResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.catalog.update_item_taxes(
            item_ids=["item_ids"],
        )
        """
        _response = self._raw_client.update_item_taxes(
            item_ids=item_ids,
            taxes_to_disable=taxes_to_disable,
            taxes_to_enable=taxes_to_enable,
            request_options=request_options,
        )
        return _response.data


class AsyncCatalogClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCatalogClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCatalogClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCatalogClient
        """
        return self._raw_client

    async def batch_delete_catalog_objects(
        self,
        *,
        object_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchDeleteCatalogObjectsResponse:
        """
        Deletes a set of [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem)s based on the
        provided list of target IDs and returns a set of successfully deleted IDs in
        the response. Deletion is a cascading event such that all children of the
        targeted object are also deleted. For example, deleting a CatalogItem will
        also delete all of its [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation)
        children.

        `BatchDeleteCatalogObjects` succeeds even if only a portion of the targeted
        IDs can be deleted. The response will only include IDs that were
        actually deleted.

        Parameters
        ----------
        object_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the CatalogObjects to be deleted. When an object is deleted, other objects
            in the graph that depend on that object will be deleted as well (for example, deleting a
            CatalogItem will delete its CatalogItemVariation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchDeleteCatalogObjectsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog.batch_delete_catalog_objects()


        asyncio.run(main())
        """
        _response = await self._raw_client.batch_delete_catalog_objects(
            object_ids=object_ids, request_options=request_options
        )
        return _response.data

    async def batch_retrieve_catalog_objects(
        self,
        *,
        object_ids: typing.Sequence[str],
        catalog_version: typing.Optional[int] = OMIT,
        include_related_objects: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchRetrieveCatalogObjectsResponse:
        """
        Returns a set of objects based on the provided ID.
        Each [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) returned in the set includes all of its
        child information including: all of its
        [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) objects, references to
        its [CatalogModifierList](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogModifierList) objects, and the ids of
        any [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax) objects that apply to it.

        Parameters
        ----------
        object_ids : typing.Sequence[str]
            The IDs of the CatalogObjects to be retrieved.

        catalog_version : typing.Optional[int]
            The specific version of the catalog objects to be included in the response.
            This allows you to retrieve historical versions of objects. The specified version value is matched against
            the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s' `version` attribute.

        include_related_objects : typing.Optional[bool]
            If `true`, the response will include additional objects that are related to the
            requested objects, as follows:

            If the `objects` field of the response contains a CatalogItem, its associated
            CatalogCategory objects, CatalogTax objects, CatalogImage objects and
            CatalogModifierLists will be returned in the `related_objects` field of the
            response. If the `objects` field of the response contains a CatalogItemVariation,
            its parent CatalogItem will be returned in the `related_objects` field of
            the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchRetrieveCatalogObjectsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog.batch_retrieve_catalog_objects(
                object_ids=["object_ids"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.batch_retrieve_catalog_objects(
            object_ids=object_ids,
            catalog_version=catalog_version,
            include_related_objects=include_related_objects,
            request_options=request_options,
        )
        return _response.data

    async def batch_upsert_catalog_objects(
        self,
        *,
        batches: typing.Sequence[CatalogObjectBatch],
        idempotency_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchUpsertCatalogObjectsResponse:
        """
        Creates or updates up to 10,000 target objects based on the provided
        list of objects. The target objects are grouped into batches and each batch is
        inserted/updated in an all-or-nothing manner. If an object within a batch is
        malformed in some way, or violates a database constraint, the entire batch
        containing that item will be disregarded. However, other batches in the same
        request may still succeed. Each batch may contain up to 1,000 objects, and
        batches will be processed in order as long as the total object count for the
        request (items, variations, modifier lists, discounts, and taxes) is no more
        than 10,000.

        Parameters
        ----------
        batches : typing.Sequence[CatalogObjectBatch]
            A batch of CatalogObjects to be inserted/updated atomically.
            The objects within a batch will be inserted in an all-or-nothing fashion, i.e., if an error occurs
            attempting to insert or update an object within a batch, the entire batch will be rejected. However, an error
            in one batch will not affect other batches within the same request.

            For each object, its `updated_at` field is ignored and replaced with a current [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates), and its
            `is_deleted` field must not be set to `true`.

            To modify an existing object, supply its ID. To create a new object, use an ID starting
            with `#`. These IDs may be used to create relationships between an object and attributes of
            other objects that reference it. For example, you can create a CatalogItem with
            ID `#ABC` and a CatalogItemVariation with its `item_id` attribute set to
            `#ABC` in order to associate the CatalogItemVariation with its parent
            CatalogItem.

            Any `#`-prefixed IDs are valid only within a single atomic batch, and will be replaced by server-generated IDs.

            Each batch may contain up to 1,000 objects. The total number of objects across all batches for a single request
            may not exceed 10,000. If either of these limits is violated, an error will be returned and no objects will
            be inserted or updated.

        idempotency_key : str
            A value you specify that uniquely identifies this
            request among all your requests. A common way to create
            a valid idempotency key is to use a Universally unique
            identifier (UUID).

            If you're unsure whether a particular request was successful,
            you can reattempt it with the same idempotency key without
            worrying about creating duplicate objects.

            See [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchUpsertCatalogObjectsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CatalogObject, CatalogObjectBatch

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog.batch_upsert_catalog_objects(
                batches=[
                    CatalogObjectBatch(
                        objects=[
                            CatalogObject(
                                id="id",
                                type="type",
                            )
                        ],
                    )
                ],
                idempotency_key="idempotency_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.batch_upsert_catalog_objects(
            batches=batches, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    async def catalog_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> CatalogInfoResponse:
        """
        Retrieves information about the Square Catalog API, such as batch size
        limits that can be used by the `BatchUpsertCatalogObjects` endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CatalogInfoResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog.catalog_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.catalog_info(request_options=request_options)
        return _response.data

    async def list_catalog(
        self,
        *,
        cursor: typing.Optional[str] = None,
        types: typing.Optional[str] = None,
        catalog_version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCatalogResponse:
        """
        Returns a list of [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s that includes
        all objects of a set of desired types (for example, all [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem)
        and [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax) objects) in the catalog. The `types` parameter
        is specified as a comma-separated list of valid [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) types:
        `ITEM`, `ITEM_VARIATION`, `MODIFIER`, `MODIFIER_LIST`, `CATEGORY`, `DISCOUNT`, `TAX`, `IMAGE`.

        __Important:__ ListCatalog does not return deleted catalog items. To retrieve
        deleted catalog items, use [SearchCatalogObjects](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-objects)
        and set the `include_deleted_objects` attribute value to `true`.

        Parameters
        ----------
        cursor : typing.Optional[str]
            The pagination cursor returned in the previous response. Leave unset for an initial request.
            The page size is currently set to be 100.
            See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.

        types : typing.Optional[str]
            An optional case-insensitive, comma-separated list of object types to retrieve.

            The valid values are defined in the [CatalogObjectType](https://developer.squareup.com/reference/square_2021-08-18/enums/CatalogObjectType) enum, including
            `ITEM`, `ITEM_VARIATION`, `CATEGORY`, `DISCOUNT`, `TAX`,
            `MODIFIER`, `MODIFIER_LIST`, or `IMAGE`.

            If this is unspecified, the operation returns objects of all the types at the version of the Square API used to make the request.

        catalog_version : typing.Optional[int]
            The specific version of the catalog objects to be included in the response.
            This allows you to retrieve historical
            versions of objects. The specified version value is matched against
            the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s' `version` attribute.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCatalogResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog.list_catalog()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_catalog(
            cursor=cursor, types=types, catalog_version=catalog_version, request_options=request_options
        )
        return _response.data

    async def upsert_catalog_object(
        self, *, idempotency_key: str, object: CatalogObject, request_options: typing.Optional[RequestOptions] = None
    ) -> UpsertCatalogObjectResponse:
        """
        Creates or updates the target [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject).

        Parameters
        ----------
        idempotency_key : str
            A value you specify that uniquely identifies this
            request among all your requests. A common way to create
            a valid idempotency key is to use a Universally unique
            identifier (UUID).

            If you're unsure whether a particular request was successful,
            you can reattempt it with the same idempotency key without
            worrying about creating duplicate objects.

            See [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.

        object : CatalogObject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpsertCatalogObjectResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CatalogObject

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog.upsert_catalog_object(
                idempotency_key="idempotency_key",
                object=CatalogObject(
                    id="id",
                    type="type",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upsert_catalog_object(
            idempotency_key=idempotency_key, object=object, request_options=request_options
        )
        return _response.data

    async def retrieve_catalog_object(
        self,
        object_id: str,
        *,
        include_related_objects: typing.Optional[bool] = None,
        catalog_version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetrieveCatalogObjectResponse:
        """
        Returns a single [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) as a
        [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) based on the provided ID. The returned
        object includes all of the relevant [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem)
        information including: [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation)
        children, references to its
        [CatalogModifierList](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogModifierList) objects, and the ids of
        any [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax) objects that apply to it.

        Parameters
        ----------
        object_id : str
            The object ID of any type of catalog objects to be retrieved.

        include_related_objects : typing.Optional[bool]
            If `true`, the response will include additional objects that are related to the
            requested object, as follows:

            If the `object` field of the response contains a `CatalogItem`, its associated
            `CatalogCategory`, `CatalogTax`, `CatalogImage` and `CatalogModifierList` objects will
            be returned in the `related_objects` field of the response. If the `object` field of
            the response contains a `CatalogItemVariation`, its parent `CatalogItem` will be returned
            in the `related_objects` field of the response.

            Default value: `false`

        catalog_version : typing.Optional[int]
            Requests objects as of a specific version of the catalog. This allows you to retrieve historical
            versions of objects. The value to retrieve a specific version of an object can be found
            in the version field of [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveCatalogObjectResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog.retrieve_catalog_object(
                object_id="object_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_catalog_object(
            object_id,
            include_related_objects=include_related_objects,
            catalog_version=catalog_version,
            request_options=request_options,
        )
        return _response.data

    async def delete_catalog_object(
        self, object_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteCatalogObjectResponse:
        """
        Deletes a single [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) based on the
        provided ID and returns the set of successfully deleted IDs in the response.
        Deletion is a cascading event such that all children of the targeted object
        are also deleted. For example, deleting a [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem)
        will also delete all of its
        [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) children.

        Parameters
        ----------
        object_id : str
            The ID of the catalog object to be deleted. When an object is deleted, other
            objects in the graph that depend on that object will be deleted as well (for example, deleting a
            catalog item will delete its catalog item variations).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteCatalogObjectResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog.delete_catalog_object(
                object_id="object_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_catalog_object(object_id, request_options=request_options)
        return _response.data

    async def search_catalog_objects(
        self,
        *,
        begin_time: typing.Optional[str] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        include_deleted_objects: typing.Optional[bool] = OMIT,
        include_related_objects: typing.Optional[bool] = OMIT,
        limit: typing.Optional[int] = OMIT,
        object_types: typing.Optional[typing.Sequence[str]] = OMIT,
        query: typing.Optional[CatalogQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchCatalogObjectsResponse:
        """
        Searches for [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) of any type by matching supported search attribute values,
        excluding custom attribute values on items or item variations, against one or more of the specified query expressions.

        This (`SearchCatalogObjects`) endpoint differs from the [SearchCatalogItems](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-items)
        endpoint in the following aspects:

        - `SearchCatalogItems` can only search for items or item variations, whereas `SearchCatalogObjects` can search for any type of catalog objects.
        - `SearchCatalogItems` supports the custom attribute query filters to return items or item variations that contain custom attribute values, where `SearchCatalogObjects` does not.
        - `SearchCatalogItems` does not support the `include_deleted_objects` filter to search for deleted items or item variations, whereas `SearchCatalogObjects` does.
        - The both endpoints have different call conventions, including the query filter formats.

        Parameters
        ----------
        begin_time : typing.Optional[str]
            Return objects modified after this [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates), in RFC 3339
            format, e.g., `2016-09-04T23:59:33.123Z`. The timestamp is exclusive - objects with a
            timestamp equal to `begin_time` will not be included in the response.

        cursor : typing.Optional[str]
            The pagination cursor returned in the previous response. Leave unset for an initial request.
            See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.

        include_deleted_objects : typing.Optional[bool]
            If `true`, deleted objects will be included in the results. Deleted objects will have their
            `is_deleted` field set to `true`.

        include_related_objects : typing.Optional[bool]
            If `true`, the response will include additional objects that are related to the
            requested object, as follows:

            If a CatalogItem is returned in the object field of the response,
            its associated CatalogCategory, CatalogTax objects,
            CatalogImage objects and CatalogModifierList objects
            will be included in the `related_objects` field of the response.

            If a CatalogItemVariation is returned in the object field of the
            response, its parent CatalogItem will be included in the `related_objects` field of
            the response.

        limit : typing.Optional[int]
            A limit on the number of results to be returned in a single page. The limit is advisory -
            the implementation may return more or fewer results. If the supplied limit is negative, zero, or
            is higher than the maximum limit of 1,000, it will be ignored.

        object_types : typing.Optional[typing.Sequence[str]]
            The desired set of object types to appear in the search results.

        query : typing.Optional[CatalogQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchCatalogObjectsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog.search_catalog_objects()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_catalog_objects(
            begin_time=begin_time,
            cursor=cursor,
            include_deleted_objects=include_deleted_objects,
            include_related_objects=include_related_objects,
            limit=limit,
            object_types=object_types,
            query=query,
            request_options=request_options,
        )
        return _response.data

    async def search_catalog_items(
        self,
        *,
        category_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        custom_attribute_filters: typing.Optional[typing.Sequence[CustomAttributeFilter]] = OMIT,
        enabled_location_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        product_types: typing.Optional[typing.Sequence[str]] = OMIT,
        sort_order: typing.Optional[str] = OMIT,
        stock_levels: typing.Optional[typing.Sequence[str]] = OMIT,
        text_filter: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchCatalogItemsResponse:
        """
        Searches for catalog items or item variations by matching supported search attribute values, including
        custom attribute values, against one or more of the specified query expressions.

        This (`SearchCatalogItems`) endpoint differs from the [SearchCatalogObjects](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-objects)
        endpoint in the following aspects:

        - `SearchCatalogItems` can only search for items or item variations, whereas `SearchCatalogObjects` can search for any type of catalog objects.
        - `SearchCatalogItems` supports the custom attribute query filters to return items or item variations that contain custom attribute values, where `SearchCatalogObjects` does not.
        - `SearchCatalogItems` does not support the `include_deleted_objects` filter to search for deleted items or item variations, whereas `SearchCatalogObjects` does.
        - The both endpoints use different call conventions, including the query filter formats.

        Parameters
        ----------
        category_ids : typing.Optional[typing.Sequence[str]]
            The category id query expression to return items containing the specified category IDs.

        cursor : typing.Optional[str]
            The pagination token, returned in the previous response, used to fetch the next batch of pending results.

        custom_attribute_filters : typing.Optional[typing.Sequence[CustomAttributeFilter]]
            The customer-attribute filter to return items or item variations matching the specified
            custom attribute expressions. A maximum number of 10 custom attribute expressions are supported in
            a single call to the [SearchCatalogItems](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-items) endpoint.

        enabled_location_ids : typing.Optional[typing.Sequence[str]]
            The enabled-location query expression to return items and item variations having specified enabled locations.

        limit : typing.Optional[int]
            The maximum number of results to return per page. The default value is 100.

        product_types : typing.Optional[typing.Sequence[str]]
            The product types query expression to return items or item variations having the specified product types.

        sort_order : typing.Optional[str]
            The order to sort the results by item names. The default sort order is ascending (`ASC`).

        stock_levels : typing.Optional[typing.Sequence[str]]
            The stock-level query expression to return item variations with the specified stock levels.

        text_filter : typing.Optional[str]
            The text filter expression to return items or item variations containing specified text in
            the `name`, `description`, or `abbreviation` attribute value of an item, or in
            the `name`, `sku`, or `upc` attribute value of an item variation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchCatalogItemsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog.search_catalog_items()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_catalog_items(
            category_ids=category_ids,
            cursor=cursor,
            custom_attribute_filters=custom_attribute_filters,
            enabled_location_ids=enabled_location_ids,
            limit=limit,
            product_types=product_types,
            sort_order=sort_order,
            stock_levels=stock_levels,
            text_filter=text_filter,
            request_options=request_options,
        )
        return _response.data

    async def update_item_modifier_lists(
        self,
        *,
        item_ids: typing.Sequence[str],
        modifier_lists_to_disable: typing.Optional[typing.Sequence[str]] = OMIT,
        modifier_lists_to_enable: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateItemModifierListsResponse:
        """
        Updates the [CatalogModifierList](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogModifierList) objects
        that apply to the targeted [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) without having
        to perform an upsert on the entire item.

        Parameters
        ----------
        item_ids : typing.Sequence[str]
            The IDs of the catalog items associated with the CatalogModifierList objects being updated.

        modifier_lists_to_disable : typing.Optional[typing.Sequence[str]]
            The IDs of the CatalogModifierList objects to disable for the CatalogItem.

        modifier_lists_to_enable : typing.Optional[typing.Sequence[str]]
            The IDs of the CatalogModifierList objects to enable for the CatalogItem.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateItemModifierListsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog.update_item_modifier_lists(
                item_ids=["item_ids"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_item_modifier_lists(
            item_ids=item_ids,
            modifier_lists_to_disable=modifier_lists_to_disable,
            modifier_lists_to_enable=modifier_lists_to_enable,
            request_options=request_options,
        )
        return _response.data

    async def update_item_taxes(
        self,
        *,
        item_ids: typing.Sequence[str],
        taxes_to_disable: typing.Optional[typing.Sequence[str]] = OMIT,
        taxes_to_enable: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateItemTaxesResponse:
        """
        Updates the [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax) objects that apply to the
        targeted [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) without having to perform an
        upsert on the entire item.

        Parameters
        ----------
        item_ids : typing.Sequence[str]
            IDs for the CatalogItems associated with the CatalogTax objects being updated.

        taxes_to_disable : typing.Optional[typing.Sequence[str]]
            IDs of the CatalogTax objects to disable.

        taxes_to_enable : typing.Optional[typing.Sequence[str]]
            IDs of the CatalogTax objects to enable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateItemTaxesResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog.update_item_taxes(
                item_ids=["item_ids"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_item_taxes(
            item_ids=item_ids,
            taxes_to_disable=taxes_to_disable,
            taxes_to_enable=taxes_to_enable,
            request_options=request_options,
        )
        return _response.data
