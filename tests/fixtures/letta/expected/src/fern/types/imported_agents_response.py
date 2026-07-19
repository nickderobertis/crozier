

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ImportedAgentsResponse(UniversalBaseModel):
    """
    Response model for imported agents
    """

    agent_ids: typing.List[str] = pydantic.Field()
    """
    List of IDs of the imported agents
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
