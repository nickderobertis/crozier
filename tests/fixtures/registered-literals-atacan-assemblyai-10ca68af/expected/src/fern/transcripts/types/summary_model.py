

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SummaryModel(enum.StrEnum):
    """
    The model to summarize the transcript
    """

    INFORMATIVE = "informative"
    CONVERSATIONAL = "conversational"
    CATCHY = "catchy"

    def visit(
        self,
        informative: typing.Callable[[], T_Result],
        conversational: typing.Callable[[], T_Result],
        catchy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SummaryModel.INFORMATIVE:
            return informative()
        if self is SummaryModel.CONVERSATIONAL:
            return conversational()
        if self is SummaryModel.CATCHY:
            return catchy()
