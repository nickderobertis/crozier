

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MessageToolResult(UniversalBaseModel):
    tool_call_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="toolCallId"), pydantic.Field(alias="toolCallId")
    ]
    content: typing.Dict[str, typing.Any]
    is_error: typing_extensions.Annotated[bool, FieldMetadata(alias="isError"), pydantic.Field(alias="isError")]
    code: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
