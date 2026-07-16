

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TypeVersionSummaryType(enum.StrEnum):
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
        if self is TypeVersionSummaryType.RESOURCE:
            return resource()
        if self is TypeVersionSummaryType.MODULE:
            return module()
        if self is TypeVersionSummaryType.HOOK:
            return hook()
