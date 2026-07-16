

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CatalogItemOptionValue(UniversalBaseModel):
    """
    An enumerated value that can link a
    `CatalogItemVariation` to an item option as one of
    its item option values.
    """

    color: typing.Optional[str] = pydantic.Field(default=None)
    """
    The HTML-supported hex color for the item option (e.g., "#ff8d4e85").
    Only displayed if `show_colors` is enabled on the parent `ItemOption`. When
    left unset, `color` defaults to white ("#ffffff") when `show_colors` is
    enabled on the parent `ItemOption`.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable description for the option value. This is a searchable attribute for use in applicable query filters.
    """

    item_option_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique ID of the associated item option.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of this item option value. This is a searchable attribute for use in applicable query filters.
    """

    ordinal: typing.Optional[int] = pydantic.Field(default=None)
    """
    Determines where this option value appears in a list of option values.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
