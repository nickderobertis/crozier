

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .application import Application
from .application_with_latest_deployment_and_build_deployment import ApplicationWithLatestDeploymentAndBuildDeployment


class ApplicationWithLatestDeploymentAndBuild(Application):
    deployment: typing.Optional[ApplicationWithLatestDeploymentAndBuildDeployment] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
