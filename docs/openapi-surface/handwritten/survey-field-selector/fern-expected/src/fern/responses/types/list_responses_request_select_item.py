

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListResponsesRequestSelectItem(enum.StrEnum):
    ANSWERS = "answers"
    KWARGS = "kwargs"
    JSON = "json"
    SELF = "self"

    def visit(
        self,
        answers: typing.Callable[[], T_Result],
        kwargs_: typing.Callable[[], T_Result],
        json: typing.Callable[[], T_Result],
        self_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListResponsesRequestSelectItem.ANSWERS:
            return answers()
        if self is ListResponsesRequestSelectItem.KWARGS:
            return kwargs_()
        if self is ListResponsesRequestSelectItem.JSON:
            return json()
        if self is ListResponsesRequestSelectItem.SELF:
            return self_()
