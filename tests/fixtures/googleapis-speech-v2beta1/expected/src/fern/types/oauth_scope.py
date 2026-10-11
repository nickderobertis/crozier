

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    HTTPS_WWW_GOOGLEAPIS_COM_AUTH_CLOUD_PLATFORM = "https://www.googleapis.com/auth/cloud-platform"
    """
    See, edit, configure, and delete your Google Cloud data and see the email address for your Google Account.
    """

    def visit(self, https_www_googleapis_com_auth_cloud_platform: typing.Callable[[], T_Result]) -> T_Result:
        if self is OauthScope.HTTPS_WWW_GOOGLEAPIS_COM_AUTH_CLOUD_PLATFORM:
            return https_www_googleapis_com_auth_cloud_platform()
