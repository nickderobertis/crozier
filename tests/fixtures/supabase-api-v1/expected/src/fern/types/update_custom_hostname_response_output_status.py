

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateCustomHostnameResponseOutputStatus(enum.StrEnum):
    ONE_NOT_STARTED = "1_not_started"
    TWO_INITIATED = "2_initiated"
    THREE_CHALLENGE_VERIFIED = "3_challenge_verified"
    FOUR_ORIGIN_SETUP_COMPLETED = "4_origin_setup_completed"
    FIVE_SERVICES_RECONFIGURED = "5_services_reconfigured"

    def visit(
        self,
        one_not_started: typing.Callable[[], T_Result],
        two_initiated: typing.Callable[[], T_Result],
        three_challenge_verified: typing.Callable[[], T_Result],
        four_origin_setup_completed: typing.Callable[[], T_Result],
        five_services_reconfigured: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateCustomHostnameResponseOutputStatus.ONE_NOT_STARTED:
            return one_not_started()
        if self is UpdateCustomHostnameResponseOutputStatus.TWO_INITIATED:
            return two_initiated()
        if self is UpdateCustomHostnameResponseOutputStatus.THREE_CHALLENGE_VERIFIED:
            return three_challenge_verified()
        if self is UpdateCustomHostnameResponseOutputStatus.FOUR_ORIGIN_SETUP_COMPLETED:
            return four_origin_setup_completed()
        if self is UpdateCustomHostnameResponseOutputStatus.FIVE_SERVICES_RECONFIGURED:
            return five_services_reconfigured()
