

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TypeConfigurationIdentifierType(enum.StrEnum):
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
        if self is TypeConfigurationIdentifierType.RESOURCE:
            return resource()
        if self is TypeConfigurationIdentifierType.MODULE:
            return module()
        if self is TypeConfigurationIdentifierType.HOOK:
            return hook()
