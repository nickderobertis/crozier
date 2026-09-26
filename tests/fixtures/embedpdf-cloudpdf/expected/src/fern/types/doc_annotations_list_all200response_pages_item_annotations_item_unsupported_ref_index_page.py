

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_unsupported_ref_index_page_kind import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRefIndexPageKind,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRefIndexPage(UniversalBaseModel):
    kind: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRefIndexPageKind
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
