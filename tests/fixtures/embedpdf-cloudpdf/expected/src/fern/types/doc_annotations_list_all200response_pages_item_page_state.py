

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_page_state_page import (
    DocAnnotationsListAll200ResponsePagesItemPageStatePage,
)
from .doc_annotations_list_all200response_pages_item_page_state_revision import (
    DocAnnotationsListAll200ResponsePagesItemPageStateRevision,
)
from .doc_annotations_list_all200response_pages_item_page_state_weak_annotation_state import (
    DocAnnotationsListAll200ResponsePagesItemPageStateWeakAnnotationState,
)


class DocAnnotationsListAll200ResponsePagesItemPageState(UniversalBaseModel):
    page: DocAnnotationsListAll200ResponsePagesItemPageStatePage
    revision: DocAnnotationsListAll200ResponsePagesItemPageStateRevision
    weak_annotation_state: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemPageStateWeakAnnotationState,
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
