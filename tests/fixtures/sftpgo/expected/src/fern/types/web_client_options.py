

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebClientOptions(enum.StrEnum):
    """
    Options:
      * `publickey-change-disabled` - changing SSH public keys is not allowed
      * `tls-cert-change-disabled` - changing TLS certificates is not allowed
      * `write-disabled` - upload, rename, delete are not allowed even if the user has permissions for these actions
      * `mfa-disabled` - enabling multi-factor authentication is not allowed. This option cannot be set if the user has MFA already enabled
      * `password-change-disabled` - changing password is not allowed
      * `api-key-auth-change-disabled` - enabling/disabling API key authentication is not allowed
      * `info-change-disabled` - changing info such as email and description is not allowed
      * `shares-disabled` - sharing files and directories with external users is not allowed
      * `password-reset-disabled` - resetting the password is not allowed
      * `shares-without-password-disabled` - creating shares without password protection is not allowed
    """

    PUBLICKEY_CHANGE_DISABLED = "publickey-change-disabled"
    TLS_CERT_CHANGE_DISABLED = "tls-cert-change-disabled"
    WRITE_DISABLED = "write-disabled"
    MFA_DISABLED = "mfa-disabled"
    PASSWORD_CHANGE_DISABLED = "password-change-disabled"
    API_KEY_AUTH_CHANGE_DISABLED = "api-key-auth-change-disabled"
    INFO_CHANGE_DISABLED = "info-change-disabled"
    SHARES_DISABLED = "shares-disabled"
    PASSWORD_RESET_DISABLED = "password-reset-disabled"
    SHARES_WITHOUT_PASSWORD_DISABLED = "shares-without-password-disabled"

    def visit(
        self,
        publickey_change_disabled: typing.Callable[[], T_Result],
        tls_cert_change_disabled: typing.Callable[[], T_Result],
        write_disabled: typing.Callable[[], T_Result],
        mfa_disabled: typing.Callable[[], T_Result],
        password_change_disabled: typing.Callable[[], T_Result],
        api_key_auth_change_disabled: typing.Callable[[], T_Result],
        info_change_disabled: typing.Callable[[], T_Result],
        shares_disabled: typing.Callable[[], T_Result],
        password_reset_disabled: typing.Callable[[], T_Result],
        shares_without_password_disabled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebClientOptions.PUBLICKEY_CHANGE_DISABLED:
            return publickey_change_disabled()
        if self is WebClientOptions.TLS_CERT_CHANGE_DISABLED:
            return tls_cert_change_disabled()
        if self is WebClientOptions.WRITE_DISABLED:
            return write_disabled()
        if self is WebClientOptions.MFA_DISABLED:
            return mfa_disabled()
        if self is WebClientOptions.PASSWORD_CHANGE_DISABLED:
            return password_change_disabled()
        if self is WebClientOptions.API_KEY_AUTH_CHANGE_DISABLED:
            return api_key_auth_change_disabled()
        if self is WebClientOptions.INFO_CHANGE_DISABLED:
            return info_change_disabled()
        if self is WebClientOptions.SHARES_DISABLED:
            return shares_disabled()
        if self is WebClientOptions.PASSWORD_RESET_DISABLED:
            return password_reset_disabled()
        if self is WebClientOptions.SHARES_WITHOUT_PASSWORD_DISABLED:
            return shares_without_password_disabled()
