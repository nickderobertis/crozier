

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmbeddingsMigratePostError400ErrorCode(enum.StrEnum):
    BAD_REQUEST = "BAD_REQUEST"

    def visit(self, bad_request: typing.Callable[[], T_Result]) -> T_Result:
        if self is EmbeddingsMigratePostError400ErrorCode.BAD_REQUEST:
            return bad_request()
