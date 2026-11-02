

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .harvest_board_harvests_ledger_version import HarvestBoardHarvestsLedgerVersion
from .harvest_board_harvests_pending_reason import HarvestBoardHarvestsPendingReason
from .harvest_board_harvests_tallied_at import HarvestBoardHarvestsTalliedAt


class HarvestBoardHarvests(UniversalBaseModel):
    pending: typing.Optional[str] = None
    pending_reason: typing_extensions.Annotated[
        typing.Optional[HarvestBoardHarvestsPendingReason],
        FieldMetadata(alias="pendingReason"),
        pydantic.Field(alias="pendingReason"),
    ] = None
    ledger_version: typing_extensions.Annotated[
        typing.Optional[HarvestBoardHarvestsLedgerVersion],
        FieldMetadata(alias="ledgerVersion"),
        pydantic.Field(alias="ledgerVersion"),
    ] = None
    tallied_at: typing_extensions.Annotated[
        typing.Optional[HarvestBoardHarvestsTalliedAt],
        FieldMetadata(alias="talliedAt"),
        pydantic.Field(alias="talliedAt"),
    ] = None
    harvests: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
