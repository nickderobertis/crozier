

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_caret_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_caret_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRefIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_caret_ref_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRefNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_caret_ref_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRefObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRefObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRef_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRef_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
