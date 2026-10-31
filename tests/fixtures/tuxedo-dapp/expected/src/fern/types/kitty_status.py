

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class KittyStatus(enum.StrEnum):
    TIRED = "tired"
    READY_TO_BREAD = "ready to bread"
    HAD_BIRTH_RECENTLY = "had birth recently"

    def visit(
        self,
        tired: typing.Callable[[], T_Result],
        ready_to_bread: typing.Callable[[], T_Result],
        had_birth_recently: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is KittyStatus.TIRED:
            return tired()
        if self is KittyStatus.READY_TO_BREAD:
            return ready_to_bread()
        if self is KittyStatus.HAD_BIRTH_RECENTLY:
            return had_birth_recently()
