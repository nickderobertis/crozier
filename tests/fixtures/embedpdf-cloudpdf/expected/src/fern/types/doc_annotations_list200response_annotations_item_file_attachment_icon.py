

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemFileAttachmentIcon(enum.StrEnum):
    PUSH_PIN = "push-pin"
    PAPERCLIP = "paperclip"
    GRAPH = "graph"
    TAG = "tag"

    def visit(
        self,
        push_pin: typing.Callable[[], T_Result],
        paperclip: typing.Callable[[], T_Result],
        graph: typing.Callable[[], T_Result],
        tag: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemFileAttachmentIcon.PUSH_PIN:
            return push_pin()
        if self is DocAnnotationsList200ResponseAnnotationsItemFileAttachmentIcon.PAPERCLIP:
            return paperclip()
        if self is DocAnnotationsList200ResponseAnnotationsItemFileAttachmentIcon.GRAPH:
            return graph()
        if self is DocAnnotationsList200ResponseAnnotationsItemFileAttachmentIcon.TAG:
            return tag()
