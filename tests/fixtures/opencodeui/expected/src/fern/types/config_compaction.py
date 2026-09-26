

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConfigCompaction(UniversalBaseModel):
    auto: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable automatic compaction when context is full (default: true)
    """

    prune: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable pruning of old tool outputs (default: true)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
