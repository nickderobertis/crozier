

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_content_text_annotations_file_citation_object_file_citation import (
    MessageContentTextAnnotationsFileCitationObjectFileCitation,
)
from .message_content_text_annotations_file_path_object_file_path import (
    MessageContentTextAnnotationsFilePathObjectFilePath,
)


class MessageContentTextObjectTextAnnotationsItem_FileCitation(UniversalBaseModel):
    type: typing.Literal["file_citation"] = "file_citation"
    text: str
    file_citation: MessageContentTextAnnotationsFileCitationObjectFileCitation
    start_index: int
    end_index: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MessageContentTextObjectTextAnnotationsItem_FilePath(UniversalBaseModel):
    type: typing.Literal["file_path"] = "file_path"
    text: str
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


MessageContentTextObjectTextAnnotationsItem = typing_extensions.Annotated[
    typing.Union[
        MessageContentTextObjectTextAnnotationsItem_FileCitation, MessageContentTextObjectTextAnnotationsItem_FilePath
    ],
    pydantic.Field(discriminator="type"),
]
