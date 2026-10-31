

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ShareCredentialDetailsSupportedAccessProtocolsItem(enum.StrEnum):
    SMB = "SMB"
    NFS = "NFS"

    def visit(self, smb: typing.Callable[[], T_Result], nfs: typing.Callable[[], T_Result]) -> T_Result:
        if self is ShareCredentialDetailsSupportedAccessProtocolsItem.SMB:
            return smb()
        if self is ShareCredentialDetailsSupportedAccessProtocolsItem.NFS:
            return nfs()
