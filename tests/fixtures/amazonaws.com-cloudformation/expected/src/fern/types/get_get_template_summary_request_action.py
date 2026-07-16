

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetGetTemplateSummaryRequestAction(str, enum.Enum):
    GET_TEMPLATE_SUMMARY = "GetTemplateSummary"

    def visit(self, get_template_summary: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetGetTemplateSummaryRequestAction.GET_TEMPLATE_SUMMARY:
            return get_template_summary()
