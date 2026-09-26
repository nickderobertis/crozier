

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_pages_insert200response_meta_affected_pages_item_revision_page_kind import (
    DocPagesInsert200ResponseMetaAffectedPagesItemRevisionPageKind,
)


class DocPagesInsert200ResponseMetaAffectedPagesItemRevisionPage(UniversalBaseModel):
    kind: DocPagesInsert200ResponseMetaAffectedPagesItemRevisionPageKind
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
