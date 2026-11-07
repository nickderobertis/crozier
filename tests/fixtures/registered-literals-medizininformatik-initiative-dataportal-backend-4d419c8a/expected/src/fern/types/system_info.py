

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .build_info import BuildInfo
from .git_info import GitInfo
from .terminology import Terminology


class SystemInfo(UniversalBaseModel):
    git: typing.Optional[GitInfo] = None
    build: typing.Optional[BuildInfo] = None
    terminology: typing.Optional[Terminology] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
