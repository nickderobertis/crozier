

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PublishTypeInputType(enum.StrEnum):
    """
    <p>The type of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
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
        if self is PublishTypeInputType.RESOURCE:
            return resource()
        if self is PublishTypeInputType.MODULE:
            return module()
        if self is PublishTypeInputType.HOOK:
            return hook()
