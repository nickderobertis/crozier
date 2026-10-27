

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .send_chat_message_request_body_content_type import SendChatMessageRequestBodyContentType


class SendChatMessageRequestBody(UniversalBaseModel):
    content: str = pydantic.Field()
    """
    The content of the message
    """

    content_type: typing_extensions.Annotated[
        typing.Optional[SendChatMessageRequestBodyContentType],
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
