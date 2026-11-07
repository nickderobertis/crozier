

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SystemInfoMeter(UniversalBaseModel):
    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current meter status
    """

    interface: typing.Optional[str] = pydantic.Field(default=None)
    """
    Communication interface type
    """

    protocol: typing.Optional[str] = pydantic.Field(default=None)
    """
    Communication protocol used
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
