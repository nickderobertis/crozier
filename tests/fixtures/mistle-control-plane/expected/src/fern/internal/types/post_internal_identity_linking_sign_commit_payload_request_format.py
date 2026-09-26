

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalIdentityLinkingSignCommitPayloadRequestFormat(enum.StrEnum):
    SSH = "ssh"

    def visit(self, ssh: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostInternalIdentityLinkingSignCommitPayloadRequestFormat.SSH:
            return ssh()
