

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1ProjectEnableLabels(enum.StrEnum):
    ALL = "all"
    NONE = "none"
    CUSTOM = "custom"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1ProjectEnableLabels.ALL:
            return all_()
        if self is V1ProjectEnableLabels.NONE:
            return none()
        if self is V1ProjectEnableLabels.CUSTOM:
            return custom()
