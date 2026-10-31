

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DestinationAccountDetailsDataDestinationType(enum.StrEnum):
    """
    Data Destination Type.
    """

    STORAGE_ACCOUNT = "StorageAccount"
    MANAGED_DISK = "ManagedDisk"

    def visit(
        self, storage_account: typing.Callable[[], T_Result], managed_disk: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is DestinationAccountDetailsDataDestinationType.STORAGE_ACCOUNT:
            return storage_account()
        if self is DestinationAccountDetailsDataDestinationType.MANAGED_DISK:
            return managed_disk()
