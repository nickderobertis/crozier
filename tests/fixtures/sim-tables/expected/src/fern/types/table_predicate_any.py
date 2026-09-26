

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class TablePredicateAny(UniversalBaseModel):
    """
    Matches a row when at least one member matches.
    """

    any: typing.List["TablePredicateAnyAnyItem"] = pydantic.Field()
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


from .table_predicate import TablePredicate
from .table_predicate_all import TablePredicateAll
from .table_predicate_all_all_item import TablePredicateAllAllItem
from .table_predicate_any_any_item import TablePredicateAnyAnyItem

update_forward_refs(
    TablePredicateAny,
    TablePredicate=TablePredicate,
    TablePredicateAll=TablePredicateAll,
    TablePredicateAllAllItem=TablePredicateAllAllItem,
    TablePredicateAnyAnyItem=TablePredicateAnyAnyItem,
)
