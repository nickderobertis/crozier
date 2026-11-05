

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConferenceListResponseMessage(enum.StrEnum):
    """
    Response message
    """

    CONFERENCE_LIST_EXECUTED = "Conference List Executed"
    CONFERENCE_LIST_FAILED_TO_PARSE_RESULT = "Conference List Failed to parse result"

    def visit(
        self,
        conference_list_executed: typing.Callable[[], T_Result],
        conference_list_failed_to_parse_result: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConferenceListResponseMessage.CONFERENCE_LIST_EXECUTED:
            return conference_list_executed()
        if self is ConferenceListResponseMessage.CONFERENCE_LIST_FAILED_TO_PARSE_RESULT:
            return conference_list_failed_to_parse_result()
