

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .online_score_config import OnlineScoreConfig


class ProjectScoreConfig(UniversalBaseModel):
    multi_select: typing.Optional[bool] = None
    destination: typing.Optional[str] = None
    online: typing.Optional[OnlineScoreConfig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
