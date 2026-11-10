

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_content_image_file_object_image_file import MessageContentImageFileObjectImageFile


class MessageContentImageFileObject(UniversalBaseModel):
    """
    References an image [File](/docs/api-reference/files) in the content of a message.
    """

    image_file: MessageContentImageFileObjectImageFile

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
