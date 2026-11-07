

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetSystemInfoResponseDevice(UniversalBaseModel):
    name: typing.Optional[str] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique device ID
    """

    model: typing.Optional[str] = None
    firmware: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device firmware version
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
