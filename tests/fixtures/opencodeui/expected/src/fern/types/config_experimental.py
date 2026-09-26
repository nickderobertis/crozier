

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ConfigExperimental(UniversalBaseModel):
    disable_paste_summary: typing.Optional[bool] = None
    batch_tool: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable the batch tool
    """

    open_telemetry: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="openTelemetry"),
        pydantic.Field(
            alias="openTelemetry",
            description="Enable OpenTelemetry spans for AI SDK calls (using the 'experimental_telemetry' flag)",
        ),
    ] = None
    """
    Enable OpenTelemetry spans for AI SDK calls (using the 'experimental_telemetry' flag)
    """

    primary_tools: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Tools that should only be available to primary agents.
    """

    continue_loop_on_deny: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Continue the agent loop when a tool call is denied
    """

    mcp_timeout: typing.Optional[int] = pydantic.Field(default=None)
    """
    Timeout in milliseconds for model context protocol (MCP) requests
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
