

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AgentDetail(UniversalBaseModel):
    agent_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="agentId"), pydantic.Field(alias="agentId", description="Unique agent identifier")
    ]
    """
    Unique agent identifier
    """

    display_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Human-readable agent name"),
    ]
    """
    Human-readable agent name
    """

    description: str = pydantic.Field()
    """
    Detailed description of the agent's purpose and capabilities.
    Helps users understand what the agent does before granting access.
    """

    logo_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="logoUrl"),
        pydantic.Field(alias="logoUrl", description="Optional URL to agent's logo or icon"),
    ] = None
    """
    Optional URL to agent's logo or icon
    """

    governance_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="governanceUrl"),
        pydantic.Field(
            alias="governanceUrl",
            description="Optional link to agent governance documentation.\nShould explain policies, compliance, and oversight.",
        ),
    ] = None
    """
    Optional link to agent governance documentation.
    Should explain policies, compliance, and oversight.
    """

    user_documentation_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="userDocumentationUrl"),
        pydantic.Field(
            alias="userDocumentationUrl",
            description="Optional link to user-facing documentation.\nShould explain how to use the agent and what to expect.",
        ),
    ] = None
    """
    Optional link to user-facing documentation.
    Should explain how to use the agent and what to expect.
    """

    agent_interface_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="agentInterfaceUrl"),
        pydantic.Field(
            alias="agentInterfaceUrl",
            description="Optional link to the agent's public interface or web UI.\nWhere users can interact with the agent directly.",
        ),
    ] = None
    """
    Optional link to the agent's public interface or web UI.
    Where users can interact with the agent directly.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
