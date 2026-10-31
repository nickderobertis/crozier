

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LineageRelationType(enum.StrEnum):
    MEMBER_OF = "member_of"
    SPECIALIZATION_OF = "specialization_of"
    ALTERNATE_OF = "alternate_of"

    def visit(
        self,
        member_of: typing.Callable[[], T_Result],
        specialization_of: typing.Callable[[], T_Result],
        alternate_of: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LineageRelationType.MEMBER_OF:
            return member_of()
        if self is LineageRelationType.SPECIALIZATION_OF:
            return specialization_of()
        if self is LineageRelationType.ALTERNATE_OF:
            return alternate_of()
