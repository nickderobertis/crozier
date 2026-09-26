

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .agent_card_supported_interfaces_item_protocol_binding import AgentCardSupportedInterfacesItemProtocolBinding


class AgentCardSupportedInterfacesItem(UniversalBaseModel):
    url: str = pydantic.Field()
    """
    Endpoint URL for this interface.
    """

    protocol_binding: typing_extensions.Annotated[
        AgentCardSupportedInterfacesItemProtocolBinding,
        FieldMetadata(alias="protocolBinding"),
        pydantic.Field(alias="protocolBinding", description="The A2A transport binding available at this URL."),
    ]
    """
    The A2A transport binding available at this URL.
    """

    protocol_version: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="protocolVersion"),
        pydantic.Field(
            alias="protocolVersion",
            description="The A2A protocol version this interface exposes (Major.Minor), e.g. '1.0'.",
        ),
    ]
    """
    The A2A protocol version this interface exposes (Major.Minor), e.g. '1.0'.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
