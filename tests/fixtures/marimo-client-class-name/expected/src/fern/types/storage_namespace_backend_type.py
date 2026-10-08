

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StorageNamespaceBackendType(enum.StrEnum):
    FSSPEC = "fsspec"
    HUGGINGFACE = "huggingface"
    OBSTORE = "obstore"

    def visit(
        self,
        fsspec: typing.Callable[[], T_Result],
        huggingface: typing.Callable[[], T_Result],
        obstore: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StorageNamespaceBackendType.FSSPEC:
            return fsspec()
        if self is StorageNamespaceBackendType.HUGGINGFACE:
            return huggingface()
        if self is StorageNamespaceBackendType.OBSTORE:
            return obstore()
