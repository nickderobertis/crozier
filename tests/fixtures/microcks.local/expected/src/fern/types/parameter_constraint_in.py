

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ParameterConstraintIn(str, enum.Enum):
    """
    Parameter location
    """

    PATH = "path"
    QUERY = "query"
    HEADER = "header"

    def visit(
        self,
        path: typing.Callable[[], T_Result],
        query: typing.Callable[[], T_Result],
        header: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ParameterConstraintIn.PATH:
            return path()
        if self is ParameterConstraintIn.QUERY:
            return query()
        if self is ParameterConstraintIn.HEADER:
            return header()
