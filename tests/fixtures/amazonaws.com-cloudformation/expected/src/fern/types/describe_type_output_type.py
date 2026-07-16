

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DescribeTypeOutputType(str, enum.Enum):
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
        if self is DescribeTypeOutputType.RESOURCE:
            return resource()
        if self is DescribeTypeOutputType.MODULE:
            return module()
        if self is DescribeTypeOutputType.HOOK:
            return hook()
