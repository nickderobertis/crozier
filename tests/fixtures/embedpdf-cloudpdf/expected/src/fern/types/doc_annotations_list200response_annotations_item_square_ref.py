

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_square_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemSquareRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_square_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemSquareRefIndexRevision,
)
from .doc_annotations_list200response_annotations_item_square_ref_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemSquareRefNmPage,
)
from .doc_annotations_list200response_annotations_item_square_ref_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemSquareRefObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemSquareRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemSquareRefObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemSquareRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemSquareRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemSquareRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemSquareRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemSquareRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemSquareRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemSquareRef_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemSquareRef_Nm,
        DocAnnotationsList200ResponseAnnotationsItemSquareRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
