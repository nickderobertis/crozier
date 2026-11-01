

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .artifact import Artifact
from .media import Media


class MediaUsage(UniversalBaseModel):
    artifacts: typing.Optional[typing.List[Artifact]] = None
    id: typing.Optional[str] = None
    media: typing.Optional[Media] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
