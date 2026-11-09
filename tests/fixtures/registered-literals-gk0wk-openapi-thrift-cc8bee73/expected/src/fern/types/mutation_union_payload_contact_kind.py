

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MutationUnionPayloadContactKind(enum.StrEnum):
    EMAIL = "email"
    PHONE = "phone"

    def visit(self, email: typing.Callable[[], T_Result], phone: typing.Callable[[], T_Result]) -> T_Result:
        if self is MutationUnionPayloadContactKind.EMAIL:
            return email()
        if self is MutationUnionPayloadContactKind.PHONE:
            return phone()
