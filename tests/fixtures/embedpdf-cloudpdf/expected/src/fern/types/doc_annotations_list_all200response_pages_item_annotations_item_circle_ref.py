

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_circle_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_circle_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRefIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_circle_ref_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRefNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_circle_ref_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRefObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRefObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRef_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRef_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
