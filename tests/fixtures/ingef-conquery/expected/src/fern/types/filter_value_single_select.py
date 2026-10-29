

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .filter_value_base import FilterValueBase


class FilterValueSingleSelect(FilterValueBase):
    value: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
