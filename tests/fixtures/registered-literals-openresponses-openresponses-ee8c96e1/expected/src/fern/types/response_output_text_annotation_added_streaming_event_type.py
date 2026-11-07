

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseOutputTextAnnotationAddedStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.output_text.annotation.added`.
    """

    RESPONSE_OUTPUT_TEXT_ANNOTATION_ADDED = "response.output_text.annotation.added"

    def visit(self, response_output_text_annotation_added: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseOutputTextAnnotationAddedStreamingEventType.RESPONSE_OUTPUT_TEXT_ANNOTATION_ADDED:
            return response_output_text_annotation_added()
