

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_polygon_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_polygon_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonRefIndexRevision,
)
from .doc_annotations_list200response_annotations_item_polygon_ref_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonRefNmPage,
)
from .doc_annotations_list200response_annotations_item_polygon_ref_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonRefObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemPolygonRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemPolygonRefObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemPolygonRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemPolygonRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemPolygonRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemPolygonRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemPolygonRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemPolygonRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemPolygonRef_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemPolygonRef_Nm,
        DocAnnotationsList200ResponseAnnotationsItemPolygonRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
