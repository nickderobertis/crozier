

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .agent_config_mode import AgentConfigMode
from .permission_config import PermissionConfig


class AgentConfig(UniversalBaseModel):
    model: typing.Optional[str] = None
    temperature: typing.Optional[float] = None
    top_p: typing.Optional[float] = None
    prompt: typing.Optional[str] = None
    tools: typing.Optional[typing.Dict[str, bool]] = pydantic.Field(default=None)
    """
    @deprecated Use 'permission' field instead
    """

    disable: typing.Optional[bool] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of when to use the agent
    """

    mode: typing.Optional[AgentConfigMode] = None
    hidden: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Hide this subagent from the @ autocomplete menu (default: false, only applies to mode: subagent)
    """

    options: typing.Optional[typing.Dict[str, typing.Any]] = None
    color: typing.Optional[str] = pydantic.Field(default=None)
    """
    Hex color code for the agent (e.g., #FF5733)
    """

    steps: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum number of agentic iterations before forcing text-only response
    """

    max_steps: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxSteps"),
        pydantic.Field(alias="maxSteps", description="@deprecated Use 'steps' field instead."),
    ] = None
    """
    @deprecated Use 'steps' field instead.
    """

    permission: typing.Optional[PermissionConfig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
