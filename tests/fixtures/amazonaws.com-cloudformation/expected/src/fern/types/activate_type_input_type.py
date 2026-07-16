

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ActivateTypeInputType(str, enum.Enum):
    """
    <p>The extension type.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>
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
        if self is ActivateTypeInputType.RESOURCE:
            return resource()
        if self is ActivateTypeInputType.MODULE:
            return module()
        if self is ActivateTypeInputType.HOOK:
            return hook()
