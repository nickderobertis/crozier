

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_cache_info_command_type import GetCacheInfoCommandType


class GetCacheInfoCommand(UniversalBaseModel):
    """
    Retrieve cache statistics.

        Collects cache usage info across all contexts (hit/miss rates, time saved, disk usage).
    """

    type: GetCacheInfoCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
