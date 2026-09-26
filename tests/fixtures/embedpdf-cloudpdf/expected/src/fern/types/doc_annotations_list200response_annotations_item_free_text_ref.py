

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_free_text_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_free_text_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRefIndexRevision,
)
from .doc_annotations_list200response_annotations_item_free_text_ref_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRefNmPage,
)
from .doc_annotations_list200response_annotations_item_free_text_ref_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRefObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemFreeTextRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemFreeTextRefObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemFreeTextRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemFreeTextRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemFreeTextRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemFreeTextRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemFreeTextRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemFreeTextRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemFreeTextRef_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemFreeTextRef_Nm,
        DocAnnotationsList200ResponseAnnotationsItemFreeTextRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
