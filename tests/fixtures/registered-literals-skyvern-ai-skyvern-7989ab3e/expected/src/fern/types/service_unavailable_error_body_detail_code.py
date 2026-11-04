

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServiceUnavailableErrorBodyDetailCode(enum.StrEnum):
    DOWNLOADED_FILES_UNAVAILABLE = "downloaded_files_unavailable"

    def visit(self, downloaded_files_unavailable: typing.Callable[[], T_Result]) -> T_Result:
        if self is ServiceUnavailableErrorBodyDetailCode.DOWNLOADED_FILES_UNAVAILABLE:
            return downloaded_files_unavailable()
