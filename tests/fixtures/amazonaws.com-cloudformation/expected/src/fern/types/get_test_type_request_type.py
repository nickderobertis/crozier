

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetTestTypeRequestType(str, enum.Enum):
    RESOURCE = "RESOURCE"
    MODULE = "MODULE"
    HOOK = "HOOK"

    def visit(
        self,
        resource: typing.Callable[[], T_Result],
        module: typing.Callable[[], T_Result],
        hook: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetTestTypeRequestType.RESOURCE:
            return resource()
        if self is GetTestTypeRequestType.MODULE:
            return module()
        if self is GetTestTypeRequestType.HOOK:
            return hook()
