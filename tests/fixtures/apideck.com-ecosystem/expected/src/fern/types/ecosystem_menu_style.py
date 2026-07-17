

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EcosystemMenuStyle(enum.StrEnum):
    LIST = "LIST"
    PILL = "PILL"
    FILTER = "FILTER"

    def visit(
        self,
        list_: typing.Callable[[], T_Result],
        pill: typing.Callable[[], T_Result],
        filter: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EcosystemMenuStyle.LIST:
            return list_()
        if self is EcosystemMenuStyle.PILL:
            return pill()
        if self is EcosystemMenuStyle.FILTER:
            return filter()
