

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RemoteStolenTrackingPeriod(UniversalBaseModel):
    """
    Modify vehicle data collection frequency through tracking timer attributes.
    """

    running: typing.Optional[int] = pydantic.Field(default=None)
    """
    Data collection frequency when vehicle is in stolen mode and ignition On
    """

    shutdown: typing.Optional[int] = pydantic.Field(default=None)
    """
    Data collection frequency when vehicle is in stolen mode and ignition Off
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
