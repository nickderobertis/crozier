

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PermittedDevice(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the device that may use the credential.
    """

    ip: typing.Optional[str] = pydantic.Field(default=None)
    """
    The IP address of the device that may use the credential.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
