

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChallengeInfoChallengeCancel(enum.StrEnum):
    """
    Indicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has been cancelled. Possible values:
    * **00**: Data element is absent or value has been sent back with the key `challengeCancel`.
    * **01**: Cardholder selected **Cancel**.
    * **02**: 3DS Requestor cancelled Authentication.
    * **03**: Transaction abandoned.
    * **04**: Transaction timed out at ACS — other timeouts.
    * **05**: Transaction timed out at ACS — first CReq not received by ACS.
    * **06**: Transaction error.
    * **07**: Unknown.
    * **08**: Transaction time out at SDK.
    """

    ZERO = "00"
    ONE = "01"
    TWO = "02"
    THREE = "03"
    FOUR = "04"
    FIVE = "05"
    SIX = "06"
    SEVEN = "07"
    EIGHT = "08"

    def visit(
        self,
        zero: typing.Callable[[], T_Result],
        one: typing.Callable[[], T_Result],
        two: typing.Callable[[], T_Result],
        three: typing.Callable[[], T_Result],
        four: typing.Callable[[], T_Result],
        five: typing.Callable[[], T_Result],
        six: typing.Callable[[], T_Result],
        seven: typing.Callable[[], T_Result],
        eight: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChallengeInfoChallengeCancel.ZERO:
            return zero()
        if self is ChallengeInfoChallengeCancel.ONE:
            return one()
        if self is ChallengeInfoChallengeCancel.TWO:
            return two()
        if self is ChallengeInfoChallengeCancel.THREE:
            return three()
        if self is ChallengeInfoChallengeCancel.FOUR:
            return four()
        if self is ChallengeInfoChallengeCancel.FIVE:
            return five()
        if self is ChallengeInfoChallengeCancel.SIX:
            return six()
        if self is ChallengeInfoChallengeCancel.SEVEN:
            return seven()
        if self is ChallengeInfoChallengeCancel.EIGHT:
            return eight()
