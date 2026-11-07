

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeviceStatus(UniversalBaseModel):
    """
    Parsed browser and operating system details for display.
    """

    browser: typing.Optional[str] = pydantic.Field(default=None)
    """
    Browser name parsed from the user agent.
    """

    os: typing.Optional[str] = pydantic.Field(default=None)
    """
    Operating system name parsed from the user agent.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
