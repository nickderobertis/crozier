

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SshAuthentications(enum.StrEnum):
    PUBLICKEY = "publickey"
    PASSWORD = "password"
    KEYBOARD_INTERACTIVE = "keyboard-interactive"
    PUBLICKEY_PASSWORD = "publickey+password"
    PUBLICKEY_KEYBOARD_INTERACTIVE = "publickey+keyboard-interactive"

    def visit(
        self,
        publickey: typing.Callable[[], T_Result],
        password: typing.Callable[[], T_Result],
        keyboard_interactive: typing.Callable[[], T_Result],
        publickey_password: typing.Callable[[], T_Result],
        publickey_keyboard_interactive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SshAuthentications.PUBLICKEY:
            return publickey()
        if self is SshAuthentications.PASSWORD:
            return password()
        if self is SshAuthentications.KEYBOARD_INTERACTIVE:
            return keyboard_interactive()
        if self is SshAuthentications.PUBLICKEY_PASSWORD:
            return publickey_password()
        if self is SshAuthentications.PUBLICKEY_KEYBOARD_INTERACTIVE:
            return publickey_keyboard_interactive()
