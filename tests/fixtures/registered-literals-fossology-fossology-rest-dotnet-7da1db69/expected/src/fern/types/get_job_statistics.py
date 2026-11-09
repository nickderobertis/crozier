

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetJobStatistics(UniversalBaseModel):
    agent_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="agentName"),
        pydantic.Field(alias="agentName", description="Name of the agent"),
    ] = None
    """
    Name of the agent
    """

    agent_desc: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="agentDesc"),
        pydantic.Field(alias="agentDesc", description="Description of the agent"),
    ] = None
    """
    Description of the agent
    """

    fired_jobs: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="firedJobs"),
        pydantic.Field(alias="firedJobs", description="Number of fired jobs"),
    ] = None
    """
    Number of fired jobs
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
