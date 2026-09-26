

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_unsupported_ref_index_revision_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRefIndexRevisionPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRefIndexRevision(UniversalBaseModel):
    doc_session_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="docSessionId"), pydantic.Field(alias="docSessionId")
    ]
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRefIndexRevisionPage
    generation: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
