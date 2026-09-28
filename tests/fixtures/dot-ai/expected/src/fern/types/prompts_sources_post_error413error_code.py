

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PromptsSourcesPostError413ErrorCode(enum.StrEnum):
    PAYLOAD_TOO_LARGE = "PAYLOAD_TOO_LARGE"

    def visit(self, payload_too_large: typing.Callable[[], T_Result]) -> T_Result:
        if self is PromptsSourcesPostError413ErrorCode.PAYLOAD_TOO_LARGE:
            return payload_too_large()
