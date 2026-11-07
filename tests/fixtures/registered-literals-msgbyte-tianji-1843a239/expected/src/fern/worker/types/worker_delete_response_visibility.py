

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class WorkerDeleteResponseVisibility(enum.StrEnum):
    PUBLIC = "Public"
    PRIVATE = "Private"

    def visit(self, public: typing.Callable[[], T_Result], private: typing.Callable[[], T_Result]) -> T_Result:
        if self is WorkerDeleteResponseVisibility.PUBLIC:
            return public()
        if self is WorkerDeleteResponseVisibility.PRIVATE:
            return private()
