

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LeadSubmitResponseType(enum.StrEnum):
    """
    AAP message type discriminator.
    """

    LEAD_SUBMIT_RESPONSE = "lead.submit.response"

    def visit(self, lead_submit_response: typing.Callable[[], T_Result]) -> T_Result:
        if self is LeadSubmitResponseType.LEAD_SUBMIT_RESPONSE:
            return lead_submit_response()
