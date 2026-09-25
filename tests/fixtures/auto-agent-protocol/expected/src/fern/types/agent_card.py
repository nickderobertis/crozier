

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .agent_card_capabilities import AgentCardCapabilities
from .agent_card_provider import AgentCardProvider
from .agent_card_supported_interfaces_item import AgentCardSupportedInterfacesItem


class AgentCard(UniversalBaseModel):
    """
    A2A v1.0 AgentCard carrying the AAP automotive-retail extension. Published at /.well-known/agent-card.json on a dealer-controlled domain. A2A v1.0 declares every transport in 'supportedInterfaces[]' (it replaced the earlier top-level 'url'/'preferredTransport'/'additionalInterfaces' and top-level 'protocolVersion'). To be a compliant AAP dealer agent, 'capabilities.extensions' MUST include an entry whose 'uri' equals 'https://autoagentprotocol.org/extensions/a2a-automotive-retail/v1.0'.
    """

    name: str = pydantic.Field()
    """
    Human-readable agent name.
    """

    description: str = pydantic.Field()
    """
    Short description of what this agent does.
    """

    supported_interfaces: typing_extensions.Annotated[
        typing.List[AgentCardSupportedInterfacesItem],
        FieldMetadata(alias="supportedInterfaces"),
        pydantic.Field(
            alias="supportedInterfaces",
            description="The A2A v1.0 service interfaces (transport + endpoint). AAP keeps the transport surface minimal: a JSONRPC interface is REQUIRED (every AAP client can rely on it); an HTTP+JSON interface MAY be added; gRPC is out of scope.",
        ),
    ]
    """
    The A2A v1.0 service interfaces (transport + endpoint). AAP keeps the transport surface minimal: a JSONRPC interface is REQUIRED (every AAP client can rely on it); an HTTP+JSON interface MAY be added; gRPC is out of scope.
    """

    provider: typing.Optional[AgentCardProvider] = pydantic.Field(default=None)
    """
    Organization operating the agent.
    """

    version: str = pydantic.Field()
    """
    Agent document version string (semver recommended).
    """

    documentation_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="documentationUrl"),
        pydantic.Field(
            alias="documentationUrl",
            description="URL to human-readable documentation describing this agent's behavior.",
        ),
    ] = None
    """
    URL to human-readable documentation describing this agent's behavior.
    """

    capabilities: AgentCardCapabilities = pydantic.Field()
    """
    A2A capability flags and extensions.
    """

    default_input_modes: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="defaultInputModes"),
        pydantic.Field(
            alias="defaultInputModes", description="Default media types accepted by this agent across all skills."
        ),
    ]
    """
    Default media types accepted by this agent across all skills.
    """

    default_output_modes: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="defaultOutputModes"),
        pydantic.Field(
            alias="defaultOutputModes", description="Default media types produced by this agent across all skills."
        ),
    ]
    """
    Default media types produced by this agent across all skills.
    """

    skills: typing.List[typing.Any] = pydantic.Field()
    """
    Skills the agent exposes. AAP defines 5 standard skill IDs (`dealer.information`, `inventory.facets`, `inventory.search`, `inventory.vehicle`, `lead.submit`); a compliant agent declares the subset it implements. Buyer agents MUST inspect `skills[]` to discover what is supported.
    """

    security_schemes: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="securitySchemes"),
        pydantic.Field(
            alias="securitySchemes",
            description="A2A security scheme definitions. AAP agents are public by default (no scheme).",
        ),
    ] = None
    """
    A2A security scheme definitions. AAP agents are public by default (no scheme).
    """

    security: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    Required security schemes (alternatives, by name). Empty or absent means anonymous access is allowed.
    """

    icon_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="iconUrl"), pydantic.Field(alias="iconUrl")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
