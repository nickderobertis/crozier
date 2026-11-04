

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .build_configuration import BuildConfiguration
from .github_url import GithubUrl
from .on_complete_action import OnCompleteAction


class CreateProviderBuildRequest(UniversalBaseModel):
    location: GithubUrl
    on_complete: typing.Optional[OnCompleteAction] = None
    build_configuration: typing.Optional[BuildConfiguration] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
