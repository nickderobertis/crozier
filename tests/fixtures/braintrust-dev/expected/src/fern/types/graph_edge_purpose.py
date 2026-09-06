

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GraphEdgePurpose(enum.StrEnum):
    """
    The purpose of the edge
    """

    CONTROL = "control"
    DATA = "data"
    MESSAGES = "messages"

    def visit(
        self,
        control: typing.Callable[[], T_Result],
        data: typing.Callable[[], T_Result],
        messages: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GraphEdgePurpose.CONTROL:
            return control()
        if self is GraphEdgePurpose.DATA:
            return data()
        if self is GraphEdgePurpose.MESSAGES:
            return messages()
