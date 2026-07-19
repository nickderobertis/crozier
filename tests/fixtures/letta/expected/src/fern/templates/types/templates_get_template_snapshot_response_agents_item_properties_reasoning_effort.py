

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TemplatesGetTemplateSnapshotResponseAgentsItemPropertiesReasoningEffort(enum.StrEnum):
    NONE = "none"
    MINIMAL = "minimal"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    XHIGH = "xhigh"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        minimal: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
        xhigh: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TemplatesGetTemplateSnapshotResponseAgentsItemPropertiesReasoningEffort.NONE:
            return none()
        if self is TemplatesGetTemplateSnapshotResponseAgentsItemPropertiesReasoningEffort.MINIMAL:
            return minimal()
        if self is TemplatesGetTemplateSnapshotResponseAgentsItemPropertiesReasoningEffort.LOW:
            return low()
        if self is TemplatesGetTemplateSnapshotResponseAgentsItemPropertiesReasoningEffort.MEDIUM:
            return medium()
        if self is TemplatesGetTemplateSnapshotResponseAgentsItemPropertiesReasoningEffort.HIGH:
            return high()
        if self is TemplatesGetTemplateSnapshotResponseAgentsItemPropertiesReasoningEffort.XHIGH:
            return xhigh()
