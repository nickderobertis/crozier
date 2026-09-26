

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_signatures_complete200response_meta_affected_pages_item_page import (
    DocSignaturesComplete200ResponseMetaAffectedPagesItemPage,
)
from .doc_signatures_complete200response_meta_affected_pages_item_revision import (
    DocSignaturesComplete200ResponseMetaAffectedPagesItemRevision,
)
from .doc_signatures_complete200response_meta_affected_pages_item_weak_annotation_state import (
    DocSignaturesComplete200ResponseMetaAffectedPagesItemWeakAnnotationState,
)


class DocSignaturesComplete200ResponseMetaAffectedPagesItem(UniversalBaseModel):
    page: DocSignaturesComplete200ResponseMetaAffectedPagesItemPage
    revision: DocSignaturesComplete200ResponseMetaAffectedPagesItemRevision
    weak_annotation_state: typing_extensions.Annotated[
        DocSignaturesComplete200ResponseMetaAffectedPagesItemWeakAnnotationState,
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
