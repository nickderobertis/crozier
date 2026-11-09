

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_content_text_annotations_file_citation_object_file_citation import (
    MessageContentTextAnnotationsFileCitationObjectFileCitation,
)


class MessageContentTextAnnotationsFileCitationObject(UniversalBaseModel):
    """
    A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "retrieval" tool to search files.
    """

    text: str = pydantic.Field()
    """
    The text in the message content that needs to be replaced.
    """

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
