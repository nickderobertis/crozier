

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .catalog_item_modifier_list_info import CatalogItemModifierListInfo
from .catalog_item_option_for_item import CatalogItemOptionForItem


class CatalogItem(UniversalBaseModel):
    """
    A [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) instance of the `ITEM` type, also referred to as an item, in the catalog.
    """

    abbreviation: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text of the item's display label in the Square Point of Sale app. Only up to the first five characters of the string are used.
    This attribute is searchable, and its value length is of Unicode code points.
    """

    available_electronically: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `true`, the item can be added to electronically fulfilled orders from the merchant's online store.
    """

    available_for_pickup: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `true`, the item can be added to pickup orders from the merchant's online store.
    """

    available_online: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `true`, the item can be added to shipping orders from the merchant's online store.
    """

    category_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the item's category, if any.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The item's description. This is a searchable attribute for use in applicable query filters, and its value length is of Unicode code points.
    """

    item_options: typing.Optional[typing.List[CatalogItemOptionForItem]] = pydantic.Field(default=None)
    """
    List of item options IDs for this item. Used to manage and group item
    variations in a specified order.
    
    Maximum: 6 item options.
    """

    label_color: typing.Optional[str] = pydantic.Field(default=None)
    """
    The color of the item's display label in the Square Point of Sale app. This must be a valid hex color code.
    """

    modifier_list_info: typing.Optional[typing.List[CatalogItemModifierListInfo]] = pydantic.Field(default=None)
    """
    A set of `CatalogItemModifierListInfo` objects
    representing the modifier lists that apply to this item, along with the overrides and min
    and max limits that are specific to this item. Modifier lists
    may also be added to or deleted from an item using `UpdateItemModifierLists`.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The item's name. This is a searchable attribute for use in applicable query filters, its value must not be empty, and the length is of Unicode code points.
    """

    product_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The product type of the item. May not be changed once an item has been created.
    
    Only items of product type `REGULAR` or `APPOINTMENTS_SERVICE` may be created by this API; items with other product
    types are read-only.
    """

    skip_modifier_screen: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `false`, the Square Point of Sale app will present the `CatalogItem`'s
    details screen immediately, allowing the merchant to choose `CatalogModifier`s
    before adding the item to the cart.  This is the default behavior.
    
    If `true`, the Square Point of Sale app will immediately add the item to the cart with the pre-selected
    modifiers, and merchants can edit modifiers by drilling down onto the item's details.
    
    Third-party clients are encouraged to implement similar behaviors.
    """

    sort_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A name to sort the item by. If this name is unspecified, namely, the `sort_name` field is absent, the regular `name` field is used for sorting.
    
    It is currently supported for sellers of the Japanese locale only.
    """

    tax_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A set of IDs indicating the taxes enabled for
    this item. When updating an item, any taxes listed here will be added to the item.
    Taxes may also be added to or deleted from an item using `UpdateItemTaxes`.
    """

    variations: typing.Optional[typing.List["CatalogObject"]] = pydantic.Field(default=None)
    """
    A list of [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) objects for this item. An item must have
    at least one variation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .catalog_item_option import CatalogItemOption
from .catalog_modifier_list import CatalogModifierList
from .catalog_object import CatalogObject

update_forward_refs(
    CatalogItem,
    CatalogItemOption=CatalogItemOption,
    CatalogModifierList=CatalogModifierList,
    CatalogObject=CatalogObject,
)
