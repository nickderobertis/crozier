

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItem,
)
from .doc_annotations_list_all200response_pages_item_page_state import (
    DocAnnotationsListAll200ResponsePagesItemPageState,
)


class DocAnnotationsListAll200ResponsePagesItem(UniversalBaseModel):
    page_state: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemPageState,
        FieldMetadata(alias="pageState"),
        pydantic.Field(alias="pageState"),
    ]
    annotations: typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
