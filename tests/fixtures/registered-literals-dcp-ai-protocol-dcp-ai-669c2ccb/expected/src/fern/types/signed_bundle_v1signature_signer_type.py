

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SignedBundleV1SignatureSignerType(enum.StrEnum):
    HUMAN = "human"
    ORGANIZATION = "organization"

    def visit(self, human: typing.Callable[[], T_Result], organization: typing.Callable[[], T_Result]) -> T_Result:
        if self is SignedBundleV1SignatureSignerType.HUMAN:
            return human()
        if self is SignedBundleV1SignatureSignerType.ORGANIZATION:
            return organization()
