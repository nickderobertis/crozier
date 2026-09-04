

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostClientMgmtClientRequestRequestGrantTypesItem(enum.StrEnum):
    AUTHORIZATION_CODE = "authorization_code"

    def visit(self, authorization_code: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostClientMgmtClientRequestRequestGrantTypesItem.AUTHORIZATION_CODE:
            return authorization_code()
