

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_file_attachment_page_kind import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentPageKind,
)


class DocAnnotationsList200ResponseAnnotationsItemFileAttachmentPage(UniversalBaseModel):
    kind: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentPageKind
    page_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="pageObjectNumber"), pydantic.Field(alias="pageObjectNumber")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
