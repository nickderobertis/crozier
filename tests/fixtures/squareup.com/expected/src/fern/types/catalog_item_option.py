

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class CatalogItemOption(UniversalBaseModel):
    """
    A group of variations for a `CatalogItem`.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The item option's human-readable description. Displayed in the Square
    Point of Sale app for the seller and in the Online Store or on receipts for
    the buyer. This is a searchable attribute for use in applicable query filters.
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The item option's display name for the customer. This is a searchable attribute for use in applicable query filters.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The item option's display name for the seller. Must be unique across
    all item options. This is a searchable attribute for use in applicable query filters.
    """

    show_colors: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, display colors for entries in `values` when present.
    """

    values: typing.Optional[typing.List["CatalogObject"]] = pydantic.Field(default=None)
    """
    A list of CatalogObjects containing the
    `CatalogItemOptionValue`s for this item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .catalog_object import CatalogObject

update_forward_refs(CatalogItemOption)
