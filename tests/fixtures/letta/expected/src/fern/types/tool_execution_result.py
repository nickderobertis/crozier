

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_state import AgentState
from .tool_execution_result_status import ToolExecutionResultStatus


class ToolExecutionResult(UniversalBaseModel):
    status: ToolExecutionResultStatus = pydantic.Field()
    """
    The status of the tool execution and return object
    """

    func_return: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    The function return object
    """

    agent_state: typing.Optional[AgentState] = pydantic.Field(default=None)
    """
    The agent state
    """

    stdout: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Captured stdout (prints, logs) from function invocation
    """

    stderr: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Captured stderr from the function invocation
    """

    sandbox_config_fingerprint: typing.Optional[str] = pydantic.Field(default=None)
    """
    The fingerprint of the config for the sandbox
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
