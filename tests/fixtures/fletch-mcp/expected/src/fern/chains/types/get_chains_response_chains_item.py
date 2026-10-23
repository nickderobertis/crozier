

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_chains_response_chains_item_network import GetChainsResponseChainsItemNetwork


class GetChainsResponseChainsItem(UniversalBaseModel):
    chain_id: typing_extensions.Annotated[int, FieldMetadata(alias="chainId"), pydantic.Field(alias="chainId")]
    name: str
    network: GetChainsResponseChainsItemNetwork
    rpc_url: typing_extensions.Annotated[str, FieldMetadata(alias="rpcUrl"), pydantic.Field(alias="rpcUrl")]
    explorer_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="explorerUrl"), pydantic.Field(alias="explorerUrl")
    ]
    provider_configured: typing_extensions.Annotated[
        bool, FieldMetadata(alias="providerConfigured"), pydantic.Field(alias="providerConfigured")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
