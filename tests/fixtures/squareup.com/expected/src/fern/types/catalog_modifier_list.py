

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class CatalogModifierList(UniversalBaseModel):
    """
    A list of modifiers applicable to items at the time of sale.

    For example, a "Condiments" modifier list applicable to a "Hot Dog" item
    may contain "Ketchup", "Mustard", and "Relish" modifiers.
    Use the `selection_type` field to specify whether or not multiple selections from
    the modifier list are allowed.
    """

    modifiers: typing.Optional[typing.List["CatalogObject"]] = pydantic.Field(default=None)
    """
    The options included in the `CatalogModifierList`.
    You must include at least one `CatalogModifier`.
    Each CatalogObject must have type `MODIFIER` and contain
    `CatalogModifier` data.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name for the `CatalogModifierList` instance. This is a searchable attribute for use in applicable query filters, and its value length is of Unicode code points.
    """

    ordinal: typing.Optional[int] = pydantic.Field(default=None)
    """
    Determines where this modifier list appears in a list of `CatalogModifierList` values.
    """

    selection_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates whether multiple options from the modifier list
    can be applied to a single `CatalogItem`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .catalog_object import CatalogObject

update_forward_refs(CatalogModifierList)
