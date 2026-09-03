

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetIntrospectRequestTokenTypeHint(enum.StrEnum):
    ACCESS_TOKEN = "access_token"
    ID_TOKEN = "id_token"

    def visit(self, access_token: typing.Callable[[], T_Result], id_token: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetIntrospectRequestTokenTypeHint.ACCESS_TOKEN:
            return access_token()
        if self is GetIntrospectRequestTokenTypeHint.ID_TOKEN:
            return id_token()
