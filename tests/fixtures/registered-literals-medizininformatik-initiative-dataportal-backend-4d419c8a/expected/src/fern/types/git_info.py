

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .git_info_build import GitInfoBuild
from .git_info_commit import GitInfoCommit


class GitInfo(UniversalBaseModel):
    build: typing.Optional[GitInfoBuild] = None
    commit: typing.Optional[GitInfoCommit] = None
    branch: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
