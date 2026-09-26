

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_versions_signatures200response_signatures_item_widget_page import (
    DocVersionsSignatures200ResponseSignaturesItemWidgetPage,
)
from .doc_versions_signatures200response_signatures_item_widget_ref import (
    DocVersionsSignatures200ResponseSignaturesItemWidgetRef,
)


class DocVersionsSignatures200ResponseSignaturesItemWidget(UniversalBaseModel):
    ref: typing.Optional[DocVersionsSignatures200ResponseSignaturesItemWidgetRef] = None
    annot_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="annotObjectNumber"), pydantic.Field(alias="annotObjectNumber")
    ]
    page: typing.Optional[DocVersionsSignatures200ResponseSignaturesItemWidgetPage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
