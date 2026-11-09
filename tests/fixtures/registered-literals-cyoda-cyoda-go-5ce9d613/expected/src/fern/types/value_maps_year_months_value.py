

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .value_maps_year_months_value_month import ValueMapsYearMonthsValueMonth


class ValueMapsYearMonthsValue(UniversalBaseModel):
    year: typing.Optional[int] = None
    month: typing.Optional[ValueMapsYearMonthsValueMonth] = None
    month_value: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="monthValue"), pydantic.Field(alias="monthValue")
    ] = None
    leap_year: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="leapYear"), pydantic.Field(alias="leapYear")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
