

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostApiV1PlayerReleasesUploadResponseDataChannel(enum.StrEnum):
    STABLE = "stable"
    BETA = "beta"

    def visit(self, stable: typing.Callable[[], T_Result], beta: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostApiV1PlayerReleasesUploadResponseDataChannel.STABLE:
            return stable()
        if self is PostApiV1PlayerReleasesUploadResponseDataChannel.BETA:
            return beta()
