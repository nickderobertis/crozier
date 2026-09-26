

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_circle_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemCircleRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_circle_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemCircleRefIndexRevision,
)
from .doc_annotations_list200response_annotations_item_circle_ref_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemCircleRefNmPage,
)
from .doc_annotations_list200response_annotations_item_circle_ref_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemCircleRefObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemCircleRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemCircleRefObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemCircleRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemCircleRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemCircleRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemCircleRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemCircleRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemCircleRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemCircleRef_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemCircleRef_Nm,
        DocAnnotationsList200ResponseAnnotationsItemCircleRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
