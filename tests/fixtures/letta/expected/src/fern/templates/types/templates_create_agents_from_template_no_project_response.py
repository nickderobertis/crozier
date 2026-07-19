

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TemplatesCreateAgentsFromTemplateNoProjectResponse(UniversalBaseModel):
    """
    Response containing created agent IDs and associated metadata
    """

    agent_ids: typing.List[str] = pydantic.Field()
    """
    Array of created agent IDs
    """

    group_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional group ID if agents were created in a group
    """

    deployment_id: str = pydantic.Field()
    """
    The deployment ID for the created agents
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
