

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_unsupported_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_unsupported_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedRefIndexRevision,
)
from .doc_annotations_list200response_annotations_item_unsupported_ref_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedRefNmPage,
)
from .doc_annotations_list200response_annotations_item_unsupported_ref_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedRefObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemUnsupportedRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemUnsupportedRefObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemUnsupportedRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemUnsupportedRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemUnsupportedRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemUnsupportedRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemUnsupportedRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemUnsupportedRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemUnsupportedRef_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemUnsupportedRef_Nm,
        DocAnnotationsList200ResponseAnnotationsItemUnsupportedRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
