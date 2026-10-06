

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSecretRequestProvider(enum.StrEnum):
    DOTENV = "dotenv"
    ENV = "env"

    def visit(self, dotenv: typing.Callable[[], T_Result], env: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateSecretRequestProvider.DOTENV:
            return dotenv()
        if self is CreateSecretRequestProvider.ENV:
            return env()
