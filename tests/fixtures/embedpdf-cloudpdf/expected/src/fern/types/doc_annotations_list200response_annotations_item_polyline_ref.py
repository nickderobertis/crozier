

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_polyline_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_polyline_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineRefIndexRevision,
)
from .doc_annotations_list200response_annotations_item_polyline_ref_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineRefNmPage,
)
from .doc_annotations_list200response_annotations_item_polyline_ref_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineRefObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemPolylineRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemPolylineRefObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemPolylineRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemPolylineRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemPolylineRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemPolylineRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemPolylineRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemPolylineRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemPolylineRef_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemPolylineRef_Nm,
        DocAnnotationsList200ResponseAnnotationsItemPolylineRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
