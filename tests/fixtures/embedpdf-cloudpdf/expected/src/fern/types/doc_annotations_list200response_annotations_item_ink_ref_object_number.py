

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_ink_ref_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemInkRefObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemInkRefObjectNumber(UniversalBaseModel):
    page: DocAnnotationsList200ResponseAnnotationsItemInkRefObjectNumberPage
    annot_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="annotObjectNumber"), pydantic.Field(alias="annotObjectNumber")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
