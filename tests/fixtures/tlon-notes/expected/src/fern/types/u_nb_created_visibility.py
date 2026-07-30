

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UNbCreatedVisibility(enum.StrEnum):
    PUBLIC = "public"
    PRIVATE = "private"

    def visit(self, public: typing.Callable[[], T_Result], private: typing.Callable[[], T_Result]) -> T_Result:
        if self is UNbCreatedVisibility.PUBLIC:
            return public()
        if self is UNbCreatedVisibility.PRIVATE:
            return private()
