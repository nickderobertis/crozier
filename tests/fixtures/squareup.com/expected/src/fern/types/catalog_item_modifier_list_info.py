

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .catalog_modifier_override import CatalogModifierOverride


class CatalogItemModifierListInfo(UniversalBaseModel):
    """
    Options to control the properties of a `CatalogModifierList` applied to a `CatalogItem` instance.
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `true`, enable this `CatalogModifierList`. The default value is `true`.
    """

    max_selected_modifiers: typing.Optional[int] = pydantic.Field(default=None)
    """
    If 0 or larger, the largest number of `CatalogModifier`s that can be selected from this `CatalogModifierList`.
    """

    min_selected_modifiers: typing.Optional[int] = pydantic.Field(default=None)
    """
    If 0 or larger, the smallest number of `CatalogModifier`s that must be selected from this `CatalogModifierList`.
    """

    modifier_list_id: str = pydantic.Field()
    """
    The ID of the `CatalogModifierList` controlled by this `CatalogModifierListInfo`.
    """

    modifier_overrides: typing.Optional[typing.List[CatalogModifierOverride]] = pydantic.Field(default=None)
    """
    A set of `CatalogModifierOverride` objects that override whether a given `CatalogModifier` is enabled by default.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
