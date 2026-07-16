

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetDeregisterTypeRequestAction(str, enum.Enum):
    DEREGISTER_TYPE = "DeregisterType"

    def visit(self, deregister_type: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDeregisterTypeRequestAction.DEREGISTER_TYPE:
            return deregister_type()
