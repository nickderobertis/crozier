

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tide_grid_item_item_value_trend import TideGridItemItemValueTrend


class TideGridItemItemValue(UniversalBaseModel):
    height: typing.Optional[float] = None
    trend: typing.Optional[TideGridItemItemValueTrend] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
