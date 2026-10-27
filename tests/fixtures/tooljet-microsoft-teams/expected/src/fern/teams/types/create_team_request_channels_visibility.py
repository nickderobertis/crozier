

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateTeamRequestChannelsVisibility(enum.StrEnum):
    PRIVATE = "private"
    PUBLIC = "public"

    def visit(self, private: typing.Callable[[], T_Result], public: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateTeamRequestChannelsVisibility.PRIVATE:
            return private()
        if self is CreateTeamRequestChannelsVisibility.PUBLIC:
            return public()
