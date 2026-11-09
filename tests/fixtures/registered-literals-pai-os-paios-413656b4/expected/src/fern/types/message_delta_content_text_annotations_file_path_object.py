

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_delta_content_text_annotations_file_path_object_file_path import (
    MessageDeltaContentTextAnnotationsFilePathObjectFilePath,
)


class MessageDeltaContentTextAnnotationsFilePathObject(UniversalBaseModel):
    """
    A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.
    """

    index: int = pydantic.Field()
    """
    The index of the annotation in the text content part.
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text in the message content that needs to be replaced.
    """

    file_path: typing.Optional[MessageDeltaContentTextAnnotationsFilePathObjectFilePath] = None
    start_index: typing.Optional[int] = None
    end_index: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
