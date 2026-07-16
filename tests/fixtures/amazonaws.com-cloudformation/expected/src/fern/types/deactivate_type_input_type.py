

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DeactivateTypeInputType(str, enum.Enum):
    """
    <p>The extension type.</p> <p>Conditional: You must specify either <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
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
        if self is DeactivateTypeInputType.RESOURCE:
            return resource()
        if self is DeactivateTypeInputType.MODULE:
            return module()
        if self is DeactivateTypeInputType.HOOK:
            return hook()
