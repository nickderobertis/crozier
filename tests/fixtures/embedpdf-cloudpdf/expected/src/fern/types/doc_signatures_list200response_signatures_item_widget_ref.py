

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_signatures_list200response_signatures_item_widget_ref_index_page import (
    DocSignaturesList200ResponseSignaturesItemWidgetRefIndexPage,
)
from .doc_signatures_list200response_signatures_item_widget_ref_index_revision import (
    DocSignaturesList200ResponseSignaturesItemWidgetRefIndexRevision,
)
from .doc_signatures_list200response_signatures_item_widget_ref_nm_page import (
    DocSignaturesList200ResponseSignaturesItemWidgetRefNmPage,
)
from .doc_signatures_list200response_signatures_item_widget_ref_object_number_page import (
    DocSignaturesList200ResponseSignaturesItemWidgetRefObjectNumberPage,
)


class DocSignaturesList200ResponseSignaturesItemWidgetRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocSignaturesList200ResponseSignaturesItemWidgetRefObjectNumberPage
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


class DocSignaturesList200ResponseSignaturesItemWidgetRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocSignaturesList200ResponseSignaturesItemWidgetRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocSignaturesList200ResponseSignaturesItemWidgetRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocSignaturesList200ResponseSignaturesItemWidgetRefIndexPage
    index: int
    revision: DocSignaturesList200ResponseSignaturesItemWidgetRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocSignaturesList200ResponseSignaturesItemWidgetRef = typing_extensions.Annotated[
    typing.Union[
        DocSignaturesList200ResponseSignaturesItemWidgetRef_ObjectNumber,
        DocSignaturesList200ResponseSignaturesItemWidgetRef_Nm,
        DocSignaturesList200ResponseSignaturesItemWidgetRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
