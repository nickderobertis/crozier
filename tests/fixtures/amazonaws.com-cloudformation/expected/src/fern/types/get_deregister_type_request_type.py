

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetDeregisterTypeRequestType(enum.StrEnum):
    RESOURCE = "RESOURCE"
    MODULE = "MODULE"
    HOOK = "HOOK"

    def visit(
        self,
        resource: typing.Callable[[], T_Result],
        module: typing.Callable[[], T_Result],
        hook: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetDeregisterTypeRequestType.RESOURCE:
            return resource()
        if self is GetDeregisterTypeRequestType.MODULE:
            return module()
        if self is GetDeregisterTypeRequestType.HOOK:
            return hook()
