

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .marimo_dataframe_search_input_def_schema0children_item_condition_column_id import (
    MarimoDataframeSearchInputDefSchema0ChildrenItemConditionColumnId,
)
from .marimo_dataframe_search_input_def_schema0children_item_condition_operator import (
    MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator,
)
from .marimo_dataframe_search_input_def_schema0operator import MarimoDataframeSearchInputDefSchema0Operator


class MarimoDataframeSearchInputDefSchema0ChildrenItem_Condition(UniversalBaseModel):
    type: typing.Literal["condition"] = "condition"
    column_id: MarimoDataframeSearchInputDefSchema0ChildrenItemConditionColumnId
    operator: MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator
    value: typing.Optional[typing.Any] = None
    negate: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MarimoDataframeSearchInputDefSchema0ChildrenItem_Group(UniversalBaseModel):
    type: typing.Literal["group"] = "group"
    operator: typing.Optional[MarimoDataframeSearchInputDefSchema0Operator] = None
    children: typing.Optional[typing.List["MarimoDataframeSearchInputDefSchema0ChildrenItem"]] = None
    negate: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


MarimoDataframeSearchInputDefSchema0ChildrenItem = typing_extensions.Annotated[
    typing.Union[
        MarimoDataframeSearchInputDefSchema0ChildrenItem_Condition,
        MarimoDataframeSearchInputDefSchema0ChildrenItem_Group,
    ],
    pydantic.Field(discriminator="type"),
]
update_forward_refs(
    MarimoDataframeSearchInputDefSchema0ChildrenItem_Group,
    MarimoDataframeSearchInputDefSchema0ChildrenItem=MarimoDataframeSearchInputDefSchema0ChildrenItem,
)
