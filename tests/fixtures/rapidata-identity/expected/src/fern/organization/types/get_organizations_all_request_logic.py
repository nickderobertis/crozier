

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetOrganizationsAllRequestLogic(enum.StrEnum):
    AND = "and"
    OR = "or"

    def visit(self, and_: typing.Callable[[], T_Result], or_: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetOrganizationsAllRequestLogic.AND:
            return and_()
        if self is GetOrganizationsAllRequestLogic.OR:
            return or_()
