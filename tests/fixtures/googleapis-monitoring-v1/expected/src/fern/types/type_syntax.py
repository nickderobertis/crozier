

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TypeSyntax(enum.StrEnum):
    """
    The source syntax.
    """

    SYNTAX_PROTO2 = "SYNTAX_PROTO2"
    SYNTAX_PROTO3 = "SYNTAX_PROTO3"
    SYNTAX_EDITIONS = "SYNTAX_EDITIONS"

    def visit(
        self,
        syntax_proto2: typing.Callable[[], T_Result],
        syntax_proto3: typing.Callable[[], T_Result],
        syntax_editions: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TypeSyntax.SYNTAX_PROTO2:
            return syntax_proto2()
        if self is TypeSyntax.SYNTAX_PROTO3:
            return syntax_proto3()
        if self is TypeSyntax.SYNTAX_EDITIONS:
            return syntax_editions()
