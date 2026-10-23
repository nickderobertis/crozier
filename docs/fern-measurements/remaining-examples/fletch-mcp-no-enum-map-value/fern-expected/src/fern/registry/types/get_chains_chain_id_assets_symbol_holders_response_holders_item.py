

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_chains_chain_id_assets_symbol_holders_response_holders_item_label_kind import (
    GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemLabelKind,
)
from .get_chains_chain_id_assets_symbol_holders_response_holders_item_sits import (
    GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemSits,
)


class GetChainsChainIdAssetsSymbolHoldersResponseHoldersItem(UniversalBaseModel):
    holder: typing.Optional[str] = None
    raw_balance: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="rawBalance"),
        pydantic.Field(alias="rawBalance", description="Base units; divide by 10^decimals"),
    ] = None
    """
    Base units; divide by 10^decimals
    """

    share_pct: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="sharePct"), pydantic.Field(alias="sharePct")
    ] = None
    as_of_block: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="asOfBlock"), pydantic.Field(alias="asOfBlock")
    ] = None
    label: typing.Optional[str] = None
    label_kind: typing_extensions.Annotated[
        typing.Optional[GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemLabelKind],
        FieldMetadata(alias="labelKind"),
        pydantic.Field(alias="labelKind"),
    ] = None
    sits: typing.Optional[GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemSits] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
