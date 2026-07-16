

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .measurement_unit_custom import MeasurementUnitCustom


class MeasurementUnit(UniversalBaseModel):
    """
    Represents a unit of measurement to use with a quantity, such as ounces
    or inches. Exactly one of the following fields are required: `custom_unit`,
    `area_unit`, `length_unit`, `volume_unit`, and `weight_unit`.
    """

    area_unit: typing.Optional[str] = pydantic.Field(default=None)
    """
    Represents a standard area unit.
    """

    custom_unit: typing.Optional[MeasurementUnitCustom] = None
    generic_unit: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reserved for API integrations that lack the ability to specify a real measurement unit
    """

    length_unit: typing.Optional[str] = pydantic.Field(default=None)
    """
    Represents a standard length unit.
    """

    time_unit: typing.Optional[str] = pydantic.Field(default=None)
    """
    Represents a standard unit of time.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Represents the type of the measurement unit.
    """

    volume_unit: typing.Optional[str] = pydantic.Field(default=None)
    """
    Represents a standard volume unit.
    """

    weight_unit: typing.Optional[str] = pydantic.Field(default=None)
    """
    Represents a standard unit of weight or mass.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
