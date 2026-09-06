

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.list_items_items_request_created_on import ListItemsItemsRequestCreatedOn
from ...types.list_items_items_request_last_published import ListItemsItemsRequestLastPublished
from ...types.list_items_items_request_last_updated import ListItemsItemsRequestLastUpdated
from ...types.list_items_live_items_request_created_on import ListItemsLiveItemsRequestCreatedOn
from ...types.list_items_live_items_request_last_published import ListItemsLiveItemsRequestLastPublished
from ...types.list_items_live_items_request_last_updated import ListItemsLiveItemsRequestLastUpdated
from .raw_client import AsyncRawItemsClient, RawItemsClient
from .types.create_item_items_request_body import CreateItemItemsRequestBody
from .types.create_item_items_response import CreateItemItemsResponse
from .types.create_item_live_items_request_body import CreateItemLiveItemsRequestBody
from .types.create_item_live_items_response import CreateItemLiveItemsResponse
from .types.create_items_items_request_field_data import CreateItemsItemsRequestFieldData
from .types.create_items_items_response import CreateItemsItemsResponse
from .types.delete_items_items_request_items_item import DeleteItemsItemsRequestItemsItem
from .types.delete_items_live_items_request_items_item import DeleteItemsLiveItemsRequestItemsItem
from .types.get_item_items_response import GetItemItemsResponse
from .types.get_item_live_items_response import GetItemLiveItemsResponse
from .types.list_items_items_request_filter_value import ListItemsItemsRequestFilterValue
from .types.list_items_items_request_sort_by import ListItemsItemsRequestSortBy
from .types.list_items_items_request_sort_order import ListItemsItemsRequestSortOrder
from .types.list_items_items_request_sort_value import ListItemsItemsRequestSortValue
from .types.list_items_items_response import ListItemsItemsResponse
from .types.list_items_live_items_request_filter_value import ListItemsLiveItemsRequestFilterValue
from .types.list_items_live_items_request_sort_by import ListItemsLiveItemsRequestSortBy
from .types.list_items_live_items_request_sort_order import ListItemsLiveItemsRequestSortOrder
from .types.list_items_live_items_request_sort_value import ListItemsLiveItemsRequestSortValue
from .types.list_items_live_items_response import ListItemsLiveItemsResponse
from .types.publish_item_items_request_body import PublishItemItemsRequestBody
from .types.publish_item_items_response import PublishItemItemsResponse
from .types.update_item_items_request_field_data import UpdateItemItemsRequestFieldData
from .types.update_item_items_response import UpdateItemItemsResponse
from .types.update_item_live_items_request_field_data import UpdateItemLiveItemsRequestFieldData
from .types.update_item_live_items_response import UpdateItemLiveItemsResponse
from .types.update_items_items_request_items_item import UpdateItemsItemsRequestItemsItem
from .types.update_items_items_response import UpdateItemsItemsResponse
from .types.update_items_live_items_request_items_item import UpdateItemsLiveItemsRequestItemsItem
from .types.update_items_live_items_response import UpdateItemsLiveItemsResponse


OMIT = typing.cast(typing.Any, ...)


class ItemsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawItemsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawItemsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawItemsClient
        """
        return self._raw_client

    def list_items(
        self,
        collection_id: str,
        *,
        cms_locale_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        created_on: typing.Optional[ListItemsItemsRequestCreatedOn] = None,
        last_published: typing.Optional[ListItemsItemsRequestLastPublished] = None,
        last_updated: typing.Optional[ListItemsItemsRequestLastUpdated] = None,
        filter: typing.Optional[typing.Dict[str, ListItemsItemsRequestFilterValue]] = None,
        sort_by: typing.Optional[ListItemsItemsRequestSortBy] = None,
        sort_order: typing.Optional[ListItemsItemsRequestSortOrder] = None,
        sort: typing.Optional[typing.Dict[str, ListItemsItemsRequestSortValue]] = None,
        translatable: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListItemsItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        List of all Items within a Collection.

        <Note>
          This endpoint supports:

          - Custom `filter[...]` queries support up to 10 filter terms and 2 text-search terms per request.
          - Custom `sort[...]` queries support up to 3 sort fields per request.
        </Note>

        Required scope | `CMS:read`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        cms_locale_id : typing.Optional[str]
            Unique identifier for a CMS Locale. This UID is different from the Site locale identifier and is listed as `cmsLocaleId` in the Sites response. To query multiple locales, input a comma separated string.

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        name : typing.Optional[str]
            Filter by the exact name of the item(s)

        slug : typing.Optional[str]
            Filter by the exact slug of the item

        created_on : typing.Optional[ListItemsItemsRequestCreatedOn]
            Filter by the creation date of the item(s)

        last_published : typing.Optional[ListItemsItemsRequestLastPublished]
            Filter by the last published date of the item(s)

        last_updated : typing.Optional[ListItemsItemsRequestLastUpdated]
            Filter by the last updated date of the item(s)

        filter : typing.Optional[typing.Dict[str, ListItemsItemsRequestFilterValue]]
            Filter collection items by custom field values. Use bracket notation:
            `filter[<fieldSlug>][<operator>]=<value>`.

            Example: `filter[price][gte]=10&filter[price][lte]=100&filter[name][contains]=shirt`.

            Filters are combined with AND. You can combine custom field filters with top-level filters such as `name`, `slug`, `createdOn`, `lastPublished`, and `lastUpdated`. OR logic and nested filter groups are not supported on GET requests.

            More filter terms can increase request latency.

            Supported operators by field type:

            | Field type | Supported operators |
            | --- | --- |
            | `id` | `eq`, `ne`, `in`, `nin` |
            | `PlainText` | `eq`, `ne`, `in`, `nin`, `contains`, `ncontains`, `exists` |
            | `Number` | `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`, `exists` |
            | `Switch` | `eq`, `ne`, `in`, `nin`, `exists` |
            | `DateTime` | `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`, `exists` |
            | `Email`, `Phone`, `Link` | `eq`, `ne`, `in`, `nin`, `contains`, `ncontains`, `exists` |
            | `Color` | `eq`, `ne`, `in`, `nin`, `exists` |
            | `Reference` | `eq`, `ne`, `in`, `nin`, `exists` |
            | `Option` | `eq`, `ne`, `in`, `nin` |
            | `RichText`, `Image`, `MultiImage`, `VideoLink`, `MultiReference` | `exists` |

            `contains` and `ncontains` are case-insensitive. `ncontains` also matches items where the field is empty or not set.

            `exists=true` matches items where the field has a value. `exists=false` matches items where the field is missing or null. For `Switch` fields, `false` is still a set value.

            Value formats:

            | Field type | Value format |
            | --- | --- |
            | `Number` | A valid number, such as `10` or `12.5` |
            | `Switch` | `true` or `false` |
            | `DateTime` | ISO 8601 date-time string |
            | `id`, `Reference` | 24-character item ID |
            | `Option` | Option ID |
            | `in`, `nin` | Comma-separated list, up to 100 values |

            Invalid fields, invalid values, and operators that do not apply to a field type return a `400 BadArgument` response.

        sort_by : typing.Optional[ListItemsItemsRequestSortBy]
            Sort results by the provided value

        sort_order : typing.Optional[ListItemsItemsRequestSortOrder]
            Sorts the results by asc or desc

        sort : typing.Optional[typing.Dict[str, ListItemsItemsRequestSortValue]]
            Sort collection items by custom fields using bracket notation: `sort[<fieldSlug>]=<asc|desc>`.

            - Example: `sort[price]=desc`
            - Multiple sort fields are applied in query-string order. When `sort[...]` is provided, it takes precedence over `sortBy` and `sortOrder`.
            - Sortable field types: `PlainText`, `Email`, `Phone`, `Number`, `DateTime`, and `Switch`.
            - Unknown fields, invalid sort directions, and non-sortable field types return a `400 BadArgument` response.

        translatable : typing.Optional[str]
            Unique identifier for the secondary Locale you're translating **into**. Returns only content that hasn't been excluded from translation for that locale.

            This is independent of `localeId`, which selects which version of the content is returned. To fetch the source text to translate, request the primary locale's content and set `translatable` to the locale you're translating into:

            `?localeId={primary locale id}&translatable={target locale id}`

            Only exclusion rules scoped to manual translation are respected — rules scoped only to automatic translation don't affect this parameter's response.

            Omitting `translatable` returns the same response as if this parameter didn't exist. The value must be the id of one of the site's secondary locales — the primary locale id, or any other value, returns a `400` error. Requires translation exclusions to be enabled for the site; if they aren't, the request returns a `403` error.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListItemsItemsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collections.items.list_items(
            collection_id="580e63fc8c9a982ac9b8b745",
            translatable="65427cf400e02b306eaa04a0",
        )
        """
        _response = self._raw_client.list_items(
            collection_id,
            cms_locale_id=cms_locale_id,
            offset=offset,
            limit=limit,
            name=name,
            slug=slug,
            created_on=created_on,
            last_published=last_published,
            last_updated=last_updated,
            filter=filter,
            sort_by=sort_by,
            sort_order=sort_order,
            sort=sort,
            translatable=translatable,
            request_options=request_options,
        )
        return _response.data

    def create_item(
        self,
        collection_id: str,
        *,
        request: CreateItemItemsRequestBody,
        skip_invalid_files: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateItemItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        Create Item(s) in a Collection.

        This endpoint accepts two request shapes, and a request must use one or the other:

        - **Single item** — send `fieldData` at the top level. Set `cmsLocaleId` to create the item in a specific locale.
        - **Multiple items** — send an `items` array with at least one entry. Each entry needs its own `fieldData`, and can set its own `cmsLocaleId`, `isDraft`, and `isArchived`. The API ignores any other property on an entry.

        ```json
        {
          "items": [
            {
              "isArchived": false,
              "isDraft": false,
              "fieldData": {
                "name": "Senior Data Analyst",
                "slug": "senior-data-analyst"
              }
            },
            {
              "isArchived": false,
              "isDraft": false,
              "fieldData": {
                "name": "Product Manager",
                "slug": "product-manager"
              }
            }
          ]
        }
        ```

        A request that carries both `fieldData` and `items` returns a `400`.

        To create items across multiple locales, please use [this endpoint.](/data/reference/cms/collection-items/staged-items/create-items)

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        request : CreateItemItemsRequestBody

        skip_invalid_files : typing.Optional[bool]
            When true, invalid files are skipped and processing continues. When false, the entire request fails if any file is invalid.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateItemItemsResponse
            Request was successful

        Examples
        --------
        from fern.collections.items import SingleItem, SingleItemFieldData

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collections.items.create_item(
            collection_id="580e63fc8c9a982ac9b8b745",
            request=SingleItem(
                is_archived=False,
                is_draft=False,
                field_data=SingleItemFieldData(
                    name="The Hitchhiker's Guide to the Galaxy",
                    slug="hitchhikers-guide-to-the-galaxy",
                ),
            ),
        )
        """
        _response = self._raw_client.create_item(
            collection_id, request=request, skip_invalid_files=skip_invalid_files, request_options=request_options
        )
        return _response.data

    def delete_items(
        self,
        collection_id: str,
        *,
        items: typing.Sequence[DeleteItemsItemsRequestItemsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete Items from a Collection.

        <Tip title="Localization Tip">Items will only be deleted in the primary locale unless a `cmsLocaleId` is included in the request.</Tip>

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        items : typing.Sequence[DeleteItemsItemsRequestItemsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.collections.items import DeleteItemsItemsRequestItemsItem

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collections.items.delete_items(
            collection_id="580e63fc8c9a982ac9b8b745",
            items=[
                DeleteItemsItemsRequestItemsItem(
                    id="580e64008c9a982ac9b8b754",
                )
            ],
        )
        """
        _response = self._raw_client.delete_items(collection_id, items=items, request_options=request_options)
        return _response.data

    def update_items(
        self,
        collection_id: str,
        *,
        skip_invalid_files: typing.Optional[bool] = None,
        items: typing.Optional[typing.Sequence[UpdateItemsItemsRequestItemsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateItemsItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        Update a single item or multiple items in a Collection.

        The limit for this endpoint is 100 items.

        <Tip title="Localization Tip">Items will only be updated in the primary locale, unless a `cmsLocaleId` is included in the request.</Tip>

        <Note title="Draft status behavior">
          `isDraft: true` doesn't unpublish an item. The resulting status depends on whether the item has been published before:

          - **Item that has never been published:** the item gets a `Draft` status.
          - **Already-published item:** the item gets a `Changes in draft` status. The live item stays published, and your changes are held back until you publish them.

          Setting `isDraft: false` queues the item to publish on the next site publish. To remove an item from the live site, use [Unpublish Live Collection Items](/data/reference/cms/collection-items/live-items/delete-items-live). For the full status mapping, see [Publishing with the CMS API](/data/docs/working-with-the-cms/publishing).
        </Note>

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        skip_invalid_files : typing.Optional[bool]
            When true, invalid files are skipped and processing continues. When false, the entire request fails if any file is invalid.

        items : typing.Optional[typing.Sequence[UpdateItemsItemsRequestItemsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateItemsItemsResponse
            Request was successful

        Examples
        --------
        from fern.collections.items import (
            UpdateItemsItemsRequestItemsItem,
            UpdateItemsItemsRequestItemsItemFieldData,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collections.items.update_items(
            collection_id="580e63fc8c9a982ac9b8b745",
            items=[
                UpdateItemsItemsRequestItemsItem(
                    id="66f6ed9576ddacf3149d5ea6",
                    cms_locale_id="66f6e966c9e1dc700a857ca5",
                    field_data=UpdateItemsItemsRequestItemsItemFieldData(
                        name="Ne Paniquez Pas",
                        slug="ne-paniquez-pas",
                    ),
                ),
                UpdateItemsItemsRequestItemsItem(
                    id="66f6ed9576ddacf3149d5ea6",
                    cms_locale_id="66f6e966c9e1dc700a857ca4",
                    field_data=UpdateItemsItemsRequestItemsItemFieldData(
                        name="No Entrar en Pánico",
                        slug="no-entrar-en-panico",
                    ),
                ),
                UpdateItemsItemsRequestItemsItem(
                    id="66f6ed9576ddacf3149d5eaa",
                    cms_locale_id="66f6e966c9e1dc700a857ca5",
                    field_data=UpdateItemsItemsRequestItemsItemFieldData(
                        name="Au Revoir et Merci pour Tous les Poissons",
                        slug="au-revoir-et-merci",
                    ),
                ),
                UpdateItemsItemsRequestItemsItem(
                    id="66f6ed9576ddacf3149d5eaa",
                    cms_locale_id="66f6e966c9e1dc700a857ca4",
                    field_data=UpdateItemsItemsRequestItemsItemFieldData(
                        name="Hasta Luego y Gracias por Todo el Pescado",
                        slug="hasta-luego-y-gracias",
                    ),
                ),
            ],
        )
        """
        _response = self._raw_client.update_items(
            collection_id, skip_invalid_files=skip_invalid_files, items=items, request_options=request_options
        )
        return _response.data

    def list_items_live(
        self,
        collection_id: str,
        *,
        cms_locale_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        created_on: typing.Optional[ListItemsLiveItemsRequestCreatedOn] = None,
        last_published: typing.Optional[ListItemsLiveItemsRequestLastPublished] = None,
        last_updated: typing.Optional[ListItemsLiveItemsRequestLastUpdated] = None,
        filter: typing.Optional[typing.Dict[str, ListItemsLiveItemsRequestFilterValue]] = None,
        sort_by: typing.Optional[ListItemsLiveItemsRequestSortBy] = None,
        sort_order: typing.Optional[ListItemsLiveItemsRequestSortOrder] = None,
        sort: typing.Optional[typing.Dict[str, ListItemsLiveItemsRequestSortValue]] = None,
        translatable: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListItemsLiveItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        List all published items in a collection.

        <Tip title="Serve data with the Content Delivery API">
          Serving data to applications in real-time? Use the Content Delivery API at `api-cdn.webflow.com` for better performance. The CDN-backed endpoint is optimized for high-volume reads, while the Data API is designed for writes and management operations.
        </Tip>

        <Note>
          This endpoint supports:

          - Custom `filter[...]` queries support up to 10 filter terms and 2 text-search terms per request.
          - Custom `sort[...]` queries support up to 3 sort fields per request.
        </Note>

        Required scope | `CMS:read`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        cms_locale_id : typing.Optional[str]
            Unique identifier for a CMS Locale. This UID is different from the Site locale identifier and is listed as `cmsLocaleId` in the Sites response. To query multiple locales, input a comma separated string.

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        name : typing.Optional[str]
            Filter by the exact name of the item(s)

        slug : typing.Optional[str]
            Filter by the exact slug of the item

        created_on : typing.Optional[ListItemsLiveItemsRequestCreatedOn]
            Filter by the creation date of the item(s)

        last_published : typing.Optional[ListItemsLiveItemsRequestLastPublished]
            Filter by the last published date of the item(s)

        last_updated : typing.Optional[ListItemsLiveItemsRequestLastUpdated]
            Filter by the last updated date of the item(s)

        filter : typing.Optional[typing.Dict[str, ListItemsLiveItemsRequestFilterValue]]
            Filter collection items by custom field values. Use bracket notation:
            `filter[<fieldSlug>][<operator>]=<value>`.

            Example: `filter[price][gte]=10&filter[price][lte]=100&filter[name][contains]=shirt`.

            Filters are combined with AND. You can combine custom field filters with top-level filters such as `name`, `slug`, `createdOn`, `lastPublished`, and `lastUpdated`. OR logic and nested filter groups are not supported on GET requests.

            More filter terms can increase request latency.

            Supported operators by field type:

            | Field type | Supported operators |
            | --- | --- |
            | `id` | `eq`, `ne`, `in`, `nin` |
            | `PlainText` | `eq`, `ne`, `in`, `nin`, `contains`, `ncontains`, `exists` |
            | `Number` | `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`, `exists` |
            | `Switch` | `eq`, `ne`, `in`, `nin`, `exists` |
            | `DateTime` | `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`, `exists` |
            | `Email`, `Phone`, `Link` | `eq`, `ne`, `in`, `nin`, `contains`, `ncontains`, `exists` |
            | `Color` | `eq`, `ne`, `in`, `nin`, `exists` |
            | `Reference` | `eq`, `ne`, `in`, `nin`, `exists` |
            | `Option` | `eq`, `ne`, `in`, `nin` |
            | `RichText`, `Image`, `MultiImage`, `VideoLink`, `MultiReference` | `exists` |

            `contains` and `ncontains` are case-insensitive. `ncontains` also matches items where the field is empty or not set.

            `exists=true` matches items where the field has a value. `exists=false` matches items where the field is missing or null. For `Switch` fields, `false` is still a set value.

            Value formats:

            | Field type | Value format |
            | --- | --- |
            | `Number` | A valid number, such as `10` or `12.5` |
            | `Switch` | `true` or `false` |
            | `DateTime` | ISO 8601 date-time string |
            | `id`, `Reference` | 24-character item ID |
            | `Option` | Option ID |
            | `in`, `nin` | Comma-separated list, up to 100 values |

            Invalid fields, invalid values, and operators that do not apply to a field type return a `400 BadArgument` response.

        sort_by : typing.Optional[ListItemsLiveItemsRequestSortBy]
            Sort results by the provided value

        sort_order : typing.Optional[ListItemsLiveItemsRequestSortOrder]
            Sorts the results by asc or desc

        sort : typing.Optional[typing.Dict[str, ListItemsLiveItemsRequestSortValue]]
            Sort collection items by custom fields using bracket notation: `sort[<fieldSlug>]=<asc|desc>`.

            - Example: `sort[price]=desc`
            - Multiple sort fields are applied in query-string order. When `sort[...]` is provided, it takes precedence over `sortBy` and `sortOrder`.
            - Sortable field types: `PlainText`, `Email`, `Phone`, `Number`, `DateTime`, and `Switch`.
            - Unknown fields, invalid sort directions, and non-sortable field types return a `400 BadArgument` response.

        translatable : typing.Optional[str]
            Unique identifier for the secondary Locale you're translating **into**. Returns only content that hasn't been excluded from translation for that locale.

            This is independent of `localeId`, which selects which version of the content is returned. To fetch the source text to translate, request the primary locale's content and set `translatable` to the locale you're translating into:

            `?localeId={primary locale id}&translatable={target locale id}`

            Only exclusion rules scoped to manual translation are respected — rules scoped only to automatic translation don't affect this parameter's response.

            Omitting `translatable` returns the same response as if this parameter didn't exist. The value must be the id of one of the site's secondary locales — the primary locale id, or any other value, returns a `400` error. Requires translation exclusions to be enabled for the site; if they aren't, the request returns a `403` error.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListItemsLiveItemsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collections.items.list_items_live(
            collection_id="580e63fc8c9a982ac9b8b745",
            translatable="65427cf400e02b306eaa04a0",
        )
        """
        _response = self._raw_client.list_items_live(
            collection_id,
            cms_locale_id=cms_locale_id,
            offset=offset,
            limit=limit,
            name=name,
            slug=slug,
            created_on=created_on,
            last_published=last_published,
            last_updated=last_updated,
            filter=filter,
            sort_by=sort_by,
            sort_order=sort_order,
            sort=sort,
            translatable=translatable,
            request_options=request_options,
        )
        return _response.data

    def create_item_live(
        self,
        collection_id: str,
        *,
        request: CreateItemLiveItemsRequestBody,
        skip_invalid_files: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateItemLiveItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        Create item(s) in a collection that will be immediately published to the live site.

        This endpoint accepts two request shapes, and a request must use one or the other:

        - **Single item** — send `fieldData` at the top level. Set `cmsLocaleId` to create the item in a specific locale.
        - **Multiple items** — send an `items` array with at least one entry. Each entry needs its own `fieldData`, and can set its own `cmsLocaleId`, `isDraft`, and `isArchived`. The API ignores any other property on an entry.

        ```json
        {
          "items": [
            {
              "isArchived": false,
              "isDraft": false,
              "fieldData": {
                "name": "Senior Data Analyst",
                "slug": "senior-data-analyst"
              }
            },
            {
              "isArchived": false,
              "isDraft": false,
              "fieldData": {
                "name": "Product Manager",
                "slug": "product-manager"
              }
            }
          ]
        }
        ```

        A request that carries both `fieldData` and `items` returns a `400`.

        To create items across multiple locales, [please use this endpoint.](/data/reference/cms/collection-items/staged-items/create-items)

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        request : CreateItemLiveItemsRequestBody

        skip_invalid_files : typing.Optional[bool]
            When true, invalid files are skipped and processing continues. When false, the entire request fails if any file is invalid.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateItemLiveItemsResponse
            Request was successful

        Examples
        --------
        from fern.collections.items import SingleLiveItem, SingleLiveItemFieldData

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collections.items.create_item_live(
            collection_id="580e63fc8c9a982ac9b8b745",
            request=SingleLiveItem(
                is_archived=False,
                is_draft=False,
                field_data=SingleLiveItemFieldData(
                    name="The Hitchhiker's Guide to the Galaxy",
                    slug="hitchhikers-guide-to-the-galaxy",
                ),
            ),
        )
        """
        _response = self._raw_client.create_item_live(
            collection_id, request=request, skip_invalid_files=skip_invalid_files, request_options=request_options
        )
        return _response.data

    def delete_items_live(
        self,
        collection_id: str,
        *,
        items: typing.Sequence[DeleteItemsLiveItemsRequestItemsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Unpublish up to 100 items from the live site and set the `isDraft` property to `true`.

        <Tip title="Localization Tip">Items will only be unpublished in the primary locale unless a `cmsLocaleId` is included in the request.</Tip>

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        items : typing.Sequence[DeleteItemsLiveItemsRequestItemsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.collections.items import DeleteItemsLiveItemsRequestItemsItem

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collections.items.delete_items_live(
            collection_id="580e63fc8c9a982ac9b8b745",
            items=[
                DeleteItemsLiveItemsRequestItemsItem(
                    id="580e64008c9a982ac9b8b754",
                )
            ],
        )
        """
        _response = self._raw_client.delete_items_live(collection_id, items=items, request_options=request_options)
        return _response.data

    def update_items_live(
        self,
        collection_id: str,
        *,
        skip_invalid_files: typing.Optional[bool] = None,
        items: typing.Optional[typing.Sequence[UpdateItemsLiveItemsRequestItemsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateItemsLiveItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        Update a single published item or multiple published items (up to 100) in a Collection

        <Tip title="Localization Tip">Items will only be updated in the primary locale, unless a `cmsLocaleId` is included in the request.</Tip>

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        skip_invalid_files : typing.Optional[bool]
            When true, invalid files are skipped and processing continues. When false, the entire request fails if any file is invalid.

        items : typing.Optional[typing.Sequence[UpdateItemsLiveItemsRequestItemsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateItemsLiveItemsResponse
            Request was successful

        Examples
        --------
        from fern.collections.items import (
            UpdateItemsLiveItemsRequestItemsItem,
            UpdateItemsLiveItemsRequestItemsItemFieldData,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collections.items.update_items_live(
            collection_id="580e63fc8c9a982ac9b8b745",
            items=[
                UpdateItemsLiveItemsRequestItemsItem(
                    id="66f6ed9576ddacf3149d5ea6",
                    cms_locale_id="66f6e966c9e1dc700a857ca5",
                    field_data=UpdateItemsLiveItemsRequestItemsItemFieldData(
                        name="Ne Paniquez Pas",
                        slug="ne-paniquez-pas",
                    ),
                ),
                UpdateItemsLiveItemsRequestItemsItem(
                    id="66f6ed9576ddacf3149d5ea6",
                    cms_locale_id="66f6e966c9e1dc700a857ca4",
                    field_data=UpdateItemsLiveItemsRequestItemsItemFieldData(
                        name="No Entrar en Pánico",
                        slug="no-entrar-en-panico",
                    ),
                ),
                UpdateItemsLiveItemsRequestItemsItem(
                    id="66f6ed9576ddacf3149d5eaa",
                    cms_locale_id="66f6e966c9e1dc700a857ca5",
                    field_data=UpdateItemsLiveItemsRequestItemsItemFieldData(
                        name="Au Revoir et Merci pour Tous les Poissons",
                        slug="au-revoir-et-merci",
                    ),
                ),
                UpdateItemsLiveItemsRequestItemsItem(
                    id="66f6ed9576ddacf3149d5eaa",
                    cms_locale_id="66f6e966c9e1dc700a857ca4",
                    field_data=UpdateItemsLiveItemsRequestItemsItemFieldData(
                        name="Hasta Luego y Gracias por Todo el Pescado",
                        slug="hasta-luego-y-gracias",
                    ),
                ),
            ],
        )
        """
        _response = self._raw_client.update_items_live(
            collection_id, skip_invalid_files=skip_invalid_files, items=items, request_options=request_options
        )
        return _response.data

    def create_items(
        self,
        collection_id: str,
        *,
        field_data: CreateItemsItemsRequestFieldData,
        skip_invalid_files: typing.Optional[bool] = None,
        cms_locale_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        is_archived: typing.Optional[bool] = OMIT,
        is_draft: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateItemsItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        Create an item or multiple items in a CMS Collection across multiple corresponding locales.

        <Note>
          - This endpoint can create up to 100 items in a request.
          - If the `cmsLocaleIds` parameter is not included in the request, an item will only be created in the primary locale.
        </Note>

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        field_data : CreateItemsItemsRequestFieldData

        skip_invalid_files : typing.Optional[bool]
            When true, invalid files are skipped and processing continues. When false, the entire request fails if any file is invalid.

        cms_locale_ids : typing.Optional[typing.Sequence[str]]
            Array of identifiers for the locales where the item will be created

        is_archived : typing.Optional[bool]
            Indicates whether the item is archived.

        is_draft : typing.Optional[bool]
            Indicates whether the item is in draft state.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateItemsItemsResponse
            Request was successful

        Examples
        --------
        from fern.collections.items import SingleCmsItem

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collections.items.create_items(
            collection_id="580e63fc8c9a982ac9b8b745",
            cms_locale_ids=[
                "66f6e966c9e1dc700a857ca3",
                "66f6e966c9e1dc700a857ca4",
                "66f6e966c9e1dc700a857ca5",
            ],
            is_archived=False,
            is_draft=False,
            field_data=SingleCmsItem(
                name="Don’t Panic",
                slug="dont-panic",
            ),
        )
        """
        _response = self._raw_client.create_items(
            collection_id,
            field_data=field_data,
            skip_invalid_files=skip_invalid_files,
            cms_locale_ids=cms_locale_ids,
            is_archived=is_archived,
            is_draft=is_draft,
            request_options=request_options,
        )
        return _response.data

    def get_item(
        self,
        collection_id: str,
        item_id: str,
        *,
        cms_locale_id: typing.Optional[str] = None,
        translatable: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetItemItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        Get details of a selected Collection Item.

        Required scope | `CMS:read`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        item_id : str
            Unique identifier for an Item

        cms_locale_id : typing.Optional[str]
            Unique identifier for a CMS Locale. This UID is different from the Site locale identifier and is listed as `cmsLocaleId` in the Sites response. This endpoint returns a single item, so it accepts one locale. To retrieve an item in several locales, use [List Collection Items](/data/reference/cms/collection-items/staged-items/list-items) with `filter[id][eq]` and a comma separated `cmsLocaleId`.

        translatable : typing.Optional[str]
            Unique identifier for the secondary Locale you're translating **into**. Returns only content that hasn't been excluded from translation for that locale.

            This is independent of `localeId`, which selects which version of the content is returned. To fetch the source text to translate, request the primary locale's content and set `translatable` to the locale you're translating into:

            `?localeId={primary locale id}&translatable={target locale id}`

            Only exclusion rules scoped to manual translation are respected — rules scoped only to automatic translation don't affect this parameter's response.

            Omitting `translatable` returns the same response as if this parameter didn't exist. The value must be the id of one of the site's secondary locales — the primary locale id, or any other value, returns a `400` error. Requires translation exclusions to be enabled for the site; if they aren't, the request returns a `403` error.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetItemItemsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collections.items.get_item(
            collection_id="580e63fc8c9a982ac9b8b745",
            item_id="580e64008c9a982ac9b8b754",
            translatable="65427cf400e02b306eaa04a0",
        )
        """
        _response = self._raw_client.get_item(
            collection_id,
            item_id,
            cms_locale_id=cms_locale_id,
            translatable=translatable,
            request_options=request_options,
        )
        return _response.data

    def delete_item(
        self,
        collection_id: str,
        item_id: str,
        *,
        cms_locale_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete an item from a collection.

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        item_id : str
            Unique identifier for an Item

        cms_locale_id : typing.Optional[str]
            Unique identifier for a CMS Locale. This UID is different from the Site locale identifier and is listed as `cmsLocaleId` in the Sites response. To query multiple locales, input a comma separated string.

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
        client.collections.items.delete_item(
            collection_id="580e63fc8c9a982ac9b8b745",
            item_id="580e64008c9a982ac9b8b754",
        )
        """
        _response = self._raw_client.delete_item(
            collection_id, item_id, cms_locale_id=cms_locale_id, request_options=request_options
        )
        return _response.data

    def update_item(
        self,
        collection_id: str,
        item_id: str,
        *,
        skip_invalid_files: typing.Optional[bool] = None,
        cms_locale_id: typing.Optional[str] = OMIT,
        is_archived: typing.Optional[bool] = OMIT,
        is_draft: typing.Optional[bool] = OMIT,
        field_data: typing.Optional[UpdateItemItemsRequestFieldData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateItemItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        Update a selected Item in a Collection.

        <Note title="Draft status behavior">
          `isDraft: true` doesn't unpublish an item. The resulting status depends on whether the item has been published before:

          - **Item that has never been published:** the item gets a `Draft` status.
          - **Already-published item:** the item gets a `Changes in draft` status. The live item stays published, and your changes are held back until you publish them.

          Setting `isDraft: false` queues the item to publish on the next site publish. To remove an item from the live site, use [Unpublish Live Collection Items](/data/reference/cms/collection-items/live-items/delete-items-live). For the full status mapping, see [Publishing with the CMS API](/data/docs/working-with-the-cms/publishing).
        </Note>

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        item_id : str
            Unique identifier for an Item

        skip_invalid_files : typing.Optional[bool]
            When true, invalid files are skipped and processing continues. When false, the entire request fails if any file is invalid.

        cms_locale_id : typing.Optional[str]
            Identifier for the locale of the CMS item

        is_archived : typing.Optional[bool]
            Boolean determining if the Item is set to archived

        is_draft : typing.Optional[bool]
            Sets the item's draft state. The resulting status depends on whether the item has been published before:

            - **Item that has never been published:** `isDraft: true` results in a `Draft` status.
            - **Already-published item:** `isDraft: true` results in a `Changes in draft` status. The live item stays published, and your changes are held back until you publish them.

            Setting `isDraft: true` never unpublishes an item. To remove an item from the live site, use [Unpublish Live Collection Items](/data/reference/cms/collection-items/live-items/delete-items-live).

        field_data : typing.Optional[UpdateItemItemsRequestFieldData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateItemItemsResponse
            Request was successful

        Examples
        --------
        from fern.collections.items import UpdateItemItemsRequestFieldData

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collections.items.update_item(
            collection_id="580e63fc8c9a982ac9b8b745",
            item_id="580e64008c9a982ac9b8b754",
            is_archived=False,
            is_draft=False,
            field_data=UpdateItemItemsRequestFieldData(
                name="The Hitchhiker's Guide to the Galaxy",
                slug="hitchhikers-guide-to-the-galaxy",
            ),
        )
        """
        _response = self._raw_client.update_item(
            collection_id,
            item_id,
            skip_invalid_files=skip_invalid_files,
            cms_locale_id=cms_locale_id,
            is_archived=is_archived,
            is_draft=is_draft,
            field_data=field_data,
            request_options=request_options,
        )
        return _response.data

    def get_item_live(
        self,
        collection_id: str,
        item_id: str,
        *,
        cms_locale_id: typing.Optional[str] = None,
        translatable: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetItemLiveItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        Get details of a selected Collection live Item.

        <Tip title="Serve data with the Content Delivery API">
          Serving data to applications in real-time? Use the Content Delivery API at `api-cdn.webflow.com` for better performance. The CDN-backed endpoint is optimized for high-volume reads, while the Data API is designed for writes and management operations.
        </Tip>

        Required scope | `CMS:read`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        item_id : str
            Unique identifier for an Item

        cms_locale_id : typing.Optional[str]
            Unique identifier for a CMS Locale. This UID is different from the Site locale identifier and is listed as `cmsLocaleId` in the Sites response. This endpoint returns a single item, so it accepts one locale. To retrieve an item in several locales, use [List Collection Items](/data/reference/cms/collection-items/staged-items/list-items) with `filter[id][eq]` and a comma separated `cmsLocaleId`.

        translatable : typing.Optional[str]
            Unique identifier for the secondary Locale you're translating **into**. Returns only content that hasn't been excluded from translation for that locale.

            This is independent of `localeId`, which selects which version of the content is returned. To fetch the source text to translate, request the primary locale's content and set `translatable` to the locale you're translating into:

            `?localeId={primary locale id}&translatable={target locale id}`

            Only exclusion rules scoped to manual translation are respected — rules scoped only to automatic translation don't affect this parameter's response.

            Omitting `translatable` returns the same response as if this parameter didn't exist. The value must be the id of one of the site's secondary locales — the primary locale id, or any other value, returns a `400` error. Requires translation exclusions to be enabled for the site; if they aren't, the request returns a `403` error.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetItemLiveItemsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collections.items.get_item_live(
            collection_id="580e63fc8c9a982ac9b8b745",
            item_id="580e64008c9a982ac9b8b754",
            translatable="65427cf400e02b306eaa04a0",
        )
        """
        _response = self._raw_client.get_item_live(
            collection_id,
            item_id,
            cms_locale_id=cms_locale_id,
            translatable=translatable,
            request_options=request_options,
        )
        return _response.data

    def delete_item_live(
        self,
        collection_id: str,
        item_id: str,
        *,
        cms_locale_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Unpublish a live item from the site and set the `isDraft` property to `true`.

        For bulk unpublishing, please use [this endpoint.](/data/v2.0.0/reference/cms/collection-items/live-items/delete-items-live)

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        item_id : str
            Unique identifier for an Item

        cms_locale_id : typing.Optional[str]
            Unique identifier for a CMS Locale. This UID is different from the Site locale identifier and is listed as `cmsLocaleId` in the Sites response. To query multiple locales, input a comma separated string.

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
        client.collections.items.delete_item_live(
            collection_id="580e63fc8c9a982ac9b8b745",
            item_id="580e64008c9a982ac9b8b754",
        )
        """
        _response = self._raw_client.delete_item_live(
            collection_id, item_id, cms_locale_id=cms_locale_id, request_options=request_options
        )
        return _response.data

    def update_item_live(
        self,
        collection_id: str,
        item_id: str,
        *,
        skip_invalid_files: typing.Optional[bool] = None,
        cms_locale_id: typing.Optional[str] = OMIT,
        is_archived: typing.Optional[bool] = OMIT,
        is_draft: typing.Optional[bool] = OMIT,
        field_data: typing.Optional[UpdateItemLiveItemsRequestFieldData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateItemLiveItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        Update a selected live Item in a Collection. The updates for this Item will be published to the live site.

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        item_id : str
            Unique identifier for an Item

        skip_invalid_files : typing.Optional[bool]
            When true, invalid files are skipped and processing continues. When false, the entire request fails if any file is invalid.

        cms_locale_id : typing.Optional[str]
            Identifier for the locale of the CMS item

        is_archived : typing.Optional[bool]
            Boolean determining if the Item is set to archived

        is_draft : typing.Optional[bool]
            Sets the item's draft state. The resulting status depends on whether the item has been published before:

            - **Item that has never been published:** `isDraft: true` results in a `Draft` status.
            - **Already-published item:** `isDraft: true` results in a `Changes in draft` status. The live item stays published, and your changes are held back until you publish them.

            Setting `isDraft: true` never unpublishes an item. To remove an item from the live site, use [Unpublish Live Collection Items](/data/reference/cms/collection-items/live-items/delete-items-live).

        field_data : typing.Optional[UpdateItemLiveItemsRequestFieldData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateItemLiveItemsResponse
            Request was successful

        Examples
        --------
        from fern.collections.items import UpdateItemLiveItemsRequestFieldData

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collections.items.update_item_live(
            collection_id="580e63fc8c9a982ac9b8b745",
            item_id="580e64008c9a982ac9b8b754",
            is_archived=False,
            is_draft=False,
            field_data=UpdateItemLiveItemsRequestFieldData(
                name="The Hitchhiker's Guide to the Galaxy",
                slug="hitchhikers-guide-to-the-galaxy",
            ),
        )
        """
        _response = self._raw_client.update_item_live(
            collection_id,
            item_id,
            skip_invalid_files=skip_invalid_files,
            cms_locale_id=cms_locale_id,
            is_archived=is_archived,
            is_draft=is_draft,
            field_data=field_data,
            request_options=request_options,
        )
        return _response.data

    def publish_item(
        self,
        collection_id: str,
        *,
        request: PublishItemItemsRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PublishItemItemsResponse:
        """
        Publish an item or multiple items.

        Required scope | `cms:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        request : PublishItemItemsRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublishItemItemsResponse
            Request was successful

        Examples
        --------
        from fern.collections.items import ItemIDs

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.collections.items.publish_item(
            collection_id="580e63fc8c9a982ac9b8b745",
            request=ItemIDs(
                item_ids=[
                    "643fd856d66b6528195ee2ca",
                    "643fd856d66b6528195ee2cb",
                    "643fd856d66b6528195ee2cc",
                ],
            ),
        )
        """
        _response = self._raw_client.publish_item(collection_id, request=request, request_options=request_options)
        return _response.data


class AsyncItemsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawItemsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawItemsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawItemsClient
        """
        return self._raw_client

    async def list_items(
        self,
        collection_id: str,
        *,
        cms_locale_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        created_on: typing.Optional[ListItemsItemsRequestCreatedOn] = None,
        last_published: typing.Optional[ListItemsItemsRequestLastPublished] = None,
        last_updated: typing.Optional[ListItemsItemsRequestLastUpdated] = None,
        filter: typing.Optional[typing.Dict[str, ListItemsItemsRequestFilterValue]] = None,
        sort_by: typing.Optional[ListItemsItemsRequestSortBy] = None,
        sort_order: typing.Optional[ListItemsItemsRequestSortOrder] = None,
        sort: typing.Optional[typing.Dict[str, ListItemsItemsRequestSortValue]] = None,
        translatable: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListItemsItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        List of all Items within a Collection.

        <Note>
          This endpoint supports:

          - Custom `filter[...]` queries support up to 10 filter terms and 2 text-search terms per request.
          - Custom `sort[...]` queries support up to 3 sort fields per request.
        </Note>

        Required scope | `CMS:read`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        cms_locale_id : typing.Optional[str]
            Unique identifier for a CMS Locale. This UID is different from the Site locale identifier and is listed as `cmsLocaleId` in the Sites response. To query multiple locales, input a comma separated string.

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        name : typing.Optional[str]
            Filter by the exact name of the item(s)

        slug : typing.Optional[str]
            Filter by the exact slug of the item

        created_on : typing.Optional[ListItemsItemsRequestCreatedOn]
            Filter by the creation date of the item(s)

        last_published : typing.Optional[ListItemsItemsRequestLastPublished]
            Filter by the last published date of the item(s)

        last_updated : typing.Optional[ListItemsItemsRequestLastUpdated]
            Filter by the last updated date of the item(s)

        filter : typing.Optional[typing.Dict[str, ListItemsItemsRequestFilterValue]]
            Filter collection items by custom field values. Use bracket notation:
            `filter[<fieldSlug>][<operator>]=<value>`.

            Example: `filter[price][gte]=10&filter[price][lte]=100&filter[name][contains]=shirt`.

            Filters are combined with AND. You can combine custom field filters with top-level filters such as `name`, `slug`, `createdOn`, `lastPublished`, and `lastUpdated`. OR logic and nested filter groups are not supported on GET requests.

            More filter terms can increase request latency.

            Supported operators by field type:

            | Field type | Supported operators |
            | --- | --- |
            | `id` | `eq`, `ne`, `in`, `nin` |
            | `PlainText` | `eq`, `ne`, `in`, `nin`, `contains`, `ncontains`, `exists` |
            | `Number` | `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`, `exists` |
            | `Switch` | `eq`, `ne`, `in`, `nin`, `exists` |
            | `DateTime` | `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`, `exists` |
            | `Email`, `Phone`, `Link` | `eq`, `ne`, `in`, `nin`, `contains`, `ncontains`, `exists` |
            | `Color` | `eq`, `ne`, `in`, `nin`, `exists` |
            | `Reference` | `eq`, `ne`, `in`, `nin`, `exists` |
            | `Option` | `eq`, `ne`, `in`, `nin` |
            | `RichText`, `Image`, `MultiImage`, `VideoLink`, `MultiReference` | `exists` |

            `contains` and `ncontains` are case-insensitive. `ncontains` also matches items where the field is empty or not set.

            `exists=true` matches items where the field has a value. `exists=false` matches items where the field is missing or null. For `Switch` fields, `false` is still a set value.

            Value formats:

            | Field type | Value format |
            | --- | --- |
            | `Number` | A valid number, such as `10` or `12.5` |
            | `Switch` | `true` or `false` |
            | `DateTime` | ISO 8601 date-time string |
            | `id`, `Reference` | 24-character item ID |
            | `Option` | Option ID |
            | `in`, `nin` | Comma-separated list, up to 100 values |

            Invalid fields, invalid values, and operators that do not apply to a field type return a `400 BadArgument` response.

        sort_by : typing.Optional[ListItemsItemsRequestSortBy]
            Sort results by the provided value

        sort_order : typing.Optional[ListItemsItemsRequestSortOrder]
            Sorts the results by asc or desc

        sort : typing.Optional[typing.Dict[str, ListItemsItemsRequestSortValue]]
            Sort collection items by custom fields using bracket notation: `sort[<fieldSlug>]=<asc|desc>`.

            - Example: `sort[price]=desc`
            - Multiple sort fields are applied in query-string order. When `sort[...]` is provided, it takes precedence over `sortBy` and `sortOrder`.
            - Sortable field types: `PlainText`, `Email`, `Phone`, `Number`, `DateTime`, and `Switch`.
            - Unknown fields, invalid sort directions, and non-sortable field types return a `400 BadArgument` response.

        translatable : typing.Optional[str]
            Unique identifier for the secondary Locale you're translating **into**. Returns only content that hasn't been excluded from translation for that locale.

            This is independent of `localeId`, which selects which version of the content is returned. To fetch the source text to translate, request the primary locale's content and set `translatable` to the locale you're translating into:

            `?localeId={primary locale id}&translatable={target locale id}`

            Only exclusion rules scoped to manual translation are respected — rules scoped only to automatic translation don't affect this parameter's response.

            Omitting `translatable` returns the same response as if this parameter didn't exist. The value must be the id of one of the site's secondary locales — the primary locale id, or any other value, returns a `400` error. Requires translation exclusions to be enabled for the site; if they aren't, the request returns a `403` error.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListItemsItemsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collections.items.list_items(
                collection_id="580e63fc8c9a982ac9b8b745",
                translatable="65427cf400e02b306eaa04a0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_items(
            collection_id,
            cms_locale_id=cms_locale_id,
            offset=offset,
            limit=limit,
            name=name,
            slug=slug,
            created_on=created_on,
            last_published=last_published,
            last_updated=last_updated,
            filter=filter,
            sort_by=sort_by,
            sort_order=sort_order,
            sort=sort,
            translatable=translatable,
            request_options=request_options,
        )
        return _response.data

    async def create_item(
        self,
        collection_id: str,
        *,
        request: CreateItemItemsRequestBody,
        skip_invalid_files: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateItemItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        Create Item(s) in a Collection.

        This endpoint accepts two request shapes, and a request must use one or the other:

        - **Single item** — send `fieldData` at the top level. Set `cmsLocaleId` to create the item in a specific locale.
        - **Multiple items** — send an `items` array with at least one entry. Each entry needs its own `fieldData`, and can set its own `cmsLocaleId`, `isDraft`, and `isArchived`. The API ignores any other property on an entry.

        ```json
        {
          "items": [
            {
              "isArchived": false,
              "isDraft": false,
              "fieldData": {
                "name": "Senior Data Analyst",
                "slug": "senior-data-analyst"
              }
            },
            {
              "isArchived": false,
              "isDraft": false,
              "fieldData": {
                "name": "Product Manager",
                "slug": "product-manager"
              }
            }
          ]
        }
        ```

        A request that carries both `fieldData` and `items` returns a `400`.

        To create items across multiple locales, please use [this endpoint.](/data/reference/cms/collection-items/staged-items/create-items)

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        request : CreateItemItemsRequestBody

        skip_invalid_files : typing.Optional[bool]
            When true, invalid files are skipped and processing continues. When false, the entire request fails if any file is invalid.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateItemItemsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.collections.items import SingleItem, SingleItemFieldData

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collections.items.create_item(
                collection_id="580e63fc8c9a982ac9b8b745",
                request=SingleItem(
                    is_archived=False,
                    is_draft=False,
                    field_data=SingleItemFieldData(
                        name="The Hitchhiker's Guide to the Galaxy",
                        slug="hitchhikers-guide-to-the-galaxy",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_item(
            collection_id, request=request, skip_invalid_files=skip_invalid_files, request_options=request_options
        )
        return _response.data

    async def delete_items(
        self,
        collection_id: str,
        *,
        items: typing.Sequence[DeleteItemsItemsRequestItemsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete Items from a Collection.

        <Tip title="Localization Tip">Items will only be deleted in the primary locale unless a `cmsLocaleId` is included in the request.</Tip>

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        items : typing.Sequence[DeleteItemsItemsRequestItemsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.collections.items import DeleteItemsItemsRequestItemsItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collections.items.delete_items(
                collection_id="580e63fc8c9a982ac9b8b745",
                items=[
                    DeleteItemsItemsRequestItemsItem(
                        id="580e64008c9a982ac9b8b754",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_items(collection_id, items=items, request_options=request_options)
        return _response.data

    async def update_items(
        self,
        collection_id: str,
        *,
        skip_invalid_files: typing.Optional[bool] = None,
        items: typing.Optional[typing.Sequence[UpdateItemsItemsRequestItemsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateItemsItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        Update a single item or multiple items in a Collection.

        The limit for this endpoint is 100 items.

        <Tip title="Localization Tip">Items will only be updated in the primary locale, unless a `cmsLocaleId` is included in the request.</Tip>

        <Note title="Draft status behavior">
          `isDraft: true` doesn't unpublish an item. The resulting status depends on whether the item has been published before:

          - **Item that has never been published:** the item gets a `Draft` status.
          - **Already-published item:** the item gets a `Changes in draft` status. The live item stays published, and your changes are held back until you publish them.

          Setting `isDraft: false` queues the item to publish on the next site publish. To remove an item from the live site, use [Unpublish Live Collection Items](/data/reference/cms/collection-items/live-items/delete-items-live). For the full status mapping, see [Publishing with the CMS API](/data/docs/working-with-the-cms/publishing).
        </Note>

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        skip_invalid_files : typing.Optional[bool]
            When true, invalid files are skipped and processing continues. When false, the entire request fails if any file is invalid.

        items : typing.Optional[typing.Sequence[UpdateItemsItemsRequestItemsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateItemsItemsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.collections.items import (
            UpdateItemsItemsRequestItemsItem,
            UpdateItemsItemsRequestItemsItemFieldData,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collections.items.update_items(
                collection_id="580e63fc8c9a982ac9b8b745",
                items=[
                    UpdateItemsItemsRequestItemsItem(
                        id="66f6ed9576ddacf3149d5ea6",
                        cms_locale_id="66f6e966c9e1dc700a857ca5",
                        field_data=UpdateItemsItemsRequestItemsItemFieldData(
                            name="Ne Paniquez Pas",
                            slug="ne-paniquez-pas",
                        ),
                    ),
                    UpdateItemsItemsRequestItemsItem(
                        id="66f6ed9576ddacf3149d5ea6",
                        cms_locale_id="66f6e966c9e1dc700a857ca4",
                        field_data=UpdateItemsItemsRequestItemsItemFieldData(
                            name="No Entrar en Pánico",
                            slug="no-entrar-en-panico",
                        ),
                    ),
                    UpdateItemsItemsRequestItemsItem(
                        id="66f6ed9576ddacf3149d5eaa",
                        cms_locale_id="66f6e966c9e1dc700a857ca5",
                        field_data=UpdateItemsItemsRequestItemsItemFieldData(
                            name="Au Revoir et Merci pour Tous les Poissons",
                            slug="au-revoir-et-merci",
                        ),
                    ),
                    UpdateItemsItemsRequestItemsItem(
                        id="66f6ed9576ddacf3149d5eaa",
                        cms_locale_id="66f6e966c9e1dc700a857ca4",
                        field_data=UpdateItemsItemsRequestItemsItemFieldData(
                            name="Hasta Luego y Gracias por Todo el Pescado",
                            slug="hasta-luego-y-gracias",
                        ),
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_items(
            collection_id, skip_invalid_files=skip_invalid_files, items=items, request_options=request_options
        )
        return _response.data

    async def list_items_live(
        self,
        collection_id: str,
        *,
        cms_locale_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        created_on: typing.Optional[ListItemsLiveItemsRequestCreatedOn] = None,
        last_published: typing.Optional[ListItemsLiveItemsRequestLastPublished] = None,
        last_updated: typing.Optional[ListItemsLiveItemsRequestLastUpdated] = None,
        filter: typing.Optional[typing.Dict[str, ListItemsLiveItemsRequestFilterValue]] = None,
        sort_by: typing.Optional[ListItemsLiveItemsRequestSortBy] = None,
        sort_order: typing.Optional[ListItemsLiveItemsRequestSortOrder] = None,
        sort: typing.Optional[typing.Dict[str, ListItemsLiveItemsRequestSortValue]] = None,
        translatable: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListItemsLiveItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        List all published items in a collection.

        <Tip title="Serve data with the Content Delivery API">
          Serving data to applications in real-time? Use the Content Delivery API at `api-cdn.webflow.com` for better performance. The CDN-backed endpoint is optimized for high-volume reads, while the Data API is designed for writes and management operations.
        </Tip>

        <Note>
          This endpoint supports:

          - Custom `filter[...]` queries support up to 10 filter terms and 2 text-search terms per request.
          - Custom `sort[...]` queries support up to 3 sort fields per request.
        </Note>

        Required scope | `CMS:read`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        cms_locale_id : typing.Optional[str]
            Unique identifier for a CMS Locale. This UID is different from the Site locale identifier and is listed as `cmsLocaleId` in the Sites response. To query multiple locales, input a comma separated string.

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        name : typing.Optional[str]
            Filter by the exact name of the item(s)

        slug : typing.Optional[str]
            Filter by the exact slug of the item

        created_on : typing.Optional[ListItemsLiveItemsRequestCreatedOn]
            Filter by the creation date of the item(s)

        last_published : typing.Optional[ListItemsLiveItemsRequestLastPublished]
            Filter by the last published date of the item(s)

        last_updated : typing.Optional[ListItemsLiveItemsRequestLastUpdated]
            Filter by the last updated date of the item(s)

        filter : typing.Optional[typing.Dict[str, ListItemsLiveItemsRequestFilterValue]]
            Filter collection items by custom field values. Use bracket notation:
            `filter[<fieldSlug>][<operator>]=<value>`.

            Example: `filter[price][gte]=10&filter[price][lte]=100&filter[name][contains]=shirt`.

            Filters are combined with AND. You can combine custom field filters with top-level filters such as `name`, `slug`, `createdOn`, `lastPublished`, and `lastUpdated`. OR logic and nested filter groups are not supported on GET requests.

            More filter terms can increase request latency.

            Supported operators by field type:

            | Field type | Supported operators |
            | --- | --- |
            | `id` | `eq`, `ne`, `in`, `nin` |
            | `PlainText` | `eq`, `ne`, `in`, `nin`, `contains`, `ncontains`, `exists` |
            | `Number` | `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`, `exists` |
            | `Switch` | `eq`, `ne`, `in`, `nin`, `exists` |
            | `DateTime` | `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`, `exists` |
            | `Email`, `Phone`, `Link` | `eq`, `ne`, `in`, `nin`, `contains`, `ncontains`, `exists` |
            | `Color` | `eq`, `ne`, `in`, `nin`, `exists` |
            | `Reference` | `eq`, `ne`, `in`, `nin`, `exists` |
            | `Option` | `eq`, `ne`, `in`, `nin` |
            | `RichText`, `Image`, `MultiImage`, `VideoLink`, `MultiReference` | `exists` |

            `contains` and `ncontains` are case-insensitive. `ncontains` also matches items where the field is empty or not set.

            `exists=true` matches items where the field has a value. `exists=false` matches items where the field is missing or null. For `Switch` fields, `false` is still a set value.

            Value formats:

            | Field type | Value format |
            | --- | --- |
            | `Number` | A valid number, such as `10` or `12.5` |
            | `Switch` | `true` or `false` |
            | `DateTime` | ISO 8601 date-time string |
            | `id`, `Reference` | 24-character item ID |
            | `Option` | Option ID |
            | `in`, `nin` | Comma-separated list, up to 100 values |

            Invalid fields, invalid values, and operators that do not apply to a field type return a `400 BadArgument` response.

        sort_by : typing.Optional[ListItemsLiveItemsRequestSortBy]
            Sort results by the provided value

        sort_order : typing.Optional[ListItemsLiveItemsRequestSortOrder]
            Sorts the results by asc or desc

        sort : typing.Optional[typing.Dict[str, ListItemsLiveItemsRequestSortValue]]
            Sort collection items by custom fields using bracket notation: `sort[<fieldSlug>]=<asc|desc>`.

            - Example: `sort[price]=desc`
            - Multiple sort fields are applied in query-string order. When `sort[...]` is provided, it takes precedence over `sortBy` and `sortOrder`.
            - Sortable field types: `PlainText`, `Email`, `Phone`, `Number`, `DateTime`, and `Switch`.
            - Unknown fields, invalid sort directions, and non-sortable field types return a `400 BadArgument` response.

        translatable : typing.Optional[str]
            Unique identifier for the secondary Locale you're translating **into**. Returns only content that hasn't been excluded from translation for that locale.

            This is independent of `localeId`, which selects which version of the content is returned. To fetch the source text to translate, request the primary locale's content and set `translatable` to the locale you're translating into:

            `?localeId={primary locale id}&translatable={target locale id}`

            Only exclusion rules scoped to manual translation are respected — rules scoped only to automatic translation don't affect this parameter's response.

            Omitting `translatable` returns the same response as if this parameter didn't exist. The value must be the id of one of the site's secondary locales — the primary locale id, or any other value, returns a `400` error. Requires translation exclusions to be enabled for the site; if they aren't, the request returns a `403` error.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListItemsLiveItemsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collections.items.list_items_live(
                collection_id="580e63fc8c9a982ac9b8b745",
                translatable="65427cf400e02b306eaa04a0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_items_live(
            collection_id,
            cms_locale_id=cms_locale_id,
            offset=offset,
            limit=limit,
            name=name,
            slug=slug,
            created_on=created_on,
            last_published=last_published,
            last_updated=last_updated,
            filter=filter,
            sort_by=sort_by,
            sort_order=sort_order,
            sort=sort,
            translatable=translatable,
            request_options=request_options,
        )
        return _response.data

    async def create_item_live(
        self,
        collection_id: str,
        *,
        request: CreateItemLiveItemsRequestBody,
        skip_invalid_files: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateItemLiveItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        Create item(s) in a collection that will be immediately published to the live site.

        This endpoint accepts two request shapes, and a request must use one or the other:

        - **Single item** — send `fieldData` at the top level. Set `cmsLocaleId` to create the item in a specific locale.
        - **Multiple items** — send an `items` array with at least one entry. Each entry needs its own `fieldData`, and can set its own `cmsLocaleId`, `isDraft`, and `isArchived`. The API ignores any other property on an entry.

        ```json
        {
          "items": [
            {
              "isArchived": false,
              "isDraft": false,
              "fieldData": {
                "name": "Senior Data Analyst",
                "slug": "senior-data-analyst"
              }
            },
            {
              "isArchived": false,
              "isDraft": false,
              "fieldData": {
                "name": "Product Manager",
                "slug": "product-manager"
              }
            }
          ]
        }
        ```

        A request that carries both `fieldData` and `items` returns a `400`.

        To create items across multiple locales, [please use this endpoint.](/data/reference/cms/collection-items/staged-items/create-items)

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        request : CreateItemLiveItemsRequestBody

        skip_invalid_files : typing.Optional[bool]
            When true, invalid files are skipped and processing continues. When false, the entire request fails if any file is invalid.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateItemLiveItemsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.collections.items import SingleLiveItem, SingleLiveItemFieldData

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collections.items.create_item_live(
                collection_id="580e63fc8c9a982ac9b8b745",
                request=SingleLiveItem(
                    is_archived=False,
                    is_draft=False,
                    field_data=SingleLiveItemFieldData(
                        name="The Hitchhiker's Guide to the Galaxy",
                        slug="hitchhikers-guide-to-the-galaxy",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_item_live(
            collection_id, request=request, skip_invalid_files=skip_invalid_files, request_options=request_options
        )
        return _response.data

    async def delete_items_live(
        self,
        collection_id: str,
        *,
        items: typing.Sequence[DeleteItemsLiveItemsRequestItemsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Unpublish up to 100 items from the live site and set the `isDraft` property to `true`.

        <Tip title="Localization Tip">Items will only be unpublished in the primary locale unless a `cmsLocaleId` is included in the request.</Tip>

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        items : typing.Sequence[DeleteItemsLiveItemsRequestItemsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.collections.items import DeleteItemsLiveItemsRequestItemsItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collections.items.delete_items_live(
                collection_id="580e63fc8c9a982ac9b8b745",
                items=[
                    DeleteItemsLiveItemsRequestItemsItem(
                        id="580e64008c9a982ac9b8b754",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_items_live(
            collection_id, items=items, request_options=request_options
        )
        return _response.data

    async def update_items_live(
        self,
        collection_id: str,
        *,
        skip_invalid_files: typing.Optional[bool] = None,
        items: typing.Optional[typing.Sequence[UpdateItemsLiveItemsRequestItemsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateItemsLiveItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        Update a single published item or multiple published items (up to 100) in a Collection

        <Tip title="Localization Tip">Items will only be updated in the primary locale, unless a `cmsLocaleId` is included in the request.</Tip>

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        skip_invalid_files : typing.Optional[bool]
            When true, invalid files are skipped and processing continues. When false, the entire request fails if any file is invalid.

        items : typing.Optional[typing.Sequence[UpdateItemsLiveItemsRequestItemsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateItemsLiveItemsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.collections.items import (
            UpdateItemsLiveItemsRequestItemsItem,
            UpdateItemsLiveItemsRequestItemsItemFieldData,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collections.items.update_items_live(
                collection_id="580e63fc8c9a982ac9b8b745",
                items=[
                    UpdateItemsLiveItemsRequestItemsItem(
                        id="66f6ed9576ddacf3149d5ea6",
                        cms_locale_id="66f6e966c9e1dc700a857ca5",
                        field_data=UpdateItemsLiveItemsRequestItemsItemFieldData(
                            name="Ne Paniquez Pas",
                            slug="ne-paniquez-pas",
                        ),
                    ),
                    UpdateItemsLiveItemsRequestItemsItem(
                        id="66f6ed9576ddacf3149d5ea6",
                        cms_locale_id="66f6e966c9e1dc700a857ca4",
                        field_data=UpdateItemsLiveItemsRequestItemsItemFieldData(
                            name="No Entrar en Pánico",
                            slug="no-entrar-en-panico",
                        ),
                    ),
                    UpdateItemsLiveItemsRequestItemsItem(
                        id="66f6ed9576ddacf3149d5eaa",
                        cms_locale_id="66f6e966c9e1dc700a857ca5",
                        field_data=UpdateItemsLiveItemsRequestItemsItemFieldData(
                            name="Au Revoir et Merci pour Tous les Poissons",
                            slug="au-revoir-et-merci",
                        ),
                    ),
                    UpdateItemsLiveItemsRequestItemsItem(
                        id="66f6ed9576ddacf3149d5eaa",
                        cms_locale_id="66f6e966c9e1dc700a857ca4",
                        field_data=UpdateItemsLiveItemsRequestItemsItemFieldData(
                            name="Hasta Luego y Gracias por Todo el Pescado",
                            slug="hasta-luego-y-gracias",
                        ),
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_items_live(
            collection_id, skip_invalid_files=skip_invalid_files, items=items, request_options=request_options
        )
        return _response.data

    async def create_items(
        self,
        collection_id: str,
        *,
        field_data: CreateItemsItemsRequestFieldData,
        skip_invalid_files: typing.Optional[bool] = None,
        cms_locale_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        is_archived: typing.Optional[bool] = OMIT,
        is_draft: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateItemsItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        Create an item or multiple items in a CMS Collection across multiple corresponding locales.

        <Note>
          - This endpoint can create up to 100 items in a request.
          - If the `cmsLocaleIds` parameter is not included in the request, an item will only be created in the primary locale.
        </Note>

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        field_data : CreateItemsItemsRequestFieldData

        skip_invalid_files : typing.Optional[bool]
            When true, invalid files are skipped and processing continues. When false, the entire request fails if any file is invalid.

        cms_locale_ids : typing.Optional[typing.Sequence[str]]
            Array of identifiers for the locales where the item will be created

        is_archived : typing.Optional[bool]
            Indicates whether the item is archived.

        is_draft : typing.Optional[bool]
            Indicates whether the item is in draft state.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateItemsItemsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.collections.items import SingleCmsItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collections.items.create_items(
                collection_id="580e63fc8c9a982ac9b8b745",
                cms_locale_ids=[
                    "66f6e966c9e1dc700a857ca3",
                    "66f6e966c9e1dc700a857ca4",
                    "66f6e966c9e1dc700a857ca5",
                ],
                is_archived=False,
                is_draft=False,
                field_data=SingleCmsItem(
                    name="Don’t Panic",
                    slug="dont-panic",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_items(
            collection_id,
            field_data=field_data,
            skip_invalid_files=skip_invalid_files,
            cms_locale_ids=cms_locale_ids,
            is_archived=is_archived,
            is_draft=is_draft,
            request_options=request_options,
        )
        return _response.data

    async def get_item(
        self,
        collection_id: str,
        item_id: str,
        *,
        cms_locale_id: typing.Optional[str] = None,
        translatable: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetItemItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        Get details of a selected Collection Item.

        Required scope | `CMS:read`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        item_id : str
            Unique identifier for an Item

        cms_locale_id : typing.Optional[str]
            Unique identifier for a CMS Locale. This UID is different from the Site locale identifier and is listed as `cmsLocaleId` in the Sites response. This endpoint returns a single item, so it accepts one locale. To retrieve an item in several locales, use [List Collection Items](/data/reference/cms/collection-items/staged-items/list-items) with `filter[id][eq]` and a comma separated `cmsLocaleId`.

        translatable : typing.Optional[str]
            Unique identifier for the secondary Locale you're translating **into**. Returns only content that hasn't been excluded from translation for that locale.

            This is independent of `localeId`, which selects which version of the content is returned. To fetch the source text to translate, request the primary locale's content and set `translatable` to the locale you're translating into:

            `?localeId={primary locale id}&translatable={target locale id}`

            Only exclusion rules scoped to manual translation are respected — rules scoped only to automatic translation don't affect this parameter's response.

            Omitting `translatable` returns the same response as if this parameter didn't exist. The value must be the id of one of the site's secondary locales — the primary locale id, or any other value, returns a `400` error. Requires translation exclusions to be enabled for the site; if they aren't, the request returns a `403` error.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetItemItemsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collections.items.get_item(
                collection_id="580e63fc8c9a982ac9b8b745",
                item_id="580e64008c9a982ac9b8b754",
                translatable="65427cf400e02b306eaa04a0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_item(
            collection_id,
            item_id,
            cms_locale_id=cms_locale_id,
            translatable=translatable,
            request_options=request_options,
        )
        return _response.data

    async def delete_item(
        self,
        collection_id: str,
        item_id: str,
        *,
        cms_locale_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete an item from a collection.

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        item_id : str
            Unique identifier for an Item

        cms_locale_id : typing.Optional[str]
            Unique identifier for a CMS Locale. This UID is different from the Site locale identifier and is listed as `cmsLocaleId` in the Sites response. To query multiple locales, input a comma separated string.

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
            await client.collections.items.delete_item(
                collection_id="580e63fc8c9a982ac9b8b745",
                item_id="580e64008c9a982ac9b8b754",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_item(
            collection_id, item_id, cms_locale_id=cms_locale_id, request_options=request_options
        )
        return _response.data

    async def update_item(
        self,
        collection_id: str,
        item_id: str,
        *,
        skip_invalid_files: typing.Optional[bool] = None,
        cms_locale_id: typing.Optional[str] = OMIT,
        is_archived: typing.Optional[bool] = OMIT,
        is_draft: typing.Optional[bool] = OMIT,
        field_data: typing.Optional[UpdateItemItemsRequestFieldData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateItemItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        Update a selected Item in a Collection.

        <Note title="Draft status behavior">
          `isDraft: true` doesn't unpublish an item. The resulting status depends on whether the item has been published before:

          - **Item that has never been published:** the item gets a `Draft` status.
          - **Already-published item:** the item gets a `Changes in draft` status. The live item stays published, and your changes are held back until you publish them.

          Setting `isDraft: false` queues the item to publish on the next site publish. To remove an item from the live site, use [Unpublish Live Collection Items](/data/reference/cms/collection-items/live-items/delete-items-live). For the full status mapping, see [Publishing with the CMS API](/data/docs/working-with-the-cms/publishing).
        </Note>

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        item_id : str
            Unique identifier for an Item

        skip_invalid_files : typing.Optional[bool]
            When true, invalid files are skipped and processing continues. When false, the entire request fails if any file is invalid.

        cms_locale_id : typing.Optional[str]
            Identifier for the locale of the CMS item

        is_archived : typing.Optional[bool]
            Boolean determining if the Item is set to archived

        is_draft : typing.Optional[bool]
            Sets the item's draft state. The resulting status depends on whether the item has been published before:

            - **Item that has never been published:** `isDraft: true` results in a `Draft` status.
            - **Already-published item:** `isDraft: true` results in a `Changes in draft` status. The live item stays published, and your changes are held back until you publish them.

            Setting `isDraft: true` never unpublishes an item. To remove an item from the live site, use [Unpublish Live Collection Items](/data/reference/cms/collection-items/live-items/delete-items-live).

        field_data : typing.Optional[UpdateItemItemsRequestFieldData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateItemItemsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.collections.items import UpdateItemItemsRequestFieldData

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collections.items.update_item(
                collection_id="580e63fc8c9a982ac9b8b745",
                item_id="580e64008c9a982ac9b8b754",
                is_archived=False,
                is_draft=False,
                field_data=UpdateItemItemsRequestFieldData(
                    name="The Hitchhiker's Guide to the Galaxy",
                    slug="hitchhikers-guide-to-the-galaxy",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_item(
            collection_id,
            item_id,
            skip_invalid_files=skip_invalid_files,
            cms_locale_id=cms_locale_id,
            is_archived=is_archived,
            is_draft=is_draft,
            field_data=field_data,
            request_options=request_options,
        )
        return _response.data

    async def get_item_live(
        self,
        collection_id: str,
        item_id: str,
        *,
        cms_locale_id: typing.Optional[str] = None,
        translatable: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetItemLiveItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        Get details of a selected Collection live Item.

        <Tip title="Serve data with the Content Delivery API">
          Serving data to applications in real-time? Use the Content Delivery API at `api-cdn.webflow.com` for better performance. The CDN-backed endpoint is optimized for high-volume reads, while the Data API is designed for writes and management operations.
        </Tip>

        Required scope | `CMS:read`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        item_id : str
            Unique identifier for an Item

        cms_locale_id : typing.Optional[str]
            Unique identifier for a CMS Locale. This UID is different from the Site locale identifier and is listed as `cmsLocaleId` in the Sites response. This endpoint returns a single item, so it accepts one locale. To retrieve an item in several locales, use [List Collection Items](/data/reference/cms/collection-items/staged-items/list-items) with `filter[id][eq]` and a comma separated `cmsLocaleId`.

        translatable : typing.Optional[str]
            Unique identifier for the secondary Locale you're translating **into**. Returns only content that hasn't been excluded from translation for that locale.

            This is independent of `localeId`, which selects which version of the content is returned. To fetch the source text to translate, request the primary locale's content and set `translatable` to the locale you're translating into:

            `?localeId={primary locale id}&translatable={target locale id}`

            Only exclusion rules scoped to manual translation are respected — rules scoped only to automatic translation don't affect this parameter's response.

            Omitting `translatable` returns the same response as if this parameter didn't exist. The value must be the id of one of the site's secondary locales — the primary locale id, or any other value, returns a `400` error. Requires translation exclusions to be enabled for the site; if they aren't, the request returns a `403` error.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetItemLiveItemsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collections.items.get_item_live(
                collection_id="580e63fc8c9a982ac9b8b745",
                item_id="580e64008c9a982ac9b8b754",
                translatable="65427cf400e02b306eaa04a0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_item_live(
            collection_id,
            item_id,
            cms_locale_id=cms_locale_id,
            translatable=translatable,
            request_options=request_options,
        )
        return _response.data

    async def delete_item_live(
        self,
        collection_id: str,
        item_id: str,
        *,
        cms_locale_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Unpublish a live item from the site and set the `isDraft` property to `true`.

        For bulk unpublishing, please use [this endpoint.](/data/v2.0.0/reference/cms/collection-items/live-items/delete-items-live)

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        item_id : str
            Unique identifier for an Item

        cms_locale_id : typing.Optional[str]
            Unique identifier for a CMS Locale. This UID is different from the Site locale identifier and is listed as `cmsLocaleId` in the Sites response. To query multiple locales, input a comma separated string.

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
            await client.collections.items.delete_item_live(
                collection_id="580e63fc8c9a982ac9b8b745",
                item_id="580e64008c9a982ac9b8b754",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_item_live(
            collection_id, item_id, cms_locale_id=cms_locale_id, request_options=request_options
        )
        return _response.data

    async def update_item_live(
        self,
        collection_id: str,
        item_id: str,
        *,
        skip_invalid_files: typing.Optional[bool] = None,
        cms_locale_id: typing.Optional[str] = OMIT,
        is_archived: typing.Optional[bool] = OMIT,
        is_draft: typing.Optional[bool] = OMIT,
        field_data: typing.Optional[UpdateItemLiveItemsRequestFieldData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateItemLiveItemsResponse:
        """
        <Tip title="Components in Rich Text">
          Rich Text field values may contain Webflow component instances as `<wf-component>` markup. On read they appear inline in the field's HTML; on write, the same markup creates or updates the instance.

          Scalar props are `prop-<propId>="…"` attributes on the `<wf-component>`. Text and rich-text props are nested `<wf-prop name="<propId>" type="text|richtext">…</wf-prop>` children.

          A write is rejected with a `400` if a component can't be resolved, contains a Collection List, populates a Slot (a component with an unpopulated Slot is allowed), includes an unknown prop, or creates a new instance in a secondary locale.

          `component-id` and each `prop-<propId>` are specific to your site's component definition — obtain them by listing your site's components (`GET /v2/sites/{site_id}/components`, plus `/components/{component_id}/properties` for prop IDs) or by reading an item that already contains the component and reusing the returned markup. Omit `data-w-id` when creating an instance (the server assigns it); keep it when updating one.
        </Tip>

        Update a selected live Item in a Collection. The updates for this Item will be published to the live site.

        Required scope | `CMS:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        item_id : str
            Unique identifier for an Item

        skip_invalid_files : typing.Optional[bool]
            When true, invalid files are skipped and processing continues. When false, the entire request fails if any file is invalid.

        cms_locale_id : typing.Optional[str]
            Identifier for the locale of the CMS item

        is_archived : typing.Optional[bool]
            Boolean determining if the Item is set to archived

        is_draft : typing.Optional[bool]
            Sets the item's draft state. The resulting status depends on whether the item has been published before:

            - **Item that has never been published:** `isDraft: true` results in a `Draft` status.
            - **Already-published item:** `isDraft: true` results in a `Changes in draft` status. The live item stays published, and your changes are held back until you publish them.

            Setting `isDraft: true` never unpublishes an item. To remove an item from the live site, use [Unpublish Live Collection Items](/data/reference/cms/collection-items/live-items/delete-items-live).

        field_data : typing.Optional[UpdateItemLiveItemsRequestFieldData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateItemLiveItemsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.collections.items import UpdateItemLiveItemsRequestFieldData

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collections.items.update_item_live(
                collection_id="580e63fc8c9a982ac9b8b745",
                item_id="580e64008c9a982ac9b8b754",
                is_archived=False,
                is_draft=False,
                field_data=UpdateItemLiveItemsRequestFieldData(
                    name="The Hitchhiker's Guide to the Galaxy",
                    slug="hitchhikers-guide-to-the-galaxy",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_item_live(
            collection_id,
            item_id,
            skip_invalid_files=skip_invalid_files,
            cms_locale_id=cms_locale_id,
            is_archived=is_archived,
            is_draft=is_draft,
            field_data=field_data,
            request_options=request_options,
        )
        return _response.data

    async def publish_item(
        self,
        collection_id: str,
        *,
        request: PublishItemItemsRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PublishItemItemsResponse:
        """
        Publish an item or multiple items.

        Required scope | `cms:write`

        Parameters
        ----------
        collection_id : str
            Unique identifier for a Collection

        request : PublishItemItemsRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublishItemItemsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.collections.items import ItemIDs

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.collections.items.publish_item(
                collection_id="580e63fc8c9a982ac9b8b745",
                request=ItemIDs(
                    item_ids=[
                        "643fd856d66b6528195ee2ca",
                        "643fd856d66b6528195ee2cb",
                        "643fd856d66b6528195ee2cc",
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publish_item(collection_id, request=request, request_options=request_options)
        return _response.data
