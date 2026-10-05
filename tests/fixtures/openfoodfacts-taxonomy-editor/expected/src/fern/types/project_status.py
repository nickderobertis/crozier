

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectStatus(enum.StrEnum):
    OPEN = "OPEN"
    EXPORTED = "EXPORTED"
    LOADING = "LOADING"
    FAILED = "FAILED"

    def visit(
        self,
        open: typing.Callable[[], T_Result],
        exported: typing.Callable[[], T_Result],
        loading: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProjectStatus.OPEN:
            return open()
        if self is ProjectStatus.EXPORTED:
            return exported()
        if self is ProjectStatus.LOADING:
            return loading()
        if self is ProjectStatus.FAILED:
            return failed()
