

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StorageBackendStoreType(enum.StrEnum):
    """
    The generic Storage Backend type. Used to identify the required workflow for reading and writing media. Any `store_product` should be compatible, as much is required for basic interoperability between TAMS implementations, with their associated generic `store_type`.
    """

    HTTP_OBJECT_STORE = "http_object_store"

    def visit(self, http_object_store: typing.Callable[[], T_Result]) -> T_Result:
        if self is StorageBackendStoreType.HTTP_OBJECT_STORE:
            return http_object_store()
