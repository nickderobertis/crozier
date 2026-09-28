

from __future__ import annotations

import typing

from .table_predicate_input_any_any_item_field import TablePredicateInputAnyAnyItemField

if typing.TYPE_CHECKING:
    from .table_predicate_input import TablePredicateInput
TablePredicateInputAnyAnyItem = typing.Union["TablePredicateInput", TablePredicateInputAnyAnyItemField]
