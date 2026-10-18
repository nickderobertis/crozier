

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemIdSix(enum.StrEnum):
    LOG_DRAIN_DEFAULT = "log_drain_default"

    def visit(self, log_drain_default: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemIdSix.LOG_DRAIN_DEFAULT:
            return log_drain_default()
