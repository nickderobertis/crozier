

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_strikeout_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_strikeout_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutRefIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_strikeout_ref_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutRefNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_strikeout_ref_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutRefObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutRefObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutRef_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutRef_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
