

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .json_value import JsonValue


class DynamicToolUiMessagePart(UniversalBaseModel):
    tool_name: typing_extensions.Annotated[str, FieldMetadata(alias="toolName"), pydantic.Field(alias="toolName")]
    tool_call_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="toolCallId"), pydantic.Field(alias="toolCallId")
    ]
    state: str
    input: JsonValue
    output: typing.Optional[JsonValue] = None
    error_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorText"), pydantic.Field(alias="errorText")
    ] = None
    provider_executed: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="providerExecuted"), pydantic.Field(alias="providerExecuted")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
