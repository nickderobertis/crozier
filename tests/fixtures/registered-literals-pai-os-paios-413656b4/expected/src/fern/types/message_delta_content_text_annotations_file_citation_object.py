

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_delta_content_text_annotations_file_citation_object_file_citation import (
    MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation,
)


class MessageDeltaContentTextAnnotationsFileCitationObject(UniversalBaseModel):
    """
    A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "retrieval" tool to search files.
    """

    index: int = pydantic.Field()
    """
    The index of the annotation in the text content part.
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text in the message content that needs to be replaced.
    """

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
