

from __future__ import annotations

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .schema_property_type import SchemaPropertyType


class SchemaProperty(UniversalBaseModel):
    items: typing.Optional[typing.List["SchemaProperty"]] = pydantic.Field(default=None)
    """
    Used if type is array
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the field (optional for array/object children)
    """

    properties: typing.Optional[typing.List["SchemaProperty"]] = pydantic.Field(default=None)
    """
    Used if type is object
    """

    type: SchemaPropertyType
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(SchemaProperty)
