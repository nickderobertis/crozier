

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_delta_content_text_annotations_file_citation_object_file_citation import (
    MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation,
)
from .message_delta_content_text_annotations_file_path_object_file_path import (
    MessageDeltaContentTextAnnotationsFilePathObjectFilePath,
)


class MessageDeltaContentTextObjectTextAnnotationsItem_FileCitation(UniversalBaseModel):
    type: typing.Literal["file_citation"] = "file_citation"
    index: int
    text: typing.Optional[str] = None
    file_citation: typing.Optional[MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation] = None
    start_index: typing.Optional[int] = None
    end_index: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MessageDeltaContentTextObjectTextAnnotationsItem_FilePath(UniversalBaseModel):
    type: typing.Literal["file_path"] = "file_path"
    index: int
    text: typing.Optional[str] = None
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


MessageDeltaContentTextObjectTextAnnotationsItem = typing_extensions.Annotated[
    typing.Union[
        MessageDeltaContentTextObjectTextAnnotationsItem_FileCitation,
        MessageDeltaContentTextObjectTextAnnotationsItem_FilePath,
    ],
    pydantic.Field(discriminator="type"),
]
