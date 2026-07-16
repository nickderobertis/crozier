

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetRegisterTypeRequestAction(str, enum.Enum):
    REGISTER_TYPE = "RegisterType"

    def visit(self, register_type: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetRegisterTypeRequestAction.REGISTER_TYPE:
            return register_type()
