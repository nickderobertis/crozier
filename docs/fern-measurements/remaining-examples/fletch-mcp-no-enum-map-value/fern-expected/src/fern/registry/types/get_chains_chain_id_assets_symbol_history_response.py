

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_chains_chain_id_assets_symbol_history_response_coverage import (
    GetChainsChainIdAssetsSymbolHistoryResponseCoverage,
)


class GetChainsChainIdAssetsSymbolHistoryResponse(UniversalBaseModel):
    chain_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="chainId"), pydantic.Field(alias="chainId")
    ] = None
    symbol: typing.Optional[str] = None
    decimals: typing.Optional[int] = pydantic.Field(default=None)
    """
    Token decimals, for converting totalSupplyRaw
    """

    from_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="from"), pydantic.Field(alias="from")
    ] = None
    to: typing.Optional[str] = None
    coverage: typing.Optional[GetChainsChainIdAssetsSymbolHistoryResponseCoverage] = None
    days: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
