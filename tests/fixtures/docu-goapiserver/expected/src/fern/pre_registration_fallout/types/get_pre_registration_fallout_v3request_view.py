

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetPreRegistrationFalloutV3RequestView(enum.StrEnum):
    STUDENTS = "students"

    def visit(self, students: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetPreRegistrationFalloutV3RequestView.STUDENTS:
            return students()
