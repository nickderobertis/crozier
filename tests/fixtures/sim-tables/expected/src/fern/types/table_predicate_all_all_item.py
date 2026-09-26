

from __future__ import annotations

import typing

from .table_predicate_all_all_item_field import TablePredicateAllAllItemField

if typing.TYPE_CHECKING:
    from .table_predicate import TablePredicate
TablePredicateAllAllItem = typing.Union["TablePredicate", TablePredicateAllAllItemField]
