

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .quay_repo_permission import QuayRepoPermission


class QuayRobotRepository(UniversalBaseModel):
    """
    Desired permission for a robot on a single repository.
    """

    name: str = pydantic.Field()
    """
    Repository name
    """

    permission: QuayRepoPermission = pydantic.Field()
    """
    Repository role: read, write, or admin
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
