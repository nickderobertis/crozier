

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteServersFromStrataMcpServerStrataStrataIdServersDeleteRequestServersItemOne(enum.StrEnum):
    ALL = "ALL"

    def visit(self, all_: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeleteServersFromStrataMcpServerStrataStrataIdServersDeleteRequestServersItemOne.ALL:
            return all_()
