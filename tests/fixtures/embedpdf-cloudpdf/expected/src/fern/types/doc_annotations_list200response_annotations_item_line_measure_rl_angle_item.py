

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_line_measure_rl_angle_item_fraction import (
    DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlAngleItemFraction,
)
from .doc_annotations_list200response_annotations_item_line_measure_rl_angle_item_label_position import (
    DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlAngleItemLabelPosition,
)


class DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlAngleItem(UniversalBaseModel):
    unit: str
    conversion: typing.Optional[float] = None
    fraction: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlAngleItemFraction] = None
    precision: typing.Optional[int] = None
    fixed: typing.Optional[bool] = None
    thousands: typing.Optional[str] = None
    decimal: typing.Optional[str] = None
    prefix_spacing: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="prefixSpacing"), pydantic.Field(alias="prefixSpacing")
    ] = None
    suffix_spacing: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="suffixSpacing"), pydantic.Field(alias="suffixSpacing")
    ] = None
    label_position: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlAngleItemLabelPosition],
        FieldMetadata(alias="labelPosition"),
        pydantic.Field(alias="labelPosition"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
