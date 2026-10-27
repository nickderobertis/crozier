

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .update_chat_message_request_body_content_type import UpdateChatMessageRequestBodyContentType


class UpdateChatMessageRequestBody(UniversalBaseModel):
    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    The updated content of the message
    """

    content_type: typing_extensions.Annotated[
        typing.Optional[UpdateChatMessageRequestBodyContentType],
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
