

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UsageStatisticsPromptTokenDetails(UniversalBaseModel):
    cached_tokens: typing.Optional[int] = None
    cache_read_tokens: typing.Optional[int] = None
    cache_creation_tokens: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
