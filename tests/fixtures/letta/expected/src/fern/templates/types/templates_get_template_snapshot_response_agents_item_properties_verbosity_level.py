

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TemplatesGetTemplateSnapshotResponseAgentsItemPropertiesVerbosityLevel(enum.StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    def visit(
        self,
        low: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TemplatesGetTemplateSnapshotResponseAgentsItemPropertiesVerbosityLevel.LOW:
            return low()
        if self is TemplatesGetTemplateSnapshotResponseAgentsItemPropertiesVerbosityLevel.MEDIUM:
            return medium()
        if self is TemplatesGetTemplateSnapshotResponseAgentsItemPropertiesVerbosityLevel.HIGH:
            return high()
