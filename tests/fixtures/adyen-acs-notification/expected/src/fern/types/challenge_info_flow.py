

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChallengeInfoFlow(enum.StrEnum):
    """
    The flow used in the challenge. Possible values:

    * **PWD_OTP_PHONE_FL**: one-time password (OTP) flow via SMS
    * **PWD_OTP_EMAIL_FL**: one-time password (OTP) flow via email
    * **OOB_TRIGGER_FL**: out-of-band (OOB) flow
    """

    PWD_OTP_PHONE_FL = "PWD_OTP_PHONE_FL"
    PWD_OTP_EMAIL_FL = "PWD_OTP_EMAIL_FL"
    OOB_TRIGGER_FL = "OOB_TRIGGER_FL"

    def visit(
        self,
        pwd_otp_phone_fl: typing.Callable[[], T_Result],
        pwd_otp_email_fl: typing.Callable[[], T_Result],
        oob_trigger_fl: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChallengeInfoFlow.PWD_OTP_PHONE_FL:
            return pwd_otp_phone_fl()
        if self is ChallengeInfoFlow.PWD_OTP_EMAIL_FL:
            return pwd_otp_email_fl()
        if self is ChallengeInfoFlow.OOB_TRIGGER_FL:
            return oob_trigger_fl()
