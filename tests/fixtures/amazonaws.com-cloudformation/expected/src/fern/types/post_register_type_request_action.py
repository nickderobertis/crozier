

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostRegisterTypeRequestAction(str, enum.Enum):
    REGISTER_TYPE = "RegisterType"

    def visit(self, register_type: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostRegisterTypeRequestAction.REGISTER_TYPE:
            return register_type()
