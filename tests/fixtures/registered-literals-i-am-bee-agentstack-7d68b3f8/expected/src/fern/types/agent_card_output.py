

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .agent_capabilities import AgentCapabilities
from .agent_card_signature import AgentCardSignature
from .agent_interface import AgentInterface
from .agent_provider import AgentProvider
from .agent_skill import AgentSkill
from .security_scheme_output import SecuritySchemeOutput


class AgentCardOutput(UniversalBaseModel):
    """
    The AgentCard is a self-describing manifest for an agent. It provides essential
    metadata including the agent's identity, capabilities, skills, supported
    communication methods, and security requirements.
    """

    additional_interfaces: typing_extensions.Annotated[
        typing.Optional[typing.List[AgentInterface]],
        FieldMetadata(alias="additionalInterfaces"),
        pydantic.Field(alias="additionalInterfaces"),
    ] = None
    capabilities: AgentCapabilities
    default_input_modes: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="defaultInputModes"), pydantic.Field(alias="defaultInputModes")
    ]
    default_output_modes: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="defaultOutputModes"), pydantic.Field(alias="defaultOutputModes")
    ]
    description: str
    documentation_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="documentationUrl"), pydantic.Field(alias="documentationUrl")
    ] = None
    icon_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="iconUrl"), pydantic.Field(alias="iconUrl")
    ] = None
    name: str
    preferred_transport: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="preferredTransport"), pydantic.Field(alias="preferredTransport")
    ] = None
    protocol_version: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="protocolVersion"), pydantic.Field(alias="protocolVersion")
    ] = None
    provider: typing.Optional[AgentProvider] = None
    security: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]] = None
    security_schemes: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[SecuritySchemeOutput]]],
        FieldMetadata(alias="securitySchemes"),
        pydantic.Field(alias="securitySchemes"),
    ] = None
    signatures: typing.Optional[typing.List[AgentCardSignature]] = None
    skills: typing.List[AgentSkill]
    supports_authenticated_extended_card: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="supportsAuthenticatedExtendedCard"),
        pydantic.Field(alias="supportsAuthenticatedExtendedCard"),
    ] = None
    url: str
    version: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
