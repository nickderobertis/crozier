

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApolloFederationConfigEnable(enum.StrEnum):
    """
    enable takes the version of apollo federation. Supported value is v1 only.
    """

    V1 = "v1"

    def visit(self, v1: typing.Callable[[], T_Result]) -> T_Result:
        if self is ApolloFederationConfigEnable.V1:
            return v1()
