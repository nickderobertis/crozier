

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VerificationRefreshStatus(enum.StrEnum):
    """
    The verification refresh status. One of the following:

    `"VERIFICATION_REFRESH_STATUS_USER_PRESENCE_REQUIRED"` User presence is required to refresh an income verification.
    `"VERIFICATION_REFRESH_SUCCESSFUL"` The income verification refresh was successful.
    `"VERIFICATION_REFRESH_NOT_FOUND"` No new data was found after the income verification refresh.
    """

    VERIFICATION_REFRESH_STATUS_USER_PRESENCE_REQUIRED = "VERIFICATION_REFRESH_STATUS_USER_PRESENCE_REQUIRED"
    VERIFICATION_REFRESH_SUCCESSFUL = "VERIFICATION_REFRESH_SUCCESSFUL"
    VERIFICATION_REFRESH_NOT_FOUND = "VERIFICATION_REFRESH_NOT_FOUND"

    def visit(
        self,
        verification_refresh_status_user_presence_required: typing.Callable[[], T_Result],
        verification_refresh_successful: typing.Callable[[], T_Result],
        verification_refresh_not_found: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VerificationRefreshStatus.VERIFICATION_REFRESH_STATUS_USER_PRESENCE_REQUIRED:
            return verification_refresh_status_user_presence_required()
        if self is VerificationRefreshStatus.VERIFICATION_REFRESH_SUCCESSFUL:
            return verification_refresh_successful()
        if self is VerificationRefreshStatus.VERIFICATION_REFRESH_NOT_FOUND:
            return verification_refresh_not_found()
