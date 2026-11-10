

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_delta_content_image_file_object_image_file import MessageDeltaContentImageFileObjectImageFile
from .message_delta_content_text_object_text import MessageDeltaContentTextObjectText


class MessageDeltaObjectDeltaContentItem_ImageFile(UniversalBaseModel):
    type: typing.Literal["image_file"] = "image_file"
    index: int
    image_file: typing.Optional[MessageDeltaContentImageFileObjectImageFile] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MessageDeltaObjectDeltaContentItem_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"
    index: int
    text: typing.Optional[MessageDeltaContentTextObjectText] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


MessageDeltaObjectDeltaContentItem = typing_extensions.Annotated[
    typing.Union[MessageDeltaObjectDeltaContentItem_ImageFile, MessageDeltaObjectDeltaContentItem_Text],
    pydantic.Field(discriminator="type"),
]
