

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_page_state_page import DocAnnotationsList200ResponsePageStatePage
from .doc_annotations_list200response_page_state_revision import DocAnnotationsList200ResponsePageStateRevision
from .doc_annotations_list200response_page_state_weak_annotation_state import (
    DocAnnotationsList200ResponsePageStateWeakAnnotationState,
)


class DocAnnotationsList200ResponsePageState(UniversalBaseModel):
    page: DocAnnotationsList200ResponsePageStatePage
    revision: DocAnnotationsList200ResponsePageStateRevision
    weak_annotation_state: typing_extensions.Annotated[
        DocAnnotationsList200ResponsePageStateWeakAnnotationState,
        FieldMetadata(alias="weakAnnotationState"),
        pydantic.Field(alias="weakAnnotationState"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
