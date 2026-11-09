

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MatchSummaryCode(enum.StrEnum):
    """
    An enum indicating the match type between data provided by user and data checked against an external data source.


    `match` indicates that the provided input data was a strong match against external data.

    `partial_match` indicates the data approximately matched against external data. For example, "Knope" vs. "Knope-Wyatt" for last name.

    `no_match` indicates that Plaid was able to perform a check against an external data source and it did not match the provided input data.

    `no_data` indicates that Plaid was unable to find external data to compare against the provided input data.

    `no_input` indicates that Plaid was unable to perform a check because no information was provided for this field by the end user.
    """

    MATCH = "match"
    PARTIAL_MATCH = "partial_match"
    NO_MATCH = "no_match"
    NO_DATA = "no_data"
    NO_INPUT = "no_input"

    def visit(
        self,
        match: typing.Callable[[], T_Result],
        partial_match: typing.Callable[[], T_Result],
        no_match: typing.Callable[[], T_Result],
        no_data: typing.Callable[[], T_Result],
        no_input: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MatchSummaryCode.MATCH:
            return match()
        if self is MatchSummaryCode.PARTIAL_MATCH:
            return partial_match()
        if self is MatchSummaryCode.NO_MATCH:
            return no_match()
        if self is MatchSummaryCode.NO_DATA:
            return no_data()
        if self is MatchSummaryCode.NO_INPUT:
            return no_input()
