

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StorageNamespacesNotificationOp(enum.StrEnum):
    STORAGE_NAMESPACES = "storage-namespaces"

    def visit(self, storage_namespaces: typing.Callable[[], T_Result]) -> T_Result:
        if self is StorageNamespacesNotificationOp.STORAGE_NAMESPACES:
            return storage_namespaces()
