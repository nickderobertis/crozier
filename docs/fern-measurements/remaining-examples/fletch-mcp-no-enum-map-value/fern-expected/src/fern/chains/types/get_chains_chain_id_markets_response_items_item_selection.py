

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_chains_chain_id_markets_response_items_item_selection_status import (
    GetChainsChainIdMarketsResponseItemsItemSelectionStatus,
)


class GetChainsChainIdMarketsResponseItemsItemSelection(UniversalBaseModel):
    """
    Recorded bounded universe comparison; expires after fifteen minutes. A stale selection withholds dominantAddress while retaining its explanation and observation time.
    """

    selected_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="selectedAt"), pydantic.Field(alias="selectedAt")
    ] = None
    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ] = None
    policy: str = pydantic.Field()
    """
    Versioned bounded selection: issuer listing, otherwise V3 quote holdings at least $10,000, otherwise V4 bounded 1% estimate at least $100. No issuer verification is inferred from economics.
    """

    status: GetChainsChainIdMarketsResponseItemsItemSelectionStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
