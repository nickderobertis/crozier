

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .data_type import DataType


class Schema(UniversalBaseModel):
    ref: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="$ref"), pydantic.Field(alias="$ref")
    ] = None
    title: typing.Optional[str] = None
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
        typing.Optional[int], FieldMetadata(alias="maxLength"), pydantic.Field(alias="maxLength")
    ] = None
    min_length: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="minLength"), pydantic.Field(alias="minLength")
    ] = None
    pattern: typing.Optional[str] = None
    max_items: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxItems"), pydantic.Field(alias="maxItems")
    ] = None
    min_items: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="minItems"), pydantic.Field(alias="minItems")
    ] = None
    unique_items: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="uniqueItems"), pydantic.Field(alias="uniqueItems")
    ] = None
    max_properties: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxProperties"), pydantic.Field(alias="maxProperties")
    ] = None
    min_properties: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="minProperties"), pydantic.Field(alias="minProperties")
    ] = None
    required: typing.Optional[typing.List[str]] = None
    enum: typing.Optional[typing.List[typing.Any]] = None
    type: typing.Optional[DataType] = None
    not_: typing_extensions.Annotated[
        typing.Optional["Schema"], FieldMetadata(alias="not"), pydantic.Field(alias="not")
    ] = None
    all_of: typing_extensions.Annotated[
        typing.Optional[typing.List["Schema"]], FieldMetadata(alias="allOf"), pydantic.Field(alias="allOf")
    ] = None
    one_of: typing_extensions.Annotated[
        typing.Optional[typing.List["Schema"]], FieldMetadata(alias="oneOf"), pydantic.Field(alias="oneOf")
    ] = None
    any_of: typing_extensions.Annotated[
        typing.Optional[typing.List["Schema"]], FieldMetadata(alias="anyOf"), pydantic.Field(alias="anyOf")
    ] = None
    discriminator: typing.Optional["SchemaDiscriminator"] = None
    items: typing.Optional["SchemaItems"] = None
    properties: typing.Optional[typing.Dict[str, "Schema"]] = None
    additional_properties: typing_extensions.Annotated[
        typing.Optional["SchemaAdditionalProperties"],
        FieldMetadata(alias="additionalProperties"),
        pydantic.Field(alias="additionalProperties"),
    ] = None
    description: typing.Optional[str] = None
    format: typing.Optional[str] = None
    default: typing.Optional[typing.Any] = None
    nullable: typing.Optional[bool] = None
    read_only: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="readOnly"), pydantic.Field(alias="readOnly")
    ] = None
    write_only: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="writeOnly"), pydantic.Field(alias="writeOnly")
    ] = None
    example: typing.Optional[typing.Any] = None
    examples: typing.Optional[typing.Any] = None
    deprecated: typing.Optional[bool] = None
    content_media_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contentMediaType"), pydantic.Field(alias="contentMediaType")
    ] = None
    content_encoding: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contentEncoding"), pydantic.Field(alias="contentEncoding")
    ] = None
    content_schema: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contentSchema"), pydantic.Field(alias="contentSchema")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .schema_additional_properties import SchemaAdditionalProperties
from .schema_discriminator import SchemaDiscriminator
from .schema_items import SchemaItems

update_forward_refs(
    Schema,
    SchemaAdditionalProperties=SchemaAdditionalProperties,
    SchemaDiscriminator=SchemaDiscriminator,
    SchemaItems=SchemaItems,
)
