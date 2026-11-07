

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class WorkerToggleActiveResponseVisibility(enum.StrEnum):
    PUBLIC = "Public"
    PRIVATE = "Private"

    def visit(self, public: typing.Callable[[], T_Result], private: typing.Callable[[], T_Result]) -> T_Result:
        if self is WorkerToggleActiveResponseVisibility.PUBLIC:
            return public()
        if self is WorkerToggleActiveResponseVisibility.PRIVATE:
            return private()
