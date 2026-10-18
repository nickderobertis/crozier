

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApiKeyResponseOutputType(enum.StrEnum):
    LEGACY = "legacy"
    PUBLISHABLE = "publishable"
    SECRET = "secret"

    def visit(
        self,
        legacy: typing.Callable[[], T_Result],
        publishable: typing.Callable[[], T_Result],
        secret: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ApiKeyResponseOutputType.LEGACY:
            return legacy()
        if self is ApiKeyResponseOutputType.PUBLISHABLE:
            return publishable()
        if self is ApiKeyResponseOutputType.SECRET:
            return secret()
