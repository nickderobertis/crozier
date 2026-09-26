

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_underline_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_underline_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineRefIndexRevision,
)
from .doc_annotations_list200response_annotations_item_underline_ref_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineRefNmPage,
)
from .doc_annotations_list200response_annotations_item_underline_ref_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineRefObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemUnderlineRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemUnderlineRefObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemUnderlineRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemUnderlineRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemUnderlineRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemUnderlineRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemUnderlineRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemUnderlineRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemUnderlineRef_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemUnderlineRef_Nm,
        DocAnnotationsList200ResponseAnnotationsItemUnderlineRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
