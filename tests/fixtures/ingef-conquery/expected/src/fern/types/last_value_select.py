

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .column_id import ColumnId
from .mapping_id import MappingId
from .select_base import SelectBase


class LastValueSelect(SelectBase):
    """
    Emits the last value among the specified column, by ValidityDate. If set, translates the values using the supplied mapping.
    """

    column: typing.Optional[ColumnId] = None
    mapping: typing.Optional[MappingId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
