

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateApiKeyBodyType(enum.StrEnum):
    PUBLISHABLE = "publishable"
    SECRET = "secret"

    def visit(self, publishable: typing.Callable[[], T_Result], secret: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateApiKeyBodyType.PUBLISHABLE:
            return publishable()
        if self is CreateApiKeyBodyType.SECRET:
            return secret()
