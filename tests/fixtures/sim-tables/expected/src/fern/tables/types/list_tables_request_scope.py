

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListTablesRequestScope(enum.StrEnum):
    """
    Which lifecycle set to list: `active` (default) for live tables, `archived` for tables a delete archived and a table restore can bring back. `folderPath` resolves against active folders only, so pairing it with `scope=archived` returns an empty page when the containing folder was archived too.
    """

    ACTIVE = "active"
    ARCHIVED = "archived"

    def visit(self, active: typing.Callable[[], T_Result], archived: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListTablesRequestScope.ACTIVE:
            return active()
        if self is ListTablesRequestScope.ARCHIVED:
            return archived()
