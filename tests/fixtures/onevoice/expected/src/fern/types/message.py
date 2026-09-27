

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .message_attachment import MessageAttachment
from .message_role import MessageRole
from .message_tool_call import MessageToolCall
from .message_tool_result import MessageToolResult


class Message(UniversalBaseModel):
    id: str
    conversation_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="conversationId"), pydantic.Field(alias="conversationId")
    ]
    role: MessageRole
    content: str
    attachments: typing.Optional[typing.List[MessageAttachment]] = None
    tool_calls: typing_extensions.Annotated[
        typing.Optional[typing.List[MessageToolCall]],
        FieldMetadata(alias="toolCalls"),
        pydantic.Field(alias="toolCalls"),
    ] = None
    tool_results: typing_extensions.Annotated[
        typing.Optional[typing.List[MessageToolResult]],
        FieldMetadata(alias="toolResults"),
        pydantic.Field(alias="toolResults"),
    ] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Complete denotes a successful turn; error denotes a failed stream, including partial text. An absent legacy status is not proof of success.
    """

    error_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="errorCode"),
        pydantic.Field(
            alias="errorCode",
            description="Machine-readable stream error code; STREAM_ERROR when no upstream code is supplied.",
        ),
    ] = None
    """
    Machine-readable stream error code; STREAM_ERROR when no upstream code is supplied.
    """

    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
