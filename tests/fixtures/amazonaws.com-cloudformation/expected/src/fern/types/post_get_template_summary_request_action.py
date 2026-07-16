

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostGetTemplateSummaryRequestAction(enum.StrEnum):
    GET_TEMPLATE_SUMMARY = "GetTemplateSummary"

    def visit(self, get_template_summary: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostGetTemplateSummaryRequestAction.GET_TEMPLATE_SUMMARY:
            return get_template_summary()
