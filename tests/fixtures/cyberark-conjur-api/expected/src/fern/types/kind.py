

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Kind(enum.StrEnum):
    VARIABLE = "variable"
    POLICY = "policy"
    USER = "user"
    ROLE = "role"
    HOST = "host"
    HOST_FACTORY = "host_factory"
    GROUP = "group"
    LAYER = "layer"

    def visit(
        self,
        variable: typing.Callable[[], T_Result],
        policy: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
        role: typing.Callable[[], T_Result],
        host: typing.Callable[[], T_Result],
        host_factory: typing.Callable[[], T_Result],
        group: typing.Callable[[], T_Result],
        layer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Kind.VARIABLE:
            return variable()
        if self is Kind.POLICY:
            return policy()
        if self is Kind.USER:
            return user()
        if self is Kind.ROLE:
            return role()
        if self is Kind.HOST:
            return host()
        if self is Kind.HOST_FACTORY:
            return host_factory()
        if self is Kind.GROUP:
            return group()
        if self is Kind.LAYER:
            return layer()
