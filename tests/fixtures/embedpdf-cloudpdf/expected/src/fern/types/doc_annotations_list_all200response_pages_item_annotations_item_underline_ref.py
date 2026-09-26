

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRefIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_ref_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRefNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_ref_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRefObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRefObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRef_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRef_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
