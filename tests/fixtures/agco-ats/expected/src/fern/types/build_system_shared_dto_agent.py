

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .build_system_shared_dto_agent_status import BuildSystemSharedDtoAgentStatus
from .build_system_shared_dto_step_configuration import BuildSystemSharedDtoStepConfiguration


class BuildSystemSharedDtoAgent(UniversalBaseModel):
    """
    A DTO for an IAgent
    """

    agent_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="AgentID"),
        pydantic.Field(alias="AgentID", description="The id of the Agent"),
    ] = None
    """
    The id of the Agent
    """

    keep_alive_interval: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="KeepAliveInterval"),
        pydantic.Field(alias="KeepAliveInterval", description="The 'Heartbeat Interval' used by the Build Agent."),
    ]
    """
    The 'Heartbeat Interval' used by the Build Agent.
    """

    machine_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="MachineName"),
        pydantic.Field(alias="MachineName", description="The machine name of the computer the agent is running on"),
    ]
    """
    The machine name of the computer the agent is running on
    """

    status: typing_extensions.Annotated[
        BuildSystemSharedDtoAgentStatus,
        FieldMetadata(alias="Status"),
        pydantic.Field(alias="Status", description="The agent status."),
    ]
    """
    The agent status.
    """

    step_configurations: typing_extensions.Annotated[
        typing.Optional[typing.List[BuildSystemSharedDtoStepConfiguration]],
        FieldMetadata(alias="StepConfigurations"),
        pydantic.Field(alias="StepConfigurations", description="The agent's step configurations"),
    ] = None
    """
    The agent's step configurations
    """

    user_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="UserID"), pydantic.Field(alias="UserID", description="The UserID of the Agent")
    ]
    """
    The UserID of the Agent
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
