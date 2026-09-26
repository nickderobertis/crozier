

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_versions_signatures200response_signatures_item_widget_ref_index_page import (
    DocVersionsSignatures200ResponseSignaturesItemWidgetRefIndexPage,
)
from .doc_versions_signatures200response_signatures_item_widget_ref_index_revision import (
    DocVersionsSignatures200ResponseSignaturesItemWidgetRefIndexRevision,
)
from .doc_versions_signatures200response_signatures_item_widget_ref_nm_page import (
    DocVersionsSignatures200ResponseSignaturesItemWidgetRefNmPage,
)
from .doc_versions_signatures200response_signatures_item_widget_ref_object_number_page import (
    DocVersionsSignatures200ResponseSignaturesItemWidgetRefObjectNumberPage,
)


class DocVersionsSignatures200ResponseSignaturesItemWidgetRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
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


class DocVersionsSignatures200ResponseSignaturesItemWidgetRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocVersionsSignatures200ResponseSignaturesItemWidgetRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocVersionsSignatures200ResponseSignaturesItemWidgetRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocVersionsSignatures200ResponseSignaturesItemWidgetRefIndexPage
    index: int
    revision: DocVersionsSignatures200ResponseSignaturesItemWidgetRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocVersionsSignatures200ResponseSignaturesItemWidgetRef = typing_extensions.Annotated[
    typing.Union[
        DocVersionsSignatures200ResponseSignaturesItemWidgetRef_ObjectNumber,
        DocVersionsSignatures200ResponseSignaturesItemWidgetRef_Nm,
        DocVersionsSignatures200ResponseSignaturesItemWidgetRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
