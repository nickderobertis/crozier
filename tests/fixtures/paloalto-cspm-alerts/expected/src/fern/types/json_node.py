

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .json_node_node_type import JsonNodeNodeType


class JsonNode(UniversalBaseModel):
    array: typing.Optional[bool] = None
    big_decimal: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="bigDecimal"), pydantic.Field(alias="bigDecimal")
    ] = None
    big_integer: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="bigInteger"), pydantic.Field(alias="bigInteger")
    ] = None
    binary: typing.Optional[bool] = None
    boolean: typing.Optional[bool] = None
    container_node: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="containerNode"), pydantic.Field(alias="containerNode")
    ] = None
    double: typing.Optional[bool] = None
    float_: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="float"), pydantic.Field(alias="float")
    ] = None
    floating_point_number: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="floatingPointNumber"), pydantic.Field(alias="floatingPointNumber")
    ] = None
    int_: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="int"), pydantic.Field(alias="int")
    ] = None
    integral_number: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="integralNumber"), pydantic.Field(alias="integralNumber")
    ] = None
    long_: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="long"), pydantic.Field(alias="long")
    ] = None
    missing_node: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="missingNode"), pydantic.Field(alias="missingNode")
    ] = None
    node_type: typing_extensions.Annotated[
        typing.Optional[JsonNodeNodeType], FieldMetadata(alias="nodeType"), pydantic.Field(alias="nodeType")
    ] = None
    null: typing.Optional[bool] = None
    number: typing.Optional[bool] = None
    object: typing.Optional[bool] = None
    pojo: typing.Optional[bool] = None
    short: typing.Optional[bool] = None
    textual: typing.Optional[bool] = None
    value_node: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="valueNode"), pydantic.Field(alias="valueNode")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
