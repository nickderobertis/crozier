

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_square_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_square_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRefIndexRevision,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_square_ref_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRefNmPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_square_ref_object_number_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRefObjectNumberPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRef_ObjectNumber(UniversalBaseModel):
    kind: typing.Literal["objectNumber"] = "objectNumber"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRefObjectNumberPage
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


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRef_Nm(UniversalBaseModel):
    kind: typing.Literal["nm"] = "nm"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRef_Index(UniversalBaseModel):
    kind: typing.Literal["index"] = "index"
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRef = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRef_ObjectNumber,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRef_Nm,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRef_Index,
    ],
    pydantic.Field(discriminator="kind"),
]
