

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .column_id import ColumnId
from .date_distance_filter_time_unit import DateDistanceFilterTimeUnit
from .filter_base import FilterBase


class DateDistanceFilter(FilterBase):
    """
    Filters events to be within a certain time period, relative to today in a predefined unit, or the last day of an available DateRestriction. Usually used to filter for the age of entities, by setting `timeUnit=YEARS`.
    """

    column: typing.Optional[ColumnId] = None
    time_unit: typing_extensions.Annotated[
        typing.Optional[DateDistanceFilterTimeUnit], FieldMetadata(alias="timeUnit"), pydantic.Field(alias="timeUnit")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
