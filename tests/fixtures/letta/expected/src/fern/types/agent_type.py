

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentType(enum.StrEnum):
    """
    Enum to represent the type of agent.
    """

    MEMGPT_AGENT = "memgpt_agent"
    MEMGPT_V2AGENT = "memgpt_v2_agent"
    LETTA_V1AGENT = "letta_v1_agent"
    REACT_AGENT = "react_agent"
    WORKFLOW_AGENT = "workflow_agent"
    SPLIT_THREAD_AGENT = "split_thread_agent"
    SLEEPTIME_AGENT = "sleeptime_agent"
    VOICE_CONVO_AGENT = "voice_convo_agent"
    VOICE_SLEEPTIME_AGENT = "voice_sleeptime_agent"

    def visit(
        self,
        memgpt_agent: typing.Callable[[], T_Result],
        memgpt_v2agent: typing.Callable[[], T_Result],
        letta_v1agent: typing.Callable[[], T_Result],
        react_agent: typing.Callable[[], T_Result],
        workflow_agent: typing.Callable[[], T_Result],
        split_thread_agent: typing.Callable[[], T_Result],
        sleeptime_agent: typing.Callable[[], T_Result],
        voice_convo_agent: typing.Callable[[], T_Result],
        voice_sleeptime_agent: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AgentType.MEMGPT_AGENT:
            return memgpt_agent()
        if self is AgentType.MEMGPT_V2AGENT:
            return memgpt_v2agent()
        if self is AgentType.LETTA_V1AGENT:
            return letta_v1agent()
        if self is AgentType.REACT_AGENT:
            return react_agent()
        if self is AgentType.WORKFLOW_AGENT:
            return workflow_agent()
        if self is AgentType.SPLIT_THREAD_AGENT:
            return split_thread_agent()
        if self is AgentType.SLEEPTIME_AGENT:
            return sleeptime_agent()
        if self is AgentType.VOICE_CONVO_AGENT:
            return voice_convo_agent()
        if self is AgentType.VOICE_SLEEPTIME_AGENT:
            return voice_sleeptime_agent()
