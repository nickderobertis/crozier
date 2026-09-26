

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationInfoChallengeIndicator(enum.StrEnum):
    """
    Specifies a preference for receiving a challenge. Possible values:

    * **01**: No preference
    * **02**: No challenge requested
    * **03**: Challenge requested (preference)
    * **04**: Challenge requested (mandate)
    * **05**: No challenge requested (transactional risk analysis is already performed)
    * **07**: No challenge requested (SCA is already performed)
    * **08**: No challenge requested (trusted beneficiaries exemption of no challenge required)
    * **09**: Challenge requested (trusted beneficiaries prompt requested if challenge required)
    * **80**: No challenge requested (secure corporate payment with Mastercard)
    * **82**: No challenge requested (secure corporate payment with Visa)
    """

    ONE = "01"
    TWO = "02"
    THREE = "03"
    FOUR = "04"
    FIVE = "05"
    SEVEN = "07"
    EIGHT = "08"
    NINE = "09"
    EIGHTY = "80"
    EIGHTY_TWO = "82"

    def visit(
        self,
        one: typing.Callable[[], T_Result],
        two: typing.Callable[[], T_Result],
        three: typing.Callable[[], T_Result],
        four: typing.Callable[[], T_Result],
        five: typing.Callable[[], T_Result],
        seven: typing.Callable[[], T_Result],
        eight: typing.Callable[[], T_Result],
        nine: typing.Callable[[], T_Result],
        eighty: typing.Callable[[], T_Result],
        eighty_two: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthenticationInfoChallengeIndicator.ONE:
            return one()
        if self is AuthenticationInfoChallengeIndicator.TWO:
            return two()
        if self is AuthenticationInfoChallengeIndicator.THREE:
            return three()
        if self is AuthenticationInfoChallengeIndicator.FOUR:
            return four()
        if self is AuthenticationInfoChallengeIndicator.FIVE:
            return five()
        if self is AuthenticationInfoChallengeIndicator.SEVEN:
            return seven()
        if self is AuthenticationInfoChallengeIndicator.EIGHT:
            return eight()
        if self is AuthenticationInfoChallengeIndicator.NINE:
            return nine()
        if self is AuthenticationInfoChallengeIndicator.EIGHTY:
            return eighty()
        if self is AuthenticationInfoChallengeIndicator.EIGHTY_TWO:
            return eighty_two()
