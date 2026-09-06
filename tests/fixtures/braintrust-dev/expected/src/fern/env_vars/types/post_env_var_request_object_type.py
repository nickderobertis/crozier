

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostEnvVarRequestObjectType(enum.StrEnum):
    """
    The type of the object the environment variable is scoped for
    """

    ORGANIZATION = "organization"
    PROJECT = "project"
    FUNCTION = "function"

    def visit(
        self,
        organization: typing.Callable[[], T_Result],
        project: typing.Callable[[], T_Result],
        function: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostEnvVarRequestObjectType.ORGANIZATION:
            return organization()
        if self is PostEnvVarRequestObjectType.PROJECT:
            return project()
        if self is PostEnvVarRequestObjectType.FUNCTION:
            return function()
