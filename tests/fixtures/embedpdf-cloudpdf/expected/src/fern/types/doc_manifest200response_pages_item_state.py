

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_manifest200response_pages_item_state_page import DocManifest200ResponsePagesItemStatePage
from .doc_manifest200response_pages_item_state_revision import DocManifest200ResponsePagesItemStateRevision
from .doc_manifest200response_pages_item_state_weak_annotation_state import (
    DocManifest200ResponsePagesItemStateWeakAnnotationState,
)


class DocManifest200ResponsePagesItemState(UniversalBaseModel):
    page: DocManifest200ResponsePagesItemStatePage
    revision: DocManifest200ResponsePagesItemStateRevision
    weak_annotation_state: typing_extensions.Annotated[
        DocManifest200ResponsePagesItemStateWeakAnnotationState,
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
