

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DenyResponseDataPersistence(enum.StrEnum):
    PERMANENT = "permanent"

    def visit(self, permanent: typing.Callable[[], T_Result]) -> T_Result:
        if self is DenyResponseDataPersistence.PERMANENT:
            return permanent()
