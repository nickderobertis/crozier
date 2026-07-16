

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TypeSummaryType(str, enum.Enum):
    """
    The kind of extension.
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
        if self is TypeSummaryType.RESOURCE:
            return resource()
        if self is TypeSummaryType.MODULE:
            return module()
        if self is TypeSummaryType.HOOK:
            return hook()
