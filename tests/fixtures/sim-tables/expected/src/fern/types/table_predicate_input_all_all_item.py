

from __future__ import annotations

import typing

from .table_predicate_input_all_all_item_field import TablePredicateInputAllAllItemField

if typing.TYPE_CHECKING:
    from .table_predicate_input import TablePredicateInput
TablePredicateInputAllAllItem = typing.Union["TablePredicateInput", TablePredicateInputAllAllItemField]
