

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NamingCase(enum.StrEnum):
    HASURA_DEFAULT = "hasura-default"
    GRAPHQL_DEFAULT = "graphql-default"

    def visit(
        self, hasura_default: typing.Callable[[], T_Result], graphql_default: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is NamingCase.HASURA_DEFAULT:
            return hasura_default()
        if self is NamingCase.GRAPHQL_DEFAULT:
            return graphql_default()
