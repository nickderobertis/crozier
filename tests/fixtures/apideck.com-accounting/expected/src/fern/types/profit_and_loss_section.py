

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class ProfitAndLossSection(UniversalBaseModel):
    id: typing.Optional[str] = None
    records: typing.Optional["ProfitAndLossRecords"] = None
    title: typing.Optional[str] = None
    total: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .profit_and_loss_records import ProfitAndLossRecords

update_forward_refs(ProfitAndLossSection)
