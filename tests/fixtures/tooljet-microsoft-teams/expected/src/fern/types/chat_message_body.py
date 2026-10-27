

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .chat_message_body_content_type import ChatMessageBodyContentType


class ChatMessageBody(UniversalBaseModel):
    content: typing.Optional[str] = None
    content_type: typing_extensions.Annotated[
        typing.Optional[ChatMessageBodyContentType],
        FieldMetadata(alias="contentType"),
        pydantic.Field(alias="contentType"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
