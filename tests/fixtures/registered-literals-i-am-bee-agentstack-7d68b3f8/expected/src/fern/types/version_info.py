

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resolved_docker_image_id import ResolvedDockerImageId
from .resolved_github_url import ResolvedGithubUrl


class VersionInfo(UniversalBaseModel):
    docker: typing.Optional[ResolvedDockerImageId] = None
    github: typing.Optional[ResolvedGithubUrl] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
