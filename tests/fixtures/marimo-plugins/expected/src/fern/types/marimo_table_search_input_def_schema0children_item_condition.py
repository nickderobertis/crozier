

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_table_search_input_def_schema0children_item_condition_column_id import (
    MarimoTableSearchInputDefSchema0ChildrenItemConditionColumnId,
)
from .marimo_table_search_input_def_schema0children_item_condition_operator import (
    MarimoTableSearchInputDefSchema0ChildrenItemConditionOperator,
)


class MarimoTableSearchInputDefSchema0ChildrenItemCondition(UniversalBaseModel):
    """
    {"direction":"row","special":"column_filter"}
    """

    column_id: MarimoTableSearchInputDefSchema0ChildrenItemConditionColumnId = pydantic.Field()
    """
    {"label":"Column","special":"column_id"}
    """

    operator: MarimoTableSearchInputDefSchema0ChildrenItemConditionOperator = pydantic.Field()
    """
    {"label":" "}
    """

    value: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    {"label":"Value"}
    """

    negate: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
