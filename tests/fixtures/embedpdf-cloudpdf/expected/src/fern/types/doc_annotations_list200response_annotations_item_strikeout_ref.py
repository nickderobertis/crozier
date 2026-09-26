

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_strikeout_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_strikeout_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutRefIndexRevision,
)
from .doc_annotations_list200response_annotations_item_strikeout_ref_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutRefNmPage,
)
from .doc_annotations_list200response_annotations_item_strikeout_ref_object_number_page import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutRefObjectNumberPage,
)


class DocAnnotationsList200ResponseAnnotationsItemStrikeoutRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsList200ResponseAnnotationsItemStrikeoutRefObjectNumberPage
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


class DocAnnotationsList200ResponseAnnotationsItemStrikeoutRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsList200ResponseAnnotationsItemStrikeoutRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemStrikeoutRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsList200ResponseAnnotationsItemStrikeoutRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemStrikeoutRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemStrikeoutRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemStrikeoutRef_ObjectNumber,
        DocAnnotationsList200ResponseAnnotationsItemStrikeoutRef_Nm,
        DocAnnotationsList200ResponseAnnotationsItemStrikeoutRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
