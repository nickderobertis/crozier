

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .vin import Vin


class MaintenanceBase(UniversalBaseModel):
    """
    Expresses next Maintenance details. Such as number of days and the mileage until the next Maintenance. The value is negative if the next maintenance (day or mileage) is already passed. At least one of the following maintenance information will be provided.
    """

    vin: Vin
    days_before_maintenance: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="daysBeforeMaintenance"),
        pydantic.Field(alias="daysBeforeMaintenance"),
    ] = None
    mileage_before_maintenance: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="mileageBeforeMaintenance"),
        pydantic.Field(alias="mileageBeforeMaintenance"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
