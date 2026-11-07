

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetSchedulerOption(UniversalBaseModel):
    job_list: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="jobList"),
        pydantic.Field(alias="jobList", description="List of jobs"),
    ] = None
    """
    List of jobs
    """

    priority_list: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="priorityList"),
        pydantic.Field(alias="priorityList", description="List of priorities"),
    ] = None
    """
    List of priorities
    """

    verbose_list: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="verboseList"),
        pydantic.Field(alias="verboseList", description="List of verbose levels"),
    ] = None
    """
    List of verbose levels
    """

    agent_list: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="agentList"),
        pydantic.Field(alias="agentList", description="List of agents"),
    ] = None
    """
    List of agents
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
