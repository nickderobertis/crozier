

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AppSettingsUpdateLatexCompilerBackend(enum.StrEnum):
    LOCAL = "local"
    REMOTE = "remote"

    def visit(self, local: typing.Callable[[], T_Result], remote: typing.Callable[[], T_Result]) -> T_Result:
        if self is AppSettingsUpdateLatexCompilerBackend.LOCAL:
            return local()
        if self is AppSettingsUpdateLatexCompilerBackend.REMOTE:
            return remote()
