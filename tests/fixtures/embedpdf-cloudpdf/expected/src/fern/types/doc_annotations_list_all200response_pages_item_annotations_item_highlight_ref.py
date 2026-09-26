

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_highlight_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_highlight_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRefIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_highlight_ref_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRefNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_highlight_ref_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRefObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRefObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRef_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRef_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
