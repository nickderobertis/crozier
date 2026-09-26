

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_line_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRefIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_ref_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRefNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_ref_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRefObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRefObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRef_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRef_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
