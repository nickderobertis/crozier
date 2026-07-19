

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .deployment_entity import DeploymentEntity


class ListDeploymentEntitiesResponse(UniversalBaseModel):
    """
    Response model for listing deployment entities.
    """

    entities: typing.Optional[typing.List[DeploymentEntity]] = None
    total_count: int
    deployment_id: str
    message: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
