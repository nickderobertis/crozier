

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .clear_cache_command_type import ClearCacheCommandType


class ClearCacheCommand(UniversalBaseModel):
    """
    Clear all cached data.

        Clears all cache contexts, freeing memory and disk space.
        Affects all cells using the @cache decorator.
    """

    type: ClearCacheCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
