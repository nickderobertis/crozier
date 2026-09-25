

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .document_ground_truth_item_raw_value import DocumentGroundTruthItemRawValue
from .document_ground_truth_item_value import DocumentGroundTruthItemValue


class DocumentGroundTruthItem(UniversalBaseModel):
    pages: typing.Optional[typing.List[int]] = None
    raw_value: typing_extensions.Annotated[
        typing.Optional[DocumentGroundTruthItemRawValue],
        FieldMetadata(alias="rawValue"),
        pydantic.Field(alias="rawValue"),
    ] = None
    confidence: typing.Optional[float] = None
    label: str
    value: DocumentGroundTruthItemValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(DocumentGroundTruthItem)
