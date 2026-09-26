

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_squiggly_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_squiggly_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyRefIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_squiggly_ref_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyRefNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_squiggly_ref_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyRefObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyRefObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyRef_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyRef_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
