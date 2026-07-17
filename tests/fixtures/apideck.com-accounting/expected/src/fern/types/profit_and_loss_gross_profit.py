

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class ProfitAndLossGrossProfit(UniversalBaseModel):
    records: typing.Optional["ProfitAndLossRecords"] = None
    total: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total gross profit
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .profit_and_loss_records import ProfitAndLossRecords
from .profit_and_loss_records_item import ProfitAndLossRecordsItem
from .profit_and_loss_section import ProfitAndLossSection

update_forward_refs(
    ProfitAndLossGrossProfit,
    ProfitAndLossRecords=ProfitAndLossRecords,
    ProfitAndLossRecordsItem=ProfitAndLossRecordsItem,
    ProfitAndLossSection=ProfitAndLossSection,
)
