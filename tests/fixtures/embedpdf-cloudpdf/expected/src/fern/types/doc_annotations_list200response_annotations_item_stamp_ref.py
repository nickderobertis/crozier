

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_stamp_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemStampRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_stamp_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemStampRefIndexRevision,
)
from .doc_annotations_list200response_annotations_item_stamp_ref_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemStampRefNmPage,
)
from .doc_annotations_list200response_annotations_item_stamp_ref_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemStampRefObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemStampRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemStampRefObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemStampRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemStampRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemStampRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemStampRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemStampRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemStampRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemStampRef_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemStampRef_Nm,
        DocAnnotationsList200ResponseAnnotationsItemStampRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
