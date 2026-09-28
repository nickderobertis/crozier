

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .marimo_table_search_input_def_schema0children_item_condition_column_id import (
    MarimoTableSearchInputDefSchema0ChildrenItemConditionColumnId,
)
from .marimo_table_search_input_def_schema0children_item_condition_operator import (
    MarimoTableSearchInputDefSchema0ChildrenItemConditionOperator,
)
from .marimo_table_search_input_def_schema0operator import MarimoTableSearchInputDefSchema0Operator


class MarimoTableSearchInputDefSchema0ChildrenItem_Condition(UniversalBaseModel):
    type: typing.Literal["condition"] = "condition"
    column_id: MarimoTableSearchInputDefSchema0ChildrenItemConditionColumnId
    operator: MarimoTableSearchInputDefSchema0ChildrenItemConditionOperator
    value: typing.Optional[typing.Any] = None
    negate: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MarimoTableSearchInputDefSchema0ChildrenItem_Group(UniversalBaseModel):
    type: typing.Literal["group"] = "group"
    operator: typing.Optional[MarimoTableSearchInputDefSchema0Operator] = None
    children: typing.Optional[typing.List["MarimoTableSearchInputDefSchema0ChildrenItem"]] = None
    negate: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


MarimoTableSearchInputDefSchema0ChildrenItem = typing_extensions.Annotated[
    typing.Union[
        MarimoTableSearchInputDefSchema0ChildrenItem_Condition, MarimoTableSearchInputDefSchema0ChildrenItem_Group
    ],
    pydantic.Field(discriminator="type"),
]
update_forward_refs(
    MarimoTableSearchInputDefSchema0ChildrenItem_Group,
    MarimoTableSearchInputDefSchema0ChildrenItem=MarimoTableSearchInputDefSchema0ChildrenItem,
)
