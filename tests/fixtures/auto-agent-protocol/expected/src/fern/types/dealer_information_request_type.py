

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DealerInformationRequestType(enum.StrEnum):
    """
    AAP message type. Skill ID plus role.
    """

    DEALER_INFORMATION_REQUEST = "dealer.information.request"

    def visit(self, dealer_information_request: typing.Callable[[], T_Result]) -> T_Result:
        if self is DealerInformationRequestType.DEALER_INFORMATION_REQUEST:
            return dealer_information_request()
