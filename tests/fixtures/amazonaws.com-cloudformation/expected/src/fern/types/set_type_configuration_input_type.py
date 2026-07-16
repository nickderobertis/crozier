

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SetTypeConfigurationInputType(enum.StrEnum):
    """
    <p>The type of extension.</p> <p>Conditional: You must specify <code>ConfigurationArn</code>, or <code>Type</code> and <code>TypeName</code>.</p>
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
        if self is SetTypeConfigurationInputType.RESOURCE:
            return resource()
        if self is SetTypeConfigurationInputType.MODULE:
            return module()
        if self is SetTypeConfigurationInputType.HOOK:
            return hook()
