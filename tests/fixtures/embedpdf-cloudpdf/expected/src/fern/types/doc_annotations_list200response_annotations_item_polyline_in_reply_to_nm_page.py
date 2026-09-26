

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_polyline_in_reply_to_nm_page_kind import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineInReplyToNmPageKind,
)


class DocAnnotationsList200ResponseAnnotationsItemPolylineInReplyToNmPage(UniversalBaseModel):
    kind: DocAnnotationsList200ResponseAnnotationsItemPolylineInReplyToNmPageKind
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
