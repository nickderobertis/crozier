

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .unified_property import UnifiedProperty


class SupportedProperty(UniversalBaseModel):
    child_properties: typing.Optional[typing.List["SupportedPropertyChildPropertiesItem"]] = pydantic.Field(
        default=None
    )
    """
    List of child properties of the unified property.
    """

    unified_property: typing.Optional[UnifiedProperty] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .supported_property_child_properties_item import SupportedPropertyChildPropertiesItem

update_forward_refs(SupportedProperty)
