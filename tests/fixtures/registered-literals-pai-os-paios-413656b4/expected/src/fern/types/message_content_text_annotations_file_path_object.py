

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_content_text_annotations_file_path_object_file_path import (
    MessageContentTextAnnotationsFilePathObjectFilePath,
)


class MessageContentTextAnnotationsFilePathObject(UniversalBaseModel):
    """
    A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.
    """

    text: str = pydantic.Field()
    """
    The text in the message content that needs to be replaced.
    """

    file_path: MessageContentTextAnnotationsFilePathObjectFilePath
    start_index: int
    end_index: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
