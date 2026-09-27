

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .body_fifteen_type import BodyFifteenType


class BodyFifteen(UniversalBaseModel):
    """
    json schema body matcher
    """

    not_: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="not"), pydantic.Field(alias="not")
    ] = None
    optional: typing.Optional[bool] = None
    type: typing.Optional[BodyFifteenType] = None
    json_schema: typing_extensions.Annotated[
        typing.Optional["Schema"], FieldMetadata(alias="jsonSchema"), pydantic.Field(alias="jsonSchema")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .schema import Schema
from .schema_additional_items import SchemaAdditionalItems
from .schema_additional_properties import SchemaAdditionalProperties
from .schema_array import SchemaArray
from .schema_dependencies_value import SchemaDependenciesValue
from .schema_items import SchemaItems

update_forward_refs(
    BodyFifteen,
    Schema=Schema,
    SchemaAdditionalItems=SchemaAdditionalItems,
    SchemaAdditionalProperties=SchemaAdditionalProperties,
    SchemaArray=SchemaArray,
    SchemaDependenciesValue=SchemaDependenciesValue,
    SchemaItems=SchemaItems,
)
