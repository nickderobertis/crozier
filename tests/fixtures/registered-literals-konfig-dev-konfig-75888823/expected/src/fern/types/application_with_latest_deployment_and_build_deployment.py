

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .build import Build
from .deployment_v2 import DeploymentV2


class ApplicationWithLatestDeploymentAndBuildDeployment(DeploymentV2):
    build: Build

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
