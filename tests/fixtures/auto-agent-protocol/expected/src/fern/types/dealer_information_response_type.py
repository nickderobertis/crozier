

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DealerInformationResponseType(enum.StrEnum):
    DEALER_INFORMATION_RESPONSE = "dealer.information.response"

    def visit(self, dealer_information_response: typing.Callable[[], T_Result]) -> T_Result:
        if self is DealerInformationResponseType.DEALER_INFORMATION_RESPONSE:
            return dealer_information_response()
