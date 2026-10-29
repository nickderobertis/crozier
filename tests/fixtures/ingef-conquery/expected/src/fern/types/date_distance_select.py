

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .column_id import ColumnId
from .date_distance_select_time_unit import DateDistanceSelectTimeUnit
from .select_base import SelectBase


class DateDistanceSelect(SelectBase):
    """
    Calculates the maximum distance of a date column, relative to today, or the end of the maximum of an available date restriction. Mostly used to calculate the age of an entity, with `timeUnit=YEARS`.
    """

    column: typing.Optional[ColumnId] = None
    time_unit: typing_extensions.Annotated[
        typing.Optional[DateDistanceSelectTimeUnit], FieldMetadata(alias="timeUnit"), pydantic.Field(alias="timeUnit")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
