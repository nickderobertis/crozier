

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Visibility(enum.StrEnum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"

    def visit(self, public: typing.Callable[[], T_Result], private: typing.Callable[[], T_Result]) -> T_Result:
        if self is Visibility.PUBLIC:
            return public()
        if self is Visibility.PRIVATE:
            return private()
