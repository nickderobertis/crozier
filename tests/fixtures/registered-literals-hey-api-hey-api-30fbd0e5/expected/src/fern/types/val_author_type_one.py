

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ValAuthorTypeOne(enum.StrEnum):
    ORG = "org"

    def visit(self, org: typing.Callable[[], T_Result]) -> T_Result:
        if self is ValAuthorTypeOne.ORG:
            return org()
