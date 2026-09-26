

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentIcon(enum.StrEnum):
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
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentIcon.PUSH_PIN:
            return push_pin()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentIcon.PAPERCLIP:
            return paperclip()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentIcon.GRAPH:
            return graph()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentIcon.TAG:
            return tag()
