

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentsImportFromRequestDedupMode(enum.StrEnum):
    """
    always-create (default) creates a new document every time. reuse-existing returns a document that already holds the same content instead of storing it twice.
    """

    ALWAYS_CREATE = "always-create"
    REUSE_EXISTING = "reuse-existing"

    def visit(
        self, always_create: typing.Callable[[], T_Result], reuse_existing: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is DocumentsImportFromRequestDedupMode.ALWAYS_CREATE:
            return always_create()
        if self is DocumentsImportFromRequestDedupMode.REUSE_EXISTING:
            return reuse_existing()
