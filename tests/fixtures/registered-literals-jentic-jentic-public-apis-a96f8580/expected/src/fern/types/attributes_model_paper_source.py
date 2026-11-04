

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AttributesModelPaperSource(enum.StrEnum):
    """
    Indicate the type of paper source used on a contract that supports both templatized and third party paper functionality. This field is required when there exists a question for selecting paper source on the template
    """

    COUNTERPARTY_PAPER = "Counterparty paper"
    OUR_PAPER = "Our paper"

    def visit(
        self, counterparty_paper: typing.Callable[[], T_Result], our_paper: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is AttributesModelPaperSource.COUNTERPARTY_PAPER:
            return counterparty_paper()
        if self is AttributesModelPaperSource.OUR_PAPER:
            return our_paper()
