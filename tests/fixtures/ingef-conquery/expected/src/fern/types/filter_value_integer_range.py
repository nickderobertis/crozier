

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .filter_value_base import FilterValueBase
from .filter_value_integer_range_value import FilterValueIntegerRangeValue


class FilterValueIntegerRange(FilterValueBase):
    value: typing.Optional[FilterValueIntegerRangeValue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
