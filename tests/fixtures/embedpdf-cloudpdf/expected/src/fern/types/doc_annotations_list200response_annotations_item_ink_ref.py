

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_ink_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemInkRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_ink_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemInkRefIndexRevision,
)
from .doc_annotations_list200response_annotations_item_ink_ref_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemInkRefNmPage,
)
from .doc_annotations_list200response_annotations_item_ink_ref_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemInkRefObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemInkRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemInkRefObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemInkRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemInkRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemInkRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemInkRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemInkRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemInkRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemInkRef_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemInkRef_Nm,
        DocAnnotationsList200ResponseAnnotationsItemInkRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
