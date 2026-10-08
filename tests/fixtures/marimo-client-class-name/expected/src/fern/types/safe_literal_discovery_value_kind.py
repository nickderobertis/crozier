

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SafeLiteralDiscoveryValueKind(enum.StrEnum):
    SAFE_LITERAL = "safe-literal"

    def visit(self, safe_literal: typing.Callable[[], T_Result]) -> T_Result:
        if self is SafeLiteralDiscoveryValueKind.SAFE_LITERAL:
            return safe_literal()
