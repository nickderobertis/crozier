

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PublisherStatus(enum.StrEnum):
    VERIFIED = "VERIFIED"
    UNVERIFIED = "UNVERIFIED"

    def visit(self, verified: typing.Callable[[], T_Result], unverified: typing.Callable[[], T_Result]) -> T_Result:
        if self is PublisherStatus.VERIFIED:
            return verified()
        if self is PublisherStatus.UNVERIFIED:
            return unverified()
