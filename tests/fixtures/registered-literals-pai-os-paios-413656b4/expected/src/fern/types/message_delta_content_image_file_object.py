

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_delta_content_image_file_object_image_file import MessageDeltaContentImageFileObjectImageFile


class MessageDeltaContentImageFileObject(UniversalBaseModel):
    """
    References an image [File](/docs/api-reference/files) in the content of a message.
    """

    index: int = pydantic.Field()
    """
    The index of the content part in the message.
    """

    image_file: typing.Optional[MessageDeltaContentImageFileObjectImageFile] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
