

from __future__ import annotations

import typing

from .table_predicate_input_field import TablePredicateInputField

if typing.TYPE_CHECKING:
    from .table_predicate_input_all import TablePredicateInputAll
    from .table_predicate_input_any import TablePredicateInputAny
TablePredicateInput = typing.Union["TablePredicateInputAll", "TablePredicateInputAny", TablePredicateInputField]
