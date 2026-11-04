

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RuleSetEnableAt(enum.StrEnum):
    ALL = "ALL"
    CLIENT = "CLIENT"
    GATEWAY = "GATEWAY"
    SERVER = "SERVER"
    NONE = "NONE"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        client: typing.Callable[[], T_Result],
        gateway: typing.Callable[[], T_Result],
        server: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RuleSetEnableAt.ALL:
            return all_()
        if self is RuleSetEnableAt.CLIENT:
            return client()
        if self is RuleSetEnableAt.GATEWAY:
            return gateway()
        if self is RuleSetEnableAt.SERVER:
            return server()
        if self is RuleSetEnableAt.NONE:
            return none()
