

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_signatures_list200response_signatures_item_widget_page import (
    DocSignaturesList200ResponseSignaturesItemWidgetPage,
)
from .doc_signatures_list200response_signatures_item_widget_ref import (
    DocSignaturesList200ResponseSignaturesItemWidgetRef,
)


class DocSignaturesList200ResponseSignaturesItemWidget(UniversalBaseModel):
    ref: typing.Optional[DocSignaturesList200ResponseSignaturesItemWidgetRef] = None
    annot_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="annotObjectNumber"), pydantic.Field(alias="annotObjectNumber")
    ]
    page: typing.Optional[DocSignaturesList200ResponseSignaturesItemWidgetPage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
