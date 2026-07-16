

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetSetTypeDefaultVersionRequestAction(str, enum.Enum):
    SET_TYPE_DEFAULT_VERSION = "SetTypeDefaultVersion"

    def visit(self, set_type_default_version: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetSetTypeDefaultVersionRequestAction.SET_TYPE_DEFAULT_VERSION:
            return set_type_default_version()
