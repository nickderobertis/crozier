

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .build_configuration import BuildConfiguration
from .build_state import BuildState
from .docker_image_id import DockerImageId
from .on_complete_action import OnCompleteAction
from .resolved_github_url import ResolvedGithubUrl


class ProviderBuild(UniversalBaseModel):
    id: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    status: BuildState
    source: ResolvedGithubUrl
    destination: DockerImageId
    build_configuration: typing.Optional[BuildConfiguration] = None
    provider_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the provider added or modified by this build
    """

    created_by: str
    on_complete: typing.Optional[OnCompleteAction] = None
    error_message: typing.Optional[str] = None
    provider_origin: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
