

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .battery_relay_state import BatteryRelayState


class Battery(UniversalBaseModel):
    name: str
    relay_state: typing_extensions.Annotated[
        typing.Optional[BatteryRelayState],
        FieldMetadata(alias="relayState"),
        pydantic.Field(alias="relayState", description="The relay state, false when no relay is fitted."),
    ] = None
    """
    The relay state, false when no relay is fitted.
    """

    cell_count: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="cellCount"), pydantic.Field(alias="cellCount")
    ] = None
    voltage: typing.Optional[typing.Any] = None
    flags: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
