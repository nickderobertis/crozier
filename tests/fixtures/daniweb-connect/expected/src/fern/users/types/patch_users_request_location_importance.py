

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchUsersRequestLocationImportance(enum.StrEnum):
    YES = "Yes"
    SOMEWHAT = "Somewhat"
    NO = "No"

    def visit(
        self,
        yes: typing.Callable[[], T_Result],
        somewhat: typing.Callable[[], T_Result],
        no: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatchUsersRequestLocationImportance.YES:
            return yes()
        if self is PatchUsersRequestLocationImportance.SOMEWHAT:
            return somewhat()
        if self is PatchUsersRequestLocationImportance.NO:
            return no()
