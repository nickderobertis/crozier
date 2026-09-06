

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .config_rank_by import ConfigRankBy


class ConfigRank(UniversalBaseModel):
    by: typing.Optional[ConfigRankBy] = pydantic.Field(default=None)
    """
    Criterion to rank search results by
    """

    trending_period: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of days to consider for trending rank
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
