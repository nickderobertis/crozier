

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeleteDeploymentResponse(UniversalBaseModel):
    """
    Response model for delete deployment operation.
    """

    deleted_blocks: typing.Optional[typing.List[str]] = None
    deleted_agents: typing.Optional[typing.List[str]] = None
    deleted_groups: typing.Optional[typing.List[str]] = None
    message: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
