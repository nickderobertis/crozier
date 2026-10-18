

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .network_ban_response_enriched_output_banned_ipv4addresses_item import (
    NetworkBanResponseEnrichedOutputBannedIpv4AddressesItem,
)


class NetworkBanResponseEnrichedOutput(UniversalBaseModel):
    banned_ipv4addresses: typing_extensions.Annotated[
        typing.List[NetworkBanResponseEnrichedOutputBannedIpv4AddressesItem],
        FieldMetadata(alias="banned_ipv4_addresses"),
        pydantic.Field(alias="banned_ipv4_addresses"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
