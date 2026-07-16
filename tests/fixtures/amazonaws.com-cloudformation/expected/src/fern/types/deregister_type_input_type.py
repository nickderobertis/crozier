

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DeregisterTypeInputType(str, enum.Enum):
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
        if self is DeregisterTypeInputType.RESOURCE:
            return resource()
        if self is DeregisterTypeInputType.MODULE:
            return module()
        if self is DeregisterTypeInputType.HOOK:
            return hook()
