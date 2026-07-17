

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ReportSummary(UniversalBaseModel):
    average_speed: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="averageSpeed"),
        pydantic.Field(alias="averageSpeed", description="in knots"),
    ] = None
    """
    in knots
    """

    device_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="deviceId"), pydantic.Field(alias="deviceId")
    ] = None
    device_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="deviceName"), pydantic.Field(alias="deviceName")
    ] = None
    distance: typing.Optional[float] = pydantic.Field(default=None)
    """
    in meters
    """

    engine_hours: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="engineHours"), pydantic.Field(alias="engineHours")
    ] = None
    max_speed: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="maxSpeed"),
        pydantic.Field(alias="maxSpeed", description="in knots"),
    ] = None
    """
    in knots
    """

    spent_fuel: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="spentFuel"),
        pydantic.Field(alias="spentFuel", description="in liters"),
    ] = None
    """
    in liters
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
