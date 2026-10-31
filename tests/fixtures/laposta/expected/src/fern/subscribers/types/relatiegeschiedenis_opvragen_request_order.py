

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RelatiegeschiedenisOpvragenRequestOrder(enum.StrEnum):
    DESC = "desc"
    ASC = "asc"

    def visit(self, desc: typing.Callable[[], T_Result], asc: typing.Callable[[], T_Result]) -> T_Result:
        if self is RelatiegeschiedenisOpvragenRequestOrder.DESC:
            return desc()
        if self is RelatiegeschiedenisOpvragenRequestOrder.ASC:
            return asc()
