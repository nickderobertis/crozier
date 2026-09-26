

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentsImportFromRequestMode(enum.StrEnum):
    """
    sync (default) holds the response open for the whole transfer. async answers 202 with the document pending and transfers in the background; it requires a connection source, and filesystem connections additionally require expected.sha256.
    """

    SYNC = "sync"
    ASYNC = "async"

    def visit(self, sync: typing.Callable[[], T_Result], async_: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocumentsImportFromRequestMode.SYNC:
            return sync()
        if self is DocumentsImportFromRequestMode.ASYNC:
            return async_()
