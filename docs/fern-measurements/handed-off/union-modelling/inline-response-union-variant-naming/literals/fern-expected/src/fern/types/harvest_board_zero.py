

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .harvest_board_zero_ledger_version import HarvestBoardZeroLedgerVersion
from .harvest_board_zero_pending_reason import HarvestBoardZeroPendingReason


class HarvestBoardZero(UniversalBaseModel):
    pending: typing.Optional[str] = None
    pending_reason: typing_extensions.Annotated[
        typing.Optional[HarvestBoardZeroPendingReason],
        FieldMetadata(alias="pendingReason"),
        pydantic.Field(alias="pendingReason"),
    ] = None
    ledger_version: typing_extensions.Annotated[
        typing.Optional[HarvestBoardZeroLedgerVersion],
        FieldMetadata(alias="ledgerVersion"),
        pydantic.Field(alias="ledgerVersion"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
