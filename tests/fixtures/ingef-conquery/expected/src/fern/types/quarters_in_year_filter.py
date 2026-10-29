

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .column_id import ColumnId
from .filter_base import FilterBase


class QuartersInYearFilter(FilterBase):
    """
    Filters for entities having events in a specific number of quarters. See QuartersInYearSelect for a more in depth description.
    """

    column: typing.Optional[ColumnId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
