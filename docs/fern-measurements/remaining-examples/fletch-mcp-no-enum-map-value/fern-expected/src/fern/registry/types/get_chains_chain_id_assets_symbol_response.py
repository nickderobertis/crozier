

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_chains_chain_id_assets_symbol_response_asset import GetChainsChainIdAssetsSymbolResponseAsset
from .get_chains_chain_id_assets_symbol_response_state import GetChainsChainIdAssetsSymbolResponseState
from .get_chains_chain_id_assets_symbol_response_trust import GetChainsChainIdAssetsSymbolResponseTrust


class GetChainsChainIdAssetsSymbolResponse(UniversalBaseModel):
    asset: typing.Optional[GetChainsChainIdAssetsSymbolResponseAsset] = None
    trust: typing.Optional[GetChainsChainIdAssetsSymbolResponseTrust] = pydantic.Field(default=None)
    """
    Derived from the row: whether bytecode was found and the contract agrees with the listing.
    """

    state: typing.Optional[GetChainsChainIdAssetsSymbolResponseState] = pydantic.Field(default=None)
    """
    The asset's live state as the registry daemon last read it; every sub-block carries the time it was read.
    """

    multiplier_history: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="multiplierHistory"),
        pydantic.Field(alias="multiplierHistory"),
    ] = None
    supply_events: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="supplyEvents"),
        pydantic.Field(alias="supplyEvents"),
    ] = None
    supply_snapshots: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="supplySnapshots"),
        pydantic.Field(alias="supplySnapshots"),
    ] = None
    corporate_actions: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="corporateActions"),
        pydantic.Field(alias="corporateActions"),
    ] = None
    control_events: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="controlEvents"),
        pydantic.Field(alias="controlEvents"),
    ] = None
    lookalikes: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    feed_rounds: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="feedRounds"),
        pydantic.Field(alias="feedRounds"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
