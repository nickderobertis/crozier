

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRefIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_ref_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRefNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_ref_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRefObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRefObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRef_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRef_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
