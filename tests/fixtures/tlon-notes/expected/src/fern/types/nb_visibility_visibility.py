

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NbVisibilityVisibility(enum.StrEnum):
    PUBLIC = "public"
    PRIVATE = "private"

    def visit(self, public: typing.Callable[[], T_Result], private: typing.Callable[[], T_Result]) -> T_Result:
        if self is NbVisibilityVisibility.PUBLIC:
            return public()
        if self is NbVisibilityVisibility.PRIVATE:
            return private()
