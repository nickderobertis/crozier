

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetListTypesRequestVisibility(enum.StrEnum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"

    def visit(self, public: typing.Callable[[], T_Result], private: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetListTypesRequestVisibility.PUBLIC:
            return public()
        if self is GetListTypesRequestVisibility.PRIVATE:
            return private()
