

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetRegisterTypeRequestType(enum.StrEnum):
    RESOURCE = "RESOURCE"
    MODULE = "MODULE"
    HOOK = "HOOK"

    def visit(
        self,
        resource: typing.Callable[[], T_Result],
        module: typing.Callable[[], T_Result],
        hook: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetRegisterTypeRequestType.RESOURCE:
            return resource()
        if self is GetRegisterTypeRequestType.MODULE:
            return module()
        if self is GetRegisterTypeRequestType.HOOK:
            return hook()
