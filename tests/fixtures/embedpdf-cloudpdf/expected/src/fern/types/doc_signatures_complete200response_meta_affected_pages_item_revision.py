

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_signatures_complete200response_meta_affected_pages_item_revision_page import (
    DocSignaturesComplete200ResponseMetaAffectedPagesItemRevisionPage,
)


class DocSignaturesComplete200ResponseMetaAffectedPagesItemRevision(UniversalBaseModel):
    doc_session_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="docSessionId"), pydantic.Field(alias="docSessionId")
    ]
    page: DocSignaturesComplete200ResponseMetaAffectedPagesItemRevisionPage
    generation: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
