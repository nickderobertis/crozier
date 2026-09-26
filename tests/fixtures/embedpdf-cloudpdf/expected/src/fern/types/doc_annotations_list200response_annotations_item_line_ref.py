

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_line_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemLineRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_line_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemLineRefIndexRevision,
)
from .doc_annotations_list200response_annotations_item_line_ref_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemLineRefNmPage,
)
from .doc_annotations_list200response_annotations_item_line_ref_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemLineRefObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemLineRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemLineRefObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemLineRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemLineRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemLineRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemLineRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemLineRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemLineRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemLineRef_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemLineRef_Nm,
        DocAnnotationsList200ResponseAnnotationsItemLineRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
