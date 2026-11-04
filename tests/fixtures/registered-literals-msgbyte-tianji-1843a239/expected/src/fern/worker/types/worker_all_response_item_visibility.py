

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class WorkerAllResponseItemVisibility(enum.StrEnum):
    PUBLIC = "Public"
    PRIVATE = "Private"

    def visit(self, public: typing.Callable[[], T_Result], private: typing.Callable[[], T_Result]) -> T_Result:
        if self is WorkerAllResponseItemVisibility.PUBLIC:
            return public()
        if self is WorkerAllResponseItemVisibility.PRIVATE:
            return private()
