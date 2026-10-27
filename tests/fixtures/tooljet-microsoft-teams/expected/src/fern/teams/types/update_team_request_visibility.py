

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateTeamRequestVisibility(enum.StrEnum):
    PRIVATE = "private"
    PUBLIC = "public"

    def visit(self, private: typing.Callable[[], T_Result], public: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateTeamRequestVisibility.PRIVATE:
            return private()
        if self is UpdateTeamRequestVisibility.PUBLIC:
            return public()
