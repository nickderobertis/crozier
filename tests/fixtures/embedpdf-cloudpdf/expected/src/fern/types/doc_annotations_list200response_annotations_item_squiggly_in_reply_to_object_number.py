

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_squiggly_in_reply_to_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyToObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyToObjectNumber(UniversalBaseModel):
    page: DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyToObjectNumberPage
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
