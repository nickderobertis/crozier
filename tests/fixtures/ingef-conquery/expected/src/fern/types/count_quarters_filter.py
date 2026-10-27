

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .column_id import ColumnId
from .count_quarters_filter_type import CountQuartersFilterType
from .filter_base import FilterBase


class CountQuartersFilter(FilterBase):
    column: typing.Optional[ColumnId] = None
    type: typing.Optional[CountQuartersFilterType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
