

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetLicensesRequestKind(enum.StrEnum):
    CANDIDATE = "candidate"
    MAIN = "main"
    ALL = "all"

    def visit(
        self,
        candidate: typing.Callable[[], T_Result],
        main: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetLicensesRequestKind.CANDIDATE:
            return candidate()
        if self is GetLicensesRequestKind.MAIN:
            return main()
        if self is GetLicensesRequestKind.ALL:
            return all_()
