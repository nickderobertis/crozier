

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class LogListResponseDataItemBody(UniversalBaseModel):
    string_value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="stringValue"), pydantic.Field(alias="stringValue")
    ] = None
    int_value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="intValue"), pydantic.Field(alias="intValue")
    ] = None
    double_value: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="doubleValue"), pydantic.Field(alias="doubleValue")
    ] = None
    bool_value: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="boolValue"), pydantic.Field(alias="boolValue")
    ] = None
    array_value: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="arrayValue"), pydantic.Field(alias="arrayValue")
    ] = None
    kvlist_value: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="kvlistValue"), pydantic.Field(alias="kvlistValue")
    ] = None
    bytes_value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bytesValue"), pydantic.Field(alias="bytesValue")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
