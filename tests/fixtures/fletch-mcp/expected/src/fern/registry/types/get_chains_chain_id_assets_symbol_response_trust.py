

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_chains_chain_id_assets_symbol_response_trust_level import GetChainsChainIdAssetsSymbolResponseTrustLevel


class GetChainsChainIdAssetsSymbolResponseTrust(UniversalBaseModel):
    """
    Derived from the row: whether bytecode was found and the contract agrees with the listing.
    """

    level: typing.Optional[GetChainsChainIdAssetsSymbolResponseTrustLevel] = None
    label: typing.Optional[str] = None
    detail: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
