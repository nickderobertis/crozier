

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    HTTPS_WWW_GOOGLEAPIS_COM_AUTH_CLOUD_PLATFORM = "https://www.googleapis.com/auth/cloud-platform"
    """
    See, edit, configure, and delete your Google Cloud data and see the email address for your Google Account.
    """

    HTTPS_WWW_GOOGLEAPIS_COM_AUTH_MONITORING = "https://www.googleapis.com/auth/monitoring"
    """
    View and write monitoring data for all of your Google and third-party Cloud and API projects
    """

    HTTPS_WWW_GOOGLEAPIS_COM_AUTH_MONITORING_READ = "https://www.googleapis.com/auth/monitoring.read"
    """
    View monitoring data for all of your Google Cloud and third-party projects
    """

    HTTPS_WWW_GOOGLEAPIS_COM_AUTH_MONITORING_WRITE = "https://www.googleapis.com/auth/monitoring.write"
    """
    Publish metric data to your Google Cloud projects
    """

    def visit(
        self,
        https_www_googleapis_com_auth_cloud_platform: typing.Callable[[], T_Result],
        https_www_googleapis_com_auth_monitoring: typing.Callable[[], T_Result],
        https_www_googleapis_com_auth_monitoring_read: typing.Callable[[], T_Result],
        https_www_googleapis_com_auth_monitoring_write: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OauthScope.HTTPS_WWW_GOOGLEAPIS_COM_AUTH_CLOUD_PLATFORM:
            return https_www_googleapis_com_auth_cloud_platform()
        if self is OauthScope.HTTPS_WWW_GOOGLEAPIS_COM_AUTH_MONITORING:
            return https_www_googleapis_com_auth_monitoring()
        if self is OauthScope.HTTPS_WWW_GOOGLEAPIS_COM_AUTH_MONITORING_READ:
            return https_www_googleapis_com_auth_monitoring_read()
        if self is OauthScope.HTTPS_WWW_GOOGLEAPIS_COM_AUTH_MONITORING_WRITE:
            return https_www_googleapis_com_auth_monitoring_write()
