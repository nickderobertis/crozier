

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BodyOperationNameType(enum.StrEnum):
    GRAPHQL = "GRAPHQL"

    def visit(self, graphql: typing.Callable[[], T_Result]) -> T_Result:
        if self is BodyOperationNameType.GRAPHQL:
            return graphql()
