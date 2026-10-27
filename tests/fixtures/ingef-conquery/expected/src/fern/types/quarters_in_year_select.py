

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .column_id import ColumnId
from .select_base import SelectBase


class QuartersInYearSelect(SelectBase):
    """
    Calculates the maximum number of quarters in a single year, over the entire observed period. e.g.: If an entity has events Q1-Q3 2020, and an event in Q1 2019, the result is 3.
    """

    column: typing.Optional[ColumnId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
