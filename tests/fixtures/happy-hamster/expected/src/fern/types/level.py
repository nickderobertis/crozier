

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .level_xp import LevelXp
from .stage import Stage


class Level(UniversalBaseModel):
    """
    level and xp of one user
    """

    stage: Stage
    level: int
    xp: LevelXp

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
