

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .measurement_unit import MeasurementUnit


class StandardUnitDescription(UniversalBaseModel):
    """
    Contains the name and abbreviation for standard measurement unit.
    """

    abbreviation: typing.Optional[str] = pydantic.Field(default=None)
    """
    UI display abbreviation for the measurement unit. For example, 'lb'.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    UI display name of the measurement unit. For example, 'Pound'.
    """

    unit: typing.Optional[MeasurementUnit] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
