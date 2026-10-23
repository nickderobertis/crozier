

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_status_response_scouting_explorer import GetStatusResponseScoutingExplorer


class GetStatusResponseScouting(UniversalBaseModel):
    """
    Catalog ticker candidates, bytecode evidence and unfinished pool coverage. A ticker match does not establish Robinhood app contract identity.
    """

    measured_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="measuredAt"), pydantic.Field(alias="measuredAt")
    ]
    catalog_symbols: typing_extensions.Annotated[
        int, FieldMetadata(alias="catalogSymbols"), pydantic.Field(alias="catalogSymbols")
    ]
    matched_tickers: typing_extensions.Annotated[
        int, FieldMetadata(alias="matchedTickers"), pydantic.Field(alias="matchedTickers")
    ]
    bytecode_checked_tickers: typing_extensions.Annotated[
        int, FieldMetadata(alias="bytecodeCheckedTickers"), pydantic.Field(alias="bytecodeCheckedTickers")
    ]
    unmatched_symbols: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="unmatchedSymbols"), pydantic.Field(alias="unmatchedSymbols")
    ]
    pending_pool_tokens: typing_extensions.Annotated[
        int, FieldMetadata(alias="pendingPoolTokens"), pydantic.Field(alias="pendingPoolTokens")
    ]
    selected_pools: typing_extensions.Annotated[
        int, FieldMetadata(alias="selectedPools"), pydantic.Field(alias="selectedPools")
    ]
    complete_volume_pools: typing_extensions.Annotated[
        int, FieldMetadata(alias="completeVolumePools"), pydantic.Field(alias="completeVolumePools")
    ]
    explorer: typing.Optional[GetStatusResponseScoutingExplorer] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
