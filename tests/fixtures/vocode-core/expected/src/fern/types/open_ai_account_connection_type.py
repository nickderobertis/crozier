

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OpenAiAccountConnectionType(enum.StrEnum):
    ACCOUNT_CONNECTION_OPENAI = "account_connection_openai"

    def visit(self, account_connection_openai: typing.Callable[[], T_Result]) -> T_Result:
        if self is OpenAiAccountConnectionType.ACCOUNT_CONNECTION_OPENAI:
            return account_connection_openai()
