

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .catalog_query_exact import CatalogQueryExact
from .catalog_query_item_variations_for_item_option_values import CatalogQueryItemVariationsForItemOptionValues
from .catalog_query_items_for_item_options import CatalogQueryItemsForItemOptions
from .catalog_query_items_for_modifier_list import CatalogQueryItemsForModifierList
from .catalog_query_items_for_tax import CatalogQueryItemsForTax
from .catalog_query_prefix import CatalogQueryPrefix
from .catalog_query_range import CatalogQueryRange
from .catalog_query_set import CatalogQuerySet
from .catalog_query_sorted_attribute import CatalogQuerySortedAttribute
from .catalog_query_text import CatalogQueryText


class CatalogQuery(UniversalBaseModel):
    """
    A query composed of one or more different types of filters to narrow the scope of targeted objects when calling the `SearchCatalogObjects` endpoint.

    Although a query can have multiple filters, only certain query types can be combined per call to [SearchCatalogObjects](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-objects).
    Any combination of the following types may be used together:
    - [exact_query](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogQueryExact)
    - [prefix_query](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogQueryPrefix)
    - [range_query](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogQueryRange)
    - [sorted_attribute_query](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogQuerySortedAttribute)
    - [text_query](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogQueryText)
    All other query types cannot be combined with any others.

    When a query filter is based on an attribute, the attribute must be searchable.
    Searchable attributes are listed as follows, along their parent types that can be searched for with applicable query filters.

    * Searchable attribute and objects queryable by searchable attributes **
    - `name`:  `CatalogItem`, `CatalogItemVariation`, `CatalogCategory`, `CatalogTax`, `CatalogDiscount`, `CatalogModifier`, 'CatalogModifierList`, `CatalogItemOption`, `CatalogItemOptionValue`
    - `description`: `CatalogItem`, `CatalogItemOptionValue`
    - `abbreviation`: `CatalogItem`
    - `upc`: `CatalogItemVariation`
    - `sku`: `CatalogItemVariation`
    - `caption`: `CatalogImage`
    - `display_name`: `CatalogItemOption`

    For example, to search for [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) objects by searchable attributes, you can use
    the `"name"`, `"description"`, or `"abbreviation"` attribute in an applicable query filter.
    """

    exact_query: typing.Optional[CatalogQueryExact] = None
    item_variations_for_item_option_values_query: typing.Optional[CatalogQueryItemVariationsForItemOptionValues] = None
    items_for_item_options_query: typing.Optional[CatalogQueryItemsForItemOptions] = None
    items_for_modifier_list_query: typing.Optional[CatalogQueryItemsForModifierList] = None
    items_for_tax_query: typing.Optional[CatalogQueryItemsForTax] = None
    prefix_query: typing.Optional[CatalogQueryPrefix] = None
    range_query: typing.Optional[CatalogQueryRange] = None
    set_query: typing.Optional[CatalogQuerySet] = None
    sorted_attribute_query: typing.Optional[CatalogQuerySortedAttribute] = None
    text_query: typing.Optional[CatalogQueryText] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
