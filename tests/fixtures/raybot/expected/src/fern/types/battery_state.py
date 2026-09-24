

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BatteryState(UniversalBaseModel):
    current: int = pydantic.Field()
    """
    The current of the battery
    """

    temp: int = pydantic.Field()
    """
    The temperature of the battery
    """

    voltage: int = pydantic.Field()
    """
    The voltage of the battery
    """

    cell_voltages: typing_extensions.Annotated[
        typing.List[int],
        FieldMetadata(alias="cellVoltages"),
        pydantic.Field(alias="cellVoltages", description="The cell voltages of the battery"),
    ]
    """
    The cell voltages of the battery
    """

    percent: int = pydantic.Field()
    """
    The percentage of the battery
    """

    fault: int = pydantic.Field()
    """
    The fault of the battery
    """

    health: int = pydantic.Field()
    """
    The health of the battery
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The updated at time of the battery"),
    ]
    """
    The updated at time of the battery
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
