

from __future__ import annotations

import typing

from .table_predicate_any_any_item_field import TablePredicateAnyAnyItemField

if typing.TYPE_CHECKING:
    from .table_predicate import TablePredicate
TablePredicateAnyAnyItem = typing.Union["TablePredicate", TablePredicateAnyAnyItemField]
