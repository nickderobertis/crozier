

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class TablePredicateInputAll(UniversalBaseModel):
    """
    Matches a row when every member matches.
    """

    all_: typing_extensions.Annotated[
        typing.List["TablePredicateInputAllAllItem"],
        FieldMetadata(alias="all"),
        pydantic.Field(
            alias="all",
            description="Members combined with AND. An empty group is rejected, because it would compile to no filter at all.",
        ),
    ]
    """
    Members combined with AND. An empty group is rejected, because it would compile to no filter at all.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .table_predicate_input import TablePredicateInput
from .table_predicate_input_all_all_item import TablePredicateInputAllAllItem
from .table_predicate_input_any import TablePredicateInputAny
from .table_predicate_input_any_any_item import TablePredicateInputAnyAnyItem

update_forward_refs(
    TablePredicateInputAll,
    TablePredicateInput=TablePredicateInput,
    TablePredicateInputAllAllItem=TablePredicateInputAllAllItem,
    TablePredicateInputAny=TablePredicateInputAny,
    TablePredicateInputAnyAnyItem=TablePredicateInputAnyAnyItem,
)
