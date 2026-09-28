

from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from .table_predicate_all import TablePredicateAll
    from .table_predicate_any import TablePredicateAny
TablePredicate = typing.Union["TablePredicateAll", "TablePredicateAny"]
