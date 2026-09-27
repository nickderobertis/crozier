

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .positive_integer import PositiveInteger
from .positive_integer_default0 import PositiveIntegerDefault0
from .schema_type import SchemaType
from .string_array import StringArray


class Schema(UniversalBaseModel):
    """
    Core schema meta-schema
    """

    id: typing.Optional[str] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="$schema"), pydantic.Field(alias="$schema")
    ] = None
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    default: typing.Optional[typing.Any] = None
    multiple_of: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="multipleOf"), pydantic.Field(alias="multipleOf")
    ] = None
    maximum: typing.Optional[float] = None
    exclusive_maximum: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="exclusiveMaximum"), pydantic.Field(alias="exclusiveMaximum")
    ] = None
    minimum: typing.Optional[float] = None
    exclusive_minimum: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="exclusiveMinimum"), pydantic.Field(alias="exclusiveMinimum")
    ] = None
    max_length: typing_extensions.Annotated[
        typing.Optional[PositiveInteger], FieldMetadata(alias="maxLength"), pydantic.Field(alias="maxLength")
    ] = None
    min_length: typing_extensions.Annotated[
        typing.Optional[PositiveIntegerDefault0], FieldMetadata(alias="minLength"), pydantic.Field(alias="minLength")
    ] = None
    pattern: typing.Optional[str] = None
    additional_items: typing_extensions.Annotated[
        typing.Optional["SchemaAdditionalItems"],
        FieldMetadata(alias="additionalItems"),
        pydantic.Field(alias="additionalItems"),
    ] = None
    items: typing.Optional["SchemaItems"] = None
    max_items: typing_extensions.Annotated[
        typing.Optional[PositiveInteger], FieldMetadata(alias="maxItems"), pydantic.Field(alias="maxItems")
    ] = None
    min_items: typing_extensions.Annotated[
        typing.Optional[PositiveIntegerDefault0], FieldMetadata(alias="minItems"), pydantic.Field(alias="minItems")
    ] = None
    unique_items: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="uniqueItems"), pydantic.Field(alias="uniqueItems")
    ] = None
    max_properties: typing_extensions.Annotated[
        typing.Optional[PositiveInteger], FieldMetadata(alias="maxProperties"), pydantic.Field(alias="maxProperties")
    ] = None
    min_properties: typing_extensions.Annotated[
        typing.Optional[PositiveIntegerDefault0],
        FieldMetadata(alias="minProperties"),
        pydantic.Field(alias="minProperties"),
    ] = None
    required: typing.Optional[StringArray] = None
    additional_properties: typing_extensions.Annotated[
        typing.Optional["SchemaAdditionalProperties"],
        FieldMetadata(alias="additionalProperties"),
        pydantic.Field(alias="additionalProperties"),
    ] = None
    definitions: typing.Optional[typing.Dict[str, "Schema"]] = None
    properties: typing.Optional[typing.Dict[str, "Schema"]] = None
    pattern_properties: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, "Schema"]],
        FieldMetadata(alias="patternProperties"),
        pydantic.Field(alias="patternProperties"),
    ] = None
    dependencies: typing.Optional[typing.Dict[str, "SchemaDependenciesValue"]] = None
    enum: typing.Optional[typing.List[typing.Any]] = None
    type: typing.Optional[SchemaType] = None
    all_of: typing_extensions.Annotated[
        typing.Optional["SchemaArray"], FieldMetadata(alias="allOf"), pydantic.Field(alias="allOf")
    ] = None
    any_of: typing_extensions.Annotated[
        typing.Optional["SchemaArray"], FieldMetadata(alias="anyOf"), pydantic.Field(alias="anyOf")
    ] = None
    one_of: typing_extensions.Annotated[
        typing.Optional["SchemaArray"], FieldMetadata(alias="oneOf"), pydantic.Field(alias="oneOf")
    ] = None
    not_: typing_extensions.Annotated[
        typing.Optional["Schema"], FieldMetadata(alias="not"), pydantic.Field(alias="not")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .schema_additional_items import SchemaAdditionalItems
from .schema_additional_properties import SchemaAdditionalProperties
from .schema_array import SchemaArray
from .schema_dependencies_value import SchemaDependenciesValue
from .schema_items import SchemaItems

update_forward_refs(
    Schema,
    SchemaAdditionalItems=SchemaAdditionalItems,
    SchemaAdditionalProperties=SchemaAdditionalProperties,
    SchemaArray=SchemaArray,
    SchemaDependenciesValue=SchemaDependenciesValue,
    SchemaItems=SchemaItems,
)
