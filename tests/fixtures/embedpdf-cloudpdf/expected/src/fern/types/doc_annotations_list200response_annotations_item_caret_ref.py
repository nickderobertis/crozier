

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_caret_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemCaretRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_caret_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemCaretRefIndexRevision,
)
from .doc_annotations_list200response_annotations_item_caret_ref_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemCaretRefNmPage,
)
from .doc_annotations_list200response_annotations_item_caret_ref_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemCaretRefObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemCaretRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemCaretRefObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemCaretRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemCaretRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemCaretRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemCaretRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemCaretRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemCaretRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemCaretRef_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemCaretRef_Nm,
        DocAnnotationsList200ResponseAnnotationsItemCaretRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
