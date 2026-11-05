

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConferenceListMembersResponseMessage(enum.StrEnum):
    """
    Response message
    """

    CONFERENCE_LIST_MEMBERS_EXECUTED = "Conference ListMembers Executed"
    CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT = "ConferenceName Parameter must be present"
    CONFERENCE_LIST_MEMBERS_FAILED_TO_PARSE_RESULT = "Conference ListMembers Failed to parse result"
    CONFERENCE_LIST_MEMBERS_FAILED_CONFERENCE_NOT_FOUND = "Conference ListMembers Failed -- Conference not found"

    def visit(
        self,
        conference_list_members_executed: typing.Callable[[], T_Result],
        conference_name_parameter_must_be_present: typing.Callable[[], T_Result],
        conference_list_members_failed_to_parse_result: typing.Callable[[], T_Result],
        conference_list_members_failed_conference_not_found: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConferenceListMembersResponseMessage.CONFERENCE_LIST_MEMBERS_EXECUTED:
            return conference_list_members_executed()
        if self is ConferenceListMembersResponseMessage.CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT:
            return conference_name_parameter_must_be_present()
        if self is ConferenceListMembersResponseMessage.CONFERENCE_LIST_MEMBERS_FAILED_TO_PARSE_RESULT:
            return conference_list_members_failed_to_parse_result()
        if self is ConferenceListMembersResponseMessage.CONFERENCE_LIST_MEMBERS_FAILED_CONFERENCE_NOT_FOUND:
            return conference_list_members_failed_conference_not_found()
