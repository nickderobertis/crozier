

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .ground_truth_list_zero_item_raw_value import GroundTruthListZeroItemRawValue


class GroundTruthListZeroItem(UniversalBaseModel):
    confidence: typing.Optional[float] = None
    pages: typing.Optional[typing.List[int]] = None
    label: str
    raw_value: typing_extensions.Annotated[
        typing.Optional[GroundTruthListZeroItemRawValue],
        FieldMetadata(alias="rawValue"),
        pydantic.Field(alias="rawValue"),
    ] = None
    value: "GroundTruthListZeroItemValue"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .ground_truth_list import GroundTruthList
from .ground_truth_list_one_item_item import GroundTruthListOneItemItem
from .ground_truth_list_one_item_item_value import GroundTruthListOneItemItemValue
from .ground_truth_list_zero_item_value import GroundTruthListZeroItemValue

update_forward_refs(
    GroundTruthListZeroItem,
    GroundTruthList=GroundTruthList,
    GroundTruthListOneItemItem=GroundTruthListOneItemItem,
    GroundTruthListOneItemItemValue=GroundTruthListOneItemItemValue,
    GroundTruthListZeroItemValue=GroundTruthListZeroItemValue,
)
