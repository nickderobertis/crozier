

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetSetTypeDefaultVersionRequestType(str, enum.Enum):
    RESOURCE = "RESOURCE"
    MODULE = "MODULE"
    HOOK = "HOOK"

    def visit(
        self,
        resource: typing.Callable[[], T_Result],
        module: typing.Callable[[], T_Result],
        hook: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetSetTypeDefaultVersionRequestType.RESOURCE:
            return resource()
        if self is GetSetTypeDefaultVersionRequestType.MODULE:
            return module()
        if self is GetSetTypeDefaultVersionRequestType.HOOK:
            return hook()
