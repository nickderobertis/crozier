

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .score_config import ScoreConfig
from .utils_meta_response import UtilsMetaResponse


class ScoreConfigs(UniversalBaseModel):
    data: typing.List[ScoreConfig]
    meta: UtilsMetaResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
