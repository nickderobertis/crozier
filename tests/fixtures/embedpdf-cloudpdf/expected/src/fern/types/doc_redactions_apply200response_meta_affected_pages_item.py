

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_redactions_apply200response_meta_affected_pages_item_page import (
    DocRedactionsApply200ResponseMetaAffectedPagesItemPage,
)
from .doc_redactions_apply200response_meta_affected_pages_item_revision import (
    DocRedactionsApply200ResponseMetaAffectedPagesItemRevision,
)
from .doc_redactions_apply200response_meta_affected_pages_item_weak_annotation_state import (
    DocRedactionsApply200ResponseMetaAffectedPagesItemWeakAnnotationState,
)


class DocRedactionsApply200ResponseMetaAffectedPagesItem(UniversalBaseModel):
    page: DocRedactionsApply200ResponseMetaAffectedPagesItemPage
    revision: DocRedactionsApply200ResponseMetaAffectedPagesItemRevision
    weak_annotation_state: typing_extensions.Annotated[
        DocRedactionsApply200ResponseMetaAffectedPagesItemWeakAnnotationState,
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
