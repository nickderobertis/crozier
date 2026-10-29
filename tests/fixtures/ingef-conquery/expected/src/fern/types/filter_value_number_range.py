

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .filter_value_base import FilterValueBase
from .filter_value_number_range_value import FilterValueNumberRangeValue


class FilterValueNumberRange(FilterValueBase):
    value: typing.Optional[FilterValueNumberRangeValue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
