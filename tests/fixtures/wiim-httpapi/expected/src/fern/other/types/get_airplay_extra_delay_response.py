

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetAirplayExtraDelayResponse(UniversalBaseModel):
    airplay_extra_delay: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="AirplayExtraDelay"),
        pydantic.Field(alias="AirplayExtraDelay", description="AirPlay extra delay in milliseconds"),
    ] = None
    """
    AirPlay extra delay in milliseconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
