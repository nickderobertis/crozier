

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelsModelsItemStatus(enum.StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelsModelsItemStatus.ACTIVE:
            return active()
        if self is ModelsModelsItemStatus.INACTIVE:
            return inactive()
