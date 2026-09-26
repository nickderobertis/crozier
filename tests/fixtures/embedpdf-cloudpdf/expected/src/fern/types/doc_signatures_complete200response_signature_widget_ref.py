

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_signatures_complete200response_signature_widget_ref_index_page import (
    DocSignaturesComplete200ResponseSignatureWidgetRefIndexPage,
)
from .doc_signatures_complete200response_signature_widget_ref_index_revision import (
    DocSignaturesComplete200ResponseSignatureWidgetRefIndexRevision,
)
from .doc_signatures_complete200response_signature_widget_ref_nm_page import (
    DocSignaturesComplete200ResponseSignatureWidgetRefNmPage,
)
from .doc_signatures_complete200response_signature_widget_ref_object_number_page import (
    DocSignaturesComplete200ResponseSignatureWidgetRefObjectNumberPage,
)


class DocSignaturesComplete200ResponseSignatureWidgetRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocSignaturesComplete200ResponseSignatureWidgetRefObjectNumberPage
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


class DocSignaturesComplete200ResponseSignatureWidgetRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocSignaturesComplete200ResponseSignatureWidgetRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocSignaturesComplete200ResponseSignatureWidgetRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocSignaturesComplete200ResponseSignatureWidgetRefIndexPage
    index: int
    revision: DocSignaturesComplete200ResponseSignatureWidgetRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocSignaturesComplete200ResponseSignatureWidgetRef = typing_extensions.Annotated[
    typing.Union[
        DocSignaturesComplete200ResponseSignatureWidgetRef_ObjectNumber,
        DocSignaturesComplete200ResponseSignatureWidgetRef_Nm,
        DocSignaturesComplete200ResponseSignatureWidgetRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
