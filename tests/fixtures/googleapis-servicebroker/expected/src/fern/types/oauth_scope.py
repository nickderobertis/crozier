

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    HTTPS_WWW_GOOGLEAPIS_COM_AUTH_CLOUD_PLATFORM = "https://www.googleapis.com/auth/cloud-platform"
    """
    View and manage your data across Google Cloud Platform services
    """

    def visit(self, https_www_googleapis_com_auth_cloud_platform: typing.Callable[[], T_Result]) -> T_Result:
        if self is OauthScope.HTTPS_WWW_GOOGLEAPIS_COM_AUTH_CLOUD_PLATFORM:
            return https_www_googleapis_com_auth_cloud_platform()
