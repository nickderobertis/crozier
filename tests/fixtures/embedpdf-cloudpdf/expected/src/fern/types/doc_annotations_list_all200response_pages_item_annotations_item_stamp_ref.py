

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_stamp_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_stamp_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRefIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_stamp_ref_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRefNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_stamp_ref_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRefObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRefObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRef_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRef_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
