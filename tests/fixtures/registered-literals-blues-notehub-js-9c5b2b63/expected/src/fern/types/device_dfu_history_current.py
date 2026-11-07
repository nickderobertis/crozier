

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeviceDfuHistoryCurrent(UniversalBaseModel):
    """
    Description of the current firmware
    """

    builder: typing.Optional[str] = pydantic.Field(default=None)
    """
    Firmware author
    """

    built: typing.Optional[str] = pydantic.Field(default=None)
    """
    Firmware build date
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Firmware description
    """

    organization: typing.Optional[str] = pydantic.Field(default=None)
    """
    Firmware organization
    """

    product: typing.Optional[str] = pydantic.Field(default=None)
    """
    Firmware product
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Firmware version
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
