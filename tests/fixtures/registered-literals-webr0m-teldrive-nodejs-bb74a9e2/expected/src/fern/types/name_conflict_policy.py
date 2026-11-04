

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NameConflictPolicy(enum.StrEnum):
    FAIL = "fail"
    REPLACE = "replace"
    RENAME = "rename"

    def visit(
        self,
        fail: typing.Callable[[], T_Result],
        replace: typing.Callable[[], T_Result],
        rename: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NameConflictPolicy.FAIL:
            return fail()
        if self is NameConflictPolicy.REPLACE:
            return replace()
        if self is NameConflictPolicy.RENAME:
            return rename()
