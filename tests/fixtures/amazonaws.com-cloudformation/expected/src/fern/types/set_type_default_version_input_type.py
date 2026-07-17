

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SetTypeDefaultVersionInputType(enum.StrEnum):
    """
    <p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
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
        if self is SetTypeDefaultVersionInputType.RESOURCE:
            return resource()
        if self is SetTypeDefaultVersionInputType.MODULE:
            return module()
        if self is SetTypeDefaultVersionInputType.HOOK:
            return hook()
