

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostSetTypeDefaultVersionRequestAction(enum.StrEnum):
    SET_TYPE_DEFAULT_VERSION = "SetTypeDefaultVersion"

    def visit(self, set_type_default_version: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostSetTypeDefaultVersionRequestAction.SET_TYPE_DEFAULT_VERSION:
            return set_type_default_version()
