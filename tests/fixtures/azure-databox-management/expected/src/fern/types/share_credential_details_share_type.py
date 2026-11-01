

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ShareCredentialDetailsShareType(enum.StrEnum):
    """
    Type of the share.
    """

    UNKNOWN_TYPE = "UnknownType"
    HCS = "HCS"
    BLOCK_BLOB = "BlockBlob"
    PAGE_BLOB = "PageBlob"
    AZURE_FILE = "AzureFile"
    MANAGED_DISK = "ManagedDisk"

    def visit(
        self,
        unknown_type: typing.Callable[[], T_Result],
        hcs: typing.Callable[[], T_Result],
        block_blob: typing.Callable[[], T_Result],
        page_blob: typing.Callable[[], T_Result],
        azure_file: typing.Callable[[], T_Result],
        managed_disk: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ShareCredentialDetailsShareType.UNKNOWN_TYPE:
            return unknown_type()
        if self is ShareCredentialDetailsShareType.HCS:
            return hcs()
        if self is ShareCredentialDetailsShareType.BLOCK_BLOB:
            return block_blob()
        if self is ShareCredentialDetailsShareType.PAGE_BLOB:
            return page_blob()
        if self is ShareCredentialDetailsShareType.AZURE_FILE:
            return azure_file()
        if self is ShareCredentialDetailsShareType.MANAGED_DISK:
            return managed_disk()
