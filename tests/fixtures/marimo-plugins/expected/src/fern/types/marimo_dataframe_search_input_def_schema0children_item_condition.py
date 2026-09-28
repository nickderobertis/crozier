

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_dataframe_search_input_def_schema0children_item_condition_column_id import (
    MarimoDataframeSearchInputDefSchema0ChildrenItemConditionColumnId,
)
from .marimo_dataframe_search_input_def_schema0children_item_condition_operator import (
    MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator,
)


class MarimoDataframeSearchInputDefSchema0ChildrenItemCondition(UniversalBaseModel):
    """
    {"direction":"row","special":"column_filter"}
    """

    column_id: MarimoDataframeSearchInputDefSchema0ChildrenItemConditionColumnId = pydantic.Field()
    """
    {"label":"Column","special":"column_id"}
    """

    operator: MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator = pydantic.Field()
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
