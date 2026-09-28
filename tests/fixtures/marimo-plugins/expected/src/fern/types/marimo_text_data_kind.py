

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoTextDataKind(enum.StrEnum):
    TEXT = "text"
    PASSWORD = "password"
    EMAIL = "email"
    URL = "url"

    def visit(
        self,
        text: typing.Callable[[], T_Result],
        password: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        url: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MarimoTextDataKind.TEXT:
            return text()
        if self is MarimoTextDataKind.PASSWORD:
            return password()
        if self is MarimoTextDataKind.EMAIL:
            return email()
        if self is MarimoTextDataKind.URL:
            return url()
