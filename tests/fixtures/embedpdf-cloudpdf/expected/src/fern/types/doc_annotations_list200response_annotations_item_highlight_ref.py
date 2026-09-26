

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_highlight_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_highlight_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightRefIndexRevision,
)
from .doc_annotations_list200response_annotations_item_highlight_ref_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightRefNmPage,
)
from .doc_annotations_list200response_annotations_item_highlight_ref_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightRefObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemHighlightRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemHighlightRefObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemHighlightRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemHighlightRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemHighlightRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemHighlightRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemHighlightRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemHighlightRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemHighlightRef_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemHighlightRef_Nm,
        DocAnnotationsList200ResponseAnnotationsItemHighlightRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
