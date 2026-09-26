

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_versions_signatures200response_signatures_item_widget_ref_object_number_page import (
    DocVersionsSignatures200ResponseSignaturesItemWidgetRefObjectNumberPage,
)


class DocVersionsSignatures200ResponseSignaturesItemWidgetRefObjectNumber(UniversalBaseModel):
    page: DocVersionsSignatures200ResponseSignaturesItemWidgetRefObjectNumberPage
    annot_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="annotObjectNumber"), pydantic.Field(alias="annotObjectNumber")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
