

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoginMethods(enum.StrEnum):
    """
    Available login methods. To enable multi-step authentication you have to allow only multi-step login methods
      * `publickey`
      * `password`, password for all the supported protocols
      * `password-over-SSH`, password over SSH protocol (SSH/SFTP/SCP)
      * `keyboard-interactive`
      * `publickey+password` - multi-step auth: public key and password
      * `publickey+keyboard-interactive` - multi-step auth: public key and keyboard interactive
      * `TLSCertificate`
      * `TLSCertificate+password` - multi-step auth: TLS client certificate and password
    """

    PUBLICKEY = "publickey"
    PASSWORD = "password"
    PASSWORD_OVER_SSH = "password-over-SSH"
    KEYBOARD_INTERACTIVE = "keyboard-interactive"
    PUBLICKEY_PASSWORD = "publickey+password"
    PUBLICKEY_KEYBOARD_INTERACTIVE = "publickey+keyboard-interactive"
    TLS_CERTIFICATE = "TLSCertificate"
    TLS_CERTIFICATE_PASSWORD = "TLSCertificate+password"

    def visit(
        self,
        publickey: typing.Callable[[], T_Result],
        password: typing.Callable[[], T_Result],
        password_over_ssh: typing.Callable[[], T_Result],
        keyboard_interactive: typing.Callable[[], T_Result],
        publickey_password: typing.Callable[[], T_Result],
        publickey_keyboard_interactive: typing.Callable[[], T_Result],
        tls_certificate: typing.Callable[[], T_Result],
        tls_certificate_password: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoginMethods.PUBLICKEY:
            return publickey()
        if self is LoginMethods.PASSWORD:
            return password()
        if self is LoginMethods.PASSWORD_OVER_SSH:
            return password_over_ssh()
        if self is LoginMethods.KEYBOARD_INTERACTIVE:
            return keyboard_interactive()
        if self is LoginMethods.PUBLICKEY_PASSWORD:
            return publickey_password()
        if self is LoginMethods.PUBLICKEY_KEYBOARD_INTERACTIVE:
            return publickey_keyboard_interactive()
        if self is LoginMethods.TLS_CERTIFICATE:
            return tls_certificate()
        if self is LoginMethods.TLS_CERTIFICATE_PASSWORD:
            return tls_certificate_password()
