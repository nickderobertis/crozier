

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ToolType(enum.StrEnum):
    CUSTOM = "custom"
    LETTA_CORE = "letta_core"
    LETTA_MEMORY_CORE = "letta_memory_core"
    LETTA_MULTI_AGENT_CORE = "letta_multi_agent_core"
    LETTA_SLEEPTIME_CORE = "letta_sleeptime_core"
    LETTA_VOICE_SLEEPTIME_CORE = "letta_voice_sleeptime_core"
    LETTA_BUILTIN = "letta_builtin"
    LETTA_FILES_CORE = "letta_files_core"
    EXTERNAL_LANGCHAIN = "external_langchain"
    EXTERNAL_COMPOSIO = "external_composio"
    EXTERNAL_MCP = "external_mcp"

    def visit(
        self,
        custom: typing.Callable[[], T_Result],
        letta_core: typing.Callable[[], T_Result],
        letta_memory_core: typing.Callable[[], T_Result],
        letta_multi_agent_core: typing.Callable[[], T_Result],
        letta_sleeptime_core: typing.Callable[[], T_Result],
        letta_voice_sleeptime_core: typing.Callable[[], T_Result],
        letta_builtin: typing.Callable[[], T_Result],
        letta_files_core: typing.Callable[[], T_Result],
        external_langchain: typing.Callable[[], T_Result],
        external_composio: typing.Callable[[], T_Result],
        external_mcp: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ToolType.CUSTOM:
            return custom()
        if self is ToolType.LETTA_CORE:
            return letta_core()
        if self is ToolType.LETTA_MEMORY_CORE:
            return letta_memory_core()
        if self is ToolType.LETTA_MULTI_AGENT_CORE:
            return letta_multi_agent_core()
        if self is ToolType.LETTA_SLEEPTIME_CORE:
            return letta_sleeptime_core()
        if self is ToolType.LETTA_VOICE_SLEEPTIME_CORE:
            return letta_voice_sleeptime_core()
        if self is ToolType.LETTA_BUILTIN:
            return letta_builtin()
        if self is ToolType.LETTA_FILES_CORE:
            return letta_files_core()
        if self is ToolType.EXTERNAL_LANGCHAIN:
            return external_langchain()
        if self is ToolType.EXTERNAL_COMPOSIO:
            return external_composio()
        if self is ToolType.EXTERNAL_MCP:
            return external_mcp()
