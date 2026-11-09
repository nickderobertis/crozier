

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WeakAliasDetermination(enum.StrEnum):
    """
    Names that are explicitly marked as low quality either by their `source` list, or by `plaid` by a series of additional checks done by Plaid. Plaid does not ever surface a hit as a result of a weak name alone. If a name has no quality issues, this value will be `none`.
    """

    NONE = "none"
    SOURCE = "source"
    PLAID = "plaid"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        source: typing.Callable[[], T_Result],
        plaid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WeakAliasDetermination.NONE:
            return none()
        if self is WeakAliasDetermination.SOURCE:
            return source()
        if self is WeakAliasDetermination.PLAID:
            return plaid()
