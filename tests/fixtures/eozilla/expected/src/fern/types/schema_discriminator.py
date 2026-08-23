

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class SchemaDiscriminator(UniversalBaseModel):
    property_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="propertyName"), pydantic.Field(alias="propertyName")
    ] = None
    mapping: typing.Optional[typing.Dict[str, "Schema"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .schema import Schema
from .schema_additional_properties import SchemaAdditionalProperties
from .schema_items import SchemaItems

update_forward_refs(
    SchemaDiscriminator, Schema=Schema, SchemaAdditionalProperties=SchemaAdditionalProperties, SchemaItems=SchemaItems
)
