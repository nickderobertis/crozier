

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_widget_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_widget_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetRefIndexRevision,
)
from .doc_annotations_list200response_annotations_item_widget_ref_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetRefNmPage,
)
from .doc_annotations_list200response_annotations_item_widget_ref_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetRefObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemWidgetRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemWidgetRefObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemWidgetRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemWidgetRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemWidgetRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemWidgetRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemWidgetRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemWidgetRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemWidgetRef_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemWidgetRef_Nm,
        DocAnnotationsList200ResponseAnnotationsItemWidgetRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
