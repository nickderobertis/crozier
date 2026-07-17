

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class ProfitAndLossRecordsItem_Section(UniversalBaseModel):
    type: typing.Literal["Section"] = "Section"
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


class ProfitAndLossRecordsItem_Record(UniversalBaseModel):
    type: typing.Literal["Record"] = "Record"
    id: typing.Optional[str] = None
    title: typing.Optional[str] = None
    value: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ProfitAndLossRecordsItem = typing_extensions.Annotated[
    typing.Union[ProfitAndLossRecordsItem_Section, ProfitAndLossRecordsItem_Record],
    pydantic.Field(discriminator="type"),
]
from .profit_and_loss_records import ProfitAndLossRecords

update_forward_refs(
    ProfitAndLossRecordsItem_Section,
    ProfitAndLossRecords=ProfitAndLossRecords,
    ProfitAndLossRecordsItem=ProfitAndLossRecordsItem,
)
