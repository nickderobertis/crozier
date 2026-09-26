

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_signatures_complete200response_signature_widget_page import (
    DocSignaturesComplete200ResponseSignatureWidgetPage,
)
from .doc_signatures_complete200response_signature_widget_ref import DocSignaturesComplete200ResponseSignatureWidgetRef


class DocSignaturesComplete200ResponseSignatureWidget(UniversalBaseModel):
    ref: typing.Optional[DocSignaturesComplete200ResponseSignatureWidgetRef] = None
    annot_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="annotObjectNumber"), pydantic.Field(alias="annotObjectNumber")
    ]
    page: typing.Optional[DocSignaturesComplete200ResponseSignatureWidgetPage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
