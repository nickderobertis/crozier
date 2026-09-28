

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class TablePredicateInputAny(UniversalBaseModel):
    """
    Matches a row when at least one member matches.
    """

    any: typing.List["TablePredicateInputAnyAnyItem"] = pydantic.Field()
    """
    Members combined with OR. An empty group is rejected, because it would compile to no filter at all.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .table_predicate_input import TablePredicateInput
from .table_predicate_input_all import TablePredicateInputAll
from .table_predicate_input_all_all_item import TablePredicateInputAllAllItem
from .table_predicate_input_any_any_item import TablePredicateInputAnyAnyItem

update_forward_refs(
    TablePredicateInputAny,
    TablePredicateInput=TablePredicateInput,
    TablePredicateInputAll=TablePredicateInputAll,
    TablePredicateInputAllAllItem=TablePredicateInputAllAllItem,
    TablePredicateInputAnyAnyItem=TablePredicateInputAnyAnyItem,
)
