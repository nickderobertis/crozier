

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BaseSliceDesNetworkUlThroughput(UniversalBaseModel):
    """
    The achievable data rate in uplink for the whole network slice (and not per user).
    """

    guaranteed: typing.Optional[float] = pydantic.Field(default=None)
    """
    kbps
    """

    maximum: typing.Optional[float] = pydantic.Field(default=None)
    """
    kbps
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
