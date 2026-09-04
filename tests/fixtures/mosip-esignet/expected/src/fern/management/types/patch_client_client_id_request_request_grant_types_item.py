

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchClientClientIdRequestRequestGrantTypesItem(enum.StrEnum):
    AUTHORIZATION_CODE = "authorization_code"

    def visit(self, authorization_code: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchClientClientIdRequestRequestGrantTypesItem.AUTHORIZATION_CODE:
            return authorization_code()
