

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LeadSubmitRequestType(enum.StrEnum):
    """
    AAP message type discriminator.
    """

    LEAD_SUBMIT_REQUEST = "lead.submit.request"

    def visit(self, lead_submit_request: typing.Callable[[], T_Result]) -> T_Result:
        if self is LeadSubmitRequestType.LEAD_SUBMIT_REQUEST:
            return lead_submit_request()
