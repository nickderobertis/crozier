

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .column_id import ColumnId
from .select_base import SelectBase


class CountQuartersSelect(SelectBase):
    """
    Emits the count of covered quarters encountered in the selected date column.
    """

    column: typing.Optional[ColumnId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
