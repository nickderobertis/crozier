

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetListTypesRequestType(str, enum.Enum):
    RESOURCE = "RESOURCE"
    MODULE = "MODULE"
    HOOK = "HOOK"

    def visit(
        self,
        resource: typing.Callable[[], T_Result],
        module: typing.Callable[[], T_Result],
        hook: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetListTypesRequestType.RESOURCE:
            return resource()
        if self is GetListTypesRequestType.MODULE:
            return module()
        if self is GetListTypesRequestType.HOOK:
            return hook()
