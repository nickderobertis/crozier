

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RetrieveAgentRequestIncludeItem(enum.StrEnum):
    AGENT_BLOCKS = "agent.blocks"
    AGENT_IDENTITIES = "agent.identities"
    AGENT_MANAGED_GROUP = "agent.managed_group"
    AGENT_PENDING_APPROVAL = "agent.pending_approval"
    AGENT_SECRETS = "agent.secrets"
    AGENT_SOURCES = "agent.sources"
    AGENT_TAGS = "agent.tags"
    AGENT_TOOLS = "agent.tools"

    def visit(
        self,
        agent_blocks: typing.Callable[[], T_Result],
        agent_identities: typing.Callable[[], T_Result],
        agent_managed_group: typing.Callable[[], T_Result],
        agent_pending_approval: typing.Callable[[], T_Result],
        agent_secrets: typing.Callable[[], T_Result],
        agent_sources: typing.Callable[[], T_Result],
        agent_tags: typing.Callable[[], T_Result],
        agent_tools: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RetrieveAgentRequestIncludeItem.AGENT_BLOCKS:
            return agent_blocks()
        if self is RetrieveAgentRequestIncludeItem.AGENT_IDENTITIES:
            return agent_identities()
        if self is RetrieveAgentRequestIncludeItem.AGENT_MANAGED_GROUP:
            return agent_managed_group()
        if self is RetrieveAgentRequestIncludeItem.AGENT_PENDING_APPROVAL:
            return agent_pending_approval()
        if self is RetrieveAgentRequestIncludeItem.AGENT_SECRETS:
            return agent_secrets()
        if self is RetrieveAgentRequestIncludeItem.AGENT_SOURCES:
            return agent_sources()
        if self is RetrieveAgentRequestIncludeItem.AGENT_TAGS:
            return agent_tags()
        if self is RetrieveAgentRequestIncludeItem.AGENT_TOOLS:
            return agent_tools()
