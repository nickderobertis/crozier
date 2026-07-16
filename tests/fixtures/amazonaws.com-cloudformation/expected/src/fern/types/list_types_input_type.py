

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ListTypesInputType(str, enum.Enum):
    """
    The type of extension.
    """

    RESOURCE = "RESOURCE"
    MODULE = "MODULE"
    HOOK = "HOOK"

    def visit(
        self,
        resource: typing.Callable[[], T_Result],
        module: typing.Callable[[], T_Result],
        hook: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListTypesInputType.RESOURCE:
            return resource()
        if self is ListTypesInputType.MODULE:
            return module()
        if self is ListTypesInputType.HOOK:
            return hook()
