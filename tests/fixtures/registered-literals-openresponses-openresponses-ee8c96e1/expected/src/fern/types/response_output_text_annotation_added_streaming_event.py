

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_output_text_annotation_added_streaming_event_type import (
    ResponseOutputTextAnnotationAddedStreamingEventType,
)
from .url_citation_body import UrlCitationBody


class ResponseOutputTextAnnotationAddedStreamingEvent(UniversalBaseModel):
    """
    A streaming event that indicated an output text annotation was added.
    """

    type: ResponseOutputTextAnnotationAddedStreamingEventType = pydantic.Field()
    """
    The type of the event, always `response.output_text.annotation.added`.
    """

    sequence_number: int = pydantic.Field()
    """
    The sequence number of the event that was emitted.
    """

    item_id: str = pydantic.Field()
    """
    The ID of the item that was updated.
    """

    output_index: int = pydantic.Field()
    """
    The index of the output item that was updated.
    """

    content_index: int = pydantic.Field()
    """
    The index of the output text content that was updated.
    """

    annotation_index: int = pydantic.Field()
    """
    The index of the annotation that was added.
    """

    annotation: typing.Optional[UrlCitationBody] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
