

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_content_image_file_object_image_file import MessageContentImageFileObjectImageFile
from .message_content_text_object_text import MessageContentTextObjectText


class MessageObjectContentItem_ImageFile(UniversalBaseModel):
    type: typing.Literal["image_file"] = "image_file"
    image_file: MessageContentImageFileObjectImageFile

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MessageObjectContentItem_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"
    text: MessageContentTextObjectText

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


MessageObjectContentItem = typing_extensions.Annotated[
    typing.Union[MessageObjectContentItem_ImageFile, MessageObjectContentItem_Text],
    pydantic.Field(discriminator="type"),
]
