

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalIdentityLinkingSignCommitPayloadResponseSignatureEncoding(enum.StrEnum):
    PEM = "pem"

    def visit(self, pem: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostInternalIdentityLinkingSignCommitPayloadResponseSignatureEncoding.PEM:
            return pem()
