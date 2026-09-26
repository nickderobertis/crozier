

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item import DocAnnotationsList200ResponseAnnotationsItem
from .doc_annotations_list200response_page_state import DocAnnotationsList200ResponsePageState


class DocAnnotationsList200Response(UniversalBaseModel):
    page_state: typing_extensions.Annotated[
        DocAnnotationsList200ResponsePageState, FieldMetadata(alias="pageState"), pydantic.Field(alias="pageState")
    ]
    annotations: typing.List[DocAnnotationsList200ResponseAnnotationsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
